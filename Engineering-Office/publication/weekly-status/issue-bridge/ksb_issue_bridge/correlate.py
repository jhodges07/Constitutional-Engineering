"""Issue correlation helpers — explicit repository targeting (CWC-CE-090 / KSB-089-D02).

Repository identity MUST come from trusted Actions context (GITHUB_REPOSITORY),
never from untrusted Issue payload fields.
"""

from __future__ import annotations

from typing import Mapping, Optional, Sequence


class CorrelateError(ValueError):
    """Fail-closed correlation argument construction."""


def resolve_trusted_repository(
    *,
    github_repository: Optional[str],
    payload_repository: Optional[str] = None,
) -> str:
    """Return OWNER/REPO from trusted env; reject payload substitution attempts."""
    trusted = (github_repository or "").strip()
    if not trusted or "/" not in trusted or trusted.count("/") != 1:
        raise CorrelateError("trusted GITHUB_REPOSITORY missing or malformed")
    owner, name = trusted.split("/", 1)
    if not owner or not name or ".." in trusted or trusted.startswith("/"):
        raise CorrelateError("trusted GITHUB_REPOSITORY invalid")
    if payload_repository is not None:
        candidate = str(payload_repository).strip()
        if candidate and candidate != trusted:
            raise CorrelateError(
                "unauthorized repository substitution from Issue payload rejected"
            )
    return trusted


def build_gh_issue_argv(
    *,
    subcommand: Sequence[str],
    repository: str,
    issue_number: int,
    extra: Optional[Sequence[str]] = None,
) -> list[str]:
    """Build `gh issue … -R OWNER/REPO <n> …` argv (no cwd/git inference)."""
    if not isinstance(issue_number, int) or issue_number < 1:
        raise CorrelateError("issue_number must be a positive integer")
    repo = resolve_trusted_repository(github_repository=repository)
    argv = ["gh", "issue", *subcommand, "-R", repo, str(issue_number)]
    if extra:
        argv.extend(extra)
    return argv


def build_success_correlation_comment(
    *,
    request_id: str,
    run_id: str,
    canonical_sha: str,
    artifact_name: str,
    run_url: str,
    runner: str = "windows-2022",
) -> str:
    """Issue comment body per KSB-ISSUE-BRIDGE-001 SUCCESS lifecycle."""
    return "\n".join(
        [
            "KSB render EXECUTION RESULT (non-canonical artifact; NON-PRODUCTION POC).",
            f"request_id={request_id}",
            f"run_id={run_id}",
            f"canonical_sha={canonical_sha}",
            f"artifact_name={artifact_name}",
            f"runner={runner}",
            f"run_url={run_url}",
            "STOP before publication. Temporary artifact ≠ canonical weekly image.",
        ]
    )


def assert_correlation_fields(
    *,
    request: Mapping[str, object],
    issue_number: int,
    run_id: int,
    artifact_name: str,
) -> None:
    """Fail closed if correlation identities are incomplete."""
    for key in ("request_id", "canonical_sha"):
        if not request.get(key):
            raise CorrelateError(f"missing correlation field: {key}")
    if issue_number < 1:
        raise CorrelateError("invalid issue_number")
    if run_id < 1:
        raise CorrelateError("invalid run_id")
    expected = f"ksb-render-{request['request_id']}"
    if artifact_name != expected:
        raise CorrelateError(
            f"artifact_name mismatch: got={artifact_name} expected={expected}"
        )
