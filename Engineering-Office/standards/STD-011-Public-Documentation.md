# STD-011 — Public Documentation

**Document ID:** STD-011  
**Title:** Public Documentation  
**Classification:** Engineering Standard  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Governing Index:** IDX-001 — Engineering Office Master Index  
**Governing Workflows:** WF-001 — Engineering Office Operating Workflow; WF-002 — Engineering Release Workflow (when release baselines apply)  
**Governing Change:** ECR-003 — Engineering Definition LOU Publication-Package Control; ECR-004 — Weekly Public Engineering Status Publication Control; ECR-005 — KSB Status Maturity Measurement Control; ECR-007 — KSB Phone-Command Orchestration Control; ECR-008 — KSB Single-Command Sunday Publication Package Control; ECR-011 — KSB Three-Step Human Command Contract; ECR-012 — KSB Human Product Delivery and Fresh Deterministic Image Composition; ECR-013 — KSB True New-Image Blank-Canvas Composition; **ECR-014 — KSB Clean Master Template and Dynamic Center-Panel Composition**  
**Governing Work Card:** CWC-CE-066 — Engineering Definition LOU Publication-Package Control Definition; CWC-CE-078 — Implement Weekly Status Publication Control and Public URL Requirement; CWC-CE-081 — Weekly Status Date Format and Public-Image Content Control Update; CWC-CE-082 — ISO Week Authority Integration; CWC-CE-085 — KSB Maturity Control Authorization / Implementation; CWC-CE-087 — KSB Phone-Command Orchestration; CWC-CE-088 — KSB Single-Command Sunday Publication Package; CWC-CE-092 — KSB Three-Step Human Command Contract; CWC-CE-094 — KSB Human Product Delivery and Fresh Deterministic Image Composition; CWC-CE-096 — KSB True New-Image Deterministic Composition; **CWC-CE-097 — KSB Clean Master Template Integration**  
**Status:** Active  
**Version:** 1.9.0  
**Effective Date:** 2026-08-30  

---

## 1. Purpose

This standard governs public-facing documentation quality, disclaimers, and publication packaging rules for the Constitutional Engineering Office.

This Version establishes controlled conventions for **two distinct package classes**:

**A. ENGINEERING DEFINITION LOU PUBLICATION PACKAGES** (Part A — §§3–20)  

including Markdown authority, PDF derivative rules, location/naming, generation requirements, verification, Git/publication boundaries, and public GitHub access relationships.

**B. WEEKLY PUBLIC ENGINEERING STATUS PACKAGES** (Part B — §§21–36)  

including weekly Markdown/image pairing, baseline/anti-drift rules, FIXED/VARIABLE fields, PUBLIC URL configuration, percentage authority, Git/publication boundaries, truth-model separation, and phone-command / follow-up orchestration.

This standard does **not** publish any LOU or weekly status. Generation, Git action, and publication each require separately authorized controlled work under WF-001.

The two package classes **SHALL NOT** silently inherit requirements that are inappropriate to the other class.

---

## 2. Scope

### 2.1 In Scope

**Part A — LOU packages:**

1. Accepted Engineering Definition Letters of Understanding (`LOU-NNN`) under TMP-002 / README-DEF-001  
2. Non-authoritative PDF publication derivatives of accepted LOUs  
3. Engineering Definition LOU Publication Packages  
4. Source ↔ derivative ↔ publication traceability for LOUs  
5. Relationship of LOU publication packages to WF-001 Git and publication gates  

**Part B — Weekly Public Engineering Status packages:**

6. BlueprintLiberty Weekly Public Engineering Status packages under `Engineering-Office/publication/weekly-status/`  
7. Weekly Markdown report / status-image pairing and manifests  
8. Approved visual baseline and anti-drift rules  
9. Controlled PUBLIC NAVIGATION URL configuration  
10. Relationship of weekly-status packages to WF-001 Git and publication gates  

### 2.2 Out of Scope

1. Legislative publication packages governed by manager-local standards (e.g., KLS-006), unless an Active control expressly makes them applicable  
2. Requirements/SPEC publication packages (future extension may be authorized by later ECR)  
3. AGCL / NBBF / NBEF / CDT normative-control publication ownership  
4. Automatic publication upon HG-D1 acceptance or upon weekly package creation  
5. Installation or download of software tooling  
6. Autonomous social-media posting, scheduled publication, or AI self-approval  
7. Automated Bill maturity-percentage formulas **except** as expressly authorized by Active **WSMAT-001 — KSB Status Maturity Measurement** under ECR-005 (CALCULATED maturity remains non-operative for weekly VARIABLE use until Human CERTIFIED KSB MATURITY for that cycle)  
8. Legislative acceptance implied by public Bill title pins  

### 2.3 Authority Position

This standard is subordinate to ARCH-001 and POL-001 and is consistent with STD-001, STD-014, STD-015, WF-001, and WF-002.  
It does not authorize Controlled Execution, Git advancement, or publication by itself.

### 2.4 Package-Class Separation

1. Part A rules apply to LOU publication packages only.  
2. Part B rules apply to Weekly Public Engineering Status packages only.  
3. LOU Markdown remains Engineering Definition source authority.  
4. Weekly Markdown reports are durable **public-status records**, not LOU sources and not engineering-truth sources.  
5. Informational artifacts (WSPC-001, README-PUB-WEEKLY-001, WSGAP-001) do not become operative CONTROL by reference.

---

## 3. Governing Principle (Part A — LOU Packages)

```text
ACCEPTED MARKDOWN
        ↓
CONTROLLED ENGINEERING DEFINITION SOURCE
        ↓
PDF GENERATION
        ↓
VERIFIED PDF DERIVATIVE
        ↓
PUBLICATION PACKAGE
        ↓
CONTROLLED GIT ACTION
        ↓
PUBLIC GITHUB SURFACE
```

1. Accepted LOU Markdown is the controlling Engineering Definition source.  
2. The PDF is a **non-authoritative publication derivative**.  
3. The PDF shall not become an independently edited source of Engineering Definition.  
4. Public GitHub presence does not create engineering authority (POL-001 / ARCH-001).  
5. Sections 3–20 apply to **LOU packages only**, unless a clause expressly states otherwise.

---

## 4. Authoritative Source

1. The authoritative Engineering Definition source for an LOU is the accepted Markdown artifact stored under:

   `Engineering-Office/definition/`

2. Filename form remains:

   `LOU-NNN-Short-Title.md`

3. HG-D1 acceptance is recorded in the LOU per TMP-002 / WF-001.  
4. Substantive corrections shall be made only in the controlled Markdown source and shall flow through the applicable Engineering Definition lifecycle (and re-acceptance when required) before PDF regeneration.

---

## 5. PDF Derivative Status

