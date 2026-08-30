# KSB-ISSUE-BRIDGE-001 — Verified ChatGPT → GitHub Issue → Actions Architecture

**Document ID:** KSB-ISSUE-BRIDGE-001  
**Classification:** Controlled Architecture (NON-PRODUCTION / PRE-IMPLEMENTATION)  
**Governing Work Card:** CWC-CE-088 Bounded Issue-Trigger Bridge Architecture Continuation  
**Related:** KSB-TRIGGER-RETURN-001; KSB-RENDER-BRIDGE-001; ECR-009 v0.3.0 **HUMAN ACCEPTED**  
**Status:** Architecture accepted — **IMPLEMENTED LOCALLY** — remote deploy Human-gated  
**Version:** 1.1.0  
**Date:** 2026-08-30  
**Preparing Agent:** CE-Engineer  
**Predecessor SHA:** `4aeaf60b330ad41b5750ce523ad850a75325aa78`  

```text
OUTCOME (architecture): A
ECR-009: v0.3.0 HUMAN ACCEPTED / LOCALLY IMPLEMENTED
REPOSITORY VISIBILITY: PUBLIC (verified)
TRIGGER: GitHub Issue opened (authorized actor only)
WORKFLOW_DISPATCH: NOT EXPOSED / NOT REQUIRED
ARTIFACT RETURN: EXPOSED — REAL-RUN PROOF PENDING
SELF-HOSTED RUNNER: ISOLATED RUNNER REQUIRED — HUMAN PROVISIONING REQUIRED
GIT: NOT ADVANCED
DEPLOYMENT: NOT PERFORMED
```

---

## 1. Live capability facts (Human-supplied; authoritative for this CWC)

| Capability | Classification |
|---|---|
| Issue create | **VERIFIED AVAILABLE** (probe `#1`) |
| Issue update/close | **VERIFIED AVAILABLE** (probe closed) |
| `workflow_dispatch` | **NOT EXPOSED** |
| `repository_dispatch` | **NOT EXPOSED** |
| Actions run/job inspection | **EXPOSED** (run `1` → 404) |
| Actions artifact list | **EXPOSED** |
| Actions artifact download | **EXPOSED** |
| Real artifact retrieval | **NOT YET PROVEN** (no real workflow/run) |
| Generic repo binary file fetch | **NOT** a viable PNG return path for this POC |

Probe evidence: `jhodges07/Constitutional-Engineering` issue `#1`, title `[NON-PROD] CWC-CE-088 TRIGGER CAPABILITY PROBE`, token `CE088-TRIGGER-PROBE-20260830`, `user=jhodges07`, `author_association=OWNER`, subsequently closed.

Repository visibility verified: **`public`** (`private: false`). Public Issue threat model **applies**.

---

## 2. Selected end-to-end path (candidate → controlled design)

```text
PHONE HUMAN
 → ChatGPT Prepare KSB Status
 → controlled status + press release (in conversation; not in Issue)
 → ChatGPT creates controlled KSB RENDER REQUEST Issue
 → GitHub Actions issues:opened
 → JOB gate (github-hosted): EVENT → AUTHORIZED → VALIDATED
 → JOB render (isolated Windows self-hosted): only if gate PASS
 → checkout pinned canonical_sha
 → verify baseline hash/dims
 → existing ksb_renderer (four variables only)
 → anti-drift PASS
 → artifact: PNG + RESULT.json
 → comment Issue with request_id / run_id / artifact name
 → ChatGPT reads Issue comment → inspects run → downloads artifact
 → reconciles RESULT.json ↔ PNG
 → KSB Sunday Publication Package COMPLETE (if all parts ready)
 → HUMAN REVIEW / PUBLICATION REQUIRED
 → STOP
```

Issue = **EXECUTION REQUEST** only — never engineering truth, maturity, CONTROL, LOU, canonical status, or publication.

---

## 3. Issue classification vs Active Git gates

| Object | Role |
|---|---|
| GitHub Issue | Non-canonical operational metadata / execution request |
| `main` / Git tree | Canonical engineering authority (HG-4 / HG-5) |
| Actions artifact | Temporary render execution artifact |
| Weekly image under `images/` | Canonical only after Human Git gates |

