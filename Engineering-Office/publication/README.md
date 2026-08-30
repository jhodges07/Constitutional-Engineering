# Engineering Office Publication Surface

**Document ID:** README-PUB-001  
**Title:** Engineering Office Publication Directory README  
**Classification:** Informational Directory Note  
**Authority:** Constitutional Engineering Office  
**Governing Standard:** STD-011 — Public Documentation (Part A LOU packages; Part B Weekly Public Engineering Status packages)  
**Governing Change:** ECR-003 — Engineering Definition LOU Publication-Package Control; ECR-004 — Weekly Public Engineering Status Publication Control  
**Governing Work Card:** CWC-CE-066; CWC-CE-078  
**Status:** Active  
**Version:** 1.1.0  
**Effective Date:** 2026-08-30  

---

## Purpose

This directory is the controlled **publication surface** for non-authoritative publication derivatives and public-status packages governed by STD-011.

Path root:

```text
Engineering-Office/publication/
```

---

## Authority Boundary

1. Files under this directory are **not** Engineering Definition LOU sources (except as expressly stated for LOU PDF derivatives vs Markdown authority).  
2. Accepted LOU Markdown under `Engineering-Office/definition/` remains authoritative for LOUs.  
3. LOU PDF files here are publication derivatives only.  
4. Weekly-status Markdown/image packages are public-status records / controlled representations, not LOU sources and not engineering-truth sources.  
5. Presence of files here does **not** authorize Git push or public release.  
6. Legislative KLS publication standards are not LOU or weekly-status authority under this surface.

---

## Engineering Definition LOU Derivatives (STD-011 Part A)

LOU PDF packages are stored at:

```text
Engineering-Office/publication/definition/LOU-NNN/
```

Naming, manifests, verification, and Git/publication gates are defined by STD-011 Part A.

---

## Weekly Public Engineering Status Packages (STD-011 Part B)

Weekly-status packages are stored at:

```text
Engineering-Office/publication/weekly-status/
```

Architecture note: `weekly-status/README.md` (README-PUB-WEEKLY-001 — informational).  
Operative packaging CONTROL: **STD-011 Part B**.  
Informational production contract: WSPC-001.  
PUBLIC URL REQUIREMENT: every package exposes Human-approved PUBLIC NAVIGATION URLS in Markdown and image; initial pin `PUBLIC_URL_01` = BlueprintLiberty.com.

---

## Current Contents

This README establishes the publication surface.

Individual LOU publication packages and weekly-status packages are created only under separately authorized CWC-CE work after applicable verification and Human gates.

---

## Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial publication-surface README under ECR-003 / CWC-CE-066. |
| 1.1.0 | 2026-08-30 | ECR-004 / CWC-CE-078: catalog weekly-status package class and PUBLIC URL pointer; preserve LOU Part A surface. |
