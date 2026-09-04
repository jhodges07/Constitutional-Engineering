# WD-BILL-A-095 — Remaining Gaps, Fiscal-Period Reconciliation, and Bounded Controls

**Document ID:** WD-BILL-A-095  
**Source ID:** SRC-BILL-A-326  
**Governing Work Card:** CWC-CE-150  
**Canonical starting SHA:** `f8bc930c8fe16a394123076dc155b6035d838f87`  
**Status:** WORKING / GAP AND PERIOD CONTROL — NOT FUTURE-STATE DESIGN — NOT ACCEPTED  
**Version:** 1.0.0  
**Retrieval date:** 2026-09-04  

```text
CY2025 ≠ FY2025
COUNTY FY (YE 31 DEC) ≠ USD FY (YE 30 JUN) ≠ KANSAS FY (1 JUL–30 JUN)
TAX YEAR ≠ LEVY YEAR ≠ COLLECTION PERIOD ≠ DISTRIBUTION PERIOD ≠ GAAP PERIOD
WHO COLLECTS ≠ WHO RECEIVES ≠ WHO EXPENDS
NO FALSE TOTAL
NO OVERLAP MAP
```

---

# 1. Fiscal-period reconciliation (verified series)

| Series | Period | Amount | Notes |
|---|---|---|---|
| State sales+use county-of-sale | **CY2023** | $833,909,687.53 | Annual revised |
| State sales+use county-of-sale | **CY2024** | $820,206,302.82 | Annual revised |
| State sales+use county-of-sale | **CY2025** | $824,258,432.76 | Monthly-file construction; annual revised **not published** |
| State **sales only** | **Kansas FY2024** | $666,509,001.27 | June 2025 coll workbook |
| State **sales only** | **Kansas FY2025** | $644,157,207.05 | June 2025 coll workbook |
| Countywide 1% **sales** pool | **CY2025** | $121,665,410.28 | KDOR countywide sales |
| Countywide 1% **sales+use** pool | **CY2025** | $149,080,878.43 | Sales parent + use parent |
| Countywide 1% **sales** | **Kansas FY2025** | $118,366,941.10 | Monthly lo files |
| Countywide 1% **use** | **Kansas FY2025** | $26,688,022.13 | Loc use Jul 2024–Jun 2025 |
| Countywide 1% **sales+use** | **Kansas FY2025** | $145,054,963.23 | Human $145M scope |
| County 12-192 share | **CY2025** KDOR Balance of County S+U | $41,127,613.64 | = Q4 $41,127,614 |
| County sales-tax revenue | **County FY2025** GAAP | $41,840,210 | ACFR |
| Wichita 12-192 | **CY2025** KDOR S+U | $85,253,695.74 | City line |
| Wichita sales taxes | **City FY2025** GAAP (YE 31 Dec) | $86,828,492 | ACFR local sales tax |
| PVD county levy | **Tax year 2025** | $205,980,345.17 | Levy, not ACFR revenue |
| County property-tax revenue | **County FY2025** GAAP | $241,512,296 | Unlike PVD 2025 levy |
| USD 259 revenues | **USD FY2025** (YE 30 Jun) | $874,033,452 | GAAP; unlike budget headlines |

A numerical similarity does **not** establish common scope.

---

# 2. Collection / distribution / recipient

```text
STATE 6.5% (+ food-rate categories): collector KDOR → recipient STATE
COUNTYWIDE 1%: collector KDOR → distributor State Treasurer (12-192)
  → recipients COUNTY GOVERNMENT + CITIES
CITY-IMPOSED RST (where any): collector KDOR → recipient IMPOSING CITY
CID/TDD: collector KDOR → district / pledged use
```

County ACFR $41.8M = **County recipient** (GAAP).  
$121.7M / $145.1M = **pool to County + cities**.  
$824.3M = **state** county-of-sale collections, **not** local government revenue.

---

# 3. Double-count controls (preserved)

Do **not** add:

- state Sedgwick-sourced collections + local collections as “Sedgwick government revenue”;
- countywide pool + County share + city shares;
- state school aid + USD revenue containing that aid;
- levy + collection of that levy;
- County + city + USD + special-district revenue into an ecosystem total without a separately authorized consolidation methodology.

**NO AGGREGATE SEDGWICK TOTAL is stated by this CWC.**

Economic incidence: **NOT DETERMINED**.

---

# 4. Remaining evidence gaps (material)

| Gap | Status |
|---|---|
| KDOR CY2025 **annual revised** state sales/use workbooks (`cy25revised.xlsx` / use) | **EVIDENCE REQUIRED** as the later confirmation copy; monthly construction **VERIFIED** |
| Complete treasurer line-item bridge ACFR PT $241,512,296 ↔ components | **UNRESOLVED** (CF-SED-001) |
| PVD $7,548,699,392 vs mill-sheet $7,546,656,630 | **UNRESOLVED** (CF-SED-002) |
| Wichita KDOR $85,253,695.74 vs ACFR $86,828,492 residual | **UNRESOLVED** (CF-SED-008) |
| KS-1700 2025 city RST inventory for all Sedgwick cities | **EVIDENCE REQUIRED** |
| 2025 in-force CID/TDD address inventory | **EVIDENCE REQUIRED** |
| Food-local stacking after 1 Jan 2025 | **LEGAL RESEARCH REQUIRED** |
| Other USD ACFRs (260, 261, 265, 266, joint districts) | **EVIDENCE REQUIRED** (not this CWC’s audit) |
| Transient guest / lodging Sedgwick instance | **EVIDENCE REQUIRED** |
| Domain 03 local incomplete surface | **EVIDENCE REQUIRED** (statewide; not closed here) |

Unresolved gaps are valid engineering results.

---

# 5. Legal-research requirements (not executed as opinions)

- K.S.A. 12-189 / 79-3603d / KDOR notice: county 1% and CID on food after 1 Jan 2025.
- No change to K.S.A. 12-192 architecture is required by the distribution evidence retrieved.

UQ-TR-001 through UQ-TR-012 and UQ-CTS-001 through UQ-CTS-016 remain **open**. Evidence answers ≠ Human policy decisions.

---

# 6. Controls preserved

| Item | Status |
|---|---|
| LOU-004 | Draft **1.10** / CANDIDATE / **NOT HUMAN-ACCEPTED** |
| HG-D1 | **NOT PASSED** |
| SPEC | **NONE** |
| HG-D2 | **NOT PASSED** |
| Bill A maturity | **19%** |
| Revenue Universe | **NOT CERTIFIED** — D01=14 D02=16 D03=5 D04=5 D05=18 D06=14 **TOTAL 72 arithmetic only** |
| Field 25 | **BLANK** |
| Field 26 | **NOT DETERMINED** |
| KLRS | **NOT CERTIFIED** |
| Domain 07 | **NOT EXECUTED** (fines/penalties in local ACFRs do not authorize Domain 07) |
| Sedgwick Future State | **NOT DESIGNED** |
| Rate / ARR / sufficiency / future distribution / senior savings | **NOT CALCULATED / NOT DETERMINED** |
| 5% + 5% | **PROVISIONAL PLANNING CEILINGS** — ceiling ≠ target; not compared to 6.5% for savings/sufficiency |
| H.R. 25 | **PRESERVED** as Future-State economic reference; current KS S/U ≠ FairTax-style Future State |
| Overlap map | **DEFERRED / NOT CREATED** — “Sedgwick County Government Overlap Map — deferred until completion of all other Bill A LOU research and Definition activities.” |

---

Libertas sine lapsu — Liberty without drift.