1. A PDF produced under this standard is a **publication derivative**, not an Engineering Definition source.  
2. Readers and operators shall treat conflicts between Markdown and PDF as evidence of derivative failure.  
3. The Markdown controls until a corrected derivative is regenerated and verified.  
4. Manual editing of PDF content to change substantive Engineering Definition is prohibited.

---

## 6. PDF Location

LOU PDF derivatives and package companion files shall reside under:

```text
Engineering-Office/publication/definition/LOU-NNN/
```

Examples:

```text
Engineering-Office/publication/definition/LOU-002/
```

Rules:

1. Do not store authoritative LOU Markdown under `publication/`.  
2. Do not treat files under `publication/` as Engineering Definition sources.  
3. The `Engineering-Office/definition/` directory remains the LOU system of record.  
4. Directory creation for a specific LOU occurs when a separately authorized package-generation CWC produces that LOU’s package (this standard defines the location; it does not itself create package contents).

---

## 7. PDF Filename Convention

Deterministic filename form:

```text
LOU-NNN-<Short-Title-Slug>-v<Version-Slug>-HG-D1-<Acceptance-Slug>.pdf
```

Where:

| Token | Rule |
|---|---|
| `LOU-NNN` | Exact Document ID |
| `<Short-Title-Slug>` | Source Markdown short-title segment with spaces/unsafe characters replaced by hyphens |
| `<Version-Slug>` | Accepted version string with spaces replaced by hyphens (example: `Draft-0.5`) |
| `<Acceptance-Slug>` | `ACCEPTED` when HG-D1 = Accepted |

Example for LOU-002 Draft 0.5:

```text
LOU-002-Constitutional-Engineering-Master-Plan-vDraft-0.5-HG-D1-ACCEPTED.pdf
```

Companion files for the same package use the same basename with suffixes:

| File | Suffix |
|---|---|
| Publication manifest | `.publication-manifest.md` |
| Verification record | `.verification.md` |

---

## 8. Version and HG-D1 Representation

Every LOU PDF derivative shall identify, on a cover page or first-page header block:

1. Document ID (`LOU-NNN`)  
2. Document title  
3. Accepted version  
4. HG-D1 status (`ACCEPTED` / other disposition only if expressly authorized for publication)  
5. Acceptance date when recorded on the source LOU  
6. Controlling Markdown repository-relative path  
7. Statement that Markdown is authoritative and PDF is a publication derivative  
8. Statement that HG-D1 acceptance does not authorize Controlled Execution  

If any required identification element is missing, verification fails.

---

## 9. Source Traceability

A reader or auditor must be able to determine:

```text
HUMAN ENGINEER DECISION
        ↓
HG-D1 ACCEPTED LOU
        ↓
CONTROLLED MARKDOWN
        ↓
DERIVATIVE GENERATION
        ↓
PDF
        ↓
DERIVATIVE VERIFICATION
        ↓
PUBLICATION AUTHORIZATION
        ↓
GIT COMMIT
        ↓
GITHUB PUBLICATION
```

Minimum machine-readable package fields (manifest):

- LOU ID  
- Source Markdown path  
- Source version  
- HG-D1 status  
- Acceptance date (if recorded)  
- Source SHA-256  
- PDF path  
- PDF SHA-256  
- Generation method / tool identity and version when available  
- Generation datetime (UTC or local with timezone)  
- Verification result (`Pass` / `Fail`)  
- Governing CWC-CE for package generation  
- Publication authorization status  

---

## 10. Engineering Definition LOU Publication Package

An **Engineering Definition LOU Publication Package** for an accepted LOU shall contain or reference:

1. Accepted Markdown source path (authoritative; remains in `definition/`)  
2. Verified PDF derivative (under §6)  
3. Publication manifest (§9)  
4. Verification record (§12)  
5. LOU ID, source version, and HG-D1 acceptance status  
6. Explicit source/derivative relationship statement  

The package may also include hash listings for all package files when required by the authorizing CWC-CE or release workflow.

This standard defines the package concept. Package construction requires a separately authorized CWC-CE.

---

## 11. PDF Generation Method

### 11.1 Required Capabilities

Any authorized generation method shall:

1. Be capable of reproducible generation for a fixed source revision  
2. Preserve headings  
3. Preserve paragraphs  
4. Preserve lists  
5. Preserve tables  
6. Preserve code/preformatted blocks where present  
7. Preserve page readability  
8. Support required source/version/acceptance identification (§8)  
9. Avoid substantive transformation of accepted content  

### 11.2 Authorized Method Class

The authorized generation method class for Engineering Definition LOU PDFs is:

**Controlled Markdown → PDF conversion using a Human Engineer–authorized local toolchain**, with exact tool identity, version, and command/parameters recorded in the publication manifest.

Candidate toolchain (when locally available and expressly authorized for use by the package-generation CWC-CE):

1. **pandoc** Markdown-to-PDF conversion with fixed, recorded options  

Other toolchains may be used only if:

1. Human Engineer expressly authorizes the toolchain in the package-generation CWC-CE; **and**  
2. The toolchain satisfies §11.1; **and**  
3. The toolchain identity/version/parameters are recorded in the package manifest.

### 11.3 Current Local Tooling Status (as of CWC-CE-066 inspection)

Inspection of the controlled local environment under CWC-CE-066 found:

- `pandoc`: **not found** on PATH  
- Common Python Markdown/PDF libraries (`markdown`, `weasyprint`, `reportlab`, `fpdf`): **not available** in the inspected Python environment  
- No Engineering Office `tools/` PDF toolchain directory present  

Therefore:

**PDF GENERATION TOOLING FOR PRODUCTION LOU PACKAGES IS CURRENTLY UNRESOLVED.**

This standard defines the method class and verification rules. It does **not** fabricate successful local tooling.  
A future package-generation CWC-CE must either:

1. use a later-verified locally available authorized toolchain; or  
2. obtain separate Human Engineer authorization to acquire/install a conforming toolchain under controlled process;

before generating a production LOU PDF.

### 11.4 Prohibitions

1. Do not install or download software under a CWC that prohibits installation.  
2. Do not generate a production LOU PDF when tooling is unresolved.  
3. Do not claim verification Pass without actual generation and checks.

---

## 12. Derivative Verification

### 12.1 Required Checks

Before publication authorization, verification shall confirm:

1. Source Markdown path and version match the HG-D1 accepted LOU  
2. PDF filename conforms to §7  
3. Cover/header identification conforms to §8  
4. Source SHA-256 matches the accepted Markdown revision used for generation  
5. PDF SHA-256 is recorded  
6. Structural correspondence is checked for material loss, including at minimum:
   - top-level heading inventory presence  
   - presence of major sections required by the source  
   - tables/lists/code blocks not silently dropped where the toolchain claims support  
7. Sampled human-readable review of critical sections (identity metadata, acceptance record, authority boundaries)  
8. No evidence of independent substantive PDF editing  

