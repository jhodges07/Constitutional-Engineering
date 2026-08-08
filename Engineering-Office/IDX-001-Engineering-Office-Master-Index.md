# IDX-001 — Engineering Office Master Index

**Document ID:** IDX-001  
**Title:** Engineering Office Master Index  
**Classification:** Engineering Office Index  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Status:** Active  
**Version:** 1.1.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This document is the authoritative catalog of all Engineering Office governing documents.

It provides:

- A single inventory of architecture, policy, standards, workflows, and related document types
- The Engineering Office document hierarchy
- Repository catalog, ownership, and relationships
- Numbering conventions for operational engineering artifacts
- The current Engineering Office baseline reference

---

## 2. Scope

### 2.1 In Scope

This index catalogs governing and operational document types under the Constitutional Engineering Office, including:

1. Architecture documents  
2. Policy documents  
3. Engineering standards  
4. Engineering workflows  
5. Numbering conventions for CWC-CE, ECR, CER, and CEP  
6. Repository list, owners, and relationships  
7. Reserved future document types  
8. The active Engineering Office baseline  

### 2.2 Out of Scope

This index does not:

1. Replace the authority of indexed documents  
2. Modify architecture, standards, policies, or workflows  
3. Catalog every file inside control or manager repositories  
4. Require UNBKE  

### 2.3 Catalog Field Model

Every cataloged document entry shall include:

| Field | Meaning |
|---|---|
| Identifier | Official document ID |
| Title | Official document title |
| Classification | Document class |
| Status | Active / Complete / Reserved / Future / etc. |
| Governing Authority | Authority under which the document operates |

---

## 3. Engineering Office Document Hierarchy

```
Human Engineer
      ↓
Architecture (ARCH)
      ↓
Policies (POL)
      ↓
Standards (STD)
      ↓
Workflows (WF)
      ↓
Templates / Indexes / Guides (as adopted)
      ↓
Managers
      ↓
CWC-CE
      ↓
ECR (when required)
      ↓
CEP
      ↓
CER
```

### 3.1 Hierarchy Diagram

```
┌──────────────────────────────────────────────┐
│         Constitutional Engineering Office     │
│                                              │
│  ARCH  →  POL  →  STD  →  WF  →  IDX/TMP... │
│                 │                            │
│                 ▼                            │
│        Operational Artifacts                 │
│     CWC-CE → ECR → CEP → CER                 │
└──────────────────────────────────────────────┘
```

Lower-authority artifacts shall not override higher-authority artifacts.

---

## 4. Architecture Documents

| Identifier | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| ARCH-001 | Constitutional Engineering Architecture | Architecture Baseline | Active | Constitutional Engineering Office |
| ARCH-002 | Engineering Manager Architecture | Architecture Baseline | Active | Constitutional Engineering Office |
| ARCH-003 | Engineering Ownership Architecture | Architecture Baseline | Draft | Constitutional Engineering Office |
| ARCH-004 | Engineering Interface Architecture | Architecture Baseline | Draft | Constitutional Engineering Office |

**Path root:** `Engineering-Office/architecture/`

| Identifier | Path |
|---|---|
| ARCH-001 | `Engineering-Office/architecture/ARCH-001-Constitutional-Engineering-Architecture.md` |
| ARCH-002 | `Engineering-Office/architecture/ARCH-002-Engineering-Manager-Architecture.md` |
| ARCH-003 | `Engineering-Office/architecture/ARCH-003-Engineering-Ownership-Architecture.md` |
| ARCH-004 | `Engineering-Office/architecture/ARCH-004-Engineering-Interface-Architecture.md` |

---

## 5. Policy Documents

| Identifier | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| POL-001 | Engineering Office Governance Policy | Engineering Office Policy | Active | Constitutional Engineering Office |

**Path:** `Engineering-Office/policies/POL-001-Engineering-Office-Governance.md`

---

## 6. Engineering Standards

