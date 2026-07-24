# Humanitarians YouTube Production Library

This repository contains educational and public-interest YouTube production materials maintained under `books/humanitarians_html/youtube`. It preserves the source files needed to inspect, edit, fact-check, rebuild, review, and publish videos while keeping credentials and large distribution media out of Git.

## Organization

Most subject collections use the naming convention:

```text
claude-for-<topic>/<video-project>/
```

The three intentional top-level exceptions are:

- `claude/` — Claude-specific productions
- `codex/` — Codex-specific productions
- `fellows/` — Humanitarians AI fellow profiles and showcases

A video project is normally one directory containing its `beat_sheet.json` and supporting production artifacts. Source-course names are added only when necessary to prevent collisions.

## Current collections

As of **July 24, 2026**, the current filesystem contains **3,950** primary `beat_sheet.json` files, **3,958** beat-sheet JSON files including named variants, and **3,993** README files across **22** top-level collections. Each linked collection README inventories its videos and derives its present production state from the files on disk.

| Directory | Collection | Beat sheets |
|---|---|---:|
| [`claude-for-artificial-intelligence/`](claude-for-artificial-intelligence/) | Artificial Intelligence | 219 |
| [`claude-for-branding/`](claude-for-branding/) | Branding | 34 |
| [`claude-for-business/`](claude-for-business/) | Business | 1 |
| [`claude-for-cancer/`](claude-for-cancer/) | Cancer | 55 |
| [`claude-for-cancer-biology/`](claude-for-cancer-biology/) | Cancer Biology | 226 |
| [`claude-for-computer-science/`](claude-for-computer-science/) | Computer Science | 91 |
| [`claude-for-design/`](claude-for-design/) | Design | 464 |
| [`claude-for-economics/`](claude-for-economics/) | Economics | 41 |
| [`claude-for-education/`](claude-for-education/) | Education | 81 |
| [`claude-for-finance/`](claude-for-finance/) | Finance | 52 |
| [`claude-for-general-education/`](claude-for-general-education/) | General Education | 52 |
| [`claude-for-marketing/`](claude-for-marketing/) | Marketing | 36 |
| [`claude-for-mathematics/`](claude-for-mathematics/) | Mathematics | 22 |
| [`claude-for-music/`](claude-for-music/) | Music | 28 |
| [`claude-for-nanomedicine/`](claude-for-nanomedicine/) | Nanomedicine | 119 |
| [`claude-for-physics/`](claude-for-physics/) | Physics | 6 |
| [`claude-for-quantum-mechanics/`](claude-for-quantum-mechanics/) | Quantum Mechanics | 538 |
| [`claude-for-video-production/`](claude-for-video-production/) | Video Production | 74 |
| [`claude-for-writing/`](claude-for-writing/) | Writing | 31 |
| [`claude/`](claude/) | Claude | 1,737 |
| [`codex/`](codex/) | Codex | 40 |
| [`fellows/`](fellows/) | Fellows | 3 |

## Beat sheets are the source of truth

The primary beat sheet records narration, timing, persona, brand, scene routing, playlist metadata, and often the intended publication surface. A folder can contain alternate beat sheets for voices, aspect ratios, brands, or cuts; those remain siblings and must not overwrite the canonical source.

Collection READMEs distinguish these states:

- **master present** — a non-slate MP4 matching the project slug exists locally
- **review cut present** — a slate/review MP4 exists
- **audio present** — per-beat audio exists but no assembled cut was found
- **beat sheet authored** — planning data exists without local rendered output

These are filesystem observations, not approval or publication claims.

## Humanitarians AI voice and presenter

The current HAI production default is **Kore**, using the Kokoro voice **`af_kore`**. Persona and audience copy should describe Kore as **“in for Humanitarians AI,”** and public channel references should use **`@HumanitariansAI`**. Historical directory identifiers such as `claude-liam-*` remain unchanged so existing paths, manifests, and links continue to resolve.

Fellows are an explicit exception to the default voice policy: each fellow
chooses one Kokoro voice, documents it, and keeps it across their report
series. The choice must be approved before the first audio generation; later
changes require an explicit documented re-voice decision.

Absent a stated preference, use a female Kokoro voice (`af_*`) for a
female-coded fellow name and a male Kokoro voice (`am_*`) for a male-coded
name. Treat this only as a default suggestion; the fellow's explicit choice
always wins.

## Typical project contents

A project may contain:

- `beat_sheet.json` and alternate voice, brand, format, or cut variants
- `FACTCHECK.md`, `PEDAGOGY.md`, `PROMPTS.md`, `SHOTLIST.md`, and `SOURCES.md`
- Manim, Remotion, Python, JavaScript, or other rendering sources
- clip manifests, timings, captions, and concatenation instructions
- images, diagrams, SVGs, fonts, and other reconstructable assets
- `_qc/REPORT.md`, QC frames, contact sheets, and layout audits
- build prompts, status notes, citations, receipts, and YouTube metadata

Some folders are complete builds; others are source packages, alternates, or retained quality-control snapshots.

## Publishing contract

Publishing is an external state change. Before uploading:

1. Resolve the exact upload master and reject slate/review cuts unless explicitly authorized.
2. Validate the beat sheet, description, title, channel, privacy, and playlist.
3. Run a dry-run against the channel upload ledger.
4. Upload in small batches and verify each returned video ID.
5. Record the ID and playlist result before starting the next batch.

OAuth credentials and upload ledgers are channel-specific, gitignored assets. Never commit them. A local master does not by itself grant permission to publish; the explicit user request and publisher gates do.

## Finding projects

Run from this repository root:

```bash
# Show all collections
find . -mindepth 1 -maxdepth 1 -type d ! -name .git | sort

# Find projects by folder fragment
find . -mindepth 2 -maxdepth 2 -type d -iname '*profile*'

# Search production text
rg -i 'responsible AI|fellow|quantum'

# List primary beat sheets
find . -mindepth 3 -maxdepth 3 -name beat_sheet.json

# Locate source, fact-check, and QC documents
find . -type f \( -name SOURCES.md -o -name FACTCHECK.md -o -name REPORT.md \)
```

## Adding or moving a project

1. Route subject material to `claude-for-<topic>/`.
2. Route Claude-only, Codex-only, and fellow-profile work to their explicit exceptions.
3. Put each project directly under the collection directory.
4. If a project name collides, add concise source context instead of overwriting it.
5. Add or refresh the collection README after substantial batch changes.
6. Keep credentials, tokens, ledgers, and large generated media out of Git.

## Repository and media policy

The Git remote is `nikbearbrown/humanitarians-youtube`. The root `.gitignore` excludes MP3 and MP4 distribution media; timing metadata and reconstructable source assets may remain tracked. This repository is a production archive, not the Humanitarians website deployment.

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Humanitarians YouTube Workshop

This folder organizes **3950 video projects** built around beat sheets. Each project README explains the subject, supplies research and fact-check prompts, and documents the free local rebuild workflow.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured audio becomes the clock, generated visual beats compile immediately, and unavailable media remains as labeled slates until a human fills the pantry. The human conducts, watches, fact-checks, refines, and decides whether anything is published.

This is currently a collection or support folder. Add each new video in its own lowercase kebab-case subfolder with a `beat_sheet.json` and README.

<!-- END BRUTALIST REBUILD GUIDE -->
