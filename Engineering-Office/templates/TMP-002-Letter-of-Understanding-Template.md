# TMP-002 — Letter of Understanding Template

**Document ID:** TMP-002  
**Title:** Letter of Understanding Template  
**Classification:** Engineering Office Template  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Governing Standard(s):** STD-001 — Engineering Workflow  
**Governing Workflow:** WF-001 — Engineering Office Operating Workflow  
**Governing Index:** IDX-001 — Engineering Office Master Index  
**Parent Template:** TMP-001 — Engineering Office Master Document Template  
**Governing ECR:** ECR-002 — Engineering Definition / LOU Controlled Adoption  
**Status:** Active  
**Version:** 1.0.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This template is the canonical structure for every Letter of Understanding (`LOU-NNN`) under Constitutional Engineering Office Engineering Definition.

LOU instances reside in `Engineering-Office/definition/`.

---

## 2. Authority Boundary (Mandatory)

**THIS LOU RECORDS ACCEPTED ENGINEERING UNDERSTANDING.**

**IT DOES NOT AUTHORIZE IMPLEMENTATION.**

Implementation requires a separately approved CWC-CE and all applicable downstream controls (ECR when required, CEP, CER, Human Acceptance, Git, and publication authorization as applicable).

Research recorded in this LOU is informative, not authoritative.  
AI research does not create engineering authority.  
Silence is not Human Engineer acceptance.

---

## 3. Instance Metadata Block (Required)

Every LOU instance shall begin with:

```markdown
# LOU-NNN — {Title}

**Document ID:** LOU-NNN  
**Title:** {Title}  
**Classification:** Letter of Understanding  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Governing Standard(s):** STD-001 — Engineering Workflow  
**Governing Workflow:** WF-001 — Engineering Office Operating Workflow  
**Governing Template:** TMP-002 — Letter of Understanding Template  
**Governing CWC-CE:** {CWC-CE that authorized creation/update, or HE exception reference}  
**Status:** Draft / Under Review / Accepted / Accepted with Conditions / Returned / Rejected / Superseded / Withdrawn  
**Version:** X.Y.Z  
**Effective Date:** YYYY-MM-DD  
**Storage Path:** Engineering-Office/definition/LOU-NNN-{Short-Title}.md  
```

---

## 4. Required Instance Sections

Every LOU instance shall contain the following sections (labels may be numbered sequentially in the instance):

### 4.1 Document Metadata

As required by Section 3.

### 4.2 Purpose

State why this LOU exists and what understanding it is intended to settle.

### 4.3 Human Engineering Intent

Record the Human Engineer’s stated intent for the subject.

### 4.4 Scope — In

List what is inside the understanding boundary.

### 4.5 Scope — Out

List what is expressly outside the understanding boundary.

### 4.6 Research Inputs

High-level inventory of research streams consulted (details belong in the Annex).

### 4.7 Research Record / Evidence Annex

Non-authoritative provenance table. Minimum columns:

| Source ID | Source Class | Source Locator | Collector | Collection Date | Source Summary | Conflicting Evidence | Verification Status | Authority Status |
|---|---|---|---|---|---|---|---|---|

**Source Class values** (classification does not confer engineering authority):

`PRIMARY-LEGAL` | `GOV-DATA` | `SECONDARY-ANALYSIS` | `TESTIMONY` | `HISTORICAL` | `SCRIPTURE` | `AI-SYNTHESIS` | `CONTROL-DOC`

**Default Authority Status:** `Non-authoritative`

**External AI provenance** (when ChatGPT, Grok, Cursor, or another AI system is used): record when available — system name; model descriptor; session/export identifier; date; prompt/context summary or controlled reference; role = `Research Assistant — Non-authoritative`. AI synthesis shall not be represented as primary authority.

### 4.8 Agreed Understanding

Numbered statements of agreed understanding proposed for (or recording) Human Engineer acceptance.

### 4.9 Rejected / Non-Adopted Interpretations

Interpretations considered and expressly not adopted.

### 4.10 Conflicting Sources

Conflicts among sources, marked `Unresolved` / `Accepted interpretation` / `Deferred`. AI shall not silently choose winners.

### 4.11 Open Questions

Unresolved questions remaining after current understanding.

### 4.12 Assumptions

Assumptions underlying the agreed understanding.

### 4.13 Deferred Items

Items deferred to later Definition or Execution work.

### 4.14 Verification Status

Verification posture of agreed statements (`Asserted` / `Provisionally accepted` / `Requires verification`, etc.).

### 4.15 Provisional Requirements Implications

Provisional implications for later SPEC/Requirements. Marked provisional until HG-D2 acceptance. **Not requirements by themselves.**

### 4.16 Authority Boundary

Restate the mandatory statement from Section 2 of this template.

### 4.17 Requirements / SPEC Transition

Identify the intended SPEC (`SPEC-NNN`) or approved equivalent path, or state deferred/waived with Human Engineer authority.

### 4.18 Human Engineer Acceptance Record

| Field | Value |
|---|---|
| Approver | Human Engineer |
| Decision | Accepted / Accepted with Conditions / Returned / Rejected |
| Date | YYYY-MM-DD |
| Conditions | … |
| Notes | … |

Silence is not acceptance.  
Acceptance does not authorize implementation.

### 4.19 Revision / Supersession

Prior LOU versions, successor references, and material-change re-acceptance notes.

### 4.20 Traceability

Links to authorizing CWC-CE, related SPEC, related CWC-CE for Controlled Execution (when later issued), and applicable ARCH/POL/STD/WF.

### 4.21 Version History

| Version | Date | Summary |
|---|---|---|
| X.Y.Z | YYYY-MM-DD | … |

---

## 5. Numbering and Storage Rules

1. Form: `LOU-NNN`  
2. Sequential integer numbering  
3. Numbers are never reused  
4. Filename convention: `LOU-NNN-Short-Title.md`  
5. Storage: `Engineering-Office/definition/`  
6. No LOU instance is created by TMP-002 itself  

---

## 6. Conformance to TMP-001

TMP-002 specializes TMP-001 for LOU artifacts.  
Where both apply, LOU-required sections in this template remain mandatory and map into the TMP-001 structural model.

---

## 7. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial LOU template under ECR-002 / CWC-CE-054. |
