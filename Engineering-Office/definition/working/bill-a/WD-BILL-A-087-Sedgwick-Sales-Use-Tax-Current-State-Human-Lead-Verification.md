# WD-BILL-A-087 — Sedgwick Sales/Use Tax Current-State Map and Human-Lead Verification

**Document ID:** WD-BILL-A-087  
**Source ID:** SRC-BILL-A-318  
**Governing Work Card:** CWC-CE-148 (architecture); **CWC-CE-150** (primary KDOR verification of Human leads)  
**Status:** WORKING / EVIDENCE VERIFICATION — NOT A BILL A RATE — NOT ACCEPTED  
**Version:** 1.1.0  
**Retrieval date:** 2026-09-04  

**CWC-CE-150:** Human-lead quantity cells below are updated from primary KDOR workbooks. Detailed provenance: WD-BILL-A-092 / WD-BILL-A-093. Architecture in §§1–2 is **preserved**. Do not treat verified Current-State collections as Bill A targets.  

```text
HUMAN-SUPPLIED FIGURES = EVIDENCE LEADS UNTIL INDEPENDENTLY VERIFIED
CURRENT KANSAS SALES/USE ≠ H.R. 25
$824.3M ≠ BILL A REVENUE TARGET
$145M ≠ BILL A LOCAL REQUIREMENT
$121M+ ≠ BILL A COUNTY REQUIREMENT
DO NOT CALCULATE IMPLIED TAX BASE FROM 6.5%
CY ≠ FY
SALES ≠ USE
COUNTYWIDE 1% ≠ ALL LOCAL SALES/USE
COUNTY SHARE ≠ COUNTYWIDE POOL
WICHITA SHARE ≠ ALL WICHITA SALES/USE RECEIPTS
ECONOMIC INCIDENCE NOT DETERMINED
```

Master: WD-BILL-A-082.

---

# 1. Current-State rate architecture (general locations)

| Layer | Rate | Who imposes | Who collects | Who receives | Geographic applicability | Status |
|---|---|---|---|---|---|---|
| State retailers’ sales tax | **6.5%** general (K.S.A. 79-3603) | State | KDOR | State (SGF / SHF split under 79-3620 — **not recalculated here**) | Statewide | VERIFIED architecture |
| State compensating use tax | **6.5%** (K.S.A. 79-3703) | State | KDOR | State | Statewide | VERIFIED architecture |
| Food / food ingredients (state) | **4%** from 1 Jan 2023; **2%** from 1 Jan 2024; **0%** from **1 Jan 2025** (K.S.A. 79-3603d; KDOR AR FY2025) | State | KDOR | State | Statewide qualifying food | VERIFIED |
| Sedgwick countywide retailers’ sales tax | **1.0%** | County (voter 1985) | **KDOR** | Apportioned county **and cities** under **K.S.A. 12-192** | Countywide (cities + unincorporated) | VERIFIED authority + current 1% rate (County ACFR/Q4) |
| Local compensating use counterpart | Matches local sales where imposed (K.S.A. 12-198) | Local via state administration | KDOR | Same recipients as local sales | Where local sales imposed | VERIFIED architecture |
| City of Wichita municipal RST | **0%** | — | — | Wichita still receives **12-192 share** of **countywide** 1% | Wichita general (non-CID) | VERIFIED as combined 7.5% structure (secondary rate tables + County/KDOR FAQ); KS-1700 line **EVIDENCE REQUIRED** as primary print |
| Other cities’ municipal RST | Variable | City | KDOR | City (city tax is **not** 12-192 split) | City limits | EVIDENCE REQUIRED (KS-1700) |
| CID / TDD / STAR overlays | Additional local % | District/city | KDOR | District / pledged use | Defined boundaries | OBSERVED class; 2025 address inventory EVIDENCE REQUIRED |

**Common combined rate (Wichita, non-special district):**

```text
6.5% STATE + 1.0% COUNTYWIDE + 0% CITY = 7.5%
```

**Do not generalize 7.5% to every Sedgwick transaction or location.** CID examples in KDOR April 2026 notices: Wichita SoCe Corner CID combined **9.5%**; Wichita 333 English CID **9%**. Human “approximately 8.5%–10.5%” is a **plausible overlay range**, **PARTIALLY VERIFIED as a class**, not a certified max/min for 2025.

Food: state 0% from 1 Jan 2025 **does not** by itself zero the county 1% or CID levies. **LEGAL RESEARCH REQUIRED** for exact food-local stacking.

---

# 2. Collection vs recipient (countywide 1%)

```text
TAXABLE EVENT (sourced sale / use)
→ CLAIM: countywide 1% RST/use
→ COLLECTION: retailer/marketplace remits to KDOR
→ DISTRIBUTION: State Treasurer per K.S.A. 12-192
→ RECIPIENTS: Sedgwick County government AND each city in the county
→ COUNTY USE (of County share): ~50% roads/bridges (incl. $1.6M bond-and-interest pledge) / ~50% GF
```

**K.S.A. 12-192(a) formula (general counties):**  
½ of revenue apportioned by **prior-year tangible property-tax levies**; ½ by **population**. Exception freeze on levy-based apportionment change **1 Jul 2025 – 31 Dec 2026**. Johnson County special rules **N/A**. Certain pledged special county taxes remitted 100% to county under 12-192(d) — **Sedgwick 1% general is the 12-192(a) path** per County documents.

