# LOU-002 Publication Manifest

**Artifact Class:** Engineering Definition LOU Publication Package Manifest  
**Governing Standard:** STD-011 — Public Documentation  
**Governing CWC-CE:** CWC-CE-068  
**ECR-003 Disposition:** Verified-Closed  

---

## Identity

| Field | Value |
|---|---|
| LOU ID | LOU-002 |
| Title | Constitutional Engineering Master Plan Letter of Understanding |
| Source Version | Draft 0.5 |
| HG-D1 Status | ACCEPTED |
| Acceptance Date | 2026-08-09 |
| Source Authority Status | Authoritative Engineering Definition (accepted Markdown) |
| Derivative Authority Status | Non-authoritative publication derivative |

## Paths

| Field | Value |
|---|---|
| Source Markdown (absolute) | `D:\Constitutional-Engineering\Engineering-Office\definition\LOU-002-Constitutional-Engineering-Master-Plan.md` |
| Source Markdown (repository-relative) | `Engineering-Office/definition/LOU-002-Constitutional-Engineering-Master-Plan.md` |
| PDF Path (absolute) | `D:\Constitutional-Engineering\Engineering-Office\publication\definition\LOU-002\LOU-002-Constitutional-Engineering-Master-Plan-vDraft-0.5-HG-D1-ACCEPTED.pdf` |
| PDF Path (repository-relative) | `Engineering-Office/publication/definition/LOU-002/LOU-002-Constitutional-Engineering-Master-Plan-vDraft-0.5-HG-D1-ACCEPTED.pdf` |
| Package Directory | `Engineering-Office/publication/definition/LOU-002/` |

## Hashes

| Field | Value |
|---|---|
| Source SHA-256 | `b7987b4232ed9d31cf2e65733c1eb946024e0b62f1ddd7f491ab89125739b63b` |
| PDF SHA-256 | `9e89073e42cace382320392d19eea334425c1a270339f6c2ca3eed17091feba5` |
| Prior CWC-CE-067 Source SHA-256 Match | PASS |

## Generation

| Field | Value |
|---|---|
| Method | Pandoc Markdown → PDF via XeLaTeX |
| Pandoc Version | 3.10.1 |
| PDF Engine | xelatex |
| PDF Engine Version | MiKTeX-XeTeX 4.16 (MiKTeX 25.12) |
| Main Font | Segoe UI (selected to preserve Unicode glyphs including ≠ and ↔) |
| Generation Datetime | 2026-08-09T16:05:37-05:00 (PDF LastWriteTime local) |
| Cover Identity Input | `_generation-cover.md` (package-local; does not modify accepted LOU Markdown) |
| Publication Authorization Status | NOT AUTHORIZED (local package only; awaiting Human publication review) |

### Generation Command

```text
pandoc
  Engineering-Office/publication/definition/LOU-002/_generation-cover.md
  Engineering-Office/definition/LOU-002-Constitutional-Engineering-Master-Plan.md
  -o Engineering-Office/publication/definition/LOU-002/LOU-002-Constitutional-Engineering-Master-Plan-vDraft-0.5-HG-D1-ACCEPTED.pdf
  --pdf-engine=xelatex
  -V geometry:margin=1in
  -V documentclass=article
  -V mainfont="Segoe UI"
  --from=markdown
  --toc
  --toc-depth=2
```

### MiKTeX Dependency Note

Initial generation attempt with `MIKTEX_AUTOINSTALL=0` hung awaiting packages. Production generation used `MIKTEX_AUTOINSTALL=1` / `MIKTEX_UNATTENDED=1` for normal MiKTeX dependency resolution under CWC-CE-068 §10. No separate software installer was run by the agent. Unicode glyph warnings under Latin Modern were remediated by regenerating with `mainfont=Segoe UI` (zero remaining “Missing character” warnings).

## Verification

| Field | Value |
|---|---|
| Verification Result | Pass |
| Verification Record | `LOU-002-Constitutional-Engineering-Master-Plan-vDraft-0.5-HG-D1-ACCEPTED.verification.md` |
| Governing Publication Control | STD-011 |
| Traceability CWC | CWC-CE-068 |

---

**Markdown remains authoritative. This PDF is a publication derivative only.**
