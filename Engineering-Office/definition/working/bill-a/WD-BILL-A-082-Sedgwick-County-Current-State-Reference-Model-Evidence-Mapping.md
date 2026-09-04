# WD-BILL-A-082 — Sedgwick County Current-State Reference-Model Evidence Mapping (Master)

**Document ID:** WD-BILL-A-082  
**Title:** Sedgwick County Current-State Reference-Model Evidence Mapping — Master Control  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-148 (active); supplemental Human sales/use evidence leads (same CWC; not CWC-CE-149)  
**Canonical starting SHA:** `d58a98c7a8278596ed4704fc9ddfca33cb8ae381`  
**Governing LOU candidate:** LOU-004 Draft 1.10 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / CURRENT-STATE EVIDENCE MAP — NOT ACCEPTED — FUTURE STATE NOT DESIGNED  
**Version:** 1.0.0  
**Effective Date:** 2026-09-04  
**Retrieval date:** 2026-09-04  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-082-Sedgwick-County-Current-State-Reference-Model-Evidence-Mapping.md  
**Source ID:** SRC-BILL-A-313  

**Companions:** WD-BILL-A-083 (entities/jurisdictions); WD-BILL-A-084 (property tax); WD-BILL-A-085 (USD/school finance); WD-BILL-A-086 (county/city/township/specials); WD-BILL-A-087 (sales/use + Human-lead verification); WD-BILL-A-088 (Universe crosswalk / flows / double-count); WD-BILL-A-089 (debt / assessments / functions); WD-BILL-A-090 (gaps / Future-State inputs); WD-BILL-A-091 (Git handoff).

```text
CURRENT STATE FIRST
EVIDENCE-FIRST
NOT FUTURE-STATE DESIGN
SEDGWICK ≠ STATEWIDE DEFAULT / RATE / TEMPLATE
SEDGWICK COUNTY GOVERNMENT ≠ THE ENTIRE ECOSYSTEM
CURRENT REVENUE ≠ REQUIRED FUTURE REVENUE
CURRENT SPENDING ≠ AUTHORIZED FUTURE SPENDING
HISTORICAL COLLECTION ≠ FUTURE ENTITLEMENT
DEPENDENCY ≠ RETAIN
PROPERTY TAX ≠ SPECIAL ASSESSMENT
CURRENT KANSAS SALES/USE TAX ≠ H.R. 25
CEILING ≠ TARGET
5% + 5% ≠ GUARANTEED 10%
NO RATE CALCULATION
NO ARR DETERMINATION
NO SUFFICIENCY CALCULATION
NO NO-DOUBLE-DIP FORMULA
NO SENIOR ELIGIBILITY
NO DISTRIBUTION ASSIGNMENT
DOMAIN 07 STATEWIDE AUDIT NOT EXECUTED
NO COMMIT / NO PUSH
```

This file is the **controlling master** for CWC-CE-148 Current-State evidence mapping. CWC-CE-146 Human Intent in WD-BILL-A-078 remains controlling for the *role* of Sedgwick as initial reference model. This CWC **executes Current-State evidence mapping**. It does **not** design the Future State.

---

# 1. CYCLE IDENTITY

| Field | Value |
|---|---|
| Cycle | CWC-CE-148 |
| Cycle type | **CURRENT-STATE EVIDENCE MAPPING** — first execution stage of the Sedgwick reference model |
| Canonical starting HEAD | `d58a98c7a8278596ed4704fc9ddfca33cb8ae381` (CWC-CE-147) |
| Supplemental input | Human-supplied sales/use evidence leads — **not auto-verified**; investigated in WD-BILL-A-087 |
| Domain 01–06 | **PRESERVED** 14 / 16 / 5 / 5 / 18 / 14 = **72**; Field 25 **BLANK**; Field 26 **NOT DETERMINED** |
| Domain 07 statewide | **NOT EXECUTED** (local fines observed as Current-State evidence only) |
| Q-BILL-A-006 | **NOT ISSUED** |
| Bill A maturity | **19% UNCHANGED** |

---

# 2. BOUNDARY

**Reference-model boundary:** the governmental fiscal ecosystem affecting taxpayers **within Sedgwick County, Kansas**.

**Not** merely Sedgwick County government.

**Sedgwick** is an engineering example / initial reference model.

```text
SEDGWICK ≠ STATEWIDE DEFAULT
SEDGWICK ≠ STATEWIDE RATE
SEDGWICK ≠ AUTOMATIC TEMPLATE RESULT
SEDGWICK FISCAL RESULTS ≠ AUTHORITY TO GENERALIZE TO ALL 105 COUNTIES
```