KDOR FAQ: city-imposed tax → city receives **actual city tax collected**; countywide general tax → formula split.

---

# 3. Human-supplied leads — verification table

| Lead | Human description | Independent finding | Status |
|---|---|---|---|
| CY2025 **$824.3M** | State sales **and** use collected from Sedgwick / county of sale | KDOR monthly county files: CY2025 sales **$649,772,028.02** + use **$174,486,404.74** = **$824,258,432.76**. Annual revised CY2025 workbook **not published**. | **VERIFIED** (monthly official files; WD-BILL-A-092) |
| CY2024 **$820.2M** | Same | `cy24revised.xlsx` Combined CY **$654,923,412.48** + `cy24reviseduse.xlsx` CY **$165,282,890.34** = **$820,206,302.82** | **VERIFIED** |
| CY2023 **$833.9M** | Same | `cy23revised.xlsx` Combined CY **$681,347,500.29** + `cy23reviseduse.xlsx` CY **$152,562,187.24** = **$833,909,687.53** | **VERIFIED** |
| State rate 6.5% | General rate | VERIFIED (79-3603; KDOR AR25). **Not** all transactions at 6.5% (food phaseout). | **VERIFIED** as general rate; **not** as uniform effective rate |
| FY2025 **$644.2M** state **sales only** | Excludes local; Human: excludes use | `062025coll.xlsx` Sedgwick FY2025 **$644,157,207.05**. **Not** use; **not** CY. | **VERIFIED** (rounding) |
| FY2024 **$666.5M** state sales only | Same | Same workbook, FY2024 **$666,509,001.27** | **VERIFIED** (rounding) |
| Countywide 1% voter 1985 | Architecture | VERIFIED in County ACFR/Q4 | **VERIFIED** |
| Kansas collects and distributes to county + cities | Architecture | VERIFIED K.S.A. 12-192; KDOR FAQ; KDOR countywide city/county rows | **VERIFIED** |
| 2025 countywide 1% **> $121 million** | Pool | `cy2025salescitiesco.xlsx` parent Sedgwick County CY sales **$121,665,410.28**. **Sales only**; **not** use; **not** FY. | **VERIFIED** |
| County gov share 2025 **$41.8M** | County receipts | County ACFR sales taxes **$41,840,210**. KDOR CY2025 Balance of County S+U **$41,127,613.64** (= Q4 **$41,127,614**). | **VERIFIED** (GAAP millions); Q4/KDOR are **unlike** GAAP (CF-SED-003) |
| County gov share 2024 **$39.6M** | County receipts | ACFR **$39.6 million** | **VERIFIED** |
| Q4 cash/budgetary 2025 **$41,127,614** vs 2024 **$39,192,136** | County collections | County Q4 report. Matches KDOR Balance of County CY2025 S+U. Two-month State disbursement lag noted. | **VERIFIED** as Q4/KDOR series; **≠** ACFR $41,840,210 |
| Wichita 2025 **nearly $7 million** | Human: Wichita share | KDOR CY2025 Wichita countywide sales **$69,575,997.23**; S+U **$85,253,695.74**. Wichita ACFR local sales tax **$86,828,492**. | **HUMAN LEAD: NOT VERIFIED / CONTRADICTED** |
| FY2025 local KDOR sales **$118.4M** + use **$26.7M** ≈ **$145M** | County + cities distributions | FY2025 local sales **$118,366,941.10** + use **$26,688,022.13** = **$145,054,963.23**. Scope = **countywide 1%** parent row (County + cities). | **VERIFIED** as that scope |
| **$121M+ vs ~$145M** | Reconciliation | **$121.7M** = CY2025 countywide **sales**; **$145.1M** = FY2025 countywide **sales+use**. Unlike period and tax type. | **CLOSED as unlike quantities** (CF-SED-004) |

**Do not compare CY state S&U totals with FY state sales-only totals without a period/scope bridge.**

---

# 4. Compiled KU taxable-sales (secondary / method caveat)

KU Institute for Policy & Social Research, *Taxable Retail Sales in Kansas, by County, 2024–2025* (`7bus14.pdf`), source note: KDOR Sales Tax Collections by County.

Sedgwick **nominal** taxable sales: **$11,136.5 million (2024)**; **$9,996.5 million (2025)** (−10.2%).

Method: collections ÷ **state sales tax rate**. **During food phaseout this overstates/understates the true tax base.** Use as **discovery only**. **Not** used to verify $824.3M (which is tax, not base, and includes use if Human description is correct).

Year-to-year decline **shall not** be attributed solely to food-tax phaseout without a KDOR decomposition. NCAA / retail-growth / post-pandemic explanations in County ACFR/Q4 are **County-stated hypotheses** for **County 1% receipts**, not proven statewide causation.

---

# 5. Double-count / Future-State input

- State 6.5% collections sourced to Sedgwick are **state revenue**, not County/USD revenue.  
- Countywide 1% is **one tax** split among County + cities — do not add County $41.8M + city shares + $121M pool.  
- City-imposed RST (where any) is **additional** to the 1%.  
- CID/TDD is **additional** and typically **pledged**.  
- **$824.3M is not a Bill A target. $145M is not a Bill A local requirement.**

No 5% revenue, combined 10%, or FairTax rate was calculated. No mechanical comparison of 6.5% to the provisional 5% ceiling for savings/sufficiency.

---

Libertas sine lapsu — Liberty without drift.
