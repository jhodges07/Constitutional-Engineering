# ECR-015 — KSB Public-Image Cleanup (Date / Breadcrumb / Template Metadata)

**Document ID:** ECR-015  
**Title:** Public-Image Cleanup — Dynamic STATUS_DATE / Stable GitHub Breadcrumb / Remove Engineering Metadata Strip  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-011 Part B §§25 / 25A  
**Governing Work Card:** **CWC-CE-107**  
**Canonicalization Work Card:** **CWC-CE-108**  
**Hosted Acceptance Work Cards:** **CWC-CE-109** / **CWC-CE-110**  
**Predecessor:** ECR-014 / CWC-CE-097–106 (hosted-render POC COMPLETE)  
**Status:** **HUMAN-ACCEPTED** (local + hosted) — **HOSTED ACCEPTANCE SATISFIED** (CWC-CE-109/110)  
**Version:** **1.0.0**  
**Effective Date:** 2026-08-30  
**Preparing Agent:** CE-Engineer  
**Canonicalization Agent:** CE-GitManager (CWC-CE-108; hosted closure CWC-CE-110)  

```text
LOCAL HUMAN VISUAL ACCEPTANCE = ACCEPT (CWC-CE-107 / CWC-CE-108)
HOSTED ACCEPTANCE RENDER = PASS (CWC-CE-109)
HOSTED HUMAN VISUAL ACCEPTANCE = ACCEPT (CWC-CE-110; "I concur.")
PUBLIC-IMAGE CLEANUP ACCEPTANCE CYCLE = COMPLETE
PUBLICATION = NOT AUTHORIZED
HOSTED-RENDER POC = COMPLETE (unchanged)
ORCH IDENTITY SYNC = OPEN (separate CWC-CE-111)
```

---

## 1. Problem

The CE-097 clean master (`…-v1.0-CANDIDATE`, 1536×1024) baked:

1. Static `Date: 2026.08.35` + non-compliant `(Week 35 of 2026)`  
2. Stale breadcrumb leaf `Live 2026.10.05 Report (Files)`  
3. Engineering metadata strip below the navy footer (local template path / date-explanation)

STD-011 §25 / §25A require compact dynamic date, no engineering metadata on the public image, and a thin GitHub breadcrumb without stale weekly dates.

---

## 2. Authorized changes (accepted)

1. Successor clean master `BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE` (1536×912) — do **not** overwrite v1.0.  
2. Crop remove engineering metadata below public footer.  
3. Blank baked date region; draw `Date: {yyyy.mm.ww}` dynamically from `status_date`.  
4. Replace stale dated breadcrumb leaf with FIXED `Report Files` (no weekly date).  
5. Preserve Minimum URL Pattern HTTPS public-navigation line.  
6. Expand anti-drift authorized rects to include STATUS_DATE.  
7. Candidate renderer `ksb_renderer@2.1.0-CWC-CE-107-CANDIDATE`.  

---

## 3. Non-goals

No maturity change · no hosted Issue under CE-107/108 · no publication · no baseline_id semantic change · no Telea/plate-over · no redesign of header/side panels/center/footer branding.

---

## 4. Identities

| Item | Value |
|---|---|
| Historical baseline_id | `BL-WEEKLY-STATUS-BASELINE-v1.0` (UNCHANGED) |
| Historical clean master | `BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE` / `01C29A8A20CA4D1798E4A407431B0A7FA1BD58F798D5837AD2A1CC1BF9E1D05C` (IMMUTABLE evidence) |
| Accepted clean master | `BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE` / `29E243233AB0872FFF2323ACC882FC477F71865CE072C4416EEFBDEC8F8576E0` |
| Accepted renderer | `ksb_renderer@2.1.0-CWC-CE-107-CANDIDATE` |
| Human-accepted PNG (19/19/4) | `5FEECAA3267D07A996968DC4116A0C8AFB8E7181D187302B06401886960D80CC` |

---

## 5. Human acceptance evidence

| Field | Value |
|---|---|
| Technical CWC | CWC-CE-107 Outcome A |
| Human statement | “I concur.” |
| Disposition | ACCEPT |
| Candidate path (non-production) | `renderer/tests/_non_production_output/CANDIDATE-CWC-CE-107-PUBLIC-CLEANUP-19-19-4.png` |
| Candidate SHA-256 | `5FEECAA3267D07A996968DC4116A0C8AFB8E7181D187302B06401886960D80CC` |
| Canonicalization | CWC-CE-108 |

---

## 6. Activation gate (satisfied)

1. Human visual ACCEPT of CWC-CE-107 candidate — **DONE** (CWC-CE-108)  
2. CE-GitManager canonicalize scoped package — **DONE** (CWC-CE-108)  
3. Hosted acceptance render with new `renderer_id` / clean master — **DONE** (CWC-CE-109)  
4. Human hosted visual ACCEPT of hosted PNG — **DONE** (CWC-CE-110; “I concur.”)  

| Hosted identity | Value |
|---|---|
| Request | KSB-RENDER-2026-08-30-008 |
| Issue | #9 |
| Run | 33343921319 |
| Tested canonical SHA | `db67fafde9a01fdaeecfb7c15e70d82054f00485` |
| Hosted PNG SHA-256 | `5FEECAA3267D07A996968DC4116A0C8AFB8E7181D187302B06401886960D80CC` |
| Deterministic vs CE-107 local candidate | PASS (exact equality) |

**Note:** Lifecycle terminology used here is repository-equivalent to “hosted acceptance requirement satisfied.” Publication / HG-6 remain separately Human-controlled. ORCH phone-procedure identity residual remains OPEN for CWC-CE-111.