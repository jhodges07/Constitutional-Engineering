# STD-014 — Engineering Change Management

**Document ID:** STD-014  
**Title:** Engineering Change Management  
**Classification:** Engineering Standard  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Status:** Active  
**Version:** 1.0.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This standard establishes the official Engineering Change Management process for the Constitutional Engineering Office.

It defines how engineering changes are proposed, categorized, analyzed, approved, implemented, verified, and recorded so that architecture, standards, repositories, and baselines remain controlled and traceable.

This standard formally establishes the **Engineering Change Request (ECR)** as an Engineering Office document type.

---

## 2. Scope

### 2.1 In Scope

This standard applies to engineering changes affecting:

1. Engineering Office architecture documents
2. Engineering Office standards
3. Engineering Office workflows, templates, prompts, agents, and audits
4. Official numbering, identifiers, indexes, and navigation of Engineering Office artifacts
5. Repository structure under Engineering Office authority when the change is architectural or standards-driven
6. Baselines declared by the Engineering Office

### 2.2 Out of Scope

This standard does not:

1. Replace domain control authority held by AGCL, NBBF, or CDT control documents
2. Authorize policy invention inside control repositories
3. Govern ordinary legislative artifact lifecycle states defined by STD-008
4. Depend on UNBKE runtime availability

### 2.3 Authority Position

This standard is subordinate to ARCH-001.  
ECRs are subordinate to approved architecture and applicable standards.  
An ECR may propose changes to architecture or standards; it does not itself override them until approved and incorporated.

---

## 3. Engineering Change Categories

Every ECR shall declare exactly one primary category:

| Category | Code | Description |
|---|---|---|
| Architecture Change | ARCH | Changes to architectural baselines, repository relationships, or authority structure |
| Standards Change | STD | Creation, revision, renumbering, or retirement of Engineering Standards |
| Workflow Change | WF | Changes to approved engineering workflows |
| Template Change | TPL | Changes to Engineering Office or manager templates that alter controlled structure |
| Repository Structure Change | REP | Controlled changes to repository layout under Engineering Office authority |
| Baseline Change | BL | Declaration, amendment, or retirement of an engineering baseline |
| Corrective Change | COR | Correction of defects, conflicts, or nonconformance without expanding intent |
| Administrative Change | ADM | Identifier, indexing, navigation, or metadata changes that do not alter engineering intent |
| Emergency Change | EMG | Time-critical change under Section 11 |

A single ECR may list secondary impacted categories, but one primary category remains mandatory.

---

## 4. Engineering Change Request (ECR) Requirements

### 4.1 Document Type

**ECR** means **Engineering Change Request**.

An ECR is the official Engineering Office artifact used to:

1. Request an engineering change
2. Record impact analysis and approvals
3. Authorize implementation
4. Record verification and closure

Upon completion, the ECR remains the durable change record.

### 4.2 ECR Numbering

1. ECR identifiers shall use the form `ECR-NNN`, where `NNN` is a zero-padded sequential integer (`ECR-001`, `ECR-002`, …).
2. Numbering is sequential within the Engineering Office ECR series.
3. Numbers are never reused.
4. Withdrawn or rejected ECRs retain their numbers and final status.
5. Filename convention: `ECR-NNN-Short-Title.md`
6. ECRs shall be stored under `Engineering-Office/audits/` unless a later approved standard designates another controlled location.

### 4.3 Required ECR Metadata

Every ECR shall include:

| Field | Requirement |
|---|---|
| Document ID | `ECR-NNN` |
| Title | Short descriptive title |
| Classification | Engineering Change Request |
| Authority | Constitutional Engineering Office |
| Governing Work Card | CWC-CE reference when initiated by a work card; otherwise `None` |
| Status | Proposed / Under Review / Approved / Rejected / Implemented / Verified / Closed / Withdrawn |
| Version | Semantic version of the ECR document |
| Effective Date | Date of issue or approval effectiveness |
| Primary Category | Category code from Section 3 |
| Requestor | Human Engineer or authorized initiating role |
| Agent | Preparing agent, if any |

### 4.4 Required ECR Sections

Every ECR shall contain, at minimum:

1. Purpose  
2. Reason for Change  
3. Description of Change  
4. Change Category  
5. Impact Analysis  
6. Documents and Repositories Affected  
7. Proposed Resolution / Implementation Plan  
8. Approval Record  
9. Verification Record  
10. Version History  

