# TMP-001 — Engineering Office Master Document Template

**Document ID:** TMP-001  
**Title:** Engineering Office Master Document Template  
**Classification:** Engineering Office Template  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Index:** IDX-001 — Engineering Office Master Index  
**Status:** Active  
**Version:** 1.0.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This document establishes the official master template from which every controlled Engineering Office document shall be derived.

TMP-001 is the canonical template for Engineering Office artifacts.  
All future Engineering Office governing documents shall be derived from TMP-001 unless an approved standard authorizes an exception.

TMP-001 does not modify existing documents. Existing documents remain valid; future revisions should converge toward this template where practical.

---

## 2. Scope

### 2.1 Supported Document Types

This master template applies to:

| Type | Series | Name |
|---|---|---|
| Architecture Documents | ARCH | Architecture baselines and architectural definitions |
| Policies | POL | Engineering Office governance and conduct policies |
| Standards | STD | Binding engineering standards |
| Workflows | WF | Operational engineering workflows |
| Engineering Work Cards | CWC-CE | Work authorization / specification |
| Engineering Change Requests | ECR | Controlled change authorization and record |
| Constitutional Engineering Reports | CER | Implementation and completion records |
| Engineering Indexes | IDX | Authoritative catalogs and indexes |
| Future Guides | GUIDE | Non-superseding implementation guidance |
| Future Specifications | SPEC | Detailed technical or domain specifications |

### 2.2 Out of Scope

This template does not:

1. Rewrite existing ARCH/POL/STD/WF/IDX documents  
2. Authorize exceptions by itself  
3. Replace document-type authority defined in ARCH-001, STD-014, STD-015, or WF-001  
4. Require UNBKE  

---

## 3. Authority

1. TMP-001 is subordinate to ARCH-001 and applicable Standards and Policies.  
2. Document-type standards (for example STD-014 for ECR, STD-015 for CER) govern type-specific required content.  
3. Where TMP-001 and a type-specific standard both apply, the type-specific required sections remain mandatory and shall be mapped into the TMP-001 structure.  
4. Exceptions to TMP-001 require approved Engineering Office authorization.

---

## 4. Required Metadata Fields

Every controlled Engineering Office document shall begin with a title heading and a metadata block containing at least:

| Field | Required | Description |
|---|---|---|
| Document ID | Yes | Official identifier (`ARCH-001`, `STD-015`, `CWC-CE-012`, etc.) |
| Title | Yes | Official document title |
| Classification | Yes | Document class (Architecture Baseline, Engineering Standard, etc.) |
| Authority | Yes | Constitutional Engineering Office, unless a narrower approved authority is expressly stated |
| Governing Architecture | Yes for ARCH/POL/STD/WF/IDX/TMP/GUIDE/SPEC; recommended otherwise | Usually `ARCH-001` |
| Governing Policy | Conditional | Include when policy-constrained |
| Governing Standard(s) | Conditional | Include when standard-constrained |
| Governing Workflow | Conditional | Include when workflow-constrained |
| Governing CWC-CE | Conditional | Required for CEP/CER; common for ECR |
| Governing ECR | Conditional | Required for CER when applicable |
| Governing CEP | Conditional | Required for CER |
| Status | Yes | `Draft` / `Active` / `Approved` / `Complete` / `Reserved` / `Deprecated` / `Withdrawn` / type-allowed equivalent |
| Version | Yes | Semantic version `MAJOR.MINOR.PATCH` |
| Effective Date | Yes | `YYYY-MM-DD` |
| Owning Manager / Agent | Conditional | Include for manager-owned or agent-prepared artifacts |

### 4.1 Metadata Block Format

```markdown
# {ID} — {Title}

**Document ID:** {ID}  
**Title:** {Title}  
**Classification:** {Classification}  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Status:** {Status}  
**Version:** {X.Y.Z}  
**Effective Date:** {YYYY-MM-DD}  
```

Additional metadata fields may follow the same bold-label pattern before the first horizontal rule.

---

## 5. Heading Conventions

1. Document title uses a single H1: `# {ID} — {Title}`  
2. Only one H1 is permitted per document.  
3. Primary sections use H2: `## N. Section Name`  
4. Subsections use H3: `### N.M Subsection Name`  
5. Deeper subsections use H4 sparingly: `#### N.M.P Name`  
6. Section numbering is decimal and sequential within the document.  
7. Do not skip heading levels.  
8. Appendix sections may use `## Appendix A — Name` after the main numbered sections.

