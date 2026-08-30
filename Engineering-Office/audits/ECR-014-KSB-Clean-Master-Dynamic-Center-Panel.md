# ECR-014 — KSB Clean Master Template and Dynamic Center-Panel Composition

**Document ID:** ECR-014  
**Title:** Clean Master Template Integration / Dynamic Kansas Legislative Engineering Status Panel  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-011 Part B; KSB-ORCH-001  
**Governing Work Card:** **CWC-CE-097**  
**Predecessor:** ECR-013; CWC-CE-096 (technical Outcome A; **Human visual REJECTED**)  
**Status:** **HUMAN VISUALLY ACCEPTED** (candidate PNG) — **CANONICALIZED under CWC-CE-098**  
**Version:** **1.0.0**  
**Effective Date:** 2026-08-30  
**Preparing Agent:** CE-Engineer  
**Canonicalization Agent:** CE-GitManager (CWC-CE-098)  

```text
HUMAN VISUAL ACCEPTANCE = ACCEPT (CWC-CE-098)
HUMAN-APPROVED ARCHITECTURE (CWC-CE-097):
CLEAN MASTER TEMPLATE (blank center status panel)
→ COPY / OPEN FRESH
→ DRAW CURRENT CENTER-PANEL CONTENT
→ NEW PNG

CWC-CE-096 FIXED-LAYER ORDINARY PATH = SUPERSEDED (not activated)
OPERATIONAL RENDERER ID: ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE
```

---

## 1. Defects / dispositions

| ID | Disposition |
|---|---|
| KSB-RENDER-002 | Remediating via clean-master architecture (not plate-over / not full fixed-layer paste) |
| CWC-CE-096 Human visual | **REJECTED** — fixed-layer paste produced white plate artifacts; architecture superseded |

---

## 2. Authorized changes

1. Ordinary render input = immutable clean master `BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE` (1536×1024).  
2. Dynamically compose full Kansas Legislative Engineering Status center panel each render.  
3. Controlled center content in `renderer/center_content.json`.  
4. `regions.json` redesigned for clean-template geometry (supersedes CE-096 plate/fixed-layer assumptions).  
5. CE-096 `FIXED-LAYER-v1.0-CWC-CE-096` retained as historical evidence; prohibited as ordinary input.  
6. Baseline v1.0 remains historical visual reference only.  
7. Candidate renderer `ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE`.  
8. Amend STD-011 / KSB-ORCH for clean-master ordinary path (ECR-013 blank-canvas fixed-layer model superseded for ordinary activation).

---

## 3. Non-goals

No generative image · no maturity change · no live Issue · no push/publication · no silent date/breadcrumb edits.

---

## 4. Template identity

| Item | Value |
|---|---|
| Controlled ID | `BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE` |
| Path | `templates/BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE.png` |
| SHA-256 | `01C29A8A20CA4D1798E4A407431B0A7FA1BD58F798D5837AD2A1CC1BF9E1D05C` |
| Dimensions | 1536 × 1024 |
| Human source | Byte-identical to provided `BL-Weekly-Status-Template-v1.0.png` |

---

## 5. Activation gate

Human visual ACCEPT recorded under CWC-CE-098 for candidate:

`CANDIDATE-CWC-CE-097-CLEAN-TEMPLATE-19-19-4.png`  
SHA-256: `78D5E2E1CA11078106DC4585867651915490E2B8745B7E2A08CDB3D303A111DD`

Git canonicalization authorized. Date / stale-breadcrumb template issues remain separate.
