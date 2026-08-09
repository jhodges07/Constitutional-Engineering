# STD-001 — Engineering Workflow Standard

**Document ID:** STD-001  
**Title:** Engineering Workflow Standard  
**Classification:** Engineering Standard  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Related Workflow:** WF-001 — Engineering Office Operating Workflow  
**Governing ECR:** ECR-002 — Engineering Definition / LOU Controlled Adoption  
**Status:** Active  
**Version:** 1.2.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This standard defines the engineering workflow used throughout the Constitutional Engineering Office.

It establishes a two-phase lifecycle:

1. **Engineering Definition** — develop and accept shared understanding and requirements before implementation authorization  
2. **Controlled Execution** — authorize, implement, verify, accept, and release governed work  

It separates engineering planning from AI implementation and from engineering reporting, and binds operational execution to WF-001.

---

## 2. Scope

### 2.1 In Scope

1. Engineering artifact roles for LOU, SPEC (Requirements), CWC-CE, ECR, CEP, and CER  
2. Minimum workflow sequence from Engineering Definition through Controlled Execution and Git actions  
3. Role boundaries for Human Engineer and AI implementers  
4. Research / evidence non-authority rules  

### 2.2 Out of Scope

1. Detailed release baseline sequencing (see WF-002)  
2. Domain-control authorship for AGCL, NBBF, or CDT  
3. UNBKE runtime dependency  
4. Legislative-specific Engineering Definition extensions (later dedicated CWC; STD-008 unchanged by ECR-002 implementation)  

---

## 3. Engineering Artifacts

### 3.0 Force Separation (Mandatory)

| Artifact | Force |
|---|---|
| **LOU** | What do we agree we understand about the problem, intent, boundaries, evidence, uncertainty, and direction? |
| **SPEC** | What must the engineered solution accomplish? (structured Requirements / Scope Definition) |
| **CWC-CE** | What specific controlled work is now authorized? |
| **ECR** | What controlled configuration change is approved when STD-014 applies? |
| **CEP** | What executable instructions implement the approved work? |
| **CER** | What was actually done and verified? |

These forces shall not be blurred.

### 3.1 LOU — Letter of Understanding

Official identifier series: `LOU-NNN` (sequential; numbers never reused).  
Storage: `Engineering-Office/definition/`.  
Template: TMP-002.

Purpose: record agreed engineering understanding after Human Engineer acceptance.

An LOU may include a **Research Record / Evidence Annex**. Research is informative, not authoritative.

**Authority limits:**

1. LOU acceptance **does not** authorize implementation.  
2. Research findings **do not** become requirements by listing alone.  
3. AI research **does not** create engineering authority.  
4. Silence is not LOU acceptance.

### 3.2 SPEC — Requirements / Scope Definition

Structured Requirements / Scope Definition preferentially uses the **SPEC** series (`SPEC-NNN`) or an expressly approved equivalent.

Purpose: define what the engineered solution must accomplish after LOU acceptance (when Engineering Definition applies).

**No parallel REQ series is authorized by this standard.**

**Authority limits:**

1. Requirements/SPEC acceptance **does not** authorize implementation.  
2. SPEC feeds CWC-CE; it does not replace CWC-CE approval.

### 3.3 CWC-CE — Constitutional Engineering Work Card

Formerly referenced historically as CEWC.  
Current official identifier series: `CWC-CE-NNN`.

Purpose: the discrete **Controlled Execution** work-authorization and task specification.

Defines:

- Objective  
- Scope  
- Deliverables  
- Acceptance Criteria  
- Constraints  
- Engineering Notes  

When Engineering Definition applies, a CWC-CE shall cite accepted LOU and SPEC (or record an explicit Human Engineer waiver for trivial/corrective work).

The CWC-CE is written for the Human Engineer.

### 3.4 CEP — Cursor Engineering Prompt

Purpose: translate an approved CWC-CE into executable instructions for Cursor AI.

Cursor should never receive incomplete engineering intent.  
Every CEP shall reference the originating CWC-CE.  
CEP shall not treat LOU or SPEC acceptance as sufficient authorization.

### 3.5 CER — Constitutional Engineering Report

Purpose: document implementation results under STD-015.

Includes, at minimum:

- Files changed  
- Summary of modifications  
- Validation performed  
- Outstanding issues  
- Recommendations / next actions  

A CER does not authorize implementation.

### 3.6 ECR — Engineering Change Request

When required by STD-014, an ECR authorizes controlled configuration change.  
LOU/SPEC acceptance never substitutes for a required ECR.

---

## 4. Engineering Workflow

### 4.1 Two-Phase Lifecycle

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
Human Engineer Requirements Approval / CWC-Readiness
    ↓

CONTROLLED EXECUTION

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
    ↓
