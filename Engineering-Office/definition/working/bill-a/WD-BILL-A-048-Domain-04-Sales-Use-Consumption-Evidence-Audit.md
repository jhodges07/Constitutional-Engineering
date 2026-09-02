# WD-BILL-A-048 — Domain 04 Sales / Use / Consumption Revenue Claims Evidence Audit

**Document ID:** WD-BILL-A-048  
**Title:** Kansas Government Revenue Universe / KLRS — Domain 04 Sales / Use / Consumption Evidence Audit  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-136; CWC-CE-137 (closure)  
**Canonical starting SHA:** `569b65183291969e681bd9c134c7f0e41f7c147f`  
**Schema authority:** WD-BILL-A-019 (unchanged)  
**Completeness method:** WD-BILL-A-020  
**Governing LOU candidate:** LOU-004 Draft 1.5 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / DOMAIN 04 CURRENT-STATE EVIDENCE EXECUTED — CLOSURE APPLIED — NOT ACCEPTED — NOT STATEWIDE COMPLETE  
**Version:** 0.2.0  
**Effective Date:** 2026-09-02  
**Retrieval date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-048-Domain-04-Sales-Use-Consumption-Evidence-Audit.md  

```text
CURRENT KANSAS SALES / USE TAX ≠ H.R. 25 FAIRTAX
SIMILARITY ≠ EQUIVALENCE
STRUCTURAL MATCH ≠ RETAIN
MATERIAL STRUCTURAL DIFFERENCE ≠ DISAPPEAR
RETAILER COLLECTION ≠ A SECOND TAX CLAIM
MARKETPLACE COLLECTION ≠ A SECOND TAX CLAIM
REMOTE-SELLER DUTY ≠ A SECOND TAX CLAIM
EXEMPTION ≠ A REVENUE CLAIM
CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE
CURRENT EXISTENCE ≠ POST-BILL-A AUTHORITY
BLANK ≠ RETAIN
HUMAN DISPOSITION = BLANK ON EVERY ROW
NO FAIRTAX RATE CALCULATION
NO FUTURE DISTRIBUTION DESIGN
NO OPERATIVE REPEAL / REPLACEMENT DRAFTING
DOMAIN 05 NOT EXECUTED
NO COMMIT / NO PUSH
```

Master register: WD-BILL-A-049. Sources: WD-BILL-A-050. Completeness: WD-BILL-A-051. Conflicts: WD-BILL-A-052. Kansas-vs-H.R.-25 crosswalk: WD-BILL-A-053. CWC-CE-136 Git handoff: WD-BILL-A-054. Closure: WD-BILL-A-055. Combined Git handoff: WD-BILL-A-056.

Human Engineering Intent (WD-BILL-A-007 / WD-BILL-A-008) is used **only as a crosswalk**. This CWC does not convert evidence findings into RETAIN / TRANSFORM / DISAPPEAR.

---

## 1. Executive finding

Kansas currently creates compulsory governmental consumption-tax claims through **four evidenced core legal architectures**, plus **one special-purpose local overlay class**:

| ID | Claim | Distinct legal claim? |
|---|---|---|
| KRU-D04-001 | State retailers' sales tax (K.S.A. 79-3603) | YES |
| KRU-D04-002 | State compensating use tax (K.S.A. 79-3703) | YES — complementary economic function; **do not double-count fiscal totals** |
| KRU-D04-003 | Local retailers' sales tax (K.S.A. 12-187 / 12-189) | YES — state enabling + local imposition; **LOCAL IMPLEMENTATION VARIABLE** |
| KRU-D04-004 | Local compensating use tax (K.S.A. 12-198) | YES — imposed by every city/county/municipal university imposing a retailers' sales tax, at the **same rate** |
| KRU-D04-005 | Special-purpose district local sales/use overlays (CID / TDD / STAR class) | YES as a **class**; ordinary city/county **rate variations are not extra rows** |

Counted verified Domain 04 claim-category records: **5**. Count follows evidence. Human dispositions: **ALL BLANK**.

