"""Anti-drift validation: changed pixels may only occur in authorized variable regions."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple

import numpy as np
from PIL import Image


Rect = Tuple[int, int, int, int]  # x, y, w, h


@dataclass(frozen=True)
class AntiDriftResult:
    pass_ok: bool
    total_changed: int
    authorized_changed: int
    unauthorized_changed: int
    changed_bbox: Tuple[int, int, int, int] | None
    authorized_rects: Sequence[Rect]
    message: str


def authorized_rects_from_regions(regions: Dict[str, Any]) -> List[Rect]:
    """Union of text + bar rectangles for the four variables (+ small antialias pad)."""
    pad = 2
    rects: List[Rect] = []
    v = regions["variables"]

    def add(r: Dict[str, int]) -> None:
        x = max(0, r["x"] - pad)
        y = max(0, r["y"] - pad)
        w = r["w"] + 2 * pad
        h = r["h"] + 2 * pad
        rects.append((x, y, w, h))

    add(v["STATUS_DATE"]["region"])
    for bill in ("BILL_A_PERCENT", "BILL_B_PERCENT", "BILL_C_PERCENT"):
        add(v[bill]["text_region"])
        add(v[bill]["bar"])
    return rects


def _in_rects(x: int, y: int, rects: Sequence[Rect]) -> bool:
    for rx, ry, rw, rh in rects:
        if rx <= x < rx + rw and ry <= y < ry + rh:
            return True
    return False


def validate_anti_drift(
    baseline_img: Image.Image | Path | str,
    rendered_img: Image.Image | Path | str,
    authorized_rects: Sequence[Rect],
    *,
    expected_size: Tuple[int, int] = (1536, 912),
) -> AntiDriftResult:
    def load(obj: Image.Image | Path | str) -> Image.Image:
        if isinstance(obj, Image.Image):
            return obj.convert("RGB")
        return Image.open(obj).convert("RGB")

    base = load(baseline_img)
    rend = load(rendered_img)

    if base.size != expected_size or rend.size != expected_size:
        return AntiDriftResult(
            pass_ok=False,
            total_changed=-1,
            authorized_changed=-1,
            unauthorized_changed=-1,
            changed_bbox=None,
            authorized_rects=list(authorized_rects),
            message=f"dimension FAIL: baseline={base.size} rendered={rend.size} expected={expected_size}",
        )

    a = np.asarray(base)
    b = np.asarray(rend)
    diff = np.any(a != b, axis=2)
    ys, xs = np.where(diff)
    total = int(xs.size)
    if total == 0:
        return AntiDriftResult(
            True,
            0,
            0,
            0,
            None,
            list(authorized_rects),
            "PASS: zero pixel differences",
        )

    auth = 0
    unauth = 0
    for x, y in zip(xs.tolist(), ys.tolist()):
        if _in_rects(x, y, authorized_rects):
            auth += 1
        else:
            unauth += 1

    bbox = (int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()))
    ok = unauth == 0
    msg = (
        f"{'PASS' if ok else 'FAIL'}: total={total} authorized={auth} unauthorized={unauth} bbox={bbox}"
    )
    return AntiDriftResult(
        pass_ok=ok,
        total_changed=total,
        authorized_changed=auth,
        unauthorized_changed=unauth,
        changed_bbox=bbox,
        authorized_rects=list(authorized_rects),
        message=msg,
    )
