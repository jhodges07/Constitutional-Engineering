#!/usr/bin/env python3
"""
CWC-CE-161 — deterministic phone-first public-review PDF renderer (ReportLab).

Page: 6in × 9in portrait. Selectable/searchable text. Clickable URLs.
Formatting-only transforms (wide tables → stacked Field/Value). No Human Intent rewrite.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
)

CANONICAL_SHA = "9e96c1b96ed46e28ac9515065d9331fd78b62bcf"
REPO_URL = "https://github.com/jhodges07/Constitutional-Engineering"
PROJECT_URL_DISPLAY = "BlueprintLiberty.com"
PROJECT_URL_HREF = "https://BlueprintLiberty.com"

PAGE_W = 6 * inch
PAGE_H = 9 * inch
MARGIN = 0.55 * inch


def repo_root() -> Path:
    return Path(__file__).resolve().parents[5]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def verify_source_state(root: Path) -> None:
    head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    origin = subprocess.check_output(
        ["git", "-C", str(root), "rev-parse", "origin/main"], text=True
    ).strip()
    if head != CANONICAL_SHA or origin != CANONICAL_SHA:
        raise SystemExit(
            f"STOP: source state mismatch. expected={CANONICAL_SHA} HEAD={head} origin/main={origin}"
        )


def escape_xml(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def inline_md(text: str) -> str:
    """Convert limited Markdown inline markup to ReportLab rich text."""
    s = escape_xml(text)
    # Links [label](url)
    s = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+|https://BlueprintLiberty\.com|BlueprintLiberty\.com)\)",
        lambda m: f'<link href="{escape_xml(m.group(2) if m.group(2).startswith("http") else "https://" + m.group(2))}" color="blue"><u>{m.group(1)}</u></link>',
        s,
    )
    # Autolink bare https URLs
    s = re.sub(
        r"(?<![\"'>])(https://[^\s<>\]]+)",
        lambda m: f'<link href="{escape_xml(m.group(1))}" color="blue"><u>{escape_xml(m.group(1))}</u></link>',
        s,
    )
    # Bold **...**
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    # Italic *...* (simple)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    # Inline code `...`
    s = re.sub(r"`([^`]+)`", r'<font face="Courier" size="9">\1</font>', s)
    return s


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


def build_styles():
    base = getSampleStyleSheet()
    styles = {
        "CoverTitle": ParagraphStyle(
            "CoverTitle",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "CoverSub": ParagraphStyle(
            "CoverSub",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=16,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "CoverWarn": ParagraphStyle(
            "CoverWarn",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "H1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            spaceBefore=14,
            spaceAfter=8,
            textColor=colors.black,
        ),
        "H2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            spaceBefore=11,
            spaceAfter=6,
        ),
        "H3": ParagraphStyle(
            "H3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            spaceBefore=9,
            spaceAfter=5,
        ),
        "Body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14.5,
            alignment=TA_JUSTIFY,
            spaceBefore=2,
            spaceAfter=6,
        ),
        "Bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14.5,
            leftIndent=12,
            spaceBefore=1,
            spaceAfter=3,
        ),
        "Meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            spaceBefore=1,
            spaceAfter=3,
        ),
        "Code": ParagraphStyle(
            "Code",
            parent=base["Code"],
            fontName="Courier",
            fontSize=8.5,
            leading=11,
            backColor=colors.Color(0.96, 0.96, 0.96),
            spaceBefore=6,
            spaceAfter=8,
        ),
        "Center": ParagraphStyle(
            "Center",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "SmallCenter": ParagraphStyle(
            "SmallCenter",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            spaceAfter=3,
        ),
    }
    return styles


class NumberedCanvas(Canvas):
    def __init__(self, *args, footer_right: str = "", **kwargs):
        self._footer_right = footer_right
        Canvas.__init__(self, *args, **kwargs)

    def showPage(self):
        self._draw_footer()
        Canvas.showPage(self)

    def save(self):
        self._draw_footer()
        Canvas.save(self)

    def _draw_footer(self):
        self.saveState()
        self.setStrokeColor(colors.grey)
        self.setLineWidth(0.4)
        y = 0.38 * inch
        self.line(MARGIN, y + 10, PAGE_W - MARGIN, y + 10)
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.black)
        self.drawString(MARGIN, y, "BlueprintLiberty.com")
        page = self._pageNumber
        label = str(page)
        self.drawCentredString(PAGE_W / 2, y, label)
        right = self._footer_right
        self.drawRightString(PAGE_W - MARGIN, y, right[:48])
        self.restoreState()


def control_table(rows: list[tuple[str, str]], styles) -> Table:
    data = [
        [
            Paragraph(f"<b>{escape_xml(k)}</b>", styles["Meta"]),
            Paragraph(inline_md(v) if not v.startswith("http") else f'<link href="{escape_xml(v)}" color="blue"><u>{escape_xml(v)}</u></link>', styles["Meta"]),
        ]
        for k, v in rows
    ]
    # Special-case SHA and URLs already handled; for SHA keep monospace-ish
    col_w = [1.55 * inch, PAGE_W - 2 * MARGIN - 1.55 * inch]
    t = Table(data, colWidths=col_w, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.5, colors.grey),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("BACKGROUND", (0, 0), (0, -1), colors.Color(0.95, 0.95, 0.95)),
            ]
        )
    )
    return t


def cover_flowables(kind: str, styles) -> list:
    notice = """THIS DOCUMENT IS PROVIDED FOR PUBLIC REVIEW AND COMMENT.