| Identifier | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| STD-001 | Engineering Workflow | Engineering Standard | Active | Constitutional Engineering Office |
| STD-002 | Git Operations | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-003 | Cursor Operations | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-004 | Engineering Reviews | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-005 | Document Numbering | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-006 | Repository Management | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-007 | Legislative Authoring | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-008 | Legislative Lifecycle | Engineering Standard | Active | Constitutional Engineering Office |
| STD-009 | Charter Authoring | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-010 | Budget Authoring | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-011 | Public Documentation | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-012 | Template Standards | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-013 | Audit Requirements | Engineering Standard | Reserved | Constitutional Engineering Office |
| STD-014 | Engineering Change Management | Engineering Standard | Active | Constitutional Engineering Office |
| STD-015 | Constitutional Engineering Reports | Engineering Standard | Active | Constitutional Engineering Office |

**Path root:** `Engineering-Office/standards/`

**Status notes:**

- `Active` = populated governing standard content exists  
- `Reserved` = identifier and filename exist in the official sequence; body content not yet authored  

Official standards sequence is maintained under STD-014 and ECR-001 history through STD-013, extended by later approved standard creations STD-014 and STD-015.

---

## 7. Engineering Workflows

| Identifier | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| WF-001 | Engineering Office Operating Workflow | Engineering Workflow | Active | Constitutional Engineering Office |
| WF-002 | Engineering Release Workflow | Engineering Workflow | Draft | Constitutional Engineering Office |

**Path root:** `Engineering-Office/workflows/`

| Identifier | Path |
|---|---|
| WF-001 | `Engineering-Office/workflows/WF-001-Engineering-Office-Operating-Workflow.md` |
| WF-002 | `Engineering-Office/workflows/WF-002-Engineering-Release-Workflow.md` |

---

## 7A. Templates

| Identifier | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| TMP-001 | Engineering Office Master Document Template | Engineering Office Template | Active | Constitutional Engineering Office |

**Path:** `Engineering-Office/templates/TMP-001-Master-Document-Template.md`

---

## 8. Engineering Work Cards

### 8.1 Document Type

| Identifier Pattern | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| CWC-CE-NNN | Constitutional Engineering Work Card | Engineering Work Authorization / Specification | Active convention | Constitutional Engineering Office |

### 8.2 Numbering Convention

1. Form: `CWC-CE-NNN`  
2. Sequential integer numbering  
3. Numbers are not reused  
4. A CWC-CE authorizes and specifies work; it does not by itself record implementation completion  

### 8.3 Authority Position

CWC-CE artifacts operate below Standards and Workflows and above CEP / CER execution records.

---

## 9. Engineering Change Requests

### 9.1 Document Type

| Identifier Pattern | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| ECR-NNN | Engineering Change Request | Engineering Change Request | Active convention | Constitutional Engineering Office |

### 9.2 Numbering Convention

1. Form: `ECR-NNN`  
2. Sequential numbering  
3. Numbers never reused  
4. Filename convention: `ECR-NNN-Short-Title.md`  
5. Storage: `Engineering-Office/audits/` unless later relocated by approved standard  

### 9.3 Current ECR Instances

| Identifier | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| ECR-001 | Standard Numbering Resolution | Engineering Change Request | Complete | Constitutional Engineering Office |

---

## 10. Constitutional Engineering Reports

### 10.1 Document Type

| Identifier Pattern | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| CER-NNN | Constitutional Engineering Report | Constitutional Engineering Report | Active convention | Constitutional Engineering Office |

### 10.2 Numbering Convention

1. Form: `CER-NNN`  
2. Sequential numbering  
3. Numbers never reused  
4. Filename convention: `CER-NNN-Short-Title.md`  
5. Storage: `Engineering-Office/audits/` unless later relocated by approved standard  

### 10.3 Current CER Instances

| Identifier | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| CER-001 | Pre-Push Engineering Audit | Constitutional Engineering Report | Submitted | Constitutional Engineering Office |
| CER-002 | Release Readiness Remediation | Constitutional Engineering Report | Submitted | Constitutional Engineering Office |

