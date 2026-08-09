# WF-001 — Engineering Office Operating Workflow

**Document ID:** WF-001  
**Title:** Engineering Office Operating Workflow  
**Classification:** Engineering Workflow  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Related Standards:** STD-001, STD-014, STD-015  
**Governing ECR:** ECR-002 — Engineering Definition / LOU Controlled Adoption  
**Governing Remediation:** CWC-CE-056 / CER-021 — Audit Finding Remediation (F-03)  
**Status:** Active  
**Version:** 1.2.0  
**Effective Date:** 2026-08-09  

---

## 1. Purpose

This workflow defines the authoritative end-to-end operational process used by the Constitutional Engineering Office for all engineering work.

It integrates Engineering Definition, human authorization, controlled change management, AI implementation, verification, Git integration, publication, and baseline updates into one technology-independent operating sequence.

---

## 2. Scope

### 2.1 In Scope

This workflow applies to all engineering activities performed under Constitutional Engineering Office authority, including:

1. Single-repository work  
2. Multi-repository work  
3. Architecture, standards, policy, workflow, template, and manager engineering  
4. Authorized work in control-document repositories and specialized manager repositories  
5. Engineering Definition artifacts (LOU, Research Annex, SPEC/Requirements)  

### 2.2 Out of Scope

This workflow does not:

1. Redefine architecture, standards, or policy content  
2. Replace domain control authority of AGCL, NBBF, or CDT  
3. Require UNBKE or any specific runtime, vendor, or AI product  
4. Authorize bypass of Human Engineer approval  

### 2.3 Authority Position

This workflow is subordinate to ARCH-001 and POL-001.  
It operationalizes STD-001, STD-014, and STD-015.  
No CEP, CER, or AI action may contradict this workflow.

---

## 3. Workflow Principles

1. **Engineering Definition precedes Controlled Execution** for material work subject to Definition under STD-001.  
2. **Controlled Execution begins with an approved CWC-CE.**  
3. Exploratory research that does **not** modify governed repository artifacts may precede a CWC.  
4. Durable controlled Engineering Definition artifacts written into the repository are governed engineering work and require approved CWC authorization (except express Human Engineer exception under POL-001).  
5. Human authority is supreme at all approval gates.  
6. AI assists execution; AI does not govern.  
7. Research is informative, not authoritative. AI research does not create engineering authority.  
8. LOU acceptance does **not** authorize implementation.  
9. Requirements/SPEC acceptance does **not** authorize implementation.  
10. ECRs are required only when controlled changes are required by STD-014.  
11. Every completed CEP produces a CER unless an approved exception exists.  
12. Human approval gates are explicit and may not be bypassed by AI. Silence is not approval.  
13. Verification must be truthful; unperformed verification shall not be reported as complete.  
14. The workflow supports single-repository and multi-repository engineering.  
15. The workflow does not require UNBKE.  
16. The workflow is technology independent.  
17. Material Controlled Execution actions remain traceable through LOU → SPEC (when applicable) → CWC-CE → ECR (when required) → CEP → CER → Git.  
18. Public trust requires engineering integrity at every stage.  
19. Historical work authorized before LOU adoption remains valid without retroactive LOU requirements.  

---

## 4. Engineering Lifecycle

The Office engineering lifecycle proceeds through the following stages:

```text
ENGINEERING DEFINITION
Human Engineering Intent
      ↓
Research / Source Collection (informative; provenance recorded)
      ↓
LOU Created / Updated
      ↓
Human Engineer LOU Acceptance (HG-D1)
      ↓
Requirements / Scope Definition (SPEC or approved equivalent)
      ↓
Human Engineer Requirements Approval / CWC-Readiness (HG-D2)
      ↓
CONTROLLED EXECUTION
CWC-CE Created
      ↓
Human Review / Approval (HG-1)
      ↓
ECR (when required) (HG-2)
      ↓
CEP Generated
      ↓
Cursor Implementation
      ↓
CER Generated
      ↓
Engineering Review
      ↓
Human Acceptance (HG-3)
      ↓
Git Commit (HG-4)
      ↓
Git Push (HG-5)
      ↓
Publication (HG-6; when authorized)
      ↓
Baseline Updated (when applicable) (HG-8)
```

### 4.1 Lifecycle Stage Definitions