**REJECTED:** ChatGPT commit/push/merge to `main` as ordinary render trigger (preserves prior rejection).

Issues sit outside the canonical engineering tree → compatible with Active controls **if** they never become source-of-truth or publication.

---

## 4. Request identity

```text
request_id = KSB-RENDER-YYYY-MM-DD-NNN
```

Example: `KSB-RENDER-2026-08-30-001`

**Title rule (human/operator aid only — not sole auth):**

```text
[KSB-RENDER] YYYY-MM-DD KSB-RENDER-YYYY-MM-DD-NNN
```

Identity reconciliation chain:

```text
KSB cycle context
 → request_id
 → Issue number
 → Actions run_id (commented on Issue + run-name)
 → artifact name
 → RESULT.json
 → PNG SHA-256
 → package COMPLETE/INCOMPLETE
```

Do not depend solely on free-form title text.

---

## 5. Machine-readable Issue body (request schema)

Body SHALL contain exactly one fenced JSON block marked:

```text
```ksb-render-request
{ ... }
```
```

### Envelope vs payload (Bill-future extensibility without implementing Bills)

```json
{
  "request_schema_version": "1.0.0",
  "publication_request_type": "KSB_WEEKLY_STATUS",
  "request_id": "KSB-RENDER-2026-08-30-001",
  "canonical_sha": "4aeaf60b330ad41b5750ce523ad850a75325aa78",
  "baseline_id": "BL-WEEKLY-STATUS-BASELINE-v1.0",
  "renderer_id": "ksb_renderer@1.0.0-CWC-CE-084",
  "render_payload": {
    "status_date": "2026-08-30",
    "bill_a_percent": 19,
    "bill_b_percent": 19,
    "bill_c_percent": 4
  }
}
```

### Four-variable firewall

`render_payload` MAY contain **only**:

`status_date` · `bill_a_percent` · `bill_b_percent` · `bill_c_percent`

- integers 0–100 inclusive for percents  
- ISO date for `status_date`  
- unknown field in `render_payload` → **REJECT**  
- no prose interpreted as renderer instructions  
- no path / shell / font / baseline / filename selectors in Issue

Envelope metadata authenticates/identifies the request; it does **not** expand renderer authority.

Press release SHALL NOT be placed in the Issue.

---

## 6. Authorization rule (mandatory; fail closed)

**Public repository:** any GitHub user may open Issues. Title/body tokens are forgeable. Therefore:

### Trusted signals (GitHub event metadata + Actions configuration — NOT Issue secrets)

**RENDER AUTHORIZED** only if **all** of the following hold:

1. `github.event_name == 'issues'` and `github.event.action == 'opened'`  
2. `github.event.issue.user.login` is in **AUTHORIZED_KSB_RENDER_ACTORS** (Actions repository Variable or Secret — allowlist maintained by Human; **not** stored in Issue body)  
3. `github.event.issue.author_association` ∈ `{ OWNER, MEMBER, COLLABORATOR }`  
4. Title matches `^[KSB-RENDER] ` (filter only; insufficient alone)  
5. Body parses as `ksb-render-request` JSON schema v1.0.0  
6. `canonical_sha` / `baseline_id` / `renderer_id` match controlled allowlists for this bridge version  
7. Duplicate/idempotency check PASS  

Otherwise:

```text
UNAUTHORIZED → comment + label ksb-render:rejected-auth → close Issue → STOP (no render job)
```

**Probe consistency:** Issue `#1` used `user=jhodges07`, `author_association=OWNER` — matches intended ChatGPT-connected Human identity.

**REJECTED authorization methods:** public body token; title prefix alone; issue number; security through obscurity.

---

## 7. Event filter and staged gates

```yaml
on:
  issues:
    types: [opened]
```

Separate:

| Stage | Meaning |
|---|---|
| EVENT RECEIVED | Any Issue opened |
| REQUEST AUTHORIZED | Actor allowlist + association PASS |
| REQUEST VALIDATED | Schema + four-variable + SHA/baseline/renderer IDs PASS |
| RENDER AUTHORIZED | Prior stages PASS and idempotency allows execution |

