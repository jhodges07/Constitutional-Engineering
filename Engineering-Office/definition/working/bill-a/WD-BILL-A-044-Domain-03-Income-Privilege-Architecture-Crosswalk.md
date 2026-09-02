# WD-BILL-A-044 — Domain 03 Income / Privilege Architecture Crosswalk

**Document ID:** WD-BILL-A-044  
**Title:** Domain 03 Current-Law Income / Privilege Architecture, Taxpayer–Remitter, H.R. 25, and AGCL Crosswalk  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-133 (opened); CWC-CE-134 (79-32,288 / 79-32,113(c) chain updates)  
**Governing LOU candidate:** LOU-004 Draft 1.3 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / CANDIDATE — NOT ACCEPTED  
**Version:** 0.2.0  
**Effective Date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-044-Domain-03-Income-Privilege-Architecture-Crosswalk.md  

```text
CURRENT-LAW ARCHITECTURE ONLY
H.R. 25 IS THE FEDERAL ECONOMIC MODEL — NOT KANSAS LAW
LEGAL TAXPAYER ≠ NECESSARILY ULTIMATE ECONOMIC SOURCE
NO HUMAN DISPOSITION
NO AGCL CONTROL IS SATISFIED
NO OPERATIVE REPEAL OR FAIRTAX DRAFTING
```

---

## 1. Individual income-tax chain (current law)

```text
PERSON / TAXPAYER
→ KANSAS RESIDENT / NONRESIDENT SOURCE RULE (79-32,109)
→ FEDERAL AGI STARTING BASE
→ KANSAS MODIFICATIONS (79-32,117)
→ KANSAS AGI
→ KANSAS DEDUCTIONS AND PERSONAL EXEMPTIONS (79-32,116)
→ KANSAS TAXABLE INCOME
→ RATE / BRACKET (79-32,110(a); nonresident ratio (b); fiduciary (d))
→ PRE-CREDIT LIABILITY
→ CREDIT
→ FINAL LIABILITY
→ WITHHOLDING (79-3296) / ESTIMATED PAYMENT (79-32,101) / REMITTANCE
→ REFUND OR BALANCE DUE
→ STATE TREASURER / SGF less IMPACT and refund fund (79-32,105)
```

Do not collapse deduction, exemption, credit, withholding, or refund into one category.

---

## 2. Corporate income-tax chain (current law)

```text
CORPORATION DOING BUSINESS IN KANSAS OR DERIVING KANSAS-SOURCE INCOME
→ FEDERAL TAXABLE INCOME
→ KANSAS ADDITIONS / SUBTRACTIONS (79-32,138)
→ ALLOCATION / APPORTIONMENT IF NOT ENTIRELY KANSAS-SOURCE (79-3271–79-3293)
→ KANSAS TAXABLE INCOME
→ NORMAL TAX 4% + SURTAX 3% OF EXCESS OVER $50,000 (79-32,110(c))
→ CREDITS
→ FINAL LIABILITY
→ ESTIMATED PAYMENT / REMITTANCE
→ SGF (79-32,105)
```

Not a complete multistate treatise.

---

## 3. Financial-institution privilege chain (current law)

```text
LISTED FINANCIAL INSTITUTION DOING BUSINESS IN KANSAS (79-1106)
→ EXCLUDED FROM KANSAS INCOME TAX ACT (79-32,113(c))  [banks, trust companies, S&Ls; credit unions exempt but not in 79-1106]
→ NET INCOME (79-1109; 79-32,138 with specified adjustments)
→ BANK SCHEDULE 79-1107  OR  TRUST/S&L SCHEDULE 79-1108
→ PRIVILEGE TAX LIABILITY
→ K-130 / PAY DIRECTOR OF TAXATION (79-1110)
→ SGF (Tax Facts Table 4 100%; organic 79-32,105 analogue NOT LOCATED)
```

In lieu of **ad valorem on intangible assets**, not a restatement of KRU-D03-002. 79-32,113(c) is the Income Tax Act exclusion.

---

## 4. Electing PTE chain (current law)

```text
ELIGIBLE S CORPORATION OR PARTNERSHIP
→ ANNUAL ELECTION (79-32,286)  [if no election: owner-level KRU-D03-001 only]
→ ENTITY TAX AT HIGHEST INDIVIDUAL RATE (79-32,287)
→ ENTITY IS TAXPAYER
→ OWNER NOT LIABLE IN SEPARATE CAPACITY; CREDIT = DIRECT SHARE; EXCESS REFUNDABLE (79-32,288)
→ SGF (aggregated in income-tax reporting; isolated actuals EVIDENCE REQUIRED)
```

