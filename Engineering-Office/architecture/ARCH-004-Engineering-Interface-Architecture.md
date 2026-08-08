# ARCH-004 — Engineering Interface Architecture

**Document ID:** ARCH-004  
**Title:** Engineering Interface Architecture  
**Classification:** Architecture Baseline  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Status:** Draft  
**Version:** 1.0.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This document defines the architectural contracts governing communication among the Constitutional Engineering Office, specialized Engineering Managers, AGCL, NBBF, CDT, Legislative Manager, and future repositories under Office authority.

It establishes:

- What an interface is within this ecosystem
- How repositories, managers, documents, and controls communicate
- How interface contracts are versioned, validated, and registered
- How breaking changes are controlled
- How present interfaces remain API-ready and UNBKE-compatible without requiring runtime dependency

ARCH-004 specializes ARCH-001 for interfaces. It does not replace ARCH-001.  
It complements ARCH-002 manager interface types, ARCH-003 ownership boundaries, POL-001, and WF-001 without redefining them.

---

## 2. Scope

### 2.1 In Scope

This architecture applies to:

1. Interfaces among Engineering-Office and all repositories under Office authority  
2. Manager interfaces defined and extended under ARCH-002  
3. Document-to-document and document-to-repository interface contracts  
4. Control-document reference interfaces for AGCL, NBBF, and CDT  
5. Cross-repository contracts for Legislative Manager and future managers  
6. Interface versioning, compatibility, registration, validation, and audit  
7. API readiness for future machine-consumable surfaces  
8. Future UNBKE integration interfaces  

### 2.2 Out of Scope

This architecture does not:

1. Implement concrete APIs, schemas, or transport protocols  
2. Modify AGCL, NBBF, or CDT control content  
3. Redefine manager domains (ARCH-002) or ownership (ARCH-003)  
4. Replace WF-001 operating sequence or STD-014 change control  
5. Require UNBKE or any specific runtime, vendor, or API stack for current operation  

### 2.3 Authority Position

```
ARCH-001
    ↓
ARCH-004 (interface architecture)
    ↓
ARCH-002 / ARCH-003 / POL-001 / Standards / Workflows
    ↓
Registered Interfaces
    ↓
Manager / Repository / Document / Control / Publication / Runtime surfaces
```

Interface contracts are subordinate to ARCH-001.  
Ownership remains governed by ARCH-003.  
Manager boundaries remain governed by ARCH-002.  
Breaking interface changes require Engineering Change control under STD-014 when applicable.

---

## 3. Interface Principles

The following principles are binding:

1. **Repositories communicate through defined interfaces.** Ad hoc cross-writing is not an interface.  
2. **References do not imply ownership.** Consuming or citing a foreign artifact does not transfer ownership.  
3. **Interface contracts are versioned.** Every registered interface has an explicit version.  
4. **Breaking interface changes require Engineering Change control.** Compatible additions may proceed under approved work; incompatible changes require ECR when STD-014 applies.  
5. **AI shall not invent undocumented interfaces.** AI may prepare interface drafts only under authorized work; undocumented channels are defects.  
6. **Interface compatibility shall be verifiable.** Compatibility claims require stated rules and validation evidence.  
7. **Future APIs shall align with interface definitions.** Machine APIs are projections of registered interfaces, not independent authority.

### 3.1 Interface Definition

An **Engineering Interface** is a versioned contract describing:

| Element | Meaning |
|---|---|
| Parties | Provider and consumer roles |
| Direction | One-way, request/response, or handoff |
| Payload / Artifact Types | What may cross the boundary |
| Authority Constraints | What the interface may and may not authorize |
| Ownership Effect | Always none by default under ARCH-003 |
| Version | Semantic interface version |
| Compatibility Class | Compatible, deprecated, or breaking relative to prior versions |

### 3.2 Non-Interface Rule

Informal chat, undocumented path writes, implied “shared folders,” and AI convenience coupling are not interfaces.  
If communication is required and no registered interface exists, participants shall stop, report the gap, and seek Human Engineer authorization to define one.

---

