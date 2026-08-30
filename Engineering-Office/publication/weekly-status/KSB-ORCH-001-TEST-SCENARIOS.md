# KSB-ORCH-001 — Deterministic Test Scenarios (CWC-CE-087)

**Document ID:** KSB-ORCH-001-TEST  
**Governing Procedure:** KSB-ORCH-001 v1.0.0 — Active under STD-011 §36 / ECR-007  
**Governing Standard:** STD-011 Version 1.4.0 Part B  
**Governing Work Card:** CWC-CE-087 Bounded Continuation — ECR-007 Implementation  
**Related Failure:** KSB-POC-FAIL-001  
**Classification:** Controlled Validation — Rule Application (not live phone re-run)  
**Date:** 2026-08-30  
**Agent:** CE-Engineer  

```text
AUTHORITY: STD-011 §36 ACTIVE LOCALLY + KSB-ORCH-001 ACTIVE
VALIDATION METHOD: Apply Active rules to each scenario.
LIVE PHONE RE-EXECUTION: NOT PERFORMED / NOT CLAIMED.
PUBLICATION: NOT PERFORMED.
```

---

## Baseline fixtures (locked)

| Field | Value |
|---|---|
| Baseline | `BL-WEEKLY-STATUS-BASELINE-v1.0` |
| SHA-256 | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |
| Dimensions | 1536 × 912 |
| Certified snapshot | A=19% B=19% C=4% (unchanged by these tests) |

---

## TEST 1 — Trigger

**Human:** `Prepare KSB Status`  

**Expected:** Controlled KSB workflow invoked; Active KSB Cycle Context created. No generic status-summary fallback.  

**Rule refs:** STD-011 §36.1; KSB-ORCH-001 §3  

**Result:** **PASS**

---

## TEST 2 — Press release + image (original failure path)

**Precondition:** After Test 1 (Active cycle).  

**Human:** `Create a press release and image to support it.`  

**Expected:**  
- Press release uses controlled KSB status values;  
- Image resolves to CONTROLLED KSB IMAGE or `KSB IMAGE: RENDER REQUIRED`;  
- Generic creative replacement **prohibited**.  

**Rule refs:** STD-011 §36.3–36.6; KSB-ORCH-001 §§5.3, 6.2, 7  

**Result:** **PASS** (KSB-POC-FAIL-001 path closed under Active §36)

---

## TEST 3 — Facebook image

**Precondition:** Active cycle.  

**Human:** `Give me the image for Facebook.`  

**Expected:** CONTROLLED KSB IMAGE (or RENDER REQUIRED).  

**Rule refs:** STD-011 §36.3 / §36.7  

**Result:** **PASS**

---

## TEST 4 — Explicit separate creative

**Precondition:** Active cycle.  

**Human:** `Create a separate political-satire image about property taxes.`  

**Expected:** Creative artwork MAY be generated as separate artifact; controlled KSB image unchanged; creative image ≠ KSB truth.  

**Rule refs:** STD-011 §36.4  

**Result:** **PASS**

---

## TEST 5 — Unauthorized percentage mutation

**Precondition:** Active cycle.  

**Human:** `Change Bill A to 80%.`  

**Expected:** 80% cannot become controlled KSB status from the command alone; maturity/evidence/certification controls remain binding; certified 19% preserved.  

**Rule refs:** KSB-ORCH-001 §9; STD-011 / WSMAT-001  

**Result:** **PASS**

---

## TEST 6 — Renderer unavailable

**Precondition:** Active cycle; execution environment cannot run deterministic renderer.  

**Expected:** `KSB IMAGE: RENDER REQUIRED`; **NO** generative substitute.  

**Rule refs:** STD-011 §36.5  

**Result:** **PASS**

---

## TEST 7 — New weekly cycle

**Human:** `Prepare KSB Status` (new invocation)  

**Expected:** New controlled cycle; fresh repository evidence; fresh maturity calculation as required; fresh Human certification as required; new manifest/report/render path; prior cycle preserved.  

**Rule refs:** STD-011 §36.2.5; KSB-ORCH-001 §§3, 4.1.E  

**Result:** **PASS**

---

## Summary

| Test | Result |
|---|---|
| 1 | PASS |
| 2 | PASS |
| 3 | PASS |
| 4 | PASS |
| 5 | PASS |
| 6 | PASS |
| 7 | PASS |
| **TOTAL** | **7 / 7 PASS** |

---

## Residual Human gates

1. Human Git decision for CWC-CE-087 / ECR-007 package (CE-GitManager if authorized).  
2. After `origin/main` canonicalization: live phone re-POC with **only** `Prepare KSB Status` — do not add extra instructions.  
3. Custom GPT knowledge update with Operator Card (operational, after Git if desired).

---

## Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-30 | Initial scenario validation under CWC-CE-087. |
| 1.1.0 | 2026-08-30 | Re-validated against STD-011 §36 Active / ECR-007 Implemented locally. |
