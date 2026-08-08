# ARCH-003 — Engineering Ownership Architecture

**Document ID:** ARCH-003  
**Title:** Engineering Ownership Architecture  
**Classification:** Architecture Baseline  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Status:** Draft  
**Version:** 1.0.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This document defines the ownership architecture for the Constitutional Engineering ecosystem.

It establishes:

- Who owns repositories, documents, and managers
- How stewardship, accountability, and authority relate
- What AI agents may and may not claim as ownership
- How shared ownership, transfer, succession, and audit operate
- How ownership remains traceable for present operations and future UNBKE mapping

ARCH-003 specializes ARCH-001 for ownership. It does not replace ARCH-001.  
It complements POL-001 stewardship rules and ARCH-002 manager boundaries without redefining them.

---

## 2. Scope

### 2.1 In Scope

This architecture applies to:

1. All repositories under Constitutional Engineering Office authority  
2. All controlled Engineering Office documents (ARCH, POL, STD, WF, TMP, IDX, CWC-CE, ECR, CEP, CER, and related series)  
3. All specialized managers registered under ARCH-002  
4. Control repositories (AGCL, NBBF, CDT) as ownership peers under Office process authority  
5. Public publication surfaces receiving approved outputs  
6. Human Engineers, stewards, Constitutional Engineer, Cursor AI, and other AI agents acting under Office authority  
7. Ownership registry, transfer, succession, and audit requirements  

### 2.2 Out of Scope

This architecture does not:

1. Assign named individual humans beyond role-level stewardship defaults  
2. Modify AGCL, NBBF, or CDT control content  
3. Redefine manager domain boundaries defined in ARCH-002  
4. Replace POL-001 conduct rules or WF-001 operating sequence  
5. Require UNBKE for current ownership operations  

### 2.3 Authority Position

```
ARCH-001
    ↓
ARCH-003 (ownership architecture)
    ↓
POL-001 / Standards / Workflows
    ↓
Repository Stewards / Document Owning Authorities / Manager Stewards
    ↓
AI preparation and implementation (never ownership)
```

Ownership architecture is subordinate to ARCH-001.  
Conduct and approval gates remain governed by POL-001 and WF-001.  
Manager domain ownership remains bounded by ARCH-002.

---

## 3. Ownership Principles

The following principles are binding:

1. **Every repository has one accountable steward.**  
2. **Every document has one owning authority.**  
3. **Ownership may be delegated but remains accountable.** Day-to-day care may be assigned; accountability does not dissolve.  
4. **AI never owns engineering artifacts.**  
5. **AI may prepare work but never assume ownership.** Preparation, drafting, and implementation support are not title.  
6. **Ownership transfers require explicit authorization.** Silence, implication, or convenience do not transfer ownership.  
7. **Shared ownership requires one designated lead steward.** Multiple participants may contribute; one lead remains accountable.  
8. **Ownership is traceable and auditable.** Ownership state shall be attributable to authorizing artifacts and registry records.

### 3.1 Ownership Definitions

| Term | Meaning |
|---|---|
| Ownership | Accountable authority for integrity, change posture, and stewardship of an artifact or surface |
| Steward | Human role accountable for a repository or designated ownership surface |
| Owning Authority | Human role or designated human office responsible for a controlled document |
| Lead Steward | Designated accountable human when contribution is shared |
| Delegation | Authorized assignment of day-to-day care without transfer of accountability |
| Transfer | Explicit reassignment of accountable ownership |
| Succession | Ordered replacement of ownership when a steward becomes unavailable |

### 3.2 Non-Ownership Rule

Contribution, authorship assistance, review comments, commit recommendations, and AI-generated drafts do not create ownership.

---

## 4. Repository Ownership

### 4.1 Repository Ownership Rule

Every repository under Constitutional Engineering Office authority shall have exactly one accountable steward.

### 4.2 Default Repository Stewardship

| Repository / Surface | Accountable Steward (role-level) |
|---|---|
| Engineering-Office | Human Engineer, supported by Constitutional Engineer |
| AGCL-Control-Documents | Human Engineer / designated AGCL steward |
| NBBF-Control-Documents | Human Engineer / designated NBBF steward |
| CDT-Control-Documents | Human Engineer / designated CDT steward |
| Legislative-Manager | Human Engineer / Legislative Manager steward |
| Future Charter-Manager | Human Engineer / designated steward when established |
| Future Budget-Manager | Human Engineer / designated steward when established |
| Future managers under ARCH-002 | Human Engineer / designated manager steward upon registration |
| Public repositories / publication surfaces | Human Engineer / designated publication steward |

