# ECR-002 — Engineering Definition / LOU Controlled Adoption

**Document ID:** ECR-002  
**Title:** Engineering Definition / LOU Controlled Adoption  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-053 (ECR preparation); CWC-CE-054 (implementation)  
**Governing Assessment:** CER-017 — Engineering Definition and Letter of Understanding Workflow Assessment (**accepted**)  
**Governing Implementation CER:** CER-019 — Engineering Definition / LOU Implementation  
**Status:** Implemented  
**Version:** 1.1.0  
**Effective Date:** 2026-08-08  
**Primary Category:** WF  
**Secondary Categories:** ARCH, STD, TPL, ADM, BL  
**Requestor:** Human Engineer  
**Agent:** CE-Engineer  

---

## 1. Purpose

Authorize the controlled adoption of an **Engineering Definition** lifecycle and **Letter of Understanding (LOU)** operational artifact type ahead of Controlled Execution, in accordance with Human Engineer-accepted CER-017 recommendations, without weakening Human Engineer supremacy, CWC-CE authorization, ECR change control, CEP implementation control, CER evidence, Git controls, repository boundaries, or publication boundaries.

This ECR defines and now records implementation of the change package under CWC-CE-054.  
**Status = Implemented** means controlled-document amendments authorized by this ECR have been applied.  
**Status is not Verified/Closed** until independent verification (CE-Auditor) and Human Engineer closure under STD-014.

---

## 2. Reason for Change

### 2.1 Problem

The current controlled workflow (STD-001 §4; WF-001 §4) begins effectively at **CWC-CE**, assuming engineering intent, research, requirements, scope, and Human Engineer understanding are already sufficient. WF-001’s `Need Identified` stage is recognition-only and creates no durable artifact.

### 2.2 Authority conflict to resolve

WF-001 §3.1 currently states that every engineering activity begins with an approved CWC-CE. The accepted Engineering Definition architecture requires a durable understanding/requirements phase **ahead of implementation authorization**. That conflict must be resolved explicitly (see §7.3), not by informal practice.

### 2.3 Design basis

CER-017 assessed the gap and recommended:

1. New LOU operational artifact type + dedicated template  
2. Research Record / Evidence Annex (non-authoritative; avoid series sprawl)  
3. Reuse SPEC for structured Requirements (no parallel REQ series)  
4. Amend STD-001 §4 and WF-001 for dual-phase lifecycle  
5. Preserve full Controlled Execution chain unchanged in force  

---

## 3. Description of Change

### 3.1 Current state

| Element | Current state |
|---|---|
| Principal workflow (STD-001 §4) | Starts at CWC-CE |
| Operating lifecycle (WF-001) | Need Identified → CWC-CE → … |
| LOU artifact | Does not exist |
| Research/evidence Office series | Does not exist |
| Requirements pre-CWC | Not separated; CWC-CE carries specification + authorization |
| SPEC | IDX-001 Future for Office; used in Legislative-Manager practice under CWC |
| First Human work gate | WF-001 HG-1 CWC-CE Approval |
| Implementation authorization | Approved CWC-CE → ECR when required → CEP |

### 3.2 Proposed state

```text
ENGINEERING DEFINITION
Human Engineering Intent
    ↓
Research / Source Collection
(informative; provenance recorded)
    ↓
Letter of Understanding (LOU)
    ↓
Human Engineer LOU Acceptance
    ↓
Requirements / Scope Definition
(SPEC or approved equivalent)
    ↓
Human Engineer Requirements Approval / CWC-readiness
    ↓
CONTROLLED EXECUTION
CWC-CE
    ↓
Human Review / Approval
    ↓
ECR (when required)
    ↓
CEP
    ↓
Implementation
    ↓
CER
    ↓
Human Acceptance
    ↓
Git Commit
    ↓
Git Push
    ↓
Release / Publication when separately authorized
```

### 3.3 Mandatory authority rules (non-negotiable)