Unrelated Issues: no-op / immediate skip (no runner cost).

### Two-job pattern (abuse control)

| Job | Runner | Work |
|---|---|---|
| `gate` | `ubuntu-latest` (GitHub-hosted) | Auth + validate only |
| `render` | Isolated Windows self-hosted | Checkout pinned SHA + render **only if** `gate` PASS |

Public spam must not reach the Windows runner.

Concurrency: one active render per `request_id`; global low concurrency limit for render job.

---

## 8. Canonical SHA / baseline / renderer binding

| Binding | Rule |
|---|---|
| Canonical SHA | Request carries explicit `canonical_sha` from KSB package prep; workflow `actions/checkout@…` **ref = that SHA**; **no** floating `main` at run time |
| Baseline | Path fixed in trusted workflow/code; verify SHA-256 `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9`, dims 1536×912; mismatch → FAIL CLOSED |
| Renderer | Invoked only from checked-out trusted tree; Issue cannot select path/script/shell/font/baseline |

---

## 9. Self-hosted runner security decision

### Threat

Public Issue events on a **public** repository must not execute untrusted code on the Human Engineer’s personal workstation.

### Required controls

1. Workflow YAML executed is from the repository default branch / trusted workflow definition — **not** from Issue content.  
2. Issue fields treated **only** as validated data (never interpolated into shell).  
3. This bridge SHALL NOT listen to `pull_request` from forks.  
4. `render` job runs only after `gate` PASS.  
5. Least-privilege `GITHUB_TOKEN` permissions; no broad secrets on render job beyond necessity.  
6. **Human workstation as runner: UNACCEPTABLE** for this public Issue-trigger design.

### Decision

```text
SELF-HOSTED RUNNER SECURITY: ISOLATED RUNNER REQUIRED
HUMAN WORKSTATION: NOT ACCEPTABLE
```

Isolated Windows environment = dedicated machine/VM with only runner + renderer dependencies + controlled fonts; no personal browser sessions, no unrelated secrets, no interactive Human daily-driver compromise path.

Runner registration remains **separately Human-gated** after ECR-009 ACCEPT — not performed under this CWC.

---

## 10. Issue → run → artifact correlation

| Mechanism | Role |
|---|---|
| `request_id` | Primary business identity |
| Issue number | GitHub object identity |
| Actions `run-name` | `KSB-RENDER {request_id} issue-{n}` |
| Issue comment (trusted workflow) | Posts `run_id`, HTML URL, artifact name, execution_result |
| Artifact name | `ksb-render-{request_id}` |

**ChatGPT reconciliation path (uses verified Issue + Actions read capabilities):**

1. Retain `request_id` + Issue number in Active KSB context.  
2. Read Issue comments until workflow posts run correlation (or poll briefly).  
3. Inspect run by `run_id`.  
4. List/download artifact by name/`run_id`.  
5. Parse RESULT.json; reconcile PNG.

```text
ISSUE # → REQUEST ID → ACTIONS RUN → ARTIFACT
```

**Correlation implementation note (CWC-CE-090 / KSB-089-D02):** workflow Issue lifecycle commands SHALL pass explicit `-R ${{ github.repository }}` (trusted Actions context). They SHALL NOT rely on cwd/.git inference. Issue payload MUST NOT supply repository identity.

Run **discovery** does not require `workflow_dispatch`. Real download remains **REAL-RUN PROOF PENDING** until Human-authorized Test #3 after D02 Git canonicalization.

---

## 11. Artifact + RESULT.json contract

### Artifact package (exactly)

1. `ksb-status.png` (or controlled filename recorded in RESULT)  
2. `RESULT.json`  

No secrets, no full workspace dump, no unrelated logs.

### RESULT.json (minimum)

