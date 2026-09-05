#!/usr/bin/env python3
"""
CWC-CE-161 — phone-first Markdown prepare for public-review PDF rendering.

Formatting-only transforms:
  - prepend cover / document-control / review disclaimer
  - reformat wide Markdown tables into stacked Field/Value blocks for narrow pages

Does NOT rewrite Human Intent or substantive LOU content.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

CANONICAL_SHA = "9e96c1b96ed46e28ac9515065d9331fd78b62bcf"
REPO_URL = "https://github.com/jhodges07/Constitutional-Engineering"
PROJECT_URL = "BlueprintLiberty.com"


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def is_separator_row(cells: list[str]) -> bool:
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) is not None for c in cells if c != "")


def reformat_tables(md: str) -> str:
    """Convert multi-column / wide tables to stacked definition-style blocks."""
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        if not lines[i].strip().startswith("|"):
            out.append(lines[i])
            i += 1
            continue
        block: list[str] = []
        j = i
        while j < len(lines) and lines[j].strip().startswith("|"):
            block.append(lines[j])
            j += 1
        if len(block) < 2:
            out.extend(block)
            i = j
            continue
        header = split_table_row(block[0])
        sep = split_table_row(block[1])
        if not is_separator_row(sep):
            out.extend(block)
            i = j
            continue
        data_rows = [split_table_row(r) for r in block[2:]]
        # Keep compact 2-col short tables as tables when likely readable.
        max_cell = max((len(c) for row in ([header] + data_rows) for c in row), default=0)
        wide = len(header) >= 3 or max_cell > 42 or any(len(row) > 2 for row in data_rows)
        if not wide and len(header) == 2:
            out.extend(block)
            i = j
            continue
        out.append("")
        out.append("*[Table reformatted for phone-first readability — cell text unchanged]*")
        out.append("")
        for n, row in enumerate(data_rows, start=1):
            # Pad/truncate to header width without inventing content
            cells = list(row) + [""] * max(0, len(header) - len(row))
            cells = cells[: len(header)]
            out.append(f"**Table row {n}**")
            out.append("")
            for h, c in zip(header, cells):
                hh = h if h else "Field"
                out.append(f"- **{hh}:** {c}")
            out.append("")
        i = j
    return "\n".join(out)


def cover_lou() -> str:
    return f"""---
title: "Bill A — LOU-004 Public Review"
author: "Constitutional Engineering Office"
---

\\thispagestyle{{plain}}

\\begin{{center}}
{{\\LARGE\\bfseries BILL A}}\\\\[0.6em]
{{\\Large\\bfseries COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT}}\\\\[1.0em]
{{\\large LETTER OF UNDERSTANDING}}\\\\[0.4em]
{{\\LARGE\\bfseries LOU-004}}\\\\[0.5em]
{{\\large DRAFT 1.10}}\\\\[1.0em]
\\CoverRule
{{\\large\\bfseries PUBLIC REVIEW CANDIDATE}}\\\\[0.45em]
{{\\bfseries NOT HUMAN-ACCEPTED}}\\\\[0.35em]
{{\\bfseries NOT PROPOSED LEGISLATIVE TEXT}}\\\\[0.35em]
{{\\bfseries HG-D1 NOT PASSED}}
\\end{{center}}

\\vspace{{1.0em}}