1. Human Engineer remains supreme engineering authority.  
2. Research is informative and does not create requirements.  
3. AI research does not create authority.  
4. LOU acceptance requires explicit Human Engineer acceptance.  
5. Silence is not acceptance.  
6. LOU acceptance **DOES NOT** authorize implementation.  
7. Requirements/SPEC acceptance **DOES NOT** authorize implementation.  
8. CWC-CE remains the discrete work-authorization mechanism.  
9. ECR remains required whenever STD-014 requires controlled change.  
10. CEP remains the implementation instruction surface.  
11. CER remains implementation/evidence reporting.  
12. Existing Git, repository, publication, and Human Acceptance gates remain intact.

### 3.4 New / activated artifact structure

| Artifact | Form | Force | Notes |
|---|---|---|---|
| LOU series | `LOU-NNN` | Agreed understanding after HE acceptance; **not** implementation authority | New operational type |
| LOU template | `TMP-002` (proposed assignment) | Template only | Derived from TMP-001 |
| Research Record / Evidence Annex | Annex to LOU (or linked annex file under LOU package) | **Non-authoritative** | No new primary series in this ECR |
| Requirements / Scope | SPEC (`SPEC-NNN`) or approved equivalent | Normative requirements after HE acceptance; **not** implementation authority | Reuse SPEC; **no REQ series** |
| Evidence classification | Normative minimum in STD-001/WF-001; optional later GUIDE | Classification ≠ authority | Avoid GUIDE dependency for adoption |

### 3.5 SPEC / Requirements disposition

1. **No parallel REQ series** under this ECR.  
2. Activate/clarify Office SPEC as the preferred structured Requirements surface after LOU acceptance for material programs.  
3. Manager-local SPECs (e.g., Legislative-Manager) remain manager artifacts and shall **cite** accepted Office LOU when Engineering Definition applies; they do not replace Office LOU.  
4. For trivial Office-only tasks, a lightweight Requirements block inside an accepted LOU package may be permitted by STD-001/WF-001, with explicit HE acceptance — material programs should use a distinct SPEC.  
5. IDX-001 shall clarify Office SPEC namespace vs manager SPEC practice to reduce collision risk (ADM).

---

## 4. Change Category

| Field | Value |
|---|---|
| Primary Category | **WF** — Workflow Change (principal lifecycle / WF-001 conflict resolution) |
| Secondary | **ARCH** — ARCH-001 / ARCH-002 workflow and artifact recognition |
| Secondary | **STD** — STD-001 (required); STD-015 (traceability); STD-008 (optional cross-reference) |
| Secondary | **TPL** — TMP-001 support + new TMP-002 LOU template |
| Secondary | **ADM** — IDX-001 catalog / numbering / navigation |
| Secondary | **BL** — Engineering Office baseline catalog update in IDX-001 |

Policy (POL-001) amendments are required for approval gates and are treated as authority-governance changes accompanying ARCH/WF (no separate POL category exists in STD-014 §3).

---

## 5. Impact Analysis

### 5.1 Architecture

| Impact | Change / no-change |
|---|---|
| Human Engineer supremacy | **No weakening** — reinforced with LOU/Requirements gates |
| Authority hierarchy ARCH→…→CWC→CEP | Preserved; LOU/SPEC added as operational artifacts **below** Standards/Workflows and **above** CWC for feed-forward only |
| Repository hierarchy | No change to AGCL/NBBF/CDT/LM/UNBKE ownership |
| ARCH-001 §8 / §9 | Amend to recognize Engineering Definition + LOU/SPEC artifact roles; optional CEWC→CWC-CE naming hygiene may be included if HE authorizes as in-scope editorial |
| ARCH-002 | Amend diagrams/text so managers consume Definition outputs; managers do not own Office LOU authority |

### 5.2 Standards

| Standard | Impact |
|---|---|
| STD-001 | **Required amendment** — artifacts (§3), workflow diagram (§4), roles, principles; dual-phase lifecycle; non-authorization disclaimers |
| STD-014 | No structural weakening; remains ECR authority for controlled changes |
| STD-015 | Optional MINOR — upstream LOU/SPEC citation in traceability when applicable |
| STD-008 | Optional — cross-reference Office Engineering Definition for legislative project initiation; no replacement of legislative lifecycle |
| STD-004 / STD-005 | **Not activated by this ECR** unless HE expands scope; LOU numbering rules shall be stated in IDX-001 + STD-001 until STD-005 Active |
| STD-002/003/006/007/009–013 | Unaffected (Reserved remain Reserved) |

