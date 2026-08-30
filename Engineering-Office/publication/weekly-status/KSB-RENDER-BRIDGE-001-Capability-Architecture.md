# KSB-RENDER-BRIDGE-001 — Phone-to-Deterministic-Render Capability Discovery & Architecture

**Document ID:** KSB-RENDER-BRIDGE-001  
**Classification:** Engineering Architecture / Capability Discovery  
**Governing Work Card:** CWC-CE-088 Bounded Runtime-Bridge Continuation  
**Related CONTROL:** STD-011 v1.5.0 §36; KSB-ORCH-001 v1.1.0; ECR-008 Implemented locally; CWC-CE-084 renderer  
**Related Proposed ECR:** ECR-009 (0.2.0-PROPOSED)  
**Related Capability Proof:** KSB-TRIGGER-RETURN-001  
**Status:** Discovery Complete — Trigger/return UNRESOLVED — **Live ChatGPT Proof Required**  
**Version:** 1.1.0  
**Date:** 2026-08-30  
**Preparing Agent:** CE-Engineer  
**Predecessor SHA:** `4aeaf60b330ad41b5750ce523ad850a75325aa78`  

```text
CONTROL CONTRACT: PASS (ECR-008 / STD-011 1.5.0 / KSB-ORCH-001 1.1.0)
RUNTIME EXECUTION: BRIDGE REQUIRED
PHONE → RENDER TRIGGER: GAP (LIVE CHATGPT PROOF REQUIRED)
ARTIFACT RETURN: GAP (LIVE CHATGPT PROOF REQUIRED)
CREATIVE SUBSTITUTION: PROHIBITED
GIT: NOT ADVANCED
LIVE HUMAN PHONE RE-POC: NOT PERFORMED
WINDOWS RUNNER: CANDIDATE / DEFERRED
```

---

## 1. Purpose

Determine whether ChatGPT (phone) can initiate an authorized remote execution of the **existing** deterministic KSB renderer without requiring the Human to open Cursor / run Python manually.

---

## 2. ChatGPT / phone capability matrix

Evidence basis: CWC-CE-074 (READ/WRITE PASS for **narrow** integration-test fields only); KSB-TRIGGER-RETURN-001; absence of verified Actions dispatch/artifact retrieval from ChatGPT; STD-011 / KSB-ORCH runtime notes.

| ID | Capability | Classification | Evidence |
|---|---|---|---|
| A | Read canonical GitHub content | **VERIFIED AVAILABLE** | CWC-CE-074 `CHATGPT_READ_STATUS: PASS` |
| B | Write authorized request artifact to GitHub | **REQUIRES ADDITIONAL INTEGRATION** / LIVE PROOF for arbitrary paths | Write proven only for CWC-074 status fields; **not** ordinary render-request / `main` trigger authority |
| C | Create/update GitHub Issue | **UNKNOWN — LIVE CHATGPT PROOF REQUIRED** | Not verified |
| D | Invoke existing GitHub workflow | **NOT AVAILABLE** (no workflows) + **LIVE PROOF** for tool exposure | Repo `workflows: []` |
| E | Invoke `workflow_dispatch` | **UNKNOWN — LIVE CHATGPT PROOF REQUIRED** | GitHub supports; project ChatGPT path unverified |
| F | Invoke `repository_dispatch` | **UNKNOWN — LIVE CHATGPT PROOF REQUIRED** | Same |
| G | Call controlled authenticated HTTP endpoint | **REQUIRES NEW INTEGRATION** | No controlled render endpoint exists |
| H | Receive/read resulting PNG / artifact reference | **UNKNOWN — LIVE CHATGPT PROOF REQUIRED** | READ class may cover RESULT.json; Actions artifact download unverified |
| I | Verify completion state | **UNKNOWN — LIVE CHATGPT PROOF REQUIRED** | Depends on H + RESULT schema |
| J | Retrieve validation evidence | **UNKNOWN — LIVE CHATGPT PROOF REQUIRED** | Depends on RESULT schema |
| K | Preserve Active KSB conversational context | **VERIFIED AVAILABLE** (orchestration) | KSB-ORCH-001 Active-cycle context |

**Critical conclusion:** CWC-074 READ/WRITE ≠ Actions dispatch or artifact retrieval. Trigger/return remain **LIVE CHATGPT PROOF REQUIRED** (see KSB-TRIGGER-RETURN-001 §12).

---

