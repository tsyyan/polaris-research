"""Build and scan a fail-closed Polaris public release candidate.

This command only creates local files. It never creates a repository, invokes a
network API, changes repository visibility, commits, or pushes.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlparse


ALLOWLIST_PATH = Path("docs/operations/PUBLIC_RELEASE_ALLOWLIST.md")
DEFAULT_OUTPUT = Path("build/public_release_candidate")
DEFAULT_MANIFEST = Path("PUBLIC_RELEASE_CANDIDATE_MANIFEST.json")

TEXT_SUFFIXES = {
    ".cfg", ".css", ".csv", ".html", ".ini", ".js", ".json", ".md",
    ".py", ".rst", ".toml", ".ts", ".txt", ".yaml", ".yml",
}
SECRET_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "aws_access_key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "github_token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "generic_credential": re.compile(
        r"(?i)\b(?:api[_-]?key|secret|token|password)\b\s*[:=]\s*[\"']?([^\"'\s]{8,})"
    ),
}
ABSOLUTE_PATH_PATTERNS = {
    "windows_absolute_path": re.compile(r"(?<![A-Za-z0-9])(?:[A-Za-z]:\\|[A-Za-z]:/)[^\s\"'<>]+"),
    "posix_home_path": re.compile(r"(?<![A-Za-z0-9])/(?:home|Users|root|var/tmp)/[^\s\"'<>]+"),
    "file_url": re.compile(r"(?i)\bfile://[^\s\"'<>]+"),
}
URL_PATTERN = re.compile(r"https?://[^\s<>()\]\"']+")
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PRIVATE_HOST_SUFFIXES = (".internal", ".local", ".localhost", ".corp", ".lan")
INTERNAL_REFERENCE_PATTERNS = {
    "private_runtime_state": re.compile(r"(?i)(?:^|[/\\])\.noesis(?:[/\\]|$)"),
    "private_memory_path": re.compile(r"(?i)(?:^|[/\\])memory/(?:context|agents)(?:/|$)"),
    "private_source_path": re.compile(r"(?i)\bC:\\NOESIS\b"),
}
# These policy files must name prohibited classes in order to document them.
POLICY_REFERENCE_EXEMPTIONS = {
    "docs/operations/PUBLIC_PRIVATE_REPOSITORY_SEPARATION_PROPOSAL.md",
    "docs/operations/PUBLIC_RELEASE_ALLOWLIST.md",
}


class ReleaseError(RuntimeError):
    """A fail-closed release preparation error."""


def _git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout.strip()


def load_allowlist(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"```json public-release-allowlist\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise ReleaseError(f"machine-readable allowlist block missing: {path}")
    data = json.loads(match.group(1))
    if data.get("schema_version") != 1:
        raise ReleaseError("unsupported allowlist schema_version")
    if not data.get("include") or not isinstance(data.get("exclude"), list):
        raise ReleaseError("allowlist must contain non-empty include and exclude lists")
    return data


def _matches(path: str, pattern: str) -> bool:
    if pattern.endswith("/**"):
        prefix = pattern[:-3].rstrip("/")
        return path == prefix or path.startswith(prefix + "/")
    return fnmatch.fnmatchcase(path, pattern)


def resolve_allowed_files(repo: Path, allowlist: dict[str, Any]) -> list[str]:
    all_files = [
        path.relative_to(repo).as_posix()
        for path in repo.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(repo).parts
    ]
    selected: set[str] = set()
    missing: list[str] = []
    for pattern in allowlist["include"]:
        matches = [path for path in all_files if _matches(path, pattern)]
        if not matches:
            missing.append(pattern)
        selected.update(matches)
    if missing:
        raise ReleaseError(f"allowlist entries matched no files: {missing}")

    excluded = {
        path
        for path in selected
        if any(_matches(path, pattern) for pattern in allowlist["exclude"])
    }
    if excluded:
        raise ReleaseError(f"include/exclude conflict: {sorted(excluded)}")
    forbidden = [path for path in selected if ".git" in PurePosixPath(path).parts]
    if forbidden:
        raise ReleaseError(f"Git metadata selected: {forbidden}")
    return sorted(selected)


def clean_output(repo: Path, output: Path) -> None:
    resolved_repo = repo.resolve()
    resolved_output = output.resolve()
    if resolved_output == resolved_repo or resolved_repo not in resolved_output.parents:
        raise ReleaseError("output must be a child directory of the repository")
    if output.exists():
        if output.is_symlink():
            raise ReleaseError("refusing to clean a symlinked output path")
        shutil.rmtree(output)
    output.mkdir(parents=True)


def copy_files(repo: Path, output: Path, files: list[str]) -> None:
    for relative in files:
        source = repo / relative
        if source.is_symlink():
            raise ReleaseError(f"symlinks are not allowed in the public candidate: {relative}")
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _is_private_host(hostname: str | None) -> bool:
    if not hostname:
        return True
    host = hostname.lower().rstrip(".")
    if host in {"localhost", "127.0.0.1", "::1"} or host.endswith(PRIVATE_HOST_SUFFIXES):
        return True
    if re.fullmatch(r"10(?:\.\d{1,3}){3}", host):
        return True
    if re.fullmatch(r"192\.168(?:\.\d{1,3}){2}", host):
        return True
    match = re.fullmatch(r"172\.(\d{1,3})(?:\.\d{1,3}){2}", host)
    return bool(match and 16 <= int(match.group(1)) <= 31)


def _scan_markdown_links(relative: str, path: Path, text: str, output: Path) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for match in MARKDOWN_LINK_PATTERN.finditer(text):
        raw_target = match.group(1).strip()
        target = raw_target.split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target_path = target.split("#", 1)[0].split("?", 1)[0]
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(output.resolve())
        except ValueError:
            exists = False
        else:
            exists = resolved.exists()
        if not exists:
            findings.append(
                {
                    "category": "broken_link",
                    "rule": "missing_local_target",
                    "file": relative,
                    "line": _line_number(text, match.start()),
                    "value": target,
                }
            )
    return findings


def scan_candidate(output: Path, files: list[str]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    scanned = 0
    for relative in files:
        path = output / relative
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {".gitignore", ".gitattributes"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append({"category": "content", "rule": "non_utf8_text", "file": relative})
            continue
        scanned += 1
        for rule, pattern in SECRET_PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append(
                    {"category": "secrets", "rule": rule, "file": relative, "line": _line_number(text, match.start())}
                )
        for rule, pattern in ABSOLUTE_PATH_PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append(
                    {
                        "category": "absolute_paths",
                        "rule": rule,
                        "file": relative,
                        "line": _line_number(text, match.start()),
                        "value": match.group(0),
                    }
                )
        for match in URL_PATTERN.finditer(text):
            value = match.group(0).rstrip(".,;:")
            if _is_private_host(urlparse(value).hostname):
                findings.append(
                    {
                        "category": "private_urls",
                        "rule": "private_or_local_host",
                        "file": relative,
                        "line": _line_number(text, match.start()),
                        "value": value,
                    }
                )
        if relative not in POLICY_REFERENCE_EXEMPTIONS:
            for rule, pattern in INTERNAL_REFERENCE_PATTERNS.items():
                for match in pattern.finditer(text):
                    findings.append(
                        {
                            "category": "internal_references",
                            "rule": rule,
                            "file": relative,
                            "line": _line_number(text, match.start()),
                            "value": match.group(0),
                        }
                    )
        if path.suffix.lower() == ".md":
            findings.extend(_scan_markdown_links(relative, path, text, output))

    by_category = {
        category: sum(1 for finding in findings if finding["category"] == category)
        for category in ("secrets", "absolute_paths", "private_urls", "internal_references", "broken_link", "content")
    }
    return {
        "status": "pass" if not findings else "fail",
        "text_files_scanned": scanned,
        "finding_count": len(findings),
        "findings_by_category": by_category,
        "findings": findings,
        "policy_reference_exemptions": sorted(POLICY_REFERENCE_EXEMPTIONS),
    }


def file_record(path: Path, relative: str) -> dict[str, Any]:
    content = path.read_bytes()
    return {"path": relative, "size": len(content), "sha256": hashlib.sha256(content).hexdigest()}


def build_manifest(
    repo: Path,
    output: Path,
    manifest_path: Path,
    allowlist: dict[str, Any],
    files: list[str],
    scan: dict[str, Any],
) -> dict[str, Any]:
    source_commit = _git(repo, "rev-parse", "HEAD")
    source_status = _git(repo, "status", "--porcelain", "--untracked-files=all")
    records = [file_record(output / relative, relative) for relative in files]
    tree_digest_input = "".join(f"{record['sha256']}  {record['path']}\n" for record in records).encode()
    manifest = {
        "schema_version": 1,
        "candidate_status": "awaiting_human_approval" if scan["status"] == "pass" else "scan_failed",
        "publication_authorized": False,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": {
            "commit": source_commit,
            "worktree_clean": not bool(source_status),
            "note": (
                "Candidate includes the current allowlisted working-tree bytes; "
                "review hashes, not the commit alone, when the worktree is not clean."
            ),
        },
        "candidate": {
            "directory": output.relative_to(repo).as_posix(),
            "file_count": len(records),
            "tree_sha256": hashlib.sha256(tree_digest_input).hexdigest(),
            "files": records,
        },
        "exclusions": [
            {"pattern": pattern, "reason": "Excluded by the approved disclosure boundary."}
            for pattern in allowlist["exclude"]
        ],
        "scan": scan,
        "human_approval": {
            "status": "pending",
            "required_before": [
                "create_public_github_repository",
                "push_candidate",
                "add_public_url_to_outreach",
            ],
            "license_and_redistribution_review_required": True,
            "approved_by": None,
            "approved_at": None,
            "destination": None,
        },
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = Path(__file__).resolve().parents[1]
    os.chdir(repo)
    output = (repo / args.output).resolve() if not args.output.is_absolute() else args.output.resolve()
    manifest_path = (repo / args.manifest).resolve() if not args.manifest.is_absolute() else args.manifest.resolve()
    try:
        manifest_path.relative_to(repo)
    except ValueError as exc:
        raise ReleaseError("manifest must be written inside the repository") from exc

    allowlist = load_allowlist(repo / ALLOWLIST_PATH)
    files = resolve_allowed_files(repo, allowlist)
    clean_output(repo, output)
    copy_files(repo, output, files)
    scan = scan_candidate(output, files)
    manifest = build_manifest(repo, output, manifest_path, allowlist, files, scan)
    print(
        json.dumps(
            {
                "candidate_status": manifest["candidate_status"],
                "output": str(output),
                "manifest": str(manifest_path),
                "files": len(files),
                "findings": scan["finding_count"],
            },
            indent=2,
        )
    )
    return 0 if scan["status"] == "pass" else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ReleaseError, OSError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(f"public release candidate build failed: {exc}", file=sys.stderr)
        sys.exit(2)
