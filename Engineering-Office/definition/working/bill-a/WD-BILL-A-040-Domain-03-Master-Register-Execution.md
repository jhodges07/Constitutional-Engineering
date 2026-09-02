# WD-BILL-A-040 — Domain 03 Master Register Execution Instance

**Document ID:** WD-BILL-A-040  
**Title:** Kansas Government Revenue Universe / KLRS Master Register — Domain 03 Execution Instance  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-133 (execution); CWC-CE-134 (closure field updates)  
**Schema authority:** WD-BILL-A-019 (this file does **not** replace the schema lock)  
**Governing LOU candidate:** LOU-004 Draft 1.3 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / DOMAIN 03 ROWS POPULATED FROM EVIDENCE — CLOSURE APPLIED — REGISTER **NOT** STATEWIDE COMPLETE — NOT ACCEPTED  
**Version:** 0.2.0  
**Effective Date:** 2026-09-02  
**Retrieval date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-040-Domain-03-Master-Register-Execution.md  

```text
EXECUTION INSTANCE OF WD-BILL-A-019 SCHEMA
DOMAIN 03 ONLY
HUMAN DISPOSITION = BLANK ON EVERY ROW
BLANK ≠ RETAIN
CURRENT EXISTENCE ≠ POST-BILL-A AUTHORITY
CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE
WITHHOLDING ≠ A SECOND INCOME TAX
KLRS CANDIDACY ≠ FINAL AUTHORIZATION
STATEWIDE UNIVERSE NOT CERTIFIED
NOT A SPEC / NOT HG-D1 / NOT HG-D2
NO INCOME-TAX REPEAL DESIGN
NO FAIRTAX RATE CALCULATION
```

Narrative audit: WD-BILL-A-039. Sources: WD-BILL-A-041. Completeness: WD-BILL-A-042. Conflicts: WD-BILL-A-043. Architecture: WD-BILL-A-044. Closure: WD-BILL-A-046.

Domain 01 rows remain in WD-BILL-A-022. Domain 02 rows remain in WD-BILL-A-031. They are **not** rewritten here.

Common field values unless a row overrides:

- Field 2 EVIDENCE DOMAIN = 03
- Field 25 HUMAN BILL A DISPOSITION = **BLANK**
- Field 26 POST-BILL-A AUTHORITY STATUS = **NOT DETERMINED**
- Field 29 SOURCE DATE / VERSION = 2025 Kansas Statutes PDFs / constitutional text as retrieved 2026-09-02; KLRD Tax Facts 2025 Supplement; Tax Facts 2024 Supplement (updated Jan 2025); KDOR Notice 25-06
- Retrieval date = 2026-09-02

Withholding, estimated payments, returns, information reporting, refund processing, and remittance timing are **COLLECTION / ADMINISTRATION MECHANISMS** and are **not** extra rows.

---

## 1. Index of Domain 03 rows

| Master Record ID | Authoritative name | Compulsory | Verification | Disposition |
|---|---|---|---|---|
| KRU-D03-001 | Kansas tax upon the Kansas taxable income of every resident individual / nonresident computation / fiduciary class (K.S.A. 79-32,110) | YES | TRACED (architecture) | BLANK |
| KRU-D03-002 | Kansas tax upon the Kansas taxable income of every corporation (normal + surtax) (K.S.A. 79-32,110(c)) | YES | TRACED (architecture) | BLANK |
| KRU-D03-003 | Privilege tax on banks, trust companies, federally chartered savings banks, and savings and loan associations (K.S.A. 79-1106 et seq.) | YES | TRACED | BLANK |
| KRU-D03-004 | Electing S corporation / partnership entity-level tax (K.S.A. 79-32,286 / 79-32,287) | YES **if elected** for the taxable period | TRACED (election architecture); isolated actual dollars EVIDENCE REQUIRED | BLANK |
| KRU-D03-005 | Local-option tax on gross earnings from money, notes, and other evidence of debt (K.S.A. 12-1,101) | YES **where locally imposed** | TRACED (enabling); LOCAL IMPLEMENTATION INCOMPLETE (Form 200 official list not transcribed) | BLANK |

