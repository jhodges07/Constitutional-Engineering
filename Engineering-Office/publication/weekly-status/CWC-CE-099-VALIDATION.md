# CWC-CE-099 — Validation Report

**Outcome:** **A**  
**Agent:** CE-Engineer  
**Date:** 2026-08-30  

---

## Human-facing summary

```text
CWC-CE-099
KSB CLEAN-MASTER BASELINE_ID CONTRACT RECONCILIATION

OUTCOME: A

ROOT CAUSE:
Issue #6 put the clean-master template ID into baseline_id.
The gate still (correctly) requires historical baseline_id
BL-WEEKLY-STATUS-BASELINE-v1.0. Rejection occurred before render.

FAILED HOSTED REQUEST: KSB-RENDER-2026-08-30-005
FAILED ISSUE: #6
FAILED RUN: 33339179855
ORIGINAL FAILURE: INVALID_INPUT: baseline_id mismatch

OLD EXPECTED baseline_id: BL-WEEKLY-STATUS-BASELINE-v1.0
REQUESTED baseline_id: BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE

FINAL baseline_id MEANING: HISTORICAL visual baseline identity
FINAL baseline_id: BL-WEEKLY-STATUS-BASELINE-v1.0
ACTIVE CLEAN MASTER: BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE
  (selected by renderer_id → regions.json; NOT via baseline_id field)
ACTIVE RENDERER: ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE

LOCAL GATE: PASS
NEGATIVE GATE TESTS: PASS
LOCAL NEW-IMAGE RENDER: PASS
MASTER IMMUTABLE: PASS
PREVIOUS WEEKLY PNG USED: NO
POPULATED BASELINE USED AS CANVAS: NO
CWC-CE-096 FIXED LAYER USED: NO
KSB MATURITY: 19 / 19 / 4 — UNCHANGED
VISUAL ARCHITECTURE: PRESERVED (byte-identical to CE-097 accepted SHA 78D5E2E1…)
HUMAN VISUAL RE-ACCEPTANCE: NOT REQUIRED
DATE ISSUE: UNCHANGED
STALE BREADCRUMB: UNCHANGED
NEW LIVE ISSUE: NOT CREATED
HOSTED TEST: NOT RUN
GIT: HANDOFF PREPARED (no commit/push under this CWC)

NEXT AGENT: Human Engineer / ChatGPT
NEXT ACTION: Review evidence; authorize next CWC for Git canonicalization
and/or one new hosted acceptance test (new request_id / new Issue — not #6).

STOP.
```

---

## Selected reconciliation

**Option A:** Keep `baseline_id` = historical baseline; `renderer_id` selects clean master.

**Why:** Proven by gate constants, orchestration package identity, and CE-097/014 architecture separating historical baseline from clean master. Redefining baseline_id to clean master would collapse two controlled concepts. Adding `render_template_id` unnecessary for this defect.

**ECR:** No new ECR required — ECR-014 already separates identities; CWC-CE-099 clarifies Issue-field mapping + operator contract. KSB-ORCH → **1.5.1** (clarification). STD-011 unchanged at **1.9.0**.

---

## Machine-usable corrected Issue body

```ksb-render-request
{
  "request_schema_version": "1.0.0",
  "publication_request_type": "KSB_WEEKLY_STATUS",
  "request_id": "KSB-RENDER-YYYY-MM-DD-NNN",
  "canonical_sha": "87e48e631edbc21cc64d96cc2095a0b2703d63d0",
  "baseline_id": "BL-WEEKLY-STATUS-BASELINE-v1.0",
  "renderer_id": "ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE",
  "render_payload": {
    "status_date": "2026-08-30",
    "bill_a_percent": 19,
    "bill_b_percent": 19,
    "bill_c_percent": 4
  }
}
```

**DO NOT** set `baseline_id` to `BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE`.

Also written to:
`issue-bridge/tests/_non_production_output/CWC-CE-099-CORRECTED-REQUEST-EXAMPLE.json`

---

## Test counts

| Suite | Result |
|---|---|
| `test_ce099_baseline_id_contract.py` | **PASS** (Issue #6 repro + correct ACCEPT + negatives + render) |
| `test_gate.py` | **20/20 PASS** |
| `test_three_step.py` | **32/32 PASS** |

Local PNG SHA = `78D5E2E1CA11078106DC4585867651915490E2B8745B7E2A08CDB3D303A111DD` (CE-097 accepted).
