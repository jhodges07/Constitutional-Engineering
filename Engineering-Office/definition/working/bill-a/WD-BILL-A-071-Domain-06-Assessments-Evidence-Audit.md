# WD-BILL-A-071 — Domain 06 Assessments Evidence Audit

**Document ID:** WD-BILL-A-071  
**Title:** Kansas Government Revenue Universe / KLRS — Domain 06 Assessments Evidence Audit  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-144  
**Canonical starting SHA:** `19343f33a830b6e2e831c4546f9709fbd1b4e1bb`  
**Schema authority:** WD-BILL-A-019 (unchanged)  
**Completeness method:** WD-BILL-A-020  
**Governing LOU candidate:** LOU-004 Draft 1.9 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / DOMAIN 06 CURRENT-STATE EVIDENCE EXECUTED — NOT ACCEPTED — NOT STATEWIDE COMPLETE  
**Version:** 1.0.0  
**Effective Date:** 2026-09-02  
**Retrieval date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-071-Domain-06-Assessments-Evidence-Audit.md  

```text
CURRENT-STATE REVENUE-CLAIM EVIDENCE AUDIT
NOT FUTURE BILL A POLICY DESIGN
AUDIT THE GOVERNMENT CLAIM, NOT THE GOVERNMENT LABEL
ASSESSMENT ≠ AUTOMATICALLY DOMAIN 06
ASSESSMENT ≠ AUTOMATICALLY RETAIN
PROPERTY-RELATED ASSESSMENT ≠ AUTOMATICALLY PROPERTY TAX
CURRENT EXISTENCE ≠ POST-BILL-A AUTHORITY
CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE
ONE CITY / COUNTY / PROJECT / PARCEL ≠ ONE CLAIM
HUMAN DISPOSITION = BLANK ON EVERY ROW
BLANK ≠ RETAIN
NO FAIRTAX RATE CALCULATION
NO REPLACEMENT-REVENUE CALCULATION
NO FUTURE DISTRIBUTION DESIGN
DOMAIN 07 AND LATER NOT EXECUTED
PROPERTY TAX: STATEWIDE ELIMINATION — MANDATORY
COUNTY SCHEDULE: 5 YEARS OR 7 YEARS
ALL-IN = NEW SYSTEM; ALL-OUT = LEGACY MINUS PROPERTY TAX
API / TAXPAYER SUPREMACY / TRANSPARENCY / ACCOUNTABILITY / RUNTIME REPUBLIC REMAIN STATEWIDE
NO COMMIT / NO PUSH
```

Master register: WD-BILL-A-072. Sources: WD-BILL-A-073. Completeness: WD-BILL-A-074. Conflicts: WD-BILL-A-075. Classification / referral: WD-BILL-A-076. Git handoff: WD-BILL-A-077.

Domain 01–05 evidence is **preserved** and **not rewritten**. Domain 05 referrals in WD-BILL-A-065 are **executed here**, not by altering Domain 05 files.

---

## 1. Executive finding

Kansas currently imposes compulsory governmental payment claims that function, in whole or in part, as **special assessments, benefit-district assessments, project/service assessments levied against property, district service assessments, or statutory industry/regulatory assessments**. The government **label** is not dispositive. A charge called an “assessment” is not automatically Domain 06. A charge not so labeled may belong here if its legal and economic function is an assessment.

