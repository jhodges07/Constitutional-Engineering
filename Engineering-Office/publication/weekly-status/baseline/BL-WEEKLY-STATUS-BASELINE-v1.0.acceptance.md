# BL-WEEKLY-STATUS-BASELINE-v1.0 — Candidate Baseline Provenance & Acceptance Record

**Document ID:** BL-WS-BASELINE-001  
**Baseline ID:** `BL-WEEKLY-STATUS-BASELINE-v1.0`  
**Baseline Version:** `1.0`  
**Classification:** Controlled Visual Baseline Record (Human-Accepted)  
**Governing Work Card:** CWC-CE-083 — Controlled KSB Status Visual Baseline Ingest; Bounded Continuation #2 (header-date correction); Human acceptance recorded 2026-08-30  
**Control Authority:** STD-011 Version 1.2.1 Part B; ECR-004; applicable weekly-status controls (WSPC-001 / WSGAP-001 informational)  
**Preparing Agent:** CE-Engineer  
**Acceptance Recording Agent:** CE-Engineer  
**Effective Date (record):** 2026-08-30  

---

## 0. Acceptance Banner

```text
HUMAN-ACCEPTED BASELINE
BL-WEEKLY-STATUS-BASELINE-v1.0
SHA-256 17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9
GAP-WS-003 CLOSED
```

**Human Engineer Acceptance State:** `ACCEPTED`

| Field | Value |
|---|---|
| Approver | Human Engineer |
| Acceptance date | 2026-08-30 |
| Accepted path | `Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` |
| Accepted SHA-256 | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |
| Accepted identity | `BL-WEEKLY-STATUS-BASELINE-v1.0` |
| Dimensions at acceptance | 1536 × 912 |
| SHA re-verification at recording | **MATCH** |
| Exact acceptance statement | `I accept Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png SHA-256 17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9 as BL-WEEKLY-STATUS-BASELINE-v1.0.` |

---

## 1. Artifact Paths

| Role | Path |
|---|---|
| **Accepted baseline PNG** | `Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` |
| This record | `Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.acceptance.md` |
| Template source (unchanged) | `Engineering-Office/publication/weekly-status/templates/BL-Weekly-Status-Template-v1.0.png` |

Template source remains a **TEMPLATE SOURCE**. It is **not** the accepted visual baseline identity.  
The accepted baseline identity is **`BL-WEEKLY-STATUS-BASELINE-v1.0`**.

---

## 2. Provenance

