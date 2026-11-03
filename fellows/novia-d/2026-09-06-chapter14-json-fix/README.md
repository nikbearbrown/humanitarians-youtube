# One Sentence, Many Sources — Chapter 14 (video 2)

**Fellow:** Novia Dsilva  
**Voice:** Bella (`af_bella`)  
**Greeting:** Hello Novia  
**Channel:** `@Medhavy`  
**Skill:** `ai-explainer`  
**Title:** One Sentence, Many Sources.  
**Clock:** 3:07 (186.9s) · 16:9 and 9:16 (same cut)

This is **video 2** for Chapter 14 (Tumor Microenvironment). It does **not** replace video 1 (`2026-08-25-chapter14-fact-check-generation`). Video 1 was the sentence-by-sentence fact-check. This week is the data-model change after review with the professor.

## Links

- **Video (16:9 + 9:16):** [Google Drive folder](https://drive.google.com/drive/folders/1VKL-SXi5Zetkg1Os_A3Vd0qVJJQpcZ_C?usp=sharing)
- **Methodology report:** [OneDrive](https://1drv.ms/t/c/b194bf3e40fce876/IQDlgwNSfLCQS6huw3mgrwQLAasS39sJQ5Y8qIgUoq4bPGo?e=arpKMk)

## What we did this week

The fact-check itself was already done (138 sentences, 46 flagged, 115 evidence entries, approved sites only). This week we changed **how that evidence is stored**.

1. **The problem.** The original workflow wrote findings into Markdown and Excel. There was no JSON. The workbook was the record: one row per assertion, one **Sites Visited** cell. That worked for a single source.
2. **Why the rows broke.** The standard became multiple independent sources per claim (usually 2–4, sometimes disagreeing). A spreadsheet row holds one value per column, so sources flattened into that one cell — you could not tell which source produced which verdict. This was not one bad row: **4 / 18 / 21 / 3** assertions had 1 / 2 / 3 / 4 sources. **42 of 46** flagged assertions hit the same wall. Markdown looks organized to a person; a program cannot trust it. Hand-retyping into Excel is where the list became a string.
3. **The fix.** JSON holds a nested `evidence[]` list: one assertion, many evidence entries. Sentence and overall verdict stored once; each source keeps its own URL and verdict. **JSON is the record. The Excel workbook is generated from it.** Fix a verdict once, regenerate. Rows are a view, not storage.
4. **Why a list matters.** Overall verdict is a judgment, not a vote. Worked example: assertion 21 (Warburg) — three CONFIRMED sources, overall TRUE. Counter-example: assertion 129 — CONFIRMED + OUTDATED → FLAGGED. A flattened cell would hide that split.

The weekly-update reel walks this as three questions, each answered on the next beat: where do three sources go; why not keep Markdown; what if sources disagree.

Counts on screen come from `SOURCE.md` (the methodology report): 25 TRUE / 9 FALSE / 12 FLAGGED; 24 of 46 need expert review.

## Rebuild

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./art run path/to/2026-09-06-chapter14-json-fix --height 1080
./art shorts path/to/2026-09-06-chapter14-json-fix --handle @Medhavy --no-endcard --drop
```

`scenes.py` is reel-local Manim (`B06_OtherRows`, `B09_OneToMany`, `B12_WarburgThree`). Remotion: ClaudeComposerAsk, ClaudeScienceLayerStack, ClaudeWindow, ClaudeCodeBeat, ClaudeVerdictArtifact, ClaudeTitleOutro. Masters and mp3s stay local; they are gitignored.