### 5.3 Workflows / Templates / Prompts

| Artifact | Impact |
|---|---|
| WF-001 | **Required** — replace Need Identified→CWC-only front end; resolve §3.1 conflict; add HG-D1/HG-D2; preserve HG-1…HG-8 and AG-1…AG-5 |
| WF-002 | No change to release philosophy; release still follows Human Acceptance under Controlled Execution |
| TMP-001 | Update supported document types to include LOU (and SPEC when activated) |
| TMP-002 (new) | LOU master template including Research Annex requirements and HE Acceptance Record |
| PROMPT-EO-CE-001 | Update: may prepare LOU/research; may not accept LOU/Requirements; may not treat them as implementation authority |

### 5.4 Repositories

| Repository | Impact |
|---|---|
| Constitutional-Engineering / Engineering-Office | Only repository authorized for this ECR’s controlled amendments |
| Legislative-Manager | **Out of scope** for this ECR implementation (optional later extension CWC) |
| AGCL / NBBF / CDT / UNBKE | **Out of scope** — no modification |

### 5.5 Identifiers and references

| Identifier | Action |
|---|---|
| `LOU-NNN` | Establish series; sequential; never reuse |
| `TMP-002` | Assign to LOU template upon implementation |
| `SPEC-NNN` | Clarify Active convention for Office Requirements use; do not invent REQ |
| IDX-001 | Catalog LOU, TMP-002, SPEC posture, updated hierarchy diagrams |
| README.md | Update workflow diagram / navigation (informational; controlled docs prevail) |

### 5.6 Baselines

IDX-001 baseline listing (BL-EO-2026-08-08 or successor declaration) shall be updated when amendments are Verified, citing this ECR. Exact baseline rename/version is an implementation detail under HE direction.

### 5.7 Traceability

Proposed durable chain (additive):

```text
LOU (accepted) → SPEC/Requirements (accepted) → CWC-CE → ECR? → CEP → CER → Git / Publication
```

Existing CWC→ECR?→CEP→CER links remain mandatory for Controlled Execution.

### 5.8 Operational continuity / UNBKE

No UNBKE dependency. Technology independent.

### 5.9 Compatibility / breaking-change character

| Aspect | Character |
|---|---|
| Additive Engineering Definition | Backward-compatible for trivial/corrective work via explicit HE waiver in CWC |
| WF-001 principle rewrite | Breaking to prior literal reading of “all activity begins at CWC”; replaced by dual-phase rules in §7.3 |
| Existing CWC/ECR/CEP/CER meaning | **Non-breaking** — force preserved |
| Historical CER-017 Pending field in file | Process note: CWC-CE-053 treats CER-017 as accepted design basis; file may be updated under implementation or left historical |

### 5.10 What does not change

1. ECR requirement triggers under STD-014  
2. CEP role  
3. CER non-authorization rule  
4. Git commit/push/publication Human Engineer gates  
5. Control-document ownership boundaries  
6. Publication ≠ enactment  

---

## 6. Documents and Repositories Affected

### 6.1 Documents requiring amendment (implementation phase)

| Document | Path | Amendment class |
|---|---|---|
| ARCH-001 | `Engineering-Office/architecture/ARCH-001-Constitutional-Engineering-Architecture.md` | ARCH MINOR |
| ARCH-002 | `Engineering-Office/architecture/ARCH-002-Engineering-Manager-Architecture.md` | ARCH MINOR |
| POL-001 | `Engineering-Office/policies/POL-001-Engineering-Office-Governance.md` | Policy / authority gates |
| STD-001 | `Engineering-Office/standards/STD-001-Engineering-Workflow.md` | STD MINOR (workflow expansion) |
| STD-015 | `Engineering-Office/standards/STD-015-Constitutional-Engineering-Reports.md` | STD optional MINOR |
| STD-008 | `Engineering-Office/standards/STD-008-Legislative-Lifecycle.md` | STD optional cross-ref |
| WF-001 | `Engineering-Office/workflows/WF-001-Engineering-Office-Operating-Workflow.md` | WF MINOR/MAJOR-as-determined at implement (lifecycle rewrite of front end) |
| TMP-001 | `Engineering-Office/templates/TMP-001-Master-Document-Template.md` | TPL |
| IDX-001 | `Engineering-Office/IDX-001-Engineering-Office-Master-Index.md` | ADM / BL |
| README.md | `README.md` | Informational navigation |
| PROMPT-EO-CE-001 | `Engineering-Office/prompts/Constitutional-Engineer.md` | Prompt |

