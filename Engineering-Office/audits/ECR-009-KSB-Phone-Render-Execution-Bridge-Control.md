# ECR-009 — KSB Phone-to-Deterministic-Render Execution Bridge Control

**Document ID:** ECR-009  
**Title:** KSB Phone Render Execution Bridge  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-011 Part B (§36 / §36.9); KSB-ORCH-001  
**Governing Work Card:** CWC-CE-088 Bounded Implementation Execution / Stale-State Correction  
**Predecessor:** ECR-008; CWC-CE-084; CWC-CE-074; KSB-TRIGGER-RETURN-001; KSB-ISSUE-BRIDGE-001  
**Related Architecture:** KSB-ISSUE-BRIDGE-001; KSB-RENDER-BRIDGE-001; KSB-TRIGGER-RETURN-001  
**Status:** Implemented  
**Disposition:** HUMAN ACCEPTED — LOCALLY IMPLEMENTED UNDER CWC-CE-088 (Git canonicalization / remote Actions / isolated runner pending separate Human gates)  
**Implementation State:** IMPLEMENTED LOCALLY — Issue-bridge gate/schema/RESULT/workflow prepared; local security tests; renderer regression; remote real-run pending Human infrastructure + Git gates  
**Operative Authority:** Locally Active for implementation package (not yet executable on GitHub until Human Git + runner + variable gates)  
**Version:** 0.3.0  
**Effective Date:** 2026-08-30  
**Primary Category:** PUB  
**Secondary Categories:** STD, ADM, SEC  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  
**Acceptance Recording Agent:** CE-Engineer  
**Implementation Agent:** CE-Engineer  

```text
HUMAN ACCEPTED
APPROVED FOR CONTROL IMPLEMENTATION
IMPLEMENTED LOCALLY UNDER CWC-CE-088
STALE PRIOR "PROPOSED — READY FOR HUMAN DECISION" REPORT: SUPERSEDED
ISSUE-TRIGGER ARCHITECTURE: AUTHORITATIVE
WORKFLOW_DISPATCH: NOT EXPOSED / NOT REQUIRED
ISOLATED WINDOWS RUNNER: REQUIRED (HUMAN WORKSTATION PROHIBITED)
NO MATURITY CHANGE (19/19/4)
NO CWC-CE-086 CHANGE
NO GIT ADVANCEMENT — NOT CANONICAL ON origin/main UNTIL HUMAN GIT GATES
NO REMOTE ACTIONS EXECUTION UNTIL HUMAN GIT + RUNNER + VARIABLE GATES
NO PUBLICATION
NO FINAL LIVE KSB PHONE POC CLAIMED
```

---

## 0. Human acceptance record

| Field | Value |
|---|---|
| Accepted version | **0.3.0** |
| Human disposition | **ACCEPT** (“I concur.” — confirmed as ECR-009 v0.3.0 ACCEPT) |
| Acceptance date | 2026-08-30 |
| Architecture changed by acceptance? | **No** — acceptance state only; substantive Issue-trigger controls unchanged |
| Next gates | Isolated Windows runner provisioning; GitHub Actions variables; runner registration; Git deploy of workflow |

Silence ≠ ACCEPT. This record documents an explicit Human ACCEPT already given.

---

## 1. Problem (unchanged substantive)

ECR-008 / STD-011 1.5.0 require a complete KSB Sunday Publication Package from `Prepare KSB Status`, including the controlled deterministic image. ChatGPT cannot run the local Python renderer in-channel. Direct Actions dispatch is not exposed. ChatGPT can create/close Issues and inspect Actions runs/artifacts.

---

## 2. Authorized architecture (accepted)

```text
ChatGPT → controlled [KSB-RENDER] Issue
 → Actions issues:opened
 → GitHub-hosted gate (auth + schema)
 → isolated Windows render job
 → existing ksb_renderer @ pinned canonical_sha
 → PNG + RESULT.json artifact
 → Issue comment correlation
 → ChatGPT retrieves artifact
 → Human review (no auto-publication)
```

Mandatory verified-capability statements remain as in 0.3.0-PROPOSED (Issue write verified; dispatch not exposed/not required; artifact APIs exposed; real-run pending).

Security-critical controls remain mandatory: actor allowlist + author_association; two-job gate/render; pinned SHA; four-variable firewall; isolated runner (not Human workstation); RESULT↔PNG reconciliation; no main-branch trigger; no creative recovery.

---

## 3. Local implementation package (this CWC)

| Component | Path |
|---|---|
| Gate / schema / RESULT | `Engineering-Office/publication/weekly-status/issue-bridge/` |
| Workflow (local) | `.github/workflows/ksb-render-bridge.yml` |
| Runner specification | `…/issue-bridge/ISOLATED-WINDOWS-RUNNER-SPEC.md` |
| Human admin gate | `…/issue-bridge/HUMAN-ADMIN-GATE.md` |

Remote execution requires separate Human gates (Git deploy, variables, isolated runner). Local implementation does **not** equal remote PASS.

---

## 4. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0-PROPOSED | 2026-08-30 | Runtime-bridge discovery. |
| 0.2.0-PROPOSED | 2026-08-30 | Live ChatGPT proof gate. |
| 0.3.0-PROPOSED | 2026-08-30 | Issue-trigger architecture. |
| 0.3.0 | 2026-08-30 | **HUMAN ACCEPTED**; local implementation under CWC-CE-088; version unchanged (acceptance ≠ new ECR revision). |
