# STD-008 — Legislative Lifecycle Standard

**Document ID:** STD-008  
**Title:** Legislative Lifecycle Standard  
**Classification:** Engineering Standard  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Owning Manager:** Legislative Manager  
**Status:** Active  
**Version:** 1.0.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This standard defines the complete engineering lifecycle for every legislative artifact produced by the Legislative Manager repository.

It establishes:

- Required lifecycle states
- Permitted state transitions
- Required reviews and approvals
- Versioning, publication, and archive rules
- Traceability and audit requirements

This standard ensures that legislative artifacts advance through governed engineering states with identifiable authority, review evidence, and publication integrity.

---

## 2. Scope

### 2.1 In Scope

This standard applies to all legislative artifacts authored, maintained, versioned, published, superseded, or archived under the Legislative Manager repository, including:

- Bills
- Acts
- Amendments
- Resolutions
- Legislative templates when treated as controlled legislative artifacts
- Derivative legislative packages intended for public or jurisdictional use

### 2.2 Out of Scope

This standard does not:

- Define legislative drafting style or clause structure
- Define legal sufficiency criteria beyond required review gates
- Authorize changes to AGCL, NBBF, or CDT control documents
- Depend on UNBKE runtime availability

### 2.3 Authority Position

This standard is subordinate to ARCH-001 and superior to Legislative Manager templates, CEWCs, and CEPs that govern legislative artifact work.

---

## 3. Legislative Artifact States

Every legislative artifact shall exist in exactly one of the following states at any time:

| State | Definition |
|---|---|
| **Proposed** | Artifact concept or placeholder has been introduced; content is not yet under formal drafting control |
| **Draft** | Artifact is under active authoring and revision |
| **Engineering Review** | Artifact is under Engineering Office / Legislative Manager engineering review for structure, standards conformance, and traceability |
| **Legal Review** | Artifact is under legal or constitutional compatibility review against source authority and related controls |
| **Public Review** | Approved draft is released for designated public or stakeholder review without final publication authority |
| **Approved** | All required reviews and approvals are complete; artifact is authorized for publication |
| **Published** | Artifact is released through an approved public repository or designated publication channel |
| **Superseded** | A newer approved version has replaced this artifact as the current authority |
| **Archived** | Artifact is retained for historical record and is no longer active for drafting, review, or publication use |

---

## 4. State Transition Rules

### 4.1 Permitted Transitions

```
Proposed
    → Draft

Draft
    → Engineering Review
    → Archived          (withdrawal before review)

Engineering Review
    → Draft             (deficiencies returned to authoring)
    → Legal Review
    → Archived          (withdrawal after engineering review failure or abandonment)

Legal Review
    → Draft             (material legal deficiencies requiring rewrite)
    → Engineering Review (engineering defects discovered during legal review)
    → Public Review
    → Approved          (public review waived by documented Human Engineer approval)
    → Archived

Public Review
    → Draft             (material changes required)
    → Engineering Review (engineering issues raised in public review)
    → Legal Review      (legal issues raised in public review)
    → Approved
    → Archived

Approved
    → Published
    → Draft             (approval withdrawn before publication; requires recorded justification)
    → Archived          (approved but never published; requires recorded justification)

Published
    → Superseded
    → Archived          (retirement without successor; requires recorded justification)

Superseded
    → Archived

Archived
    → (terminal; no outbound transition except restoration by explicit Human Engineer approval returning to Draft)
```

### 4.2 Transition Constraints

1. No state may be skipped unless this standard expressly permits the skip.
2. The only permitted skip of Public Review is Approved entry directly from Legal Review with documented Human Engineer waiver.
3. Transition into Approved requires completion of all required reviews and approvals for that artifact.
4. Transition into Published requires Approved state and satisfaction of Publication Rules.
5. Transition into Superseded requires a successor artifact that has reached Approved or Published state.
6. Every transition shall record: prior state, new state, actor, timestamp, and authorizing reference.
7. AI assistants may prepare transition recommendations; they may not unilaterally authorize state changes.