IT IS NOT ENACTED LAW.

IT IS NOT PROPOSED LEGISLATIVE TEXT.

LOU-004 HAS NOT YET BEEN HUMAN-ACCEPTED.

HG-D1 HAS NOT PASSED.

COMMENTS AND PROPOSALS FROM REVIEWERS DO NOT AUTOMATICALLY ALTER THE CONTROLLED LOU.

THE HUMAN ENGINEER RETAINS FINAL AUTHORITY OVER HUMAN INTENT."""
    if kind == "summary":
        notice = notice.replace(
            "HG-D1 HAS NOT PASSED.\n\nCOMMENTS",
            "HG-D1 HAS NOT PASSED.\n\nTHIS SUMMARY DOES NOT REPLACE LOU-004.\n\nCOMMENTS",
        )

    story: list = []
    story.append(Spacer(1, 0.35 * inch))
    story.append(Paragraph("BILL A", styles["CoverTitle"]))
    story.append(Paragraph("COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT", styles["CoverSub"]))
    story.append(Spacer(1, 0.15 * inch))
    if kind == "lou":
        story.append(Paragraph("LETTER OF UNDERSTANDING", styles["Center"]))
        story.append(Paragraph("LOU-004", styles["CoverTitle"]))
        story.append(Paragraph("DRAFT 1.10", styles["CoverSub"]))
    else:
        story.append(Paragraph("HUMAN REVIEW SUMMARY", styles["CoverSub"]))
        story.append(Paragraph("WD-BILL-A-113", styles["Center"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph("PUBLIC REVIEW CANDIDATE", styles["CoverWarn"]))
    if kind == "summary":
        story.append(Paragraph("SUMMARY DOES NOT REPLACE LOU-004", styles["CoverWarn"]))
    story.append(Paragraph("NOT HUMAN-ACCEPTED", styles["CoverWarn"]))
    story.append(Paragraph("NOT PROPOSED LEGISLATIVE TEXT", styles["CoverWarn"]))
    story.append(Paragraph("HG-D1 NOT PASSED", styles["CoverWarn"]))
    story.append(Spacer(1, 0.25 * inch))
    story.append(
        Paragraph(
            f'Project URL: <link href="{PROJECT_URL_HREF}" color="blue"><u>{PROJECT_URL_DISPLAY}</u></link>',
            styles["Center"],
        )
    )
    story.append(
        Paragraph(
            f'Canonical repository:<br/><link href="{REPO_URL}" color="blue"><u>{REPO_URL}</u></link>',
            styles["SmallCenter"],
        )
    )
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("Document-control block", styles["H2"]))
    if kind == "lou":
        rows = [
            ("Document", "LOU-004"),
            ("Bill", "Bill A — Comprehensive Kansas Tax-System Replacement"),
            ("Draft", "1.10"),
            ("Review status", "PUBLIC REVIEW CANDIDATE"),
            ("Human acceptance", "NOT HUMAN-ACCEPTED"),
            ("HG-D1", "NOT PASSED"),
            ("Bill A maturity", "19% UNCHANGED"),
            ("Canonical repository", "Constitutional-Engineering"),
            ("Canonical Git SHA", CANONICAL_SHA),
            ("Repository URL", REPO_URL),
            ("Project URL", PROJECT_URL_DISPLAY),
        ]
    else:
        rows = [
            ("Document", "WD-BILL-A-113"),
            ("Bill", "Bill A — Comprehensive Kansas Tax-System Replacement"),
            ("Governing LOU", "LOU-004 Draft 1.10"),
            ("Review status", "PUBLIC REVIEW CANDIDATE"),
            ("Human acceptance", "NOT HUMAN-ACCEPTED"),
            ("HG-D1", "NOT PASSED"),
            ("Bill A maturity", "19% UNCHANGED"),
            ("Role", "INFORMATIONAL SUMMARY — DOES NOT REPLACE LOU-004"),
            ("Canonical repository", "Constitutional-Engineering"),
            ("Canonical Git SHA", CANONICAL_SHA),
            ("Repository URL", REPO_URL),
            ("Project URL", PROJECT_URL_DISPLAY),
        ]
    story.append(control_table(rows, styles))
    story.append(Spacer(1, 0.18 * inch))
    story.append(Paragraph("External-review notice", styles["H2"]))
    story.append(Preformatted(notice, styles["Code"]))
    story.append(Spacer(1, 0.1 * inch))
    if kind == "lou":
        story.append(
            Paragraph(
                "Reviewers are invited to examine architecture for ambiguity, missing considerations, "
                "unintended consequences, internal contradictions, unclear taxpayer or government effects, "
                "transition concerns, constitutional/legal research questions, implementation concerns, and "
                "disagreements with Human Intent. Reviewer comments remain external review evidence until "
                "classified through a later controlled process.",
                styles["Body"],
            )
        )
    else:
        story.append(
            Paragraph(
                "Serious reviewers should read the complete LOU-004, especially <b>§2.0</b>. "
                "This summary is a phone-readable orientation map only. "
                "<b>THIS SUMMARY DOES NOT REPLACE LOU-004.</b>",
                styles["Body"],
            )
        )
    story.append(PageBreak())
    return story


def parse_md_to_flowables(md: str, styles) -> list:
    md = reformat_tables(md)
    lines = md.splitlines()
    story: list = []
    i = 0
    para_buf: list[str] = []
    in_code = False
    code_buf: list[str] = []

    def flush_para():
        nonlocal para_buf
        if not para_buf:
            return
        text = " ".join(x.strip() for x in para_buf)
        if text:
            # metadata-looking lines
            if text.startswith("**") and ":**" in text[:80]:
                story.append(Paragraph(inline_md(text), styles["Meta"]))
            else:
                story.append(Paragraph(inline_md(text), styles["Body"]))
        para_buf = []

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            if in_code:
                flush_para()
                story.append(Preformatted("\n".join(code_buf), styles["Code"]))
                code_buf = []
                in_code = False
            else:
                flush_para()
                in_code = True
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # Table (compact 2-col retained)
        if line.strip().startswith("|"):
            flush_para()
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            if len(block) >= 2 and is_separator_row(split_table_row(block[1])):
                header = split_table_row(block[0])
                rows = [split_table_row(r) for r in block[2:]]
                data = [[Paragraph(inline_md(c), styles["Meta"]) for c in header]]
                for r in rows:
                    cells = list(r) + [""] * max(0, len(header) - len(r))
                    data.append([Paragraph(inline_md(c), styles["Meta"]) for c in cells[: len(header)]])
                usable = PAGE_W - 2 * MARGIN
                if len(header) == 2:
                    widths = [usable * 0.38, usable * 0.62]
                else:
                    widths = [usable / len(header)] * len(header)
                t = Table(data, colWidths=widths, hAlign="LEFT", repeatRows=1)
                t.setStyle(
                    TableStyle(
                        [
                            ("BOX", (0, 0), (-1, -1), 0.5, colors.grey),
                            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.lightgrey),
                            ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.93, 0.93, 0.93)),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 3),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                            ("TOPPADDING", (0, 0), (-1, -1), 3),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                        ]
                    )
                )
                story.append(t)
                story.append(Spacer(1, 0.08 * inch))
            else:
                for b in block:
                    story.append(Paragraph(inline_md(b), styles["Meta"]))
            continue

        if not line.strip():
            flush_para()
            i += 1
            continue

        if line.startswith("# "):
            flush_para()
            story.append(Paragraph(inline_md(line[2:].strip()), styles["H1"]))
            i += 1
            continue
        if line.startswith("## "):
            flush_para()
            story.append(Paragraph(inline_md(line[3:].strip()), styles["H2"]))
            i += 1
            continue
        if line.startswith("### "):
            flush_para()
            story.append(Paragraph(inline_md(line[4:].strip()), styles["H3"]))
            i += 1
            continue
        if line.startswith("#### "):
            flush_para()
            story.append(Paragraph(inline_md(line[5:].strip()), styles["H3"]))
            i += 1
            continue

        if re.match(r"^[-*]\s+", line.strip()):
            flush_para()
            text = re.sub(r"^[-*]\s+", "", line.strip())
            story.append(Paragraph("• " + inline_md(text), styles["Bullet"]))
            i += 1
            continue
        if re.match(r"^\d+\.\s+", line.strip()):
            flush_para()
            story.append(Paragraph(inline_md(line.strip()), styles["Bullet"]))
            i += 1
            continue
        if line.strip() == "---":
            flush_para()
            story.append(HRFlowable(width="100%", thickness=0.6, color=colors.grey, spaceBefore=6, spaceAfter=6))
            i += 1
            continue

        para_buf.append(line)
        i += 1

    flush_para()
    if in_code and code_buf:
        story.append(Preformatted("\n".join(code_buf), styles["Code"]))
    return story


def render_pdf(*, kind: str, source: Path, out_pdf: Path, footer_right: str, title: str, subject: str) -> dict:
    styles = build_styles()
    body = source.read_text(encoding="utf-8")
    story = cover_flowables(kind, styles) + parse_md_to_flowables(body, styles)

    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    def make_canvas(filename, **kwargs):
        return NumberedCanvas(filename, footer_right=footer_right, **kwargs)

    doc = SimpleDocTemplate(
        str(out_pdf),
        pagesize=(PAGE_W, PAGE_H),
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=0.55 * inch,
        bottomMargin=0.65 * inch,
        title=title,
        author="Constitutional Engineering Office / BlueprintLiberty",
        subject=subject,
        creator="CWC-CE-161 phone-first public-review renderer (ReportLab)",
        keywords="Bill A, LOU-004, Public Review Candidate, NOT HUMAN-ACCEPTED, HG-D1 NOT PASSED, "
        + CANONICAL_SHA,
    )
    doc.build(story, canvasmaker=make_canvas)

    import pymupdf

    pdf = pymupdf.open(out_pdf)
    page_count = pdf.page_count
    # verify page size on page 0
    r = pdf[0].rect
    pdf.close()
    return {
        "filename": out_pdf.name,
        "path": str(out_pdf),
        "pdf_sha256": sha256_file(out_pdf),
        "file_size_bytes": out_pdf.stat().st_size,
        "page_count": page_count,
        "page_width_pt": round(r.width, 2),
        "page_height_pt": round(r.height, 2),
    }


def main() -> int:
    root = repo_root()
    pub = Path(__file__).resolve().parents[1]
    pdf_dir = pub / "pdf"
    verify_source_state(root)

    lou_src = root / "Engineering-Office/definition/LOU-004-Bill-A-Comprehensive-Kansas-Tax-System-Replacement.md"
    sum_src = root / "Engineering-Office/definition/working/bill-a/WD-BILL-A-113-LOU-004-Human-Review-Summary.md"

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    artifacts = []

    a = render_pdf(
        kind="lou",
        source=lou_src,
        out_pdf=pdf_dir / "Bill-A-LOU-004-Public-Review-Draft-1.10.pdf",
        footer_right="LOU-004 Draft 1.10 | Public Review Candidate",
        title="Bill A LOU-004 Public Review Draft 1.10",
        subject=f"Public-review PDF from LOU-004 Draft 1.10 @ {CANONICAL_SHA} — NOT HUMAN-ACCEPTED",
    )
    a["source_markdown"] = str(lou_src.relative_to(root)).replace("\\", "/")
    a["source_git_sha"] = CANONICAL_SHA
    a["path"] = str(Path(a["path"]).relative_to(root)).replace("\\", "/")
    artifacts.append(a)
    print("LOU PDF", a["page_count"], "pages", a["pdf_sha256"])

    b = render_pdf(
        kind="summary",
        source=sum_src,
        out_pdf=pdf_dir / "Bill-A-LOU-004-Review-Summary.pdf",
        footer_right="WD-BILL-A-113 | Summary ≠ LOU-004",
        title="Bill A LOU-004 Human Review Summary",
        subject=f"WD-BILL-A-113 informational summary @ {CANONICAL_SHA} — does not replace LOU-004",
    )
    b["source_markdown"] = str(sum_src.relative_to(root)).replace("\\", "/")
    b["source_git_sha"] = CANONICAL_SHA
    b["path"] = str(Path(b["path"]).relative_to(root)).replace("\\", "/")
    artifacts.append(b)
    print("Summary PDF", b["page_count"], "pages", b["pdf_sha256"])

    identity = {
        "cwc": "CWC-CE-161",
        "canonical_git_sha": CANONICAL_SHA,
        "render_timestamp_utc": stamp,
        "toolchain": "Python ReportLab + pymupdf validation; prepare table reformatting",
        "page_size": "6in x 9in portrait (432pt x 648pt)",
        "artifacts": artifacts,
    }
    out_id = pub / "validation" / "CWC-CE-161-ARTIFACT-IDENTITY.json"
    out_id.parent.mkdir(parents=True, exist_ok=True)
    out_id.write_text(json.dumps(identity, indent=2) + "\n", encoding="utf-8")
    print("wrote", out_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