Counted Domain 03 verified **claim-category** records: **5**.  
Count follows evidence. Human dispositions: **ALL BLANK**.

---

## 2. Thirty-two-field records

### KRU-D03-001 — Kansas individual income tax

| # | Field | Value |
|---|---|---|
| 1 | MASTER RECORD ID | KRU-D03-001 |
| 2 | EVIDENCE DOMAIN | 03 |
| 3 | AUTHORITATIVE NAME | A tax is hereby imposed upon the Kansas taxable income of every resident, and to the extent specified in subsection (b) upon the Kansas taxable income of every nonresident, which is equal to the rates listed for tax year 2024 and all tax years thereafter (K.S.A. 79-32,110(a)–(b)); fiduciaries taxed at (a)(2) rates (79-32,110(d)) |
| 4 | COMMON / ALTERNATE NAME | Kansas individual income tax; personal income tax; fiduciary income tax (same Act, not a second claim) |
| 5 | GOVERNMENT LEVEL | state |
| 6 | GOVERNMENT ENTITY / ENTITY CLASS | State of Kansas; administered by Kansas Department of Revenue; remitted to State Treasurer |
| 7 | RECEIPT OR CLAIM TYPE | Income tax on Kansas taxable income of individuals and fiduciaries |
| 8 | COMPULSORY STATUS | YES |
| 9 | CURRENT LEGAL AUTHORITY | Kan. Const. art. 11, § 2; K.S.A. 79-32,110; 79-32,109; 79-32,116; 79-32,117; 79-32,105. Contingent later-year rate modifications: 79-32,110c / L. 2025, ch. 116 — **not current TY 2026 rates** (KDOR Notice 25-06) |
| 10 | PAYMENT / REVENUE TRIGGER | Kansas taxable income of a resident individual; nonresident computation under 79-32,110(b) using modified Kansas source income (79-32,109(h)); fiduciary Kansas taxable income. Legal trigger is **taxable income / sourced income**, not a retail consumption event. |
| 11 | LEGALLY OBLIGATED PARTY | The individual / estate / trust. Employer is a **withholding agent** (79-3296), not a second taxpayer of this claim. Economic incidence **NOT ESTABLISHED**. Ultimate economic source (Human intent): people with money. |
| 12 | CONSEQUENCE OF NONPAYMENT | Kansas Income Tax Act remedies apply (79-3294). Penalties/interest **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory claim on earning / receiving / realizing Kansas taxable income (federal AGI starting point ± Kansas modifications − Kansas deductions and personal exemptions). Deductions, exemptions, and credits are **not** collapsed into one category. |
| 14 | RATE / CALCULATION / AMOUNT METHOD | TY 2024+: married joint — 5.2% of Kansas taxable income not over $46,000; $2,392 + 5.58% of excess. All other individuals / fiduciaries — 5.2% not over $23,000; $1,196 + 5.58% of excess. Nonresident: (a) tax × (modified Kansas source income / Kansas AGI). Credits reduce pre-credit liability; withholding/estimated payments are **prepayment**, not a second tax. |
| 15 | STATED PURPOSE | Constitutional: state power to levy and collect taxes on incomes from whatever source derived (art. 11, § 2). Statutory: imposition of tax (79-32,110). |
| 16 | REVENUE DESTINATION | State Treasurer credits **State General Fund**, less IMPACT amounts (74-50,107) and income-tax refund fund (cap $4,000,000) (79-32,105). Homestead/79-255 refunds paid from that fund are **not** this claim. |
| 17 | FUND / POOL TYPE | SGF (general); refund revolving fund; IMPACT program credits |
| 18 | ADMINISTRATIVE / OVERHEAD TREATMENT | KDOR administration; withholding (79-3294–79-3296); estimated tax (79-32,101) |
| 19 | DEBT / BOND / CONTRACT / FEDERAL-MATCH / OTHER DEPENDENCIES | `[LEGAL EFFECT UNKNOWN]` as to impairment if this claim disappeared. IMPACT (74-50,107) is a **destination/transfer** dependency — **REFERRED TO DOMAIN 09** as a transfer class, not a Domain 03 tax. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | KLRD Tax Facts 2025 Supplement (thousands, taxes levied for collection): FY2024 Individual **$4,523,616**; FY2025 Individual **$4,695,736**. DoA June FY2024 SGF receipts: Individual **$4,503,615,413**. Tax Facts Table 4 Individual Income **Other Funds** FY2025 **$20,000 thousand** = IMPACT / 74-50,107 job-creation withholding-credit cap (CF-D03-001 **RESOLVED — ACCOUNTING CLASSIFICATION**). Levy ≠ collections. **CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE.** |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT (earning/receiving income ≠ intended taxable event). H.R. 25 is not Kansas law. Withholding: COLLECTION-MECHANISM ISSUE for later design — not a current second claim. |
| 22 | AGCL 00A–00J CLASSIFICATION | 00A QUESTION REQUIRED; 00C POTENTIAL CONFLICT surface (income/accumulation vs intended consumption event); 00H POTENTIAL CONFLICT surface (art. 11 § 2 authorization ≠ retention). **Never SATISFIED.** |
| 23 | CURRENT-STATE STATUS | Evidenced current Kansas individual/fiduciary income-tax architecture. **Not** future authorization. |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM. Not final authorization. |
| 25 | HUMAN BILL A DISPOSITION | **BLANK** |
| 26 | POST-BILL-A AUTHORITY STATUS | **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-135–146, 158, 173, 175, 177 |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-161–164, 166–167, 179 |
| 29 | SOURCE DATE / VERSION | 79-32,110 2025 PDF (history through L. 2025, ch. 116, § 4); 79-32,110b / 110c retrieved CWC-CE-134; Tax Facts 2025 Supplement; Notice 25-06; DoA June FY2024 SGF receipts (2024-07-02) |
| 30 | VERIFICATION STATUS | TRACED (architecture). Exhaustive 79-32,117 modifications / credits not inventoried. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D03-001 **RESOLVED**; UNK-D03-001 **RESOLVED**; UNK-D03-004 **PARTIALLY RESOLVED**; UNK-D03-005 **PARTIALLY RESOLVED** |
| 32 | NOTES / TRACEABILITY | Nonresident and fiduciary treatment are **computation/taxpayer-class variants**, not extra rows. Do not add withholding or estimated-payment receipts to this line. Dual 2025 amendment path 79-32,110 vs 79-32,110b: same current rates; compilation label **LEGAL INTERPRETATION REQUIRED**. Table 4 Other Funds is IMPACT allocation, not a second claim. |