Kansas **taxes tangible personal property sold at retail plus specifically enumerated services** (79-3603(a)–(x)). It does **not** tax all services except exemptions. It does **not** provide a general H.R. 25-style business-purpose exemption. Used property sold by a retailer is generally **taxable**. Isolated/occasional sales are generally **exempt**, except **motor vehicles and trailers** (79-3603(o); 79-3606(l)). State food-and-food-ingredients rate is **0% commencing January 1, 2025**; **local** food tax remains (79-3603d; **12-189a(d)**; KDOR Notice 24-21). CWC-CE-137: SB 33 **not** current law; Tax Facts Table 5 combined local sales/use FY2025 **$1,731,014 thousand**; CID/TDD/STAR enabling statutes retrieved; count remains **5**.

**CURRENT KANSAS SALES / USE TAX is not the Bill A replacement tax.** H.R. 25 remains a **federal economic model**, not Kansas law.

Completeness: **DOMAIN 04 SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS** (WD-BILL-A-051). Kansas Government Revenue Universe: **NOT CERTIFIED**. KLRS: **NOT CERTIFIED**. Bill A maturity: **19% UNCHANGED**. Domain 05: **NOT EXECUTED**.

---

## 2. Method and discovery principle

Audit by legal authority + taxable event + taxable property/service + obligated party + collector/remitter + rate + sourcing + exemption + destination + economic function — **not** merely by the label “sales tax.”

A claim belongs in Domain 04 only when evidence establishes that its **principal function** is a sales/use/consumption revenue claim.

Do **not**:

- pull Domain 01 excise claims into Domain 04 merely because they occur at retail;
- pull Domain 05 fees into Domain 04 merely because they occur during a transaction;
- double-count the same claim because different parties collect/remit it;
- create a row for every city, county, local rate, seller type, remote seller, marketplace facilitator, exemption, taxable service, food transaction, retailer, or filing method.

PRIMARY-LEGAL and GOV-DATA remain distinguishable. AI/search results are discovery aids only. Introduced bills are not current law. Historical phase-down rates are not presented as current.

---

## 3. State retailers' sales tax (KRU-D04-001)

### 3.1 Legal authority and taxable event

K.S.A. 79-3603 (2025 PDF) levies a tax for the **privilege of selling tangible personal property at retail or rendering or furnishing services taxable under the Kansas retailers' sales tax act**. The tax is imposed upon **enumerated bases (a)–(x)**.

Current **state rate: 6.5%**, except food and food ingredients under 79-3603d.

On and after January 1, 2025, **18% of the tax rate** imposed pursuant to 79-3603 and 79-3603d is levied for the **state highway fund** (17% from January 1, 2023). This is a **destination of a portion of the rate**, not a second tax.

An additional **2%** may apply in designated redevelopment districts (74-8921) until bonds are paid / first-series maturity. That overlay is a **rate/destination mechanism**, not a fifth statewide claim.

### 3.2 Current-state chain (evidenced)

```text
PURCHASER
→ TAXABLE RETAIL TRANSACTION (TPP at retail OR enumerated service)
→ SALES PRICE (79-3602)
→ EXEMPTION / EXCLUSION (79-3606; resale via 79-3602(jj))
→ STATE RATE 6.5% (food 0% under 79-3603d from 2025-01-01)
→ TAX
→ RETAILER COLLECTION / REMITTANCE
→ STATE RECEIPT
→ SGF + STATE HIGHWAY FUND (18% of the rate) [+ redevelopment overlay where applicable]
```

Legal incidence is assigned as a **privilege tax on the retailer** of selling at retail / furnishing taxable services. Economic incidence: **NOT ESTABLISHED**. Retailer remittance is **not** a second claim and is **not** proof of ultimate economic source. Human intent (crosswalk only): people with money are the ultimate economic source.

### 3.3 Taxable property

Principal base: **gross receipts from the sale of tangible personal property at retail** (79-3603(a)), including used property when sold by a person engaged in the business of selling such property. Resale is structurally outside “retail sale” (79-3602(jj): any sale, lease or rental **for any purpose other than for resale, sublease or subrent**).

### 3.4 Taxable services — enumerated, not all-services

Kansas taxes **only specifically enumerated services** in 79-3603, including structurally:

