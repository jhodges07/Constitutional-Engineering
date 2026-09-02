# WD-BILL-A-028 — Domain 01 Evidence Closure and Reconciliation (CWC-CE-128)

**Document ID:** WD-BILL-A-028  
**Title:** Domain 01 Excise / Excise-Type Evidence Closure and Reconciliation  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-128  
**Prior execution:** CWC-CE-127 / WD-BILL-A-022–027  
**Governing LOU candidate:** LOU-004 Draft 0.9 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / CLOSURE EXECUTED — DISPOSITIONS **BLANK** — NOT ACCEPTED  
**Version:** 0.1.0  
**Effective Date:** 2026-09-02  
**Retrieval date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-028-Domain-01-Evidence-Closure-Reconciliation.md  

```text
EVIDENCE CLOSURE + RECONCILIATION
NOT POLICY DISPOSITION
BLANK ≠ RETAIN
MOTOR FUEL IS NOT RETAINED
GAMING RECEIPT ≠ AUTOMATIC DOMAIN 01 MEMBERSHIP
UNK-EX-005 REMAINS RESERVED
NO DOMAIN 02 EXECUTION
NOT A SPEC / NOT HG-D1 / NOT HG-D2
```

CWC-CE-127 work is preserved. This file records additional locators, conflict-closure status, reclassifications, and completeness reassessment. It does **not** silently overwrite WD-BILL-A-023.

---

## 1. Starting posture reconciled

| Item | Status |
|---|---|
| Canonical SHA | `0580ce067cfffeeb55483219f110ac2e19cb4613` — MATCHED |
| CWC-CE-127 artifacts | WD-BILL-A-022–027 present (uncommitted) |
| Domain 01 starting count | 14 verified records |
| Beyond gasoline | YES — VERIFIED (CWC-CE-127) |
| Completeness starting | SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS |

---

## 2. Target 1 — Destination statutes

All six outstanding destination authorities were retrieved as **2025 Kansas Statutes** PDFs from the official Revisor media path on 2026-09-02, except as noted.

### 2.1 K.S.A. 79-3387 — cigarette / tobacco (and related act) disposition — TRACED

- **Governs:** “All revenue collected or received by the director from **taxes imposed by this act**.”
- **Destination:** entire tax remittance credited to the **state general fund**.
- **Separate pool:** license fees, K.S.A. 79-3324a forfeiture proceeds, and fines → **cigarette and tobacco products regulation fund** (K.S.A. 79-3391), “used exclusively for cigarette and tobacco products regulation and enforcement, and not for any other purpose.”
- **Admin:** tax itself has **no** statutory KDOR skim in 79-3387(a). Regulation fund is a **restricted enforcement pool** for fees/fines/forfeitures.
- **Current-law:** History through L. 2017, ch. 96, § 19; June 22 — same 2017 chapter that amended K.S.A. 79-3399 (e-cigarette tax).
- **CF-D01-006:** PARTIALLY RESOLVED. 79-3399 still has no remittance clause of its own. 79-3387 was amended in the same 2017 chapter as 79-3399; both sit in Article 33. KLRD Tax Facts FY2024 reports **Electronic Cigarette** as a **separate SGF line** ($4,294 thousand, 100% SGF). Do **not** treat that GOV-DATA line as a statutory sentence that 79-3399 is inside “this act,” but the working destination for the **tax** is SGF with that dual support.

### 2.2 K.S.A. 79-4108 — liquor enforcement disposition — TRACED

- **Governs:** taxes imposed by K.S.A. 79-4101 through 79-4105 (KRU-D01-009).
- **Default destination:** **state general fund**. Remaining moneys in the former county and city alcoholic liquor control enforcement fund transferred to SGF.
- **Exception (b):** sales on Kansas state fairgrounds: **30% SGF**, remainder **state fair capital improvements fund** (K.S.A. 2-223); expires if the state fair is located outside Hutchinson city limits.
- **Exception (c):** **STAR-bond remittance** — secretary may remit **up to 100%** of enforcement tax collected on consumer sales inside a specified STAR bond project district tax increment to city/county or KDFA **bond debt service funds**. History through L. 2024, ch. 2, § 8 (Special Session); July 1.
- **Purpose restriction:** 79-4101 still recites “enforcement” revenue; 79-4108 default is unrestricted SGF. That is **POTENTIAL CONFLICT** vs uniform standard A/B, not a silent reconciliation.
- **Dependency:** liquor-enforcement STAR-bond path is now **DEPENDENCY VERIFIED** (alongside drink-tax 79-41a03(d)(2)).