### KRU-D03-002 — Kansas corporate income tax

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D03-002 / 03 |
| 3 | AUTHORITATIVE NAME | A tax is hereby imposed upon the Kansas taxable income of every corporation doing business within this state or deriving income from sources within this state (K.S.A. 79-32,110(c)) |
| 4 | COMMON / ALTERNATE NAME | Kansas corporate income tax; corporation income tax; corporate surtax |
| 5–6 | LEVEL / ENTITY | State / State of Kansas; KDOR; State Treasurer |
| 7–8 | TYPE / COMPULSORY | Corporate income tax (normal + surtax) / YES |
| 9 | CURRENT LEGAL AUTHORITY | 79-32,110(c); Kansas taxable income 79-32,138; allocation/apportionment 79-3271 through 79-3293 (UDITPA — structural only). Modifiable under 74-50,321 or 79-32,110c. |
| 10 | PAYMENT / REVENUE TRIGGER | Kansas taxable income of a corporation doing business in Kansas or deriving income from Kansas sources |
| 11 | LEGALLY OBLIGATED PARTY | The corporation. Estimated-tax remitter: the corporation (79-32,101(a)(2)). Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Income Tax Act remedies. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory claim on corporate Kansas taxable income (federal taxable income ± Kansas modifications; apportioned/allocated if not entirely Kansas-source) |
| 14 | RATE / CALCULATION | **Normal tax 4%** of Kansas taxable income **plus surtax 3%** of Kansas taxable income in excess of **$50,000**, unless later modified under 74-50,321 or 79-32,110c. Notice 25-06: no TY 2026 79-32,110c cut. |
| 15 | STATED PURPOSE | Statutory imposition of tax on corporate Kansas taxable income |
| 16–17 | DESTINATION / FUND | SGF via 79-32,105 (same credit path as KRU-D03-001) |
| 18 | ADMINISTRATIVE | KDOR; corporate estimated tax |
| 19 | DEPENDENCIES | `[LEGAL EFFECT UNKNOWN]` if disappeared. Distinct from KRU-D03-003. |
| 20 | RECEIPT DATA | Tax Facts (thousands): FY2024 Corporation **$1,419,201**; FY2025 Corporation **$1,313,558**. DoA June FY2024 SGF: Corporation **$1,419,200,508**. Do not add KRU-D03-003. |
| 21 | H.R. 25 | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| 22 | AGCL | 00A QUESTION REQUIRED; 00C / 00H POTENTIAL CONFLICT surface. Never SATISFIED. |
| 23–24 | CURRENT-STATE / KLRS | Current corporate income-tax architecture evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27–28 | LOCATORS | SRC-BILL-A-136, 140, 141, 145, 146, 158, 173 / SRC-BILL-A-161–163, 166–167 |
| 29 | SOURCE DATE | 79-32,110 / 79-32,138 / 79-32,113 2025 PDFs; Tax Facts 2025 Supplement |
| 30 | VERIFICATION | TRACED (architecture). Not a multistate treatise. |
| 31 | CONFLICTS | CF-D03-002 **RESOLVED — DIFFERENT LEGAL CLAIMS**; residual federally chartered savings-bank naming **LEGAL INTERPRETATION REQUIRED** |
| 32 | NOTES | Corporation **franchise** tax is **REFERRED TO DOMAIN 05**. **79-32,113(c)** exempts banks, trust companies, S&Ls (also insurance companies, credit unions) from the Income Tax Act. Do not double-count with KRU-D03-003. Credit unions are not a Domain 03 privilege row. |

