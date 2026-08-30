# FIRST AUTHORITATIVE KSB MATURITY RECALCULATION — CWC-CE-085

**Document ID:** KSB-MATURITY-CALC-001  
**Classification:** Evidence Snapshot + Calculated Maturity Ledger  
**Authority:** Active WSMAT-001 v1.0.0 under STD-011 v1.3.0 / ECR-005  
**Governing Work Card:** CWC-CE-085 — ECR-005 Human Acceptance Implementation  
**Evaluator:** CE-Engineer (AI authorized measurer/proposer)  
**Status:** CALCULATED — **HUMAN CERTIFIED** (see KSB-MATURITY-CERT-001)  
**Calculation Date:** 2026-08-30  
**Version:** 1.0.0  

```text
CALCULATED MATURITY PRODUCED UNDER WSMAT-001
HUMAN CERTIFICATION: SEE KSB-MATURITY-CERT-001-CWC-CE-085.md
CERTIFIED VALUES: Bill A=19% Bill B=19% Bill C=4% (ACCEPT)
PROVISIONAL 27/27/8 NOT INHERITED
NO LOU HG-D1 PASSED
```

---

## Evidence Snapshot (common)

| Field | Value |
|---|---|
| `status_calendar_date` | 2026-08-30 (evaluation date; STATUS_DATE for public package not certified here) |
| `repository` | `X:\GitHub\Constitutional-Engineering` |
| `branch` | `main` |
| `commit_sha` | `c99c0b33ef3f923e979a8136cad1e8f07ab42dba` (local HEAD == origin/main at start; control changes local-only, uncommitted) |
| `calculation_control` | WSMAT-001 Version 1.0.0 |
| `std_packaging` | STD-011 Version 1.3.0 |
| `ecr` | ECR-005 Implemented locally |
| `baseline_sha256` | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` (immutable) |
| `HG-D1_Bill_A` | NOT PASSED |
| `HG-D1_Bill_B` | NOT PASSED |
| `HG-D1_Bill_C` | NOT PASSED |
| `evaluator` | CE-Engineer |

Formula: `raw = 100 × credited_stage_units / 13`; `public = ROUND_HALF_UP(raw)`.

---

## BILL A — COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT

**CALCULATED MATURITY: 19%**  
**CERTIFIED KSB MATURITY: 19%**  
**HUMAN DISPOSITION: ACCEPT**  
**CERTIFICATION RECORD:** `KSB-MATURITY-CERT-001-CWC-CE-085.md`

### Stage ledger

**KS-S01**  
State: CA  
Units: 1.00  
Evidence: CONTROLLED public pin (STD-011 §26) + RECOGNIZED_DRAFT problem/purpose for Bill A in LOU-001 Draft 0.3 (`Engineering-Office/definition/LOU-001-Kansas-Two-Bill-Tax-Engineering-Project.md`) describing comprehensive replacement + shared elimination destination.

**KS-S02**  
State: ID  
Units: 0.50  
Evidence: RECOGNIZED_DRAFT Human Engineering Intent recorded in LOU-001 §2 for Bill A; HE intent not Human-accepted (HG-D1 not passed) → cannot be CA.

**KS-S03**  
State: ID  
Units: 0.50  
Evidence: INFORMATIVE RESEARCH package exists (`Engineering-Office/packages/ChatGPT-Kansas-Tax-Engineering/`, including research model materials). No HE acceptance of research sufficiency; LOU not accepted → not CA.

**KS-S04**  
State: ID  
Units: 0.50  
Evidence: RECOGNIZED_DRAFT LOU-001 Draft 0.3 covers Bill A; Acceptance Status NOT ACCEPTED; HG-D1 PENDING → ID, not RR (no explicit ready-for-review declaration beyond draft pending), not CA.

**KS-S05…KS-S13**  
State: NS (credit blocked)  
Units: 0.00 each  
Evidence: HARD GATE HG-D1 unsatisfied. Any SPEC drafts / legislative packages / downstream work = WORK EXISTS — MATURITY CREDIT BLOCKED (e.g., package SPEC drafts under `packages/ChatGPT-Kansas-Tax-Engineering/`).

### Totals

| Item | Value |
|---|---|
| FIRST UNSATISFIED HARD GATE | HG-D1 — LOU Acceptance |
| DOWNSTREAM CREDIT BLOCKED | KS-S05 through KS-S13 |
| CREDITED STAGE UNITS | 2.50 / 13.00 |
| RAW MATURITY | 19.230769…% |
| ROUNDING | ROUND_HALF_UP → **19%** |

---

## BILL B — KANSAS PROPERTY-TAX ELIMINATION

**CALCULATED MATURITY: 19%**  
**CERTIFIED KSB MATURITY: 19%**  
**HUMAN DISPOSITION: ACCEPT**  
**CERTIFICATION RECORD:** `KSB-MATURITY-CERT-001-CWC-CE-085.md`

Evaluated independently under WSMAT-001 (not assumed equal to Bill A).

### Stage ledger

**KS-S01**  
State: CA  
Units: 1.00  
Evidence: CONTROLLED public pin (STD-011 §26) + RECOGNIZED_DRAFT problem/purpose for Bill B in LOU-001 Draft 0.3 (property-tax elimination mandate / zero destination).

**KS-S02**  
State: ID  
Units: 0.50  
Evidence: RECOGNIZED_DRAFT intent in LOU-001 §2 for Bill B; HG-D1 not passed → not CA.

**KS-S03**  
State: ID  
Units: 0.50  
Evidence: Same informative tax-engineering research package supports both bills’ Engineering Definition research; no HE research-sufficiency acceptance → ID.

**KS-S04**  
State: ID  
Units: 0.50  
Evidence: RECOGNIZED_DRAFT LOU-001 Draft 0.3 covers Bill B; NOT ACCEPTED / HG-D1 PENDING → ID.

**KS-S05…KS-S13**  
State: NS (credit blocked)  
Units: 0.00 each  
Evidence: HARD GATE HG-D1 unsatisfied.

### Totals

| Item | Value |
|---|---|
| FIRST UNSATISFIED HARD GATE | HG-D1 — LOU Acceptance |
| DOWNSTREAM CREDIT BLOCKED | KS-S05 through KS-S13 |
| CREDITED STAGE UNITS | 2.50 / 13.00 |
| RAW MATURITY | 19.230769…% |
| ROUNDING | ROUND_HALF_UP → **19%** |

---

## BILL C — KANSAS NBEF ACT (Node-Based Educational Framework)

**CALCULATED MATURITY: 4%**  
**CERTIFIED KSB MATURITY: 4%**  
**HUMAN DISPOSITION: ACCEPT**  
**CERTIFICATION RECORD:** `KSB-MATURITY-CERT-001-CWC-CE-085.md`

### Stage ledger

**KS-S01**  
State: ID  
Units: 0.50  
Evidence: CONTROLLED public title pin only (STD-011 §26 / CWC-CE-077). No recognized Engineering Definition problem statement for Bill C legislative object → pin alone capped at ID per WSMAT-001 §9.1.

**KS-S02**  
State: NS  
Units: 0.00  
Evidence: UNKNOWN / NOT VERIFIED — no Bill C HE-intent LOU/ED draft found.

**KS-S03**  
State: NS  
Units: 0.00  
Evidence: UNKNOWN / NOT VERIFIED — no Bill C legislative research package verified. NBEF framework repository maturity is not Bill C legislative research credit.

**KS-S04**  
State: NS  
Units: 0.00  
Evidence: No Bill C legislative LOU. Framework ≠ Bill C LOU firewall enforced.

**KS-S05…KS-S13**  
State: NS (credit blocked)  
Units: 0.00 each  
Evidence: HARD GATE HG-D1 unsatisfied (LOU not started / not passed).

### Totals

| Item | Value |
|---|---|
| FIRST UNSATISFIED HARD GATE | HG-D1 — LOU Acceptance (NOT STARTED for Bill C legislative LOU) |
| DOWNSTREAM CREDIT BLOCKED | KS-S02 partial eligibility exists only with evidence; KS-S05–S13 blocked |
| CREDITED STAGE UNITS | 0.50 / 13.00 |
| RAW MATURITY | 3.846153…% |
| ROUNDING | ROUND_HALF_UP → **4%** |

---

## Comparison to prior provisional samples

| Bill | Provisional (non-authoritative) | First authoritative calculated |
|---|---|---|
| A | 27% | **19%** |
| B | 27% | **19%** |
| C | 8% | **4%** |

Difference is expected: Active WSMAT-001 applies stricter S02/S03 CA rules (HE acceptance required for CA) and S01 pin-alone cap (Bill C). Values were recalculated from zero; not inherited.

---

## Human certification requested

**COMPLETED under CWC-CE-085 Final Phone-POC continuation.**

See `KSB-MATURITY-CERT-001-CWC-CE-085.md`:

| Bill | Calculated | Certified | Disposition |
|---|---|---|---|
| A | 19% | 19% | ACCEPT |
| B | 19% | 19% | ACCEPT |
| C | 4% | 4% | ACCEPT |

Silence is not certification. This record is the Human Engineer certification.

---

## Planning note only (not authorization)

After successful completion of the first phone-originated KSB Status POC, the Human Engineer intends to move Bills A, B, and C toward controlled PUBLIC REVIEW of their respective Letters of Understanding for Kansas citizens and legislative candidates.  
**This note does not authorize publication or outreach.**
