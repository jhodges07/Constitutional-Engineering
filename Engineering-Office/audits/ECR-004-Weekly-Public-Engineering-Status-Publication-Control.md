# ECR-004 — Weekly Public Engineering Status Publication Control

**Document ID:** ECR-004  
**Title:** Weekly Public Engineering Status Publication Control  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-076 — Weekly Status Authority-Gap Closure and Control Design; CWC-CE-077 — Weekly Status Architecture Git Gate and ECR-004 Control Acceptance Gate; CWC-CE-078 — Implement Weekly Status Publication Control and Public URL Requirement; CWC-CE-081 — Weekly Status Date Format and Public-Image Content Control Update; CWC-CE-082 — ISO Week Authority Integration  
**Related Prior Work:** CWC-CE-073 (architecture); CWC-CE-074 (ChatGPT↔GitHub↔Cursor FULL PASS); CWC-CE-075 (WSPC-001 proposed production contract; OUTCOME B)  
**Status:** Implemented  
**Disposition:** HUMAN ACCEPTED — IMPLEMENTED UNDER CWC-CE-078 (Verified-Closed disposition pending separate HE verification gate if required by STD-014); STD-011 Part B amended under CWC-CE-081 to Version 1.2.0; ISO-8601 `ww` authorized under CWC-CE-082 (STD-011 Version 1.2.1)  
**Implementation State:** IMPLEMENTED — STD-011 Version 1.2.1 Part B  
**Operative Authority:** STD-011 Part B (Weekly Public Engineering Status packages) is Active packaging CONTROL; this ECR does not by itself authorize weekly package generation, phone POC, or publication  
**Version:** 1.0.4  
**Effective Date:** 2026-08-30  
**Primary Category:** STD  
**Secondary Categories:** ADM, REP, PUB  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  
**Acceptance Recording Agent:** CE-GitManager  
**Implementation Agent:** CE-Engineer  

---

## 0. Activation Banner

```text
HUMAN ACCEPTED
APPROVED FOR CONTROL IMPLEMENTATION
IMPLEMENTED UNDER CWC-CE-078
STD-011 VERSION 1.2.1 PART B ACTIVE FOR WEEKLY-STATUS PACKAGING RULES
(CWC-CE-081 DATE-FORMAT / PUBLIC-IMAGE CONTENT; CWC-CE-082 ISO-8601 ww)
WEEKLY PACKAGE GENERATION / PHONE POC / SOCIAL PUBLICATION NOT AUTHORIZED BY THIS ECR ALONE
```

Human Engineer acceptance under CWC-CE-077 authorized controlled implementation.  
CWC-CE-078 implements STD-011 Part B (including PUBLIC URL REQUIREMENT).  
CWC-CE-081 amends STD-011 Part B to Version 1.2.0 (STATUS_DATE `yyyy.mm.ww`; public-image exclusions; Bill A/B/C pins; breadcrumb/Repo/acronym rules).  
CWC-CE-082 records Human authorization of ISO-8601 week-of-year for `ww` only and advances STD-011 Part B to Version **1.2.1**.  
Package generation, phone POC, and social-media publication remain separately authorized.

---

## 1. Purpose

Close **GAP-WS-001** and **GAP-WS-002** by authorizing controlled extension of **STD-011 — Public Documentation** to govern **BlueprintLiberty Weekly Public Engineering Status packages**, without collapsing WF-001 Human gates or treating public representations as engineering truth.

This ECR does **not** authorize:

- first weekly package generation;  
- phone POC execution;  
- baseline mockup fabrication;  
- deterministic renderer implementation;  
- automated percentage calculation;  
- Facebook / other platform posting;  
- activation of STD-002;  
- legislative acceptance of any bill.

---

## 2. Reason for Change

### 2.1 Problem

CWC-CE-075 (accepted OUTCOME B) recorded that:

1. STD-011 Active 1.0.0 governs Engineering Definition **LOU PDF** packages only;  
2. no ECR / dedicated CONTROL activates weekly-status production;  
3. WSPC-001 is informational only and must not be silently promoted.