---

# 3. METHODOLOGY

Order executed:

```text
CURRENT STATE → VERIFIED EVIDENCE → CONTROLLED MAPPING → GAPS / CONFLICTS / UNKNOWNS
```

Source hierarchy: Kansas statutes / Revisor; KDOR; PVD; KSDE (via USD ACFR / mill sheet); Sedgwick County ACFR and mill-levy sheet; USD 259 ACFR; county GIS / official municipality-USD list. Secondary sources (KU Statistical Abstract compilations; Wichita Eagle) may **assist discovery** and are **not** used to override primary evidence.

Evidence statuses used: **VERIFIED**; **PARTIALLY VERIFIED**; **EVIDENCE REQUIRED**; **LEGAL RESEARCH REQUIRED**; **CLASSIFICATION REQUIRED**; **NOT APPLICABLE**; **NOT DETERMINED**.

Human-supplied figures remain **HUMAN EVIDENCE LEADS** until independently verified.

No quantity was guessed. Incompatible periods were not silently combined. No implied tax base was calculated from the 6.5% rate.

---

# 4. TEMPORAL CONTROL

| Calendar | Use in this package |
|---|---|
| **CY / tax year 2025** | PVD ad valorem summary; mill-levy sheet; countywide 1% architecture as levied |
| **County fiscal year ended 31 Dec 2025** | Sedgwick County ACFR; County Q4 financial report |
| **USD fiscal year ended 30 Jun 2025** | USD 259 ACFR |
| **Kansas state fiscal year (1 Jul–30 Jun)** | Human FY2025 sales-tax leads; **not independently totaled from KDOR monthly files in this CWC** |
| **Distribution lag** | County Q4: State disbursements typically occur **two months after purchase date** |

```text
CY2025 ≠ FY2025 ≠ COUNTY FY2025 ≠ USD FY2025
TAX LEVY ≠ TAX COLLECTION ≠ BUDGET AUTHORITY ≠ EXPENDITURE ≠ DEBT ≠ FUND BALANCE ≠ TRANSFER
```

---

# 5. QUANTITY-TYPE CONTROL (NO FALSE TOTAL)

No single “Sedgwick government costs $X” number is claimed.

Conditions for an aggregated total are **not met**: unlike fiscal years (county CY vs USD FY vs state FY); intergovernmental transfers (state aid → USD); overlapping taxpayers; debt proceeds distinct from operating revenue; city/USD/county ACFRs not consolidated.

**NO AGGREGATED TOTAL SHALL BE CLAIMED.**

---

# 6. COLLECTION ARCHITECTURE (CONCEPT)

Where evidence permits, distinguish:

```text
TAXABLE EVENT
→ LEGAL TAX CLAIM
→ COLLECTION MECHANISM
→ STATE COLLECTION (KDOR / county treasurer as applicable)
→ STATE RETENTION AND/OR LOCAL DISTRIBUTION
→ GOVERNMENTAL RECIPIENT
→ GOVERNMENTAL FUNCTION
```

Statutory remitter ≠ economic incidence. **ECONOMIC INCIDENCE: NOT DETERMINED.**

---

# 7. FIREWALLED CONCLUSIONS (THIS CWC)

| Item | Status |
|---|---|
| Future-State design | **NOT DESIGNED** |
| ARR | **NOT DETERMINED** (UQ-TR-003 remains open; Current-State is an **input**) |
| Revenue sufficiency | **NOT CALCULATED** |
| No-double-dip formula | **NOT DESIGNED** |
| Senior eligibility / savings | **NOT DETERMINED / NOT CALCULATED** |
| 5% / 5% | **PROVISIONAL PLANNING CEILINGS ONLY** — not compared to 6.5% for savings/sufficiency |
| Bill A rates / replacement revenue / local distribution / USD future share | **NOT CALCULATED / NOT ASSIGNED** |
| H.R. 25 | **PRESERVED** — current Kansas sales/use ≠ Bill A FairTax-style Future State |

---

# 8. WHAT THIS PACKAGE MAPS

See companions. Completeness of this first execution stage: **SUBSTANTIALLY COMPLETE FOR ARCHITECTURE WITH EXPLICIT GAPS** (WD-BILL-A-090). Not every minor entity is enumerated. Material fiscal architectures are not silently omitted.

---

Libertas sine lapsu — Liberty without drift.