- telecommunications (with 79-3673 sourcing; exclusions in the section);
- gas, water, electricity, heat sold at retail (residential/agricultural **state rate 0%** for specified delivered fuels after the 2006 rate change; commercial generally remains taxable unless a 79-3606 exemption applies);
- meals and drinks;
- admissions;
- coin-operated devices (except coin-operated laundry);
- hotel/room rental;
- renting/leasing TPP;
- dry cleaning/laundry (except coin-op laundry);
- vehicle washing;
- cable/subscriber television;
- contractor materials becoming part of realty (79-3603(l));
- recreation fees; club dues;
- isolated/occasional sale of **motor vehicles or trailers** (79-3603(o));
- installing/applying TPP, with original-construction / residence / bridge-highway exceptions (79-3603(p));
- repairing/servicing TPP (79-3603(q));
- maintenance agreements (79-3603(r));
- **prewritten computer software** and services to modify/update/maintain it, including electronic delivery (79-3603(s));
- telephone answering; prepaid calling;
- bingo/charitable raffle tickets **exempt** (79-3603(v)/(w));
- food/food ingredients via 79-3603d (79-3603(x)).

This is **not** an exhaustive service encyclopedia. Professional, medical, legal, accounting, and most other unlisted services are **outside** the enumerated list unless another paragraph captures them. **MATERIAL STRUCTURAL DIFFERENCE** from H.R. 25’s broad final-consumption service architecture.

### 3.5 Collection / remittance

The retailer collects and remits. Remote-seller economic nexus and marketplace-facilitator collection are **mechanisms of this claim (and of compensating use, as applicable)** — not extra Domain 04 rows.

---

## 4. State compensating use tax (KRU-D04-002)

### 4.1 Legal authority and taxable event

K.S.A. 79-3703 (2025 PDF) imposes a tax/excise for the privilege of **using, storing, or consuming** tangible personal property in Kansas, at **6.5%** of consideration paid. Food follows 79-3603d. The same **18% SHF share** of the rate applies from January 1, 2025. The same redevelopment **2%** overlay may apply.

79-3703(e): property purchased or leased in or out of state and subsequently used in Kansas is subject **if the same property/transaction would have been subject to retailers' sales tax if the transaction had occurred wholly in Kansas**.

KDOR consumers’ compensating-use guidance: rate matches the 6.5% state sales-tax rate; **labor services are not subject to use tax**; local use tax applies if levied by the city/county on transactions subject to state use tax.

### 4.2 Distinct legal claim; complementary function

Sales tax (79-3603) and compensating use tax (79-3703) are **distinct legal claims**. They serve complementary economic functions: tax in-state retail sales, and tax Kansas use/storage/consumption of TPP on which sales tax was not otherwise paid or credited.

**Do not double-count fiscal totals.** A transaction generally bears one or the other, not both, as to the same state consumption claim (credit/paid-elsewhere mechanics remain administrative).

Retailers’ compensating use (out-of-state seller collection) and consumers’ compensating use (purchaser remittance) are **collection variants of KRU-D04-002**, not separate claims.

### 4.3 Candidate chain (authoritative wording controls)

```text
PROPERTY ACQUIRED
→ KANSAS USE / STORAGE / CONSUMPTION
→ SALES TAX NOT OTHERWISE PAID OR CREDITED
→ USE-TAX LIABILITY (if the same transaction would have been subject to RST)
→ SELLER COLLECTION OR PURCHASER REMITTANCE
→ STATE RECEIPT (SGF + SHF share of the rate) / LOCAL WHERE LEVIED
```

Use tax generally attaches to **TPP**, not to the enumerated labor services of 79-3603. That is a current-law structural difference between the two claims.

---

## 5. Local retailers' sales tax (KRU-D04-003)

### 5.1 State enabling vs local imposition

**K.S.A. 12-187:** city and county retailers' sales taxes require **election**. City: governing body submits, or must submit on petition of not less than 10% of city electors. County: board may submit; must submit on specified petition or city/taxing-subdivision resolutions.

**K.S.A. 12-189 (2025 PDF, history through L. 2025, ch. 126, May 8):**

- City rates in **0.05%** increments, **not to exceed 2% general + 1% special**. City special-purpose taxes **expire after 10 years** from first collection.
- Countywide rates **not to exceed 1%**, in **0.25%** increments, **except** numerous county-specific statutory authorizations for higher rates/purposes.
- KDOR **administers**. Local tax **identical in application and exemptions** to the Kansas retailers' sales tax act (except as specifically provided in 12-189a).
- Collections credited to the county and city retailers' sales tax fund; remitted at least quarterly (Wilson County capital-improvements exception; redevelopment bond-fund exception).