Without an Active packaging CONTROL, recurring or POC weekly packages lack an operative location/naming/manifest/Git/publication boundary set.

### 2.2 Design basis

1. Prefer **extending STD-011** (public documentation surface) over inventing a parallel uncontrolled publication system (**Option A**, with POC carve-out — see §6).  
2. Preserve POL-001 / WF-001 Human supremacy for Git and publication.  
3. Preserve truth ladder: Evidence → AI-Proposed Assessment → Human-Approved Status → Mechanically Generated Representation.  
4. Keep WSPC-001 as informative contract language until HE directs otherwise; STD-011 becomes the operative packaging CONTROL after Verified implementation.  
5. Do not activate STD-002 merely for POC convenience.

---

## 3. Description of Change (Proposed)

### 3.1 Current state

| Element | Current state |
|---|---|
| STD-011 | Active 1.0.0 — LOU publication packages only |
| Weekly-status workspace | Local architecture + WSPC-001 (informational); capability-test on GitHub |
| Weekly package CONTROL | None |
| Baseline mockup | Absent (`baseline/` empty) |

### 3.2 Proposed STD-011 extension (summary)

Add a STD-011 section (or Part B) for **Weekly Public Engineering Status Packages**:

1. **Package root:**

   ```text
   Engineering-Office/publication/weekly-status/
   ```

2. **Required pairing:**

   - `reports/YYYY-MM-DD-BlueprintLiberty-Weekly-Status.md`  
   - `images/YYYY-MM-DD-BlueprintLiberty-Weekly-Status.png`  
   - corresponding `manifests/` entry  

3. **Authority:** Markdown report is the durable weekly public-status **record**; image is a controlled derivative view; neither is Engineering Definition LOU source.  

4. **Baseline:** approved visual baseline under `baseline/` with identifier, version, provenance, and checksum.  

5. **VARIABLE fields (initial):** `STATUS_DATE`, `BILL_A_PERCENT`, `BILL_B_PERCENT`, `BILL_C_PERCENT` only.  

6. **FIXED fields:** per HE-approved baseline; anti-drift validation required before package acceptance.  

7. **Percentages:** Human-approved unless a later CONTROL authorizes deterministic calculation.  

8. **Git / publication:** WF-001 HG-4 / HG-5 / HG-6 remain Human-gated; platforms are destinations only.  

9. **POC vs production:** a phone POC CWC does not authorize recurring production or autonomous publication.

Exact STD-011 normative text SHALL be authored only under a subsequent CWC after HE approves this ECR (implementation CWC), mirroring ECR-003 → CWC-CE-066 pattern.

### 3.3 IDX-001 / README-PUB updates (proposed)

After STD-011 amendment implementation:

- catalog weekly-status package class in IDX-001;  
- update README-PUB-001 / README-PUB-WEEKLY-001 pointers without promoting informational notes to CONTROL by implication.

---

## 4. POC Carve-Out (Does Not Replace This ECR)

A later Human-authorized **phone POC CWC** may proceed only after:

1. this ECR is **Approved** (or HE records an explicit temporary waiver naming which STD-011 rules are waived for one POC);  
2. GAP-WS-003 closed (approved baseline ingested);  
3. GAP-WS-006 closed (architecture + WSPC-001 on GitHub);  
4. Bill C **public title pin** accepted (Kansas NBEF Act / Node-Based Educational Framework) without implying legislative enactment;  
5. HE-approved percentages / narrative for that POC week.

POC success does **not** auto-authorize recurring production.

---

## 5. Impacts

| Area | Impact |
|---|---|
| STD-011 | Scope extension (after approval + implementation CWC) |
| weekly-status workspace | Becomes controlled packaging surface |
| LOU packages | Unchanged |
| AGCL/NBBF/NBEF/CDT/Legislative-Manager | No normative edit under this ECR |
| Automation | Not authorized |

---

## 6. Alternatives Considered