### 2.3 K.S.A. 79-4227 — mineral severance disposition — TRACED

Order of credit:

1. Mineral production tax **refund fund** (cap $50,000) as ordered by the director.
2. **7%** of the remainder → **special county mineral production tax fund**; quarterly to producing counties; county treasurer credits **50% county general fund** and **50%** to school districts by assessed mineral value.
3. Remainder for FY2016+ (distributed FY2017+) for counties with ≥$100,000 oil/gas excise receipts: **20%** to **mineral production education fund** (Revisor note: section reference should be K.S.A. 72-5130, not 72-6462*); **remainder to SGF**.
4. The AR25 “12.41% Oil and Gas Valuation Depletion Trust Fund” split is the **FY2013–2015** formula in the same section — **not** the current FY2016+ formula.

**CF-D01-007:** RESOLVED — DIFFERENT ACCOUNTING BASES (and AR25 destination table **stale** as to the 12.41% trust-fund share). Net-after-credit collections ≠ SGF remainder after refund fund + 7% county + 20% education fund.

### 2.4 K.S.A. 79-4219 — mineral credit against tax — TRACED

- Oil: credit **3.67% of gross value** of oil severed and taxable, for taxpayers liable for ad valorem tax on oil property.
- Gas: **3.67% of gross value** for FY1997 and thereafter (phased 2% then 3% in earlier years).
- Closes the AR25 “8% with 3.67% property tax credit” rate-table note. Credit reduces tax due; it is **not** a destination.

### 2.5 K.S.A. 79-34,142 — motor-fuel distribution — TRACED

Credits amounts received pursuant to K.S.A. **79-3408, 79-3408c, 79-3491a, 79-3492, and 79-34,118**:

- **State highway fund 66.37%**
- **Special city and county highway fund 33.63%**

Covers KRU-D01-001, 002, and 003 (trip permits). AR25 FY2025 actual ~65.9% / 33.4% after refunds is **PARTIALLY MATCHED** to this statutory split (refunds and 79-3425c equalization transfers sit around the split).

Related: **K.S.A. 79-3425** (retrieved) first credits the motor-vehicle fuel tax **refund fund**, then remainder per 79-34,142, and still **cross-cites expired 79-34,161**. **K.S.A. 79-3425c** (retrieved): $625,000 quarterly from special city/county highway fund to **county equalization and adjustment fund**; 57% of remaining SCCHF to counties / 43% to cities; county road-and-bridge use; **cities may use receipts to pay bonds issued under K.S.A. 79-3425g**.

**K.S.A. 79-34,164** (current 2025 PDF): provisions of 79-34,160 through 79-34,163 **expire July 1, 2018**. 79-34,161 2025 Revisor PDF path returned **404**. Historical compiled text limited the $875,000/quarter credit to **FY2005 through FY2018**.

### 2.6 K.S.A. 75-5182 — bingo / charitable gaming disposition — TRACED

- License/registration fees → **state charitable gaming regulation fund** (except K.S.A. 75-5183).
- Tax levied by 75-5176 remitted to state treasurer; credited to the same fund (except 75-5183).
- Moneys “shall be expended for the **administration and enforcement** of the Kansas charitable gaming act.”
- Year-end excess over amounts required to pay those operating expenses **transferred to SGF** (75-5182(d)).
- Subsection (c) refers to subsections (d) **and (e)**; retrieved PDF text includes (d) then History — **(e) CURRENT VERSION TO BE VERIFIED**.
- **UNK-EX-005 evidence (not a test):** bingo tax pool is statutorily an **administration/enforcement** fund with SGF spillover of surplus. POTENTIAL CONFLICT vs uniform standard D.

---

## 3. Target 2 — Lottery / casino / gaming classification

PRIMARY-LEGAL retrieved: K.S.A. **74-8734** (full 2025 PDF); **74-8711** (lottery operating fund; history through L. 2025, ch. 117, § 198; April 25); **74-8768** (ELARF).

These pathways are **not** added as Domain 01 verified excise rows. Receipt of money ≠ compulsory Domain 01 membership (Q-BILL-A-005 Option (a)).

