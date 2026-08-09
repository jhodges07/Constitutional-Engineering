# ARCH-002 — Engineering Manager Architecture

**Document ID:** ARCH-002  
**Title:** Engineering Manager Architecture  
**Classification:** Architecture Baseline  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Status:** Active  
**Version:** 1.1.0  
**Effective Date:** 2026-08-08  
**Governing ECR:** ECR-002 — Engineering Definition / LOU Controlled Adoption  

---

## 1. Purpose

This document defines the architecture governing every specialized engineering manager within the Constitutional Engineering ecosystem.

It establishes:

- What a manager is
- What a manager may and may not do
- The standard structure every manager shall follow
- How managers interface with the Engineering Office, control repositories, and each other
- How future managers are added without modifying existing managers

ARCH-002 specializes ARCH-001 for the manager layer. It does not replace ARCH-001.

---

## 2. Scope

### 2.1 In Scope

This architecture applies to:

1. All current specialized managers  
2. All future specialized managers added under this architecture  
3. Manager repositories, folders, required documents, lifecycle, interfaces, registration, and certification  
4. Manager relationships to the Engineering Office, AGCL, NBBF, CDT, and future UNBKE  

### 2.2 Out of Scope

This architecture does not:

1. Draft legislation, charters, budgets, policies, ballots, audits, APIs, or publications  
2. Modify AGCL, NBBF, or CDT control content  
3. Redefine Engineering Office standards, policies, or workflows  
4. Require UNBKE for current manager operation  

### 2.3 Authority Position

```
ARCH-001
    ↓
ARCH-002
    ↓
Standards / Policies / Workflows
    ↓
Registered Managers
    ↓
Manager Specs / Templates / Prompts
    ↓
Accepted Office LOU / SPEC (consume only; do not own Office LOU authority)
    ↓
CWC-CE → ECR (when required) → CEP → CER
```

Managers are subordinate to Architecture, Policy, Standards, and Workflows.  
Managers may **consume** accepted Engineering Definition outputs (Office LOU / SPEC).  
Managers shall **not** own, redefine, or substitute for Office LOU authority.  
LOU/SPEC acceptance does not authorize manager implementation; approved CWC-CE remains required.

---

## 3. Manager Definition

A **Specialized Engineering Manager** is a domain-scoped engineering system that:

1. Operates under Constitutional Engineering Office authority  
2. Owns a bounded engineering domain  
3. Produces domain artifacts through approved workflow  
4. Consumes architecture, standards, policies, workflows, and applicable controls  
5. Does not hold Office-wide governance authority  

A manager may be implemented as:

- a dedicated repository, and/or  
- a defined manager surface inside an authorized repository structure  

In either form, the manager remains architecturally distinct and separately registerable.

### 3.1 Initial Managers

| Manager | Code | Domain | Current Status |
|---|---|---|---|
| Legislative Manager | `MGR-LEG` | Legislative and statutory engineering artifacts | Active |
| Charter Manager | `MGR-CHR` | Charter and organic local governance instruments | Declared |
| Budget Manager | `MGR-BDG` | Budget and fiscal engineering aligned to NBBF | Declared |
| Policy Manager | `MGR-POL` | Policy artifact engineering under Office standards | Declared |
| Election Manager | `MGR-ELC` | Election process and election-instrument engineering | Declared |
| Audit Manager | `MGR-AUD` | Audit package and conformance-evidence engineering | Declared |
| Publication Manager | `MGR-PUB` | Publication packaging and release engineering | Declared |
| API Manager | `MGR-API` | Interface/API specification engineering for governed surfaces | Declared |

`Active` means an operational manager surface exists.  
`Declared` means the manager is architecturally recognized and may be stood up later without redesigning this architecture.

---

## 4. Manager Responsibilities

Every specialized manager shall:

1. Maintain clear domain scope and refuse out-of-scope work  
2. Conform to ARCH-001, ARCH-002, POL-001, applicable standards, and WF-001  
3. Preserve traceability from artifacts to source authority and governing work cards  
4. Consume control documents without superseding them  
5. Produce domain templates, specifications, and prompts only within assigned scope  
6. Support STD-008 lifecycle rules when producing lifecycle-controlled artifacts  
7. Report conflicts, gaps, and uncertainty to the Constitutional Engineer / Human Engineer  
8. Prepare CERs through approved implementation workflow when CEP work is executed  
9. Keep public-facing outputs publication-ready only after approved publication gates  
10. Remain operable without UNBKE  

---

## 5. Manager Authority Boundaries

### 5.1 Managers May

1. Own domain engineering structure inside their registered scope  
2. Author domain specifications, templates, and prompts  
3. Reference AGCL, NBBF, CDT, and Engineering Office governing documents  
4. Recommend ECRs when controlled change appears necessary  
5. Coordinate with other managers through defined interfaces  

### 5.2 Managers Shall Not

