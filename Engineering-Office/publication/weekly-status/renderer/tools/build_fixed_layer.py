#!/usr/bin/env python3
"""OFFLINE builder for FIXED-LAYER-v1.0-CWC-CE-096.

NOT part of ordinary weekly render. Ordinary render never derives the fixed
layer from the populated baseline at runtime.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image

WEEKLY = Path(__file__).resolve().parents[2]
BASELINE = WEEKLY / "baseline" / "BL-WEEKLY-STATUS-BASELINE-v1.0.png"
REGIONS = WEEKLY / "renderer" / "regions.json"
OUT = WEEKLY / "renderer" / "assets" / "FIXED-LAYER-v1.0-CWC-CE-096.png"

CLEAR = {
    "STATUS_DATE": {"x": 1275, "y": 10, "w": 260, "h": 38, "rgb": [128, 173, 228]},
    "BILL_A_TEXT": {"x": 940, "y": 430, "w": 160, "h": 55, "rgb": [254, 254, 254]},
    "BILL_B_TEXT": {"x": 940, "y": 560, "w": 160, "h": 55, "rgb": [254, 254, 253]},
    "BILL_C_TEXT": {"x": 940, "y": 680, "w": 160, "h": 55, "rgb": [255, 255, 254]},
}


def main() -> int:
    regions = json.loads(REGIONS.read_text(encoding="utf-8"))
    im = Image.open(BASELINE).convert("RGB")
    assert im.size == (1536, 912)
    rgb = np.array(im)
    for r in CLEAR.values():
        x, y, w, h = r["x"], r["y"], r["w"], r["h"]
        rgb[y : y + h, x : x + w] = np.array(r["rgb"], dtype=np.uint8)
    for bill in ("BILL_A_PERCENT", "BILL_B_PERCENT", "BILL_C_PERCENT"):
        bar = regions["variables"][bill]["bar"]
        x, y, w, h = bar["x"] - 2, bar["y"] - 2, bar["w"] + 4, bar["h"] + 4
        x, y = max(0, x), max(0, y)
        rgb[y : y + h, x : x + w] = np.array(bar["track_rgb"], dtype=np.uint8)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(rgb, "RGB").save(OUT, format="PNG", compress_level=9, optimize=False)
    digest = hashlib.sha256(OUT.read_bytes()).hexdigest().upper()
    print(f"Wrote {OUT}")
    print(f"SHA256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
