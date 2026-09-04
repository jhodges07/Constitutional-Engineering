# WD-BILL-A-092 — KDOR Sedgwick State and Local Sales/Use Evidence-Gap Closure

**Document ID:** WD-BILL-A-092  
**Source ID:** SRC-BILL-A-323  
**Governing Work Card:** CWC-CE-150  
**Canonical starting SHA:** `f8bc930c8fe16a394123076dc155b6035d838f87`  
**Status:** WORKING / CURRENT-STATE EVIDENCE — NOT A BILL A RATE — NOT ACCEPTED  
**Version:** 1.0.0  
**Retrieval date:** 2026-09-04  

```text
HUMAN-SUPPLIED FIGURES WERE EVIDENCE LEADS
PRIMARY KDOR WORKBOOKS CONTROL WHERE RETRIEVED
DO NOT CALCULATE AN IMPLIED TAX BASE
DO NOT DIVIDE COLLECTIONS BY 6.5% TO INFER A BILL A BASE
CY ≠ FY
SALES ≠ USE
STATE COUNTY-OF-SALE ≠ LOCAL DISTRIBUTION
CURRENT KANSAS SALES/USE ≠ H.R. 25
$824.3M ≠ BILL A REVENUE TARGET
$145M ≠ BILL A LOCAL REQUIREMENT
```

Supersedes the **EVIDENCE REQUIRED** cells in WD-BILL-A-087 §3 for the quantities verified below. Architecture in WD-BILL-A-087 §1–2 is preserved.

Official index: `https://www.ksrevenue.gov/prsalesreports.html`. Files are Excel workbooks under `https://www.ksrevenue.gov/pdf/`, not the guessed PDF paths from CWC-CE-148.

---

# 1. Provenance table — state sales and use (Sedgwick)

| Quantity | Exact amount | Tax type | Period | Sourcing | Gross/net | Food interaction | Report | Location | Status |
|---|---|---|---|---|---|---|---|---|---|
| Human CY2025 **$824.3M** | **$824,258,432.76** (sales **$649,772,028.02** + use **$174,486,404.74**) | State **sales and use** collections | **CY2025** (Jan–Dec 2025 month-of current-year columns summed) | County-of-sale (KDOR county row `Sedgwick`) | Collections as published (refund/adjustment treatment not separately disclosed in the monthly county files) | 2025 state food rate **0%** (K.S.A. 79-3603d). Food at 0% contributes **$0** state collections. Combined collections are **not** all at 6.5%. | KDOR *Monthly State Sales Tax Collections by County* `01`–`12``2025coll.xlsx`; *Monthly State Use Tax Collections by County* `01`–`12``2025colluse.xlsx` | Sedgwick row; month-of current-year column (typically column index 2) | **VERIFIED** from official monthly files. Annual revised workbook `cy25revised.xlsx` / `cy25reviseduse.xlsx` **not published** as of retrieval. |
| Human CY2024 **$820.2M** | **$820,206,302.82** (sales Combined **$654,923,412.48** + use **$165,282,890.34**) | State **sales and use** | **CY2024** Calendar Year column | County-of-sale `Sedgwick` | Calendar Year collections as published | Combined = General + Food. General collections **$624,278,869.64**. Food collections **$30,644,542.84** at the **2%** 2024 food rate. | `pdf/cy24revised.xlsx` sheets Combined / General / Food; `pdf/cy24reviseduse.xlsx` sheet 2024 | Sedgwick row; **Calendar Year** / **CY Total** column | **VERIFIED** |
| Human CY2023 **$833.9M** | **$833,909,687.53** (sales Combined **$681,347,500.29** + use **$152,562,187.24**) | State **sales and use** | **CY2023** | County-of-sale `Sedgwick` | Calendar Year collections as published | Combined = General + Food. General **$624,124,345.69**. Food **$57,223,154.60** at the **4%** 2023 food rate. | `pdf/cy23revised.xlsx` Combined / General / Food; `pdf/cy23reviseduse.xlsx` | Sedgwick row; Calendar Year / CY Total | **VERIFIED** |
| Human FY2025 **$644.2M** state **sales only** | **$644,157,207.05** | State **sales** only (not use) | Kansas **FY2025** = July 2024–June 2025 (file header) | County-of-sale `Sedgwick` | FYTD collections as published | Food phaseout in progress across the FY (0% from 1 Jan 2025). Sales-only FY total is **not** a uniform 6.5% series. | `pdf/062025coll.xlsx` (*June 2025 State Sales Tax Collections by County*) | Sedgwick row; Fiscal Year to Date current-year column | **VERIFIED** (Human $644.2M is rounding) |
| Human FY2024 **$666.5M** state **sales only** | **$666,509,001.27** | State **sales** only | Kansas **FY2024** = July 2023–June 2024 | County-of-sale `Sedgwick` | FYTD collections as published | Food at 4% then 2% during that FY | Same June 2025 workbook, prior-FY column; corroborated by the FYTD prior-year column | Sedgwick row; Fiscal Year to Date prior-year column | **VERIFIED** (Human $666.5M is rounding) |

**Do not add** CY sales+use to FY sales-only. **Do not add** state collections to local distributions.