KDOR Pub. KS-1510: cities max **3%** (2% general + 1% special); counties **1%** general unless legislative action authorizes more. Official current combined rates: KDOR **Pub. KS-1700** / rate locator. This CWC does **not** inventory every jurisdiction.

**LOCAL IMPLEMENTATION VARIABLE.** Rate variations are **not** separate claims.

### 5.2 SB 33 (2025–2026 session)

House adoption of a conference committee report on SB 33 was located (vote view 2026-04-09). **Conference / passed-chamber status is not current law.** CWC-CE-137: official SOS 2026 Session Laws chapter index (enrolled Ch. 1–157) contains **no** Senate Bill 33; Chapter 33 is **Senate Bill 334**. **UNK-D04-001: RESOLVED — NOT ENACTED / NOT CURRENT LAW** as of 2026-09-02. Current-law rate architecture remains **12-189 2025 PDF** (history through L. 2025, ch. 126).

### 5.3 Distribution (current evidence; no future formula)

Countywide sales tax is apportioned under **K.S.A. 12-192** (½ property-levy formula / population; Johnson County special rules). Revenue pledged to a special project that exceeds project cost is credited to city or county general fund. **No future Bill A distribution is designed here.**

---

## 6. Local compensating use tax (KRU-D04-004)

**K.S.A. 12-198 (2025 PDF):** a compensating use tax **is hereby imposed by every city, county or municipal university imposing a retailers' sales tax**, at the **same rate**, on using or storing TPP, registerable vehicles, or vessels. Identical in application and exemptions to the Kansas compensating tax. KDOR administers. Countywide use-tax revenue is apportioned as under 12-192.

Local use therefore **follows local sales-tax imposition automatically** under 12-198 — not a separate local election for use tax.

**K.S.A. 12-199** is an **in-state motor-vehicle local-rate differential collection mechanism** (purchaser pays the difference to the county treasurer at registration when destination local rate exceeds origin dealer rate). It is **not** a fifth Domain 04 claim. Documented under KRU-D04-004 / motor-vehicle architecture.

---

## 7. Food / food ingredients (current law as of 2026-09-02)

**K.S.A. 79-3603d (2025 PDF):** state rate on food and food ingredients:

| Period | State rate |
|---|---|
| 2023 | 4% |
| 2024 | 2% |
| **Commencing January 1, 2025 and thereafter** | **0%** |

This is a **rate schedule of the existing sales/use tax**, **not a repeal** and **not a separate claim**. Prepared food is generally excluded from the 0% schedule except listed bakery / unheated / NAICS-311 exceptions.

**PRIMARY-LEGAL:** K.S.A. **12-189a(d)** — sales of food and food ingredients remain subject to city/county taxes under 12-187 et seq. even when exempt from **state** sales tax.  
**KDOR Notice 24-21 / Pub. KS-1223:** **local city/county taxes on food remain.** CID / TDD / STAR overlays still apply where levied. CWC-CE-137: no later enacted law in the SOS 2026 chapter index was located changing the 0% state food rate. **0% RATE ≠ DISAPPEAR.**

Do not present 4% or 2% as current state food rates.

---

## 8. Resale

**PRIMARY-LEGAL:** 79-3602(jj) — “retail sale” / “sale at retail” means any sale, lease or rental **for any purpose other than for resale, sublease or subrent**. 79-3602(ii) — retailer sells to the user or consumer **and not for resale**.

**GOV-DATA:** Pub. KS-1510 — sales for resale (inventory) require an exemption certificate (ST-28A). Buyer must have a Kansas sales-tax account number (drop-shipment exception). Items must be for resale in the usual course of business; tools/equipment/fixtures used by the buyer are **not** resale. Rental-fleet vehicles purchased for leasing are treated as resale inventory (ST-28A).

**Resale exemption ≠ H.R. 25 general business-purpose exemption.**

---

## 9. Business inputs / manufacturing / production (HIGH-PRIORITY)

Kansas uses a **patchwork of specific exemptions**, not a general business-purpose exemption.

Evidenced major classes (79-3606; not exhaustive):

