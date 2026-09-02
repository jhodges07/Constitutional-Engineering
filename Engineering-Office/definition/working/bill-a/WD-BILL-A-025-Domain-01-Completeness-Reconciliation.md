# WD-BILL-A-025 — Domain 01 Completeness / Reconciliation

**Document ID:** WD-BILL-A-025  
**Title:** Domain 01 Completeness and Reconciliation Report  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-127; CWC-CE-128  
**Governing method:** WD-BILL-A-020 CMP-A–U  
**Governing LOU candidate:** LOU-004 Draft 0.9 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING — DOMAIN 01 **SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS** — STATEWIDE UNIVERSE **NOT CERTIFIED** — NOT ACCEPTED  
**Version:** 0.2.0  
**Effective Date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-025-Domain-01-Completeness-Reconciliation.md  
**Source ID:** SRC-BILL-A-054  

```text
DOMAIN 01 COMPLETENESS ONLY
KANSAS GOVERNMENT REVENUE UNIVERSE IS NOT CERTIFIED
DO NOT TREAT GAPS AS ABSENCE OF CLAIMS
```

---

## 1. Domain classification

**DOMAIN 01 SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS**

Basis: KDOR official business-tax-type index was used as the primary GOV-DATA sweep surface for excise-labeled and excise-adjacent claims; each counted row was tied to current Revisor/Legislature statutory text (or, for 79-3492, official 2026 HTML quotation); FY2025 KDOR Annual Report rate and destination tables were reconciled to those statutes; CWC-CE-128 closed destination statutes, classified gaming off Domain 01, matched KLRD Tax Facts FY2024 named lines, matched ACFR aggregates, and retrieved the KDOR TGT rate list. Gaps below remain explicit. Completeness is **not** omniscience and is **not** a statewide Universe certification. **Not upgraded** to COMPLETE UNDER DEFINED METHOD.

---

## 2. CMP-A–U as applied to Domain 01

| ID | Control | Domain 01 result |
|---|---|---|
| CMP-A | Constitutional authority sweep | **NOT PERFORMED** as a constitution-wide sweep. Individual claims rest on statutes. Constitutional dedication of highway/SGF `[CITATION/TEXT NEEDED]`. |
| CMP-B | Statutory title/chapter sweep | **PARTIAL.** Targeted: K.S.A. Ch. 79 arts. 33, 34, 41, 41a, 42, 51; Ch. 41 art. 5; Ch. 12 art. 16 TGT; Ch. 65 art. 34 tire; Ch. 75 art. 51 bingo. Not a line-by-line read of all K.S.A. |
| CMP-C | Session-law / recent-change check | **PARTIAL.** History lines recorded. Introduced 2026 bills flagged as **not current**. 79-41a03 includes 2024 Special Session amendment (STAR bonds). |
| CMP-D | KDOR revenue/tax-type reconciliation | **PERFORMED** against https://www.ksrevenue.gov/bustaxtypes.html. Indexed excise/excise-type items mapped to rows or to D01-INV referrals. Lottery/casino **not** on that KDOR list. |
| CMP-E | KLRD tax/revenue publication reconciliation | **PERFORMED** against KLRD Tax Facts 2024 Supplement (updated Jan 2025) FY2024 named lines. FY2025 Tax Facts not retrieved. |
| CMP-F | State budget revenue-source reconciliation | **PARTIAL / EVIDENCE ACCESS BLOCKED.** April 2025 and Spring 2026 CRE short-memo PDFs returned HTTP 500 this session. November 2024 CRE long memo PARTIAL. |
| CMP-G | ACFR / financial-statement reconciliation | **PERFORMED at aggregate level.** SGF “Tobacco and liquor taxes” and “Severance taxes” aggregated; motor fuels inside Highway Fund with sales/use/registration. Lottery reported as enterprise. |
| CMP-H | Agency fee/revenue authority | **PARTIAL.** ABC gallonage/drink/enforcement covered. Lottery/casino classified and **referred** (not Domain 01 counted). |
| CMP-I | Local-government authority sweep | **PARTIAL.** TGT enabling verified; KDOR-administered implementation list retrieved. Other local excises not exhaustively searched. Non-KDOR TGT incomplete. |
| CMP-J | County revenue-authority reconciliation | **PARTIAL** — KDOR TGT county list only. |
| CMP-K | City revenue-authority reconciliation | **PARTIAL** — KDOR TGT city list only. |
| CMP-L | School-district | **NOT APPLICABLE** to Domain 01 on evidence retrieved (no school excise found; absence is not proof). |
| CMP-M | Township / special-district | **NOT PERFORMED.** |
| CMP-N | Bond / debt revenue-source | **PERFORMED for identified Domain 01 streams.** Liquor-drink STAR 79-41a03(d)(2); liquor-enforcement STAR 79-4108(c); motor-fuel SHF pledge 68-2320 + ACFR. Specific indenture **not sampled**. Federal-aid POTENTIAL only. |
| CMP-O | Duplicate / alias normalization | **PERFORMED** for counted rows (e.g. AR25 “liquor excise” = liquor drink tax 79-41a02; gasoline/gasohol/E85 share 79-3408; 65-3424 vs 65-3424d). |
| CMP-P | Economic-function normalization | **PERFORMED** at Domain 01 working level (volume, pack, wholesale-price, gross receipts, severance, local lodging). |
| CMP-Q | Unexplained Domain 01 receipt report | **NARROWED.** Mineral net vs SGF closed as different accounting bases (CF-D01-007). AR25 “Other Taxes and Fees” and ABC aggregate lines still not fully allocated to KRU-D01 IDs. FY2025 cigarette/tobacco SGF $96,261,221 remains combined; KLRD FY2024 splits cigarette/tobacco/e-cig. |
| CMP-R | Unmatched-legal-authority report | CF-D01-002 closed (AR25 source error). CF-D01-001 closed as different accounting concepts. CF-D01-008 opened (79-3425 cites expired 79-34,161). |
| CMP-S | Source-gap report | See §3. |
| CMP-T | Domain-coverage matrix | Domain 01 executed; 02–12 **not executed**. Statewide coverage **not** claimed. |
| CMP-U | Exception / unknown register | WD-BILL-A-026. |

