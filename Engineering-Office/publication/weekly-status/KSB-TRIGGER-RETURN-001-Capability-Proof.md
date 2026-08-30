# KSB-TRIGGER-RETURN-001 — ChatGPT Trigger / Artifact-Return Capability Proof

**Document ID:** KSB-TRIGGER-RETURN-001  
**Classification:** Capability Proof / Architecture Resolution (NON-PRODUCTION)  
**Governing Work Card:** CWC-CE-088 Bounded Trigger / Artifact-Return Capability Continuation  
**Related:** KSB-RENDER-BRIDGE-001; ECR-009 (Proposed); CWC-CE-074; STD-011 v1.5.0; KSB-ORCH-001 v1.1.0  
**Status:** Discovery Complete — Live ChatGPT Proof Required  
**Version:** 1.0.0  
**Date:** 2026-08-30  
**Preparing Agent:** CE-Engineer  
**Predecessor SHA:** `4aeaf60b330ad41b5750ce523ad850a75325aa78`  

```text
OUTCOME (this doc): B at issuance — SUPERSEDED for trigger selection by KSB-ISSUE-BRIDGE-001
LIVE PROOF STATUS: INCORPORATED (Human-supplied) — see KSB-ISSUE-BRIDGE-001 / ECR-009 0.3.0
SELECTED TRIGGER (post-proof): GitHub Issue opened (authorized actor)
WORKFLOW_DISPATCH: NOT EXPOSED / NOT REQUIRED
ARTIFACT RETURN: EXPOSED — REAL-RUN PROOF PENDING
NO PRODUCTION WORKFLOW DEPLOYED
NO SELF-HOSTED RUNNER REGISTERED
GIT: NOT ADVANCED
KSB IMAGE: RENDER REQUIRED
PACKAGE STATE: INCOMPLETE
```

---

## 1. Controlling question

What authenticated mechanism **actually available to the intended ChatGPT phone workflow** can:

A. initiate the controlled KSB render operation; **and**  
B. retrieve or make available the controlled PNG + validation result to the same KSB workflow;

without requiring the Human to open Cursor or a desktop tool?

Three layers MUST remain distinct:

| Layer | Meaning |
|---|---|
| GitHub supports X | Platform API / product feature exists |
| ChatGPT can invoke X | Product surface may expose the operation |
| **This project’s ChatGPT↔GitHub integration can invoke X** | Proven by CWC evidence or live project proof |

Only the third layer authorizes bridge design reliance.

---

## 2. CWC-CE-074 — exact proven statement (no extrapolation)

**Authority artifact:**  
`Engineering-Office/publication/weekly-status/integration-test/CHATGPT-GITHUB-CAPABILITY-TEST.md`

**Canonical commits:**

| SHA | Message | What it proves |
|---|---|---|
| `f2e48bc` | add non-production ChatGPT GitHub capability test | Test object created |
| `943d905` | verify ChatGPT GitHub write capability | Status fields set to READ/WRITE PASS |
| `e418c8d` | record Cursor round-trip verification PASS | Cursor verified GitHub-hosted result |

**Recorded capability fields (current):**

```text
CHATGPT_READ_STATUS: PASS
CHATGPT_WRITE_STATUS: PASS
CHATGPT_WRITE_TIMESTAMP: 2026-08-30T08:00:00-05:00
CURSOR_VERIFICATION_STATUS: PASS
```

### Proven

| Operation | Proven? | Exact evidence |
|---|---|---|
| **READ** GitHub-hosted file content | **YES** | Challenge token retrieved from GitHub copy (Human-pasted chat text explicitly disallowed) |
| **WRITE** narrowly authorized fields on that one file | **YES** | Commit `943d905` by `jhodges07` updating only authorized status fields on `main` |
| Cursor round-trip of GitHub interchange | **YES** | `CURSOR_VERIFICATION_STATUS: PASS` |

### Explicitly NOT proven by CWC-CE-074

