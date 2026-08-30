# Weekly Status Manifest — 2026-08-30

**Document ID:** MANIFEST-KSB-2026-08-30  
**Package Class:** Weekly Public Engineering Status  
**Governing Work Card:** CWC-CE-085 — First Phone-Originated KSB Status POC  
**Governing CONTROL:** STD-011 Version 1.3.0 Part B; WSMAT-001 Version 1.0.0; ECR-005  
**Status:** GENERATED LOCALLY — VALIDATED — NOT PUBLISHED — GIT NOT ADVANCED  
**Preparing Agent:** CE-Engineer  

---

## 1. Status Date

| Field | Value |
|---|---|
| Calendar production date | `2026-08-30` |
| ISO-8601 week-of-year (`ww`) | `35` (verified via `date.isocalendar()` / WSMAT/renderer contract) |
| Public `STATUS_DATE` | `2026.08.35` |
| Publication week id | `2026-W35` (ISO week number; calendar year remains 2026) |

---

## 2. Certified Maturity VARIABLES

| Variable | Value | Source |
|---|---|---|
| `BILL_A_PERCENT` | **19** | Human CERTIFIED (`KSB-MATURITY-CERT-001`) — ACCEPT of calculated 19% |
| `BILL_B_PERCENT` | **19** | Human CERTIFIED (`KSB-MATURITY-CERT-001`) — ACCEPT of calculated 19% |
| `BILL_C_PERCENT` | **4** | Human CERTIFIED (`KSB-MATURITY-CERT-001`) — ACCEPT of calculated 4% |

Evidence snapshot: `KSB-MATURITY-CALC-001-CWC-CE-085.md`  
Certification record: `KSB-MATURITY-CERT-001-CWC-CE-085.md`

---

## 3. Public Bill Identities (FIXED)

| Bill | Title |
|---|---|
| A | COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT |
| B | KANSAS PROPERTY-TAX ELIMINATION |
| C | KANSAS NBEF ACT (Node-Based Educational Framework) |

---

## 4. Artifact Paths

| Artifact | Path |
|---|---|
| Renderer input (four-key) | `manifests/2026-08-30-BlueprintLiberty-Weekly-Status.renderer-input.json` |
| Markdown report | `reports/2026-08-30-BlueprintLiberty-Weekly-Status.md` |
| PNG image | `images/2026-08-30-BlueprintLiberty-Weekly-Status.png` |
| Visual baseline | `baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` |

---

## 5. Baseline / Renderer

| Field | Value |
|---|---|
| Baseline ID | `BL-WEEKLY-STATUS-BASELINE-v1.0` |
| Baseline SHA-256 | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |
| Dimensions | 1536 × 912 |
| Renderer | `renderer/` version `1.0.0-CWC-CE-084` |
| Anti-drift | **PASS** — unauthorized changed pixels = 0 (total changed 20260, all authorized) |
| Output PNG SHA-256 | `10BE46068452820CB557604377D88D7C5B2F952C71BABBF2892E5C9FE2F5D83F` |
| Determinism (double-render) | **PASS** (identical SHA) |

---

## 6. Human / Publication / Git States

| Gate | State |
|---|---|
| Human maturity certification | **CERTIFIED** (ACCEPT 19/19/4) |
| Package generation acceptance | Generated under CWC-CE-085 — pending Human Git review |
| HG-D1 (any bill LOU) | **NOT PASSED** |
| Git commit SHA | *pending — not committed* |
| Publication authorization (HG-6) | **NOT AUTHORIZED** |
| Public LOU review | **NOT STARTED** |

---

## 7. PUBLIC NAVIGATION URL

| Slot | Display | Destination intent |
|---|---|---|
| `PUBLIC_URL_01` | BlueprintLiberty.com | Human-approved BlueprintLiberty public website |

---

## 8. Explicit non-claims

This package does **not** claim LOU acceptance, SPEC acceptance, legislative introduction/enactment, candidate support, or public LOU review.
