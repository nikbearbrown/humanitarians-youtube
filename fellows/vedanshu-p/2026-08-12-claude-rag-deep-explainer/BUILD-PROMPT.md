# BUILD-PROMPT — Two Kinds Of Memory.

Paste-ready Claude Code prompt that carries this reel from its current
state (Gate D1 previz, 28/35 filled) to a clean final master. Run from the
`brutalist.art` toolkit root (this reel lives in the book, not the toolkit —
CLAUDE.md rule 4).

```
Reel: C:\Users\vedan\Downloads\ai1-cli-main\youtube\claude-liam-rag-deep-explainer

Current state: audio LOCKED (35 Kokoro mp3s, 6:11). GATE P signed in
PEDAGOGY.md. GATE F closed in FACTCHECK.md (9/9 rows). Gate D1 previz
COMPLETE: claude-liam-rag-deep-explainer-slate.mp4, 28/35 filled, zero
BLOCKER/MAJOR (see _qc/REPORT.md). SHOPPING.md is the human's — 7 Tier-1
VOX slots, all generic/illustrative, no rights escalation needed.

1. Pantry fill: drop the 7 files named in SHOPPING.md into pantry/, exact
   filenames (B02.png, B03.png, B09.png, B19.png, B20.png, B28.png,
   B29.png). Runs R1 (B02->B03), R2 (B19->B20), R3 (B28->B29) each need
   their pair to read as the SAME visual family (paper/light/palette) —
   see each entry's camera + GEN PROMPT.
2. NOTE for whoever runs this next: run.sh does NOT work end-to-end on
   Windows/Git-Bash in this checkout (MSYS path translation breaks its
   inline python3 -c calls — see BUILD-LOG.md for the confirmed repro).
   Render manually instead:
   a. cd <REEL> && manim -qh --fps 24 -r 1920,1080 scenes.py <NewSceneIfAny>
      (only needed if you add new Manim beats; the existing 8 are done)
   b. python runtime/scripts/remotion_scenes.py <REEL> --force
      (only re-renders beats whose media is missing/forced; VOX beats are
      untouched by this step — they're STILL-type, not remotion-pattern)
   c. PYTHONIOENCODING=utf-8 python runtime/scripts/compile.py <REEL> \
      --review --height 1080 --force
      (Windows: PYTHONIOENCODING=utf-8 avoids a cp1252 crash on the
      status-line arrow glyph — see the sibling reels' BUILD-PROMPT.md)
3. Visual QC on the new slate.mp4 (mandatory, never skip): sample frames,
   READ the PNGs, 9-point rubric, update _qc/REPORT.md. Pay special
   attention to the 3 vox runs (R1/R2/R3) for continuity — same visual
   family across each pair.
4. When all 7 pantry slots are filled and QC passes clean:
   PYTHONIOENCODING=utf-8 python runtime/scripts/compile.py <REEL> --height 1080
   (drop --review; this is the clean final master, refuses if slates remain
   — pass --allow-slates only on an explicit human "ship with slates" call,
   logged in BUILD-LOG.md)
5. Never publish. Master stays in this reel folder for human review.
```

## What's already done (as of this build)

- `scenes.py` — 8 Manim scenes, all rendered and QC'd.
- `beat_sheet.json` — 34 beats across 6 acts, GATE P signed PASS, GATE F
  closed, audio locked, 28/35 rendered.
- `PEDAGOGY.md` / `BUILD-LOG.md` / `FACTCHECK.md` / `SOURCES.md` /
  `CHECKS-REPORT.md` / `SHOPPING.md` / `_qc/REPORT.md` — all written.
- Review cut: `claude-liam-rag-deep-explainer-slate.mp4` (371.4s, 6:11,
  28/35 filled — 7 VOX slates by design).

## If re-running after a content edit

- Same personal-author channel as both sibling reels:
  `@VedanshuDaxeshPatel`, Kokoro `am_onyx` ("Onyx"), no IN-FOR-BEAR framing.
- Reused components (`RagExecutiveSummary`, `RagRetrieveGenerate`,
  `RagThreeFixes`, `RagPredictCard`, `RagFitsInPrompt`, `FluencySegmentCard`,
  `DeepQuoteCard`) live in the shared toolkit's `runtime/remotion/src/`
  (`RagIllu.tsx`, `DeepExplainerIllu.tsx`, `FluencyTrap.tsx`) — editing their
  PROPS is safe; editing their motion math affects every reel that reuses
  them (this session's sibling `ai-explainer`/`cli-explainer` builds
  included). If a beat's visual needs genuinely new motion, add a new
  component rather than forking a shared one.