| Stage | Meaning |
|---|---|
| Human Engineering Intent | Human Engineer states the engineering problem/intent under consideration |
| Research / Source Collection | Informative source gathering with provenance; non-authoritative |
| LOU Created / Updated | Letter of Understanding drafted under TMP-002 in `Engineering-Office/definition/` |
| HG-D1 LOU Acceptance | Human Engineer accepts, conditionally accepts, returns, or rejects the LOU |
| Requirements / Scope Definition | SPEC (preferred) or approved equivalent defines what must be accomplished |
| HG-D2 Requirements Acceptance / CWC-Readiness | Human Engineer accepts Requirements/SPEC readiness for Controlled Execution |
| CWC-CE Created | Discrete Controlled Execution work is specified and proposed |
| Human Review / Approval | Human Engineer reviews and approves/rejects/returns the CWC-CE |
| ECR (when required) | Controlled change is authorized under STD-014 |
| CEP Generated | Approved work is translated into executable Cursor instructions |
| Cursor Implementation | Authorized AI implementation occurs within approved scope |
| CER Generated | Implementation and verification are reported under STD-015 |
| Engineering Review | Results are reviewed for conformance and completeness |
| Human Acceptance | Human Engineer accepts, conditionally accepts, or rejects results |
| Git Commit | Approved changes are committed to repository history |
| Git Push | Approved commits are pushed to the designated remote |
| Publication | Approved artifacts are released through designated channels |
| Baseline Updated | Engineering baseline is amended when the work changes controlled configuration |

### 4.2 Definition vs Execution Boundary

1. LOU acceptance and Requirements/SPEC acceptance establish understanding and requirements only.  
2. Neither acceptance authorizes Cursor implementation, Git advancement, or publication.  
3. Implementation-class Controlled Execution requires approved CWC-CE and all applicable downstream gates.  

---

## 5. Roles and Responsibilities

| Role | Workflow Responsibility |
|---|---|
| Human Engineer | Accepts LOU and Requirements/SPEC; approves CWC-CE, ECR, CER acceptance, Git actions, publication, exceptions, and baseline updates |
| Constitutional Engineer | Prepares LOU / SPEC / CWC-CE / ECR / CEP routing; documents research as informative; maintains cross-repository integrity; supports engineering review; does not accept LOU/SPEC |
| Specialized Manager | Consumes accepted Engineering Definition outputs within domain; executes domain-scoped work within approved CEP boundaries; does not own Office LOU authority |
| Cursor AI | Implements approved CEP; drafts CER; never bypasses approval gates; never treats LOU/SPEC as implementation authority |
| Repository Steward | Ensures repository integrity during commit, push, and publication stages |
| Public Publication Steward | Confirms only approved artifacts enter public channels |

AI roles may prepare artifacts and perform authorized implementation.  
AI roles may not grant Human Engineer approvals.

---

## 6. Workflow Inputs

| Input | Required When |
|---|---|
| Human Engineering Intent | Always for Engineering Definition |
| Research Record / Evidence Annex | When research informs an LOU |
| Draft or accepted LOU | When Engineering Definition applies to material work |
| Accepted SPEC / Requirements (or HE waiver) | Before Definition-dependent implementation-class CWC |
| Draft or approved CWC-CE | Always before Controlled Execution implementation |
| Applicable architecture / standards / policy references | Always |
| ECR | When STD-014 requires controlled change authorization |
| CEP | Before Cursor implementation |
| Repository access and path scope | Before implementation |
| Prior baseline identifiers | When baseline-affecting work is proposed |
| Exception / waiver record | When an approved exception or HE waiver alters normal sequence |

---

## 7. Workflow Outputs

| Output | Produced At |
|---|---|
| Accepted LOU (when Definition applies) | After HG-D1 |
| Accepted SPEC / Requirements (when Definition applies) | After HG-D2 |
| Approved CWC-CE | After Human Review (HG-1) |
| Approved ECR (when required) | After ECR approval (HG-2) |
| Executable CEP | After CEP generation / approval under governing process |
| Implemented repository changes | After Cursor Implementation |
| CER | After implementation reporting |
| Human Acceptance record | After Human Acceptance (HG-3) |
| Git commit identifier(s) | After Git Commit |
| Push / remote confirmation | After Git Push |
| Publication record | After Publication |
| Updated baseline declaration (when applicable) | After Baseline Updated |

---

## 8. Standard Operating Sequence

### 8.0 Engineering Definition (when applicable)

#### 8.0.1 Human Engineering Intent