---

## 3. Source-gap report (Domain 01)

| Gap | Effect |
|---|---|
| KLRD Tax Facts FY2025 / Briefing Book | FY2024 matched; later editions not retrieved |
| CRE April 2025 / Spring 2026 PDFs | HTTP 500 this session — EVIDENCE ACCESS BLOCKED |
| 75-5182(e) | CURRENT VERSION TO BE VERIFIED |
| Local TGT not administered by KDOR | AUTHORITY vs KDOR implementation bounded; non-KDOR home-rule INCOMPLETE |
| KAR (administrative regulations) | Not fetched; legally material rate/admin details may live there |
| Exhaustive Ch. 79 / Ch. 12 / home-rule charter ordinances | Possible additional local commodity/activity levies |
| Sampled highway bond indenture | Statute 68-2320 + ACFR used; EXAMPLE DOCUMENT not sampled |
| CMP-A constitutional sweep | Still not performed as a constitution-wide sweep |

---

## 4. KDOR Business Tax Types mapping (CMP-D)

| KDOR index item | Domain 01 treatment |
|---|---|
| Cigarette/Tobacco Products | KRU-D01-004, 005, 006 |
| Liquor Drink | KRU-D01-008 |
| Liquor Enforcement | KRU-D01-009 |
| Mineral | KRU-D01-010 |
| Motor Fuel | KRU-D01-001, 002, 003 |
| Tire Excise | KRU-D01-012 |
| Transient Guest | KRU-D01-013 |
| Vehicle Rental Excise | KRU-D01-011 |
| Charitable Gaming Bingo/Raffles | Bingo → KRU-D01-014; raffle license fee remains D01-INV / Domain 05 until separately evidenced |
| Clean Drinking Water / Water Protection | D01-INV-002 → Domain 05 |
| Dry Cleaning Environmental Surcharge/Solvent Fee | D01-INV-001 → Domain 05 |
| Drug Tax Stamps | D01-INV-006 → Domain 07 |
| Privilege (banks/trusts/S&Ls) | D01-INV-007 → Domain 03 |
| Sand Royalty | D01-INV-005 → Domain 11/12 |
| Sales / Use / Income / Withholding / Franchise / Corporate | Out of Domain 01 |

Gallonage tax is administered by ABC and appears in AR25, not as a separate bullet on the business-tax-types landing page; it is still verified (KRU-D01-007).

---

## 5. What this CWC does **not** certify

- Completeness of the Kansas Government Revenue Universe.
- Completeness of Domains 02–12.
- That every Kansas local ordinance has been read.
- That no additional state excise exists outside the KDOR index.
- Post-Bill-A KLRS membership.
- Any RETAIN / TRANSFORM / DISAPPEAR.

---

## 6. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-02 | CWC-CE-127 Domain 01 completeness: substantially complete with explicit gaps. |
| 0.2.0 | 2026-09-02 | CWC-CE-128: CMP-E/G performed; CMP-F blocked; destination statutes closed; completeness **not** upgraded. |
