# Constitutional Engineering

**Document ID:** README-EO-001  
**Title:** Constitutional Engineering Repository Front Door  
**Classification:** Repository Root README  
**Authority:** Constitutional Engineering Office  
**Governing Index:** [IDX-001 — Engineering Office Master Index](Engineering-Office/IDX-001-Engineering-Office-Master-Index.md)  
**Status:** Active  
**Version:** 1.1.0  
**Effective Date:** 2026-08-08  
**Governing ECR:** ECR-002 — Engineering Definition / LOU Controlled Adoption  

This repository is the **engineering-control environment** for Constitutional Engineering.  
It holds the Constitutional Engineering Office’s architecture, policy, standards, workflows, audits, certifications, and operating prompts.

It is **not** the legislative production repository.

---

## Mission

Constitutional Engineering designs and maintains the engineering systems required to produce and preserve **constitutionally constrained, rules-based governance artifacts**.

The work is about structure, authority boundaries, traceability, and integrity—so that approved control documents remain the source of governing truth, and so that government engineering projects can proceed under explicit human authority rather than ad hoc invention.

Plainly:

- Build the method before drafting the instrument.  
- Keep authority explicit.  
- Keep every material action traceable.  
- Do not invent law, policy, or missing authority.

---

## What This Repository Is

This repository governs **how** Constitutional Engineering work is authorized, structured, reviewed, evidenced, and released.

Inside [Engineering-Office/](Engineering-Office/) you will find the controlling surfaces for:

- architecture  
- policy  
- standards  
- workflows  
- templates  
- audits / change records  
- certifications  
- agent operating prompts  

If you need the authoritative catalog of Office documents, start here:

**[IDX-001 — Engineering Office Master Index](Engineering-Office/IDX-001-Engineering-Office-Master-Index.md)**

IDX-001 is the authoritative navigation and catalog surface for the Engineering Office.

---

## What This Repository Is Not

Documents in this repository:

- do **not** themselves constitute enacted law  
- do **not** automatically authorize legislative action  
- do **not** replace AGCL, NBBF, or CDT control ownership  
- do **not** make GitHub presence equivalent to public policy publication  
- do **not** grant AI agents human approval authority  

Legislative packages, jurisdiction work, and production drafting belong in the specialized manager environment (Legislative Manager), under Office governance—not as a substitute for this repository’s control role.

---

## Constitutional Engineering Office

The **Constitutional Engineering Office** provides:

1. Architectural authority over the Constitutional Engineering platform  
2. Engineering standards that bind repositories under its authority  
3. Traceable workflows that separate specification, implementation, and reporting  
4. Coordination among control-document repositories and specialized managers  
5. Preparation for future runtime integration without requiring that runtime for present operation  

The Office does **not** invent policy.  
It engineers structure, consistency, authority boundaries, and document integrity.

Primary governance policy:

- [POL-001 — Engineering Office Governance Policy](Engineering-Office/policies/POL-001-Engineering-Office-Governance.md)

---

## Human Engineer Authority

**Human authority is supreme.**

AI agents (including Cursor agents) may prepare, recommend, and implement only within authorized scope. They:

- assist; they do not govern  
- do not approve their own work  
- do not invent policy or controls  
- do not own engineering artifacts  
- must stop and escalate when authority is missing or conflicting  

Where required by policy and workflow, **Human Engineer decisions** control:

- work authorization  
- acceptance of results  
- commits, tags, pushes, and publication  
- exceptions and release certification  

See [POL-001](Engineering-Office/policies/POL-001-Engineering-Office-Governance.md).

---

## Engineering Architecture

| Document | Role |
|---|---|
| [ARCH-001](Engineering-Office/architecture/ARCH-001-Constitutional-Engineering-Architecture.md) | System architecture baseline: Office purpose, repository hierarchy, authority hierarchy |
| [ARCH-002](Engineering-Office/architecture/ARCH-002-Engineering-Manager-Architecture.md) | Specialized manager architecture: domains, structure, registration, certification |
| [ARCH-003](Engineering-Office/architecture/ARCH-003-Engineering-Ownership-Architecture.md) | Ownership and stewardship: repositories, documents, AI non-ownership |
| [ARCH-004](Engineering-Office/architecture/ARCH-004-Engineering-Interface-Architecture.md) | Interface contracts: how repositories and managers communicate without transferring ownership |

Architecture directory:

- [Engineering-Office/architecture/](Engineering-Office/architecture/)

---

## Engineering Workflow

Controlled engineering work proceeds under:

- [STD-001 — Engineering Workflow Standard](Engineering-Office/standards/STD-001-Engineering-Workflow.md)  
- [WF-001 — Engineering Office Operating Workflow](Engineering-Office/workflows/WF-001-Engineering-Office-Operating-Workflow.md)  
- [WF-002 — Engineering Release Workflow](Engineering-Office/workflows/WF-002-Engineering-Release-Workflow.md)  

Typical progression:

```text
ENGINEERING DEFINITION
Human Engineering Intent
    → Research / Source Collection (informative)
    → LOU (Letter of Understanding)
    → Human Engineer LOU Acceptance
    → Requirements / Scope (SPEC preferred)
    → Human Engineer Requirements Approval / CWC-Readiness
        ↓
CONTROLLED EXECUTION
CWC-CE (work authorization)
    → Human Review / Approval
    → ECR when required (controlled change)
    → CEP (implementation instructions)
    → Implementation
    → CER (evidence / report)
    → Human Acceptance
    → Git Commit / Tag / Push (only when authorized)
    → Baseline certification / publication (only when authorized)
```

LOU acceptance and Requirements/SPEC acceptance do **not** authorize implementation.  
Controlled Execution requires an approved CWC-CE.

Definition surface:

- [Engineering-Office/definition/](Engineering-Office/definition/)  
- [TMP-002 — Letter of Understanding Template](Engineering-Office/templates/TMP-002-Letter-of-Understanding-Template.md)

Release gates are explicit. Silence is not approval.

---

## Engineering Standards

Standards bind engineering practice across repositories under Office authority.

### Active / operative standards commonly referenced

| ID | Document |
|---|---|
| STD-001 | [Engineering Workflow](Engineering-Office/standards/STD-001-Engineering-Workflow.md) |
| STD-008 | [Legislative Lifecycle](Engineering-Office/standards/STD-008-Legislative-Lifecycle.md) |
| STD-014 | [Engineering Change Management](Engineering-Office/standards/STD-014-Engineering-Change-Management.md) |
| STD-015 | [Constitutional Engineering Reports](Engineering-Office/standards/STD-015-Constitutional-Engineering-Reports.md) |

### Official standards sequence (including Reserved placeholders)

| ID | Document |
|---|---|
| STD-002 | [Git Operations](Engineering-Office/standards/STD-002-Git-Operations.md) |
| STD-003 | [Cursor Operations](Engineering-Office/standards/STD-003-Cursor-Operations.md) |
| STD-004 | [Engineering Reviews](Engineering-Office/standards/STD-004-Engineering-Reviews.md) |
| STD-005 | [Document Numbering](Engineering-Office/standards/STD-005-Document-Numbering.md) |
| STD-006 | [Repository Management](Engineering-Office/standards/STD-006-Repository-Management.md) |
| STD-007 | [Legislative Authoring](Engineering-Office/standards/STD-007-Legislative-Authoring.md) |
| STD-009 | [Charter Authoring](Engineering-Office/standards/STD-009-Charter-Authoring.md) |
| STD-010 | [Budget Authoring](Engineering-Office/standards/STD-010-Budget-Authoring.md) |
| STD-011 | [Public Documentation](Engineering-Office/standards/STD-011-Public-Documentation.md) |
| STD-012 | [Template Standards](Engineering-Office/standards/STD-012-Template-Standards.md) |
| STD-013 | [Audit Requirements](Engineering-Office/standards/STD-013-Audit-Requirements.md) |

Standards directory:

- [Engineering-Office/standards/](Engineering-Office/standards/)

Reserved standards hold allocated identifiers in the official sequence; they are not a license to invent missing normative rules.

---

## Engineering Office Structure

Committed Engineering Office surfaces represented in this repository:

| Path | Purpose |
|---|---|
| [Engineering-Office/architecture/](Engineering-Office/architecture/) | Architecture baselines (ARCH series) |
| [Engineering-Office/audits/](Engineering-Office/audits/) | CER / ECR evidence and change records |
| [Engineering-Office/certifications/](Engineering-Office/certifications/) | Office baseline and readiness certifications |
| [Engineering-Office/definition/](Engineering-Office/definition/) | LOU instances (Engineering Definition) |
| [Engineering-Office/policies/](Engineering-Office/policies/) | Governance policy |
| [Engineering-Office/prompts/](Engineering-Office/prompts/) | Operating prompts for Office / manager roles |
| [Engineering-Office/standards/](Engineering-Office/standards/) | Engineering standards (STD series) |
| [Engineering-Office/templates/](Engineering-Office/templates/) | Controlled templates (including [TMP-001](Engineering-Office/templates/TMP-001-Master-Document-Template.md), [TMP-002](Engineering-Office/templates/TMP-002-Letter-of-Understanding-Template.md)) |
| [Engineering-Office/workflows/](Engineering-Office/workflows/) | Operating and release workflows |