| Option | Summary | Disposition |
|---|---|---|
| A — Extend STD-011 via ECR | Aligns public docs under one standard | **Recommended permanent path** |
| B — Dedicated weekly STD/SPEC | Clean separation; more catalog surface | Acceptable later if STD-011 becomes overloaded |
| C — POC-only CWC authority | Faster demo; weak permanent control | **Allowed only as temporary bridge after HE approval**, not as permanent substitute |
| D — Combination | A for permanent + C for first phone POC after minimum closures | **Recommended overall architecture** |

---

## 7. Implementation Requirements (After HE Approval)

1. Human Engineer **Approves** ECR-004.  
2. Separately authorize implementation CWC (STD-011 amendment + IDX/README updates).  
3. Do not generate weekly packages under the implementation CWC unless that CWC expressly says so.  
4. Verified-Closed disposition follows STD-014 / HE acceptance (pattern of ECR-003).

---

## 8. Verification Criteria (Future)

Verification Pass requires:

1. STD-011 contains weekly-status package rules;  
2. LOU package rules remain intact;  
3. WSPC-001 not silently marked Active CONTROL;  
4. WF-001 gates preserved in text;  
5. no weekly package fabricated solely to “prove” the ECR.

---

## 9. Human Acceptance (CWC-CE-077)

| Field | Value |
|---|---|
| Approver | Human Engineer |
| Decision | **Approved** — HUMAN ACCEPTED / APPROVED FOR CONTROL IMPLEMENTATION |
| Date | 2026-08-30 |
| Governing Acceptance | CWC-CE-077 |
| Acceptance Basis | Explicit Human Engineer decisions in CWC-CE-077 Decision 4 (control-change intent accepted subject to scope verification against CWC-CE-076 Option D) |
| Implementation State | **IMPLEMENTED** under CWC-CE-078 (STD-011 Version 1.2.1 Part B after CWC-CE-081/082 amendments) |
| STD-011 amendment | Completed under CWC-CE-078; amended under CWC-CE-081 to Version 1.2.0; ISO-8601 `ww` under CWC-CE-082 to Version 1.2.1 |
| PUBLIC URL REQUIREMENT | Integrated (`PUBLIC_URL_01` = BlueprintLiberty.com) |
| Phone POC / weekly production / social publication | **Not** authorized by ECR acceptance or STD-011 amendment alone |

Scope verification under CWC-CE-077 confirmed ECR-004 does **not** materially exceed the CWC-CE-076 Option D boundaries (Human supremacy; public representation ≠ engineering truth; evidence → AI proposal → HE-approved status → mechanical representation; AI cannot approve itself; HE-gated percentages; WF-001 Git gates; Human-controlled publication; FIXED anti-drift; VARIABLE fields limited to STATUS_DATE / BILL_A_PERCENT / BILL_B_PERCENT / BILL_C_PERCENT; phone as trigger only; POC ≠ production; no scheduled automation; no autonomous social publication).

---

## 10. Implementation Record (CWC-CE-078)

| Field | Value |
|---|---|
| Implementing CWC | CWC-CE-078 |
| STD-011 ending version | 1.1.0 |
| Part B sections | §§21–35 |
| PUBLIC URL pin | `PUBLIC_URL_01` = BlueprintLiberty.com |
| Bill C public title pin preserved | Kansas NBEF Act (Node-Based Educational Framework) |
| Baseline present | NO — next hard prerequisite |
| Renderer implemented | NO — deferred to later CWC after baseline ingest |
| Weekly package fabricated | NO |

---

## 10A. Amendment Record (CWC-CE-081)

| Field | Value |
|---|---|
| Amending CWC | CWC-CE-081 |
| STD-011 ending version (as of CWC-CE-081) | 1.2.0 |
| STATUS_DATE display form | `yyyy.mm.ww` (compact on public image; no legend) |
| Week-of-year (`ww`) algorithm (as of CWC-CE-081) | Was OPEN — superseded by §10B |
| Public-image exclusions | Engineering metadata / development strip excluded (STD-011 §25A) |
| Template identity | `BL-Weekly-Status-Template-v1.0.png` under `templates/` (not public content; not baseline) |
| Baseline present | NO — GAP-WS-003 remains OPEN |
| Renderer implemented | NO — GAP-WS-004 remains OPEN |

---

## 10B. Amendment Record (CWC-CE-082)