### 6.2 Documents to create (implementation phase)

| Document | Proposed path | Notes |
|---|---|---|
| TMP-002 — LOU Template | `Engineering-Office/templates/TMP-002-Letter-of-Understanding-Template.md` | Required |
| (Optional) first LOU instance | Deferred to pilot CWC | Not required to close this ECR’s document amendments |

### 6.3 Documents inspected; not amended by this ECR unless HE expands scope

| Document | Disposition |
|---|---|
| STD-004 | Reserved — leave Reserved |
| STD-005 | Reserved — leave Reserved; interim numbering in IDX/STD-001 |
| WF-002 | No amendment required for Definition adoption |
| ARCH-003 / ARCH-004 | Draft; no mandatory change for LOU adoption (ownership rules already compatible) |

### 6.4 Repositories affected

| Repository | Action under this ECR |
|---|---|
| Constitutional-Engineering | Amend/create listed Office documents only after HE approval + implementation authorization |
| All others | **None** |

---

## 7. Proposed Resolution / Implementation Plan

### 7.1 Artifact ownership

| Concern | Owning authority |
|---|---|
| Engineering Definition phase rules | Human Engineer / Constitutional Engineering Office via STD-001 + WF-001 |
| LOU instances | Human Engineer accepting authority; Constitutional Engineer / CE-Engineer may prepare |
| Research Annex | Drafted by preparer; never AI-owned; disposition via LOU acceptance |
| SPEC / Requirements | Office or designated manager steward per ARCH-002/003; HE acceptance for force |
| CWC / ECR / CEP / CER | Unchanged |
| AI | May research/draft/recommend; may not accept, own, or authorize |

### 7.2 LOU lifecycle (normative intent for STD-001/WF-001)

| State | Meaning |
|---|---|
| Draft | Under preparation |
| Under Review | Submitted for Human Engineer decision |
| Accepted | HE explicitly accepted (or accepted with conditions recorded) |
| Accepted with Conditions | Binding only with recorded conditions |
| Returned | Revision required |
| Rejected | Not accepted; retained |
| Superseded | Replaced by later accepted LOU version |
| Withdrawn | Withdrawn before acceptance |

**Revision rule:** Material understanding changes require new LOU version + re-acceptance. Editorial PATCH may be defined in template/STD-001. Changes that alter ARCH/STD/WF baselines still require STD-014 ECR.

### 7.3 Resolution of WF-001 “begins with CWC-CE” conflict

**Replace** the absolute principle with dual-phase rules:

1. **Engineering Definition** develops and accepts understanding and requirements **before** Controlled Execution for material work subject to Engineering Definition.  
2. **Controlled Execution** of implementation-class repository change **begins with an approved CWC-CE** (and ECR when STD-014 requires).  
3. **LOU acceptance and Requirements/SPEC acceptance never authorize implementation.**  
4. **Durable Engineering Definition artifacts** written into Constitutional-Engineering (LOU, Office SPEC, related annexes) are themselves governed work and require an approved CWC-CE (definition-class / assessment-class / adoption-class as applicable), except where Human Engineer records an express narrow exception under POL-001.  
5. **Exploratory research** (chat, external AI, reading) may occur without a CWC when it does **not** modify governed repository artifacts.  
6. **Waivers:** Trivial corrective/administrative Controlled Execution may waive LOU/Requirements by **explicit Human Engineer statement in the CWC**; AI may not waive.

This preserves CWC supremacy for repository modification while establishing Engineering Definition ahead of implementation authorization.

### 7.4 Research provenance rules

Research Record / Evidence Annex (non-authoritative) shall record at minimum:

| Field | Requirement |
|---|---|
| Source ID | Stable local reference |
| Source class | Taxonomy below |
| Locator | Cite / URL / export id / etc. |
| Collector | Human or AI system identity |
| Date collected | Required |
| Summary | Informative only |
| Conflicts noted | Required when present |
| Authority status | Always `Non-authoritative` until HE adopts into LOU/SPEC |