---

## 6. Numbering Conventions

| Series | Pattern | Example |
|---|---|---|
| ARCH | `ARCH-NNN` | ARCH-001 |
| POL | `POL-NNN` | POL-001 |
| STD | `STD-NNN` | STD-015 |
| WF | `WF-NNN` | WF-001 |
| CWC-CE | `CWC-CE-NNN` | CWC-CE-015 |
| ECR | `ECR-NNN` | ECR-001 |
| CER | `CER-NNN` | CER-001 |
| CEP | `CEP-NNN` | CEP-001 |
| IDX | `IDX-NNN` | IDX-001 |
| TMP | `TMP-NNN` | TMP-001 |
| GUIDE | `GUIDE-NNN` | GUIDE-001 |
| SPEC | `SPEC-NNN` | SPEC-001 |
| ADR | `ADR-NNN` | ADR-001 |
| NOTE | `NOTE-NNN` | NOTE-001 |

Rules:

1. `NNN` is a zero-padded sequential integer.  
2. Numbers are never reused within a series.  
3. Filename convention: `{ID}-{Short-Title}.md`  
4. Short titles use hyphens, not spaces.  
5. Document versioning uses semantic versioning independent of the series number.

---

## 7. Markdown Conventions

1. Use GitHub-flavored Markdown.  
2. Insert a horizontal rule `---` after metadata and between major logical blocks when useful.  
3. Use bullet lists for unordered requirements; numbered lists for sequences and ranked rules.  
4. Use bold sparingly for field labels and critical terms.  
5. Use inline code for identifiers, paths, statuses, and literal values.  
6. Do not use HTML tables when Markdown tables suffice.  
7. Keep lines readable; prefer short paragraphs.  
8. Do not embed conversational prompt language in governing documents.  
9. Write in engineering language: normative, precise, non-theatrical.

### 7.1 Normative Language

| Term | Meaning |
|---|---|
| shall | Mandatory |
| shall not | Prohibited |
| may | Optional permission |
| should | Recommended but not mandatory |
| required | Mandatory condition |

---

## 8. Diagram Conventions

1. Prefer fenced code blocks with monospace flow diagrams for hierarchies and sequences.  
2. Use top-to-bottom flow with `↓` for primary sequences.  
3. Use boxes (`┌ ┐ │ └ ┘`) for system/context diagrams when helpful.  
4. Diagram titles belong in the preceding heading or an introductory sentence.  
5. Diagrams illustrate; they do not replace normative text.  
6. Keep diagrams technology independent unless the document is expressly tool-specific.

Example:

```text
Need Identified
      ↓
CWC-CE Created
      ↓
Human Review
```

---

## 9. Table Conventions

1. Tables shall include a header row.  
2. Alignment should remain simple left-aligned unless numeric comparison benefits from other alignment.  
3. Use tables for catalogs, matrices, metadata maps, and approval gates.  
4. Every row should be complete; use `None`, `N/A`, or `TBD` explicitly rather than blanks when absence is meaningful.  
5. Do not use tables for long narrative prose.

---

## 10. Cross-Reference Conventions

1. Reference documents by identifier and title on first substantive mention: `ARCH-001 — Constitutional Engineering Architecture`.  
2. Later mentions may use identifier alone: `ARCH-001`.  
3. Reference sections as `Section N` or `Section N.M`.  
4. Reference repository paths in inline code.  
5. Do not invent identifiers.  
6. If a referenced document is missing or conflicting, report the gap; do not fabricate content.  
7. Operational artifacts shall cite governing parents:
   - CEP → CWC-CE (+ ECR when applicable)
   - CER → CWC-CE + CEP (+ ECR when applicable)
   - ECR → CWC-CE when initiated by one

---

## 11. Version History Format

Every controlled document shall end with a Version History section containing:

```markdown
## {N}. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | YYYY-MM-DD | Initial release summary. |
```

Rules:

1. Newest or initial entry may be listed first or chronologically ascending; ascending is preferred for new documents.  
2. Summaries state the reason for change, not a file dump.  
3. MAJOR changes that break compatibility shall be identified as such in the summary when applicable.

---

## 12. Master Section Model

### 12.1 Required Sections

Unless a type-specific standard expressly replaces the label while preserving equivalent content, every governing document shall include:

1. Document Metadata  
2. Purpose  
3. Scope  
4. Authority  
5. Requirements *(or type-equivalent normative body)*  
6. Responsibilities *(or type-equivalent role/duty section)*  
7. Conformance  
8. References  
9. Version History  

### 12.2 Optional Sections

Optional sections may be included when useful:

1. Definitions  
2. Background  
3. Principles  
4. Assumptions  
5. Constraints  
6. Diagrams / Models  
7. Examples  
8. Appendices  
9. Approval Record  
10. Verification Record  

### 12.3 Document-Type-Specific Sections

Type-specific standards and the matrices in Section 14 define additional mandatory sections for CWC-CE, ECR, CER, and other specialized types.

---

## 13. Canonical Skeleton Template

Use the following skeleton for new governing documents, then adapt type-specific sections as required:

```markdown
# {ID} — {Title}

**Document ID:** {ID}  
**Title:** {Title}  
**Classification:** {Classification}  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Status:** Draft  
**Version:** 0.1.0  
**Effective Date:** YYYY-MM-DD  

---

## 1. Purpose

{Why this document exists.}

---

## 2. Scope

### 2.1 In Scope

{What this document covers.}

### 2.2 Out of Scope

{What this document does not cover.}

---

## 3. Authority

{Authority position relative to ARCH/POL/STD/WF and other artifacts.}

---

## 4. Definitions

{Optional. Define terms not already standardized elsewhere.}

---

## 5. Requirements

{Normative requirements. Rename only when type-specific standard requires an equivalent body structure.}

---

## 6. Responsibilities

{Who does what under this document.}

---

## 7. Conformance

{How conformance is determined and what nonconformance means.}

---

## 8. References

| Identifier | Title | Relationship |
|---|---|---|
| ARCH-001 | Constitutional Engineering Architecture | Governing architecture |

---

## 9. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | YYYY-MM-DD | Initial draft. |
```

---

## 14. Document-Type Application Matrix

### 14.1 ARCH — Architecture Documents

| Section Class | Sections |
|---|---|
| Required | Metadata, Purpose, Scope, Authority, Requirements/System Architecture body, Responsibilities, Conformance, References, Version History |
| Recommended | Principles, Repository hierarchy, Relationship diagrams, Baseline statements |
| Type-Specific | System architecture, repository relationships, authority hierarchy, future runtime posture |

### 14.2 POL — Policies

| Section Class | Sections |
|---|---|
| Required | Metadata, Purpose, Scope, Authority, Requirements/Policy body, Responsibilities, Conformance/Compliance, References, Version History |
| Recommended | Principles, Ethics, Exceptions |
| Type-Specific | Human/AI responsibilities, separation of duties, stewardship, approval authority |

### 14.3 STD — Standards

| Section Class | Sections |
|---|---|
| Required | Metadata, Purpose, Scope, Authority, Requirements, Responsibilities, Conformance, References, Version History |
| Recommended | Definitions, Principles |
| Type-Specific | As required by the standard’s subject (lifecycle states, change categories, report sections, etc.) |

### 14.4 WF — Workflows

| Section Class | Sections |
|---|---|
| Required | Metadata, Purpose, Scope, Authority, Requirements/Sequence body, Responsibilities, Conformance, References, Version History |
| Recommended | Principles, Inputs, Outputs, Decision points |
| Type-Specific | Operating sequence, approval gates, AI execution gates, verification gates, Git/publication/exception paths |

### 14.5 CWC-CE — Engineering Work Cards

| Section Class | Sections |
|---|---|
| Required | Metadata, Purpose/Objective, Scope, Authority, Requirements/Deliverables, Responsibilities/Assigned Agent, Acceptance Criteria, Constraints, References, Version History |
| Optional | Definitions, Engineering Notes |
| Type-Specific | Objective, Deliverables, Acceptance Criteria, Constraints, Assigned Agent |

Minimum CWC-CE body:

1. Objective  
2. Scope  
3. Deliverables  
4. Acceptance Criteria  
5. Constraints  
6. Engineering Notes (optional)  

### 14.6 ECR — Engineering Change Requests

| Section Class | Sections |
|---|---|
| Required per STD-014 mapped into TMP-001 | Metadata, Purpose, Reason for Change, Description of Change, Change Category, Impact Analysis, Documents and Repositories Affected, Proposed Resolution / Implementation Plan, Approval Record, Verification Record, Version History |
| Optional | Definitions, Background |
| Type-Specific | Change Category, Impact Analysis, Approval Record, Verification Record |