Do **not** add entity payments to owner receipts as additional net revenue.

---

## 5. Local 12-1,101 chain (current law)

```text
STATE ENABLING AUTHORITY (12-1,101)
→ LOCAL ORDINANCE / RESOLUTION (not automatic)
→ GROSS EARNINGS FROM MONEY, NOTES, OTHER EVIDENCE OF DEBT (12-1,102)
→ RATE WITHIN STATUTORY CAPS
→ LOCAL DESTINATION
→ OFFICIAL IMPOSING LIST: KDOR FORM 200 (not transcribed here)
```

Enabling ≠ every jurisdiction imposes.

---

## 6. Legal taxpayer / remitter / withholding agent / incidence

| Record | Legal taxpayer | Statutory remitter | Withholding agent | Economic incidence | Ultimate economic source (Human intent) |
|---|---|---|---|---|---|
| KRU-D03-001 | Individual / fiduciary | Taxpayer | Employer (79-3296) where applicable | **NOT ESTABLISHED** | People with money — **not rewritten** |
| KRU-D03-002 | Corporation | Corporation | N/A (estimated payments are remittance) | **NOT ESTABLISHED** | People with money — **not rewritten** |
| KRU-D03-003 | Listed financial institution | The institution | N/A | **NOT ESTABLISHED** | People with money — **not rewritten** |
| KRU-D03-004 | Electing PTE | The entity | N/A | **NOT ESTABLISHED** | People with money — **not rewritten** |
| KRU-D03-005 | Holder of taxed gross earnings (local) | Local / KDOR administration | N/A | **NOT ESTABLISHED** | People with money — **not rewritten** |

LEGAL TAXPAYER ≠ NECESSARILY ULTIMATE ECONOMIC SOURCE.

---

## 7. H.R. 25 / Bill A Human-intent relationship

H.R. 25 remains **FEDERAL ECONOMIC MODEL / NOT KANSAS LAW**.

| Record | Current-law trigger | H.R. 25 relationship |
|---|---|---|
| KRU-D03-001 | Taxable income / sourced income | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| KRU-D03-002 | Corporate Kansas taxable income | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| KRU-D03-003 | Privilege of listed financial business measured by net income | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| KRU-D03-004 | Elective entity-level tax on pass-through income | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| KRU-D03-005 | Gross earnings from money/notes/evidence of debt | STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| Withholding / estimated | Collection / prepayment | COLLECTION-MECHANISM ISSUE (later design); **not** a current second claim |

**HUMAN DISPOSITION = BLANK** on every row. Potential conflict ≠ DISAPPEAR.

Existing Human intent: mere existence/ownership/possession/accumulation of economic resources is not the intended taxable event. This file records the **actual current-law trigger**. It does not editorialize a future treatment.

---

## 8. AGCL 00A–00J (Domain 03 surface only)

Permitted classes only. **Never SATISFIED.**

| Control | Domain 03 classification |
|---|---|
| 00A | QUESTION REQUIRED — duration/expiration of any surviving post-Bill-A claim still empty; current income claims do not fill expiration |
| 00B | NOT APPLICABLE as a Domain 03 current-law finding |
| 00C | POTENTIAL CONFLICT surface — earning/receiving/realizing income or privilege measured by net income vs intended consumption event / property-precedes-claim architecture |
| 00D | QUESTION REQUIRED (unasked) |
| 00E | EVIDENCE REQUIRED / `[LEGAL EFFECT UNKNOWN]` if these claims disappeared; IMPACT transfer is Domain 09 candidate |
| 00F | EVIDENCE REQUIRED — completeness not certified |
| 00G | PROVISIONAL ALIGNMENT of register fields; not satisfaction |
| 00H | POTENTIAL CONFLICT surface — art. 11 § 2 **AUTHORITY VERIFIED** ≠ Human retention; 12-140 / 19-101a local limitations VERIFIED |
| 00I | NOT APPLICABLE — no criminal drafting; penalties referred to Domain 07 |
| 00J | PROVISIONAL ALIGNMENT of version-control intent; Domain 03 discovery does not authorize claims |

---

## 9. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-02 | CWC-CE-133 architecture / taxpayer-remitter / H.R. 25 / AGCL crosswalk. No dispositions. No FairTax drafting. |
| 0.2.0 | 2026-09-02 | CWC-CE-134: 79-32,113(c) exclusion; 79-32,288 owner-credit chain; Form 200 pointer. H.R. 25 / AGCL classifications unchanged. No SATISFIED. No dispositions. |
