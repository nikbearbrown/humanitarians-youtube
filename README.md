# Humanitarians YouTube Production Library

This repository contains course, educational, and public-interest YouTube production materials maintained under `books/humanitarians_html/youtube` in the Bear Textbooks workspace. It preserves the files needed to inspect, edit, fact-check, and rebuild videos without storing final MP3 or MP4 renders.

## Organization

Every beat-sheet video project lives exactly two levels below the repository root:

```text
<topic>/<video-project>/
```

For example:

```text
education/example-course-video/
cancer-biology/apoptosis-vs-necrosis/
quantum-mechanics/example-quantum-video/
claude/example-claude-video/
```

There are no `_collected` source trees. A project belongs directly under its best-fit topic, regardless of the book or workspace from which it originated. Names are expanded with source context only when necessary to prevent collisions.

## Topic routing

The primary routing source is [`books/YouTube.json`](../../YouTube.json), which maps source folders to topics and YouTube playlists. Folder matching is case-insensitive. When a source is absent from that file, its topic is inferred conservatively from the source and project names.

Courses and educational video projects belong in this Humanitarians library. Musinique is reserved for independent music and Claude-specific creative work; Medhavy is reserved for its science collections.

The current library contains 3,747 beat-sheet project folders across 21 topics:

| Topic | Projects |
|---|---:|
| Artificial Intelligence | 219 |
| Branding | 34 |
| Business | 1 |
| Cancer | 55 |
| Cancer Biology | 226 |
| Claude | 1,536 |
| Codex | 40 |
| Computer Science | 91 |
| Design | 465 |
| Economics | 41 |
| Education | 81 |
| Finance | 52 |
| General Education | 52 |
| Marketing | 36 |
| Mathematics | 22 |
| Music | 28 |
| Nanomedicine | 119 |
| Physics | 6 |
| Quantum Mechanics | 538 |
| Video Production | 74 |
| Writing | 31 |

These counts describe folders containing beat-sheet files. A topic can also contain course documentation or other supporting material without a beat sheet.

## Root production documents

The repository root also contains batch manifests, build logs, project-idea documents, and production scripts that apply across multiple projects. Read these before rebuilding or reorganizing a batch.

## Typical project contents

A project may contain:

- `beat_sheet.json` and alternate voice, brand, format, or cut variants
- `FACTCHECK.md`, `PEDAGOGY.md`, `PROMPTS.md`, `SHOTLIST.md`, and `SOURCES.md`
- Python or JavaScript scene and rendering code
- clip manifests, timing metadata, and concatenation instructions
- images, diagrams, SVGs, typography, and other assets under `media/`
- QC frames, overview sheets, layout audits, and final reports
- build prompts, status notes, citations, receipts, and publication metadata

Some folders are complete builds; others are source packages, alternates, or retained quality-control snapshots.

## Finding projects

Run these commands from `books/humanitarians_html/youtube`:

```bash
# Show all topic directories
find . -mindepth 1 -maxdepth 1 -type d ! -name .git | sort

# Find projects by folder-name fragment
find . -mindepth 2 -maxdepth 2 -type d -iname '*profile*'

# Search all production text
rg -i 'Aditi Deodhar|Aravind Balaji|responsible AI'

# List primary beat sheets
find . -mindepth 3 -maxdepth 3 -name 'beat_sheet.json'

# Find source and fact-check documents
find . -type f \( -name 'SOURCES.md' -o -name 'FACTCHECK.md' \)

# Locate quality-control artifacts
find . -type f \( -iname '*qc*' -o -iname '*audit*' \)
```

## Adding or moving a project

1. Look up the source folder in `books/YouTube.json`.
2. Convert its topic to lowercase kebab case.
3. Put the complete project at `<topic>/<video-project>/`.
4. If the same project name already exists, add concise source context instead of overwriting it.
5. Do not introduce another source, course, `youtube`, or `_collected` layer.
6. Keep final MP3 and MP4 renders outside this repository.

The reusable organizer is `SCRIPTS/flatten_humanitarians_youtube.py` at the Bear Textbooks repository root.

## Media policy

The root `.gitignore` excludes all `*.mp3` and `*.mp4` files. A directory named `mp3/` may still contain tracked JSON timing metadata. Supporting formats such as PNG, JPEG, SVG, M4A, Markdown, JSON, HTML, and source code may be retained when required to reconstruct or inspect a production.

## Repository scope

This is a production archive for Humanitarians YouTube courses and educational videos. It is not the Humanitarians website, a deployment repository, or storage for finished distribution media.
