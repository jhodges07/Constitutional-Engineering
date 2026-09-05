#!/usr/bin/env python3
"""
CWC-CE-161 — render Bill A phone-first public-review PDFs (pandoc + XeLaTeX).

Reproducible: prepare Markdown → pandoc → XeLaTeX → PDF.
Does not modify Definition source documents.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]  # Constitutional-Engineering
PUB = Path(__file__).resolve().parents[1]  # …/bill-a/public-review
RENDERER = Path(__file__).resolve().parent
PDF_DIR = PUB / "pdf"
BUILD = RENDERER / "_build"

CANONICAL_SHA = "9e96c1b96ed46e28ac9515065d9331fd78b62bcf"
LOU_SRC = ROOT / "Engineering-Office/definition/LOU-004-Bill-A-Comprehensive-Kansas-Tax-System-Replacement.md"
SUM_SRC = ROOT / "Engineering-Office/definition/working/bill-a/WD-BILL-A-113-LOU-004-Human-Review-Summary.md"

LOU_PDF_NAME = "Bill-A-LOU-004-Public-Review-Draft-1.10.pdf"
SUM_PDF_NAME = "Bill-A-LOU-004-Review-Summary.pdf"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def verify_source_state() -> None:
    head = subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
    origin = subprocess.check_output(
        ["git", "-C", str(ROOT), "rev-parse", "origin/main"], text=True
    ).strip()
    if head != CANONICAL_SHA or origin != CANONICAL_SHA:
        raise SystemExit(
            f"STOP: source state mismatch. expected={CANONICAL_SHA} HEAD={head} origin/main={origin}"
        )
    if not LOU_SRC.is_file() or not SUM_SRC.is_file():
        raise SystemExit("STOP: source Markdown missing")
    # Confirm blobs exist at expected SHA
    for rel in (
        "Engineering-Office/definition/LOU-004-Bill-A-Comprehensive-Kansas-Tax-System-Replacement.md",
        "Engineering-Office/definition/working/bill-a/WD-BILL-A-113-LOU-004-Human-Review-Summary.md",
    ):
        subprocess.check_call(["git", "-C", str(ROOT), "cat-file", "-e", f"{CANONICAL_SHA}:{rel}"])
    print(f"source-state: PASS ({CANONICAL_SHA})")


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print(">>", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(cwd) if cwd else None)


def prepare(kind: str, source: Path, out_md: Path) -> None:
    run(
        [
            sys.executable,
            str(RENDERER / "prepare_phone_first_md.py"),
            "--kind",
            kind,
            "--source",
            str(source),
            "--out",
            str(out_md),
        ]
    )


def pandoc_pdf(prepared_md: Path, out_pdf: Path, *, footer_right: str, title: str, subject: str, keywords: str) -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)
    header = RENDERER / "phone-first-header.tex"
    # XeLaTeX + auto package install on MiKTeX
    env = os.environ.copy()
    env["MIKTEX_AUTOINSTALL"] = "1"
    cmd = [
        "pandoc",
        str(prepared_md),
        "-f",
        "markdown+raw_tex+pipe_tables+grid_tables+fenced_code_blocks+strikeout+task_lists",
        "-t",
        "pdf",
        "--pdf-engine=xelatex",
        "--toc",
        "--toc-depth=2",
        "-V",
        "documentclass=article",
        "-V",
        "fontsize=11pt",
        "-V",
        f"PhoneFooterRight={footer_right}",
        "-V",
        f"title={title}",
        "-V",
        f"CJKmainfont=",  # no-op safety
        "--include-in-header",
        str(header),
        "-M",
        f"title={title}",
        "-M",
        "author=Constitutional Engineering Office / BlueprintLiberty",
        "-M",
        f"subject={subject}",
        "-M",
        f"keywords={keywords}",
        "-M",
        f"source-git-sha={CANONICAL_SHA}",
        "-M",
        "review-status=PUBLIC REVIEW CANDIDATE — NOT HUMAN-ACCEPTED",
        "-o",
        str(out_pdf),
    ]
    print(">>", " ".join(cmd))
    subprocess.check_call(cmd, env=env, cwd=str(BUILD))


def main() -> int:
    verify_source_state()
    BUILD.mkdir(parents=True, exist_ok=True)

    lou_md = BUILD / "lou-004-prepared.md"
    sum_md = BUILD / "wd-bill-a-113-prepared.md"
    prepare("lou", LOU_SRC, lou_md)
    prepare("summary", SUM_SRC, sum_md)

    lou_pdf = PDF_DIR / LOU_PDF_NAME
    sum_pdf = PDF_DIR / SUM_PDF_NAME

    pandoc_pdf(
        lou_md,
        lou_pdf,
        footer_right="LOU-004 Draft 1.10 | Public Review Candidate",
        title="Bill A LOU-004 Public Review Draft 1.10",
        subject="Public-review PDF derived from LOU-004 Draft 1.10 — NOT HUMAN-ACCEPTED",
        keywords="Bill A, LOU-004, Draft 1.10, Public Review Candidate, NOT HUMAN-ACCEPTED, HG-D1 NOT PASSED",
    )
    pandoc_pdf(
        sum_md,
        sum_pdf,
        footer_right="WD-BILL-A-113 | Summary ≠ LOU-004",
        title="Bill A LOU-004 Human Review Summary",
        subject="Informational review summary WD-BILL-A-113 — does not replace LOU-004",
        keywords="Bill A, WD-BILL-A-113, Review Summary, does not replace LOU-004, NOT HUMAN-ACCEPTED",
    )

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    identity = {
        "cwc": "CWC-CE-161",
        "canonical_git_sha": CANONICAL_SHA,
        "render_timestamp_utc": stamp,
        "toolchain": "pandoc + XeLaTeX + prepare_phone_first_md.py",
        "page_size": "6in x 9in portrait",
        "artifacts": [],
    }
    for path, src in ((lou_pdf, str(LOU_SRC.relative_to(ROOT))), (sum_pdf, str(SUM_SRC.relative_to(ROOT)))):
        # page count via pymupdf if available
        page_count = None
        try:
            import fitz  # type: ignore

            doc = fitz.open(path)
            page_count = doc.page_count
            doc.close()
        except Exception:
            page_count = None
        identity["artifacts"].append(
            {
                "filename": path.name,
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "source_markdown": src.replace("\\", "/"),
                "source_git_sha": CANONICAL_SHA,
                "pdf_sha256": sha256_file(path),
                "file_size_bytes": path.stat().st_size,
                "page_count": page_count,
            }
        )
        print(path.name, "SHA-256", identity["artifacts"][-1]["pdf_sha256"], "pages", page_count)

    out_id = PUB / "validation" / "CWC-CE-161-ARTIFACT-IDENTITY.json"
    out_id.write_text(json.dumps(identity, indent=2) + "\n", encoding="utf-8")
    print("wrote", out_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