Master catalog:

- [Engineering-Office/IDX-001-Engineering-Office-Master-Index.md](Engineering-Office/IDX-001-Engineering-Office-Master-Index.md)

**Note:** An `agents/` directory is **not** present in the committed Git tree of this repository as of this README. Do not assume GitHub navigation to `agents/` is valid until tracked content exists there.

---

## Master Index

### Start here for authoritative navigation

**[IDX-001 — Engineering Office Master Index](Engineering-Office/IDX-001-Engineering-Office-Master-Index.md)**

IDX-001 catalogs architecture, policy, standards, workflows, operational artifact conventions, repository relationships, and the Office baseline listing.  
It is a catalog. It does not outrank architecture, policy, or standards.

---

## Audits and Evidence

Engineering actions are recorded, not silently overwritten.

| Type | Purpose |
|---|---|
| **CER** | Constitutional Engineering Report — implementation/audit evidence under STD-015 |
| **ECR** | Engineering Change Request / change record under STD-014 |

Tracked evidence currently in this repository includes:

- [CER-001 — Pre-Push Engineering Audit](Engineering-Office/audits/CER-001-PrePush-Engineering-Audit.md)  
- [CER-002 — Release Readiness Remediation](Engineering-Office/audits/CER-002-Release-Readiness-Remediation.md)  
- [CER-003 — Git Repository Initialization](Engineering-Office/audits/CER-003-Git-Repository-Initialization.md)  
- [CER-004 — GitHub Remote Establishment](Engineering-Office/audits/CER-004-GitHub-Remote-Establishment.md)  
- [CER-005 — GitHub Remote Completion](Engineering-Office/audits/CER-005-GitHub-Remote-Completion.md)  
- [CER-006 — Baseline 1.0 Staging Verification](Engineering-Office/audits/CER-006-Baseline-1.0-Staging-Verification.md)  
- [ECR-001 — Standard Numbering Resolution](Engineering-Office/audits/ECR-001-Standard-Numbering-Resolution.md)  

Audits directory:

- [Engineering-Office/audits/](Engineering-Office/audits/)

---

## Certifications

CERT-EO artifacts record Office-level readiness and baseline evaluation. They are evidence packages for Human Engineer decision—not self-executing releases.

| Document | What it evaluates |
|---|---|
| [CERT-EO-001 — Engineering Office Baseline 1.0](Engineering-Office/certifications/CERT-EO-001-Engineering-Office-Baseline-1.0.md) | Whether Baseline 1.0 is Ready / Ready with Conditions / Not Ready for official certification |
| [CERT-EO-002 — Operational Readiness](Engineering-Office/certifications/CERT-EO-002-Operational-Readiness.md) | Whether the Office may operate as the governing platform for Government Engineering, and under what class |

Certifications directory:

- [Engineering-Office/certifications/](Engineering-Office/certifications/)

---

## AI Governance

Cursor AI agents operate under delegated, bounded authority.

They may:

- prepare drafts and packages  
- implement approved scope  
- report verification truthfully  

They shall not:

- invent authority, policy, or controls  
- approve their own work  
- expand scope as “helpful” unauthorized change  
- claim ownership of engineering artifacts  
- bypass Human Engineer gates  

Office prompt surfaces:

- [Constitutional Engineer](Engineering-Office/prompts/Constitutional-Engineer.md)  
- [Git Manager](Engineering-Office/prompts/Git-Manager.md)  
- [Legislative Manager redirect](Engineering-Office/prompts/Legislative_Manager.md) (points to the canonical Legislative Manager operating manual in the Legislative-Manager repository)

---

## Relationship to Legislative Manager

| Repository | Responsibility |
|---|---|
| **Constitutional-Engineering** (this repo) | Governs engineering method, authority, standards, workflow, review, evidence, and release controls |
| **Legislative-Manager** (separate repo) | Production environment where legislative engineering packages and jurisdiction-specific work are organized |

Do not blur these roles.

- This repository does **not** become a bill factory by hosting Office controls.  
- Legislative-Manager does **not** redefine Office architecture or policy by producing packages.  
- Managers consume Office governance; they do not supersede it.

---

## Relationship to AGCL / NBBF / CDT / UNBKE

As established by Office architecture and index:

| System | Role (as governed here) |
|---|---|
| **AGCL** | Control-document system for AGCL controls; referenced by managers; ownership remains with AGCL control repository |
| **NBBF** | Control-document system for node-based budget / fiscal controls; referenced when applicable; ownership remains with NBBF control repository |
| **CDT** | Control-document system for Constitutional Digital Twin structural representation; twin readiness is an engineering objective; ownership remains with CDT control repository |
| **UNBKE** | Future runtime / knowledge integration layer; **not required** for current Office operation |

References do not transfer ownership.  
This README does not invent architectural ownership beyond what Office documents already establish.

---

## Repository Status

Accurate posture as of this README (do not overclaim):

1. This repository exists as a Git repository with a GitHub remote and committed Engineering Office content.  
2. [CERT-EO-001](Engineering-Office/certifications/CERT-EO-001-Engineering-Office-Baseline-1.0.md) records Baseline 1.0 evaluation with recommendation **Not Ready**, status **Pending Human Engineer Acceptance**.  
3. [CERT-EO-002](Engineering-Office/certifications/CERT-EO-002-Operational-Readiness.md) records recommendation **Operational with Restrictions**, status **Pending Human Engineer Acceptance**.  
4. Some architecture/workflow documents remain Draft pending Human Engineer acceptance (including ARCH-003, ARCH-004, and WF-002 as cataloged).  
5. Presence on GitHub is **not** by itself a claim that Baseline 1.0 is certified, that all Draft documents are accepted, or that publication/enactment has occurred.

For catalog status details, use [IDX-001](Engineering-Office/IDX-001-Engineering-Office-Master-Index.md).

---

## How to Navigate

Recommended sequence for an authorized engineer new to this repository:

1. Read **this README**  
2. Open **[IDX-001](Engineering-Office/IDX-001-Engineering-Office-Master-Index.md)**  
3. Review **[POL-001](Engineering-Office/policies/POL-001-Engineering-Office-Governance.md)**  
4. Review architecture: [ARCH-001](Engineering-Office/architecture/ARCH-001-Constitutional-Engineering-Architecture.md) → [ARCH-002](Engineering-Office/architecture/ARCH-002-Engineering-Manager-Architecture.md) → [ARCH-003](Engineering-Office/architecture/ARCH-003-Engineering-Ownership-Architecture.md) → [ARCH-004](Engineering-Office/architecture/ARCH-004-Engineering-Interface-Architecture.md)  
5. Review applicable standards and workflows ([STD-001](Engineering-Office/standards/STD-001-Engineering-Workflow.md), [WF-001](Engineering-Office/workflows/WF-001-Engineering-Office-Operating-Workflow.md), [WF-002](Engineering-Office/workflows/WF-002-Engineering-Release-Workflow.md), and others as needed)  
6. Review relevant CER/CERT evidence under [audits/](Engineering-Office/audits/) and [certifications/](Engineering-Office/certifications/)  
7. Enter **Legislative-Manager** only when performing authorized legislative engineering under Office governance  

---

## Publication Boundary

GitHub repository presence:

- does **not** constitute public policy publication by itself  
- does **not** constitute legal enactment  
- does **not** constitute legislative authorization  

Publication, release certification, and project package publication require explicit Human Engineer authorization under applicable workflows and standards.

---

## Disclaimer

This repository contains engineering-control documentation for Constitutional Engineering.  
It is not legal advice, not enacted law, and not a substitute for constitutional, statutory, or control-document authority.

AI-assisted materials remain subject to Human Engineer review and acceptance where required.  
When uncertain about authority, stop and escalate rather than invent.

---

## Controlled versus Informational

| Class | Examples in this repo | Force |
|---|---|---|
| **Controlled governing documents** | ARCH, POL, STD, WF, IDX, TMP, CER, ECR, CERT (as issued) | Binding within Office authority according to their status and acceptance |
| **Operating prompts** | `Engineering-Office/prompts/` | Binding operating instructions for agents within superior ARCH/POL/STD/WF constraints |
| **Root informational notes** | This README; other root notes as present | Orientation and navigation; do not outrank controlled governing documents |

If this README conflicts with a controlled governing document, the controlled document prevails.

---

## Version History

| Version | Date | Summary |
|---|---|---|
| 0.0.0 | 2026-08-08 | Reserved workspace-root README stub (CER-001 remediation). |
| 1.0.0 | 2026-08-08 | Replace stub with GitHub repository front door under CWC-CE-048. |
| 1.1.0 | 2026-08-08 | ECR-002 / CWC-CE-054: dual-phase Engineering Definition / Controlled Execution front-door workflow; definition/ navigation. |