| Working ID | Pathway | Legal / economic mechanism | Classification | Domain |
|---|---|---|---|---|
| KRU-REF-08-001 | Sale of lottery tickets and shares (74-8711(b)) | Voluntary purchase of chance; remitted to **lottery operating fund**; prizes, retailer compensation, lottery operating expenses; monthly transfer to **state gaming revenues fund** (79-4801) of the greater of excess operating funds or ≥30% of ticket revenues (≥20% pull-tabs) | **NON-COMPULSORY GOVERNMENT RECEIPT** / **ENTERPRISE / CONTRACTUAL RECEIPT** / **GOVERNMENTAL SHARE OF GAMING REVENUE** | **REFERRED TO DOMAIN 08** |
| KRU-REF-08-002 | Lottery gaming facility state share (74-8734(h)(12)) | Kansas lottery retains “full, complete and ultimate **ownership and operational control**” of the gaming operation; manager operates on behalf of the State; contract must pay State **not less than 22%** of lottery gaming facility revenues to **ELARF** (74-8768) | **GOVERNMENTAL SHARE OF GAMING REVENUE** / **ENTERPRISE** (state-owned lottery games, contracted manager) | **REFERRED TO DOMAIN 08** |
| KRU-REF-08-003 | Sports wagering state share (74-8734(i); 74-8711(f)–(h)) | If the management contract includes sports wagering: State receives **10%** of sports wagering revenues from that manager; LOF then statutory splits (white-collar crime fund $750,000; 2% problem gambling; 80% attracting professional sports fund) | **GOVERNMENTAL SHARE OF GAMING REVENUE** / **MIXED** statutory transfers | **REFERRED TO DOMAIN 08** |
| KRU-REF-05-001 | Lottery gaming facility **privilege fee** (74-8734(h)(6)) | One-time **$25,000,000** (NE/SC zones) or **$5,500,000** (SE/SW) paid upon contract approval to **lottery gaming facility manager fund**; unpaid in 30 days voids contract (74-8734(k)). (h)(19) requires State to repay the fee plus 10% compounded interest if State violates specified exclusivity through July 1, 2032 | **REGULATORY / PRIVILEGE CLAIM** (contract condition of being selected as manager of a **state** gaming operation — not a general public excise) | **REFERRED TO DOMAIN 05** |
| KRU-REF-08-004 | Local shares of lottery gaming facility revenues (74-8734(h)(13)–(16)) | 2% problem-gambling grant fund; 1–3% city/county shares by zone | **GOVERNMENTAL SHARE OF GAMING REVENUE** (statutory contract terms) | **REFERRED TO DOMAIN 08** (local share also Domain 09/06 later) |
| KRU-D01-014 | Bingo taxes (75-5176) | **Tax** on licensee gross receipts / distributor faces and instant tickets | Remains **COMPULSORY GOVERNMENTAL CLAIM** | **Domain 01 retained** (not reclassified) |

**ELARF (74-8768):** expenditures/transfers only for reduction of state debt, state infrastructure, university engineering initiative, and KPERS UAL reduction; $10.5M/year to Kan-grow engineering funds through FY2031; then 50% of remainder quarterly to KPERS until 80% funded. This is **post-receipt use of enterprise gaming share**, not a Domain 01 excise.

**H.R. 25:** XW-HR25-007/013 — chance is not §101 taxable property/service; tax would fall on taxable gaming **services of the gaming sponsor**. Kansas lottery/casino structure is a **state-owned sponsor** with a contracted manager. Crosswalk: EVIDENCE REQUIRED for later Kansas-mirror gaming-services treatment. Human CWC-CE-123 note that state lottery tickets are not a Kansas FairTax taxable transaction remains; PDF VERIFY still required. **H.R. 25 is not Kansas law.**

**ACFR FY2025 (GOV-DATA):** Lottery reported as a **business-type / enterprise** activity (operating revenues including lottery prize awards); ELARF receivable $87,890 thousand. Consistent with Domain 08 referral, not Domain 01.

D01-INV-008 is **RECLASSIFIED / REFERRED** (history preserved): not a verified Domain 01 row.

---

## 4. Target 3 — Statewide fiscal reconciliation

Sources retrieved:

- KDOR AR25 (already CWC-CE-127)
- **KLRD Kansas Tax Facts**, 2024 Supplement to the Ninth Edition (updated Jan 2025), https://klrd.gov/wp-content/uploads/2025/01/2024-Tax-Facts_updated-Jan-2025.pdf — FY2024 receipts (thousands)
- **Kansas ACFR** FY2025, Department of Administration — governmental-fund SGF actuals **aggregate** “Tobacco and liquor taxes” $218,372 thousand; “Severance taxes” $26,494 thousand
- **Consensus Revenue Estimates:** April 2025 short memo URL returned **HTTP 500** this retrieval; November 2024 long memo retrieved; Spring 2026 short memo also **HTTP 500**. Search-index snippets of CRE tables are **not** treated as PRIMARY locators. Status: **EVIDENCE ACCESS BLOCKED** for the April 2025 / Spring 2026 PDFs in this session; November 2024 CRE long memo **PARTIAL**.

Do not invent disaggregation.

| Domain 01 class | Official fiscal line | Status |
|---|---|---|
| Motor fuel (001–003) | KLRD FY2024 Motor Fuels $458,281 thousand, **0 SGF / all other funds**; AR25 FY2025 gross $466,271,554; ACFR Highway Fund revenues **aggregated** with sales/use and registration | MATCHED (KLRD/AR25 named); ACFR **AGGREGATED WITH OTHER REVENUE** |
| Cigarette (004) | KLRD FY2024 Cigarette $90,094 thousand; CRE Nov 2024 uses cigarette as an SGF excise line | MATCHED (KLRD); CRE **PARTIALLY MATCHED** (Nov 2024 memo) |
| Tobacco products (005) | KLRD FY2024 Tobacco Products $10,509 thousand | MATCHED |
| E-cigarette (006) | KLRD FY2024 Electronic Cigarette $4,294 thousand, **100% SGF** | MATCHED (separate line) |
| Gallonage (007) | KLRD FY2024 Liquor Gallonage $26,100 thousand | MATCHED |
| Liquor drink (008) | KLRD FY2024 Liquor Drink $61,124 thousand (state collections before local split) | MATCHED; local 70% share is not an SGF line |
| Liquor enforcement (009) | KLRD FY2024 Liquor Enforcement $83,715 thousand | MATCHED |
| Mineral (010) | KLRD FY2024 Severance $43,372 thousand combined; Oil $38,551 (SGF $25,924 / other $12,627); Gas $4,821; AR25 FY2025 net $39,457,569 vs SGF $26,493,817; ACFR SGF severance $26,494 thousand FY2025 | PARTIALLY MATCHED / see CF-D01-007 |
| Vehicle rental (011) | KLRD Table 4 FY2024 Vehicle Rental Excise **$81 thousand, 0 SGF / all other** | MATCHED as a named line; statewide economic collections likely remitted onward (amount is residual/other, **not** proof of $81k total tax imposed) |
| Tires (012) | KLRD FY2024 New Tires $974 thousand, **0 SGF** | MATCHED |
| Transient guest (013) | KLRD combined state+local TGT FY2024 $63,579 thousand; **State Transient Guest** $1,287 thousand **100% SGF** (~2% of combined, consistent with 12-1694 skim) | MATCHED (state skim + combined local) |
| Bingo (014) | KLRD FY2024 Bingo/Raffle $313 thousand, **0 SGF** | MATCHED (aggregated bingo/raffle) |
| Lottery / ELARF | ACFR enterprise Lottery; ELARF $87,890 thousand | MATCHED as enterprise — **not** Domain 01 |

Zero or small fiscal lines do **not** erase legal authority (vehicle rental $81 thousand other-funds residual). Legal authority does **not** prove FY2025 material collections beyond the lines above.

---

## 5. Target 4 — Transient guest / local authority

**AUTHORITY VERIFIED** (unchanged): K.S.A. 12-1693 and 12-1697, statutory enabling **not to exceed 2%**.

**LOCAL IMPLEMENTATION VERIFIED (KDOR-administered list):** Official KDOR *Transient Guest Tax Rates and Filers*, “as of July 1, 2026,” https://www.ksrevenue.gov/pdf/tgratesfilers.pdf (also indexed at https://ksrevenue.gov/prtgreports.html).

KDOR counts: **39 counties**, **126 cities (including special districts)**, **165** city and county jurisdictions with a listed rate.

Rates **materially exceed 2%** on the official list, including (examples, not exhaustive): Atchison County 4%; Chase County 6%; Geary County 7%; Shawnee County 7%; Abilene 8%; Kansas City 10% (and listed STAR/special jurisdictions at 10%); Goddard 9%; Overland Park 9%; Olathe 9%; Mission 9%; Wichita 6%; Topeka 7%. Osborne County is listed at **1.00%** (below the cap).

