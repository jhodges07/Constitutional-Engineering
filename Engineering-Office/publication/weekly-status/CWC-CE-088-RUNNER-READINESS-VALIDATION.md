# CWC-CE-088 — Isolated Windows Runner / Remote-POC Readiness Validation

**Document ID:** CWC-CE-088-RUNNER-READINESS-VALIDATION  
**Governing Work Card:** CWC-CE-088 Bounded Isolated Windows Runner Provisioning and Remote-POC Readiness Continuation  
**Preparing Agent:** CE-Engineer  
**Date:** 2026-08-30  
**Predecessor:** `4aeaf60b330ad41b5750ce523ad850a75325aa78`  

---

## A–CN Validation Report

| ID | Item | Result |
|---|---|---|
| A | Outcome | **B** |
| B | Agent identity | CE-Engineer |
| C | Repository root | `X:\GitHub\Constitutional-Engineering` |
| D | Repository identity | `jhodges07/Constitutional-Engineering` |
| E | Branch | `main` |
| F | Local HEAD | `4aeaf60b330ad41b5750ce523ad850a75325aa78` |
| G | origin/main | `4aeaf60b330ad41b5750ce523ad850a75325aa78` |
| H | Canonical predecessor relationship | **MATCHED** |
| I | Staged inventory | **EMPTY** |
| J | Modified inventory | Prior CWC-088 dirty set preserved |
| K | Untracked inventory | Bridge package + handoff docs + prior CWC-088 |
| L | Unrelated Human work preserved? | **YES** |
| M | ECR-009 state | v0.3.0 HUMAN ACCEPTED / IMPLEMENTED LOCALLY |
| N | Issue bridge state | IMPLEMENTED LOCALLY — intact |
| O | Gate test result | **19/19 PASS** (re-run) |
| P | Renderer regression | **19/19 PASS** (re-run) |
| Q | Anti-drift regression | **PASS** (suite) |
| R | Workflow path | `.github/workflows/ksb-render-bridge.yml` |
| S | Workflow trigger | `issues: [opened]` only |
| T | Workflow permissions | `contents: read`, `issues: write` |
| U | Gate runner | `ubuntu-latest` |
| V | Render runner labels | `self-hosted`, `Windows`, `ksb-render-windows` |
| W | Human workstation excluded? | **YES** |
| X | Isolated Windows environment available? | **NO** |
| Y | Isolation mechanism | Dedicated Windows VM (Human to provision) |
| Z | Windows version | Spec: Win10/11 or Server 2019+ x64 |
| AA | CPU requirement | ≥2 vCPU |
| AB | RAM requirement | ≥4 GB (8 preferred) |
| AC | Storage requirement | ≥40 GB free |
| AD | Python version | Render candidate **3.12.10**; gate job 3.11 |
| AE | Pillow version | **12.3.0** (lock candidate) |
| AF | OpenCV version | **5.0.0** (lock candidate) |
| AG | Git version/requirement | Git for Windows (current stable) |
| AH | Font availability | Required `C:\Windows\Fonts\arialbd.ttf` on VM; **not** committed |
| AI | Font identity verification | VM must verify path exists; no font binary in Git |
| AJ | Runner software requirement | Official GitHub Actions Windows x64 runner |
| AK | Runner identity | `KSB-RENDER-WIN-01` (suggested) |
| AL | Runner scope | Repository-scoped preferred |
| AM | Runner account | Dedicated low-privilege Windows user |
| AN | Network requirements | Outbound HTTPS to GitHub Actions only |
| AO | Inbound ports required? | **NO** |
| AP | Secret handling | No secrets in Git; registration token ephemeral |
| AQ | Registration token required? | **YES** (Human obtains at registration) |
| AR | Human registration action required? | **YES** |
| AS | AUTHORIZED_KSB_RENDER_ACTORS state | **HUMAN ACTION REQUIRED** (repo vars count 0) |
| AT | Initial authorized actor | `jhodges07` |
| AU | ALLOWED_KSB_CANONICAL_SHAS state | **READY AFTER GIT** / HUMAN ACTION REQUIRED |
| AV | SHA bootstrap sequence | Documented in GIT-HANDOFF-MANIFEST §2 — **PASS** |
| AW | Workflow security review | **PASS** (Issue data → gate only; Windows needs authorized=true; pinned checkout; no PR/fork) |
| AX | Public copied-Issue result | REJECT (local gate re-run) |
| AY | Unauthorized actor result | REJECT |
| AZ | Hostile-input result | REJECT |
| BA | Four-variable firewall | **PASS** |
| BB | Fifth-field rejection | **PASS** |
| BC | Canonical SHA binding | **PASS** |
| BD | Baseline verification | **PASS** |
| BE | Renderer binding | **PASS** |
| BF | Isolated deterministic fixture result | **HUMAN PROVISIONING REQUIRED** |
| BG | Isolated deterministic SHA run 1 | N/A |
| BH | Isolated deterministic SHA run 2 | N/A |
| BI | Historical fixture comparison | Local suite still `758AFA76…` — not claimed for VM |
| BJ | Isolated anti-drift result | **HUMAN PROVISIONING REQUIRED** |
| BK | Unauthorized changed regions | N/A on VM; local suite unauthorized=0 on PASS cases |
| BL | Human admin instructions path | `issue-bridge/HUMAN-PROVISIONING-STEPS.md` |
| BM | Git handoff manifest path | `issue-bridge/GIT-HANDOFF-MANIFEST.md` |
| BN | Exact proposed Git package | See handoff manifest §3 |
| BO | Files staged | **NONE** |
| BP | Commits | **NONE** |
| BQ | Pushes | **NONE** |
| BR | Workflow deployed? | **NO** |
| BS | Runner registered? | **NO** |
| BT | Runner online? | **NO** |
| BU | Actions variables configured? | **NO** |
| BV | Remote POC Issue created? | **NO** |
| BW | Remote POC performed? | **NO** |
| BX | Real artifact created? | **NO** (Actions) |
| BY | ChatGPT artifact return proof? | **NO** — EXPOSED / REAL-RUN PENDING |
| BZ | Final phone POC performed? | **NO** |
| CA | Publication performed? | **NO** |
| CB | KSB maturity | 19 / 19 / 4 |
| CC | Maturity changed? | **NO** |
| CD | CWC-CE-086 changed? | **NO** |
| CE | HG-D1 changed? | **NO** |
| CF | HG-PR changed? | **NO** |
| CG | Candidate outreach? | **NO** |
| CH | Tests PASS/PARTIAL/FAIL | Local PASS; isolated PENDING |
| CI | First remaining Human gate | **ISOLATED WINDOWS RUNNER: HUMAN PROVISIONING REQUIRED** |
| CJ | Exact Human action required | Create dedicated Windows VM per HUMAN-PROVISIONING-STEPS.md |
| CK | Git integration readiness | **READY** for CE-GitManager after Human Git authority (package prepared) |
| CL | Recommended next continuation | Human provisions VM; optionally authorize CE-GitManager in parallel for package push |
| CM | Recommended next Cursor AI agent | After VM: **CE-Engineer**; for Git: **CE-GitManager** |
| CN | Final STOP confirmation | **STOP** |

---

## Workflow security review (summary)

| Control | Status |
|---|---|
| Trigger only `issues:opened` | PASS |
| No push/PR/schedule/dispatch | PASS |
| Gate on `ubuntu-latest` before Windows | PASS |
| `render` `needs: gate` + `authorized == true` | PASS |
| Labels include `ksb-render-windows` | PASS |
| `contents: read` only | PASS |
| Issue body not used as shell/script path | PASS (normalized JSON only) |
| Checkout of Issue author fork/PR | Not present — PASS |
| Unauthorized public Issue schedules Windows | Blocked at gate — PASS |

---

## Controlled state preserved

```text
KSB IMAGE: RENDER REQUIRED
PACKAGE STATE: INCOMPLETE
ARTIFACT RETURN: EXPOSED — REAL-RUN PROOF PENDING
```