### KRU-D03-003 — Financial-institution privilege tax

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D03-003 / 03 |
| 3 | AUTHORITATIVE NAME | It is the purpose and intent of the legislature to levy a tax on national banking associations, state banks, trust companies, federally chartered savings banks and savings and loan associations doing business in Kansas, in lieu of ad valorem taxes levied on the intangible assets of such institutions (K.S.A. 79-1106); rates 79-1107 / 79-1108 |
| 4 | COMMON / ALTERNATE NAME | Financial-institution privilege tax; bank privilege tax; savings-and-loan privilege tax |
| 5–8 | LEVEL / TYPE / COMPULSORY | State / privilege tax measured by net income / YES |
| 9 | AUTHORITY | 79-1106; 79-1107 (banks); 79-1108 (trust companies / S&Ls); net income 79-1109; income-tax exemption **79-32,113(c)** |
| 10–11 | TRIGGER / OBLIGOR | Privilege of doing the listed financial business, measured by net income / the institution |
| 12 | NONPAYMENT | Privilege-tax / Income Tax Act collection architecture as applicable. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Distinct **privilege** claim measured by **net income**, in lieu of **ad valorem on intangibles** (79-1106). Not collapsed into KRU-D03-002. 79-32,113(c) is the Income Tax Act exclusion. |
| 14 | RATE / CALCULATION | TY 2024+: banks — normal **1.94%** of net income + surtax **2.125%** of net income over **$25,000**. Trust companies / S&Ls — normal **1.93%** + surtax **2.25%** over $25,000. Subject to 79-32,110c; Notice 25-06: no TY 2026 cut. Two schedules, **one row**. |
| 15 | STATED PURPOSE | 79-1106: tax in lieu of ad valorem on intangible assets of the listed institutions |
| 16–17 | DESTINATION / FUND | PRIMARY-LEGAL: pay to the state / director of taxation (79-1107, 79-1110). GOV-DATA: Tax Facts Table 4 **100% SGF**. Organic SGF-credit analogue to 79-32,105: **NOT LOCATED**. 79-1111 is administration, not fund-credit. |
| 18 | ADMINISTRATIVE | KDOR K-130 privilege return; separate-entity filing (2025 Privilege Tax instructions) |
| 19 | DEPENDENCIES | 79-32,113(c) exclusion **VERIFIED**. Federally chartered savings-bank naming vs 79-32,113(c) “savings and loan associations”: **LEGAL INTERPRETATION REQUIRED** (not a third claim). |
| 20 | RECEIPT DATA | Tax Facts (thousands): FY2024 **$46,580**; FY2025 **$48,986**. DoA June FY2024 SGF: Financial Institutions **$46,579,609**. Do not split banks vs S&Ls without official split. |
| 21 | H.R. 25 | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| 22 | AGCL | 00A QUESTION REQUIRED; 00C / 00H POTENTIAL CONFLICT surface. Never SATISFIED. |
| 23–24 | CURRENT-STATE / KLRS | Distinct current privilege claim evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27–28 | LOCATORS | SRC-BILL-A-147–150, 158, 173, 176 / SRC-BILL-A-161–166 |
| 29 | SOURCE DATE | 79-1106–1110 2025 PDFs; 79-32,113; KDOR 2025 Privilege book; Tax Facts 2025 Supplement |
| 30 | VERIFICATION | TRACED |
| 31 | CONFLICTS | CF-D03-002 **RESOLVED**; UNK-D03-002 **RESOLVED** (residual naming LIR); UNK-D03-006 **PARTIALLY RESOLVED** |
| 32 | NOTES | Do not call this merely “corporate income tax.” Do not double-count with KRU-D03-002. Credit unions are income-tax exempt under 79-32,113(c) but **not** listed in 79-1106 — not a Domain 03 privilege row. |