**Evidence classes (classification ≠ authority):**

`PRIMARY-LEGAL` | `GOV-DATA` | `SECONDARY-ANALYSIS` | `TESTIMONY` | `HISTORICAL` | `SCRIPTURE` | `AI-SYNTHESIS` | `CONTROL-DOC`

**AI research (ChatGPT, Grok, Cursor, etc.):** mandatory system identity, date/time, session/export id if available, prompt/context summary or link, role label `Research assistant — non-authoritative`, and HE disposition at LOU review.

**Conflicts:** record all sides; LOU marks `Unresolved` / `Accepted interpretation` / `Deferred`; AI shall not silently choose.

**Promotion path:** Research → (optional) LOU agreed statement → HE LOU acceptance → SPEC/Requirements → HE Requirements acceptance → CWC-CE authorization → …  

### 7.5 Human Engineer acceptance gates (new + preserved)

| Gate | Required before |
|---|---|
| **HG-D1 LOU Acceptance** | Treating LOU as agreed understanding input to Requirements/CWC |
| **HG-D2 Requirements Acceptance / CWC-readiness** | Issuing implementation-class CWC that depends on Engineering Definition |
| HG-1 CWC-CE Approval | CEP execution / repository implementation (unchanged force) |
| HG-2 ECR Approval | Controlled-change implementation when required (unchanged) |
| HG-3 Human Acceptance | CER closure / normal Git advancement (unchanged) |
| HG-4…HG-8 | Unchanged (Git commit/push, publication, exception, baseline) |

Silence is not acceptance at any gate.

### 7.6 Requirements / SPEC transition

Accepted LOU **feeds** SPEC/Requirements; does not equal them.  
Accepted SPEC/Requirements **feed** CWC-CE; do not replace CWC-CE approval.

### 7.7 CWC transition

Implementation-class CWC-CE shall cite, when Engineering Definition applies:

1. Accepted LOU ID + version **or** explicit HE waiver  
2. Accepted SPEC/Requirements ID + version **or** explicit HE waiver  
3. Applicable ARCH/POL/STD/WF references  

### 7.8 TMP-002 minimum content (for implementation)

1. Metadata (ID, title, status, version, dates)  
2. Human Engineering Intent  
3. Scope of understanding (in/out)  
4. Research Record / Evidence Annex (or mandatory link)  
5. Agreed understanding statements  
6. Rejected interpretations  
7. Conflicts (Unresolved / Accepted / Deferred)  
8. Open questions / assumptions / deferred items / verification status  
9. Provisional implications for Requirements (marked provisional)  
10. Authority boundary disclaimer (non-implementation)  
11. Human Engineer Acceptance Record  
12. Revision / supersession history  

### 7.9 Implementation sequence (post-approval)

1. Human Engineer approves this ECR (and any conditions).  
2. Issue implementation CWC-CE (recommended) referencing ECR-002 + CWC-CE-053.  
3. Amend ARCH-001, ARCH-002, POL-001, STD-001, WF-001 (core).  
4. Create TMP-002; update TMP-001 supported types.  
5. Update IDX-001 catalog, hierarchy, numbering conventions, baseline listing.  
6. Update README workflow diagram.  
7. Update PROMPT-EO-CE-001.  
8. Optional: STD-015 traceability; STD-008 cross-reference.  
9. Produce CER for implementation; verify per §9.  
10. Separate pilot CWC for first substantive LOU (recommended; not required to verify document amendments alone).

### 7.10 Backward compatibility

| Work type | Posture after adoption |
|---|---|
| In-flight CWCs approved before Effective Date | May complete under prior rules unless HE directs otherwise |
| New material programs | Engineering Definition applies |
| Trivial corrective/admin work | HE waiver permitted in CWC |
| Assessment/read-only CWCs | Remain valid; may produce CERs without LOU when Definition artifacts are not being created |

### 7.11 Rollback / rejection posture

| Outcome | Effect |
|---|---|
| ECR Rejected / Withdrawn | No controlled amendments; retain ECR/CER as history |
| Implementation partial failure | CER records partial; do not claim Active LOU system |
| Rollback after partial amend | Reverse via corrective ECR/CWC; do not leave half-amended authority diagrams claiming LOU Active |

