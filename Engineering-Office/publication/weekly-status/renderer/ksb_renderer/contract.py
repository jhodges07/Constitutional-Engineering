"""Input contract and validation for KSB Status deterministic renderer."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Any, Mapping


class InputValidationError(ValueError):
    """Fail-closed input validation error. No successful render may proceed."""


AUTHORIZED_KEYS = frozenset(
    {"status_date", "bill_a_percent", "bill_b_percent", "bill_c_percent"}
)


@dataclass(frozen=True)
class NormalizedInput:
    calendar_date: date
    status_date_compact: str  # yyyy.mm.ww
    bill_a_percent: int
    bill_b_percent: int
    bill_c_percent: int


def format_status_date(d: date) -> str:
    """yyyy.mm.ww — calendar yyyy/mm; ISO-8601 week for ww only."""
    yyyy = d.year
    mm = d.month
    ww = d.isocalendar()[1]
    return f"{yyyy:04d}.{mm:02d}.{ww:02d}"


def _parse_calendar_date(value: Any) -> date:
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if not isinstance(value, str):
        raise InputValidationError("status_date must be a calendar date string YYYY-MM-DD")
    s = value.strip()
    try:
        return date.fromisoformat(s)
    except ValueError as exc:
        raise InputValidationError(
            f"status_date is not a parseable calendar date YYYY-MM-DD: {value!r}"
        ) from exc


def _parse_percent(name: str, value: Any, lo: int, hi: int) -> int:
    if value is None:
        raise InputValidationError(f"{name} is missing")
    if isinstance(value, bool):
        raise InputValidationError(f"{name} must be an integer percent, not bool")
    if isinstance(value, float):
        if not value.is_integer():
            raise InputValidationError(
                f"{name} must be an integer percent; fractional values are rejected (no silent rounding)"
            )
        value = int(value)
    if isinstance(value, str):
        raise InputValidationError(f"{name} must be numeric integer, not string")
    if not isinstance(value, int):
        raise InputValidationError(f"{name} must be an integer percent")
    if value < lo or value > hi:
        raise InputValidationError(
            f"{name}={value} out of controlled range [{lo}, {hi}] (no silent clamp)"
        )
    return value


def validate_and_normalize(
    raw: Mapping[str, Any],
    *,
    percent_min: int = 0,
    percent_max: int = 100,
) -> NormalizedInput:
    """Validate Human-supplied weekly variables. Fail closed on defect."""
    if not isinstance(raw, Mapping):
        raise InputValidationError("input must be a mapping/object")

    unknown = set(raw.keys()) - AUTHORIZED_KEYS
    if unknown:
        raise InputValidationError(
            f"unauthorized keys present (no fifth weekly variable allowed): {sorted(unknown)}"
        )

    for key in AUTHORIZED_KEYS:
        if key not in raw:
            raise InputValidationError(f"required key missing: {key}")

    cal = _parse_calendar_date(raw["status_date"])
    compact = format_status_date(cal)
    a = _parse_percent("bill_a_percent", raw["bill_a_percent"], percent_min, percent_max)
    b = _parse_percent("bill_b_percent", raw["bill_b_percent"], percent_min, percent_max)
    c = _parse_percent("bill_c_percent", raw["bill_c_percent"], percent_min, percent_max)

    return NormalizedInput(
        calendar_date=cal,
        status_date_compact=compact,
        bill_a_percent=a,
        bill_b_percent=b,
        bill_c_percent=c,
    )