Verification outcomes: `Pass` / `Fail` / `Not performed`.

### 12.2 Failure Stop Rule

If PDF generation loses, changes, truncates, reorders, or materially misrepresents source content, **verification fails and publication stops**.

Failed derivatives shall not be published.  
Remediation occurs by correcting generation parameters/toolchain or correcting the Markdown source through the applicable Engineering Definition lifecycle, then regenerating.

Unperformed verification shall be labeled `Not performed` and does not authorize publication.

---

## 13. Public Markdown and Public PDF Models

### 13.1 Public Markdown Model

```text
GitHub visitor
        ↓
Repository
        ↓
Accepted LOU Markdown in Engineering-Office/definition/
        ↓
Readable rendered Markdown
```

Public Markdown is the controlling Engineering Definition text as rendered by GitHub.  
It remains subject to repository Git controls and does not by itself constitute legal enactment or Controlled Execution authorization.

### 13.2 Public PDF Model

```text
GitHub visitor
        ↓
PDF publication derivative under Engineering-Office/publication/definition/LOU-NNN/
        ↓
Open / download PDF
```

Public PDF is a convenience derivative for open/download readability.  
Public visitors shall be able to distinguish:

**CONTROLLED SOURCE** (`definition/`)  

from:

**PUBLICATION DERIVATIVE** (`publication/definition/`).

---

## 14. Git and Publication Control Boundaries

1. PDF generation does **not** authorize stage, commit, push, release, or publication.  
2. Git Commit requires Human Engineer approval under WF-001 HG-4 / STD-002 (when Active) / applicable Git standards.  
3. Git Push requires Human Engineer approval under WF-001 HG-5.  
4. Publication requires explicit Publication Approval under WF-001 §14 after Human Acceptance of the publication package work.  
5. HG-D1 LOU acceptance does **not** authorize package generation, Git advancement, or publication.  
6. WF-002 release-baseline rules may apply when LOU publication is included in a certified baseline; they do not replace this standard’s derivative rules.

---

## 15. Human Authorization Points

| Step | Authorization required |
|---|---|
| Accept LOU Engineering Definition | HG-D1 |
| Generate/verify publication package | Separately approved CWC-CE |
| Resolve/install PDF toolchain (if needed) | Separately approved Human Engineer / CWC-CE authorization |
| Stage/commit package + source | HG-4 / explicit HE commit authorization |
| Push to remote | HG-5 / explicit HE push authorization |
| Publish as public package | WF-001 Publication Approval |

Silence is not authorization.

---

## 16. Reusability

This convention applies to all future accepted Engineering Definition LOUs (`LOU-NNN`), including subordinate LOUs, unless a later Active control expressly establishes a different requirement for a specific LOU class.

---

## 17. Disclaimers (Minimum)

Publication packages and public derivatives shall not imply:

1. Legal enactment  
2. Constitutional amendment  
3. Controlled Execution authorization  
4. Requirements/SPEC acceptance  
5. Implementation authorization  
6. That PDF supersedes Markdown  

---

## 18. Relationship to Reserved History

Identifier `STD-011` was previously Reserved (Version 0.0.0).  
Version 1.0.0 activates normative body content for Engineering Definition LOU publication packages under ECR-003 / CWC-CE-066.  
Version 1.1.0 adds Part B Weekly Public Engineering Status packages under ECR-004 / CWC-CE-078, including the PUBLIC URL REQUIREMENT, without weakening Part A LOU rules.

Broader public-documentation topics beyond these package classes may be added by later approved ECR revision of this standard.

---

## 19. Nonconformance

Nonconforming publication derivatives, missing verification, or independent PDF editing are engineering defects requiring corrective controlled work.  
They shall not be treated as accepted Engineering Definition.

Nonconforming weekly-status packages (anti-drift failure, unauthorized URL change, missing Human-approved percentages, missing PUBLIC URL exposure, or unpaired Markdown/image) are engineering defects.  
They shall not be treated as authorized public weekly status and shall not be published.

---

## 20. Version History

| Version | Date | Summary |
|---|---|---|
| 0.0.0 | 2026-08-08 | Reserved placeholder formally classified under CER-001 remediation / CWC-CE-033. |
| 1.0.0 | 2026-08-09 | Activated under ECR-003 / CWC-CE-066. Establishes Engineering Definition LOU Publication Package convention: Markdown authority, PDF derivative location/naming, generation method class, tooling gap reporting, verification/failure-stop, Git/publication boundaries, and public source/derivative distinction. |
| 1.1.0 | 2026-08-30 | ECR-004 / CWC-CE-078: adds Part B Weekly Public Engineering Status package class; PUBLIC URL REQUIREMENT; FIXED/VARIABLE and percentage rules; Bill C public title pin recognition; preserves Part A LOU rules and WF-001 Human gates. |
| 1.2.0 | 2026-08-30 | CWC-CE-081: STATUS_DATE = yyyy.mm.ww display form; public-image exclusion of engineering metadata; template identity without public rendering; Bill A/B/C public title pins; GitHub breadcrumb / Repo terminology / acronym readability; ww algorithm remains Human-decision open. |
| 1.2.1 | 2026-08-30 | CWC-CE-082: Human-authorized ISO-8601 week-of-year for `ww` only; `yyyy`/`mm` remain calendar components; year-boundary rule; renderer may calculate `ww`; public-image explanation prohibition preserved. |
| 1.3.0 | 2026-08-30 | ECR-005 / CWC-CE-085: authorizes deterministic KSB maturity calculation under Active WSMAT-001; distinguishes CALCULATED vs CERTIFIED maturity; preserves Human certification; Bill identity integrity; no grandfathering of provisional percentages. |
| 1.4.0 | 2026-08-30 | ECR-007 / CWC-CE-087: adds Part B §36 phone-command orchestration / follow-up context; binds Active KSB Cycle, controlled-image routing, creative-artwork firewall, renderer failure-safe (`KSB IMAGE: RENDER REQUIRED`), and Active KSB-ORCH-001. |
| 1.5.0 | 2026-08-30 | ECR-008 / CWC-CE-088: `Prepare KSB Status` targets complete KSB Sunday Publication Package (controlled status + 450–550-word press release + controlled KSB image); COMPLETE/INCOMPLETE semantics; KSB-PR-TMP-001; preserves CWC-CE-087 firewalls. |
| 1.5.1 | 2026-08-30 | CWC-CE-088 defect remediation: §36.10 Human acceptance requires complete package; diagnostics/partial infrastructure ≠ PASS (KSB-POC-FAIL-002). |
| 1.6.0 | 2026-08-30 | ECR-011 / CWC-CE-092: three-step Human command contract (Prepare→STATUS; Next→press release; Next→controlled image); supersedes one-shot Prepare delivery; preserves Sunday package completeness and firewalls. |
| 1.7.0 | 2026-08-30 | ECR-012 / CWC-CE-094: Command 2 single-copy press-release box; Command 3 inline controlled PNG; engineering artifact ≠ Human product; fresh plate-fill composition (no ordinary inpaint). |
| 1.8.0 | 2026-08-30 | ECR-013 / CWC-CE-096: true new blank-canvas composition each render; fixed-layer asset; populated baseline not ordinary canvas; Human visual acceptance gate for candidate renderer. |
| 1.9.0 | 2026-08-30 | ECR-014 / CWC-CE-097: clean master template (blank center panel) + dynamic center-panel composition; CE-096 fixed-layer path superseded after Human visual rejection. |