### 4.3 Repository Ownership Boundaries

1. Repository stewardship covers structure, integrity, access discipline, and change posture for that repository.  
2. Stewardship of a repository does not grant ownership of foreign control concepts held in peer repositories.  
3. Managers may reference control repositories; they shall not claim ownership of AGCL, NBBF, or CDT content.  
4. Public surfaces receive approved outputs; they do not acquire architectural ownership of source repositories.  
5. Repository stewardship may be recorded in the Ownership Registry (Section 15).

### 4.4 Accountability Retention

Delegation of day-to-day repository care is permitted.  
Accountability remains with the designated steward unless ownership is expressly transferred under Section 12.

---

## 5. Document Ownership

### 5.1 Document Ownership Rule

Every controlled document shall have exactly one owning authority.

### 5.2 Owning Authority by Document Class

| Document Class | Default Owning Authority |
|---|---|
| Architecture (ARCH) | Human Engineer / Constitutional Engineering Office |
| Policy (POL) | Human Engineer / Constitutional Engineering Office |
| Standard (STD) | Human Engineer / Constitutional Engineering Office |
| Workflow (WF) | Human Engineer / Constitutional Engineering Office |
| Template (TMP) | Human Engineer / Constitutional Engineering Office |
| Index (IDX) | Human Engineer / Constitutional Engineering Office |
| CWC-CE / ECR / CEP / CER | Human Engineer as authorizing/accepting authority; preparer is not owner |
| Manager specs, templates, prompts | Designated manager steward under ARCH-002 boundaries |
| Control documents (AGCL / NBBF / CDT) | Owning control repository steward / designated domain steward |

### 5.3 Document Ownership Rules

1. Metadata fields such as Authority, Governing Architecture, and Owning Manager identify governance and preparation context; they do not permit AI ownership.  
2. A document’s owning authority is responsible for integrity, authorized change, and disposition posture.  
3. Preparing a document under CWC-CE / CEP does not transfer ownership to the preparer.  
4. Manager-local documents are owned within manager scope; they remain subordinate to Office architecture and policy.  
5. When a document references foreign controls, ownership of the referenced controls remains with the foreign owning repository.

### 5.4 Document Identity and Ownership Trace

Document ID, version, status, and owning authority shall remain reconcilable through indexes, registry entries, or governing work artifacts.

---

## 6. Manager Ownership

### 6.1 Manager Ownership Rule

Every registered manager under ARCH-002 shall have one designated steward.

### 6.2 What Manager Ownership Covers

Manager ownership covers:

1. Manager identity and domain-boundary integrity  
2. Manager-local specifications, templates, and prompts  
3. Manager registration and certification posture as recorded under ARCH-002  
4. Escalation of conflicts and out-of-scope requests  

### 6.3 What Manager Ownership Does Not Cover

Manager ownership does not include:

1. Ownership of Engineering Office ARCH / POL / STD / WF baselines  
2. Ownership of AGCL, NBBF, or CDT control content  
3. Ownership of another manager’s repository or registered surface  
4. Authority to self-activate, self-certify, or self-approve Human Engineer gates  

### 6.4 Manager Ownership and Interfaces

Cross-manager interfaces are reference-based and contract-based.  
Interface participation does not transfer ownership.  
Cross-manager modification requires explicit authorization in the governing CWC-CE and remains subject to each steward’s accountability.

---

## 7. Steward Responsibilities

Every steward shall:

1. Keep ownership identity clear and current in the Ownership Registry or approved equivalent record  
2. Preserve repository or document purpose against unauthorized structural drift  
3. Ensure change activity respects approval gates under POL-001 and WF-001  
4. Maintain traceability from material changes to authorizing artifacts  
5. Ensure publication occurs only through approved process  
6. Report conflicts, gaps, lost succession coverage, and ownership ambiguity to the Human Engineer  
7. Accept that delegated helpers do not become owners by contribution alone  
8. Support ownership audits under Section 14  

### 7.1 Steward Limits

Stewards shall not:

1. Transfer ownership informally  
2. Permit AI to be recorded as owner or steward  
3. Expand domain ownership by implication  
4. Suppress ownership defects to preserve schedule  