The Human Engineer states engineering intent for the subject under consideration.

#### 8.0.2 Research / Source Collection

Research may be collected by Human Engineer, Constitutional Engineer, or AI assistants.  
Research remains informative, not authoritative. AI research does not create engineering authority.  
Classification of evidence does **not** confer engineering authority.

**Normative taxonomy and annex field requirements** are controlled by:

1. **STD-001 §4.5** — Research Record / Evidence Annex rules and initial source-class taxonomy  
2. **TMP-002** — operational LOU Research Record / Evidence Annex structure  

WF-001 does not duplicate the taxonomy table. Operators shall use the STD-001 / TMP-002 controlling surfaces to avoid drift.

Accepted source classes (informative labels only; listed for operator awareness; normative definitions remain in STD-001):

`PRIMARY-LEGAL` | `GOV-DATA` | `SECONDARY-ANALYSIS` | `TESTIMONY` | `HISTORICAL` | `SCRIPTURE` | `AI-SYNTHESIS` | `CONTROL-DOC`

Exploratory research outside controlled repository writing may precede CWC.  
Provenance for research recorded into durable LOU artifacts follows STD-001 / TMP-002.

#### 8.0.3 LOU Created / Updated

An LOU is prepared using TMP-002 and stored under `Engineering-Office/definition/` with identifier `LOU-NNN`.  
Creating or modifying durable LOU files in the repository requires approved CWC authorization unless an express Human Engineer exception applies.

#### 8.0.4 HG-D1 — LOU Acceptance

The Human Engineer records `Accepted` / `Accepted with Conditions` / `Returned` / `Rejected`.  
Silence is not acceptance.  
LOU acceptance does **not** authorize implementation.

#### 8.0.5 Requirements / Scope Definition

Structured Requirements preferentially use SPEC (`SPEC-NNN`) or an approved equivalent.  
No REQ series is used under this workflow.

#### 8.0.6 HG-D2 — Requirements Acceptance / CWC-Readiness

The Human Engineer accepts Requirements/SPEC readiness for Controlled Execution, accepts with conditions, returns, or rejects.  
Requirements/SPEC acceptance does **not** authorize implementation.

#### 8.0.7 Waivers

Trivial/corrective Controlled Execution may waive LOU/SPEC only by explicit Human Engineer authorization recorded in the CWC.  
AI may not waive.

### 8.1 CWC-CE Created

A CWC-CE is authored defining objective, scope, deliverables, acceptance criteria, constraints, and repositories in scope.  
When Engineering Definition applies, the CWC-CE cites accepted LOU and SPEC (or records HE waiver).  
Every Controlled Execution activity that will modify governed artifacts shall have a CWC-CE.

### 8.2 Human Review

The Human Engineer reviews the CWC-CE and issues one of:

- Approve  
- Return for revision  
- Reject  

Implementation is forbidden until the CWC-CE is approved.

### 8.3 ECR (When Required)

If the approved work constitutes a controlled change under STD-014, an ECR is prepared and approved before CEP execution of that controlled change.  
If no controlled change is required, this stage is recorded as `Not required`.

### 8.4 CEP Generated

An approved CEP is generated from the approved CWC-CE and, when applicable, approved ECR.  
The CEP shall reference its governing CWC-CE and ECR when applicable.  
CEP shall not treat LOU or SPEC acceptance as sufficient authorization.

### 8.5 Cursor Implementation

Cursor AI implements only the approved CEP scope.  
Single-repository and multi-repository work are both valid when authorized by the CWC-CE / CEP.  
Unauthorized repositories and paths shall not be modified.

### 8.6 CER Generated

A CER is produced for the completed CEP unless an approved exception expressly waives CER generation.  
Failed or partial implementations still produce a CER.

### 8.7 Engineering Review

Engineering review checks scope conformance, verification integrity, deviations, repository coverage, and readiness for Human Acceptance.

### 8.8 Human Acceptance

The Human Engineer records acceptance, acceptance with follow-up, or rejection on the CER path.  
Closed CER status requires Human Acceptance per STD-015.

### 8.9 Git Commit

Approved accepted changes are committed under applicable Git standards and Human Engineer approval.  
Commit identifiers are recorded in the CER when available.

### 8.10 Git Push

Approved commits are pushed to the designated remote under Human Engineer approval.  
Push status is recorded truthfully.

### 8.11 Publication

If the work includes publication, only accepted and approved artifacts are published through designated channels.  
Public review materials are not publication unless separately approved.