---

# PART B — WEEKLY PUBLIC ENGINEERING STATUS PACKAGES

## 21. Weekly-Status Governing Principle

```text
CONTROLLED REPOSITORY EVIDENCE
        ↓
AI-DERIVED EVIDENCE
        ↓
AI-PROPOSED ASSESSMENT
        ↓
HUMAN-APPROVED STATUS
        ↓
MECHANICALLY GENERATED PUBLIC REPRESENTATION
        ↓
HUMAN GIT GATES (WF-001 HG-4 / HG-5)
        ↓
HUMAN PUBLICATION GATE (WF-001 HG-6)
```

1. A PUBLIC REPRESENTATION SHALL NOT BECOME A SOURCE OF ENGINEERING TRUTH.  
2. ENGINEERING TRUTH SHALL FLOW FROM CONTROLLED REPOSITORY EVIDENCE INTO THE PUBLIC REPRESENTATION.  
3. AI SHALL NOT approve itself.  
4. Facebook, X, Substack, websites, and similar platforms are publication **destinations**, not systems of record.  
5. WSPC-001 remains informational engineering definition unless later Human-authorized promotion occurs through controlled process.

---

## 22. Weekly Package Root and Naming

Package root:

```text
Engineering-Office/publication/weekly-status/
```

Required pairing for an authorized weekly package:

```text
reports/YYYY-MM-DD-BlueprintLiberty-Weekly-Status.md
images/YYYY-MM-DD-BlueprintLiberty-Weekly-Status.png
manifests/<corresponding-manifest>
```

Optional supporting locations: `baseline/`, `archive/`, `integration-test/` (non-production).

Historical weekly reports and images **SHALL NOT** be silently overwritten.

---

## 23. Weekly Package Contents

An authorized Weekly Public Engineering Status package shall contain or reference:

1. Status manifest  
2. Markdown weekly report  
3. Corresponding weekly status image  
4. Press release (when produced under §36.9 — KSB Sunday Publication Package)  
5. Evidence references / source commit references as applicable  
6. Human acceptance state  
7. Git traceability (after commit)  
8. Publication authorization state  
9. Package completion state (`COMPLETE` / `INCOMPLETE`) when prepared under §36.9  

Package construction requires a separately authorized CWC-CE. This standard defines the package class; it does not fabricate weekly packages.

When a weekly package is prepared under §36.9, the status manifest SHOULD identify the paired report, press release, controlled image, package completion state, and applicable validation identity for retrospective audit.

---

## 24. Markdown Report Authority

1. The Markdown weekly report is the durable weekly **public-status record**.  
2. It is **not** an Engineering Definition LOU source.  
3. It is **not** the authoritative source for underlying engineering truth.  
4. It SHALL reference its corresponding image with a repository-relative Markdown image link using the same `YYYY-MM-DD`.  
5. Minimum content targets include Status Date, Publication Week, Bill A/B/C engineering percentages, evidence references, concise public narrative, image reference, Human acceptance state, publication authorization state, PUBLIC NAVIGATION URL section, and post-commit Git SHA when available.

---

## 25. Image Model and Anti-Drift

```text
CLEAN MASTER TEMPLATE (immutable; blank Kansas Legislative Engineering Status panel)
+ CONTROLLED DESIGN SPECIFICATION
+ CONTROLLED CENTER-PANEL CONTENT (titles/descriptions/badges/tracks)
+ CURRENT CONTROLLED VARIABLE VALUES (status_date contract retained; percents)
= WEEKLY STATUS IMAGE (NEW PNG EVERY RENDER)
```

**Clean master role (CWC-CE-097 / ECR-014):** Ordinary weekly render input. Center status panel starts blank. Master file SHALL NOT be overwritten by render.

**Baseline role:** `BL-WEEKLY-STATUS-BASELINE-v1.0` remains historical Human-accepted visual reference (integrity). It SHALL NOT be the ordinary weekly composition input.

**CWC-CE-096 fixed layer:** Historical candidate evidence only — SHALL NOT be ordinary render input.

1. Approved visual baseline resides under `baseline/` with identifier, version, provenance, and checksum.  
2. Ordinary weekly VARIABLE fields are limited to:

   - `STATUS_DATE`  
   - `BILL_A_PERCENT`  
   - `BILL_B_PERCENT`  
   - `BILL_C_PERCENT`  

3. **`STATUS_DATE` public representation** for this package class SHALL be:

   ```text
   yyyy.mm.ww
   ```

   Where:

   - `yyyy` = four-digit **calendar year** of the KSB Status date  
   - `mm` = two-digit **calendar month** of the KSB Status date  
   - `ww` = **ISO-8601 week-of-year number**, zero-padded to two digits (`01`–`53`)  

   Human-approved display-form example: `2026.08.35`  

   **Semantic boundary (mandatory):** Only `ww` uses ISO-8601 week-number calculation.  
   `yyyy` and `mm` remain the ordinary calendar year and calendar month of the KSB Status date.  
   This form is **NOT** an ISO week-date (`YYYY-Www-D`) representation.  
   Implementations SHALL **NOT** substitute the ISO week-numbering year for `yyyy`.

   **Year-boundary behavior:** Near a calendar-year boundary, `yyyy.mm` SHALL use calendar year/month of the KSB Status date, while `ww` SHALL use the ISO-8601 week-of-year number (which may belong to an adjacent ISO week-numbering year). The ISO week-numbering year SHALL NOT overwrite `yyyy`.

   The public weekly image SHALL display only the compact date value (or an approved compact label containing that value).  
   The public weekly image SHALL **NOT** contain:

   - `yyyy` / `mm` / `ww` definitions;  
   - ISO-8601 explanations;  
   - week-number calculation notes;  
   - template filename/path;  
   - local filesystem information;  
   - renderer-development information;  
   - other engineering metadata prohibited by §25A.  

   Do **not** create separate ordinary weekly variables for year, month, and week unless a later CONTROL requires them.  
   The controlled public value remains the single VARIABLE `STATUS_DATE`.

