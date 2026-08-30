"""Fence-safe KSB Issue body construction (CWC-CE-102 / KSB-RENDER-004).

PowerShell treats backtick (U+0060) as an escape character. Embedding the
literal triple-backtick + ksb-render-request opening fence inside a
PowerShell-invoked python -c double-quoted string collapses that fence to a
single backtick (CWC-CE-101 / Issue #7).

This module builds and validates Issue bodies in Python using only
string constants from ksb_issue_bridge.constants (no shell interpolation).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from ksb_issue_bridge.constants import BODY_FENCE_END, BODY_FENCE_START
from ksb_issue_bridge.gate import (
    GateReject,
    build_issue_body,
    extract_request_json,
    validate_envelope,
)


def opening_fence_line() -> str:
    """Exact opening fence line required by the canonical parser."""
    return BODY_FENCE_START


def closing_fence_line() -> str:
    """Exact closing fence line required by the canonical parser."""
    return BODY_FENCE_END


def assert_literal_fences(body: str) -> None:
    """Fail if opening/closing fences are not exact triple-backtick markers."""
    if BODY_FENCE_START not in body:
        raise ValueError(
            f"opening fence missing: expected {BODY_FENCE_START!r} "
            f"(len={len(BODY_FENCE_START)}; backtick_count="
            f"{BODY_FENCE_START.count(chr(96))})"
        )
    # Opening must be exactly three backticks + identifier
    if not BODY_FENCE_START.startswith(chr(96) * 3):
        raise ValueError("BODY_FENCE_START constant corrupted")
    if BODY_FENCE_START.count(chr(96)) != 3:
        raise ValueError(
            f"BODY_FENCE_START must contain exactly 3 backticks, got "
            f"{BODY_FENCE_START.count(chr(96))}"
        )
    # After opening fence there must be a newline before JSON (parser contract)
    idx = body.find(BODY_FENCE_START)
    after = body[idx + len(BODY_FENCE_START) : idx + len(BODY_FENCE_START) + 1]
    if after != "\n":
        raise ValueError(
            f"newline required immediately after opening fence; got {after!r}"
        )
    # Closing fence: first ``` after JSON start
    json_start = idx + len(BODY_FENCE_START) + 1
    end = body.find(BODY_FENCE_END, json_start)
    if end < 0:
        raise ValueError("closing triple-backtick fence missing")
    if body[end : end + 3] != chr(96) * 3:
        raise ValueError("closing fence is not three literal backticks")


def write_issue_body_file(
    request: Mapping[str, Any],
    path: Path | str,
    *,
    preface: str | None = None,
) -> Path:
    """Write a UTF-8 Issue body via build_issue_body (fence-safe).

    preface: optional text before the fenced block (must not contain the
    opening fence identifier alone in a way that confuses the parser; prefer
    plain prose). Default matches build_issue_body preface.
    """
    path = Path(path)
    if preface is None:
        body = build_issue_body(request)
    else:
        body = (
            preface.rstrip()
            + "\n\n"
            + BODY_FENCE_START
            + "\n"
            + json.dumps(dict(request), indent=2)
            + "\n"
            + BODY_FENCE_END
            + "\n"
        )
    assert_literal_fences(body)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8", newline="\n")
    # Round-trip readback
    roundtrip = path.read_text(encoding="utf-8")
    if roundtrip != body and roundtrip.replace("\r\n", "\n") != body:
        raise RuntimeError("round-trip body mismatch after write")
    assert_literal_fences(roundtrip.replace("\r\n", "\n"))
    return path


def pre_submit_validate(
    body: str,
    *,
    allowed_shas: list[str] | frozenset[str],
) -> dict[str, Any]:
    """Mandatory pre-submission check: fence → JSON → envelope.

    Returns extracted request dict on success; raises GateReject on failure.
    """
    assert_literal_fences(body)
    data = extract_request_json(body)
    validate_envelope(data, allowed_shas=allowed_shas)
    return data


def gh_issue_create_argv(
    *,
    repo: str,
    title: str,
    body_file: Path | str,
) -> list[str]:
    """Exact safe GitHub CLI argv — body via --body-file only (no PS interpolation)."""
    return [
        "gh",
        "issue",
        "create",
        "-R",
        repo,
        "--title",
        title,
        "--body-file",
        str(Path(body_file)),
    ]


def powershell_corruption_demo(intended_triple_fence_fragment: str) -> str:
    """Document what PowerShell does to backticks in double-quoted contexts.

    This is not used for production construction. For tests only.
    """
    # Simulate PowerShell escape: `X → X for most chars; `` → `
    # Triple ``` in PS double-quotes becomes ` (one backtick) when each
    # ` escapes the next character.
    out: list[str] = []
    i = 0
    s = intended_triple_fence_fragment
    while i < len(s):
        if s[i] == "`" and i + 1 < len(s):
            out.append(s[i + 1])
            i += 2
        else:
            out.append(s[i])
            i += 1
    return "".join(out)