## 3. GitHub-side discovery

| Finding | Result |
|---|---|
| `.github/workflows` in repo | **Absent** |
| Actions enabled on repo | **Yes** (`enabled: true`, `allowed_actions: all`) |
| Existing workflows | **0** |
| Branch protection / secrets for render | Not configured for render bridge |
| Automation conventions | None for KSB render |

Actions is a **viable platform candidate**, not an implemented bridge.

---

## 4. Renderer-side discovery

| Item | Value |
|---|---|
| Path | `Engineering-Office/publication/weekly-status/renderer/` |
| Version | `1.0.0-CWC-CE-084` |
| Language | Python 3 |
| Dependencies | Pillow (`PIL`), OpenCV (`cv2`), NumPy |
| Font | **Windows** `C:\Windows\Fonts\arialbd.ttf` (Arial Bold) — hard requirement in `regions.json` / `render.py` |
| Baseline | `BL-WEEKLY-STATUS-BASELINE-v1.0.png` SHA `17F574D4…` |
| Input | exactly `status_date`, `bill_a_percent`, `bill_b_percent`, `bill_c_percent` |
| Anti-drift | unauthorized changed pixels = 0; dims 1536×912 |
| Local tests | **19 / 19 PASS** (this continuation re-verified contract subset) |

### Font / environment determinism (mandatory)

Moving execution to a typical **GitHub-hosted Linux runner** without the authorized Windows Arial Bold font will:

1. fail closed (font missing), **or**  
2. if a different font were substituted without authority, alter glyph metrics / pixels / SHA-256.

**Therefore:** a Linux hosted-runner bridge is **not** determinism-safe under current renderer authority without a separate Human-authorized font/environment control (and Arial redistribution is a licensing constraint).

**Preferred candidate runner for byte-identity continuity:** Windows self-hosted runner (or other environment proven to produce identical SHA to the accepted local Windows renderer).

---

## 5. Rejected / deferred alternatives

| Alternative | Disposition | Why |
|---|---|---|
| Generative / creative KSB image | **REJECTED** | Absolute firewall (STD-011 §36.5 / KSB-ORCH-001) |
| HTML/CSS “similar” renderer | **REJECTED** | Replaces rendering authority |
| ChatGPT auto-commit render request to `main` to trigger Actions | **REJECTED** | Bypasses HG-4/HG-5 Git gates; race/loop risk |
| Manual “open Cursor and run Python” as ordinary Sunday path | **REJECTED as final bridge** | Violates phone-first requirement |
| Public unauthenticated HTTP render API | **REJECTED** | Unacceptable attack surface |
| External cloud service | **DEFERRED** | Needs Human auth; cost/auth/ops; not smallest until Actions path decided |

---

## 6. Selected candidate architecture (NOT IMPLEMENTED)

**Identity:** `KSB-RENDER-BRIDGE — GitHub Actions + controlled dispatch + Windows-deterministic runner`

```text
PHONE HUMAN
 → ChatGPT Prepare KSB Status
 → (certification if required; context persists)
 → ChatGPT prepares status + press release locally in conversation
 → CONTROLLED RENDER REQUEST (four variables only)
 → AUTHORIZED DISPATCH (workflow_dispatch / verified Custom GPT Action — TBD)
 → Actions runner (Windows self-hosted preferred)
 → checkout pinned canonical SHA
 → verify baseline SHA
 → execute existing ksb_renderer
 → anti-drift PASS
 → upload Actions artifact + machine-readable RESULT.json
 → ChatGPT retrieves artifact reference / completion state
 → PACKAGE COMPLETE (if all deliverables ready)
 → HUMAN REVIEW/PUBLICATION REQUIRED
```

### Trigger mechanism

| Layer | State |
|---|---|
| GitHub `workflow_dispatch` | Platform-available; **no workflow exists**; ChatGPT invocation **UNVERIFIED** |
| Custom GPT Action → GitHub API | **REQUIRES ADDITIONAL INTEGRATION** + Human secrets/auth design |
| Repository file write as trigger | **REJECTED** for ordinary auto-commit to protected history |

```text
TRIGGER BRIDGE: UNRESOLVED
```

### Authentication / least privilege (target)

- Fine-grained credential permitting only `actions: write` (dispatch) + `actions: read` (artifacts) on this repo — not admin.  
- No public unauthenticated endpoint.  
- Render request validated: four keys only; integer percents 0–100; ISO date; reject path/shell injection.

