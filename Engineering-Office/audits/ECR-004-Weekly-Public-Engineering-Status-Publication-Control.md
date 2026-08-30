# ECR-004 — Weekly Public Engineering Status Publication Control

**Document ID:** ECR-004  
**Title:** Weekly Public Engineering Status Publication Control  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-076 — Weekly Status Authority-Gap Closure and Control Design; CWC-CE-077 — Weekly Status Architecture Git Gate and ECR-004 Control Acceptance Gate  
**Related Prior Work:** CWC-CE-073 (architecture); CWC-CE-074 (ChatGPT↔GitHub↔Cursor FULL PASS); CWC-CE-075 (WSPC-001 proposed production contract; OUTCOME B)  
**Status:** Approved  
**Disposition:** HUMAN ACCEPTED — APPROVED FOR CONTROL IMPLEMENTATION  
**Implementation State:** NOT YET IMPLEMENTED  
**Operative Authority:** NONE — STD-011 not yet amended; ECR acceptance alone does not activate weekly-status CONTROL  
**Version:** 0.2.0  
**Effective Date:** 2026-08-30 (Human acceptance of change intent; operative packaging rules await implementation CWC)  
**Primary Category:** STD  
**Secondary Categories:** ADM, REP, PUB  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  
**Acceptance Recording Agent:** CE-GitManager  

---

## 0. Activation Banner

```text
HUMAN ACCEPTED
APPROVED FOR CONTROL IMPLEMENTATION
NOT YET IMPLEMENTED
STD-011 NOT MODIFIED BY CWC-CE-077
```

Human Engineer acceptance under CWC-CE-077 authorizes a **later** controlled implementation of the approved STD-011 extension.  
This ECR remains **non-operative for packaging** until that implementation CWC is completed and verified.  
CWC-CE-077 does **not** amend STD-011, authorize a phone POC, authorize weekly production, or authorize social-media publication.

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
| Implementation State | **NOT YET IMPLEMENTED** |
| STD-011 amendment | Deferred to a separately authorized implementation CWC |
| Phone POC / weekly production / social publication | **Not** authorized by this acceptance |

Scope verification under CWC-CE-077 confirmed ECR-004 does **not** materially exceed the CWC-CE-076 Option D boundaries (Human supremacy; public representation ≠ engineering truth; evidence → AI proposal → HE-approved status → mechanical representation; AI cannot approve itself; HE-gated percentages; WF-001 Git gates; Human-controlled publication; FIXED anti-drift; VARIABLE fields limited to STATUS_DATE / BILL_A_PERCENT / BILL_B_PERCENT / BILL_C_PERCENT; phone as trigger only; POC ≠ production; no scheduled automation; no autonomous social publication).

---

## 10. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0-PROPOSED | 2026-08-30 | Proposed under CWC-CE-076. Not operative. Awaiting Human Engineer acceptance. |
| 0.2.0 | 2026-08-30 | CWC-CE-077: Human Engineer acceptance recorded; Status Approved; APPROVED FOR CONTROL IMPLEMENTATION; NOT YET IMPLEMENTED; STD-011 unchanged. |
