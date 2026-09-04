# WD-BILL-A-090 — Sedgwick Current-State Gaps, Conflicts, Unknowns, and Future-State Input Requirements

**Document ID:** WD-BILL-A-090  
**Source ID:** SRC-BILL-A-321  
**Governing Work Card:** CWC-CE-148; **CWC-CE-150** dispositions  
**Status:** WORKING / GAP REGISTER — NOT FUTURE-STATE DESIGN — NOT ACCEPTED  
**Version:** 1.1.0  
**Retrieval date:** 2026-09-04  

```text
GAP ≠ LICENSE TO INVENT
UNRESOLVED ≠ FORCE RECONCILIATION
INPUT REQUIREMENT ≠ DESIGNED MECHANISM
THIS CWC DOES NOT DESIGN THE FUTURE STATE
UQ-TR-001–012 REMAIN OPEN
UQ-CTS-001–016 REMAIN OPEN
```

Master: WD-BILL-A-082.

Completeness of this first execution stage: **SUBSTANTIALLY COMPLETE FOR ARCHITECTURE WITH EXPLICIT GAPS.** Not every minor entity is enumerated. Material fiscal architectures are not silently omitted.

---

# 1. Conflicts / unlike quantities (do not collapse)

| ID | Items | Status |
|---|---|---|
| CF-SED-001 | County ACFR property taxes **$241,512,296** vs PVD county district **$205,980,345.17** | **PARTIALLY CLASSIFIED / NUMERICAL BRIDGE UNRESOLVED** (WD-BILL-A-094) |
| CF-SED-002 | PVD taxable value **$7,548,699,392** vs mill-sheet county AV **$7,546,656,630** | **UNRESOLVED** |
| CF-SED-003 | County ACFR sales taxes **$41,840,210** vs Q4/KDOR BoC **$41,127,614** | **CLOSED as unlike quantities** (GAAP vs KDOR/Q4); both County-share |
| CF-SED-004 | CY2025 countywide **sales $121,665,410.28** vs FY2025 countywide **sales+use $145,054,963.23** | **CLOSED as explained unlike quantities** (CY vs FY; sales vs sales+use) |
| CF-SED-005 | Human Wichita **nearly $7M** vs KDOR/ACFR Wichita 12-192 / sales-tax series | **CLOSED** — HUMAN LEAD **NOT VERIFIED / CONTRADICTED** |
| CF-SED-006 | USD 259 ACFR revenues **$874,033,452** vs news/budget **~$1.01B / ~$1.32B** | **CLOSED as unlike-quantity classification** (no new USD audit) |
| CF-SED-007 | KU taxable-sales method vs food-phaseout non-uniform rate | **CLOSED as methodological classification** (WD-BILL-A-094) |
| CF-SED-008 | Wichita KDOR CY2025 12-192 S+U **$85,253,695.74** vs Wichita ACFR local sales tax **$86,828,492** | **UNRESOLVED residual** — do not force |

Year-to-year sales-tax change explanations (food phaseout; NCAA; retail growth; post-pandemic normalization): **HYPOTHESES / EVIDENCE LEADS**, not proven causation.

---

# 2. Evidence required (material)

| Gap | Why it matters | Suggested primary source |
|---|---|---|
| KDOR CY2025 **annual revised** state sales/use workbooks | Confirm monthly-file CY2025 construction | `cy25revised.xlsx` / `cy25reviseduse.xlsx` when published (`prsalesreports.html`) |
| KS-1700 city RST inventory for all 20 Sedgwick cities | Combined-rate map; Wichita 0% primary print | KDOR KS-1700 / city-county rate publication |
| 2025 in-force CID/TDD inventory | Combined 8.5–10.5% class; CF-SED-008 residual | KDOR notices; city ordinances |
| Line-item bridge ACFR PT $241,512,296 ↔ components | CF-SED-001 numerical bridge | Treasurer collection report + ACFR note |
| PVD vs mill-sheet AV difference **$2,042,762** | CF-SED-002 | PVD / Clerk certification timing note |
| Wichita KDOR vs ACFR residual **$1,574,796.26** | CF-SED-008 | City ACFR note + KDOR city line / CID |
| Other USD ACFRs (260, 261, 265, 266, joint 385/375, etc.) | School-finance ecosystem | Each USD ACFR |
| Joint-city / joint-USD out-of-county AV | Boundary completeness | Adjacent-county mill sheets |
| Food-local stacking legal rule | County 1% / CID on food after 1 Jan 2025 | K.S.A. 12-189 / 79-3603d / KDOR notice |
| Transient guest / lodging receipts | D01-013 Sedgwick instance | KDOR / city lodging reports |
| Domain 03 local incomplete surface | Statewide gap, not closed here | Later Domain 03 residual CWC |

