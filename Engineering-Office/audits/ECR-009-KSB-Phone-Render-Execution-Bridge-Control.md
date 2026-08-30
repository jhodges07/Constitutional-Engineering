# ECR-009 — KSB Phone-to-Deterministic-Render Execution Bridge Control

**Document ID:** ECR-009  
**Title:** KSB Phone Render Execution Bridge  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-011 Part B (§36 / §36.9); KSB-ORCH-001  
**Governing Work Card:** CWC-CE-088 GitHub-Hosted Windows POC Acceleration Continuation  
**Predecessor:** ECR-008; CWC-CE-084; CWC-CE-074; KSB-TRIGGER-RETURN-001; KSB-ISSUE-BRIDGE-001  
**Related Architecture:** KSB-ISSUE-BRIDGE-001; KSB-RENDER-BRIDGE-001; KSB-TRIGGER-RETURN-001  
**Status:** Implemented  
**Disposition:** HUMAN ACCEPTED — GIT CANONICAL (0.3.0) + HOSTED-WINDOWS NON-PRODUCTION POC PATH AUTHORIZED UNDER CWC-CE-088 (this revision pending Git handoff)  
**Implementation State:** Issue-bridge canonical at `20fc998…`; hosted-Windows workflow change prepared locally for NON-PRODUCTION POC  
**Operative Authority:** Hosted-Windows POC path authorized by Human Engineer direction (CWC-CE-088 acceleration); Git canonicalization of this revision pending CE-GitManager  
**Version:** 0.3.1  
**Effective Date:** 2026-08-30  
**Primary Category:** PUB  
**Secondary Categories:** STD, ADM, SEC  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  

```text
HUMAN ACCEPTED (0.3.0 architecture)
0.3.1 — HOSTED WINDOWS NON-PRODUCTION POC PATH (Human-directed acceleration)
SELF-HOSTED ISOLATED VM: FALLBACK / FUTURE DEPLOYMENT MODEL (not required for current POC)
HUMAN WORKSTATION AS RUNNER: PROHIBITED
NO MATURITY CHANGE (19/19/4)
NO CWC-CE-086 CHANGE
NO PUBLICATION AUTHORITY FROM HOSTED EXECUTION
HOSTED DETERMINISM: REAL-RUN PROOF PENDING UNTIL PHONE/CHATGPT POC
```

---

## 0. Human acceptance / acceleration record

| Field | Value |
|---|---|
| Accepted architecture | **0.3.0** Issue-trigger bridge |
| Acceleration disposition | Human directs: **do not wait for local Windows VM**; use GitHub-hosted Windows for NON-PRODUCTION POC |
| Revision | **0.3.1** — execution-host authority only; authorization/SHA/baseline/renderer/anti-drift unchanged |

---

## 1. Problem (unchanged substantive)

ECR-008 / STD-011 1.5.0 require a complete KSB Sunday Publication Package from `Prepare KSB Status`, including the controlled deterministic image. ChatGPT cannot run the local Python renderer in-channel.

---

## 2. Authorized architecture

```text
ChatGPT → controlled [KSB-RENDER] Issue
 → Actions issues:opened
 → GitHub-hosted gate (auth + schema)  [ubuntu-latest]
 → Windows render job
      NON-PRODUCTION POC: GitHub-hosted windows-2022
      FALLBACK / FUTURE: self-hosted [self-hosted, Windows, ksb-render-windows]
 → existing ksb_renderer @ pinned canonical_sha
 → PNG + RESULT.json artifact
 → Issue comment correlation
 → ChatGPT retrieves artifact
 → Human review (no auto-publication)
```

### 2.1 Execution host (0.3.1)

| Host | Authority |
|---|---|
| GitHub-hosted `windows-2022` | **Authorized for NON-PRODUCTION KSB bridge POC** after workflow Git integration + SHA allowlist update + real-run certification |
| Self-hosted `ksb-render-windows` | Remains valid **fallback / future** deployment model; not required for current POC path |
| Human daily-driver workstation | **PROHIBITED** |

Hosted execution MUST pass deterministic / anti-drift / font / baseline evidence on the real run before being treated as certified. Local tests ≠ hosted certification.

Security-critical controls remain mandatory: actor allowlist + author_association; two-job gate/render; pinned SHA; four-variable firewall; RESULT↔PNG reconciliation; no main-branch trigger; no creative recovery; no publication from bridge success.

---

## 3. Implementation package

| Component | Path |
|---|---|
| Gate / schema / RESULT | `Engineering-Office/publication/weekly-status/issue-bridge/` |
| Workflow | `.github/workflows/ksb-render-bridge.yml` |
| Self-hosted provisioning (fallback) | `…/issue-bridge/HUMAN-PROVISIONING-STEPS.md` |

---

## 4. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0-PROPOSED | 2026-08-30 | Runtime-bridge discovery. |
| 0.2.0-PROPOSED | 2026-08-30 | Live ChatGPT proof gate. |
| 0.3.0-PROPOSED | 2026-08-30 | Issue-trigger architecture. |
| 0.3.0 | 2026-08-30 | HUMAN ACCEPTED; Git-integrated at `20fc998…`. |
| 0.3.1 | 2026-08-30 | GitHub-hosted Windows NON-PRODUCTION POC path; self-hosted remains fallback; Human workstation still prohibited. |