## 4. Repository Interfaces

### 4.1 Repository Interface Map

```
Engineering-Office
        │
        ├── Office→Manager Interface ────────► Specialized Managers
        ├── Office→Control Process Interface ► AGCL / NBBF / CDT
        ├── Office→Publication Interface ────► Public surfaces
        └── Office→Runtime Interface (future)► UNBKE

AGCL / NBBF / CDT
        │
        ├── Control→Manager Reference Interface ► Managers (consume only)
        └── Control Peer Separation ────────────► No cross-ownership

Managers
        │
        ├── Manager→Office Interface
        ├── Manager→Control Interface
        ├── Manager→Peer Interface
        ├── Manager→Publication Interface
        └── Manager→Runtime Interface (future)
```

### 4.2 Repository Interface Rules

1. Each repository exposes only registered provider interfaces.  
2. Consumers reference provider artifacts; they do not silently modify provider-controlled paths.  
3. Cross-repository modification requires explicit CWC-CE scope and steward awareness under ARCH-003.  
4. Engineering Office process authority does not convert into domain-control ownership of AGCL, NBBF, or CDT.  
5. Public repositories are consumers of approved publication packages; they do not redefine source interfaces.

### 4.3 Default Repository Interface Roles

| Repository / Surface | Primary Provider Role | Primary Consumer Role |
|---|---|---|
| Engineering-Office | Architecture, standards, workflows, templates, indexes | Manager outputs for conformance review |
| AGCL-Control-Documents | AGCL controls | None required for peer controls |
| NBBF-Control-Documents | NBBF controls | None required for peer controls |
| CDT-Control-Documents | CDT controls / twin structures | None required for peer controls |
| Legislative-Manager | Legislative domain artifacts | Office + applicable controls |
| Future managers | Domain artifacts within ARCH-002 scope | Office + applicable controls |
| Public surfaces | Published packages | Approved handoffs only |
| UNBKE (future) | Runtime index/query surfaces | Registered Runtime Interfaces |

---

## 5. Manager Interfaces

### 5.1 Canonical Manager Interface Types

Consistent with ARCH-002, every manager shall recognize these interface types:

| Interface Type | Purpose |
|---|---|
| Office Interface | Consume ARCH/POL/STD/WF/TMP/IDX; submit work through WF-001 |
| Control Interface | Reference applicable AGCL/NBBF/CDT controls |
| Peer Interface | Exchange references with other managers without transferring ownership |
| Publication Interface | Hand off approved packages to Publication Manager / public surfaces |
| Runtime Interface (future) | Optional UNBKE integration when declared operational |

### 5.2 Manager Interface Rules

1. Interfaces are reference-based and contract-based, not ownership-based.  
2. Cross-manager work requires explicit scope in the governing CWC-CE.  
3. No manager may silently write into another manager’s controlled paths.  
4. Interface additions for a new manager shall be additive.  
5. Legislative Manager, as the active manager, shall use registered Office, Control, Peer, and Publication interfaces; Runtime remains optional and non-blocking.  
6. Declared managers inherit the same interface types upon activation under ARCH-002.

### 5.3 Peer Interface Discipline

Peer interfaces may exchange:

- Identifiers and references  
- Compatibility metadata  
- Handoff manifests for approved packages  

Peer interfaces shall not:

- Transfer ownership  
- Expand domain scope by implication  
- Create undocumented write channels  

---

## 6. Document Interfaces

### 6.1 Document Interface Rule

Controlled documents interact through declared governing and reference relationships, not through informal supersession.

### 6.2 Document Relationship Types

| Relationship | Meaning |
|---|---|
| Governs | Superior document constrains subordinate artifacts |
| References | Cites foreign or peer authority without ownership transfer |
| Derives From | Produced under authorizing artifact (e.g., CER under CEP) |
| Indexes | Catalogs existence/status without rewriting content |
| Implements | Conforms to architecture/standard/workflow requirements |

### 6.3 Document Interface Rules

