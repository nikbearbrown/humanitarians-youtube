# PEDAGOGY — claude-liam-docx

Skill: `docx` · Modifier: `skill-teardown`

## PREDICT (viewer question before watching)
"Why does Claude need a skill for this — can't it just write Python to generate Word docs?"

## What the viewer will learn
1. .docx is a ZIP of XML — the unpack/edit/repack path requires no library at all
2. docx-js has 5 silent failure modes (A4 default, unicode bullets, WidthType.PERCENTAGE, etc.)
3. For edits: Edit tool + str_replace is the right approach, not Python scripts

## CONFIRM (what the reel reveals)
- Two paths: create (docx-js) vs edit (unpack → XML → repack)
- 5 critical docx-js rules are all fatal: silent wrong output, not errors
- XML edit path: 3 steps in order, use Edit tool (not Python scripts), tracked changes require replacing whole `<w:r>` blocks

## LAWS CHECKED
- ✅ TRIGGER is clear: Word doc / .docx / report / memo / TOC / headings / page numbers
- ✅ SELF-DEMO: B02 and B03 show verbatim rule content from SKILL.md
- ✅ HANDOFF LAW: BHTF narration reads prompt aloud AND explains what to watch for
- ✅ ILLUSTRATE LAW: UI only at B00 and BHTF bookends
- ✅ ASK→RESULT law: B00 shows ask + TRIGGER + result

## VERDICT: PASS
