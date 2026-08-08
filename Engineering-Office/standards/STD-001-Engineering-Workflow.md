# STD-001 — Engineering Workflow Standard

**Document ID:** STD-001  
**Title:** Engineering Workflow Standard  
**Classification:** Engineering Standard  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Related Workflow:** WF-001 — Engineering Office Operating Workflow  
**Status:** Active  
**Version:** 1.1.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This standard defines the engineering workflow used throughout the Constitutional Engineering Office.

It separates engineering planning from AI implementation and from engineering reporting, and binds operational execution to WF-001.

---

## 2. Scope

### 2.1 In Scope

1. Engineering artifact roles for CWC-CE, CEP, and CER  
2. Minimum workflow sequence from specification through Git actions  
3. Role boundaries for Human Engineer and AI implementers  

### 2.2 Out of Scope

1. Detailed release baseline sequencing (see WF-002)  
2. Domain-control authorship for AGCL, NBBF, or CDT  
3. UNBKE runtime dependency  

---

## 3. Engineering Artifacts

### 3.1 CWC-CE — Constitutional Engineering Work Card

Formerly referenced historically as CEWC.  
Current official identifier series: `CWC-CE-NNN`.

Purpose: the engineering specification.

Defines:

- Objective  
- Scope  
- Deliverables  
- Acceptance Criteria  
- Constraints  
- Engineering Notes  

The CWC-CE is written for the Human Engineer.

### 3.2 CEP — Cursor Engineering Prompt

Purpose: translate an approved CWC-CE into executable instructions for Cursor AI.

Cursor should never receive incomplete engineering intent.  
Every CEP shall reference the originating CWC-CE.

### 3.3 CER — Constitutional Engineering Report

Purpose: document implementation results under STD-015.

Includes, at minimum:

- Files changed  
- Summary of modifications  
- Validation performed  
- Outstanding issues  
- Recommendations / next actions  

---

## 4. Engineering Workflow

```
CWC-CE
    ↓
Human Review / Approval
    ↓
ECR (when required by STD-014)
    ↓
CEP
    ↓
Cursor Implementation
    ↓
CER
    ↓
Human Acceptance
    ↓
Git Commit (approved)
    ↓
Git Push (approved)
```

Release baseline certification after acceptance is governed by WF-002.

---

## 5. Roles

### 5.1 Human Engineer

1. Defines engineering intent  
2. Approves work authorization  
3. Approves commits, pushes, tags, and publication as required  
4. Remains final authority under POL-001  

### 5.2 Constitutional Engineer / Architecture Support

1. Designs and maintains architecture integrity  
2. Prepares CWC-CE / ECR / CEP routing packages  
3. Reviews CER quality and cross-repository consistency  
4. Does not govern in place of the Human Engineer  

### 5.3 Cursor AI / Implementing Agents

1. Implements approved CEP scope only  
2. Never changes repositories outside approved scope  
3. Never commits, tags, or pushes without Human Engineer approval  
4. Never invents policy, controls, or missing authority  

---

## 6. Engineering Principles

1. Specification before implementation.  
2. Human approval before repository modification.  
3. Every implementation traces to a CWC-CE.  
4. Every completed CEP produces a CER unless an approved exception exists.  
5. Git history reflects approved engineering work.  
6. Truthful verification only; unperformed checks are not reported as complete.  
7. AI assists; AI does not own or approve.  

---

## 7. Conformance

Conformance to STD-001 is mandatory for Engineering Office workflow practice.  
Where STD-001 and WF-001 both apply, WF-001 provides the authoritative operating sequence detail and STD-001 provides the binding artifact/role principles.  
Conflicts escalate to the Human Engineer.

---

## 8. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial workflow standard content (pre-metadata form). |
| 1.1.0 | 2026-08-08 | CER-001 remediation: add Office metadata, align CEWC→CWC-CE naming, add Version History, bind to WF-001/STD-014/STD-015. |