### 7.12 Version impacts (planned at implementation)

| Document | Planned version impact |
|---|---|
| ARCH-001 | MINOR |
| ARCH-002 | MINOR |
| POL-001 | MINOR |
| STD-001 | MINOR (or MAJOR if HE judges dual-phase incompatible with 1.x readers — default MINOR additive) |
| WF-001 | MINOR (front-end expansion) unless HE directs MAJOR |
| TMP-001 | MINOR |
| IDX-001 | MINOR |
| README | MINOR |
| PROMPT-EO-CE-001 | MINOR |
| TMP-002 | 1.0.0 initial |
| STD-015 / STD-008 | PATCH/MINOR if touched |

---

## 8. Approval Record

| Field | Value |
|---|---|
| Approver | Human Engineer |
| Role | Human Engineer |
| Decision | **Approved for Implementation** |
| Date | 2026-08-08 |
| Conditions | Per CWC-CE-054 Human Engineer Decision (LOU-NNN; definition/; TMP-002; Research Annex; SPEC reuse; no REQ; include STD-015; do not modify STD-008; preserve non-implementation authority) |
| Authorizing Artifacts | CWC-CE-054; accepted CER-017; accepted CER-018; this ECR-002 |

AI may not approve this ECR.

---

## 9. Verification Record

| Field | Value |
|---|---|
| Implementer verification | CE-Engineer under CWC-CE-054 / CER-019 |
| Independent verifier | **Pending CE-Auditor** |
| Date (implementer checks) | 2026-08-08 |
| Result | **Pass with Follow-up** — implementer checklist complete; independent audit required before Verified/Closed |
| Evidence summary | Controlled amendments applied; TMP-002 and definition/ created; no LOU instance created; no foreign repos modified; not staged/committed |
| Follow-up | CE-Auditor independent verification; Human Engineer acceptance of CER-019; then ECR Verified/Closed |

### 9.1 Validation requirements (for implementation CER)

Before ECR-002 may reach Verified/Closed after implementation:

1. STD-001 §4 shows Engineering Definition + Controlled Execution dual-phase diagram. — **Implementer: Pass**  
2. STD-001/WF-001 expressly state LOU and Requirements/SPEC acceptance do **not** authorize implementation. — **Implementer: Pass**  
3. WF-001 CWC-start conflict resolved. — **Implementer: Pass**  
4. HG-D1 and HG-D2 exist; HG-1…HG-8 preserved. — **Implementer: Pass**  
5. LOU type cataloged in IDX-001; TMP-002 exists; TMP-001 lists LOU. — **Implementer: Pass**  
6. Research Annex non-authority rule and AI provenance requirements present. — **Implementer: Pass**  
7. SPEC reuse stated; no REQ series introduced. — **Implementer: Pass**  
8. CWC/ECR/CEP/CER force statements preserved. — **Implementer: Pass**  
9. No modifications outside Constitutional-Engineering authorized paths. — **Implementer: Pass**  
10. README/IDX navigation updated. — **Implementer: Pass**  
11. Prompt updated to forbid AI LOU acceptance. — **Implementer: Pass**  
12. Version histories updated on all amended controlled documents. — **Implementer: Pass**  
13. Independent CE-Auditor certification. — **Pending**  

---

## 10. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Proposed ECR under CWC-CE-053 based on accepted CER-017 design basis; defines Engineering Definition / LOU adoption package; implementation deferred pending Human Engineer approval and authorized implementation work. |
| 1.1.0 | 2026-08-08 | CWC-CE-054: Human Engineer Approved for Implementation; controlled documents implemented; status set to Implemented; independent verification pending CE-Auditor before Verified/Closed. |

---

## Appendix A — Success Criteria Conformance (Design)

This change package is constructed so that Engineering Definition / LOU adoption **does not weaken**:

- Human Engineer authority  
- CWC-CE authorization  
- ECR change control  
- CEP implementation control  
- CER evidence requirements  
- independent verification  
- Git controls  
- repository boundaries  
- publication boundaries  

**Design PASS.** Implementation applied under CWC-CE-054. Independent verification pending CE-Auditor before Verified/Closed.