- ingredient/component parts for property/services produced for ultimate retail sale — 79-3606(m);
- property consumed in production, manufacture, processing, mining, drilling, refining, compounding, waste treating, providing services, or crop irrigation for ultimate retail sale — 79-3606(n);
- integrated production machinery/equipment, installation/repair/maintenance, and parts — 79-3606(kk) (ST-201);
- farm/aquaculture machinery and equipment — 79-3606(t);
- agricultural animals/feed/seed-type inputs — 79-3606(o) and related;
- project exemption certificates for qualifying government/school/hospital/correctional construction — 79-3606(d)/(e);
- specified utility exemptions / expired (w) vs current 79-3603 0% residential/ag rate.

Office equipment, ordinary business consumables, professional services, and many utilities used commercially remain **taxable unless a listed exemption applies**.

**Classification vs H.R. 25 §102:** **MATERIAL STRUCTURAL DIFFERENCE.** STRUCTURAL MATCH ≠ RETAIN. DIFFERENCE ≠ DISAPPEAR.

---

## 10. Construction

**79-3603(l):** contractors generally taxed on materials that become part of realty.  
**79-3603(p):** installing/applying TPP is taxable, with original-construction / residence / specified bridge-highway exceptions.  
**79-3606(d)/(e):** project exemption certificates for qualifying public/nonprofit/U.S. projects; contractor tools/equipment used on the job are **not** exempted by those PECs.

Kansas construction architecture taxes **contractor materials** as retail consumption in many private projects. H.R. 25 business-purpose treatment of construction inputs is a **MATERIAL STRUCTURAL DIFFERENCE** (bounded; no future design).

---

## 11. Utilities

**79-3603** taxes retail sales of gas, water, electricity, and heat, with **state rate 0%** for specified residential and agricultural delivered fuels after the 2006 statutory rate change. Commercial/industrial generally taxable unless 79-3606(kk) or another exemption applies. **79-3606(w)** residential/ag mains-delivered exemption text **expired December 31, 2005**; current residential/ag **state-rate 0%** lives in 79-3603, not in that expired exemption paragraph.

Telecommunications: enumerated taxable service with 79-3673 sourcing. Franchise / 911 / regulatory fees: **REFERRED TO DOMAIN 05** (and prepaid wireless 911 collection by marketplace facilitators under 79-5602(e) is a **fee-collection mechanism**, not a Domain 04 claim).

---

## 12. Digital / software

**79-3603(s):** prewritten computer software and services of modifying, updating, or maintaining software are taxable, **including electronic delivery**.  
**Pub. KS-1510:** customized software sales/services are **exempt**; hardware is taxable. Special sourcing exists for electronically delivered software.

**CWC-CE-137 (EDU-71R + 79-3603(s); UNK-D04-002 PARTIALLY RESOLVED):** ASP / remote access without possessory rights — administrative treatment **not taxable**. Electronic entertainment downloads generally **not TPP** when delivered electronically. Subscriber television (including internet-delivered subscriber programming) **taxable** as enumerated subscriber TV. Equating every modern “SaaS” or generic streaming-subscription label to those fact patterns: **LEGAL INTERPRETATION REQUIRED**. Taxability is **not inferred from technological similarity**. No new claim row. See WD-BILL-A-055.

---

## 13. Remote sellers (mechanism, not a claim)

**K.S.A. 79-3702(h)(1)(G) (2025 PDF):** a retailer that does not have physical/other (A)–(F) contacts is a “retailer doing business in this state” if, during the current or immediately preceding calendar year, the retailer had **in excess of $100,000** of **cumulative gross receipts** from sales to customers in Kansas (all sales in the statutory receipt test). First-time current-year threshold: collect/remit on sales **in excess of** $100,000 in that year.

This is **nexus / collection duty** for KRU-D04-001 / KRU-D04-002. **Not a separate revenue claim.**

---

## 14. Marketplace facilitators (mechanism, not a claim)

**K.S.A. 79-5602:** facilitator collects/remits if it makes or facilitates taxable sales for delivery into Kansas exceeding **$100,000** in the current or preceding calendar year (own sales **or** facilitated sales).  
**K.S.A. 79-5603:** facilitator collects on own and facilitated taxable sales and **remains liable to the state**. Agreements with marketplace sellers do not shift state liability (with specified waiver/large-seller exceptions).

KDOR Notice 21-14 (implementation): in-state facilitator → retailers’ sales tax; out-of-state → retailers’ compensating use tax.