| Operation | Status |
|---|---|
| Arbitrary file create/update | NOT PROVEN (write boundary was three status fields only) |
| Branch create / non-`main` write | NOT PROVEN |
| Commit / push as general Git authority | NOT PROVEN as unrestricted; only the authorized test write landed |
| Issue create/update | NOT PROVEN |
| Pull request create/update | NOT PROVEN |
| Actions workflow list | NOT PROVEN |
| `workflow_dispatch` | NOT PROVEN |
| `repository_dispatch` | NOT PROVEN |
| Actions run status | NOT PROVEN |
| Actions artifact list | NOT PROVEN |
| Actions artifact download | NOT PROVEN |
| Webhook | NOT PROVEN |
| Generic authenticated HTTP call | NOT PROVEN |

```text
HISTORICAL PROOF SUMMARY:
READ = VERIFIED
WRITE = VERIFIED (narrow integration-test file fields only)
ACTIONS DISPATCH = NOT IN EVIDENCE
ACTIONS ARTIFACT RETRIEVAL = NOT IN EVIDENCE
```

Do **not** interpret “GitHub read/write PASS” as Actions dispatch or artifact retrieval.

---

## 3. Capability matrix — project ChatGPT↔GitHub integration

| Capability | Classification | Evidence / required proof |
|---|---|---|
| READ repository content | **VERIFIED AVAILABLE** | CWC-CE-074 READ PASS |
| WRITE (authorized test fields) | **VERIFIED AVAILABLE** | CWC-CE-074 WRITE PASS / `943d905` |
| CREATE/UPDATE arbitrary file | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | Not in CWC-074 authorized boundary |
| BRANCH operation (create/update non-main) | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | Not proven |
| COMMIT/PUSH (general) | **NOT EXPOSED as general authority** | Proven only as narrow authorized write effect |
| ISSUE create/write | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | Not proven |
| PR create/write | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | Not proven |
| Actions workflow list | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | Repo has 0 workflows; tool exposure unknown |
| `workflow_dispatch` | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | GitHub supports; project ChatGPT path unverified |
| `repository_dispatch` | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | Same |
| Actions run status | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | Same |
| Actions artifact list | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | Same |
| Actions artifact download | **UNKNOWN — REQUIRES LIVE CHATGPT PROOF** | Same |
| Webhook | **NOT EXPOSED** | No project webhook integration |
| Generic authenticated HTTP | **REQUIRES NEW INTEGRATION** | No project-controlled render endpoint; ChatGPT Action/plugin not authorized |
| Active KSB conversational continuity | **VERIFIED AVAILABLE** (orchestration design) | KSB-ORCH-001 Active-cycle context |

---

## 4. GitHub platform inventory (not ChatGPT capability)

| Finding | Result |
|---|---|
| Actions enabled | Yes |
| Workflows present | **0** (`total_count: 0`) |
| `.github/` in tree | Absent |
| Production render workflow | Must **not** be created under this continuation |

GitHub supporting Actions ≠ ChatGPT can dispatch Actions in this project.

---

## 5. Trigger candidates

### A — `workflow_dispatch`

| Question | Answer |
|---|---|
| Can ChatGPT identify a workflow? | **UNKNOWN — LIVE PROOF REQUIRED** |
| Can ChatGPT initiate it? | **UNKNOWN — LIVE PROOF REQUIRED** |
| Pass four controlled values? | **UNKNOWN** (depends on tool + future workflow inputs) |
| Control branch/SHA? | **UNKNOWN** |
| Obtain run ID? | **UNKNOWN** |
| Read run status later? | **UNKNOWN** |

```text
TRIGGER A = UNVERIFIED
```

### B — `repository_dispatch`

Not exposed in project evidence. Do not design around it until live proof shows the ChatGPT integration can create repository_dispatch events.

```text
TRIGGER B = UNVERIFIED / NOT DESIGNED AROUND
```

### C — Controlled GitHub object (issue / PR / request branch)

Investigative only.

| Mechanism | Assessment |
|---|---|
| ChatGPT commit render request to **canonical `main`** to trigger Actions | **REJECTED** — conflicts with HG-4/HG-5; CWC-074 write proof does not authorize ordinary Sunday auto-commits to `main` |
| Issue as request object | **UNKNOWN** — issue create not proven; could be live-tested safely; Actions would still need a listener workflow (not authorized to deploy yet) |
| Non-canonical request branch | **UNKNOWN** — branch write not proven; merge-to-main MUST remain Human-gated |
| PR as trigger | **UNKNOWN** — PR create not proven; same Git-gate concerns if auto-merge |

