# PEDAGOGY — claude-liam-pdf

Skill: `pdf` · Modifier: `skill-teardown`

## PREDICT (viewer question before watching)
"There are so many PDF libraries — how does Claude know which one to use for which job?"

## What the viewer will learn
1. Three Python libraries own distinct domains: pypdf (manipulation), pdfplumber (extraction), reportlab (creation)
2. For scanned PDFs, OCR requires a two-step pipeline: pdf2image + pytesseract
3. ReportLab subscripts/superscripts must use XML markup tags, never Unicode characters

## CONFIRM (what the reel reveals)
- TRIGGER: any .pdf mention, "extract text/tables", "merge/split/rotate", "create PDF", "fill form", "OCR"
- Library routing: pypdf for merge/split/rotate/encrypt, pdfplumber for text+table extraction, reportlab for creation
- CLI tools: pdftotext (layout-preserving), qpdf (merge/split/rotate/decrypt), pdftk
- FORMS.md and REFERENCE.md are separate specialist files — read them for form-filling and advanced use

## LAWS CHECKED
- ✅ TRIGGER is clear: .pdf file / "extract" / "merge" / "create PDF" / "fill form" / "OCR"
- ✅ SELF-DEMO: B02 shows verbatim quick-reference table from SKILL.md (8 tasks → best tool)
- ✅ HANDOFF LAW: BHTF narration reads prompt aloud AND explains what to watch for
- ✅ ILLUSTRATE LAW: UI only at B00 and BHTF bookends
- ✅ ASK→RESULT law: B00 shows ask + TRIGGER + result

## VERDICT: PASS