**Path root:** `Engineering-Office/audits/`

---

## 11. Cursor Engineering Prompts

### 11.1 Document Type

| Identifier Pattern | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| CEP-NNN | Cursor Engineering Prompt | Cursor Engineering Prompt | Active convention | Constitutional Engineering Office |

### 11.2 Numbering Convention

1. Form: `CEP-NNN`  
2. Sequential numbering  
3. Numbers never reused  
4. Every CEP shall reference its governing CWC-CE  
5. Every completed CEP produces a CER unless an approved exception exists  

### 11.3 Authority Position

CEPs translate approved work into executable implementation instructions.  
CEPs do not authorize work and do not replace CERs.

---

## 12. Repository List

| Repository | Path / Location | Role | Status |
|---|---|---|---|
| Engineering-Office | `D:\Constitutional-Engineering\Engineering-Office` | Architectural root; standards, policies, workflows, audits | Active |
| AGCL-Control-Documents | `X:\GitHub\AGCL-Control-Documents` | AGCL control documents | Active |
| NBBF-Control-Documents | `X:\GitHub\NBBF-Control-Documents\NBBF-Control-Documents` | NBBF control documents | Active |
| CDT-Control-Documents | `X:\GitHub\CDT-Control-Documents` | CDT control documents | Reserved (empty surface; not in Release Baseline 1.0 set) |
| Legislative-Manager | `X:\GitHub\Legislative-Manager` | Specialized legislative manager | Active |
| Charter-Manager | Future | Specialized charter manager | Future |
| Budget-Manager | Future | Specialized budget manager | Future |
| UNBKE | Future | Runtime / knowledge engine | Future (not required) |
| Public Repositories | Designated per publication approval | Publication distribution surfaces | As authorized |

**Repository count (current active):** 4  
**Repository count (including reserved/empty CDT and future declared):** 8 primary surfaces (+ public repositories as designated)

---

## 13. Repository Owners

| Repository | Accountable Steward | Supporting Role |
|---|---|---|
| Engineering-Office | Human Engineer | Constitutional Engineer |
| AGCL-Control-Documents | Human Engineer / designated AGCL steward | Constitutional Engineer |
| NBBF-Control-Documents | Human Engineer / designated NBBF steward | Constitutional Engineer |
| CDT-Control-Documents | Human Engineer / designated CDT steward | Constitutional Engineer |
| Legislative-Manager | Human Engineer / Legislative Manager steward | Legislative Manager / Constitutional Engineer |
| Charter-Manager (future) | Human Engineer / designated steward | TBD when established |
| Budget-Manager (future) | Human Engineer / designated steward | TBD when established |
| Public repositories | Human Engineer / designated publication steward | Repository stewards as assigned |

---

## 14. Repository Relationships

```
Engineering-Office
      │
      ├─ governs engineering process for ──► AGCL-Control-Documents
      ├─ governs engineering process for ──► NBBF-Control-Documents
      ├─ governs engineering process for ──► CDT-Control-Documents
      │
      └─ governs manager practice for ─────► Legislative-Manager
                                             Charter-Manager (future)
                                             Budget-Manager (future)

AGCL / NBBF / CDT
      │
      └─ provide domain controls consumed by managers and derived artifacts

Managers / Control Repositories
      │
      └─ publish approved outputs to ──────► Public Repositories

UNBKE (future)
      │
      └─ optional future runtime; not a current dependency
```

### 14.1 Document Dependency Diagram

```
                    ARCH-001
                        │
              ARCH-002 / ARCH-003 / ARCH-004
                        │
                     POL-001
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
     STD-001         STD-014         STD-015
   (Workflow)      (Change Mgmt)      (CER)
        │               │               │
        └───────────────┼───────────────┘
                        ▼
                  WF-001 / WF-002
                        │
                  IDX-001 / TMP-001
                        │
         CWC-CE ──► ECR ──► CEP ──► CER
                        │
                        ▼
              Repository Implementations
```

Relationship rules:

1. Architecture governs policy and standards.  
2. Standards govern workflows and operational artifacts.  
3. WF-001 operationalizes the end-to-end work sequence.  
4. WF-002 operationalizes release baselines after Human Acceptance.  
5. IDX-001 catalogs; it does not outrank architecture or standards.  
6. TMP-001 governs master document structure for controlled Office documents.  
7. ECR is required only for controlled changes under STD-014.  
8. CER records implementation under STD-015.  

---

## 15. Future Document Types

The following document types are reserved for future adoption. They are not active governing series at the effective date of this index.

| Type | Identifier Pattern | Intended Use | Status |
|---|---|---|---|
| ADR | ADR-NNN | Architecture Decision Records | Future |
| SPEC | SPEC-NNN | Detailed technical or domain specifications | Future |
| NOTE | NOTE-NNN | Non-normative engineering notes | Future |
| GUIDE | GUIDE-NNN | Implementation guidance subordinate to standards | Future |

Note: `TMP-001` is Active and cataloged in Section 7A. Additional TMP-series documents may be adopted later.

Future types become active only through approved Engineering Office process and index update.

---

## 16. Engineering Office Baseline

### 16.1 Baseline Name

**Engineering Office Baseline BL-EO-2026-08-08**

### 16.2 Included Governing Documents

| Identifier | Title | Status |
|---|---|---|
| ARCH-001 | Constitutional Engineering Architecture | Active |
| ARCH-002 | Engineering Manager Architecture | Active |
| ARCH-003 | Engineering Ownership Architecture | Draft (pending Human Engineer acceptance) |
| ARCH-004 | Engineering Interface Architecture | Draft (pending Human Engineer acceptance) |
| POL-001 | Engineering Office Governance Policy | Active |
| STD-001 | Engineering Workflow | Active |
| STD-002 through STD-007 | Reserved standards in official sequence | Reserved |
| STD-008 | Legislative Lifecycle | Active |
| STD-009 through STD-013 | Reserved standards in official sequence | Reserved |
| STD-014 | Engineering Change Management | Active |
| STD-015 | Constitutional Engineering Reports | Active |
| WF-001 | Engineering Office Operating Workflow | Active |
| WF-002 | Engineering Release Workflow | Draft (pending Human Engineer acceptance) |
| TMP-001 | Engineering Office Master Document Template | Active |
| IDX-001 | Engineering Office Master Index | Active |
| ECR-001 | Standard Numbering Resolution | Complete |
| CER-001 | Pre-Push Engineering Audit | Submitted |
| CER-002 | Release Readiness Remediation | Submitted |

### 16.3 Baseline Rules

1. This baseline is the current authoritative Engineering Office configuration cataloged by IDX-001.  
2. Baseline changes require approved process under STD-014 / WF-001 / WF-002 when controlled configuration or release changes.  
3. Reserved standards remain part of the official numbering sequence even before full normative authorship; Reserved placeholder files shall carry Document ID, Status=`Reserved`, and Version History.  
4. Draft architecture/workflow documents remain cataloged but are not treated as Human-Accepted release gates until accepted.  
5. UNBKE is not part of the active operational baseline.  
6. CDT-Control-Documents remains a reserved empty surface until populated under authorized work; it is excluded from Release Baseline 1.0 synchronization requirements unless expressly added by Human Engineer.  

---

## 17. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Engineering Office Master Index establishing the authoritative governing-document catalog. |
| 1.1.0 | 2026-08-08 | CER-001 remediation: catalog ARCH-002/003/004, TMP-001, WF-002, CER-001/CER-002; correct TMP series posture; mark CDT reserved/empty; expand baseline listing. |

---

## Appendix A — Index Document Self-Entry

| Identifier | Title | Classification | Status | Governing Authority |
|---|---|---|---|---|
| IDX-001 | Engineering Office Master Index | Engineering Office Index | Active | Constitutional Engineering Office |

**Path:** `Engineering-Office/IDX-001-Engineering-Office-Master-Index.md`