| Field | Value |
|---|---|
| Source filename | `BL-Weekly-Status-Template-v1.0.png` |
| Source SHA-256 | `2993459AAF4AE61D4F96415C3D7928F780A94BCE6DE4221330D0B3766A249F0F` |
| Source dimensions | 1536 × 1024 px (RGB) |
| Cleaning operation 1 | Deterministic vertical crop removing rejected development-only strip below public navy footer |
| Crop rule | Keep rows `y = 0 .. 911` inclusive; discard `y ≥ 912` |
| Cleaning operation 2 (CWC-CE-083 Cont. #2) | Bounded removal of header explanatory parenthetical `(Week 35 of 2026)` with local background restoration |
| Pre-correction candidate SHA-256 | `E2FB8E3C5CC45FC060E33FEED9FE47FCF03A3BA13C994F313014E25575A80B76` |
| Unauthorized redesign | **NO** |
| Candidate dimensions | 1536 × 912 px (RGB) |
| **Accepted baseline SHA-256** | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |
| Producing CWC | CWC-CE-083 (+ Bounded Continuation #2) |
| Producing agent | CE-Engineer |

### 2.1 Rejected material removed

**From template bottom strip (crop):**

1. Local template filename  
2. Local template path / `X:\` drive information  
3. Date-format explanation legend (`yyyy` / `mm` / `ww` definitions)  
4. Example-date explanation / “reads as” text  

**From header (Continuation #2):**

5. Explanatory parenthetical `(Week 35 of 2026)` beneath `Date: 2026.08.35`

### 2.2 Header-date correction method (Continuation #2)

1. Re-verified pre-correction candidate SHA = `E2FB8E3C…A80B76`.  
2. Rebuilt that candidate deterministically from template crop (integrity check).  
3. Built an anomaly mask in authorized window approximately `x=1285..1515`, `y=34..56` for pixels differing from column sky/flag reference rows; dilated for antialias; vivid red flag-stripe pixels excluded from mask expansion.  
4. Applied OpenCV Telea inpaint (`inpaintRadius=3`) only on masked pixels.  
5. Confirmed no pixel changes outside the authorized window; Date line rows `y=18..32` unchanged.

### 2.3 Pixel-difference evidence (Continuation #2)

| Metric | Value |
|---|---|
| Changed-pixel count | 2920 |
| Changed-pixel bounding box | `x=1285..1515`, `y=34..56` |
| Out-of-authorized-window changes | **0** |
| Changes in Date-line rows y=18..32 | **0** |
| Changes in flag body left of x=1285 | **0** |

Note: the parenthetical glyph region overlapped the extreme right edge of the U.S. flag photograph. Pixels under that overlap within the authorized text window were restored by inpaint; flag pixels left of the authorized window were untouched.

### 2.4 Public composition terminus

Public composition ends with the approved navy footer containing:

- `BlueprintLiberty.com`  
- `Libertas sine lapsu — Liberty without drift.`  
- `Engineering the Republic. For the People. By the People.`  

Visible header date on this candidate:

```text
Date: 2026.08.35
```

`2026.08.35` remains a **PLACEHOLDER** for the `STATUS_DATE` region (not weekly engineering truth).

---

## 3. Human Acceptance Gate — CLOSED

Exact Human Engineer statement received and recorded 2026-08-30:

```text
I accept Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png
SHA-256 17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9
as BL-WEEKLY-STATUS-BASELINE-v1.0.
```

**GAP-WS-003:** **CLOSED** under this Human acceptance of the exact pixel artifact.  
Git integration (stage/commit/push) remains a separate Human Git gate unless/until expressly authorized.

---

## 4. FIXED-Element Inventory (from candidate artifact)

| Element | Observation |
|---|---|
| Canvas dimensions / aspect | 1536 × 912 px |
| Background composition | White/light body panels; navy headers/footer; Capitol photograph in header-right |
| Major layout regions | Header + VSM band + 3-column body + GitHub breadcrumb band + navy public footer |
| Header / subtitle | Preserved |
| Typography / colors / icons | Preserved as rendered (no redesign) |
| Capitol / flags | Preserved; only authorized parenthetical-overlap pixels restored |
| VSM / repository area / Repo terminology | Preserved |
| Bill-title labels | Bill A/B/C titles preserved |
| Status-panel / Why This Matters | Preserved |
| GitHub breadcrumb | Preserved (HTTPS only; no local paths) |
| BlueprintLiberty.com / motto / footer | Preserved |
| Date placement | Header top-right; visible compact form `Date: 2026.08.35` |
| Percentage placement | Center status panel regions (placeholder digits only) |

---

## 5. VARIABLE-Element Inventory

| Variable | Semantic identity | Intended visual region | Formatting rule | Authority source | Human approval required |
|---|---|---|---|---|---|
| `STATUS_DATE` | Compact weekly status date | Header top-right date region | `yyyy.mm.ww` (`ww` = ISO-8601 week-of-year). Compact value only; no `(Week NN of YYYY)` suffix; no algorithm legend on image. | STD-011 v1.2.1 | Yes for weekly package value |
| `BILL_A_PERCENT` | Bill A maturity % | Center Bill A progress region | Human-approved; example digits placeholder only | Human-supplied / Human-approved | **Yes — always** |
| `BILL_B_PERCENT` | Bill B maturity % | Center Bill B progress region | Same | Human-supplied / Human-approved | **Yes — always** |
| `BILL_C_PERCENT` | Bill C maturity % | Center Bill C progress region | Same | Human-supplied / Human-approved | **Yes — always** |

Do **not** split `STATUS_DATE` into YEAR / MONTH / WEEK variables.

Controlled configuration (not ordinary weekly VARIABLE): `PUBLIC_URL_01` = `BlueprintLiberty.com`

---

## 6. Bill Title Pins (FIXED public copy)

| Bill | Title |
|---|---|
| Bill A | `COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT` |
| Bill B | `KANSAS PROPERTY-TAX ELIMINATION` |
| Bill C | `KANSAS NBEF ACT` |

---

## 7. STD-011 Compliance Check (candidate)

| Requirement | Result |
|---|---|
| Compact `STATUS_DATE` display; no `(Week NN of YYYY)` | **PASS** |
| No yyyy/mm/ww legend / ISO explanation on image | **PASS** |
| No local filename / `X:\` path / development metadata | **PASS** |
| `PUBLIC_URL_01` = BlueprintLiberty.com | **PASS** |
| Four ordinary VARIABLES only | **PASS** |
| Percentages remain Human-approved placeholders | **PASS** |

---

## 8. Replacement Procedure

A renderer, AI agent, weekly workflow, or publication process SHALL **NOT** silently modify or replace this baseline.

Future baseline replacement SHALL require at minimum:

1. new controlled candidate artifact;  
2. provenance record;  
3. SHA-256 of the new artifact;  
4. FIXED/VARIABLE inventory reconciliation;  
5. explicit Human Engineer acceptance of the exact new pixel artifact;  
6. baseline version increment;  
7. applicable control/change record;  
8. archival of the superseded baseline.

---

## 9. Supersession Rule

1. Only one **accepted** visual baseline identity is operative for ordinary weekly anti-drift at a time.  
2. A newer accepted baseline supersedes the prior only after Human acceptance and controlled recording.  
3. Template sources and candidates do **not** supersede an accepted baseline.  
4. Prior accepted baselines SHALL be retained in archive/history as required by the authorizing CWC.

---

## 10. Gap Disposition

| Gap | Ending state |
|---|---|
| GAP-WS-003 | **CLOSED** — Human-accepted baseline SHA `17F574D4…` recorded |
| GAP-WS-004 | **OPEN** — renderer not implemented |

---

## 11. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0-CANDIDATE | 2026-08-30 | CWC-CE-083: candidate via development-strip crop; SHA `E2FB8E3C…`; HE acceptance pending. |
| 0.1.1-CANDIDATE | 2026-08-30 | CWC-CE-083 Cont. #2: removed `(Week 35 of 2026)`; SHA `17F574D4…`; HE acceptance pending; GAP-WS-003 remains OPEN. |
| 1.0.0-ACCEPTED | 2026-08-30 | Human Engineer accepted exact artifact SHA `17F574D4…` as `BL-WEEKLY-STATUS-BASELINE-v1.0`; GAP-WS-003 CLOSED. |
