#!/usr/bin/env python3
"""Local correlation tests for KSB-089-D02 remediation (CWC-CE-090). No live Issues."""

from __future__ import annotations

import re
import sys
from pathlib import Path

_BRIDGE_ROOT = Path(__file__).resolve().parents[1]
_REPO_ROOT = _BRIDGE_ROOT.parents[3]
if str(_BRIDGE_ROOT) not in sys.path:
    sys.path.insert(0, str(_BRIDGE_ROOT))

from ksb_issue_bridge.correlate import (
    CorrelateError,
    assert_correlation_fields,
    build_gh_issue_argv,
    build_success_correlation_comment,
    resolve_trusted_repository,
)

WF = _REPO_ROOT / ".github" / "workflows" / "ksb-render-bridge.yml"


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def main() -> int:
    # Trusted repo resolution
    repo = resolve_trusted_repository(github_repository="jhodges07/Constitutional-Engineering")
    check("trusted_repo", repo == "jhodges07/Constitutional-Engineering")

    try:
        resolve_trusted_repository(github_repository="")
        check("reject_empty_repo", False)
    except CorrelateError:
        check("reject_empty_repo", True)

    try:
        resolve_trusted_repository(
            github_repository="jhodges07/Constitutional-Engineering",
            payload_repository="evil/other",
        )
        check("reject_payload_repo_substitution", False)
    except CorrelateError as exc:
        check("reject_payload_repo_substitution", True, str(exc))

    # Same trusted value in payload is allowed (no substitution)
    same = resolve_trusted_repository(
        github_repository="jhodges07/Constitutional-Engineering",
        payload_repository="jhodges07/Constitutional-Engineering",
    )
    check("allow_matching_payload_repo", same == "jhodges07/Constitutional-Engineering")

    argv = build_gh_issue_argv(
        subcommand=["comment"],
        repository="jhodges07/Constitutional-Engineering",
        issue_number=3,
        extra=["--body", "test"],
    )
    check(
        "explicit_repo_flag",
        argv[:6] == ["gh", "issue", "comment", "-R", "jhodges07/Constitutional-Engineering", "3"],
        " ".join(argv),
    )
    check("no_cwd_dependency_in_argv", "-R" in argv and argv[argv.index("-R") + 1].count("/") == 1)

    body = build_success_correlation_comment(
        request_id="KSB-RENDER-2026-08-30-002",
        run_id="33334671439",
        canonical_sha="91e74163eee82f0fca36acab7aae22f963caf2af",
        artifact_name="ksb-render-KSB-RENDER-2026-08-30-002",
        run_url="https://github.com/jhodges07/Constitutional-Engineering/actions/runs/33334671439",
    )
    for token in (
        "request_id=KSB-RENDER-2026-08-30-002",
        "run_id=33334671439",
        "artifact_name=ksb-render-KSB-RENDER-2026-08-30-002",
        "canonical_sha=91e74163eee82f0fca36acab7aae22f963caf2af",
    ):
        check(f"comment_contains_{token.split('=')[0]}", token in body)

    assert_correlation_fields(
        request={
            "request_id": "KSB-RENDER-2026-08-30-002",
            "canonical_sha": "91e74163eee82f0fca36acab7aae22f963caf2af",
        },
        issue_number=3,
        run_id=33334671439,
        artifact_name="ksb-render-KSB-RENDER-2026-08-30-002",
    )
    check("correlation_fields_ok", True)

    try:
        assert_correlation_fields(
            request={
                "request_id": "KSB-RENDER-2026-08-30-002",
                "canonical_sha": "91e74163eee82f0fca36acab7aae22f963caf2af",
            },
            issue_number=3,
            run_id=33334671439,
            artifact_name="ksb-render-WRONG",
        )
        check("reject_bad_artifact_name", False)
    except CorrelateError:
        check("reject_bad_artifact_name", True)

    # Workflow must use explicit -R github.repository (not bare gh issue …)
    text = WF.read_text(encoding="utf-8")
    check("workflow_exists", WF.is_file())
    correlate_hits = len(re.findall(r"gh issue comment -R \"\$\{\{ github\.repository \}\}\"", text))
    # PowerShell form uses $repo variable after assignment from github.repository
    has_pwsh_repo = '$repo = "${{ github.repository }}"' in text and "gh issue comment -R $repo" in text
    has_bash_repo = 'gh issue comment -R "${{ github.repository }}"' in text
    check("workflow_explicit_repo_targeting", has_pwsh_repo and has_bash_repo, f"pwsh={has_pwsh_repo} bash={has_bash_repo}")
    # No bare comment without -R remaining in correlate/reject (except comments in docs)
    bare = re.findall(r"gh issue comment \"\$\{\{ github\.event\.issue\.number \}\}\"", text)
    check("no_bare_issue_comment_without_repo", len(bare) == 0, str(bare))
    bare_close = re.findall(r'gh issue close "\$\{\{ github\.event\.issue\.number \}\}"', text)
    check("no_bare_issue_close_without_repo", len(bare_close) == 0, str(bare_close))

    print("\ncorrelation tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
