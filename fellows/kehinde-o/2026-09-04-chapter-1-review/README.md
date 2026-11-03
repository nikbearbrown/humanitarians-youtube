# Chapter One, Reviewed

**Volunteer:** Kehinde Obidele

A project update on the human fact-check of chapter 1 of the Medhavy cancer
textbook: what the workbook asks a reviewer to do, what the counts were, what
the failures had in common, and what carries into chapter 2.

## Video Files

The 4K rendered videos are on the shared Google Drive under
`Medhavy_Kehinde/Fact Check/Chapter 1/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)** (`Medhavy_Kehinde/Fact Check/Chapter 1/`)

| File | Aspect | Spec |
|---|---|---|
| `chapter1.mp4` | 16:9 | 3840x2160, 30fps, 2m 13s |
| `chapter1-short.mp4` | 9:16 | 2160x3840, 30fps, 2m 13s, native render |

## Chapter 1 by the numbers

136 sentences flagged for human review in the main tab. Every one looked up
against a primary source: PubMed and PMC, the FDA Orange and Purple Books,
NCI SEER, CDC and WHO.

| Outcome | Rows |
|---|---|
| Held up against the source | 105 |
| False, corrected with a source link | 21 |
| Could not be settled either way | 10 |

105 + 21 + 10 = 136.

## What the failures had in common

Two independent things can be wrong with a cited sentence, and they fail
separately: the **citation** (a real identifier with invented authors) and the
**claim** (a real paper that does not say what the sentence says). Numbers drift
and figures age, so a citation that resolves is not a claim that checks out.

## Files in this repo

- `beat_sheet.json` — the script. One beat per moment, everything derives from it.
- `PEDAGOGY.md` — narration gate, must read VERDICT: PASS before audio runs.

Media files are not committed. The rendered videos live on the shared Drive.

## Rebuild

```bash
python3 runtime/scripts/generate_audio_kokoro.py books/hai/youtube/chapter-1-review
./art run    books/hai/youtube/chapter-1-review
python3 runtime/scripts/compile.py books/hai/youtube/chapter-1-review --height 2160 --fps 30
./art shorts books/hai/youtube/chapter-1-review
```
