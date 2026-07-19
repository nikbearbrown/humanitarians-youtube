# SOURCES — claude-liam-docx

## Primary source

- `anthropics/skills/skills/docx/SKILL.md` — the skill this reel teardowns

## Key facts used

- A `.docx` file is a ZIP archive containing XML files
- docx-js defaults to A4 (not US Letter) — silent failure
- WidthType.PERCENTAGE breaks in Google Docs without warning
- Unicode bullets produce corrupted documents — use LevelFormat.BULLET
- `\n` inside text produces broken XML — use separate Paragraph elements
- Tables need dual widths: `columnWidths` on table AND `width` on each cell, both in DXA
- Edit path: unpack.py → Edit tool str_replace → pack.py
- Tracked changes: replace entire `<w:r>` element, never inject inside a run
- Element order in `<w:pPr>`: pStyle → numPr → spacing → ind → jc → rPr LAST
- Auto-repair handles: durableId overflow, missing xml:space="preserve"
- Auto-repair won't fix: malformed XML, invalid nesting, missing relationships
- LibreOffice needed for .doc → .docx conversion (not available in Claude sessions)
