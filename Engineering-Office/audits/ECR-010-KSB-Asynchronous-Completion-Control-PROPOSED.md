# ECR-010 — KSB Asynchronous Completion and Human Command Contract (AMENDED)

**Document ID:** ECR-010  
**Title:** KSB Asynchronous Completion / Continuation / Duplicate-Request Firewall  
**Classification:** Engineering Change Request — **AMENDED PROPOSAL**  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-011 Part B (§36); KSB-ORCH-001  
**Governing Work Card:** CWC-CE-089; **CWC-CE-090** (bounded amendment)  
**Predecessor:** ECR-008; ECR-009; CWC-CE-088  
**Related Evidence:** CWC-CE-089-ASYNC-COMPLETION-DESIGN; CWC-CE-090 validation; Actions run `33334671439`; Issue `#3`; request `KSB-RENDER-2026-08-30-002`  
**Status:** **AMENDED — BOUNDED HUMAN CONCURRENCE RECORDED (CWC-CE-090)**  
**Version:** **0.1.1-AMENDED**  
**Effective Date:** (full ECR remains gated; D02 remediation authorized under CWC-CE-090)  
**Primary Category:** PUB  
**Secondary Categories:** STD, ADM, SEC  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  

```text
HUMAN ENGINEER DECISION (CWC-CE-090): AMEND
HUMAN ENGINEER DECISION (CWC-CE-092): D01 SUPERSEDED by three-step contract (ECR-011)

KSB-089-D01: SUPERSEDED BY ECR-011 THREE-STEP MODEL (not Continue-command design)
KSB-089-D02: AUTHORIZED FOR BOUNDED REMEDIATION (CWC-CE-090) — remediated
HOSTED FIXTURE: INVESTIGATION AUTHORIZED
HISTORICAL FIXTURE REPLACEMENT: NOT AUTHORIZED
TEST #2 RERUN: NOT AUTHORIZED
TEST #3: NOT AUTHORIZED UNDER CWC-CE-090
PUBLICATION: NOT AUTHORIZED
ASYNC Continue-command SEMANTICS: NOT AUTHORIZED — superseded by Prepare/Next/Next
```

---

## 0. Amendment record (CWC-CE-090)

| Field | Value |
|---|---|
| Prior version | `0.1.0-PROPOSED` |
| This version | **`0.1.1-AMENDED`** |
| Human disposition | **AMEND** (concurred with CWC-CE-089 Outcome C analysis; narrowed implementation) |
| Authorized now | Repair **KSB-089-D02** (Issue→run→artifact correlation without git-cwd inference); investigate hosted vs historical fixture semantics |
| Explicitly deferred | Full async Human command contract (**KSB-089-D01**); Continue/Prepare-resume implementation; STD-011 §36.11 / KSB-ORCH 1.2.0 async semantics |

This amendment records the Human concurrence for the **bounded** disposition above. It does **not** Human-accept the full original 0.1.0 async implementation package.

---

## 1. Problem (unchanged facts)

Acceptance Test #2 demonstrated:

1. **KSB-089-D01:** ChatGPT returned before Actions finished — Human did not receive the complete package in-turn.  
2. **KSB-089-D02:** After successful hosted render + artifact upload, `gh issue comment` failed (`fatal: not a git repository`) because repository identity was inferred from cwd/.git while the Windows job used path-scoped checkouts.

---

## 2. Authorized change under this amendment (CWC-CE-090 only)

### 2.1 KSB-089-D02 — AUTHORIZED

Prefer explicit repository targeting:

```text
gh issue <verb> -R ${{ github.repository }} <issue_number> …
```

Trusted source: GitHub Actions `github.repository` for the repository that received the triggering Issue.  
**Forbidden:** repository identity from untrusted Issue payload / request JSON.

Preserve Issue lifecycle already defined by **KSB-ISSUE-BRIDGE-001 §12**:

| Terminal | Behavior |
|---|---|
| SUCCESS | Comment RESULT summary; label `ksb-render:succeeded`; close Issue |
| FAILURE | Comment failure class; label `ksb-render:failed`; close Issue |
| REJECT paths | Comment; rejected-* label; close |

### 2.2 Hosted fixture investigation — AUTHORIZED (observe-only)

Investigate Test #2 PNG vs historical fixture `758AFA76…` and prior local `10BE46…` output.  
**Do not** replace historical fixture. **Do not** change baseline.

### 2.3 KSB-089-D01 — PARKED (NOT AUTHORIZED to implement)

Preserve candidate model for later Human consideration:

```text
Prepare KSB Status → request → IN PROGRESS if incomplete
→ Continue KSB Status / Prepare-resume → reconcile existing run/artifact → complete package
```

Do **not** implement under CWC-CE-090.

---

## 3. Security constraints (must preserve)

`issues:opened` · `AUTHORIZED_KSB_RENDER_ACTORS` · `author_association` · `[KSB-RENDER]` · schema · four variables · SHA/baseline/renderer allowlists · idempotency · gate-before-render · fail-closed · Issue/request/run/artifact correlation.

Explicit `-R` must not enable correlation against an arbitrary repository from Issue content.

---

## 4. Deferred implementation package (after future Human ACCEPT of remaining D01 scope)

| Item | Status under 0.1.1-AMENDED |
|---|---|
| STD-011 §36.11 async / continuation | **DEFERRED** |
| KSB-ORCH-001 Continue / resume | **DEFERRED** |
| ChatGPT async operator instructions | **DEFERRED** |
| Workflow D02 `-R` correlation fix | **AUTHORIZED / implement under CWC-CE-090** |

---

## 5. Disposition

| Field | Value |
|---|---|
| Disposition | **AMENDED** — D02 + fixture investigation authorized; D01 parked |
| Full async ECR ACCEPT | **NOT GRANTED** |
| CE-Engineer self-accept of D01 | **PROHIBITED** |