4. **Week-of-year (`ww`) algorithm authority (CWC-CE-082):** The Human Engineer authorizes **ISO-8601 week-of-year numbering** for the `ww` component only.  
   A deterministic renderer **MAY** calculate `ww` mechanically from the KSB Status date under ISO-8601 week rules.  
   Human-supplied complete `STATUS_DATE` values in `yyyy.mm.ww` form remain valid when they conform to this convention.  
   No other week-number algorithm (Sunday-start, Monday-start-without-ISO, first-full-week variants outside ISO-8601, etc.) is authorized for this package class unless a later CONTROL expressly replaces this rule.

5. FIXED visual elements (layout, typography, colors, titles, Bill title strings, Value Stream layout, motto, GitHub breadcrumb structure, PUBLIC URL region, and other HE-approved visuals) SHALL NOT change during an ordinary weekly cycle.  
6. Anti-drift validation is required before package acceptance. Failure stops publication.  
7. Deterministic rendering (SVG or HTML/CSS→PNG or repository-authorized equivalent) is the intended mature method. Generative-image text rendering SHALL NOT be the authoritative renderer for controlled text or percentages.  
8. Baseline ingest and renderer implementation require separately authorized CWCs when not already present.

---

## 25A. Public Image Content Boundary (CWC-CE-081)

### 25A.1 Engineering Metadata ≠ Public Image Content

Engineering/configuration metadata MAY exist in baseline acceptance records, manifests, renderer configuration, controlled documentation, repository README files, and validation artifacts.

It SHALL **NOT** be rendered on ordinary public weekly-status images merely because it is needed to engineer or validate the template.

```text
ENGINEERING METADATA
≠
PUBLIC IMAGE CONTENT
```

Only explicitly authorized public content may appear on the public weekly image.

### 25A.2 Public-Image Exclusions

Ordinary public weekly-status images SHALL **NOT** display:

1. local template filename;  
2. local template path;  
3. drive letters;  
4. `X:\GitHub` (or other local filesystem) paths;  
5. filesystem instructions;  
6. date-format explanation / `yyyy` / `mm` / `ww` definitions;  
7. example-date explanation;  
8. template-development notes;  
9. renderer-development notes;  
10. control-development notes.  

The intended public weekly image ends with the approved public footer containing public-facing branding/content.  
Development-metadata regions beneath that footer are outside the public-image composition and SHALL be removed before baseline acceptance.

This section defines the requirement. Cleaning/cropping a Human-supplied candidate image requires separately authorized baseline-ingest work.

### 25A.3 Template File Identity (Engineering Configuration)

| Property | Value |
|---|---|
| Template source filename | `BL-Weekly-Status-Template-v1.0.png` |
| Intended local template path | `Engineering-Office/publication/weekly-status/templates/BL-Weekly-Status-Template-v1.0.png` |
| Controlled accepted baseline identity (conceptual) | `BL-WEEKLY-STATUS-BASELINE-v1.0` |

Template filename/path are **engineering/template configuration**.  
They SHALL **NOT** appear on the public image.  
Presence of a template file does **not** close GAP-WS-003; baseline ingest requires a Human-approved cleaned public composition under separately authorized CWC.

### 25A.4 GitHub Breadcrumb and Repository Terminology

1. A thin public GitHub breadcrumb immediately above the `BlueprintLiberty.com` footer is an authorized public concept.  
2. Its purpose is to help a reader find the minimum GitHub location(s) needed to inspect controlled public evidence.  
3. The public image may use `Repo` provided it also includes the explanatory relationship:

   ```text
   Constitutional-Engineering Repo
   =
   Constitutional-Engineering Repository
   ```

4. Do **not** use the form `Repo (Repo)`.

### 25A.5 Acronym Readability

Where public-facing acronyms are used, the public image SHALL provide enough context for a reasonable reader to determine their meaning without requiring private engineering knowledge.  
Visual redesign is not authorized solely by this clause; baseline/ingest CWCs reconcile the accepted composition.

---

## 26. Bill Title Pins (Public FIXED Copy)

Human-approved public FIXED Bill titles for weekly-status display (CWC-CE-081):

| Bill | Public FIXED title |
|---|---|
| Bill A | `COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT` |
| Bill B | `KANSAS PROPERTY-TAX ELIMINATION` |
| Bill C | `KANSAS NBEF ACT` |

Controlled Bill C identity expansion (public readability):

```text
Kansas NBEF Act
(Node-Based Educational Framework)
```

1. These are **public weekly-status title pins**, not legislative acceptance.  
2. They do not create or accept an NBEF LOU/SPEC or tax LOU acceptance.  
3. Changing a Bill title pin requires Human Engineer authorization through controlled change.  
4. If a supplied visual mockup conflicts with these pins, do **not** silently edit the mockup; stop for Human disposition.

---

## 27. Percentage Authority

1. `BILL_A_PERCENT`, `BILL_B_PERCENT`, and `BILL_C_PERCENT` are ordinary weekly VARIABLE fields for Weekly Public Engineering Status packages.

2. When **WSMAT-001 — KSB Status Maturity Measurement** is Active:
   1. Authorized AI evaluators SHALL produce **CALCULATED MATURITY** by applying Active WSMAT-001 to a recorded evidence snapshot.
   2. CALCULATED MATURITY is non-operative for package VARIABLE fields until the Human Engineer issues **CERTIFIED KSB MATURITY** for that KSB Status cycle (ACCEPT or MODIFY).
   3. REJECT returns the cycle to recalculation or Human disposition; silence is not certification.
   4. If Human MODIFIES a value, the package/certification record SHALL retain both calculated and certified values and a brief disposition reason.
   5. Algorithm, weighting, stage model, and gate rules SHALL NOT be silently altered; changes require controlled ECR/STD/WSMAT amendment.

3. When WSMAT-001 is **not** Active, percentages SHALL be **HUMAN-SUPPLIED** or **HUMAN-APPROVED** only.

4. AI/ChatGPT MAY measure and propose; AI SHALL NOT certify, satisfy Human Gates, invent evidence, bypass hard gates, or publish uncertified maturity.

5. Bill identifiers used in maturity calculation SHALL match STD-011 §26 public Bill title pins and the same legislative object across LOU/SPEC/CWC/drafting/Git/publication. WSMAT-001 activation requires Bill A/B identity integrity as required by ECR-005.

6. Provisional/sample percentages produced before WSMAT-001 Active (including any CWC-CE-085 provisional values) are **not grandfathered**. The first cycle under Active WSMAT-001 SHALL recalculate Bills A/B/C from zero.

7. Detailed stage criteria, hard-gate ceilings, rounding (`round_half_up` of `100 × credited_stage_units / 13`), and evidence-snapshot requirements are normative in Active WSMAT-001 and are incorporated by reference.

---

## 28. PUBLIC URL REQUIREMENT