---

## 8. Human Engineer Authority

The Human Engineer holds supreme ownership authority under this architecture.

The Human Engineer may:

1. Assign, confirm, delegate, transfer, and succeed stewardship  
2. Designate lead stewards for shared ownership surfaces  
3. Approve ownership registry entries and ownership audit closures  
4. Resolve ownership conflicts among repositories, documents, and managers  
5. Authorize exceptions to ownership procedure when expressly recorded  
6. Remain final accountable authority unless ownership is expressly reassigned by the Human Engineer  

Delegation of drafting, analysis, or implementation support is not delegation of ownership governance.

---

## 9. AI Agent Authority

### 9.1 AI May

1. Prepare ownership-related drafts, registry entries, transfer packages, and audit checklists  
2. Recommend stewardship assignments and identify ownership gaps  
3. Implement authorized CEP scope that creates or modifies artifacts  
4. Record files created, modified, renamed, or deleted accurately  
5. Report uncertainty about ownership truthfully  

### 9.2 AI Shall Not

1. Own any repository, document, manager, or engineering artifact  
2. Assume stewardship by preparing or implementing work  
3. Approve ownership transfers, succession, or audit closure  
4. Record itself as Owning Authority, Steward, or Lead Steward  
5. Invent ownership where registry or authorizing artifacts are silent  
6. Bypass Human Engineer ownership gates  

### 9.3 AI Non-Ownership Principle

AI authorship assistance never ripens into ownership.  
An AI-prepared artifact remains owned by the designated human owning authority upon Human Engineer acceptance under applicable workflow.

---

## 10. Shared Ownership Rules

### 10.1 Shared Contribution vs Shared Ownership

Multiple humans and AI agents may contribute to a surface.  
Shared contribution does not create equal ownership.

### 10.2 Lead Steward Requirement

Where more than one human participates in stewardship duties for the same repository, document class set, or manager surface:

1. Exactly one Lead Steward shall be designated  
2. The Lead Steward remains accountable  
3. Supporting stewards may be recorded as delegates or contributors  
4. Absence of a Lead Steward is an ownership defect  

### 10.3 Shared Ownership Prohibitions

1. “Everyone owns it” is not a valid ownership state.  
2. Dual equal ownership without a Lead Steward is prohibited.  
3. AI may not be a Lead Steward or co-owner.  

---

## 11. Cross-Repository Ownership

### 11.1 Peer Ownership Rule

AGCL, NBBF, and CDT are ownership peers under Engineering Office process authority.  
None owns another’s control content.

### 11.2 Cross-Repository Rules

1. Reference across repositories is permitted and expected.  
2. Reference does not transfer ownership.  
3. Cross-repository modification requires explicit scope in the governing CWC-CE and steward awareness for each affected repository.  
4. Derived artifacts do not acquire ownership of source controls.  
5. Publication packages do not relocate ownership from source repositories to public surfaces.  
6. Engineering Office architectural authority does not convert into domain-control ownership of AGCL, NBBF, or CDT content.

### 11.3 Conflict Handling

If ownership of a concept appears claimed by more than one repository, participants shall stop, report the conflict, and seek Human Engineer resolution.  
No AI agent may silently choose an ownership winner.

---

## 12. Ownership Transfer

### 12.1 Transfer Rule

Ownership transfers require explicit Human Engineer authorization.

### 12.2 Required Transfer Elements

An ownership transfer package shall record at least:

| Element | Description |
|---|---|
| Subject | Repository, document, manager, or ownership surface |
| Current Owner / Steward | Accountable party before transfer |
| Proposed Owner / Steward | Accountable party after transfer |
| Effective Date | Transfer effective date |
| Authorizing Artifact | CWC-CE / ECR / equivalent Human Engineer authorization |
| Reason | Why transfer is required |
| Registry Update | Ownership Registry update action |
| Acceptance | Human Engineer approval record |

### 12.3 Transfer Prohibitions

1. Silence is not transfer.  
2. Repository inactivity is not transfer.  
3. AI recommendation is not transfer.  
4. Informal chat acknowledgment is not transfer unless expressly captured as Human Engineer authorization in an approved artifact.  
5. Partial transfer of accountability without Lead Steward designation is prohibited for shared surfaces.

### 12.4 Effect of Transfer

Upon approved transfer:

1. Prior steward accountability ends as of the effective date for prospective acts  
2. New steward accountability begins as of the effective date  
3. Historical authorship and prior stewardship remain auditable  