**LEGAL TAX CLAIM remains 79-3603 / 79-3703 (and local counterparts).** Marketplace responsibility is collection/remittance.

---

## 15. Sourcing

Kansas is a **destination-based sourcing** state (Streamlined Sales Tax Project participant).

**K.S.A. 79-3670:** retail sale (excluding lease/rental) sourced to: (1) seller business location if received there; else (2) location of receipt/delivery known to seller; else (3) purchaser address in ordinary business records; else (4) address obtained at consummation / payment instrument; else (5) origin-style default (ship-from / electronic availability / service-provided location).

**K.S.A. 12-191:** local situs follows 79-3670, with **exceptions**: watercraft, modular/manufactured/mobile homes, and motor vehicles/trailers/semi-trailers/aircraft that are not transportation equipment are sourced to the **retailer’s place of business**. Isolated/occasional motor vehicle or trailer sale: situs where the sale is made (negotiation-location rule if negotiations occurred in different cities/counties).

Telecom: **79-3673**. This CWC does **not** design a future Bill A distribution formula.

---

## 16. Used property and occasional/casual sales (HIGH-PRIORITY)

**Used property sold by a retailer:** generally **taxable** as TPP at retail (79-3603(a)). Kansas does **not** generally exempt used goods.

**Isolated or occasional sales:** exempt under 79-3606(l), **except** isolated/occasional **motor vehicles** specifically taxed under 79-3603(o). Definition: 79-3602(q) — nonrecurring sale by a person **not engaged at the time in the business** of selling such property/services; includes specified repossession and limited auction/agent sales; religious organization nonrecurring sale of property acquired for resale is deemed not engaged in that business.

**Pub. KS-1510:** garage/estate/farm-type infrequent sales by non-dealers generally not taxed; **isolated/occasional motor vehicle or trailer is taxable**. Inventory sold in a business liquidation remains taxable; fixtures may qualify as isolated if tax was previously paid.

**Used mobile/manufactured homes:** 79-3606(bb) exempts sales other than the original retail sale.

**Do not assume USED = EXEMPT or USED = TAXABLE as a single Kansas rule.** Architecture: **retailer used-goods taxable; casual TPP generally exempt; vehicles/trailers taxable even if isolated.**

H.R. 25 (XW-HR25-001 / proposed IRC §2(14)): **used property excluded from “property.”** **MATERIAL STRUCTURAL DIFFERENCE.**

---

## 17. Mixed use / business-to-personal conversion (HIGH-PRIORITY)

**79-3703(e)** taxes subsequent Kansas use of property if the same transaction would have been subject to retailers’ sales tax.  
**Pub. KS-1510** filing examples include **personal use of inventory** (withdrawn goods treated as taxable).  
**79-3606(d)** contractor misuse of PEC materials: tax becomes due; criminal misdemeanor for unauthorized disposal without paying tax.

No general H.R. 25-style mixed-use allocation statute (business vs personal percentage) was located. Kansas relies on **category exemptions + use tax if exempt property is later used in a taxable way**, plus inventory-withdrawal examples. **CWC-CE-137 architecture: CATEGORY-SPECIFIC MECHANISMS ONLY / NO GENERAL EQUIVALENT LOCATED.** UNK-D04-003 **PARTIALLY RESOLVED**. No future design.

---

## 18. Motor vehicles; rentals/leases; excise stacking

**Sales/use on vehicle purchases:** 79-3603(a)/(o); local 12-191 origin sourcing for dealer sales; 12-199 destination local-rate catch-up. Keep separate from:

- Domain 01 vehicle rental excise (**KRU-D01-011**);
- Domain 02 property / in-lieu vehicle taxation;
- Domain 05 registration/title fees.

**Rentals/leases of TPP:** 79-3603 enumerated base; 79-3602(kk) dwelling lease **>28 consecutive days** is not a “sale.” Rental-fleet purchases: resale (KS-1510). Vehicle **rentals** are **not** the 12-199 local compensating-use vehicle-registration mechanism (KS-1526).

**Excise stacking (relationship only; Domain 01 not reopened):**