### 8.12 Baseline Updated (When Applicable)

If the work changes an Engineering Baseline (for example architecture baseline or standards sequence), the baseline is updated through the governing ECR / approval record and cited from the CER / ECR package.  
If no baseline change occurred, this stage is `Not applicable`.

---

## 9. Decision Points

| Decision Point | Question | Outcomes |
|---|---|---|
| DP-D1 | Does Engineering Definition apply? | Apply Definition / HE waiver for trivial-corrective / Not applicable (historical) |
| DP-D2 | Is LOU accepted (HG-D1)? | Accept / Accept with Conditions / Return / Reject |
| DP-D3 | Are Requirements/SPEC accepted (HG-D2)? | Accept / Accept with Conditions / Return / Reject / Waived by HE |
| DP-1 | Is a CWC-CE required for Controlled Execution / durable repo writes? | Yes for governed engineering work; if no governed work, stop |
| DP-2 | Is the CWC-CE approved? | Approve / Return / Reject |
| DP-3 | Is an ECR required under STD-014? | Create ECR / Not required |
| DP-4 | Is the ECR approved (when required)? | Approve / Return / Reject |
| DP-5 | Is the CEP ready for execution? | Execute / Revise / Hold |
| DP-6 | Did implementation complete, partially complete, or fail? | Complete / Partial / Fail → still CER |
| DP-7 | Did verification pass? | Pass / Fail / Partial / Not performed |
| DP-8 | Does Human Engineer accept results? | Accept / Accept with Follow-up / Reject |
| DP-9 | Is Git commit authorized? | Commit / Hold |
| DP-10 | Is Git push authorized? | Push / Hold |
| DP-11 | Is publication required and authorized? | Publish / Not applicable / Hold |
| DP-12 | Is baseline update required? | Update baseline / Not applicable |

AI may recommend decisions. AI may not finalize Human Engineer decisions.

---

## 10. Human Approval Gates

The following gates require explicit Human Engineer approval:

| Gate | Required Before |
|---|---|
| **HG-D1 LOU Acceptance** | Treating LOU as accepted understanding for Requirements / CWC feed-forward |
| **HG-D2 Requirements Acceptance / CWC-Readiness** | Issuing Definition-dependent implementation-class CWC |
| HG-1 CWC-CE Approval | CEP execution / repository implementation under Controlled Execution |
| HG-2 ECR Approval | Controlled-change implementation under STD-014 |
| HG-3 Human Acceptance | CER closure and normal Git advancement of accepted work |
| HG-4 Git Commit Approval | Creating official commit history for the work |
| HG-5 Git Push Approval | Updating remote shared history |
| HG-6 Publication Approval | Public release |
| HG-7 Exception Approval | Any departure from this workflow |
| HG-8 Baseline Update Approval | Declaring or amending an Engineering Baseline |

Rules:

1. Approval shall be recorded in the governing artifact.  
2. Silence is not approval.  
3. AI shall never bypass approval gates.  
4. Conditional approval is valid only with recorded conditions.  
5. HG-D1 and HG-D2 do not authorize implementation.  

---

## 11. AI Execution Gates

Cursor AI and other AI agents may proceed with Controlled Execution implementation only when all applicable gates are satisfied:

| Gate | Condition |
|---|---|
| AG-1 | Approved CWC-CE exists and is referenced |
| AG-2 | Approved ECR exists when STD-014 requires it, or ECR is expressly `Not required` |
| AG-3 | Approved CEP exists and matches authorized scope |
| AG-4 | Target repositories and paths are inside approved scope |
| AG-5 | No unresolved conflict with ARCH-001, applicable standards, or POL-001 has been ignored |

If any AI Execution Gate fails, AI shall stop and report the blocker.

AI shall not:

1. Self-approve LOU, SPEC, CWC-CE, ECR, CER, commit, push, or publication  
2. Expand scope during execution  
3. Skip CER generation after CEP completion absent approved exception  
4. Report unverified work as verified  
5. Treat LOU or SPEC acceptance as implementation authorization  

---

## 12. Verification Gates

Verification occurs before Human Acceptance and is recorded in the CER.