**CF-D01-003:** PARTIALLY RESOLVED. Statutory enabling cap remains 2%. Official statewide KDOR implementation list shows widespread rates above 2%, consistent with the LPA/AG home-rule pathway. This CWC does **not** conclude which legal theory each city used. It records the **fact** of official rates above 2%.

**Still incomplete:** jurisdictions that home-ruled a TGT **KDOR does not administer** (AG Op. 82-17 / 2024-2). Label for that remainder: **LOCAL IMPLEMENTATION INVENTORY INCOMPLETE (non-KDOR-administered home-rule levies)**.

No uncontrolled ordinance-by-ordinance survey was performed. No additional statewide local commodity excise class was verified from this TGT list.

---

## 6. Target 5 — Debt / bond / contract / federal dependencies

| Subject | Classification | Evidence |
|---|---|---|
| Motor fuel / State Highway Fund → KDOT highway revenue bonds | **DEPENDENCY VERIFIED** (statewide statutory + ACFR description). **EXAMPLE DOCUMENT** of a specific indenture was **not** sampled. **STATEWIDE UNIVERSAL RULE:** K.S.A. **68-2320** — bonds “payable solely from revenues accruing to the **state highway fund** and transferred to the highway bond debt service fund and **pledged** to their payment.” Debt-service cap 18% of projected SHF revenues for additional post-2010 bonds. | 68-2320 2025 PDF; ACFR FY2025: KDOT has outstanding Highway Revenue Bonds (T-Works); SHF revenues “include **motor fuels taxes**, state sales taxes, compensating use taxes, and drivers’ license and vehicle registration fees.” Series 2024A $694,015,000 and 2025A $729,980,000 issued (partial refundings). |
| Federal highway / federal-aid | **POTENTIAL DEPENDENCY** | 68-2320(c)(2)(B) subtracts “interest subsidy payments expected to be received from the federal government” from debt-service requirements. Not a matching-grant statute for the motor-fuel tax itself. Federal dyed-diesel definition remains in 79-3408(c)(6). |
| City use of SCCHF for street bonds | **DEPENDENCY VERIFIED** (local) | 79-3425c(c): city treasurers credit SCCHF receipts to a street/highway fund “and for the payment of bonds, and interest thereon, issued pursuant to K.S.A. 79-3425g.” |
| Liquor drink STAR bonds | **DEPENDENCY VERIFIED** | 79-41a03(d)(2) (CWC-CE-127) |
| Liquor enforcement STAR bonds | **DEPENDENCY VERIFIED** (new this CWC) | 79-4108(c) |
| STAR bonds generally | ACFR: local STAR bonds paid proportionally from State and local **sales-tax** shares; **not** on State balance sheet; not a general obligation. Liquor STAR remittances are **additional** statutory streams, not the ACFR sales-tax description. | **EXAMPLE** of ACFR program description, not a universal liquor-indenture sample |
| ELARF / KPERS / engineering | **DEPENDENCY VERIFIED** for **referred** gaming share, not Domain 01 | 74-8768 |
| Privilege-fee repayment if exclusivity breached | **POTENTIAL DEPENDENCY** (referred Domain 05) | 74-8734(h)(19) |
| Constitutional impairment if a Domain 01 claim disappeared | **LEGAL EFFECT UNKNOWN** — not analyzed |

No constitutional impairment conclusion is made.

---

## 7. Target 6 — Conflict reconciliation

| ID | Closure status | Reason |
|---|---|---|
| CF-D01-001 | **RESOLVED — DIFFERENT ACCOUNTING CONCEPTS** | 79-5117(c) legally credits **SGF** then remits to counties. KLRD Table 4 FY2024 shows Vehicle Rental Excise **$81 thousand, 0 SGF / all other funds** — consistent with SGF as **waypoint**, not retained general revenue. AR25 “Rental Motor Vehicle Excise Tax Fund” is an operational label for that remittance path. No separate current statute creating that fund name was located. Ultimate county apportionment is common to all three sources. |
| CF-D01-002 | **RESOLVED — SOURCE ERROR IDENTIFIED** (AR25 section number) | Imposition is **65-3424d**. 65-3424 is definitions. AR25 cited the article root. Rate $0.25 and waste-tire fund match 65-3424d. |
| CF-D01-003 | **PARTIALLY RESOLVED** | Enabling cap 2% remains current law. Official KDOR July 1, 2026 rate list shows many implemented rates **above 2%**. Home-rule is the evidenced pathway; each ordinance’s legal theory is not adjudicated here. Non-KDOR-administered levies remain incomplete. |
| CF-D01-004 | **RESOLVED — DIFFERENT TIME PERIODS** | K.S.A. **79-34,164** (2025 PDF): 79-34,160 through 79-34,163 **expire July 1, 2018**. Historical 79-34,161 limited the $875,000/quarter credit to **FY2005–FY2018**. FY2025 actual $0 is consistent with expiration. AR25 distribution **table** is stale. Residual conflict: **79-3425 still cross-cites 79-34,161**. Open as CF-D01-008. |
| CF-D01-007 | **RESOLVED — DIFFERENT ACCOUNTING BASES** | 79-4219 3.67% property-tax credit reduces tax due. 79-4227 then refund fund + 7% county + 20% education fund (current) before SGF. AR25 net-after-credit ≠ SGF line. AR25 12.41% trust-fund share is the **pre-FY2016** formula. KLRD FY2024 oil severance SGF vs total illustrates the same split. |