---

## 13. Ownership Succession

### 13.1 Succession Purpose

Succession preserves continuity when a steward becomes unavailable, is reassigned, or a surface is suspended or retired.

### 13.2 Succession Order (Default)

Unless a more specific succession designation is recorded:

1. Designated successor steward (if registered)  
2. Human Engineer  
3. Temporary Lead Steward expressly appointed by the Human Engineer  

### 13.3 Succession Rules

1. Succession shall be explicit and recorded.  
2. Temporary succession remains accountable stewardship, not informal caretaker status without ownership duties.  
3. AI may prepare succession packages; AI may not appoint successors.  
4. Manager retirement or suspension under ARCH-002 does not erase historical ownership records.  
5. Succession gaps are ownership defects and shall be corrected before dependent production work continues on the affected surface.

---

## 14. Ownership Audit Requirements

### 14.1 Audit Purpose

Ownership audits verify that stewardship, document owning authority, manager stewards, transfers, and succession remain complete, current, and non-AI.

### 14.2 Minimum Audit Checks

An ownership audit shall confirm:

1. Every in-scope repository has one accountable steward  
2. Sampled controlled documents have one owning authority  
3. Every active/registered manager has a designated steward  
4. Shared surfaces have one Lead Steward  
5. No AI agent is recorded as owner or steward  
6. Transfers since last audit have authorizing artifacts  
7. Succession coverage exists or gaps are recorded  
8. Cross-repository ownership claims do not improperly fork foreign controls  
9. Ownership Registry entries match observed reality or discrepancies are listed  

### 14.3 Audit Outcomes

| Outcome | Meaning |
|---|---|
| Pass | No material ownership defects |
| Partial | Defects found; production may continue only where unaffected and Human Engineer permits |
| Fail | Material ownership defects block affected production work until corrected |

AI may prepare audit evidence packages.  
Human Engineer closes ownership audits.

---

## 15. Ownership Registry

### 15.1 Registry Purpose

The Ownership Registry is the authoritative record of stewardship and owning-authority assignments for surfaces under this architecture.

### 15.2 Required Registry Fields

| Field | Description |
|---|---|
| Subject ID / Path | Repository, document ID, manager code, or surface path |
| Subject Type | Repository / Document / Manager / Publication Surface / Other |
| Owner or Steward | Accountable human role or designated human steward |
| Lead Steward | Required when shared contribution exists |
| Delegates | Optional day-to-day care assignees |
| Status | Active / Temporary / Suspended / Transferred / Retired |
| Effective Date | Date current ownership became effective |
| Authorizing Artifact | CWC-CE / ECR / Human Engineer record authorizing current state |
| Succession Designation | Named successor or default-to-Human-Engineer |
| Notes | Non-authoritative clarifications |

### 15.3 Registry Rules

1. The Engineering Office shall maintain an Ownership Registry entry surface under Office control (dedicated registry document, index appendix, or approved equivalent).  
2. Until a dedicated registry document exists, approved registry artifacts or authorized index appendices may carry ownership records under CWC-CE authorization.  
3. Registry updates for transfer or succession require Human Engineer authorization.  
4. AI may draft registry updates; AI may not finalize them as authority.  
5. Absence of a registry entry for an in-scope production surface is an ownership defect.

### 15.4 Relationship to Other Registries

Manager Registration under ARCH-002 remains authoritative for manager identity and domain.  
Ownership Registry records stewardship of those managers and does not redefine manager architecture.

---

## 16. Future UNBKE Ownership Mapping

1. UNBKE is a future runtime and knowledge integration layer.  
2. Current ownership operations shall not depend on UNBKE.  
3. Ownership identifiers (repository paths, document IDs, manager codes, steward roles, transfer records) should remain suitable for future UNBKE indexing.  
4. When UNBKE ownership mapping is authorized, it shall be additive:
   - map existing Ownership Registry fields
   - preserve human accountability
   - never assign AI as owner in mapped records
5. UNBKE availability shall not by itself transfer ownership.  
6. Existing ownership records shall not require rewrite solely because UNBKE becomes available; mapping updates shall be additive under approved work.

---

## 17. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Engineering Ownership Architecture defining repository, document, and manager ownership; steward, human, and AI authority; shared ownership, transfer, succession, audit, registry, and future UNBKE mapping. |