Kansas doctrine distinguishes a **special assessment** from a **general tax**. A special assessment is levied according to **special benefit** conferred on particular property (*State Highway Commission v. City of Topeka*, 193 Kan. 335 (1964)). A **tax** is a forced contribution for general governmental services (*Executive Aircraft Consulting, Inc. v. City of Newton*, 252 Kan. 421 (1993)). A city **transportation utility fee** levied on all developed property for general street maintenance was held a **tax** and a prohibited **excise tax** under K.S.A. 12-194 — **not** a special assessment (*Heartland Apartment Ass'n v. City of Mission*, 305 Kan. 250, 382 P.3d 308 (2016)). That holding is **not** applied as a conclusion that every stormwater or utility charge is illegal.

Counted verified Domain 06 **claim-category** records: **14**. Count follows evidence, not the search surface. Human dispositions: **ALL BLANK**. Post-Bill-A authority: **NOT DETERMINED** on every row.

Do **not** infer: assessment ≠ property tax, therefore assessment = RETAIN.

| ID | Claim-category | Distinct legal claim? |
|---|---|---|
| KRU-D06-001 | Municipal special assessments — General Improvement and Assessment Law (K.S.A. 12-6a01 et seq.) | YES as a **class**; one city / project / parcel ≠ one row. Allied older street method (12-602 / 12-608) noted, not separately counted |
| KRU-D06-002 | County sewer-district special assessments (K.S.A. 19-27a01 et seq.) | YES as a **class** |
| KRU-D06-003 | Drainage-district special assessments (K.S.A. ch. 24, e.g. 24-422 / 24-424) | YES as a **class** |
| KRU-D06-004 | Watershed-district special assessments against especially benefited lands (K.S.A. 24-1209 / 24-1217) | YES as a **class**. District **mill levies** referred to Domain 02, not counted here |
| KRU-D06-005 | Irrigation-district assessments (K.S.A. 42-718 class) | YES as a **class** |
| KRU-D06-006 | County water-supply / distribution-district special assessments (K.S.A. 19-3540) | YES as a **class**. Distinct from rural-water **rates** (82a-619 — **no tax levy**; Domain 08) |
| KRU-D06-007 | CID / TDD **special assessments** (K.S.A. 12-6a28 / 12-6a29; 12-17,143) | YES as a **class**. Distinct from CID/TDD **sales-tax overlays** (KRU-D04-005) |
| KRU-D06-008 | Nuisance / weed / demolition / service-cost assessments to the tax roll (K.S.A. 12-1617e; 12-1755; 12-6a17) | YES as a **class** — police-power cost recovery via special-assessment lien |
| KRU-D06-009 | Business-improvement-district annual service fees (K.S.A. 12-1791) | YES as a **class**. Label “fee” not dispositive. Distinct from Domain 05 occupation licenses |
| KRU-D06-010 | Insurance guaranty-association assessments (K.S.A. 40-2906 class) | YES as a **class**. Distinct from KRU-D05-016 **fees** and from premium **tax** |
| KRU-D06-011 | Workers-compensation-fund annual assessments (K.S.A. 44-566a) | YES |
| KRU-D06-012 | KCC public-utility / common-carrier assessments (K.S.A. 66-1502 / 66-1503) | YES as a **class** with two mechanisms |
| KRU-D06-013 | Grain-commodity first-purchaser assessments (K.S.A. 2-3007) | YES as a **class** (corn/sorghum/soy/wheat/sunflower). Refund architecture noted. Not Domain 01 gallonage excise |
| KRU-D06-014 | Municipal stormwater / drainage utility charges (home-rule / ordinance class) | YES as a **class**; **CLASSIFICATION REQUIRED** (fee vs tax vs special assessment); **LOCAL IMPLEMENTATION VARIABLE** |

Completeness: **DOMAIN 06 SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS** (WD-BILL-A-074). Kansas Government Revenue Universe: **NOT CERTIFIED**. KLRS: **NOT CERTIFIED**. Bill A maturity: **19% UNCHANGED**. Domain 07 and later: **NOT EXECUTED**.

Arithmetic with Domains 01–05: **58 + 14 = 72** verified claim-category records. **72 ≠ 72 retained claims. 72 ≠ 72 future Bill A claims.**

---

## 2. Method and discovery principle

Audit by legal authority + trigger + obligated party + assessment base + amount method + purpose + destination + recurrence + property/ownership/benefit relationship + enforcement + economic function — **not** merely by the word “assessment.”

Search surface in CWC-CE-144 is **not** a finding that every listed item exists or belongs in Domain 06.

Granularity: materially distinct **architectures**, not one row per city, county, improvement project, parcel, statutory form, or assessment district.

---

## 3. Domain 05 / Domain 02 handoff (not redone)

| Prior referral | This CWC |
|---|---|
| WD-BILL-A-030 / 031 / 034: municipal improvement-district special assessments (12-6a01) → Domain 06 | **KRU-D06-001** |
| WD-BILL-A-065: special assessments / benefit districts / TUF-type taxes → Domain 06 | Assessments executed. **TUF** recorded as **tax/excise doctrine**, **not** a verified Domain 06 current claim (Heartland) |
| WD-BILL-A-065 KRU-D05-007 possible Domain 06 | Building **permits** remain Domain 05. Special-assessment financing of improvements is KRU-D06-001. Impact/excise “fees” remain **LEGAL INTERPRETATION REQUIRED** in Domain 05 |
| WD-BILL-A-065 KRU-D05-008 industry assessments | Executed as KRU-D06-010–013 where evidenced |
| KRU-D04-005 CID/TDD **sales tax** | **Not duplicated.** CID/TDD **special assessments** = KRU-D06-007 |

Domain 02’s **16** verified property claim-categories are **unchanged**. General ad valorem / mill-levy claims remain Domain 02.

---

## 4. Property-tax boundary

An assessment **against real property** is not automatically Domain 02.

| Test (working) | Domain 02 | Domain 06 |
|---|---|---|
| Trigger | General ownership / classified value / mill levy | Special benefit, project, district, police-power cost recovery, or industry/regulatory base |
| Collection on tax roll | Common | Also common (12-6a10; 19-27a07; 24-424). **Collection mechanism ≠ classification** |
| Recurrence | Typically annual general levy | Installment special tax (often ≤20 years), event-triggered cost recovery, or periodic industry assessment |

Statewide Human Intent remains: **PROPERTY TAX = ZERO** for every Kansas county. This CWC does **not** decide whether any Domain 06 assessment survives Bill A. ALL-IN / ALL-OUT does **not** classify Domain 06. The 5-year / 7-year choice is the **property-tax elimination schedule**, not an assessment schedule.

---

## 5. Special-assessment architecture (property / benefit)

### 5.1 Municipal GIAL (KRU-D06-001)

K.S.A. 12-6a02 authorizes a city, as a complete alternative to other methods, to make municipal works that confer a **special benefit** upon property in a definable area and to **levy and collect special assessments** upon property deemed benefited. Authorized works include streets/curbs/sidewalks, storm and sanitary sewers, street lights, waterworks, parking, and other enumerated improvements. K.S.A. 12-6a08 apportions cost according to special benefits (front foot, square foot, value, or other reasonable plan imposing substantially equal burdens on similarly benefited property). K.S.A. 12-6a10: assessments collected **concurrent with general property taxes**, payable in **not more than 20 equal annual installments**, certified as **special taxes**. Bonds may finance the improvement (12-6a14 / 12-6a15). **DEBT DEPENDENCY VERIFIED** as architecture; impairment **LEGAL EFFECT UNKNOWN**. Dependency ≠ RETAIN.

Older street-improvement special assessments (12-602 / 12-608) remain an allied **method**, not a second counted architecture.

**LOCAL IMPLEMENTATION VARIABLE.** One ordinance ≠ statewide inventory.

### 5.2 County sewer (KRU-D06-002)

K.S.A. 19-27a02 / 19-27a07: county commissioners as sewer-district governing body levy special assessments by resolution after roll, notice, and hearing. Assessment becomes a **lien** from the effective date of the resolution. Challenges limited (30-day architecture). Collected as other taxes.

### 5.3 Drainage districts (KRU-D06-003)

K.S.A. 24-422 / 24-424: assessors apportion estimated cost to lands protected/benefited; board confirms; amounts become special assessments and liens; certified to county clerk and collected as other taxes. 30-day limitation on actions.

### 5.4 Watershed (KRU-D06-004)

K.S.A. 24-1209 (ninth): power to **levy taxes and assessments**. K.S.A. 24-1217: if financing is by special assessment against lands **especially benefited**, three appraisers apportion by relative benefit; assessment shall **not exceed estimated benefits**. District **general mill levies** are **referred to Domain 02** and are **not** this row.

### 5.5 Irrigation (KRU-D06-005)

K.S.A. 42-718: board levies an assessment against district lands sufficient for interest, obligations, O&M, and general fund; certified to county clerk; collected as other taxes. Water rentals/tolls may exist as a **separate** user charge (**Domain 08 referral**), not collapsed here.

### 5.6 County water-supply districts (KRU-D06-006)

K.S.A. 19-3540: costs assessed against lots within the district (exclusive of improvements) as one tax, or by equal-area or other reasonable assessment plan; bonds authorized. Distinct from **rural water districts** (82a-619): **no power to levy any taxes**; rates → **Domain 08**.

### 5.7 CID / TDD special assessments (KRU-D06-007)

CID petitions may specify amount and method of **assessment** (12-6a28 / 12-6a29) **in addition to or instead of** CID sales tax (12-6a31 = KRU-D04-005). TDD: 12-17,143 authorizes special assessments following 12-6a01 procedures (with listed exceptions). **Do not double-count** the sales-tax overlay.

### 5.8 Nuisance / demolition / service-cost (KRU-D06-008)

K.S.A. 12-1617e: unpaid abatement/weed/nuisance costs **assessed and charged** against the lot and extended on the tax roll. K.S.A. 12-1755: demolition/raze cost recovery by special assessment. K.S.A. 12-6a17: **service assessments** where the city performs work a person was legally required to perform. Function: **police-power cost recovery**, not a GIAL improvement-benefit district. Event-triggered. **LOCAL IMPLEMENTATION VARIABLE.**

---

## 6. District service / regulatory / commodity assessments

### 6.1 BID service fees (KRU-D06-009)

K.S.A. 12-1791: city may annually levy **business improvement service fees** applicable only to businesses in the district; special fund (12-1792); factors may include space, front footage, employees, type of business. Expressly **in addition to** city-wide license fees / occupation taxes (Domain 05). Label “fee”; function is a **district assessment** on businesses. **LOCAL IMPLEMENTATION VARIABLE.**

### 6.2 Insurance guaranty (KRU-D06-010)

K.S.A. 40-2906(1)(3): Kansas Insurance Guaranty Association shall **assess** member insurers in proportion to net direct written premiums; cap **2%** of preceding-year net direct written premiums. Condition of the statutory insolvency-protection system. Distinct from 40-252 **premium tax** and from KRU-D05-016 **licensing fees**. Life/health guaranty architecture is **allied class**, not a second counted row unless later evidence requires split. **EVIDENCE REQUIRED** whether assessments are currently levied in a given year (insolvency-contingent).

### 6.3 Workers compensation fund (KRU-D06-011)

K.S.A. 44-566a: annual June 1 assessment by the commissioner of insurance against carriers, self-insurers, and group-funded pools; due July 1; credited to the workers compensation fund. Apportioned by claims paid/payable.

### 6.4 KCC (KRU-D06-012)

K.S.A. 66-1502: investigation/appraisal expense assessments against the utility, fiscal-year cap **0.6%** of intrastate gross operating revenues (with listed exceptions). K.S.A. 66-1503: quarterly operating-expenditure assessments against all jurisdictional utilities/carriers, cap the greater of **$100** or **0.2%** of intrastate gross operating revenues. Two **mechanisms**, one **class**. Distinct from Domain 05 licenses.

### 6.5 Grain commodity checkoffs (KRU-D06-013)

K.S.A. 2-3007: assessments **hereby levied** on grain sorghum, corn, soybeans, wheat, and sunflowers marketed through commercial channels; collected by first purchaser as a deduction; statutory **refund** procedure (generally ≥$5). Compulsory at sale with refund right. **Not** Domain 01 motor-fuel/cigarette gallonage. One class; commodity ≠ extra row.

---

## 7. Stormwater / TUF classification surface (KRU-D06-014)

Municipal **stormwater / drainage utility charges** exist by local ordinance (home rule). Kan. Att'y Gen. Op. 93- (Topeka stormwater) discussed fee/tax/special-assessment attributes; AG opinions are **not** controlling holdings. *Heartland* later held Mission’s **TUF** (all developed property; general street maintenance; trip-generation formula) is a **tax** and prohibited **excise** under 12-194 — **not** a special assessment and **not** a valid fee.

KRU-D06-014 records the **class of municipal stormwater/drainage utility charges** as **CLASSIFICATION REQUIRED**. It does **not** count Mission’s invalidated TUF as a current lawful claim. It does **not** hold that every stormwater charge is a valid special assessment. **LOCAL IMPLEMENTATION VARIABLE.**

---

## 8. Fee / penalty / enterprise / excise / sales / income boundaries

| Boundary | Referral | Do not |
|---|---|---|
| License / permit / occupation / filing | Domain 05 (preserved 18) | Recast as assessment |
| General ad valorem / mills / vehicle property tax | Domain 02 (preserved 16) | Duplicate as assessment |
| CID/TDD/STAR **sales tax** | Domain 04 KRU-D04-005 | Duplicate as assessment |
| Fines, late interest as punishment, misdemeanor sewer penalties | **Domain 07 — not executed** | Count as Domain 06 |
| Rural-water rates; irrigation water rentals; municipal utility **consumption** rates | **Domain 08 — not executed** | Count as Domain 06 |
| Motor-fuel / cigarette / liquor gallonage | Domain 01 | Collapse checkoff into excise |
| Financial-institution **privilege tax** | Domain 03 | Collapse KCC assessment into privilege tax |

---

## 9. Purpose / destination / recurrence / debt

| Pattern | Typical destination | Recurrence | Debt |
|---|---|---|---|
| GIAL / sewer / drainage / CID-TDD assessments | Project / improvement / bond-and-interest funds | Installment special tax (often ≤20 years) | GO / special-obligation architecture common; **DEPENDENCY VERIFIED** as class; impairment **LEGAL EFFECT UNKNOWN** |
| Nuisance/demolition | Reimburse city fund that paid abatement | Event | Usually none |
| BID | Special BID fund (12-1792) | Annual | **EVIDENCE REQUIRED** |
| Guaranty / WC / KCC | Statutory association / WC fund / KCC appropriations | Annual or event (insolvency / investigation) | **EVIDENCE REQUIRED** |
| Commodity checkoff | Commodity commissions via KDA | Per marketed unit | None evidenced |
| Stormwater utility | LOCAL IMPLEMENTATION VARIABLE | Typically periodic | **EVIDENCE REQUIRED** |

Do not infer future Bill A treatment from destination.

---

## 10. Fiscal scale

Isolated statewide Domain 06 total: **EVIDENCE REQUIRED**. Special assessments are collected locally on the tax roll and are often embedded in city/county bond-and-interest or project funds. Kansas ACFR “charges for services” **mixes** enterprise, fees, and other charges — **not** a Domain 06 total. Do not sum unlike categories. **CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE.** Representative local implementation (e.g. Leavenworth 2024 nuisance-assessment ordinance) establishes existence, not statewide dollars.

---

## 11. Constitutional / legal findings (bounded)

| Issue | Finding |
|---|---|
| Special assessment vs general tax | *State Highway Commission v. City of Topeka*, 193 Kan. 335 (1964): special assessment levied according to benefits conferred; distinct from general tax; special assessment on state property does not violate Art. 11 / 79-201a as a general tax would. **Do not generalize beyond supported scope.** |
| Fee vs tax | *Executive Aircraft*, 252 Kan. 421 (1993): nature and function, not label. **Not** applied as a holding that every Domain 06 row is a valid assessment. |
| TUF | *Heartland*, 305 Kan. 250 (2016): Mission TUF = tax and prohibited excise under 12-194. **Not** a special assessment. **Not** counted as a current Domain 06 claim. |
| Home rule | Art. 12 § 5 remains the local-authority surface for stormwater/BID/nuisance implementation. 12-194 limits local **excise** taxes. **LEGAL INTERPRETATION REQUIRED** for unclassified utility charges. |
| Uniformity / Art. 11 | General property tax is Domain 02. Special assessments are a **different** claim type in Kansas doctrine. Whether Art. 11 / Art. 6 school-finance architecture constrains **future** assessment treatment: **LEGAL INTERPRETATION REQUIRED**. Not a disposition. |

No constitutional amendment. No unsupported conclusion that Kansas currently permits or prohibits a future Bill A assessment architecture.

---

## 12. AGCL mapping (never SATISFIED)

See WD-BILL-A-004. Audit questions only: signal before claim (notice/hearing common for GIAL/sewer/drainage); identifiable authority; purpose restriction (project vs general); expiration (installment term vs perpetual mill); exit (pay off assessment; stop the regulated activity; refund checkoff); debt dependency; remedy (30-day challenge windows). Compatible intent is **not** satisfaction. **Never SATISFIED.**

---

## 13. H.R. 25

H.R. 25 remains the Human-selected **federal economic model**, not Kansas law. Domain 06 special assessments generally attach to **property benefit / district / industry**, not H.R. 25 final-consumption taxable events. Future Bill A treatment: **NOT DETERMINED**. No FairTax rate. No replacement-revenue calculation. No future distribution formula. Domain 06 evidence does **not** authorize changing the H.R. 25 economic standard.

---

## 14. County architecture preservation (not reopened)

```text
PROPERTY TAX: STATEWIDE ELIMINATION — MANDATORY
COUNTY PROPERTY-TAX SCHEDULE: 5 YEARS OR 7 YEARS
COUNTY TAX-SYSTEM CHOICE: ALL-IN = NEW SYSTEM; ALL-OUT = LEGACY MINUS PROPERTY TAX
API / TAXPAYER SUPREMACY / TRANSPARENCY / ACCOUNTABILITY / RUNTIME REPUBLIC = NON-OPTIONAL
```

UQ-CTS-001–016 remain open. This CWC does not assign Domain 06 claims to either schedule.

---

## 15. What this CWC does not do

Does not RETAIN / TRANSFORM / DISAPPEAR any assessment. Does not declare any assessment legitimate as future policy. Does not execute Domains 07–12. Does not calculate a FairTax rate or replacement revenue. Does not draft operative or criminal language. Does not advance HG-D1 / SPEC / HG-D2 / maturity. Does not commit or push. Does not reopen CWC-CE-142 / CWC-CE-143 county architecture. Does not alter Domain 01–05 evidence bodies.

---

Libertas sine lapsu — Liberty without drift.