**Project URL:** [{PROJECT_URL}](https://BlueprintLiberty.com)

**Canonical repository:** [{REPO_URL}]({REPO_URL})

\\vspace{{0.6em}}

### Document-control block

| Field | Value |
|---|---|
| Document | LOU-004 |
| Bill | Bill A — Comprehensive Kansas Tax-System Replacement |
| Draft | 1.10 |
| Review status | PUBLIC REVIEW CANDIDATE |
| Human acceptance | NOT HUMAN-ACCEPTED |
| HG-D1 | NOT PASSED |
| Bill A maturity | 19% UNCHANGED |
| Canonical repository | Constitutional-Engineering |
| Canonical Git SHA | `{CANONICAL_SHA}` |
| Repository URL | {REPO_URL} |
| Project URL | {PROJECT_URL} |

\\vspace{{0.5em}}

### External-review notice

```text
THIS DOCUMENT IS PROVIDED FOR PUBLIC REVIEW AND COMMENT.

IT IS NOT ENACTED LAW.

IT IS NOT PROPOSED LEGISLATIVE TEXT.

LOU-004 HAS NOT YET BEEN HUMAN-ACCEPTED.

HG-D1 HAS NOT PASSED.

COMMENTS AND PROPOSALS FROM REVIEWERS DO NOT AUTOMATICALLY ALTER THE CONTROLLED LOU.

THE HUMAN ENGINEER RETAINS FINAL AUTHORITY OVER HUMAN INTENT.
```

Reviewers are invited to examine architecture for ambiguity, missing considerations, unintended consequences, internal contradictions, unclear taxpayer or government effects, transition concerns, constitutional/legal research questions, implementation concerns, and disagreements with Human Intent. Reviewer comments remain external review evidence until classified through a later controlled process.

\\newpage

"""


def cover_summary() -> str:
    return f"""---
title: "Bill A — LOU-004 Human Review Summary"
author: "Constitutional Engineering Office"
---

\\thispagestyle{{plain}}

\\begin{{center}}
{{\\LARGE\\bfseries BILL A}}\\\\[0.6em]
{{\\Large\\bfseries COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT}}\\\\[1.0em]
{{\\large HUMAN REVIEW SUMMARY}}\\\\[0.35em]
{{\\normalsize WD-BILL-A-113}}\\\\[1.0em]
\\CoverRule
{{\\large\\bfseries PUBLIC REVIEW CANDIDATE}}\\\\[0.45em]
{{\\bfseries SUMMARY DOES NOT REPLACE LOU-004}}\\\\[0.35em]
{{\\bfseries NOT HUMAN-ACCEPTED}}\\\\[0.35em]
{{\\bfseries NOT PROPOSED LEGISLATIVE TEXT}}\\\\[0.35em]
{{\\bfseries HG-D1 NOT PASSED}}
\\end{{center}}

\\vspace{{1.0em}}

**Project URL:** [{PROJECT_URL}](https://BlueprintLiberty.com)

**Canonical repository:** [{REPO_URL}]({REPO_URL})

\\vspace{{0.6em}}

### Document-control block

| Field | Value |
|---|---|
| Document | WD-BILL-A-113 |
| Bill | Bill A — Comprehensive Kansas Tax-System Replacement |
| Governing LOU | LOU-004 Draft 1.10 |
| Review status | PUBLIC REVIEW CANDIDATE |
| Human acceptance | NOT HUMAN-ACCEPTED |
| HG-D1 | NOT PASSED |
| Bill A maturity | 19% UNCHANGED |
| Role | INFORMATIONAL SUMMARY — DOES NOT REPLACE LOU-004 |
| Canonical repository | Constitutional-Engineering |
| Canonical Git SHA | `{CANONICAL_SHA}` |
| Repository URL | {REPO_URL} |
| Project URL | {PROJECT_URL} |

\\vspace{{0.5em}}

### External-review notice

```text
THIS DOCUMENT IS PROVIDED FOR PUBLIC REVIEW AND COMMENT.

IT IS NOT ENACTED LAW.

IT IS NOT PROPOSED LEGISLATIVE TEXT.

LOU-004 HAS NOT YET BEEN HUMAN-ACCEPTED.

HG-D1 HAS NOT PASSED.

THIS SUMMARY DOES NOT REPLACE LOU-004.

COMMENTS AND PROPOSALS FROM REVIEWERS DO NOT AUTOMATICALLY ALTER THE CONTROLLED LOU.

THE HUMAN ENGINEER RETAINS FINAL AUTHORITY OVER HUMAN INTENT.
```

Serious reviewers should read the complete LOU-004, especially **§2.0**. This summary is a phone-readable orientation map only.

\\newpage

"""


def prepare(kind: str, source: Path, dest: Path) -> None:
    body = source.read_text(encoding="utf-8")
    body = reformat_tables(body)
    if kind == "lou":
        front = cover_lou()
    elif kind == "summary":
        front = cover_summary()
    else:
        raise SystemExit(f"unknown kind: {kind}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(front + body, encoding="utf-8")
    print(f"prepared: {dest}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", choices=("lou", "summary"), required=True)
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    prepare(args.kind, args.source, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