- Motor fuel: 79-3606(a) exempts motor-vehicle fuel **upon which sales or excise tax has been paid, not subject to refund**. Bounded class: **SPECIAL INTERACTION** (general case RST-exempt when conditions met; residual refund/exception treatise **EVIDENCE REQUIRED**). Domain 01 not reopened. **CURRENT STACKING ≠ FUTURE BILL A STACKING AUTHORIZATION**.
- Cigarettes/e-cigarettes: 79-3606(a) **excepts** them — **GENERAL SALES TAX ALSO APPLIES**.
- Vehicle rental (79-5117) and new tires (65-3424d): excepted from 79-3606(a) — **GENERAL SALES TAX ALSO APPLIES**.
- Transient guest tax (KRU-D01-013) stacks with 79-3603 lodging — **GENERAL SALES TAX ALSO APPLIES**.
- Bingo: 79-3603(v)/(w) sales-tax exempt; Domain 01 KRU-D01-014 remains the bingo tax — **GENERAL SALES TAX EXEMPT**.
- Mineral severance: **NOT MATERIAL** as a retail-consumption interaction in this bounded review. See WD-BILL-A-055 §8.

Lottery/casino: **REFERRED TO DOMAIN 08** (prior Domain 01 referral). Sales/use relationship: bingo tickets exempt; other gaming not reopened.

---

## 19. Exempt organizations / agriculture / medical / tax-base mechanics

Structural exemption classes (not an inventory of certificates): government and political subdivisions (79-3606(b), with business-use exceptions); schools/educational institutions (c); hospitals/blood banks (b); contractor PECs (d)/(e); prescription drugs (p); insulin (q); specified durable medical (r); isolated sales (l); agriculture (o)/(t); used manufactured homes (bb).

**Bad debts / returns / coupons / trade-ins:** KS-1510 / 79-3602 sales-price rules. Bad-debt deduction is a **base adjustment**, not a claim. Manufacturer coupons reimbursed to the seller remain in sales price; seller-funded discounts generally reduce price (79-3602). Not converted into rows.

---

## 20. Fiscal scale

**Do not equate current receipts with required Bill A replacement revenue.**

KLRD Tax Facts 2025 Supplement (thousands, taxes levied for collection, FY2025):

| Line | Levy-for-collection | SGF | Other Funds |
|---|---|---|---|
| Retail Sales | $3,191,983 | $2,581,699 | $610,284 |
| Compensating Use | $1,088,011 | $893,761 | $194,250 |

DoA June FY2025 SGF final: Retail Sales **$2,581,698,730**; Compensating Use **$893,761,380**; combined SGF **$3,475,460,110**.

CRE Nov 2025 notes food-rate reduction and **shift of receipts from SGF to SHF**. Estimates ≠ actuals. Other Funds columns are consistent with the statutory **18% of rate to SHF** (not a second tax).

Local sales/use: state-collected. **Do not add local distributions to SGF.** CWC-CE-137: Tax Facts 2025 Supplement Table 5 Exhibit **Local Sales and Use FY2025 $1,731,014 thousand** (Counties $876,062k; Cities $763,613k; special-district footnote 5 $91,339k). Isolated local sales-only vs use-only split: **EVIDENCE REQUIRED**. Table 1 combined “Sales and Use” FY2025 **$6,011,008 thousand** = Retail $3,191,983k + Use $1,088,011k + Local $1,731,014k (footnote 2: state+local). **Not** a third tax. **Not** replacement-revenue need.

---

## 21. Dependencies

| Item | Classification |
|---|---|
| 18% of state sales/use **rate** to State Highway Fund (79-3603 / 79-3703) | **DEPENDENCY VERIFIED** (destination). Impairment if disappeared: **LEGAL EFFECT UNKNOWN** |
| Local government reliance on 12-187/12-189/12-198 receipts | **DEPENDENCY VERIFIED** (statutory remittance). Retention not inferred |
| 12-192 county/city apportionment | **DEPENDENCY VERIFIED** as current distribution. Not a future formula |
| Redevelopment / STAR extra 2% until bonds paid (74-8921; 12-189 redevelopment bond fund) | **POTENTIAL DEPENDENCY** / destination overlay. Impairment: **LEGAL EFFECT UNKNOWN** |
| CID 12-6a31 additional ≤2% / TDD 12-17,145 additional ≤1% | **POTENTIAL DEPENDENCY** (project/bond). Enabling **TRACED** |
| STAR 12-17,169 increment pledge of **existing** state/local sales/use | **DEPENDENCY VERIFIED** as statutory pledge architecture; project-level **POTENTIAL DEPENDENCY**. Not a sixth claim |
| IMPACT / other Domain 03 transfers | Not Domain 04 |

