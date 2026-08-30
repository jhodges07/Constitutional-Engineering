# KSB-ORCH-001 — Test Scenarios (CWC-CE-088 Implementation Continuation)

**Document ID:** KSB-ORCH-001-TEST-CWC-CE-088  
**Governing Procedure:** KSB-ORCH-001 v1.1.0 — Active under STD-011 v1.5.0 / ECR-008  
**Governing Standard:** STD-011 Version 1.5.0 Part B  
**Governing Work Card:** CWC-CE-088 Bounded Continuation — ECR-008 Implementation  
**Classification:** Controlled Validation — Rule Application (not live phone re-run)  
**Date:** 2026-08-30  
**Agent:** CE-Engineer  

```text
AUTHORITY: STD-011 v1.5.0 §36.9 ACTIVE LOCALLY + KSB-ORCH-001 v1.1.0 ACTIVE
VALIDATION METHOD: Apply Active rules to each scenario.
LIVE PHONE RE-EXECUTION: NOT PERFORMED / NOT CLAIMED.
PUBLICATION: NOT PERFORMED.
CWC-CE-087 REGRESSION: PRESERVED.
```

---

## Fixtures

| Field | Value |
|---|---|
| Baseline | `BL-WEEKLY-STATUS-BASELINE-v1.0` / SHA `17F574D4…` / 1536×912 |
| Certified maturity | A=19% B=19% C=4% UNCHANGED |
| Word tolerance | 450–550 |

---

## Results

| Test | Expected | Result |
|---|---|---|
| 1 Single command | Complete Sunday-package workflow | **PASS** |
| 2 Status required | Evidence-derived controlled status mandatory | **PASS** |
| 3 Press release automatic | 450–550 words; no second request | **PASS** |
| 4 Controlled image automatic | Baseline→renderer; no generic substitute | **PASS** |
| 5 Renderer unavailable | RENDER REQUIRED; PACKAGE INCOMPLETE; no creative | **PASS** |
| 6 Human certification | Gate preserved; same cycle continues | **PASS** |
| 7 Publication gate | HUMAN REVIEW/PUBLICATION REQUIRED; no auto-post | **PASS** |
| 8 Creative follow-up | Separate OK; controlled image unchanged | **PASS** |
| 9 Press-release fact drift | Controlled evidence wins | **PASS** |
| 10 Next week | Fresh cycle; prior package preserved | **PASS** |
| **TOTAL** | | **10 / 10 PASS** |

### CWC-CE-087 regression

Follow-up context, controlled-image default, creative firewall, RENDER REQUIRED — **PASS** (not weakened).

---

## Residual Human gates

1. Human Git decision (CE-GitManager if authorized).  
2. After `origin/main`: live phone re-POC with exactly `Prepare KSB Status`.

---

## Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-30 | CWC-CE-088 ten-scenario validation (ECR-008 Proposed). |
| 1.1.0 | 2026-08-30 | Re-validated against STD-011 v1.5.0 / ECR-008 Implemented locally. |