### Request identity (proposed)

```text
KSB-RENDER-<YYYY-MM-DD>-<NNN>
```

Fields: status_date, bill_a/b/c_percent, baseline_id/sha, renderer_version, canonical_sha, request_id, requesting_cycle_id.

### Idempotency

Same `(status_date, A, B, C, baseline_sha, renderer_version, canonical_sha)` → return prior successful artifact; do not mint conflicting authoritative images. Changed inputs → new request id.

### Artifact return

Actions artifact (private to workflow run) + RESULT.json readable via API; optional later promotion into `images/` only under Human Git gates. Temporary ≠ canonical publication artifact.

### Failure states (preserve package INCOMPLETE)

`BRIDGE UNAVAILABLE` · `AUTHORIZATION FAILED` · `INVALID INPUT` · `BASELINE HASH MISMATCH` · `RENDERER VERSION MISMATCH` · `DEPENDENCY FAILURE` · `FONT/ENVIRONMENT MISMATCH` · `RENDER FAILED` · `ANTI-DRIFT FAILED` · `ARTIFACT UPLOAD FAILED` · `ARTIFACT RETRIEVAL FAILED` · `TIMEOUT` · `UNKNOWN FAILURE`

All map to:

```text
KSB IMAGE: RENDER REQUIRED
PACKAGE STATE: INCOMPLETE
```

No creative recovery.

---

## 7. Local POC results (engineering; not phone E2E)

| Test | Result |
|---|---|
| 1 Capability discovery | **PASS** (classified; not assumed) |
| 2 Authorized input | **PASS** |
| 3 Unauthorized fifth field | **PASS** (reject) |
| 4 Baseline verification | **PASS** (hash match; mismatch would fail closed in renderer) |
| 5 Determinism | **PASS** on local Windows (renderer suite 19/19; double-render SHA identity) |
| 6 Anti-drift | **PASS** (renderer suite) |
| 7 Failure-safe / no creative | **PASS** (rule application; STD-011 §36.5) |
| 8 Artifact retrieval | **NOT YET IMPLEMENTABLE** (no bridge) |
| 9 Human publication gate | **PASS** (control preserves STOP) |
| 10 End-to-end bridge POC | **PARTIAL — TRIGGER BOUNDARY UNRESOLVED** |

---

## 8. Cost / latency (estimate)

| Metric | Class |
|---|---|
| Cost | **ZERO/INCLUDED** if using included Actions minutes + self-hosted idle machine; **UNKNOWN** if paid runners |
| Latency | **UNKNOWN** until POC; local render is seconds; Actions queue + checkout likely tens of seconds to minutes |

---

## 9. Remaining runtime gap (exact)

1. **ChatGPT→authenticated render trigger** unverified (LIVE CHATGPT PROOF REQUIRED — KSB-TRIGGER-RETURN-001).  
2. **ChatGPT←artifact/result retrieval** unverified (same).  
3. **No Actions workflow implemented** (and none may be added under this capability-proof continuation).  
4. **Font/environment:** current renderer requires Windows `arialbd.ttf`; runner selection **deferred**.  
5. ChatGPT **write-to-main as trigger** conflicts with existing Git Human gates (REJECTED).

Until closed: ordinary phone package remains:

```text
KSB IMAGE: RENDER REQUIRED
PACKAGE STATE: INCOMPLETE
```

when the deterministic renderer cannot execute in-channel.

---

## 10. Authority decision

Bridge implementation is **NOT** already fully authorized by existing controls.

**ECR-009 remains Proposed (0.2.0)** — MODIFY-before-ACCEPT recommendation:

- live ChatGPT trigger/return proof gate;  
- controlled render-request schema;  
- Actions (or equivalent) execution bridge **only if proven**;  
- runner/font determinism rules (selection deferred);  
- artifact-return / temporary-vs-canonical rules;  
- least-privilege auth;  
- explicit prohibition on creative recovery and Git-gate bypass.

Do **not** self-accept ECR-009. Do **not** deploy workflow/runner until proof + Human ACCEPT.

---

## 11. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-30 | CWC-CE-088 runtime-bridge discovery; Outcome C trigger gap; ECR-009 Proposed. |
| 1.1.0 | 2026-08-30 | Aligned to KSB-TRIGGER-RETURN-001 / ECR-009 0.2.0; trigger/return = LIVE CHATGPT PROOF REQUIRED. |