Every Weekly Public Engineering Status package SHALL expose the Human-approved PUBLIC NAVIGATION URL set in **both**:

1. the Markdown weekly status report; and  
2. the corresponding public weekly status image.

### 28.1 Initial PUBLIC URL PIN

| Slot | Display Label | Destination Intent |
|---|---|---|
| `PUBLIC_URL_01` | `BlueprintLiberty.com` | Human-approved BlueprintLiberty public website |

Initial authorized set contains only `PUBLIC_URL_01`. Unused slots SHALL NOT be displayed.

### 28.2 Markdown URL Requirement

1. The Markdown report SHALL include a clearly identifiable public navigation section (preferred heading: `Learn More / Project URLs`, or equivalent).  
2. Each enabled PUBLIC URL SHALL appear as a usable Markdown hyperlink.  
3. Display text for `PUBLIC_URL_01` SHALL be `BlueprintLiberty.com`.  
4. PUBLIC NAVIGATION URLS SHALL NOT be confused with ENGINEERING EVIDENCE URLS.

### 28.3 Image URL Requirement

1. The weekly status image SHALL visibly display each enabled PUBLIC URL as human-readable controlled text.  
2. For the initial baseline, `BlueprintLiberty.com` SHALL appear in the controlled visual URL/footer region.  
3. Long GitHub URLs SHALL NOT substitute for the public project URL on the image.  
4. Engineering evidence URLs belong in the report/manifest as appropriate, not as replacements for PUBLIC NAVIGATION URLS.

### 28.4 PUBLIC NAVIGATION vs ENGINEERING EVIDENCE

| Class | Purpose |
|---|---|
| PUBLIC NAVIGATION URLS | Human-approved project destinations for the public |
| ENGINEERING EVIDENCE URLS | Repository commits, controlled documents, evidence references, traceability links |

These classes SHALL NOT be conflated.

### 28.5 URL Control / Configuration Model

Candidate logical slots: `PUBLIC_URL_01`, `PUBLIC_URL_02`, `PUBLIC_URL_03`, …

Minimum deterministic properties per enabled slot:

| Property | Rule |
|---|---|
| `slot_id` | e.g. `PUBLIC_URL_01` |
| `display_label` | Human-readable label (e.g. `BlueprintLiberty.com`) |
| `destination_url` | Human-approved destination corresponding to the public website |
| `order` | Display order among enabled slots |
| `enabled` | `true` / `false` (disabled slots not displayed) |

PUBLIC URL values are **controlled configuration / baseline content**, not ordinary weekly maturity variables.

### 28.6 URL Authority

An ordinary weekly cycle SHALL NOT invent, add, remove, rename, reorder, redirect, or substitute a PUBLIC URL.  
Such changes require Human Engineer authorization through the applicable controlled change mechanism (ECR / CWC as required).

---

## 29. Weekly Git and Publication Boundaries

1. Creating weekly package files does **not** authorize stage, commit, push, or publication.  
2. Git Commit requires Human Engineer approval under WF-001 HG-4.  
3. Git Push requires Human Engineer approval under WF-001 HG-5.  
4. Publication requires explicit Human Publication Approval under WF-001 HG-6.  
5. STD-002 remains Reserved unless later activated; operators follow WF-001 + POL-001 + HE Git gates.  
6. ChatGPT ↔ GitHub ↔ Cursor interchange capability (CWC-CE-074) does **not** grant unrestricted write authority.  
7. Automatic Facebook / X / Substack / website posting, scheduled publication, and autonomous AI publication are **not** authorized by this standard.

---

## 30. Weekly Human Authorization Points

| Step | Authorization required |
|---|---|
| Trigger weekly preparation | Approved CWC-CE or explicit HE command under controlling CWC |
| Accept evidence digest / candidate narrative / percentages | Human Engineer |
| Accept weekly package (Markdown + image + manifest) | Human Engineer package acceptance |
| Stage/commit weekly package | HG-4 / explicit HE commit authorization |
| Push to remote | HG-5 / explicit HE push authorization |
| Publish to platforms | HG-6 / explicit HE publication authorization |
| Change PUBLIC URL set or Bill title pins | Human Engineer controlled change |
| Change visual baseline | Human Engineer controlled baseline ingest/replacement |

Silence is not authorization.

---

## 31. Baseline Ingest Requirement

1. Controlled image packages require an HE-approved baseline under `baseline/`.  
2. Conceptual baseline identity: `BL-WEEKLY-STATUS-BASELINE-v1.0` (exact filename per ingest CWC).  
3. Baseline SHALL define or include controlled visual regions for:

   - `BlueprintLiberty.com` (PUBLIC_URL_01 display)  
   - `STATUS_DATE`  
   - `BILL_A_PERCENT`  
   - `BILL_B_PERCENT`  
   - `BILL_C_PERCENT`  

4. This standard does **not** fabricate the Human-approved mockup.  
5. Absence of an accepted baseline is a hard prerequisite gap for controlled image production.

---

## 32. Deterministic Renderer Authority Position

1. Sufficient packaging CONTROL now exists for a **later** CWC to implement a deterministic renderer after baseline ingest.  
2. Minimum renderer target: approved baseline/template + approved controlled configuration + approved weekly variables → deterministic weekly image.  
3. Preferred: SVG or HTML/CSS → PNG.  
4. Renderer implementation is **out of scope** for CWC-CE-078 when no Human-supplied approved baseline is present.

---

## 33. POC vs Recurring Production

1. A phone POC CWC does not authorize recurring weekly production.  
2. A successful phone POC does not authorize scheduled automation or autonomous publication.  
3. Recurring production requires HE-authorized standing process under this standard plus applicable CWC triggers.

---

## 34. Weekly-Status Disclaimers (Minimum)

Weekly Public Engineering Status packages shall not imply:

1. Legal enactment  
2. Constitutional amendment  
3. Legislative acceptance of Bill A / Bill B / Bill C / NBEF  
4. Controlled Execution authorization  
5. That public representation supersedes controlled repository evidence  
6. That AI approval replaces Human Engineer approval  

---

## 35. Relationship to Informational Artifacts

| Artifact | Role |
|---|---|
| WSPC-001 | Informational production-contract definition |
| README-PUB-WEEKLY-001 | Informational architecture / directory note |
| WSGAP-001 | Informational gap-closure / design record |
| ECR-004 | Change authorization for Part B |
| ECR-007 | Change authorization for Part B §36 phone-command orchestration |
| ECR-008 | Change authorization for Part B §36 KSB Sunday Publication Package / single-command complete package |
| KSB-ORCH-001 | Operative phone-command / follow-up / Sunday-package orchestration procedure (under ECR-007 / ECR-008) |
| KSB-PR-TMP-001 | Operative KSB press-release structure template (under ECR-008) |
| STD-011 Part B | Operative packaging CONTROL for weekly-status packages |

