# WD-BILL-A-087 — Sedgwick Sales/Use Tax Current-State Map and Human-Lead Verification

**Document ID:** WD-BILL-A-087  
**Source ID:** SRC-BILL-A-318  
**Governing Work Card:** CWC-CE-148 (supplemental Human evidence input; **not** CWC-CE-149)  
**Status:** WORKING / EVIDENCE VERIFICATION — NOT A BILL A RATE — NOT ACCEPTED  
**Version:** 1.0.0  
**Retrieval date:** 2026-09-04  

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
| CY2025 **$824.3M** | State sales **and** use collected from Sedgwick / county of sale | Controlling KDOR county-of-sale **annual** PDF not retrieved (report index exists at `ksrevenue.gov/prsalesreports.html`; direct PDF URL 404 in this cycle). KU Abstract compiles **taxable sales** from KDOR using **collections ÷ 6.5%**, which is **invalid as a uniform converter during food phaseout**. | **EVIDENCE REQUIRED** |
| CY2024 **$820.2M** | Same | Same | **EVIDENCE REQUIRED** |
| CY2023 **$833.9M** | Same | Same | **EVIDENCE REQUIRED** |
| State rate 6.5% | General rate | VERIFIED (79-3603; KDOR AR25). **Not** all transactions at 6.5% (food phaseout). | **VERIFIED** as general rate; **not** as uniform effective rate |
| FY2025 **$644.2M** state **sales only** | Excludes local; Human: excludes use | KDOR monthly *State Sales Tax Collections by County* files exist; this CWC did **not** sum 12 months. KU 2025 Sedgwick **nominal taxable sales $9,996.5 million** (CY, compiled) × 6.5% = **$649.8 million** — **order-of-magnitude only**, methodologically flawed, **CY not FY**. | **EVIDENCE REQUIRED** (do not treat $649.8M as verification of $644.2M) |
| FY2024 **$666.5M** state sales only | Same | Same | **EVIDENCE REQUIRED** |
| Countywide 1% voter 1985 | Architecture | VERIFIED in County ACFR/Q4 | **VERIFIED** |
| Kansas collects and distributes to county + cities | Architecture | VERIFIED K.S.A. 12-192; KDOR FAQ | **VERIFIED** |
| 2025 countywide 1% **> $121 million** | Pool | Wichita Eagle (secondary) matches Human wording. **No KDOR CY2025 countywide distribution PDF in hand.** County share $41.8M is **consistent with** a ~$120M pool if County receives ~1/3 under 12-192, **but that arithmetic is not a verification**. | **PARTIALLY VERIFIED** (secondary + consistency); **primary KDOR total EVIDENCE REQUIRED** |
| County gov share 2025 **$41.8M** | County receipts | County ACFR: Sales taxes **$41.8 million** (2025). Narrative: countywide 1% retail sales **and use**. | **VERIFIED** (GAAP millions; County FY/CY 2025) |
| County gov share 2024 **$39.6M** | County receipts | ACFR **$39.6 million** | **VERIFIED** |
| Q4 cash/budgetary 2025 **$41,127,614** vs 2024 **$39,192,136** | County collections | County Q4 report. Two-month State disbursement lag noted. | **VERIFIED** as Q4 budgetary series; **≠** ACFR $41.8M |
| Wichita 2025 **nearly $7 million** | Human: Wichita share | Eagle repeats Human. **In tension** with (a) “Wichita more than half of city share” if city share ≈ pool − $41.8M, and (b) Wichita being the largest city. Possible distinct stream (GF half of Wichita’s 12-192 share; a subset; error). | **EVIDENCE REQUIRED** — **not** inferred |
| FY2025 local KDOR sales **$118.4M** + use **$26.7M** ≈ **$145M** | County + cities distributions | KDOR City/County annual distribution reports exist; **not totaled from primary file in this CWC**. | **EVIDENCE REQUIRED** |
| **$121M+ vs ~$145M** | Reconciliation | **Not resolved by assumption.** Candidate causes: CY vs FY; countywide 1% vs **all** local (city + CID + use); sales vs sales+use; recipient scope; lag/adjustments. | **UNRESOLVED** |

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