```text
TRIGGER C = NOT RECOMMENDED as ordinary path unless live-proven AND Human Git gates preserved
```

### D — External authenticated HTTP endpoint

```text
REQUIRES NEW INTEGRATION
```

No controlled render endpoint exists. Public unauthenticated endpoint **REJECTED**.

### E — Plugin / connector extension (narrow)

If live proof shows built-in GitHub integration cannot dispatch / retrieve artifacts, the **smallest new integration** is a Custom GPT Action (or equivalent) exposing only:

1. `START_KSB_RENDER` (four variables + request identity + pinned SHA)  
2. `GET_KSB_RENDER_STATUS`  
3. `GET_KSB_RENDER_RESULT` (RESULT contract + artifact reference)

This remains **design-only** until Human authority after proof.

---

## 6. Artifact-return candidates

### A — Actions artifact

| Layer | Classification |
|---|---|
| GitHub capability | Platform supports upload/download of Actions artifacts |
| ChatGPT connector capability | **UNKNOWN — LIVE PROOF REQUIRED** |
| Active chat workflow capability | **UNKNOWN — LIVE PROOF REQUIRED** |

Do not assume Actions upload ⇒ ChatGPT retrieval.

### B — Controlled repository object (readable by verified READ)

If RESULT.json (and optionally PNG) are placed on a **non-canonical** path/branch that ChatGPT can READ:

| Property | Assessment |
|---|---|
| Compatible with VERIFIED READ | **Yes (class)** — if content is readable text/JSON; PNG binary readability **LIVE PROOF REQUIRED** |
| Auto-merge to main | **FORBIDDEN** |
| Canonical publication | Still HG-gated |
| Race / duplicates | Requires request-id idempotency |

### C — Controlled private storage + authenticated retrieval

Document-only if A and B fail live proof. **Not implemented.**

---

## 7. Required result contract (any viable return)

Machine-readable RESULT must expose at least:

request identity · run identity · repository SHA · status_date · bill_a/b/c_percent · baseline identity/SHA · renderer identity · render status · validation · anti-drift · dimensions · output SHA-256 · artifact identity/location

Active KSB workflow must distinguish **SUCCESS** vs **RENDER REQUIRED**.

Asynchronous states: `REQUESTED | QUEUED | RUNNING | VALIDATING | SUCCEEDED | FAILED | EXPIRED`  
Package remains **INCOMPLETE** while pending.

---

## 8. Security rules (design constraints; not yet implemented)

| Rule | Requirement |
|---|---|
| Input | Only four renderer variables (or request-id resolving to them); unknown fifth field → REJECT |
| Execution | No arbitrary shell/Python/Git/path/baseline/renderer selection |
| Auth | Authenticated caller; least privilege (render start/status/result only) |
| Canonical SHA | Prefer **request-time pinned SHA** recorded on the request; runner checks out that SHA (avoid floating `main` TOCTOU) |
| Output | Unverified PNG alone does not satisfy KSB image requirement |
| Human gates | Cannot silently merge to main, publish, change maturity, pass HG-PR/HG-D1 |
| Creative recovery | **PROHIBITED** |

---

## 9. Windows runner / font program

Windows self-hosted remains the **leading continuity candidate** (Arial Bold determinism).  

**Runner decision DEFERRED** until trigger-and-return path is proven.  
**Alternate font program NOT STARTED.**

---

## 10. Bill-level extensibility (design note only)

Prefer a bounded **publication-render request** transport abstraction (request type + four-or-N controlled variables + pinned SHA + RESULT contract) so future Human-authorized Bill status renderers can reuse the same execution transport.

**Not implemented:** Bill-specific templates, images, commands, or maturity systems. KSB remains the reference POC.

---

## 11. Selected architecture pending proof