Dependency ≠ RETAIN. No impairment analysis.

---

## 22. Constitutional sweep (bounded)

No Kansas constitutional provision was located that **mandates** a state retailers’ sales tax or compensating use tax analogous to Kan. Const. art. 11, § 2 (income) or art. 11, § 1 (property uniformity).

| Finding | Class |
|---|---|
| Sales/use taxation exists by **statute** (Ch. 79 art. 36/37; Ch. 12 local enabling) | **AUTHORITY VERIFIED** (statutory) |
| Specific constitutional **mandate** to impose sales/use tax | **Not located** — do not infer statutory authority is constitutionally required |
| Art. 11, § 1 uniformity | **NOT APPLICABLE TO DOMAIN 04 UNDER EVIDENCE REVIEWED** — property classification/uniformity; Revisor annotation 117 *City of Chanute*, 156 Kan. 538 (inapplicable to license/excise including sales and use) |
| Local election requirements (12-187) | Statutory **LIMITATION VERIFIED** on local imposition |
| Home-rule sales tax independent of 12-187 | **EVIDENCE REQUIRED** / not assumed |

Constitutional authorization ≠ Human retention decision.

---

## 23. AGCL trace (never SATISFIED)

| Control | Domain 04 classification |
|---|---|
| 00A Clear signal before claim | **QUESTION REQUIRED** — current RST/use law provides identifiable statutory signals (authority, event, party, rate, collector, timing, destination, exemption) but this CWC does **not** self-certify Human-intent signal compliance |
| 00C Taxable event / base | **POTENTIAL CONFLICT** surface vs Human intent: Kansas taxes used retailer goods, enumerated-only services, and many business inputs; H.R. 25 / Human intent centers on **new final consumption**. Also **PROVISIONAL ALIGNMENT** surface: retail consumption event exists. Neither is SATISFIED or a disposition |
| 00H Constitutional / statutory authority | **PROVISIONAL ALIGNMENT** that current claims have statutory authority; **QUESTION REQUIRED** as to post-Bill-A authority. Current existence ≠ future authority |
| Other 00A–00J | **NOT APPLICABLE** or **EVIDENCE REQUIRED** where not reached. **Never SATISFIED** |

---

## 24. Cross-domain referrals (stop; do not execute)

| Item | Referral |
|---|---|
| Motor-fuel / cigarette / liquor gallonage / tire / drycleaning environmental / vehicle rental excise / transient guest / bingo | Domain 01 (existing KRU-D01 rows) |
| Vehicle property / in-lieu | Domain 02 |
| Income / privilege | Domain 03 |
| Registration/title; franchise; 911; occupation licenses | Domain 05 |
| Penalties/interest on sales/use | Domain 07 |
| Lottery / casino enterprise | Domain 08 |
| Intergovernmental local remittance **as transfer class** (state collection → local treasurer) | Administrative path of KRU-D04-003/004; Domain 09 not opened as a separate tax |
| Bond proceeds | Domain 10 |

---

## 25. Signal analysis (evidence only)

Where current sales/use law establishes a compulsory claim, identifiable legal signals exist for **authority** (statute), **taxable event** (retail sale / use-storage-consumption), **obligated party** (retailer privilege; purchaser use-tax liability), **rate** (6.5% / 0% food / local variable), **collection duty** (retailer, remote seller over threshold, marketplace facilitator, or consumer), **timing** (returns; vehicle registration for 12-199), **destination** (SGF/SHF/local funds), and **exemption** (79-3606; certificates). This is **not** self-certified compliance with Human intent.

---

## 26. Controls preserved

HG-D1 **NOT PASSED**. SPEC **NONE**. HG-D2 **NOT PASSED**. Maturity **19% UNCHANGED**. LOU-004 remains **DRAFT / CANDIDATE / NOT HUMAN-ACCEPTED**. Domain 05 **NOT EXECUTED**. No Kansas FairTax rate, replacement-revenue, prebate, retailer-compensation, transition, or future distribution formula. No operative or criminal drafting. No publication. No commit/push.