CWC-CE-148 gaps **closed by CWC-CE-150 primary retrieval:** CY2023–2025 state S/U; FY2024–FY2025 state sales-only; FY2025 local S/U; CY2025 countywide 1% sales pool; Wichita 12-192 dollars (WD-BILL-A-092 / 093). **Not** converted into Future-State design.

---

# 3. Mapping to open UQ-TR questions (do **not** close)

| UQ | This CWC’s Current-State input | Still open |
|---|---|---|
| UQ-TR-001 senior eligibility | No senior count, age screen, or homestead inventory executed | **OPEN** |
| UQ-TR-002 sufficiency definition | Current collections mapped as **inputs**, not as the test | **OPEN** |
| UQ-TR-003 ARR | Explicitly **not** last year’s revenue; no ARR computed | **OPEN** |
| UQ-TR-004 5%/5% relationship | 6.5% **not** compared to 5% for savings/sufficiency | **OPEN** |
| UQ-TR-005 local envelope | Functions observed; envelope **not** assigned | **OPEN** |
| UQ-TR-006 USD treatment | PVD school share 43.18% is Current-State **levy** share, not assignment | **OPEN** |
| UQ-TR-007 intergovernmental flows | Architecture in WD-BILL-A-088 | **OPEN** |
| UQ-TR-008 debt | County GO/SA/revenue stocks observed | **OPEN** |
| UQ-TR-009 special assessments | $5.0M SA debt with gov commitment observed | **OPEN** |
| UQ-TR-010 ALL-OUT architecture | Not designed | **OPEN** |
| UQ-TR-011 Sedgwick scope | **First Current-State mapping executed** for the governmental fiscal ecosystem affecting taxpayers within Sedgwick County. Exact remaining entity-depth is still a Human/execution question (gaps in §2). This CWC does **not** close UQ-TR-011 as a Human decision | **OPEN** (role executed in part; not closed) |
| UQ-TR-012 no-double-dip formula | Not invented | **OPEN** |

UQ-CTS-001–016 remain **open** (WD-BILL-A-069).

---

# 4. Future-State **input requirements** (not design)

A later Human-authorized Future-State engineering CWC will still need, at minimum:

1. Authoritative KDOR county-of-sale and local-distribution series (CY and FY separately).  
2. A clean property-tax levy ↔ collection ↔ GAAP bridge for County and material cities/USDs.  
3. Function-level **authority** review (constitutional/statutory), not merely ACFR expense labels.  
4. Intergovernmental netting rules so state aid is not double-counted into ARR.  
5. Debt and special-assessment legal treatment once property tax = zero.  
6. Senior eligibility definition (Human).  
7. Rate architecture under provisional 5%/5% **ceilings** — calculation **not** performed here.  
8. Confirmation that current Kansas RST/use is **not** the H.R. 25 Future State.

These are **requirements to gather/decide later**. They are **not** Bill A rates, ARR, sufficiency, or distribution formulas.

---

# 5. Confirmation of firewalls

| Item | Status after this CWC |
|---|---|
| Future-State design | **NOT DESIGNED** |
| Bill A state/local/combined rate | **NOT CALCULATED** |
| Replacement revenue / ARR / sufficiency | **NOT CALCULATED** |
| No-double-dip formula | **NOT DESIGNED** |
| USD/county/city Future-State allocation | **NOT ASSIGNED** |
| Senior savings | **NOT CALCULATED** |
| H.R. 25 | **PRESERVED** (current KS S/U ≠ FairTax-style Future State) |
| 5% + 5% | **CEILINGS ONLY** |
| CWC-CE-149 | **PASS** (canonicalize CWC-CE-148 map); SHA `f8bc930c8fe16a394123076dc155b6035d838f87` |
| CWC-CE-150 | **EXECUTED** (evidence-gap closure; WD-BILL-A-092–096) |
| CWC-CE-151 | **NOT CREATED** |
| Maturity | **19% UNCHANGED** |
| HG-D1 / SPEC / HG-D2 | **NOT PASSED / NONE / NOT PASSED** |
| Overlap map | **DEFERRED / NOT CREATED** — Sedgwick County Government Overlap Map — deferred until completion of all other Bill A LOU research and Definition activities |

---

Libertas sine lapsu — Liberty without drift.