| Item | State |
|---|---|
| Selected trigger | **UNRESOLVED** — preferred candidate remains Actions `workflow_dispatch` **if** live ChatGPT proof (or authorized Custom GPT Action) verifies it |
| Selected artifact return | **UNRESOLVED** — prefer Actions artifact **if** ChatGPT can retrieve; fallback candidate = RESULT.json on non-canonical readable location using VERIFIED READ |
| Authentication | **GAP** until credential/tool model proven |
| Least privilege | **Design PASS / implementation GAP** |
| Trigger/return architecture | **PARTIAL** — Live ChatGPT Proof Required |

---

## 12. LIVE CHATGPT CAPABILITY PROOF REQUIRED

Cursor cannot invent ChatGPT product tool exposure. Perform these tests from the **intended phone ChatGPT workflow** with the **same GitHub connection** used for CWC-CE-074.

### PROOF-0 — Tool inventory

**Test:** Ask ChatGPT to list every GitHub operation/tool it can actually invoke in this session (exact names).  
**Safe object:** None.  
**Success evidence:** Explicit tool inventory (even if short).  
**Failure evidence:** Refusal / “I can only read” / no tool list.

### PROOF-1 — Actions workflow list

**Test:** “Using your GitHub integration, list Actions workflows for `jhodges07/Constitutional-Engineering`.”  
**Expected if tool exists:** Empty list / total_count 0 (repo has no workflows).  
**Expected if tool missing:** Clear inability — classify **NOT EXPOSED**.  
**No publication. No workflow creation. No maturity change.**

### PROOF-2 — workflow_dispatch probe

**Test:** Attempt to dispatch a workflow named `ksb-render-bridge` (or any named workflow).  
**Expected:**  
- Tool missing → **NOT EXPOSED**  
- Tool present + no workflow → controlled API/tool error (still proves exposure)  
**Do not create a production workflow for this proof.**

### PROOF-3 — Run status probe

**Test:** Attempt to get status for a nonexistent run ID (e.g., `1`).  
**Expected:** Tool missing → NOT EXPOSED; tool present → controlled not-found error.

### PROOF-4 — Artifact list/download probe

**Test:** Attempt to list Actions artifacts for the repository / a nonexistent run.  
**Expected:** Tool missing → NOT EXPOSED; tool present → empty or not-found.

### PROOF-5 — Issue create (alternate trigger probe)

**Test:** Create issue titled exactly:

```text
[NON-PROD] CWC-CE-088 TRIGGER CAPABILITY PROBE
```

Body must include token:

```text
CE088-TRIGGER-PROBE-20260830
```

**Success:** Issue URL + number returned.  
**Then:** Human closes/deletes the issue.  
**Do not** attach Actions automation yet.  
**Do not** treat issue create alone as a complete render bridge.

### PROOF-6 — Binary/PNG readability (artifact-return class)

**Test:** Ask ChatGPT to read from GitHub the accepted baseline PNG path and report whether it can obtain the file bytes or only metadata/link:

```text
Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png
```

**Expected success evidence:** Clear statement of retrieveability (bytes/hash vs link-only).  
**Do not modify the baseline.**

### PROOF-7 — Active-context continuity (optional, same chat)

**Test:** In one KSB chat, after a long pause, ask ChatGPT to restate Active-cycle Bill A/B/C values and package completeness rule.  
**Success:** Context retained without restarting Sunday package assembly.

---

## 13. Decision tree after live proof

| If live proof shows… | Next architecture |
|---|---|
| workflow_dispatch + run status + artifact retrieval available | Refine ECR-009 toward Actions bridge; then Human ACCEPT may authorize non-prod fixture workflow + runner under separate CWC |
| READ available; Actions APIs NOT EXPOSED; issue/branch write available | Evaluate IssueOps / request-branch design with Human Git gates; still needs execution environment |
| Only READ + narrow WRITE (CWC-074 class) | **NEW INTEGRATION REQUIRED** — Custom GPT Action with START/STATUS/GET RESULT |
| No reliable authenticated trigger at all | Outcome C / BLOCKED until integration decision |

---

## 14. Failure-safe (current correct behavior)

Until bridge is operational:

```text
KSB IMAGE: RENDER REQUIRED
PACKAGE STATE: INCOMPLETE
```

No creative substitution.

---

## 15. Version history

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-30 | Capability proof from CWC-074 evidence; Outcome B; live ChatGPT proof pack; ECR-009 modify recommendation. |