1. Metadata fields (Governing Architecture, Governing Policy, Governing Standard, Governing Workflow, Governing CWC-CE/ECR/CEP) are part of the document interface contract.  
2. A reference from Document A to Document B does not make A the owner of B.  
3. Indexes may point to documents; indexes do not become substitute authority for those documents.  
4. Templates define structural interfaces for future documents; populated instances remain separately owned under ARCH-003.  
5. AI shall not invent governing relationships absent in authorized metadata or work scope.

### 6.4 Series Interface Expectations

| Series | Typical Provider Role | Typical Consumer Role |
|---|---|---|
| ARCH | System structure and authority contracts | All Office participants and managers |
| POL / STD / WF | Binding conduct, practice, and sequence | Implementers and managers |
| TMP | Structural patterns | Document authors |
| IDX | Discovery and registration surfaces | Humans and future APIs/UNBKE |
| CWC-CE → ECR → CEP → CER | Work authorization chain | Implementers and auditors |

---

## 7. Control Document Interfaces

### 7.1 Control Interface Rule

Managers and Office artifacts may consume AGCL, NBBF, and CDT through Control Interfaces.  
Controls remain owned by their control repositories.

### 7.2 Control Interface Contracts

| Control System | Interface Purpose | Consumer Constraint |
|---|---|---|
| AGCL | Supply constitutional/structural control authority | Consumers reference; do not fork ownership |
| NBBF | Supply fiscal/node budget control authority | Consumers reference; do not redefine NBBF |
| CDT | Supply twin/relationship structural authority | Consumers remain CDT-compatible where relevant |

### 7.3 Control Interface Rules

1. Control Interfaces are primarily read/reference interfaces for managers.  
2. Proposed changes to control content require work authorized against the owning control repository, not manager-local rewrite.  
3. Logical separation among AGCL, NBBF, CDT, and UNBKE remains mandatory.  
4. Affinity (primary or secondary) does not create ownership.  
5. Absence of a needed control reference is a gap to escalate, not a license to invent controls.

---

## 8. Cross-Repository Contracts

### 8.1 Contract Definition

A **Cross-Repository Contract** is a registered interface between two or more repositories specifying allowed exchanges, directions, and change rules.

### 8.2 Minimum Contract Fields

| Field | Description |
|---|---|
| Contract ID | Unique interface identifier |
| Provider Repository | Source of truth for provided artifacts |
| Consumer Repository | Authorized consumer |
| Interface Type | Office / Control / Peer / Publication / Runtime / Document / Other |
| Allowed Exchanges | References, manifests, packages, metadata, etc. |
| Prohibited Exchanges | Silent writes, ownership claims, undocumented channels |
| Version | Semantic version |
| Compatibility Policy | Rules for compatible vs breaking change |
| Owning Steward (provider) | Accountable steward under ARCH-003 |
| Authorizing Artifact | CWC-CE / ECR / architecture registration basis |
| Status | Proposed / Registered / Active / Deprecated / Retired |

### 8.3 Cross-Repository Rules

1. Every material cross-repository communication path used in production shall map to a registered contract or an approved temporary exception.  
2. Contracts are additive when new repositories or managers enter the ecosystem.  
3. Existing contracts shall not be silently rewritten as a condition of adding a new party.  
4. Publication contracts admit only approved packages.  
5. AI may draft contracts; Human Engineer authorization is required for registration and breaking revisions.

### 8.4 Initial Contract Families

| Contract Family | Parties (illustrative) |
|---|---|
| Office↔Manager | Engineering-Office ↔ Legislative Manager / future managers |
| Manager↔Control | Legislative Manager ↔ AGCL / NBBF / CDT (as applicable) |
| Manager↔Manager | Peer exchanges among registered managers |
| Office↔Control (process) | Engineering process governance without domain ownership transfer |
| Publication | Approved provider → public surface |
| Runtime (future) | Registered surfaces ↔ UNBKE |

---

## 9. Interface Versioning

### 9.1 Versioning Scheme

Interface versions use semantic versioning `MAJOR.MINOR.PATCH`:

| Change Class | Version Impact | Meaning |
|---|---|---|
| MAJOR | Breaking | Incompatible change to parties, required fields, authority effects, or exchange semantics |
| MINOR | Compatible expansion | Additive optional fields, new compatible consumers, non-breaking extensions |
| PATCH | Clarification | Non-semantic clarifications, typo fixes, documentation precision |

### 9.2 Versioning Rules

1. Every registered interface shall declare its current version.  
2. Consumers shall declare the interface version(s) they depend on when material.  
3. Deprecated versions remain readable for audit until expressly retired.  
4. Version identifiers are never reused for different semantics.  
5. Document semantic versions and interface contract versions are related but independently declared when both apply.

### 9.3 Breaking Change Gate

Breaking (MAJOR) interface changes require:

1. Explicit Human Engineer authorization  
2. Engineering Change control under STD-014 when applicable  
3. Compatibility impact statement  
4. Registry update  
5. Consumer notification / migration note for known registered consumers  

---

## 10. Interface Compatibility

### 10.1 Compatibility Classes

| Class | Meaning |
|---|---|
| Compatible | Consumer of prior version can continue without mandatory rewrite |
| Transition | Dual-support period; both versions accepted under stated rules |
| Breaking | Prior consumers must migrate; cannot assume silent compatibility |
| Deprecated | Still valid temporarily; no new dependents |
| Retired | No longer authorized for production use |

### 10.2 Compatibility Rules

1. Compatibility shall be declared, not assumed.  
2. Additive optional fields are the preferred expansion method.  
3. Removing required fields, changing meaning of existing fields, or altering authority effects is breaking.  
4. Reference-only expansion is generally compatible if prior exchanges remain valid.  
5. Ownership effects never appear as a side effect of a “compatible” interface change.

### 10.3 Verifiability Requirement

A compatibility claim is valid only when:

1. Prior and new contract versions are identified  
2. Allowed/prohibited exchange differences are stated  
3. Validation evidence exists or is expressly waived by Human Engineer with recorded reason  

---

## 11. Interface Registration

### 11.1 Registration Purpose

Interface Registration is the additive process by which an interface contract becomes an authorized communication path.

### 11.2 Required Registration Data

| Field | Description |
|---|---|
| Interface / Contract ID | Unique identifier |
| Name | Human-readable name |
| Interface Type | Office / Control / Peer / Publication / Runtime / Document / Other |
| Provider | Repository, manager, or document series providing the surface |
| Consumer(s) | Authorized consumers |
| Version | Current semantic version |
| Status | Proposed / Registered / Active / Deprecated / Retired |
| Compatibility Basis | Relation to prior version if any |
| Ownership Effect | Must state `None` unless an approved exceptional model is expressly authorized |
| Authorizing Artifact | CWC-CE / ECR / architecture basis |
| Effective Date | Registration effective date |
| Steward | Provider-side accountable steward |

### 11.3 Additive Registration Rule

1. New interfaces are added by creating new registration records.  
2. Existing interfaces shall not be rewritten solely to admit a new consumer when an additive consumer entry or new minor version suffices.  
3. ARCH-004 itself is updated only when interface architecture rules change, not merely when a new interface is registered.  
4. Until a dedicated Interface Registry document exists, approved registry artifacts or authorized index appendices may carry registration records under CWC-CE authorization.

### 11.4 AI Restriction

AI shall not invent undocumented interfaces or treat unregistered channels as registered.  
AI may prepare registration packages under authorized work only.

---

## 12. Interface Validation

### 12.1 Validation Purpose

Interface validation confirms that a claimed exchange conforms to a registered contract and version.

### 12.2 Minimum Validation Checks

1. Interface ID exists and status is Active (or expressly authorized Transition/Deprecated use)  
2. Provider and consumer are authorized for the exchange  
3. Exchange type is within Allowed Exchanges  
4. Exchange does not perform Prohibited Exchanges  
5. Version compatibility rules are satisfied  
6. Ownership effect remains none (or approved exceptional model)  
7. Cross-repository writes appear only when CWC-CE scope authorizes them  
8. No AI-invented undocumented channel is used  

### 12.3 Validation Outcomes

