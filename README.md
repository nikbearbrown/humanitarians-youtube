# Humanitarians AI YouTube Production Library

This repository contains the non-MP3, non-MP4 materials used to research, script, assemble, and quality-check Humanitarians AI video projects. It mirrors the YouTube production tree maintained at `books/humanitarians_html/youtube` in the Bear Textbooks workspace.

The repository is intended to preserve production provenance and make projects inspectable without storing final MP3 or MP4 renders.

## Main collection

### `claude/`

The consolidated Claude and AI video archive. It contains approximately 155,000 files and more than 5,600 beat-sheet variants.

The directory has two broad forms of content:

- `claude/_collected/` preserves projects imported from other books and production workspaces using their original relative paths.
- Direct children of `claude/` are Humanitarians AI production folders maintained as first-class projects, including profiles, explainers, and topic-driven videos.

The preserved hierarchy prevents naming collisions and records where each collected project originated.

## Root production documents

The repository root may also contain batch manifests, build logs, project-idea documents, and production scripts. These files describe work across multiple video folders and should be read before rebuilding or reorganizing a batch.

## Typical project anatomy

A production folder may include:

- `beat_sheet.json` plus voice, brand, short-form, or alternate-cut variants
- `FACTCHECK.md`, `PEDAGOGY.md`, `PROMPTS.md`, `SHOTLIST.md`, `SOURCES.md`, or related editorial documents
- Python or JavaScript scene and rendering code
- `clips/manifest.json`, timing data, and concatenation files
- image, diagram, SVG, typography, and supporting assets under `media/`
- `_qc/` frames, overview sheets, layout audits, and final QC reports
- build prompts, status notes, receipts, citations, and publication metadata

The exact contents vary by project and production generation. Some directories are complete builds; others are source packages, alternates, or retained QC snapshots.

## Finding a project

```bash
# Find profile projects
find claude -type d -iname '*profile*'

# Find a person or topic across all production text
rg -i 'Aditi Deodhar|Aravind Balaji|responsible AI' claude

# List primary beat sheets
find claude -name 'beat_sheet.json'

# Find source and fact-check documents
find claude -type f \( -name 'SOURCES.md' -o -name 'FACTCHECK.md' \)

# Locate quality-control artifacts
find claude -type f \( -iname '*qc*' -o -iname '*audit*' \)
```

## Media policy

The root `.gitignore` excludes:

```gitignore
*.mp3
*.mp4
```

Directories named `mp3/` may contain tracked JSON timing files; these are metadata, not audio. Other supporting formats—including PNG, JPEG, SVG, M4A, Markdown, JSON, and source code—may be included when they are part of the production package.

## Working safely

1. Read the beat sheet and editorial notes before changing a project.
2. Check source, fact-check, and pedagogy documents for claims and intent.
3. Use timing and manifest files to understand beat-to-asset relationships.
4. Inspect QC frames and layout reports before accepting visual changes.
5. Preserve the collected source hierarchy when adding projects from elsewhere.
6. Keep final MP3 and MP4 renders outside this repository.
7. Avoid assuming that generated files are canonical when hand-authored source files are available.

## Repository scope

This is a production archive for Humanitarians AI YouTube work. It is not the Humanitarians AI website, not a deployment repository, and not a storage location for finished video distribution files.

