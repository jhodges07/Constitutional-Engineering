#!/usr/bin/env python3
"""CWC-CE-107 — build successor clean master (does NOT overwrite v1.0-CANDIDATE).

Operations (deterministic, no Telea/generative tooling):
1. Crop public composition to navy-footer bottom (1536×912) — remove engineering metadata.
2. Blank baked STATUS_DATE + week parenthetical with sampled sky fill.
3. Blank stale dated breadcrumb leaf; redraw stable FIXED label \"Report Files\".

Writes:
  templates/BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE.png
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "templates" / "BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE.png"
DST = ROOT / "templates" / "BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE.png"

PUBLIC_HEIGHT = 912  # rows [0, 912) — first light metadata row is y=912
# Date text bbox (includes Date line + Week parenthetical); leave sky for dynamic stamp
DATE_BLANK = (1278, 8, 1525, 58)  # x0,y0,x1,y1 inclusive-ish
# Stale leaf after publication/weekly-status folder crumb (includes prior chevron/globe)
CRUMB_BLANK = (1282, 824, 1518, 848)
CRUMB_LABEL = ">  Report Files"
CRUMB_XY = (1288, 828)
CRUMB_RGB = (20, 45, 95)
CRUMB_BG = (253, 253, 254)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def _sky_fill(arr: np.ndarray, box: tuple[int, int, int, int]) -> None:
    """Fill date rect with horizontally sampled sky from immediately left of the box."""
    x0, y0, x1, y1 = box
    sample_x0 = max(0, x0 - 80)
    sample = arr[y0 : y1 + 1, sample_x0:x0]
    if sample.size == 0:
        fill = np.array([128, 172, 228], dtype=np.uint8)
        arr[y0 : y1 + 1, x0 : x1 + 1] = fill
        return
    # Per-row median of sample columns → paint across blank width
    for yi in range(y0, y1 + 1):
        row_sample = arr[yi, sample_x0:x0]
        med = np.median(row_sample, axis=0).astype(np.uint8)
        arr[yi, x0 : x1 + 1] = med


def build() -> str:
    if not SRC.is_file():
        raise SystemExit(f"missing source clean master: {SRC}")
    src_sha = sha256_bytes(SRC.read_bytes())
    if src_sha != "01C29A8A20CA4D1798E4A407431B0A7FA1BD58F798D5837AD2A1CC1BF9E1D05C":
        raise SystemExit(f"REFUSING: unexpected source SHA {src_sha}")

    im = Image.open(SRC).convert("RGB")
    if im.size != (1536, 1024):
        raise SystemExit(f"unexpected source size {im.size}")

    # Crop engineering metadata below public footer
    public = im.crop((0, 0, 1536, PUBLIC_HEIGHT))
    arr = np.array(public)

    _sky_fill(arr, DATE_BLANK)

    # Breadcrumb leaf blank + stable FIXED label (no weekly date)
    x0, y0, x1, y1 = CRUMB_BLANK
    arr[y0 : y1 + 1, x0 : x1 + 1] = np.array(CRUMB_BG, dtype=np.uint8)

    out = Image.fromarray(arr)
    draw = ImageDraw.Draw(out)
    font = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 14)
    draw.text(CRUMB_XY, CRUMB_LABEL, font=font, fill=CRUMB_RGB)

    DST.parent.mkdir(parents=True, exist_ok=True)
    # Refuse overwrite of v1.0
    if DST.resolve() == SRC.resolve():
        raise SystemExit("REFUSING to overwrite v1.0 clean master")
    out.save(DST, format="PNG", compress_level=9, optimize=False)
    digest = sha256_bytes(DST.read_bytes())
    # Prove source immutable
    if sha256_bytes(SRC.read_bytes()) != src_sha:
        raise SystemExit("SOURCE CLEAN MASTER MUTATED")
    print(f"WROTE {DST}")
    print(f"SIZE {out.size[0]}x{out.size[1]}")
    print(f"SHA256 {digest}")
    print(f"SOURCE_IMMUTABLE PASS ({src_sha})")
    return digest


if __name__ == "__main__":
    build()