---

## 5. Required Reviews

### 5.1 Engineering Review

Required before Legal Review.

Engineering Review shall verify:

1. Unique identifier and version metadata are present and valid
2. Conformance to applicable Engineering Office standards
3. Conformance to Legislative Manager templates and structural requirements
4. Traceability fields are complete
5. Related control documents are identified and not contradicted by invention
6. Repository placement and naming are correct

### 5.2 Legal Review

Required before Public Review or Approved (if Public Review is waived).

Legal Review shall verify:

1. Consistency with declared source authority
2. Compatibility with related control documents
3. Absence of unresolved conflicts with higher-authority controls
4. Clear jurisdiction and applicability statements
5. That legal deficiencies are resolved or expressly deferred with Human Engineer approval

### 5.3 Public Review

Required before Approved unless waived under Section 4.2.

Public Review shall:

1. Use an Approved-for-public-review package derived from Legal Review completion
2. Record review window, distribution scope, and feedback disposition
3. Return the artifact to an earlier state if material changes are required

### 5.4 Review Evidence

Each completed review shall record:

- Reviewer identity
- Review type
- Date
- Result (Pass / Fail / Pass with Conditions)
- Conditions or findings
- Linked artifact identifier and version

---

## 6. Required Approvals

### 6.1 Approval Gates

| Transition | Required Approval Authority |
|---|---|
| Proposed → Draft | Legislative Manager authoring authority or Human Engineer |
| Draft → Engineering Review | Author confirmation that draft is review-ready |
| Engineering Review → Legal Review | Engineering reviewer approval |
| Legal Review → Public Review | Legal reviewer approval |
| Legal Review → Approved (waiver path) | Legal reviewer approval and Human Engineer waiver of Public Review |
| Public Review → Approved | Human Engineer approval after feedback disposition |
| Approved → Published | Human Engineer publication approval |
| Any → Archived (non-terminal lifecycle end) | Human Engineer approval |
| Published → Superseded | Human Engineer approval identifying successor |
| Archived → Draft (restoration) | Human Engineer approval |

### 6.2 Approval Record

Every approval shall be recorded in the artifact approval history with:

- Approver identity
- Role
- Decision
- Date
- Artifact identifier and version
- Conditions, if any

### 6.3 Authority Limits

1. Cursor AI and other AI assistants cannot grant lifecycle approvals.
2. Specialized managers cannot approve publication without Human Engineer authority.
3. Approval of a lower-authority artifact cannot override ARCH-001, applicable standards, or control documents.

---

## 7. Versioning Rules

### 7.1 Version Format

Legislative artifacts shall use semantic versioning:

| Component | Meaning |
|---|---|
| MAJOR | Incompatible change to operative legal/engineering effect or structure |
| MINOR | Backward-compatible substantive addition or revision |
| PATCH | Clarification, correction, or non-substantive editorial change |

### 7.2 Version Assignment Rules

1. Every new legislative artifact begins at version `0.1.0` while in Proposed or initial Draft, unless Human Engineer directs otherwise.
2. Transition to Approved requires a release candidate version suitable for approval, typically `1.0.0` for first approval.
3. Any material change after Approved or Published requires a new version and re-entry to Draft or the appropriate review state.
4. Published artifacts shall not be silently edited in place.
5. Superseded artifacts retain their final version number permanently.
6. Version history shall record version, date, summary of change, and authorizing CEWC where applicable.

---

## 8. Repository Responsibilities

### 8.1 Legislative Manager Repository

Responsible for:

1. Authoring and maintaining legislative artifacts
2. Maintaining lifecycle state metadata
3. Preserving approval history and review evidence
4. Organizing artifacts by jurisdiction and template structure
5. Preparing publication packages
6. Retaining superseded and archived artifacts

### 8.2 Engineering Office

Responsible for:

1. Governing this standard
2. Engineering review criteria and audit expectations
3. Ensuring lifecycle conformance with ARCH-001 and related standards

### 8.3 Control Document Repositories

