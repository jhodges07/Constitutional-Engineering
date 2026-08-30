"""KSB Issue-bridge controlled constants (ECR-009 / KSB-ISSUE-BRIDGE-001)."""

from __future__ import annotations

import re

REQUEST_SCHEMA_VERSION = "1.0.0"
PUBLICATION_REQUEST_TYPE = "KSB_WEEKLY_STATUS"

BASELINE_ID = "BL-WEEKLY-STATUS-BASELINE-v1.0"
BASELINE_SHA256 = "17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9"
BASELINE_WIDTH = 1536
BASELINE_HEIGHT = 912

RENDERER_ID = "ksb_renderer@1.0.0-CWC-CE-084"

TITLE_PREFIX = "[KSB-RENDER] "
REQUEST_ID_RE = re.compile(r"^KSB-RENDER-\d{4}-\d{2}-\d{2}-\d{3}$")
SHA40_RE = re.compile(r"^[0-9a-f]{40}$")

TRUSTED_ASSOCIATIONS = frozenset({"OWNER", "MEMBER", "COLLABORATOR"})

ENVELOPE_KEYS = frozenset(
    {
        "request_schema_version",
        "publication_request_type",
        "request_id",
        "canonical_sha",
        "baseline_id",
        "renderer_id",
        "render_payload",
    }
)

RENDER_PAYLOAD_KEYS = frozenset(
    {"status_date", "bill_a_percent", "bill_b_percent", "bill_c_percent"}
)

# Markers for machine-readable Issue body extraction
BODY_FENCE_START = "```ksb-render-request"
BODY_FENCE_END = "```"

ARTIFACT_NAME_PREFIX = "ksb-render-"

RESULT_SCHEMA_VERSION = "1.0.0"