```json
{
  "schema_version": "1.0.0",
  "request_id": "KSB-RENDER-2026-08-30-001",
  "issue_number": 2,
  "run_id": 123456789,
  "canonical_sha": "…",
  "status_date": "2026-08-30",
  "bill_a_percent": 19,
  "bill_b_percent": 19,
  "bill_c_percent": 4,
  "baseline_id": "BL-WEEKLY-STATUS-BASELINE-v1.0",
  "baseline_sha256": "17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9",
  "renderer_identity": "ksb_renderer@1.0.0-CWC-CE-084",
  "output_filename": "ksb-status.png",
  "output_sha256": "…",
  "output_dimensions": [1536, 912],
  "renderer_test_result": "PASS|FAIL",
  "anti_drift_result": "PASS|FAIL",
  "execution_result": "SUCCEEDED|FAILED|REJECTED"
}
```

PNG alone **never** satisfies KSB image requirement without RESULT validation PASS + anti-drift PASS.

---

## 12. Issue lifecycle

| Terminal state | Behavior |
|---|---|
| SUCCESS | Comment RESULT summary; label `ksb-render:succeeded`; close Issue |
| FAILURE | Comment failure class; label `ksb-render:failed`; close Issue |
| INVALID REQUEST | Comment; label `ksb-render:rejected-invalid`; close |
| UNAUTHORIZED | Comment; label `ksb-render:rejected-auth`; close |
| DUPLICATE | Comment prior run/artifact refs; label `ksb-render:duplicate`; close |

Issue state ≠ publication authority.

---

## 13. Replay / idempotency

Same `request_id` + `canonical_sha` + identical four renderer values → return prior successful artifact references; **do not** mint conflicting authoritative outputs.

Changed percent or SHA → new `request_id` (or explicit supersession field in a later schema version under separate authority).

---

## 14. Human certification & publication

Upstream only:

```text
CONTROLLED EVIDENCE → MATURITY → HUMAN CERTIFICATION → render_payload → Issue
```

Bridge does not calculate/certify/change maturity.

Successful render ends at:

```text
KSB SUNDAY PUBLICATION PACKAGE — READY FOR HUMAN REVIEW
```

No Facebook / BlueprintLiberty.com / release / merge-to-main / candidate outreach.

---

## 15. Later implementation plan (NOT authorized now)

After Human ACCEPT of ECR-009 + separate implementation CWC:

1. One Actions workflow (`ksb-render-bridge.yml`) with `gate` + `render` jobs  
2. Request schema validator  
3. RESULT schema writer  
4. Non-production fixture values for first real-run proof  
5. Isolated Windows runner registration (Human-gated)  
6. `AUTHORIZED_KSB_RENDER_ACTORS` variable  
7. Artifact packaging + Issue comment correlator  

**Do not implement under this continuation.**

---

## 16. Real-run proof plan (Test 12 — execute later)

Non-production only:

1. Human ACCEPTs ECR-009 and authorizes implementation CWC.  
2. Deploy workflow + isolated runner + actor allowlist.  
3. ChatGPT creates Issue with fixture `render_payload` (not live publication values required).  
4. Confirm unauthorized alternate account Issue is rejected at `gate`.  
5. Confirm authorized Issue reaches render; baseline verified; renderer runs; anti-drift PASS.  
6. Artifact contains only PNG + RESULT.json.  
7. ChatGPT discovers run via Issue comment; lists artifact; downloads; reconciles RESULT↔PNG.  
8. Confirm no merge/publish/maturity change.  
9. Close/label Issue per lifecycle.  

**PASS criterion:** end-to-end without Cursor/manual Python; real artifact retrieval proven.  
**Not executed under this CWC.**

---

## 17. Architecture classification

```text
VIABLE WITH ADDITIONAL CONTROLS
```

Controls mandatory in ECR-009 (not optional convention):

- actor allowlist + author_association  
- two-job gate/render split  
- pinned SHA checkout  
- four-variable firewall  
- isolated Windows runner (not Human workstation)  
- Issue comment correlation  
- RESULT↔PNG reconciliation  
- no main-branch trigger; no creative recovery  

---

## 18. Version history

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-30 | Issue-trigger architecture from live ChatGPT proofs; public-repo threat model; isolated runner required. |