Release / Publication
(when separately authorized)
```

Release baseline certification after acceptance is governed by WF-002.

### 4.2 Engineering Definition Rules

1. Research is informative, not authoritative.  
2. AI research does not create engineering authority.  
3. LOU acceptance requires explicit Human Engineer acceptance (HG-D1).  
4. Requirements/SPEC acceptance requires explicit Human Engineer acceptance (HG-D2).  
5. Silence is not acceptance.  
6. LOU acceptance does **not** authorize implementation.  
7. Requirements/SPEC acceptance does **not** authorize implementation.  
8. Exploratory research that does not modify governed repository artifacts may precede a CWC.  
9. Durable Engineering Definition artifacts written into the repository are governed engineering work and require approved CWC authorization (definition-class / assessment-class / adoption-class as applicable), except where the Human Engineer records an express narrow exception under POL-001.  

### 4.3 Controlled Execution Rules

1. Controlled Execution begins with an approved CWC-CE.  
2. CWC-CE remains the discrete Controlled Execution authorization mechanism.  
3. ECR remains required whenever STD-014 requires controlled change.  
4. Existing Human Approval Gates HG-1…HG-8 and AI Execution Gates AG-1…AG-5 remain in force as detailed in WF-001.  

### 4.4 Human Engineer Definition Gates

| Gate | Required before |
|---|---|
| **HG-D1 — LOU Acceptance** | Treating an LOU as accepted engineering understanding for Requirements / CWC feed-forward |
| **HG-D2 — Requirements Acceptance / CWC-Readiness** | Issuing implementation-class CWC that depends on Engineering Definition |

### 4.5 Research Record / Evidence Annex

When research is recorded under an LOU, the Research Record / Evidence Annex shall support at minimum:

| Field | Requirement |
|---|---|
| Source ID | Stable local reference |
| Source Class | Taxonomy class below |
| Source Locator | Citation, URL, export id, or equivalent |
| Collector | Human or AI system identity |
| Collection Date | Required |
| Source Summary | Informative only |
| Conflicting Evidence | Required when present |
| Verification Status | As known |
| Authority Status | Default: `Non-authoritative` |

**Initial source classes** (classification does not confer engineering authority):

`PRIMARY-LEGAL` | `GOV-DATA` | `SECONDARY-ANALYSIS` | `TESTIMONY` | `HISTORICAL` | `SCRIPTURE` | `AI-SYNTHESIS` | `CONTROL-DOC`

**External AI provenance** (ChatGPT, Grok, Cursor, or other): when available, record system name, model descriptor, session/export identifier, date, prompt/context summary or controlled reference, and role = `Research Assistant — Non-authoritative`. AI synthesis shall not be represented as primary authority.

No separate primary Research Record document series is authorized by this standard.

### 4.6 Backward Compatibility

Work authorized before LOU adoption remains valid without retroactive LOU requirements.  
Future material projects should use Engineering Definition when applicable.  
Trivial/corrective work may waive LOU/SPEC only through explicit Human Engineer authorization in the CWC.

---

## 5. Roles

### 5.1 Human Engineer

1. Defines engineering intent  
2. Accepts or rejects LOUs (HG-D1)  
3. Accepts or rejects Requirements/SPEC / CWC-readiness (HG-D2)  
4. Approves work authorization (CWC-CE)  
5. Approves commits, pushes, tags, and publication as required  
6. Remains final authority under POL-001  

### 5.2 Constitutional Engineer / Architecture Support

1. Designs and maintains architecture integrity  
2. Prepares LOU / SPEC / CWC-CE / ECR / CEP routing packages when authorized  
3. Collects and documents research as informative only  
4. Reviews CER quality and cross-repository consistency  
5. Does not govern in place of the Human Engineer  
6. Does not accept LOUs or Requirements/SPEC  
7. Does not convert research into requirements without Human Engineer acceptance  

### 5.3 Cursor AI / Implementing Agents

1. Implements approved CEP scope only  
2. Never changes repositories outside approved scope  
3. Never commits, tags, or pushes without Human Engineer approval  
4. Never invents policy, controls, or missing authority  
5. Never treats LOU or SPEC acceptance as implementation authorization  

---

## 6. Engineering Principles

1. Engineering Definition precedes Controlled Execution for material work subject to Definition.  
2. Specification before implementation.  
3. Human approval before repository modification that advances governed artifacts.  
4. Every Controlled Execution implementation traces to a CWC-CE.  
5. Every completed CEP produces a CER unless an approved exception exists.  
6. Git history reflects approved engineering work.  
7. Truthful verification only; unperformed checks are not reported as complete.  
8. AI assists; AI does not own or approve.  
9. Research informs; research does not authorize.  
10. LOU and SPEC acceptances do not authorize implementation.  

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
| 1.2.0 | 2026-08-08 | ECR-002 / CWC-CE-054: add Engineering Definition / LOU / SPEC phase; dual-phase lifecycle; research non-authority; HG-D1/HG-D2; preserve Controlled Execution CWC supremacy. |