1. Redefine ARCH-001, ARCH-002, policies, or standards  
2. Approve their own work in place of Human Engineer acceptance  
3. Invent policy, law, or controls  
4. Modify another manager’s repository or registered structure without approved cross-manager work  
5. Claim ownership of AGCL, NBBF, or CDT concepts  
6. Bypass CWC-CE / ECR / CEP / CER workflow requirements  
7. Depend on UNBKE as a hard requirement  

### 5.3 Boundary Rule

If a requested action is outside a manager’s registered domain, the manager shall stop and escalate.  
Domain expansion requires Manager Registration update under Section 17, not informal scope creep.

---

## 6. Standard Manager Structure

Every manager shall implement the following logical architecture:

```
Manager
├── Identity (code, name, domain, status)
├── Specifications
├── Templates
├── Prompts
├── Workflows (manager-local, subordinate to WF-001)
├── Audits / Records (as applicable)
└── Interfaces
    ├── Engineering Office
    ├── Control Repositories
    ├── Peer Managers
    └── Publication Surfaces
```

Managers may add domain-specific substructures.  
Managers shall not omit the required folders and documents defined below.

---

## 7. Required Manager Folders

Unless an approved exception is recorded, every manager repository or manager surface shall include:

| Folder | Purpose |
|---|---|
| `specifications/` | Manager and domain specifications |
| `templates/` | Domain templates organized by jurisdiction or domain taxonomy |
| `prompts/` | Manager operating prompts and agent instructions |
| `audits/` | Manager-local audit, ECR/CER copies or references as applicable |
| `workflows/` | Optional manager-local procedures subordinate to WF-001 |

Minimum required folders:

1. `specifications/`  
2. `templates/`  
3. `prompts/`  

Recommended folders:

4. `audits/`  
5. `workflows/`  

Legislative Manager currently satisfies the minimum through existing `specifications/`, `templates/`, and `prompts/` surfaces. Declared managers shall create the minimum structure when activated.

---

## 8. Required Manager Documents

Every registered manager shall maintain, at minimum:

| Document | Requirement |
|---|---|
| Manager Charter / Spec | Defines domain, responsibilities, and boundaries |
| Manager Prompt | Operating instructions for the manager agent |
| Template Index or root templates tree | Domain template organization |
| Registration Record reference | Link to Engineering Office manager registry entry |

When activated, a manager should have:

1. `specifications/SPEC-XXX-{Manager}-Architecture.md` or equivalent manager domain spec  
2. `prompts/{Manager}.md`  
3. Populated or explicitly reserved `templates/` taxonomy  

Document creation for declared managers occurs under approved CWC-CE work and shall not require modification of unrelated managers.

---

## 9. Manager Lifecycle

```
Proposed
    ↓
Registered
    ↓
Structured
    ↓
Certified
    ↓
Active
    ↓
Suspended
    ↓
Retired
```

| State | Meaning |
|---|---|
| Proposed | Manager concept identified |
| Registered | Manager identity and domain recorded under Section 17 |
| Structured | Required folders/documents created |
| Certified | Section 18 certification completed |
| Active | Authorized for production engineering work |
| Suspended | Temporarily barred from production work |
| Retired | Permanently withdrawn; records retained |

Lifecycle transitions require Human Engineer approval.  
AI may prepare transition packages; AI may not self-activate a manager.

---

## 10. Manager Interfaces

### 10.1 Interface Types

| Interface | Purpose |
|---|---|
| Office Interface | Consume ARCH/POL/STD/WF/TMP/IDX and submit work through WF-001 |
| Control Interface | Reference applicable AGCL/NBBF/CDT controls |
| Peer Interface | Exchange references with other managers without transferring ownership |
| Publication Interface | Hand off approved packages to Publication Manager / public surfaces |
| Runtime Interface (future) | Optional UNBKE integration when declared operational |

### 10.2 Interface Rules

1. Interfaces are reference-based and contract-based, not ownership-based.  
2. Cross-manager work requires explicit scope in the governing CWC-CE.  
3. No manager may silently write into another manager’s controlled paths.  
4. Interface additions for a new manager shall be additive.

---

## 11. Repository Relationships

```
Engineering-Office
        │
        ├─ registers / certifies / governs ──► Managers
        │
        ├─ governs engineering process ─────► AGCL / NBBF / CDT
        │
        └─ receives architecture conformance from managers

Managers
        │
        ├─ Legislative Manager (active)
        ├─ Charter Manager
        ├─ Budget Manager
        ├─ Policy Manager
        ├─ Election Manager
        ├─ Audit Manager
        ├─ Publication Manager
        └─ API Manager

Managers consume controls; controls do not depend on managers for authority.
Approved outputs may flow to public repositories through publication gates.
```

### 11.1 Independence Rule

Each manager is independently versioned and deployable.  
Activation of one declared manager shall not require modification of another manager’s artifacts.

---

## 12. Engineering Office Relationship

