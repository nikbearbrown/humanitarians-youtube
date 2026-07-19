# PROMPTS — folder-structure-auditor

Beat-prefixed prompts for open slots. All slate beats are human-filled after render.

## B04 — manim (rendered automatically by vox_run.sh via B04_DirectoryTree)
No prompt needed — Manim scene is defined in vox_scenes.py.

## B01 — slate visual intent
Directory listing showing: project/ ├─ report_v1.md ├─ report_v2.md ├─ report_final.md └─ report_final_v2.md at same level. Agent cursor (blinking block) hovering over report_final.md. Bottom caption: "structure failure, not agent failure" in CRIMSON.

## B06 — slate visual intent
Two-column before/after table. LEFT "Before": 4 rows — config.py [HIGH], secrets.env [HIGH], temp/ [MED], __pycache__/ [HIGH]. RIGHT "After restructure": config/ [—], .env [—], temp/ [MED], __pycache__/ [HIGH]. Green checkmarks on resolved rows.

## B07 — slate visual intent
Dark INK background. Large text: "Folder structure = agent communication". Two bullet lines: "Human browse: any file will do" / "Agent navigate: canonical = the only file". CRIMSON rule at bottom.

## B08 — slate visual intent
Next steps card: numbered list 1) run auditor on project root 2) prioritize agent-touched folders 3) archive before deleting. Teaser line: "next: session state generator →" in SLATE.
