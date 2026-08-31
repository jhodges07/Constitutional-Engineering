"""Anti-drift validation: changed pixels may only occur in authorized regions.

CWC-CE-097: ordinary comparison reference is the CLEAN MASTER TEMPLATE.
Authorized region is the Kansas Legislative Engineering Status center panel
where dynamic bill content is composed.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

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
    """Dynamic surfaces: center panel + STATUS_DATE (CWC-CE-107)."""
    pad = 2
    rects: List[Rect] = []
    b = regions["center_panel"]["bounds"]
    rects.append(
        (
            max(0, int(b["x"]) - pad),
            max(0, int(b["y"]) - pad),
            int(b["w"]) + 2 * pad,
            int(b["h"]) + 2 * pad,
        )
    )
    sd = regions.get("status_date") or {}
    ab = sd.get("authorized_bounds")
    if ab:
        rects.append(
            (
                max(0, int(ab["x"]) - pad),
                max(0, int(ab["y"]) - pad),
                int(ab["w"]) + 2 * pad,
                int(ab["h"]) + 2 * pad,
            )
        )
    return rects


def _in_rects(x: int, y: int, rects: Sequence[Rect]) -> bool:
    for rx, ry, rw, rh in rects:
        if rx <= x < rx + rw and ry <= y < ry + rh:
            return True
    return False


def validate_anti_drift(
    reference_img: Image.Image | Path | str,
    rendered_img: Image.Image | Path | str,
    authorized_rects: Sequence[Rect],
    *,
    expected_size: Tuple[int, int] | None = None,
) -> AntiDriftResult:
    def load(obj: Image.Image | Path | str) -> Image.Image:
        if isinstance(obj, Image.Image):
            return obj.convert("RGB")
        return Image.open(obj).convert("RGB")

    ref = load(reference_img)
    rend = load(rendered_img)
    if expected_size is None:
        expected_size = ref.size

    if ref.size != expected_size or rend.size != expected_size:
        return AntiDriftResult(
            pass_ok=False,
            total_changed=-1,
            authorized_changed=-1,
            unauthorized_changed=-1,
            changed_bbox=None,
            authorized_rects=list(authorized_rects),
            message=f"dimension FAIL: ref={ref.size} rendered={rend.size} expected={expected_size}",
        )

    a = np.asarray(ref)
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