Informational artifacts remain non-operative unless later Human-authorized promotion occurs through controlled process.

---

## 36. Phone-Command Orchestration and Follow-Up Context

**Governing procedure:** Active **KSB-ORCH-001 — KSB Phone-Command Orchestration Procedure**.  
**Governing ECR:** ECR-007; ECR-008; ECR-011; **ECR-012**.

### 36.1 Human trigger

The Human command:

```text
Prepare KSB Status
```

(and authorized equivalents such as “Prepare this week’s BlueprintLiberty status”) establishes an **Active KSB Cycle Context** under Active KSB-ORCH-001 and begins the **KSB Sunday Publication Package** (§36.9) under the **three-step Human command contract** (§36.11).

Ordinary controlled sequence (Human need not recite plumbing):

```text
Prepare KSB Status
 → CONTROLLED KSB STATUS   (stop)
 → Next
 → ≈500-WORD PRESS RELEASE (stop)
 → Next
 → CONTROLLED KSB IMAGE (baseline → deterministic renderer → anti-drift / bridge)
 → PACKAGE VALIDATION (COMPLETE when all three products returned)
 → STOP FOR HUMAN REVIEW/PUBLICATION
```

`Prepare KSB Status` SHALL return the controlled **STATUS** product and **stop**. It SHALL NOT automatically return the press release or controlled image, and SHALL NOT create a render Issue solely because Step 1 was invoked.

The Human SHALL NOT be required to manage GitHub Issues, Actions runs, artifacts, correlation identifiers, or renderer plumbing during ordinary successful progression. Technical ceremony remains behind the commands. Human certification, Git, and publication gates remain where this standard and WF-001 require them. Preparation does **not** authorize HG-6 publication.

### 36.2 Active-cycle follow-up context

While the cycle is Active, follow-up requests concerning the status, report, image, graphic, press release, social-media post, weekly update, Facebook post, publication material, or supporting media SHALL retain that cycle’s controlled artifact identity **without** requiring the Human to repeat the trigger phrase.

An Active cycle ends when:

1. the workflow is completed and the Human closes the cycle; **or**  
2. the Human explicitly changes subject/workflow; **or**  
3. another controlled workflow supersedes it; **or**  
4. the Human explicitly requests a separate artifact class (e.g., distinct creative artwork); **or**  
5. a new `Prepare KSB Status` starts a **new** cycle (prior cycle preserved historically).

### 36.3 Controlled KSB image routing (DEFAULT)

Ambiguous requests for “the image,” “status image,” “weekly image,” “Facebook image,” “social-media image,” “graphic,” “image to support it,” or reasonably equivalent wording DEFAULT to the **CONTROLLED KSB IMAGE**.

The authoritative controlled KSB image SHALL originate from:

```text
ACCEPTED KSB BASELINE
 → AUTHORIZED VARIABLE INPUT
 → DETERMINISTIC RENDERER
 → ANTI-DRIFT VALIDATION
```

Generic / generative image creation SHALL **NOT** substitute for this path as the weekly status image (§25.7 remains binding).

### 36.4 Creative-artwork firewall

```text
CONTROLLED KSB IMAGE
≠
CREATIVE SUPPORTING ARTWORK
```

Creative image generation may occur only when Human intent clearly requests a separate creative artifact (for example: “Create a separate political satire image,” “Give me another illustration,” “Make a new artistic image about property taxes”).  

Such artwork SHALL be labeled as **not** the controlled KSB status image and SHALL NOT replace or inherit KSB engineering authority.

### 36.5 Renderer failure-safe (mandatory)

If the ChatGPT/phone (or other) execution environment cannot invoke the authorized deterministic renderer:

```text
KSB IMAGE: RENDER REQUIRED
PACKAGE STATE: INCOMPLETE
```

(or the exact authorized equivalent under KSB-ORCH-001).

The operator SHALL preserve controlled status values, baseline identity, rendering requirement, and workflow context, and SHALL identify the controlled render bridge (e.g., Cursor / local CE-Engineer / authorized interchange). Status and press release may be prepared where otherwise authorized. The package **cannot** become COMPLETE without the controlled image.

**Substituting generative/creative artwork and presenting it as the KSB status image is prohibited.**  
A visible incomplete controlled workflow is preferable to a visually complete uncontrolled artifact.

### 36.6 Press release (ordinary deliverable + follow-up)

Under `Prepare KSB Status`, a press release is a **mandatory ordinary deliverable** of the KSB Sunday Publication Package (§36.9), not merely an optional follow-up.

1. Target length: approximately **500** words; controlled tolerance **450–550** words.  
2. Structure: Active **KSB-PR-TMP-001**.  
3. Facts SHALL derive from the controlled KSB status and canonical evidence only.  
4. Path convention: `press-releases/YYYY-MM-DD-BlueprintLiberty-KSB-Press-Release.md`.  
5. Follow-up requests (e.g., “Create a press release and image to support it,” “Shorten the press release”) remain valid for editorial refinement within the Active cycle.  
6. If rendering is unavailable, report `KSB IMAGE: RENDER REQUIRED` and `PACKAGE STATE: INCOMPLETE`; do **not** generate a replacement infographic as the status image.

Press-release text is publication/supporting prose and does **not** become engineering truth. It SHALL NOT silently alter percentages, Bill identities, status date, maturity meaning, or certification state.

```text
CONTROLLED REPOSITORY EVIDENCE
 → CONTROLLED STATUS
 → PRESS RELEASE
```

Never reverse. Inconsistent derived claims SHALL be rejected or corrected; controlled evidence wins.

### 36.7 Social-media follow-up

During an Active cycle, requests such as “Give me the image for Facebook,” “Prepare the Facebook post,” or “Give me the social-media status” remain bound to the controlled KSB cycle unless the Human explicitly requests a separate creative artifact.

A social-media package may contain: controlled KSB image (or RENDER REQUIRED state); controlled status values; Human-reviewable supporting prose / press release; controlled public URL; controlled status date.  

Social-media publication (WF-001 HG-6) does not modify engineering evidence and is not authorized by this section alone.

### 36.8 Procedure detail

Operator states, cycle field inventory, phone-first ceremony rules, COMPLETE/INCOMPLETE classification, and scenario routing detail are controlled by Active **KSB-ORCH-001**. Conflicts between informal operator guidance and this section escalate to the Human Engineer; this section and §25 control packaging truth.

### 36.9 KSB Sunday Publication Package

**Package identity:** `KSB Sunday Publication Package` — ordinary weekly Human-reviewable publication set within the Weekly Public Engineering Status package class.