### 14.7 CER — Constitutional Engineering Reports

| Section Class | Sections |
|---|---|
| Required per STD-015 mapped into TMP-001 | Metadata, Purpose, Authorized Work, Implementation Summary, Files Created, Files Modified, Files Renamed, Files Deleted, Repositories Affected, Deviations from Approved Scope, Verification Performed, Verification Evidence, Outstanding Issues, Git Commit References, Git Push / Publication Status, Human Acceptance, Version History |
| Optional | Definitions, Recommendations |
| Type-Specific | File action lists, verification evidence, Git references, Human Acceptance |

### 14.8 IDX — Engineering Indexes

| Section Class | Sections |
|---|---|
| Required | Metadata, Purpose, Scope, Authority, Catalog body, Conformance or Baseline statement, References, Version History |
| Recommended | Hierarchy diagrams, dependency diagrams |
| Type-Specific | Document catalogs, repository catalogs, numbering conventions, baseline listing |

### 14.9 GUIDE — Future Guides

| Section Class | Sections |
|---|---|
| Required | Metadata, Purpose, Scope, Authority, Guidance body, Responsibilities, Conformance (advisory limits), References, Version History |
| Recommended | Examples, diagrams |
| Type-Specific | Explicit statement that GUIDE content is subordinate to ARCH/POL/STD/WF |

### 14.10 SPEC — Future Specifications

| Section Class | Sections |
|---|---|
| Required | Metadata, Purpose, Scope, Authority, Requirements/Specification body, Responsibilities, Conformance, References, Version History |
| Recommended | Definitions, interface models, diagrams |
| Type-Specific | Normative specification detail without inventing higher-level policy |

---

## 15. Section Ordering Standard

Default section order for governing documents:

1. Metadata  
2. Purpose  
3. Scope  
4. Authority  
5. Definitions (optional)  
6. Requirements / type-equivalent normative body  
7. Responsibilities  
8. Type-specific required sections  
9. Conformance  
10. References  
11. Version History  
12. Appendices (optional)  

For ECR and CER, preserve the type-specific required section set and order defined by STD-014 and STD-015. Those type orders are authoritative for those document types.

---

## 16. Requirements

1. All future Engineering Office governing documents shall be derived from TMP-001 unless an approved exception exists.  
2. Required metadata fields shall be present and accurate.  
3. Heading, numbering, Markdown, diagram, table, cross-reference, and version-history conventions in this template shall be followed.  
4. Document-type-specific mandatory sections remain mandatory.  
5. TMP-001 shall not be used to justify modification of existing documents without separate approved work authorization.  
6. Templates subordinate to TMP-001 may specialize structure but shall not contradict TMP-001.

---

## 17. Responsibilities

| Role | Responsibility |
|---|---|
| Human Engineer | Approves adoption of TMP-001-derived documents and exceptions |
| Constitutional Engineer | Applies TMP-001 when drafting governing documents |
| Specialized Managers | Derive manager-facing controlled documents from TMP-001 where applicable |
| Cursor AI | Uses TMP-001 structure when directed by approved CEP to create new governing documents |

---

## 18. Conformance

A new Engineering Office governing document conforms to TMP-001 when it:

1. Uses the correct series identifier and filename convention  
2. Includes required metadata  
3. Follows heading and section-ordering rules applicable to its type  
4. Includes required and type-specific mandatory sections  
5. Uses prescribed Markdown, table, diagram, and cross-reference conventions  
6. Includes Version History in the standard format  

Nonconformance is an engineering defect and shall be corrected before the document is treated as baseline-quality.

---

## 19. References

| Identifier | Title | Relationship |
|---|---|---|
| ARCH-001 | Constitutional Engineering Architecture | Governing architecture |
| POL-001 | Engineering Office Governance Policy | Governing policy |
| STD-014 | Engineering Change Management | ECR type authority |
| STD-015 | Constitutional Engineering Reports | CER type authority |
| WF-001 | Engineering Office Operating Workflow | Operating sequence authority |
| IDX-001 | Engineering Office Master Index | Catalog authority |

---

## 20. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Engineering Office Master Document Template establishing the canonical template for Engineering Office artifacts. |