| Outcome | Meaning |
|---|---|
| Pass | Exchange conforms to registered interface |
| Partial | Material conformance with recorded gaps; Human Engineer decides continuity |
| Fail | Exchange violates contract; stop and correct |

### 12.4 Validation Authority

AI may perform and report validation checks.  
Human Engineer accepts validation outcomes for production gates when required by workflow.

---

## 13. API Readiness

### 13.1 API Readiness Rule

Future APIs shall align with registered interface definitions.  
An API is a machine-consumable projection of an interface contract, not an independent source of architectural authority.

### 13.2 API Readiness Requirements

Interfaces intended for later API exposure should preserve:

1. Stable identifiers (interface ID, document ID, manager code, repository path)  
2. Explicit version fields  
3. Clear provider/consumer roles  
4. Machine-mappable allowed/prohibited exchange rules  
5. Ownership-neutral semantics  
6. Traceability to authorizing artifacts  

### 13.3 API Boundary Rules

1. API Manager (`MGR-API`), when activated under ARCH-002, engineers API specifications against registered interfaces.  
2. APIs shall not invent repository authority or ownership.  
3. APIs shall not bypass publication or Human Engineer approval gates.  
4. Absence of an implemented API does not invalidate the underlying interface contract.  
5. Current operations shall not hard-depend on API runtime availability.

### 13.4 Readiness States

| State | Meaning |
|---|---|
| Contract-only | Interface registered; no API projection yet |
| Spec-ready | Sufficient stability for API specification work |
| Spec-defined | API specification exists under manager/Office authority |
| Implemented | API projection exists; still subordinate to interface contract |
| Deprecated/Retired | Follows interface compatibility classes |

---

## 14. Future UNBKE Integration Interfaces

### 14.1 UNBKE Interface Posture

1. UNBKE is a future runtime and knowledge integration layer.  
2. No current repository or manager shall hard-depend on UNBKE.  
3. Runtime Interface is optional and additive.  
4. UNBKE integration, when authorized, shall consume registered interface identifiers and versions.

### 14.2 Future Runtime Interface Expectations

When authorized, UNBKE Integration Interfaces should support:

1. Indexing of document IDs, manager codes, repository paths, and interface IDs  
2. Query of interface registry and compatibility metadata  
3. Traceability from runtime views to authorizing artifacts  
4. Preservation of ownership neutrality (references ≠ ownership)  
5. Additive mapping without forcing rewrite of existing contracts  

### 14.3 UNBKE Non-Disruption Rule

UNBKE availability shall not by itself:

1. Create new undocumented interfaces  
2. Transfer ownership  
3. Invalidate Office, Control, Peer, or Publication interfaces  
4. Require immediate API implementation  

Existing interfaces shall remain operable without UNBKE.

---

## 15. Interface Audit Requirements

### 15.1 Audit Purpose

Interface audits verify that production communication paths are registered, versioned, ownership-neutral, and free of AI-invented channels.

### 15.2 Minimum Audit Checks

1. Material cross-repository paths map to registered interfaces or approved exceptions  
2. Interface versions are present and coherent  
3. Breaking changes since last audit have ECR / Human Engineer authorization when required  
4. Compatibility claims have verifiable basis  
5. Control Interfaces do not claim foreign ownership  
6. Manager Peer Interfaces do not create silent write channels  
7. Publication Interfaces admit only approved packages  
8. API projections, if any, align to registered interfaces  
9. No hard UNBKE dependency has been introduced  
10. AI did not invent undocumented interfaces in the audited period  

### 15.3 Audit Outcomes

| Outcome | Meaning |
|---|---|
| Pass | No material interface defects |
| Partial | Defects found; affected paths constrained pending correction |
| Fail | Material interface defects block affected production exchanges until corrected |

AI may prepare interface audit packages.  
Human Engineer closes interface audits.

---

## 16. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Engineering Interface Architecture defining repository, manager, document, and control interfaces; cross-repository contracts; versioning; compatibility; registration; validation; API readiness; UNBKE integration posture; and audit requirements. |
