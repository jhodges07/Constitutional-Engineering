# ECR-011 — KSB Three-Step Human Command Contract

**Document ID:** ECR-011  
**Title:** KSB Three-Step Human Command Contract (Status → Press Release → Controlled Image)  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-011 Part B (§36); KSB-ORCH-001  
**Governing Work Card:** **CWC-CE-092**  
**Predecessor:** ECR-008; ECR-009; ECR-010 (D01 parked; D02 remediated); CWC-CE-088; CWC-CE-089; CWC-CE-090  
**Status:** **HUMAN ACCEPTED** (source: CWC-CE-092 Human Engineer concurrence)  
**Version:** **1.0.0**  
**Effective Date:** 2026-08-30 (local implementation under CWC-CE-092; Git canonicalization pending)  
**Primary Category:** PUB  
**Secondary Categories:** STD, ADM  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  

```text
HUMAN ACCEPTED — CWC-CE-092
THREE-STEP COMMAND CONTRACT
Prepare KSB Status → STATUS
Next → PRESS RELEASE
Next → CONTROLLED IMAGE
KSB-089-D01: SUPERSEDED by this Human-selected model
NO PUBLICATION
NO MATURITY / BASELINE / RENDERER CHANGE
NO LIVE RENDER UNDER THIS ECR IMPLEMENTATION
```

---

## 1. Problem

Predecessor orchestration (ECR-008 / STD-011 §36.9–§36.10) bound `Prepare KSB Status` to returning the complete Sunday package in one interaction. Hosted image execution is asynchronous and outlives a ChatGPT turn (KSB-089-D01). Forcing status + press release + image into one command made ordinary Sundays brittle and over-coupled image plumbing to Human conversation.

---

## 2. Authorized change

Human-facing products advance **one boundary per command**:

| Step | Human command | Product returned | Render Issue |
|---|---|---|---|
| 1 | `Prepare KSB Status` | Controlled KSB **STATUS** only | **MUST NOT** create |
| 2 | `Next` (status complete; PR incomplete) | ≈500-word **PRESS RELEASE** | **MUST NOT** create |
| 3 | `Next` (PR complete; image incomplete) | **CONTROLLED IMAGE** path | At most **one** request for the package |

Package COMPLETE (all three products) remains required before Human review/publication readiness. Publication remains a separate Human gate.

**KSB-089-D01 disposition:** **SUPERSEDED** by this three-step model (not the parked “Continue KSB Status” design).

---

## 3. Non-goals

No baseline/renderer/fixture/maturity change · no publication · no bill release · no candidate contact · no new live hosted test under this ECR’s implementation CWC · no generative image substitution.

---

## 4. Implementation package

| Artifact | Action |
|---|---|
| STD-011 | → **1.6.0** §36.11 three-step; amend §36.1 / §36.10 relationship |
| KSB-ORCH-001 | → **1.2.0** operator procedure |
| Operator card | Align to three-step |
| Orchestration state machine + tests | Local deterministic |

---

## 5. Disposition

| Field | Value |
|---|---|
| Disposition | **HUMAN ACCEPTED** via CWC-CE-092 |
| Git | Pending CE-GitManager after local validation |
