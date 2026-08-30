# ECR-009 — KSB Phone-to-Deterministic-Render Execution Bridge Control

**Document ID:** ECR-009  
**Title:** KSB Phone Render Execution Bridge  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-011 Part B (§36 / §36.9); KSB-ORCH-001  
**Governing Work Card:** CWC-CE-088 Live Acceptance-Test Defect Remediation  
**Predecessor:** ECR-008; CWC-CE-084; CWC-CE-074; KSB-TRIGGER-RETURN-001; KSB-ISSUE-BRIDGE-001  
**Related Architecture:** KSB-ISSUE-BRIDGE-001; KSB-RENDER-BRIDGE-001; KSB-TRIGGER-RETURN-001  
**Related Failure:** KSB-POC-FAIL-002  
**Status:** Implemented  
**Disposition:** HUMAN ACCEPTED — GIT CANONICAL (0.3.0) + HOSTED-WINDOWS NON-PRODUCTION POC PATH (0.3.1) + DEPENDENCY PIN CORRECTION (this revision pending Git handoff)  
**Implementation State:** Issue-bridge + hosted-Windows path at `9e7f5b40…` failed Test #1 on invalid OpenCV pin; active pin corrected to `opencv-python==5.0.0.93` under CWC-CE-088  
**Operative Authority:** Hosted-Windows POC path authorized; OpenCV pin correction evidence-backed (PyPI / Test #1); Git canonicalization pending CE-GitManager  
**Version:** 0.3.2  
**Effective Date:** 2026-08-30  
**Primary Category:** PUB  
**Secondary Categories:** STD, ADM, SEC  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  

```text
HUMAN ACCEPTED (0.3.0 architecture)
0.3.1 — HOSTED WINDOWS NON-PRODUCTION POC PATH
0.3.2 — OPENCV PIN CORRECTION (opencv-python==5.0.0.93)
TEST #1 FAIL RECORDED (KSB-POC-FAIL-002) — DO NOT ERASE
SELF-HOSTED ISOLATED VM: FALLBACK / FUTURE DEPLOYMENT MODEL
HUMAN WORKSTATION AS RUNNER: PROHIBITED
NO MATURITY CHANGE (19/19/4)
NO CWC-CE-086 CHANGE
NO PUBLICATION AUTHORITY FROM HOSTED EXECUTION
```

---

## 0. Human acceptance / acceleration record

| Field | Value |
|---|---|
| Accepted architecture | **0.3.0** Issue-trigger bridge |
| Acceleration disposition | Human directs: **do not wait for local Windows VM**; use GitHub-hosted Windows for NON-PRODUCTION POC |
| Revision | **0.3.1** — execution-host authority only; authorization/SHA/baseline/renderer/anti-drift unchanged |
| Defect remediation | **0.3.2** — active OpenCV pin `opencv-python==5.0.0.93` (Test #1: `==5.0.0` no matching distribution); see `issue-bridge/DEPENDENCIES.md` |

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
| Active dependency lock | `…/issue-bridge/DEPENDENCIES.md` (`opencv-python==5.0.0.93`) |
| Workflow | `.github/workflows/ksb-render-bridge.yml` |
| Self-hosted provisioning (fallback) | `…/issue-bridge/HUMAN-PROVISIONING-STEPS.md` |
| Acceptance Test #1 FAIL record | `…/weekly-status/KSB-POC-FAIL-002-Acceptance-Test-1.md` |

---

## 4. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0-PROPOSED | 2026-08-30 | Runtime-bridge discovery. |
| 0.2.0-PROPOSED | 2026-08-30 | Live ChatGPT proof gate. |
| 0.3.0-PROPOSED | 2026-08-30 | Issue-trigger architecture. |
| 0.3.0 | 2026-08-30 | HUMAN ACCEPTED; Git-integrated at `20fc998…`. |
| 0.3.1 | 2026-08-30 | GitHub-hosted Windows NON-PRODUCTION POC path; self-hosted remains fallback; Human workstation still prohibited. |
| 0.3.2 | 2026-08-30 | Correct active OpenCV pin to `opencv-python==5.0.0.93` after Test #1 FAIL (`==5.0.0` unresolved); KSB-POC-FAIL-002 recorded. |