### KRU-D03-004 — Electing pass-through entity tax

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D03-004 / 03 |
| 3 | AUTHORITATIVE NAME | Notwithstanding K.S.A. 79-32,129 and 79-32,139, for tax years beginning on and after January 1, 2022, an S corporation or partnership may elect to be subject to tax at the entity level (K.S.A. 79-32,286); tax computed under 79-32,287 |
| 4 | COMMON / ALTERNATE NAME | Kansas PTE tax; SALT parity entity-level tax; electing pass-through entity tax |
| 5–8 | LEVEL / TYPE / COMPULSORY | State / entity-level income tax **if elected** / YES if elected for the period |
| 9 | AUTHORITY | 79-32,286; 79-32,287; owner-credit architecture **79-32,288 RETRIEVED** |
| 10 | TRIGGER | Annual election by eligible S corporation or partnership; then tax on the entity’s taxable base under 79-32,287 |
| 11 | OBLIGOR | The electing pass-through entity is a taxpayer (79-32,287(e)). Owners are not liable in a separate capacity (79-32,288); credit = owner’s direct share; excess refundable. Economic incidence **NOT ESTABLISHED**. |
| 12 | NONPAYMENT | Income Tax Act remedies. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Elective entity-level income tax at the highest individual rate; purpose includes federal SALT-cap workaround / avoiding owner-level double tax (KDOR SALT Parity FAQ). Default (no election): owner-level KRU-D03-001 — **not** a separate claim. |
| 14 | RATE / CALCULATION | Highest individual rate under 79-32,110(a) for that year. TY 2024+ highest rate **5.58%**. Base: nonresident Kansas-source share + resident share (statewide or Kansas-only, consistent method) (79-32,287(a)). |
| 15 | STATED PURPOSE | Entity-level election; credits attributable to PTE activities pass through to owners (79-32,287(c)); 79-32,288 owner credit |
| 16–17 | DESTINATION / FUND | Same 79-32,105 SGF path as income tax (not separately isolated in Tax Facts) |
| 18 | ADMINISTRATIVE | Annual election; entity return |
| 19 | DEPENDENCIES | Owner credit / anti-double-tax **79-32,288**. Isolated statewide **actual** PTE dollars **UNK-D03-003 EVIDENCE REQUIRED**. CRE: **net-neutral shift** (estimate). Do **not** add PTE receipts to KRU-D03-001/002 as additional net revenue. |
| 20 | RECEIPT DATA | **AGGREGATED REPORTING** inside individual/corporate income-tax lines. Isolated **actual** PTE dollars: **EVIDENCE REQUIRED**. CRE FY2023 corporation **+$602 million** is a **shift estimate**, not isolated actual. |
| 21 | H.R. 25 | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| 22 | AGCL | 00A QUESTION REQUIRED; 00C POTENTIAL CONFLICT surface. Never SATISFIED. |
| 23–24 | CURRENT-STATE / KLRS | Current elective entity-level claim evidenced / CANDIDATE COMPULSORY CLAIM (when elected) |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27–28 | LOCATORS | SRC-BILL-A-151–152, 136, 160 / SRC-BILL-A-164, 180 |
| 29 | SOURCE DATE | 79-32,286 / 79-32,287 / 79-32,288 2025 PDFs; KDOR SALT Parity FAQ; CRE Long Memo 05-05-2023 |
| 30 | VERIFICATION | TRACED (election architecture); isolated actuals EVIDENCE REQUIRED |
| 31 | CONFLICTS | UNK-D03-003 **EVIDENCE REQUIRED**; UNK-D03-011 **RESOLVED** |
| 32 | NOTES | Distinct because the entity is the statutory taxpayer when the election is in force. Not a second claim for non-electing pass-throughs. 79-32,288 is not a new claim. |