| Topic | Rule |
|---|---|
| Authority | Engineering Office is architectural and process superior |
| Managers consume | ARCH, POL, STD, WF, TMP, IDX |
| Managers produce | Domain artifacts and manager-local specs/templates/prompts |
| Escalation | Conflicts and boundary questions escalate to Constitutional Engineer / Human Engineer |
| Change control | Office-level changes use ECR under STD-014 when required |

Managers specialize execution.  
The Engineering Office governs architecture and engineering process.

---

## 13. AGCL Relationship

| Manager | AGCL Affinity |
|---|---|
| Legislative Manager | Primary affinity for legislative form under AGCL-applicable controls |
| Charter Manager | Affinity for charter structures constrained by AGCL-applicable controls |
| Policy Manager | Affinity where policy artifacts implicate AGCL controls |
| Other managers | Reference AGCL only when domain scope requires it |

AGCL controls remain owned by AGCL-Control-Documents.  
Managers may reference AGCL; they shall not fork AGCL ownership.

---

## 14. NBBF Relationship

| Manager | NBBF Affinity |
|---|---|
| Budget Manager | Primary affinity |
| Legislative Manager | Reference when fiscal/statutory packages implicate NBBF |
| Audit Manager | Reference when auditing fiscal/node controls |
| Other managers | Reference only when domain scope requires it |

NBBF controls remain owned by NBBF-Control-Documents.  
Budget Manager activation shall align to NBBF without modifying NBBF ownership.

---

## 15. CDT Relationship

| Manager | CDT Affinity |
|---|---|
| Charter Manager | Structural charter/governance relationship modeling |
| Legislative Manager | Layer and authority relationship metadata for twin readiness |
| Election Manager | Electoral structure relationships when applicable |
| API Manager | Interface representations that expose twin-accessible structures |
| Other managers | Provide metadata sufficient for future CDT compatibility when relevant |

CDT controls remain owned by CDT-Control-Documents.  
Managers shall remain CDT-compatible where structural relationships are engineered.  
No manager requires a completed CDT runtime to operate.

---

## 16. Future UNBKE Relationship

1. UNBKE is a future runtime and knowledge integration layer.  
2. No manager shall hard-depend on UNBKE.  
3. Managers should keep identifiers, metadata, and relationships suitable for future UNBKE indexing.  
4. UNBKE integration, when authorized, shall be additive through Runtime Interface updates and registration records.  
5. Existing managers shall not require rewrite solely because UNBKE becomes available.

---

## 17. Manager Registration Requirements

### 17.1 Registration Purpose

Manager Registration is the additive process by which a new manager enters the ecosystem without modifying existing managers.

### 17.2 Required Registration Data

Every manager registration shall include:

| Field | Description |
|---|---|
| Manager Code | Unique `MGR-XXX` code |
| Manager Name | Official name |
| Domain Statement | Precise domain boundary |
| Status | Proposed / Registered / Structured / Certified / Active / Suspended / Retired |
| Repository or Surface Path | Location of manager assets |
| Primary Control Affinities | AGCL / NBBF / CDT / none / combination |
| Peer Interfaces | Known interface partners |
| Steward | Accountable human steward |
| Governing CWC-CE | Work card authorizing registration |
| Effective Date | Registration effective date |

### 17.3 Additive Registration Rule

1. New managers are added by creating new registration records and new manager surfaces.  
2. Existing manager documents shall not be rewritten as a condition of adding a new manager.  
3. Cross-references in indexes or registries may be updated under approved work.  
4. ARCH-002 itself is updated only when manager architecture rules change, not merely when a new manager is registered.  
5. Initial managers listed in Section 3.1 are pre-declared by this architecture; activation still requires Structured and Certified states.

### 17.4 Registry Location

The Engineering Office shall maintain a Manager Registry entry surface under Office control (index appendix, registry document, or equivalent).  
Until a dedicated registry document exists, IDX updates or an approved registry artifact may carry registration records under CWC-CE authorization.

---

## 18. Manager Certification Requirements

A manager may become Active only after certification confirms:

1. Unique manager code and domain statement exist  
2. Required folders exist  
3. Required manager documents exist  
4. Authority boundaries are explicit  
5. Control affinities do not claim foreign ownership  
6. WF-001 conformance path is defined  
7. Steward is assigned  
8. No hard UNBKE dependency exists  
9. Human Engineer certification approval is recorded  

Certification package contents:

- Registration record  
- Structure checklist  
- Boundary checklist  
- Interface checklist  
- Human Engineer approval  

Failed certification keeps the manager in Registered or Structured state until defects are corrected.

---

## 19. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Engineering Manager Architecture defining manager definition, structure, interfaces, registration, certification, and the initial manager set. |
| 1.1.0 | 2026-08-08 | ECR-002 / CWC-CE-054: managers may consume accepted Engineering Definition outputs without owning or redefining Office LOU authority. |