AGCL, NBBF, and CDT remain authoritative for their controls.  
Legislative artifacts may reference controls but shall not modify them.

### 8.4 Public Repositories

Responsible solely for hosting Approved-for-publication artifacts.  
Public repositories are not lifecycle systems of record for Draft or in-review states.

### 8.5 Separation Rule

Lifecycle state of record resides in the Legislative Manager repository unless a designated Engineering Office register is expressly authorized by a later standard.

---

## 9. Traceability Requirements

### 9.1 Mandatory Metadata

Every legislative artifact shall include:

| Field | Requirement |
|---|---|
| Unique identifier | Persistent artifact ID, unique within Legislative Manager scope |
| Version number | Semantic version per Section 7 |
| Author | Identified authoring agent or human author |
| Engineering reviewer | Identified engineering reviewer (required from Engineering Review onward) |
| Approval history | Chronological record of approvals and state transitions |
| Source authority | Constitutional, statutory, charter, or control basis authorizing the artifact |
| Related control documents | Explicit references to applicable AGCL / NBBF / CDT controls |
| Related standards | Explicit references to applicable Engineering Office standards |
| Effective date | Date the approved/published artifact becomes operative, or "TBD" while pre-approval |
| Superseded-by reference | Identifier and version of successor artifact when status is Superseded; otherwise "None" |

### 9.2 Additional Traceability Rules

1. Every lifecycle-affecting change should trace to an authorizing CEWC when performed under Constitutional Engineering workflow.
2. Every CEP used to modify a legislative artifact shall reference its CEWC.
3. Conflicts with control documents shall be reported, not resolved by invention.
4. Published artifacts shall remain traceable to their Legislative Manager source identifier and version.

---

## 10. Publication Rules

1. Only artifacts in Approved state may transition to Published.
2. Publication requires Human Engineer approval.
3. The published package shall include identifier, version, effective date, and source authority.
4. Publication channels shall be designated in the approval record.
5. Public Review materials are not Published artifacts unless separately approved for publication.
6. No direct edit of a Published artifact is permitted; corrections require a new version and lifecycle re-entry.
7. Publication shall not occur if mandatory metadata is incomplete.
8. Publication shall not occur if unresolved Fail results remain on required reviews.

---

## 11. Archive Rules

1. Archived is a retention state for historical integrity.
2. Artifacts may be archived from earlier states when withdrawn, abandoned, or retired under Human Engineer approval.
3. Superseded artifacts should be archived after successor publication unless retained as Superseded for active cross-reference needs.
4. Archived artifacts shall remain readable and traceable.
5. Archived artifacts shall not be used as the current operative text.
6. Restoration from Archived to Draft requires Human Engineer approval and a new version increment if content will change.
7. Archive actions shall record reason, date, approver, and any successor reference.

---

## 12. Audit Requirements

### 12.1 Auditable Records

The following shall be auditable for every legislative artifact:

1. Current state
2. Full state transition history
3. Mandatory metadata completeness
4. Review outcomes
5. Approval history
6. Version history
7. Publication record, if any
8. Supersession and archive records

### 12.2 Audit Checks

Audits shall verify that:

1. No unauthorized state transition occurred
2. Required reviews were completed before approval
3. Public Review waiver, if used, is documented
4. Published artifacts match approved source versions
5. Superseded artifacts identify successors
6. Traceability fields are complete and consistent with ARCH-001
7. No artifact depends on UNBKE for lifecycle validity

### 12.3 Nonconformance

Lifecycle nonconformance is an engineering defect.  
Affected artifacts shall return to the appropriate prior state until corrected and re-approved.

---

## 13. Conformance

A legislative artifact conforms to STD-008 when it:

1. Uses only defined lifecycle states
2. Follows permitted transitions
3. Completes required reviews and approvals
4. Maintains mandatory metadata
5. Obeys versioning, publication, and archive rules
6. Remains auditable end-to-end

Nonconforming artifacts are not eligible for Approved or Published status.

---

## 14. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Legislative Lifecycle Standard for Legislative Manager artifacts. |
