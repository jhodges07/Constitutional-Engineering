# BlueprintLiberty Weekly Public Engineering Status — Workspace

**Document ID:** README-PUB-WEEKLY-001  
**Title:** Weekly Public Engineering Status Workspace  
**Classification:** Informational Architecture / Directory Note  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-073 (architecture); CWC-CE-075 (WSPC-001 pointer); CWC-CE-077 (Human informational acceptance / Git gate); CWC-CE-078 (STD-011 Part B implementation pointer)  
**Predecessors:** CWC-CE-071 (PASS); CWC-CE-072 (STOP/BLOCKED — path); CWC-CE-073 (canonical workspace); CWC-CE-074 (FULL PASS — HUMAN ACCEPTED); CWC-CE-075–077 (accepted); CWC-CE-078 (STD-011 Part B)  
**Status:** Human-Accepted Informational Architecture / Directory Note — Not Operative CONTROL  
**Human Acceptance:** ACCEPTED 2026-08-30 under CWC-CE-077 (Decision 2) — remains informational; does **not** become operative CONTROL  
**Operative Packaging CONTROL:** STD-011 Version 1.3.0 Part B (ECR-004 packaging; ECR-005 / WSMAT-001 maturity measurement; CWC-CE-081–085)  
**Initial PUBLIC_URL_01:** BlueprintLiberty.com  
**Version:** 0.3.5  
**Effective Date:** 2026-08-30  
**Canonical Local Repository Root:** `X:\GitHub\Constitutional-Engineering`

---

## 0. Production Contract Pointer (Informational)

Proposed Weekly Status Production Contract (CWC-CE-075):

```text
Engineering-Office/publication/weekly-status/PRODUCTION-CONTRACT-CWC-CE-075.md
```

**Document ID:** WSPC-001  
**Classification:** Informational Engineering Definition — Proposed / Not Operative CONTROL  

Operative weekly-status packaging CONTROL is **STD-011 Part B**.  
This README remains an architecture/directory note. WSPC-001 does **not** become operative CONTROL by being referenced here.

Gap-closure design record (informational):

```text
Engineering-Office/publication/weekly-status/GAP-CLOSURE-MATRIX-CWC-CE-076.md
```

**Document ID:** WSGAP-001

---

## 1. Purpose

Establish the controlled local foundation for a repeatable **BlueprintLiberty.com Weekly Public Engineering Status** product.

Intended weekly pairing:

- one Markdown status report; and
- one corresponding status image;

with permanent historical retention in Git.

This document **defines architecture**. It is **not** STD-011 body text, not an ECR, not a SPEC, and not publication authorization.

---

## 2. Authority Boundary / No Silent Promotion

1. Research, architecture, templates, mockups, manifests, and directories identified here do **not** silently become operative CONTROL.  
2. STD-011 Part B presently governs Weekly Public Engineering Status packaging. Extension of STD-011 beyond Active text requires separately Human-authorized ECR.  
3. Presence of this workspace does **not** by itself authorize staging, commit, push, Facebook posting, or public release.  
4. A public representation (Facebook, website, etc.) is an **output/view**, not engineering truth.  
5. PUBLIC NAVIGATION URLS (initial: BlueprintLiberty.com) are controlled configuration under STD-011 §28 and are not ordinary weekly maturity variables.

**Principle:**

> A PUBLIC REPRESENTATION SHALL NOT BECOME A SOURCE OF ENGINEERING TRUTH.  
> ENGINEERING TRUTH SHALL FLOW FROM CONTROLLED REPOSITORY EVIDENCE INTO THE PUBLIC REPRESENTATION.

---

## 3. Directory Structure

```text
Engineering-Office/publication/weekly-status/
  README.md          ← this architecture note
  baseline/          ← approved visual baseline / mockup (Human-supplied)
  manifests/         ← weekly or package manifests (when authorized)
  reports/           ← durable weekly Markdown status records
  images/            ← weekly rendered status images
  archive/           ← optional long-term archive placements when authorized
```

Empty subdirectories are established as logical locations. Production weekly reports/images are **not** fabricated under CWC-CE-073.

---

## 4. Naming Standard (Proposed)

### 4.1 Markdown report

```text
reports/YYYY-MM-DD-BlueprintLiberty-Weekly-Status.md
```

### 4.2 Status image

```text
images/YYYY-MM-DD-BlueprintLiberty-Weekly-Status.png
```

### 4.3 Report ↔ image reference (conceptual)