### KRU-D03-005 — Local-option gross-earnings / intangibles tax (K.S.A. 12-1,101)

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D03-005 / 03 |
| 3 | AUTHORITATIVE NAME | The governing body of any county, city or township is hereby authorized to levy a tax on the gross earnings derived from money, notes and other evidence of debt having a tax situs in such county, city or township (K.S.A. 12-1,101) |
| 4 | COMMON / ALTERNATE NAME | Local intangibles tax; intangibles tax; local gross-earnings tax on money/notes |
| 5–6 | LEVEL / ENTITY | **Local** (county / city / township that imposes). State enabling. Schools: Tax Facts FY2025 intangibles **$0**. |
| 7–8 | TYPE / COMPULSORY | Local-option tax on **gross earnings** from money, notes, and other evidence of debt / YES **where imposed** |
| 9 | AUTHORITY | 12-1,101; definitions 12-1,102. City general income tax **prohibited** except 12-1,101–12-1,109 (12-140). County general income tax **prohibited** except the same (19-101a(a)(12)). |
| 10 | TRIGGER | Gross earnings from money, notes, and other evidence of debt having tax situs in the imposing jurisdiction, **if** ordinance/resolution imposed (by Sept. 1 of preceding year) |
| 11 | OBLIGOR | Person/entity with taxed gross earnings in the jurisdiction. Economic incidence **NOT ESTABLISHED**. |
| 12 | NONPAYMENT | Local/KDOR administration under 12-1,101 family. Penalties **REFERRED TO DOMAIN 07** if distinct. |
| 13 | ECONOMIC FUNCTION | Gross-earnings local tax on specified intangible **income-type** interests — **not** classified tangible-property ad valorem (Domain 02 correctly referred it). Enabling ≠ every jurisdiction imposes. Classification: **AUTHORITY EXISTS BUT LOCAL IMPLEMENTATION VARIABLE**. |
| 14 | RATE / CALCULATION | County: 1/8 of 1% up to **¾ of 1%**. City / township (township outside third-class city limits): 1/8 of 1% up to **2¼%**. Steps of 1/8 of 1%. |
| 15 | STATED PURPOSE | Local-option tax on specified gross earnings |
| 16–17 | DESTINATION / FUND | Imposing county / city / township. State intangibles Tax Facts column **$0**. |
| 18 | ADMINISTRATIVE | Ordinance/resolution; county clerk list to KDOR by July 15 (12-1,101); official rate list **KDOR Form 200** |
| 19 | DEPENDENCIES | Petition/election paths to eliminate or impose (12-1,101(e)–(f)). Statewide imposing roster: Form 200 **not transcribed**. **LOCAL IMPLEMENTATION INCOMPLETE** as a narrative inventory. |
| 20 | RECEIPT DATA | Tax Facts (thousands): FY2024 intangibles **$1,389**; FY2025 **$2,445**. FY2025 local split: counties **$1,310**; cities **$623**; townships **$512**; schools **$0**. |
| 21 | H.R. 25 | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| 22 | AGCL | 00A QUESTION REQUIRED; 00C / 00H POTENTIAL CONFLICT surface (local income-type claim vs consumption architecture; 12-140 / 19-101a limitations). Never SATISFIED. |
| 23–24 | CURRENT-STATE / KLRS | Enabling **CURRENT**; imposition VARIABLE / CANDIDATE COMPULSORY CLAIM where imposed |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27–28 | LOCATORS | SRC-BILL-A-153–157 (SRC-BILL-A-120 is the Domain 02 referral locator) / SRC-BILL-A-161–162, 178 |
| 29 | SOURCE DATE | 12-1,101 / 12-1,102 / 12-140 / 19-101a 2025 PDFs; Tax Facts 2025 Supplement; Form 200 current to July 1, 2025 |
| 30 | VERIFICATION | TRACED (enabling + fiscal aggregate + official Form 200 list). Narrative roster **not transcribed**. |
| 31 | CONFLICTS | UNK-D03-007 **PARTIALLY RESOLVED** |
| 32 | NOTES | Referral from UNK-D02-006 **CLOSED** here. Do not generalize this narrow authority into general local income-tax power. Introduced local earnings-tax bills are **NOT CURRENT LAW**. Do not invent jurisdiction lists. |

---

## 3. Mechanisms recorded but not inventoried as claims

| Mechanism | Classification | Authority |
|---|---|---|
| Employer withholding | COLLECTION / PREPAYMENT for KRU-D03-001 | 79-3294; 79-3295; 79-3296; 79-32,100d |
| Estimated income-tax payments | PAYMENT MECHANISM for KRU-D03-001 / 002 | 79-32,101 |
| Income-tax refund processing | ADMINISTRATION | 79-32,105 refund fund |
| Information reporting / returns | ADMINISTRATION | Kansas Income Tax Act |
| Withholding / estimated penalties | **REFERRED TO DOMAIN 07** | not a Domain 03 tax claim |

---

## 4. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-02 | CWC-CE-133: 5 Domain 03 claim-category rows. Dispositions BLANK. Schema fields 1–32 unchanged. |
| 0.2.0 | 2026-09-02 | CWC-CE-134: field strengthening from closure evidence. Count remains 5. Field 25 BLANK. Field 26 NOT DETERMINED. |
