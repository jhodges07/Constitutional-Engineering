# WD-BILL-A-090 — Sedgwick Current-State Gaps, Conflicts, Unknowns, and Future-State Input Requirements

**Document ID:** WD-BILL-A-090  
**Source ID:** SRC-BILL-A-321  
**Governing Work Card:** CWC-CE-148  
**Status:** WORKING / GAP REGISTER — NOT FUTURE-STATE DESIGN — NOT ACCEPTED  
**Version:** 1.0.0  
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
| CF-SED-001 | County ACFR property taxes **$241.5M** vs PVD county district **$206.0M** | **UNRESOLVED** — bridge EVIDENCE REQUIRED |
| CF-SED-002 | PVD taxable value **$7,548,699,392** vs mill-sheet county AV **$7,546,656,630** | **UNRESOLVED** (small) |
| CF-SED-003 | County ACFR sales taxes **$41.8M** vs Q4 budgetary **$41,127,614** | **UNLIKE BASES** (GAAP vs budgetary / lag) — both County-share series |
| CF-SED-004 | Human **>$121M** countywide 1% vs Human **~$145M** KDOR local sales+use | **UNRESOLVED** — do not force (WD-BILL-A-087) |
| CF-SED-005 | Human Wichita **nearly $7M** vs implied city remainder of a ~$121M pool after $41.8M County share | **UNRESOLVED / EVIDENCE REQUIRED** |
| CF-SED-006 | USD 259 ACFR revenues **$874.0M** vs news/budget **~$1.01B / ~$1.32B** | **UNLIKE QUANTITIES** |
| CF-SED-007 | KU taxable-sales method (collections ÷ 6.5%) vs food-phaseout non-uniform rate | **METHOD CONFLICT** — KU not used to verify Human CY tax totals |

Year-to-year sales-tax change explanations (food phaseout; NCAA; retail growth; post-pandemic normalization): **HYPOTHESES / EVIDENCE LEADS**, not proven causation.

---

# 2. Evidence required (material)

| Gap | Why it matters | Suggested primary source |
|---|---|---|
| KDOR county-of-sale CY2023–2025 state sales **and** use line items | Human $824.3 / $820.2 / $833.9M | `https://ksrevenue.gov/prsalesreports.html` annual/monthly county files |
| KDOR FY2024–FY2025 state **sales-only** county totals | Human $644.2 / $666.5M; use-tax exclusion | KDOR *State Sales Tax Collections by County* |
| KDOR city/county local distribution FY2025 sales **and** use | Human $118.4M + $26.7M ≈ $145M | KDOR local distribution reports |
| KDOR countywide 1% CY/FY distribution total | Human >$121M | KDOR countywide sales-tax distribution PDF |
| KS-1700 city RST inventory for all 20 Sedgwick cities | Combined-rate map; Wichita 0% primary print | KDOR KS-1700 / city-county rate publication |
| 2025 in-force CID/TDD inventory | Combined 8.5–10.5% class | KDOR notices; city ordinances |
| Wichita ACFR-scale fiscal map | Municipal property tax, fees, enterprises, 12-192 share | City of Wichita ACFR |
| Exact Wichita 12-192 dollar share | Human ~$7M conflict | KDOR distribution + city CAFR |
| Line-item bridge ACFR PT $241.5M ↔ PVD $206.0M | Quantity-type control | County ACFR note + treasurer collection report |
| Other USD ACFRs (260, 261, 265, 266, joint 385/375, etc.) | School-finance ecosystem | Each USD ACFR |
| Joint-city / joint-USD out-of-county AV | Boundary completeness | Adjacent-county mill sheets |
| Food-local stacking legal rule | County 1% / CID on food after 1 Jan 2025 | K.S.A. 12-189 / 79-3603d / KDOR notice |
| Transient guest / lodging receipts | D01-013 Sedgwick instance | KDOR / city lodging reports |
| Domain 03 local incomplete surface | Statewide gap, not closed here | Later Domain 03 residual CWC |

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
| CWC-CE-149 | **NOT CREATED** |
| Maturity | **19% UNCHANGED** |
| HG-D1 / SPEC / HG-D2 | **NOT PASSED / NONE / NOT PASSED** |

---

Libertas sine lapsu — Liberty without drift.