| Field | Value |
|---|---|
| Amending CWC | CWC-CE-082 |
| Human decision | ACCEPT CWC-CE-081 OUTCOME B; authorize ISO-8601 `ww` |
| STD-011 ending version | **1.2.1** |
| STATUS_DATE form | `yyyy.mm.ww` |
| `yyyy` | Calendar year of KSB Status date (NOT ISO week-numbering year) |
| `mm` | Calendar month of KSB Status date |
| `ww` | ISO-8601 week-of-year number (`01`–`53`); renderer MAY calculate |
| Year-boundary rule | Calendar `yyyy.mm` + ISO `ww`; do not overwrite `yyyy` with ISO week-year |
| Public-image date explanations | Prohibited (compact value only) |
| Baseline present | NO — GAP-WS-003 remains OPEN |
| Renderer implemented | NO — GAP-WS-004 remains OPEN |

ECR-004 alone still does **NOT** authorize weekly package generation, phone POC, renderer implementation, automated Bill percentages, social publication, or STD-002 activation.

---

## 10C. Amendment Record (CWC-CE-083 — Baseline Acceptance)

| Field | Value |
|---|---|
| Amending CWC | CWC-CE-083 |
| Baseline identity | `BL-WEEKLY-STATUS-BASELINE-v1.0` |
| Baseline path | `Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` |
| Baseline SHA-256 | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |
| Dimensions | 1536 × 912 |
| Human acceptance | **ACCEPTED** 2026-08-30 (exact path + SHA) |
| GAP-WS-003 | **CLOSED** |
| Renderer implemented | NO — GAP-WS-004 remains OPEN |
| Git remote integration | Pending separate Human Git gate unless already authorized |

---

## 10D. Amendment Record (CWC-CE-084 — Deterministic Renderer)

| Field | Value |
|---|---|
| Amending CWC | CWC-CE-084 |
| Renderer location | `Engineering-Office/publication/weekly-status/renderer/` |
| Renderer version | 1.0.0-CWC-CE-084 |
| Variables | `STATUS_DATE`, `BILL_A_PERCENT`, `BILL_B_PERCENT`, `BILL_C_PERCENT` only |
| Anti-drift | Implemented; unauthorized pixels must be 0 |
| Local test suite | PASS (NON-PRODUCTION) |
| GAP-WS-004 | **CLOSED** (local); Git integration separate |
| Production KSB Status | **NOT** generated under this CWC |
| Phone POC | **NOT** authorized by this amendment |

---

## 11. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0-PROPOSED | 2026-08-30 | Proposed under CWC-CE-076. Not operative. Awaiting Human Engineer acceptance. |
| 0.2.0 | 2026-08-30 | CWC-CE-077: Human Engineer acceptance recorded; Status Approved; APPROVED FOR CONTROL IMPLEMENTATION; NOT YET IMPLEMENTED; STD-011 unchanged. |
| 1.0.0 | 2026-08-30 | CWC-CE-078: STD-011 Version 1.1.0 Part B implemented; PUBLIC URL REQUIREMENT integrated; Implementation State = IMPLEMENTED; packaging CONTROL active; package generation/POC/publication remain separately gated. |
| 1.0.1 | 2026-08-30 | CWC-CE-081: records STD-011 Version 1.2.0 Part B amendment (date format / public-image content); GAP-WS-003/004 remain OPEN; ww algorithm Human-decision open. |
| 1.0.2 | 2026-08-30 | CWC-CE-082: Human-authorized ISO-8601 `ww`; STD-011 Version 1.2.1; ww algorithm blocker removed; GAP-WS-003/004 remain OPEN. |
| 1.0.3 | 2026-08-30 | CWC-CE-083: Human-accepted visual baseline `BL-WEEKLY-STATUS-BASELINE-v1.0` SHA `17F574D4…`; GAP-WS-003 CLOSED; GAP-WS-004 remains OPEN. |
| 1.0.4 | 2026-08-30 | CWC-CE-084: deterministic renderer + anti-drift locally validated; GAP-WS-004 CLOSED (Git gate separate); no production KSB Status. |