| Gate | Verification Focus |
|---|---|
| VG-1 Deliverable Gate | Required deliverables exist at stated paths |
| VG-2 Scope Gate | Changes match approved CWC-CE / ECR / CEP scope |
| VG-3 Integrity Gate | No unauthorized files or repositories changed |
| VG-4 Traceability Gate | Identifiers and references are complete and consistent (including LOU/SPEC when applicable) |
| VG-5 Acceptance Criteria Gate | CWC-CE acceptance criteria status is assessed truthfully |
| VG-6 Multi-Repo Gate | All authorized repositories are accounted for |

Verification outcomes: `Pass` / `Fail` / `Partial` / `Not performed`.  
Unperformed verification shall be labeled `Not performed`.

---

## 13. Git Integration

Git is the durable history mechanism for approved implementation.

### 13.1 Git Sequence

```
Human Acceptance (or explicit Human Engineer commit authorization)
      ↓
Git Commit
      ↓
Git Push
```

### 13.2 Git Rules

1. Commit and push require Human Engineer approval under applicable Git standards.  
2. CER shall record commit identifiers when available.  
3. CER shall record push status truthfully.  
4. Multi-repository work shall record commit references per affected repository.  
5. Destructive Git operations remain prohibited absent explicit Human Engineer approval.  
6. Git actions do not replace Human Acceptance; they follow authorized acceptance/process.  

---

## 14. Publication Workflow

```
Human Acceptance
      ↓
Publication Approval
      ↓
Publish approved artifacts only
      ↓
Record publication channel and status
```

Publication rules:

1. Only accepted, publication-authorized artifacts may be published.  
2. Draft, in-review, failed, or partial packages are not published unless expressly authorized as such.  
3. Publication status is recorded in the CER or linked publication record.  
4. Public repositories are distribution surfaces, not systems of engineering authorization.  

If publication is not part of the work, record `Not applicable`.

---

## 15. Exception Workflow

Approved exceptions may alter sequence only under POL-001 and Human Engineer approval.

```
Exception Need Identified
      ↓
Human Engineer Exception Approval Recorded
      ↓
Exception-Bounded Execution
      ↓
CER records exception reference and effects
      ↓
Return to standard workflow at next valid gate
```

Exception rules:

1. Exceptions shall be narrow, time-bounded or terminal-conditioned, and recorded.  
2. Exceptions never authorize false reporting or fabricated verification.  
3. Emergency containment follows STD-014 Emergency Changes when applicable, then returns to this workflow.  
4. Expired exceptions have no force.  

---

## 16. Workflow Completion

Controlled Execution work is complete when all applicable conditions are met:

1. When Engineering Definition applied: HG-D1 and HG-D2 satisfied or expressly waived by Human Engineer  
2. Approved CWC-CE exists  
3. Required ECR is approved or expressly not required  
4. CEP execution results are reported by CER (unless approved exception)  
5. Verification gates are recorded truthfully  
6. Human Acceptance is recorded  
7. Required Git commit / push actions are completed or expressly deferred with recorded status  
8. Publication is completed or expressly not applicable  
9. Baseline is updated or expressly not applicable  
10. Outstanding issues are listed or expressly `None`  

Partial or failed work may complete the reporting workflow through CER and Human Acceptance without being treated as successful implementation.

---

## 17. Conformance

Work conforms to WF-001 when it:

1. Applies Engineering Definition when required by STD-001 for material work, or records an authorized HE waiver / historical exception  
2. Begins Controlled Execution with an approved CWC-CE  
3. Uses ECR only when and whenever STD-014 requires it  
4. Produces a CER for each completed CEP unless an approved exception exists  
5. Honors all Human Approval Gates including HG-D1 and HG-D2 when applicable  
6. Prevents AI bypass of approval or verification integrity  
7. Does not treat LOU or SPEC acceptance as implementation authorization  
8. Supports and correctly reports single- or multi-repository scope  
9. Integrates Git and publication status truthfully  
10. Updates baselines when applicable  
11. Does not require UNBKE  
12. Remains technology independent  

Nonconformance is an engineering defect and shall be corrected before closure of dependent records.

---

## 18. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Engineering Office Operating Workflow establishing the authoritative end-to-end operating sequence. |
| 1.1.0 | 2026-08-08 | ECR-002 / CWC-CE-054: Engineering Definition front-end; resolve CWC-start conflict; HG-D1/HG-D2; preserve Controlled Execution gates and CWC supremacy. |
| 1.2.0 | 2026-08-09 | CWC-CE-056 / CER-021 F-03: normative cross-reference to STD-001/TMP-002 research taxonomy; reaffirm research/AI non-authority. |
