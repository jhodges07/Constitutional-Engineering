# WD-BILL-A-088 — Sedgwick Revenue-Universe Crosswalk, Intergovernmental Flows, and Double-Count Controls

**Document ID:** WD-BILL-A-088  
**Source ID:** SRC-BILL-A-319  
**Governing Work Card:** CWC-CE-148  
**Status:** WORKING / CURRENT-STATE OBSERVATION — KRU ROWS PRESERVED — NOT ACCEPTED  
**Version:** 1.0.0  
**Retrieval date:** 2026-09-04  

```text
SEDGWICK OBSERVATION ≠ STATEWIDE COUNT CHANGE
FIELD 25 REMAINS BLANK
FIELD 26 REMAINS NOT DETERMINED
14 / 16 / 5 / 5 / 18 / 14 = 72 PRESERVED
72 ≠ 72 RETAINED CLAIMS
UNIVERSE NOT CERTIFIED
KLRS NOT CERTIFIED
STATE AID → USD IS BOTH USD REVENUE AND STATE SPENDING
COUNTYWIDE 1% POOL ≠ COUNTY SHARE + CITY SHARES ADDED A SECOND TIME
```

Master: WD-BILL-A-082. Sales/use: WD-BILL-A-087. Property tax: WD-BILL-A-084. USDs: WD-BILL-A-085.

This file **observes** Sedgwick Current-State instances of existing KRU claim-category rows. It does **not** add, delete, or re-count statewide rows.

---

# 1. Domain 02 — property claims (observed in Sedgwick)

| KRU ID | Claim class | Sedgwick observation | Status |
|---|---|---|---|
| KRU-D02-001 | Ad valorem property tax (general architecture) | Countywide PVD tax **$878,232,443** (tax year 2025) | **OBSERVED** |
| KRU-D02-002 | USD 20-mill general fund | Mill sheet 20.000 all listed USDs | **OBSERVED** |
| KRU-D02-003 | USD supplemental general / LOB | Variable mills (e.g. USD 259 block) | **OBSERVED** (column pairing EVIDENCE REQUIRED) |
| KRU-D02-004 | USD capital outlay | Variable, typically ≤8 mills | **OBSERVED** |
| KRU-D02-005 | Bond and interest (USD/county/city) | County Bond & Interest 1.654; USD/city B&I variable | **OBSERVED** |
| KRU-D02-006 | County general / dedicated county mills | TOTAL COUNTY **27.567** (GF 23.222 + roads 0.861 + WSU 1.500 + aging 0.330 + B&I 1.654) | **OBSERVED** |
| KRU-D02-007 | City ad valorem | Wichita city total **32.340**; other cities variable | **OBSERVED** |
| KRU-D02-008 | Township ad valorem | PVD township class **$7.52M**; mills ~3–16 | **OBSERVED** |
| KRU-D02-009 | Fire district | Fire mill **16.754** on fire AV **$1.41B**; PVD fire tax **$23.66M** | **OBSERVED** |
| KRU-D02-010 | State education building 1.000 mill | TOTAL STATE 1.500 includes this | **OBSERVED** |
| KRU-D02-011 | State institutional building 0.500 mill | Same | **OBSERVED** |
| KRU-D02-012 | Motor-vehicle in-lieu | County Q4 GF **$18,146,020** (2025) — not inside PVD $878.2M | **OBSERVED** at county GF |

Cemetery / drainage / improvement / library / watershed / rec commission / TIF mills: **OBSERVED as mill-sheet classes** (WD-BILL-A-083). Per-row Domain 02 vs Domain 06 classification remains as statewide: **CLASSIFICATION REQUIRED** where mixed.

Oil and gas: PVD 0.02% — **POTENTIALLY APPLICABLE / SMALL**.

---

# 2. Domain 04 — sales/use (observed in Sedgwick)