```markdown
![BlueprintLiberty Weekly Engineering Status](../images/YYYY-MM-DD-BlueprintLiberty-Weekly-Status.png)
```

Use the same `YYYY-MM-DD` in both filenames for a given week.  
Historical weekly reports **SHALL NOT** be silently overwritten when a later week is produced.

---

## 5. Weekly Markdown Record — Required Content (Target)

Each weekly Markdown status report should eventually contain at least:

| Field | Role |
|---|---|
| Status Date | Variable (`STATUS_DATE`) — public representation `yyyy.mm.ww` (STD-011); `ww` = ISO-8601 week-of-year (CWC-CE-082); compact value only on public image |
| Publication Week | Durable week identity |
| Bill A Engineering Percentage | Variable (`BILL_A_PERCENT`) — Human/authorized source only |
| Bill B Engineering Percentage | Variable (`BILL_B_PERCENT`) — Human/authorized source only |
| Bill C Engineering Percentage | Variable (`BILL_C_PERCENT`) — Human/authorized source only |
| Repository / status evidence references | Traceability to controlled evidence |
| Concise public status narrative | Public-facing summary |
| Corresponding image reference | Relative Markdown image link |
| Human acceptance state | Acceptance / pending |
| Publication authorization state | Authorized / not authorized |
| Publication destinations (when known) | Facebook / other — destinations only |
| Git commit SHA after controlled publication commit | Post-commit traceability |

The Markdown file is the durable weekly public-status record. Platforms are destinations, not the system of record.

---

## 6. Controlled Image Model

```text
ONE APPROVED BASELINE
+ CONTROLLED VARIABLE VALUES
= WEEKLY STATUS IMAGE
```

- Approved / Human-accepted baseline: `baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` (SHA-256 `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9`).  
- Weekly generated image: stored under `images/`.  
- **CWC-CE-083:** **GAP-WS-003 CLOSED** on Human acceptance of the exact baseline artifact.  
- **CWC-CE-084:** deterministic renderer under `renderer/` locally validated; **GAP-WS-004 CLOSED** (Git gate separate).

### 6.1 FIXED fields (ordinary weekly cycle — do not change)

Unless later changed by Human-authorized controlled change:

- image dimensions / aspect ratio  
- overall layout  
- title  
- section positions  
- typography specification  
- approved colors  
- icons / icon specification  
- Value Stream layout  
- repository names and descriptions  
- Bill A / Bill B / Bill C titles  
- BlueprintLiberty.com spelling and placement  
- approved motto  
- fixed explanatory text  
- other Human-approved visual elements  

### 6.2 VARIABLE fields (initially authorized candidates only)

- `STATUS_DATE` (public form `yyyy.mm.ww`; `yyyy`/`mm` calendar; `ww` ISO-8601; no legend on public image)  
- `BILL_A_PERCENT`  
- `BILL_B_PERCENT`  
- `BILL_C_PERCENT`  

Public FIXED Bill titles (STD-011 §26 / CWC-CE-081):

- Bill A: `COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT`  
- Bill B: `KANSAS PROPERTY-TAX ELIMINATION`  
- Bill C: `KANSAS NBEF ACT` / `Kansas NBEF Act (Node-Based Educational Framework)`  

Template engineering identity (not public image content):

```text
templates/BL-Weekly-Status-Template-v1.0.png
```

Public images SHALL NOT display local template filename/path, drive letters, date-format explanations, or other engineering metadata (STD-011 §25A).  

Expansion of VARIABLE fields requires controlled Human authorization.

### 6.3 Anti-drift rule

A Weekly Public Engineering Status artifact **SHALL NOT** redesign, reinterpret, restyle, add, remove, reposition, rename, or silently modify a FIXED visual element.  
Only fields explicitly designated VARIABLE may change during an ordinary weekly status cycle.

### 6.4 Percentage authority

Under STD-011 v1.3.0 / Active WSMAT-001, authorized AI evaluators **MEASURE AND CALCULATE** maturity; the Human Engineer **CERTIFIES** (ACCEPT / MODIFY / REJECT).  
CALCULATED maturity is non-operative for weekly VARIABLE fields until CERTIFIED. Silence is not certification.  
No AI system may invent evidence, bypass hard gates, or certify its own percentages.

### 6.5 Deterministic rendering direction

Mature system **SHOULD NOT** depend on generative-image text rendering for controlled text or percentages.  
Intended support: SVG, HTML/CSS→image, or another repository-authorized deterministic format with placeholders such as:

```text
{{STATUS_DATE}}
{{BILL_A_PERCENT}}
{{BILL_B_PERCENT}}
{{BILL_C_PERCENT}}
```

Renderer implementation is **out of scope** for CWC-CE-073.

---

## 7. ChatGPT / Cursor / GitHub Operating Model (Architecture Target)

```text
CURSOR AI
    ↕
LOCAL WORKING REPOSITORIES
X:\GitHub
    ↕
GITHUB
    ↕
CHATGPT
    ↕
HUMAN ENGINEER
```

- GitHub is the shared controlled interchange between ChatGPT and Cursor.  
- ChatGPT is **not** assumed to have direct filesystem access to `X:\GitHub`.  
- ChatGPT GitHub access requires separate capability testing and Human authorization before production reliance.

Desired future capability sequence:

1. ChatGPT reads authorized GitHub repositories.  
2. ChatGPT evaluates repository evidence for weekly status.  
3. Controlled percentages come from authorized evidence or Human acceptance.  
4. ChatGPT drafts the weekly Markdown report.  
5. Controlled image template receives approved variable values.  
6. Markdown + image are written to this workspace through an authorized GitHub/local workflow.  
7. Human Engineer reviews.  
8. Human Engineer authorizes publication.  
9. Human Engineer publishes to Facebook / other platforms.  
10. GitHub retains the historical weekly record.

---

## 8. Sunday Operating Model (Architecture Target — Not Scheduled)

```text
SUNDAY
→ Read repository status
→ Reconcile controlled evidence
→ Determine candidate Bill A/B/C maturity
→ Human acceptance of percentages
→ Generate weekly Markdown status
→ Render weekly image from approved baseline
→ Validate fixed text/layout
→ Human publication review
→ Commit/push controlled weekly package (when separately authorized)
→ Human publishes to Facebook/other platforms
→ Archive remains permanently addressable in GitHub
```

CWC-CE-073 does **not** schedule automation and does **not** publish.

---

## 9. Future Automation Boundaries

Automation **MAY** eventually (under later Human-authorized CONTROL):

- collect repository evidence;  
- identify changes since previous Sunday;  
- draft status narrative;  
- calculate candidate maturity when a future CONTROL authorizes calculation;  
- populate approved percentages;  
- render deterministic image;  
- create Markdown;  
- validate filenames / BlueprintLiberty.com spelling / image↔report pairing;  
- prepare Git changes;  
- present the package for Human acceptance.  

Automation **SHALL NOT** silently:

- change engineering truth;  
- approve itself;  
- publish itself;  
- invent percentages;  
- alter the fixed visual baseline; or  
- bypass Human publication authority.

---

## 10. Platforms

Facebook, X, Substack, websites, and similar are **publication destinations**.  
The Git-controlled weekly status package remains the traceable historical record.

---

## 11. Canonical Workspace Note

Canonical local GitHub workspace for this repository:

```text
X:\GitHub\Constitutional-Engineering
```

Established under CWC-CE-073 by preservation-safe copy from `D:\Constitutional-Engineering`.  
The original `D:\` copy remains intact pending separate Human cleanup authority.

---

## 12. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-08-30 | Initial architecture/directory note under CWC-CE-073. Not operative CONTROL. No weekly reports/images fabricated. |
| 0.2.0 | 2026-08-30 | CWC-CE-075 pointer + CWC-CE-077 Human informational acceptance recorded. Remains Not Operative CONTROL. |
| 0.3.0 | 2026-08-30 | CWC-CE-078: pointer to STD-011 Part B as operative packaging CONTROL; PUBLIC_URL_01 = BlueprintLiberty.com; README remains non-operative directory note. |
| 0.3.1 | 2026-08-30 | CWC-CE-081: STATUS_DATE yyyy.mm.ww; public-image metadata exclusions; Bill A/B/C public titles; template path note; ww algorithm open. |
| 0.3.2 | 2026-08-30 | CWC-CE-082: ISO-8601 `ww` Human authorization noted; remains Not Operative CONTROL. |
| 0.3.3 | 2026-08-30 | CWC-CE-083: candidate baseline path noted; GAP-WS-003 remains OPEN pending HE acceptance. |
| 0.3.4 | 2026-08-30 | CWC-CE-083: Human accepted baseline SHA `17F574D4…`; GAP-WS-003 CLOSED. |
| 0.3.5 | 2026-08-30 | CWC-CE-084: renderer pointer; GAP-WS-004 CLOSED locally. |