Additional sections are permitted when needed for clarity.

### 4.5 Relationship to CWC-CE

1. A Constitutional Engineering Work Card (`CWC-CE-NNN`, also referenced historically as CEWC) may direct preparation of an ECR.
2. When an ECR is governed by a CWC-CE, the ECR shall cite that work card in metadata.
3. Routine CWC-CE implementation that does not alter baselines, standards numbering, architecture, or controlled structure does not require an ECR.
4. An ECR is required when a change alters architecture, standards, official identifiers, baselines, or other controlled Engineering Office configuration defined in this standard.
5. A CEP implementing an approved ECR shall reference both the ECR and its governing CWC-CE when both exist.

### 4.6 Relationship to Standards

1. Standards govern engineering practice; ECRs propose controlled changes within or to that practice.
2. Creation, renumbering, revision, or retirement of a Standard requires an ECR, except where a CWC-CE expressly authorizes initial creation of a new Standard and no existing Standard identifiers or baselines are disturbed.
3. After approval, Standards shall be updated only as authorized by the ECR.
4. No Standard may be silently renumbered, retitled by identifier, or replaced without ECR coverage when other artifacts depend on its identifier.

### 4.7 Relationship to Architecture

1. ARCH-001 and successor architecture documents are the highest Engineering Office authority below Human Engineer approval.
2. Architecture changes require an ECR with primary category ARCH.
3. An ECR cannot declare itself superior to architecture.
4. Approved architecture changes become effective only when the architecture document is updated and the ECR reaches Verified or Closed status.

---

## 5. Approval Authority

### 5.1 Approval Matrix

| Change Category | Minimum Approval Authority |
|---|---|
| ADM | Human Engineer |
| COR | Human Engineer |
| TPL | Human Engineer |
| WF | Human Engineer |
| STD | Human Engineer |
| REP | Human Engineer |
| BL | Human Engineer |
| ARCH | Human Engineer |
| EMG | Human Engineer (may be recorded after immediate containment per Section 11) |

### 5.2 Approval Workflow

```
ECR Proposed
      ↓
Impact Analysis Complete
      ↓
Under Review
      ↓
Human Engineer Decision
      ├── Rejected / Withdrawn
      └── Approved
            ↓
      Implementation
            ↓
      Verification
            ↓
      Closed
```

### 5.3 Approval Rules

1. AI assistants and specialized managers may prepare ECRs; they may not approve them.
2. Approval shall be recorded in the ECR Approval Record with approver, role, decision, date, and conditions.
3. Conditional approval is permitted; conditions must be satisfied before Closed status.
4. Rejected ECRs shall record the rejection reason and remain retained.

---

## 6. Impact Analysis

Every ECR shall analyze impact across at least the following dimensions:

1. **Architecture** — effects on ARCH documents, authority hierarchy, or system relationships  
2. **Standards** — affected STD identifiers, titles, and conformance obligations  
3. **Workflows / Templates / Prompts** — dependent Engineering Office artifacts  
4. **Repositories** — Engineering Office, control repositories, managers, and public repositories  
5. **Identifiers and References** — numbering, cross-references, indexes, navigation  
6. **Baselines** — whether a declared baseline changes  
7. **Traceability** — whether CEPs, CWCs, or derived artifacts require update  
8. **Operational Continuity** — whether current operations remain possible without UNBKE or other future components  

Impact Analysis shall state:

- What changes
- What does not change
- Compatibility or breaking-change character
- Required follow-on updates

---

## 7. Change Verification

### 7.1 Verification Requirements

Before an ECR may close, verification shall confirm:

1. Approved scope was implemented without unauthorized expansion  
2. Affected identifiers are unique and consistent  
3. Cross-references, indexes, and navigation are updated or confirmed unaffected  
4. No unintended document intent changes occurred  
5. Repository updates match the ECR authorization  
6. Version histories of changed controlled documents record the change  
7. Acceptance criteria from the governing CWC-CE, if any, are satisfied  

### 7.2 Verification Record

The ECR shall record:

- Verifier identity
- Date
- Verification result (Pass / Fail / Pass with Follow-up)
- Evidence summary
- Outstanding follow-up items, if any

Fail results return the ECR to Implementation or Under Review as appropriate.

---

## 8. Repository Update Requirements

### 8.1 Update Procedure

When an approved ECR requires repository updates, the following procedure applies:

1. Confirm ECR status is Approved.  
2. Limit modifications to the documents, paths, and repositories listed in the ECR.  
3. Apply identifier and reference updates before declaring completion.  
4. Preserve document intent except where the ECR expressly authorizes intent change.  
5. Record implementation results in the ECR or linked CER.  
6. Perform verification per Section 7.  
7. Commit and push only under applicable Git standards and Human Engineer approval.  

### 8.2 Multi-Repository Rules

1. Each affected repository shall be identified explicitly.  
2. Cross-repository changes shall preserve logical separation among AGCL, NBBF, CDT, and UNBKE.  
3. Control document content shall not be modified by an Engineering Office ECR unless the ECR expressly authorizes a controlled engineering correction and Human Engineer approval is recorded.  
4. Public repositories receive only approved published outputs; they are not the system of record for ECR state.

### 8.3 Restriction Recital

Implementers shall not:

- Modify documents outside ECR scope
- Create or delete standards unless authorized by the ECR
- Reuse retired identifiers
- Introduce UNBKE hard dependencies

---

## 9. Version Control Rules

1. ECRs use semantic versioning for the ECR document itself.  
2. Controlled documents modified under an ECR shall increment versions according to their governing versioning policy.  
3. Breaking changes to architecture or standards require MAJOR version increments on the affected controlled documents.  
4. Administrative renumbering without intent change is at least a MINOR or PATCH change as determined by the affected document’s versioning policy; the ECR shall state which.  
5. Git history shall reflect approved engineering work associated with the ECR.  
6. The ECR identifier shall be cited in commit messages when the change is ECR-governed, unless Git standards prescribe an equivalent traceable reference form.

---

## 10. Change History

1. Every ECR shall maintain a Version History section.  
2. The Engineering Office shall retain closed, rejected, and withdrawn ECRs as historical records.  
3. Change history shall be sufficient to reconstruct:
   - prior state
   - new state
   - authority for change
   - verification outcome
4. Superseded numbering maps, baseline declarations, and architecture transitions shall remain discoverable through ECR records.

---

## 11. Emergency Changes

### 11.1 Definition

An Emergency Change is a change required to stop active integrity failure, data loss risk, security exposure, or blocking repository corruption where delay would cause material harm to Engineering Office integrity.

### 11.2 Emergency Rules

1. Primary category shall be EMG, with the substantive category listed as secondary.  
2. Human Engineer authorization is still required; if verbal/immediate authorization is used, it shall be recorded in the ECR at the earliest opportunity.  
3. An ECR shall be opened no later than the completion of immediate containment.  
4. Impact Analysis and Verification may be abbreviated for containment but must be completed before Closed status.  
5. Emergency status does not authorize architecture or standards overrides beyond the minimum change needed for containment.  
6. Follow-on non-emergency ECR(s) shall be opened if enduring corrective work remains.

---

## 12. Engineering Baseline Management

### 12.1 Baseline Definition

An **Engineering Baseline** is a named, approved set of controlled Engineering Office artifacts and identifiers that defines the current authoritative configuration for subsequent work.

### 12.2 Baseline Rules

1. Architecture baselines and standards sequences are Engineering Baselines.  
2. Baseline creation, amendment, or retirement requires an ECR with primary category BL, or ARCH/STD when those categories are the substantive change and baseline impact is documented.  
3. Each baseline declaration shall identify:
   - Baseline name or ID
   - Effective date
   - Included artifact identifiers and versions
   - Governing ECR
4. Work performed after a baseline effective date shall conform to that baseline unless a later approved baseline supersedes it.  
5. ECR-001 and successor configuration-resolution ECRs are part of the change history supporting the active standards baseline.

### 12.3 Current Standards Baseline Reference

The active Engineering Standards baseline is the official sequential STD series as last established or amended by approved ECR.  
New Standards receive the next sequential STD identifier and shall not reuse identifiers.

---

## 13. Conformance

An engineering change is conformant to STD-014 when it:

1. Uses a properly numbered ECR when required  
2. Declares a valid change category  
3. Completes required sections and impact analysis  
4. Obtains Human Engineer approval before non-emergency implementation  
5. Updates repositories only within authorized scope  
6. Completes verification before closure  
7. Preserves architecture and standards authority relationships  

Nonconforming changes are engineering defects and require corrective ECR action.

---

## 14. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Engineering Change Management Standard; establishes ECR as an Engineering Office document type. |