| KRU ID | Claim class | Sedgwick observation | Status |
|---|---|---|---|
| KRU-D04-001 | State retailers’ sales tax 6.5% | Architecture **VERIFIED**. Human CY/FY dollar leads **EVIDENCE REQUIRED** (WD-BILL-A-087) | Architecture **OBSERVED**; quantities **EVIDENCE REQUIRED** |
| KRU-D04-002 | State compensating use tax 6.5% | Distinct from sales. Human CY totals described as sales **and** use; FY “sales only” described as excluding use | Architecture **OBSERVED**; split quantities **EVIDENCE REQUIRED** |
| KRU-D04-003 | City/county RST | Countywide **1.0%** voter 1985 **VERIFIED**. Wichita municipal RST **0%**. Other city RST **EVIDENCE REQUIRED** (KS-1700) | Countywide **OBSERVED**; city inventory incomplete |
| KRU-D04-004 | Local compensating use | Counterpart where local sales imposed | Architecture **OBSERVED** |
| KRU-D04-005 | CID / TDD / STAR overlays | Class **OBSERVED**; 2025 in-force inventory **EVIDENCE REQUIRED** | Class **OBSERVED** |

Food-tax phaseout (79-3603d) is a **rate treatment inside KRU-D04-001**, not a new counted row.

---

# 3. Other domains (Sedgwick observation only)

| Domain / KRU | Observation | Status |
|---|---|---|
| D01 KRU-D01-013 transient guest | Potentially applicable (lodging in Wichita/county) | **POTENTIALLY APPLICABLE** — Sedgwick receipts **EVIDENCE REQUIRED** |
| D03 local 12-1,101 / related | Local earnings/privilege inventory incomplete statewide | **INCOMPLETE** — not closed by this CWC |
| D05 (fees/licenses) | County Code Inspection business-type; city licenses | Architecture **OBSERVED**; inventory **not executed** as Domain 05 re-audit |
| D06 001 / 007 / 008 / 014 | Special assessments; improvement districts; TIF-adjacent; stormwater/TUF class | **POTENTIALLY APPLICABLE**. County YE 2025 special-assessment debt with governmental commitment **$5.0M** (WD-BILL-A-089) |
| D07 fines | County Q4 GF Fines & Forfeitures **$56,811** | **OBSERVED locally only**. Statewide Domain 07 **NOT EXECUTED** |

No KRU row count is changed.

---

# 4. Intergovernmental flows (architecture)

```text
TAXPAYER
 → COUNTY TREASURER (ad valorem / in-lieu) → COUNTY / CITY / USD / TOWNSHIP / SPECIAL
 → RETAILER / MARKETPLACE → KDOR → STATE RETENTION (6.5%) AND/OR LOCAL DISTRIBUTION (1% + city/CID)
STATE
 → USD (BASE / LOB aid / special education / capital / bond aid)
 → COUNTY (KDADS / KDHE operating grants; other)
FEDERAL
 → USD / COUNTY (restricted grants)
```

**Who imposes ≠ who collects ≠ who receives ≠ who spends.**

Economic incidence: **NOT DETERMINED.**

---

# 5. Double-count controls (mandatory)

Do **not** add:

1. PVD countywide **$878.2M** + County ACFR property taxes **$241.5M** (the ACFR line is a **recipient subset** of a different basis).  
2. PVD UNFD **$379.2M** + USD 259 ACFR property taxes **$132.3M** (USD 259 is one district; GAAP ≠ levy; school FY ≠ tax year).  
3. Countywide 1% pool (**>$121M lead**) + County share **$41.8M** + city shares (the $41.8M **is** the County piece of the pool).  
4. State Sedgwick-sourced RST/use (**$824.3M lead**) + local 1% + city RST as if they were one recipient’s revenue. State 6.5% is **state** revenue.  
5. USD 259 total revenues **$874.0M** + state aid inside that total, then again as state expenditure, as a single “Sedgwick cost.”  
6. County primary-government revenues **$539.2M** + USD + cities as an ecosystem total (unlike years; transfers; debt proceeds).  

**NO AGGREGATED “SEDGWICK GOVERNMENT COSTS $X” IS CLAIMED.**

---

# 6. Future-State firewall

Observation of a KRU row in Sedgwick does **not**:

- fill Field 25;  
- change Field 26;  
- assign USD, county, or city Future-State shares;  
- convert current collections into AUTHORIZED REVENUE REQUIREMENT.

UQ-TR-007 (intergovernmental flows) remains **open**. This file supplies Current-State **architecture input**, not a formula.

---

Libertas sine lapsu — Liberty without drift.