CF-D01-005 (introduced bills) unchanged — not current law.  
CF-D01-006 PARTIALLY RESOLVED (§2.1).  
**CF-D01-008** (new): 79-3425 still cites expired 79-34,161.

---

## 8. Target 7 — Regulatory / administrative check

No exhaustive KAR audit.

| Item | Result |
|---|---|
| TGT implementation | Official KDOR rate/filer PDF is agency implementation material sufficient to bound KDOR-administered rates |
| Tire | KDOR Pub. KS-1530 already used; statute 65-3424d controls |
| Motor-fuel refund / distribution | 79-3425 / 79-34,142 / 79-3425c retrieved; KAR 92-14 **not fetched** — `[TO BE VERIFIED]` |
| Cigarette regulation fund | 79-3387(b) + 79-3391 cited; KAR not fetched |
| Bingo | 75-5182 is the material admin-retention statute |

Statute remains primary.

---

## 9. Inventory control

| Item | Result |
|---|---|
| Newly discovered Domain 01 compulsory excise rows | **None** added |
| Reclassified / referred | D01-INV-008 lottery/casino/privilege-fee pathways → Domain 08 / 05 as in §3. History preserved. Bingo remains Domain 01 |
| Verified Domain 01 count | **14** (evidence still supports the CWC-CE-127 counted set; the number is not preserved for consistency) |
| Beyond motor fuel | **11** |
| Original beyond-gasoline finding | **YES — VERIFIED — UNCHANGED** |

Human disposition: **BLANK** on every row. Motor fuel **NOT RETAINED**.

---

## 10. Uniform standard / UNK-EX-005 / AGCL (status only)

Uniform A–J: additional **POTENTIAL CONFLICT** evidence — 75-5182 admin/enforcement pool + SGF surplus; 79-4101 “enforcement” purpose vs 79-4108 SGF default; TGT 2% skim confirmed by KLRD $1,287 thousand SGF line vs $63,579 thousand combined TGT.

UNK-EX-005: **RESERVED.** Additional evidence collected (75-5182; 12-1694 + KLRD state TGT line; 79-3387(b) restricted regulation fund for fees/fines not the tax). Final test **not** engineered.

AGCL: 00C POTENTIAL CONFLICT strengthened (verified SGF destinations). 00E EVIDENCE REQUIRED → **POTENTIAL CONFLICT / EVIDENCE REQUIRED** for motor-fuel SHF pledge (68-2320 + ACFR) and liquor STAR remittances. **No control SATISFIED.**

---

## 11. Completeness reassessment (WD-BILL-A-020)

**DOMAIN 01 SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS**

Not upgraded to COMPLETE UNDER DEFINED METHOD: CMP-E (KLRD Tax Facts) is now **performed for FY2024**; CMP-F Consensus line-item PDFs for April 2025 / Spring 2026 were **HTTP 500**; CMP-G ACFR aggregates several Domain 01 classes; KAR 92-series not fetched; non-KDOR TGT still incomplete; no sampled bond indenture (statute + ACFR used instead).

Statewide Kansas Government Revenue Universe: **NOT CERTIFIED.**  
KLRS: **NOT CERTIFIED.**  
Domain 02: **NOT EXECUTED.**

Remaining gaps: WD-BILL-A-026 v0.2.0.

---

## 12. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-02 | CWC-CE-128 Domain 01 closure/reconciliation. Count remains 14. Dispositions BLANK. Motor fuel not RETAINED. |
