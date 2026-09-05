# Phone-First Public-Review PDF Rendering Standard (CWC-CE-161)

**Document ID:** PR-PDF-RENDER-001  
**Governing Work Card:** CWC-CE-161  
**Status:** ACTIVE for Bill A public-review candidate PDFs  
**Reuse:** Designed for later Bill A revisions, SPEC review artifacts, Bill B/C, and other CE public-review documents — without becoming a full publication platform.

---

## 1. Authority model

```text
CANONICAL GITHUB EVIDENCE
→ CONTROLLED PDF RENDERING
→ PDF VALIDATION
→ HUMAN VISUAL REVIEW
→ EXTERNAL HUMAN REVIEW
```

PDFs are **derived review artifacts**. They are **not** Definition source truth.

Never:

```text
FACEBOOK PDF → ENGINEERING TRUTH
```

---

## 2. Toolchain (deterministic)

| Layer | Choice |
|---|---|
| Language | Python 3 |
| Layout engine | ReportLab |
| PDF inspection | PyMuPDF (`pymupdf`) |
| Source format | Canonical Markdown in Git |
| Primary entrypoint | `renderer/render_phone_first_pdf.py` |
| Validation entrypoint | `renderer/validate_ce161.py` |

**Not authoritative:** manual Word editing.

**Optional / non-primary:** pandoc + XeLaTeX files retained under `renderer/` (`prepare_phone_first_md.py`, `phone-first-header.tex`, `render_bill_a_public_review.py`) for experimentation. Bill A CWC-CE-161 production artifacts were generated with ReportLab after XeLaTeX/MiKTeX interactive install hangs on this host.

### Dependencies (local)

```text
pip install reportlab markdown pymupdf
```

---

## 3. Page geometry

| Parameter | Value |
|---|---|
| Page size | **6 in × 9 in** portrait (432 × 648 pt) |
| Margins | ≈ 0.55 in (bottom ≈ 0.65 in for footer) |
| Orientation | Portrait |

---

## 4. Typography / readability

| Rule | Value |
|---|---|
| Body font | Helvetica 10.5 pt |
| Body leading | 14.5 pt (~1.38×) |
| H1 / H2 / H3 | 14 / 12 / 11 pt bold |
| Alignment | Justified body; centered cover |
| Contrast | Black text on white; no decorative body background |
| Code / notices | Courier ~8.5–9 pt on light gray panel |
| Prioritization | Readability over packing density |

---

## 5. Heading rules

- Markdown `#` → H1, `##` → H2, `###`/`####` → H3  
- Strong visual hierarchy; spacing before headings preserved  
- Source heading text preserved (no retitling of controlled sections)

---

## 6. Hyperlink handling

- Markdown links and bare `https://` URLs become ReportLab link annotations  
- Cover and control block include clickable:
  - `https://BlueprintLiberty.com`
  - `https://github.com/jhodges07/Constitutional-Engineering`
- Repository URL printed as full human-readable text (no shortener, no mirror)

---

## 7. Table handling

- Compact 2-column tables may remain as tables on the narrow page  
- Wide / multi-column tables are **reformatted** into stacked Field/Value bullet blocks  
- Cell text is copied unchanged  
- A formatting note is inserted: phone-first readability only

---

## 8. Header / footer

- No running header clutter  
- Footer (restrained):
  - Left: `BlueprintLiberty.com`
  - Center: page number
  - Right: short document identity (e.g., `LOU-004 Draft 1.10 | Public Review Candidate`)  
- Full GitHub URL is on the cover/control block (not required on every page)

---

## 9. Cover + document-control + review notice

Both PDFs prepend:

1. Professional cover with required Bill A / status warnings  
2. Document-control block including **full** canonical Git SHA  
3. External-review notice (public review; not law; not proposed legislative text; not Human-accepted; HG-D1 not passed; comments do not auto-alter LOU; Human Engineer retains Human Intent authority)

Summary PDF additionally states: **SUMMARY DOES NOT REPLACE LOU-004**.

---

## 10. Metadata

PDF Info dictionary populated with:

- Title  
- Author (`Constitutional Engineering Office / BlueprintLiberty`)  
- Subject (includes review status / SHA)  
- Keywords (includes NOT HUMAN-ACCEPTED / HG-D1 NOT PASSED)  
- Creator (`CWC-CE-161 phone-first public-review renderer`)

**Forbidden:** “Final Approved” or false acceptance metadata.

---

## 11. Output paths

```text
Engineering-Office/publication/bill-a/public-review/
  renderer/
  pdf/
  validation/
  issue-bridge/
```

Definition sources remain under `Engineering-Office/definition/`.

---

## 12. Reproducibility

From repository root at the verified canonical SHA:

```text
python Engineering-Office/publication/bill-a/public-review/renderer/render_phone_first_pdf.py
python Engineering-Office/publication/bill-a/public-review/renderer/validate_ce161.py
```

The render script **STOP**s if `HEAD` / `origin/main` ≠ expected canonical SHA.

PDF SHA-256 values are recorded in `validation/CWC-CE-161-ARTIFACT-IDENTITY.json`.

---

## 13. Validation method

`validate_ce161.py` checks:

- open / page size / portrait  
- selectable/searchable text  
- required URLs, full SHA, status warnings, Draft 1.10 / summary warnings  
- clickable GitHub link annotations  
- source→PDF heading sample + controlled phrase presence + word coverage  
- phone-readability heuristics on representative pages  

Human visual acceptance remains a **separate** gate (this standard does not authorize Facebook publication).
