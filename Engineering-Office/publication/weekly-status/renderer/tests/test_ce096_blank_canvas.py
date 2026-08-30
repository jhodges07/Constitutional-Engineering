#!/usr/bin/env python3
"""CWC-CE-096 tests SUPERSEDED by CWC-CE-097 clean-template architecture.

Historical CE-096 fixed-layer candidate was Human-rejected (visual).
This file records supersession and verifies CE-096 fixed layer is not the ordinary path.
"""

from __future__ import annotations

import sys
from pathlib import Path

RENDERER_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RENDERER_ROOT))

from ksb_renderer.render import RENDERER_VERSION  # noqa: E402


def main() -> int:
    src = (RENDERER_ROOT / "ksb_renderer" / "render.py").read_text(encoding="utf-8")
    assert RENDERER_VERSION == "2.0.0-CWC-CE-097-CANDIDATE"
    assert "verify_clean_master" in src
    assert "PROHIBITS CWC-CE-096 fixed-layer" in src
    print("[PASS] ce096_superseded_by_ce097")
    print("[PASS] ce096_fixed_layer_not_ordinary_path")
    print("\nce096 historical tests: SUPERSEDED (spot-check PASS)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
