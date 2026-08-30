"""RESULT.json writer for KSB Issue-bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Optional

from .constants import RESULT_SCHEMA_VERSION


def build_result(
    *,
    request: Mapping[str, Any],
    run_id: Optional[int],
    output_filename: str,
    output_sha256: str,
    output_width: int,
    output_height: int,
    renderer_test_result: str,
    anti_drift_result: str,
    execution_result: str,
    baseline_sha256: str,
) -> dict[str, Any]:
    return {
        "schema_version": RESULT_SCHEMA_VERSION,
        "request_id": request["request_id"],
        "issue_number": request["issue_number"],
        "run_id": run_id,
        "canonical_sha": request["canonical_sha"],
        "status_date": request["status_date"],
        "bill_a_percent": request["bill_a_percent"],
        "bill_b_percent": request["bill_b_percent"],
        "bill_c_percent": request["bill_c_percent"],
        "baseline_id": request["baseline_id"],
        "baseline_sha256": baseline_sha256,
        "renderer_identity": request["renderer_id"],
        "output_filename": output_filename,
        "output_sha256": output_sha256,
        "output_width": output_width,
        "output_height": output_height,
        "renderer_test_result": renderer_test_result,
        "anti_drift_result": anti_drift_result,
        "execution_result": execution_result,
    }


def write_result(path: Path, result: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