| Deliverable | Requirement |
|---|---|
| A — Controlled KSB Status | Manifest + Markdown report (§22–§24); evidence-derived; maturity ≠ political probability |
| B — Press release | ≈500 words (450–550); KSB-PR-TMP-001; derived from controlled status (§36.6) |
| C — Controlled KSB Status Image | Accepted baseline → four VARIABLES → deterministic renderer → anti-drift PASS (§25 / §36.3–§36.5) |

**COMPLETE** only if all are true:

1. controlled status exists;  
2. required maturity certification for the cycle is satisfied;  
3. press release exists within controlled requirements and reconciles with controlled status/evidence;  
4. controlled KSB image exists;  
5. deterministic renderer validation passes;  
6. anti-drift validation passes;  
7. required manifest/package references are present (§23);  
8. applicable package validation passes.

If any mandatory condition fails:

```text
PACKAGE STATE: INCOMPLETE
UNRESOLVED: <exact component>
```

Generative/creative substitution SHALL **NOT** convert INCOMPLETE → COMPLETE.

**Human certification continuity:** If certification is required mid-cycle, the workflow may stop at `HUMAN CERTIFICATION REQUIRED`. After the Human decides, the **same** Active KSB Cycle continues toward the complete Sunday package without requiring the Human to repeat `Prepare KSB Status` or separately request the press release/image.

**Publication gate:** Successful package preparation ends at Human review/publication required. `Prepare KSB Status` does not itself publish.

### 36.10 Human acceptance / complete-package contract (amended by ECR-011 / CWC-CE-092)

The **KSB Sunday Publication Package** (§36.9) remains COMPLETE only when the Human has received all three products (status + press release + controlled image). Infrastructure partial PASS ≠ package COMPLETE.

Under the three-step contract (§36.11):

- Step-1 command success = STATUS product correctly returned (not full package).  
- Step-2 command success = PRESS RELEASE returned from the same package identity.  
- Step-3 command success = CONTROLLED IMAGE returned (or truthful IN PROGRESS / BLOCKED).  
- Package readiness for Human review/publication requires all three products.

```text
SUNDAY PACKAGE COMPLETE ≠ SINGLE-COMMAND PREPARE DELIVERY
PARTIAL PACKAGE ≠ PACKAGE COMPLETE
RUNTIME / BRIDGE DIAGNOSTIC ≠ PACKAGE SUCCESS
IMAGE_GEN ≠ CONTROLLED KSB IMAGE
```

Press release remains a required package component and SHALL NOT be blocked by image queue/failure. Status SHALL NOT be blocked by image production.

### 36.11 Three-step Human command contract (ECR-011 / CWC-CE-092)

Canonical Human sequence:

```text
Prepare KSB Status → STATUS
Next → PRESS RELEASE (~450–550 words)
Next → CONTROLLED IMAGE
```

| Active package condition | `Next` means |
|---|---|
| STATUS complete; press release not returned | Return PRESS RELEASE (no render Issue) |
| Press release complete; image not returned | Enter controlled image path (at most one render request) |
| Image IN PROGRESS | Reconcile **existing** request; no duplicate Issue |
| Package COMPLETE | Report complete / Human review required; do **not** start a new weekly cycle |

Package continuity across steps SHALL preserve: cycle identity; status date; Bill A/B/C; certification/evidence basis; baseline ID; renderer ID; canonical SHA where applicable; render request ID once created.

**KSB-089-D01:** SUPERSEDED by this three-step model (not the parked “Continue KSB Status” design).

### 36.12 Human-product presentation (ECR-012 / CWC-CE-094)

| Step | Human product | Presentation rule |
|---|---|---|
| 1 | STATUS | Displayed directly in the ChatGPT reply |
| 2 | PRESS RELEASE | Entire publishable text in **exactly one** copyable text/code box |
| 3 | CONTROLLED IMAGE | Controlled PNG displayed **inline** in the reply |

GitHub Actions ZIP/artifact / RESULT.json / hashes remain **engineering evidence**. They SHALL NOT be the ordinary primary Human-facing substitute for the visible PNG.

### 36.13 Fresh deterministic composition (ECR-012 / CWC-CE-094) — HISTORICAL

Weekly controlled images under ECR-012 used:

```text
CONTROLLED BASELINE (appearance / anti-drift reference)
+ CLEAN VARIABLE PLATES (plate_rgb / track_rgb)
+ CURRENT CONTROLLED VARIABLES
→ DETERMINISTIC COMPOSITOR
→ NEW PNG
```

Ordinary weekly composition SHALL NOT depend on Telea inpaint. ECR-012 prohibited painting-over prior weekly output files. Historical placeholder raster inside the accepted baseline PNG was cleared by solid plate fill before current values were drawn.

**Supersession:** Ordinary weekly architecture under **ECR-013 / CWC-CE-096** (§36.14) replaces plate-over-populated-baseline as the authorized ordinary path.

### 36.14 True new-image blank-canvas composition (ECR-013 / CWC-CE-096)

Every ordinary KSB render SHALL create a **new image from scratch**:

```text
Image.new BLANK 1536×912
+ CONTROLLED FIXED LAYER (zero weekly variable ink)
+ CURRENT CONTROLLED VARIABLES ONLY
→ DETERMINISTIC COMPOSITOR
→ NEW PNG
```

PROHIBITED as ordinary composition canvas:

1. previous weekly KSB output PNG;  
2. populated `BL-WEEKLY-STATUS-BASELINE-v1.0`;  
3. any architecture whose primary method is erase / cover / inpaint / enlarge-mask of historical weekly variable pixels on a populated raster.

Historical weekly variable pixels on the new canvas before current variables are drawn SHALL be **zero** (never drawn — not merely masked).

Anti-drift for ordinary renders SHALL compare against the controlled **fixed layer** (authorized variable rectangles only).

Candidate renderer identity for this change: `ksb_renderer@2.0.0-CWC-CE-096-CANDIDATE`.  
Automated test PASS does **not** constitute operational acceptance; Human visual acceptance is required before activation.

**Supersession:** CWC-CE-096 Human visual acceptance = REJECTED. Ordinary path under **ECR-014 / CWC-CE-097** (§36.15) supersedes fixed-layer paste for activation.

Generative image creation SHALL NOT substitute for this path.

### 36.15 Clean master + dynamic center panel (ECR-014 / CWC-CE-097)

Every ordinary KSB render SHALL:

```text
OPEN CLEAN MASTER TEMPLATE (pristine)
→ COPY INTO RENDER MEMORY
→ DYNAMICALLY DRAW KANSAS LEGISLATIVE ENGINEERING STATUS CENTER PANEL
→ WRITE NEW PNG (never overwrite master)
```

The clean master center panel SHALL contain zero Bill A/B/C weekly status rendering before composition. Progress tracks begin empty; fills and percentages are functions of current controlled maturity only.

Candidate renderer: `ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE`.  
Human visual acceptance required before operational activation.

Generative image creation SHALL NOT substitute for this path.