KDOR annual revised files also contain a **Taxable Sales** column. That column is a KDOR-computed figure using category-specific rates (General ÷ 6.5%; Food ÷ the then-effective food rate). **This CWC does not adopt that column, or any collections÷6.5% quotient, as a Bill A tax base.** See CF-SED-007 in WD-BILL-A-094.

---

# 2. Provenance table — local / countywide distributions

| Quantity | Exact amount | What it is | Period | Recipients in the parent row | Status |
|---|---|---|---|---|---|
| Human FY2025 local sales **~$118.4M** | **$118,366,941.10** | City/County **local sales-tax distributions**, parent row `Sedgwick County` in monthly `*lo.xlsx`. Rate shown **0.01**; commencement **2008-01-01**. This is the **countywide 1% sales** distribution pool (County + cities), **not** Sedgwick County government alone, **not** city-imposed RST as an add-on inside this parent total. | Kansas **FY2025** (Jul 2024–Jun 2025), summing each file’s current-year month amount | County government + cities of Sedgwick County under the countywide 1% | **VERIFIED** (Human $118.4M is rounding) |
| Human FY2025 local use **~$26.7M** | **$26,688,022.13** | City/County **local use-tax distributions**, parent row `Sedgwick County`. Constructed as CY2024 Jul–Dec + CY2025 Jan–Jun from `CY24LocUseTaxDist.xlsx` and `CY25LocUseTaxDist.xlsx`. | Kansas **FY2025** | Same countywide 1% recipient set | **VERIFIED** (Human $26.7M is rounding) |
| Human FY2025 local combined **~$145M** | **$145,054,963.23** | FY2025 local **sales + use** of the countywide 1% (parent `Sedgwick County` rows) | Kansas **FY2025** | County + cities of the countywide 1%. **Does not** by itself include separate city-imposed RST or CID/TDD overlays as extra amounts inside this parent total. | **VERIFIED** as that defined scope (Human $145M is rounding) |
| Human 2025 countywide 1% **>$121M** | **$121,665,410.28** | KDOR *Countywide Sales Tax Distributions to Cities and Counties* parent `Sedgwick County` **Calendar Year total** | **CY2025**, **sales only** (not use) | County + cities (see WD-BILL-A-093) | **VERIFIED**. Matching YTD file `loytd2025.xlsx` parent total **$121,665,417.50** ($7.22 rounding). |
| CY2025 countywide **use** | **$27,415,468.15** | `CY25CountywideUse.xlsx` parent `Sedgwick County` Calendar Year total | **CY2025**, **use only** | Same 12-192 recipient set | **VERIFIED** |
| CY2025 countywide sales **+** use | **$149,080,878.43** | Sum of the two parent CY totals | **CY2025** | Countywide 1% pool, sales and use | **VERIFIED** as arithmetic of two official parent rows. **Not** the Human FY $145M series. |

City of Sedgwick (indented `Sedgwick`) is a **small city share** (~$49,991.56 CY2025 countywide sales), **not** the county parent.

---

# 3. Scope classification — what the Human local series is and is not

```text
FY2025 $118.4M + $26.7M ≈ $145M
= COUNTYWIDE 1% LOCAL SALES + LOCAL USE
  DISTRIBUTED TO SEDGWICK COUNTY GOVERNMENT AND CITIES
  ON KANSAS FY2025
≠ SEDGWICK COUNTY GOVERNMENT REVENUE ALONE
≠ ALL LOCAL SALES/USE IN THE COUNTY (CITY RST / CID / TDD EXTRA)
≠ CY2025 COUNTYWIDE SALES-ONLY $121.7M
≠ STATE 6.5% SEDGWICK-SOURCED COLLECTIONS
```

Municipal retailer sales taxes imposed by cities (other than the countywide 1%) and CID/TDD overlays: **OBSERVED as a class**; 2025 KS-1700 inventory remains **EVIDENCE REQUIRED**. They are **not** inside the $121.7M / $145.1M parent totals.

---

# 4. Food-tax temporal control (state)

| Calendar year | State general RST | State food rate (K.S.A. 79-3603d) | KDOR file treatment |
|---|---|---|---|
| 2023 | 6.5% | **4%** | `cy23revised.xlsx` General / Food / Combined |
| 2024 | 6.5% | **2%** | `cy24revised.xlsx` General / Food / Combined |
| 2025 | 6.5% | **0%** from 1 Jan 2025 | Monthly 2025 sales files; no annual revised workbook yet |

State food 0% **does not** by itself zero the countywide 1% or CID levies. Exact food-local stacking: **LEGAL RESEARCH REQUIRED** (preserved from WD-BILL-A-087).

---

# 5. Double-count / Future-State firewall

Do **not** add state Sedgwick-sourced collections + local countywide distributions and call the sum Sedgwick government revenue.

Do **not** treat any figure in this file as a Bill A rate, ARR, sufficiency input, or replacement-revenue target.

H.R. 25 remains the Human-selected Future-State consumption-tax reference. **Current Kansas sales/use ≠ H.R. 25.**

---

Libertas sine lapsu — Liberty without drift.
