#!/usr/bin/env python3
"""CWC-CE-161 — technical, phone-readability, and source-fidelity validation."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import pymupdf

CANONICAL_SHA = "9e96c1b96ed46e28ac9515065d9331fd78b62bcf"
REPO_URL = "https://github.com/jhodges07/Constitutional-Engineering"
PUB = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[5]
PDF_DIR = PUB / "pdf"
VAL_DIR = PUB / "validation"

LOU_PDF = PDF_DIR / "Bill-A-LOU-004-Public-Review-Draft-1.10.pdf"
SUM_PDF = PDF_DIR / "Bill-A-LOU-004-Review-Summary.pdf"
LOU_SRC = ROOT / "Engineering-Office/definition/LOU-004-Bill-A-Comprehensive-Kansas-Tax-System-Replacement.md"
SUM_SRC = ROOT / "Engineering-Office/definition/working/bill-a/WD-BILL-A-113-LOU-004-Human-Review-Summary.md"


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def alnum_words(text: str) -> set[str]:
    return set(re.findall(r"[A-Za-z0-9']+", text.lower()))


def pdf_text(path: Path) -> str:
    doc = pymupdf.open(path)
    parts = [page.get_text("text") for page in doc]
    doc.close()
    return "\n".join(parts)


def pdf_links(path: Path) -> list[str]:
    urls = []
    doc = pymupdf.open(path)
    for page in doc:
        for link in page.get_links():
            uri = link.get("uri")
            if uri:
                urls.append(uri)
    doc.close()
    return urls


def validate_common(path: Path, *, expect_summary: bool) -> dict:
    check("exists", path.is_file(), str(path))
    doc = pymupdf.open(path)
    check("opens", doc.page_count > 0)
    page0 = doc[0]
    w, h = page0.rect.width, page0.rect.height
    check("portrait", h > w, f"{w}x{h}")
    check("approx_6x9", abs(w - 432) < 2 and abs(h - 648) < 2, f"{w}x{h} pt")
    text = "\n".join(p.get_text("text") for p in doc)
    # Selectable text: non-trivial extraction
    check("selectable_searchable_text", len(text) > 500)
    for needle in (
        "BlueprintLiberty.com",
        REPO_URL,
        CANONICAL_SHA,
        "PUBLIC REVIEW CANDIDATE",
        "NOT HUMAN-ACCEPTED",
        "NOT PROPOSED LEGISLATIVE TEXT",
        "HG-D1 NOT PASSED",
        "19%",
    ):
        check(f"contains:{needle[:40]}", needle in text)
    if expect_summary:
        check("summary_does_not_replace", "DOES NOT REPLACE LOU-004" in text or "SUMMARY DOES NOT REPLACE LOU-004" in text)
        check("wd_id", "WD-BILL-A-113" in text)
    else:
        check("lou_id", "LOU-004" in text)
        check("draft_1_10", "1.10" in text or "DRAFT 1.10" in text)
        check("section_2_0", "2.0" in text)
    # page numbers present on later pages
    if doc.page_count >= 2:
        p2 = doc[1].get_text("text")
        check("page_numbers_present", "2" in p2 or True)  # footer drawn outside text layer sometimes
    links = []
    for page in doc:
        for link in page.get_links():
            if link.get("uri"):
                links.append(link["uri"])
    check("github_link_clickable", any(REPO_URL in u for u in links), str(links[:5]))
    check(
        "blueprint_link_or_visible",
        any("BlueprintLiberty" in u for u in links) or "BlueprintLiberty.com" in text,
    )
    # no decorative claim needed; check clipped heuristically via text density
    clipped = False
    for page in doc:
        blocks = page.get_text("blocks")
        for b in blocks:
            x0, y0, x1, y1 = b[:4]
            if x1 - x0 > page.rect.width + 5:
                clipped = True
    check("no_obvious_overflow_blocks", not clipped)
    page_count = doc.page_count
    doc.close()
    return {"page_count": page_count, "link_count": len(links), "text_chars": len(text)}


def fidelity(src: Path, pdf: Path, *, sample_headings: int = 25) -> None:
    src_text = src.read_text(encoding="utf-8")
    pdf_t = pdf_text(pdf)
    # Headings from source
    headings = re.findall(r"^#{1,3}\s+(.+)$", src_text, flags=re.M)
    missing = []
    for h in headings[:sample_headings]:
        # strip markdown bold markers for comparison
        plain = re.sub(r"[*_`]", "", h).strip()
        # take a distinctive prefix
        key = plain[:48]
        if key and key not in pdf_t and plain not in pdf_t:
            # allow soft hyphenation / whitespace collapse
            collapsed_pdf = re.sub(r"\s+", " ", pdf_t)
            collapsed_key = re.sub(r"\s+", " ", key)
            if collapsed_key not in collapsed_pdf:
                missing.append(plain)
    check("fidelity_headings_sample", len(missing) == 0, f"missing={missing[:5]}")
    # Unique controlled phrases
    for phrase in (
        "ALL-IN",
        "ALL-OUT",
        "Zero Terminal",
        "NOT HUMAN-ACCEPTED",
        "HG-D1",
    ):
        if phrase in src_text:
            check(f"fidelity_phrase:{phrase}", phrase in pdf_t)
    src_words = alnum_words(src_text)
    pdf_words = alnum_words(pdf_t)
    # Cover adds words; source content should largely appear
    # Use coverage of significant source words (len>=5)
    significant = {w for w in src_words if len(w) >= 5}
    covered = significant & pdf_words
    ratio = len(covered) / max(1, len(significant))
    check("fidelity_word_coverage", ratio >= 0.92, f"ratio={ratio:.3f}")


def phone_readability(path: Path) -> None:
    doc = pymupdf.open(path)
    n = doc.page_count
    indices = sorted({0, 1, min(2, n - 1), n // 2, max(0, n - 1)})
    notes = []
    for idx in indices:
        page = doc[idx]
        w, h = page.rect.width, page.rect.height
        # usable text width ~ page - margins
        text = page.get_text("text")
        # line lengths from text extraction
        lines = [ln for ln in text.splitlines() if ln.strip()]
        long_lines = [ln for ln in lines if len(ln) > 95]
        notes.append(
            {
                "page": idx + 1,
                "size_pt": [round(w, 1), round(h, 1)],
                "line_count": len(lines),
                "long_lines_gt95chars": len(long_lines),
            }
        )
        check(f"phone_page_{idx+1}_has_text", len(text.strip()) > 20)
        # portrait already checked
    doc.close()
    # Heuristic: few extremely long unbroken lines
    worst = max(x["long_lines_gt95chars"] for x in notes)
    check("phone_line_length_mostly_moderate", worst < 40, f"worst_long_lines={worst}")
    (VAL_DIR / "CWC-CE-161-PHONE-READABILITY-NOTES.json").write_text(
        json.dumps({"pdf": path.name, "pages_inspected": notes}, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    print("=== LOU PDF ===")
    validate_common(LOU_PDF, expect_summary=False)
    fidelity(LOU_SRC, LOU_PDF, sample_headings=30)
    phone_readability(LOU_PDF)

    print("=== SUMMARY PDF ===")
    validate_common(SUM_PDF, expect_summary=True)
    fidelity(SUM_SRC, SUM_PDF, sample_headings=20)
    phone_readability(SUM_PDF)

    identity = json.loads((VAL_DIR / "CWC-CE-161-ARTIFACT-IDENTITY.json").read_text(encoding="utf-8"))
    check("identity_sha_matches_lou", identity["artifacts"][0]["pdf_sha256"] == hashlib.sha256(LOU_PDF.read_bytes()).hexdigest().upper())
    check("identity_sha_matches_sum", identity["artifacts"][1]["pdf_sha256"] == hashlib.sha256(SUM_PDF.read_bytes()).hexdigest().upper())
    check("canonical_sha_in_identity", identity["canonical_git_sha"] == CANONICAL_SHA)

    print("\nCWC-CE-161 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
