# BUILD-PROMPT — Every Fix Has A Ceiling.

Paste-ready Claude Code prompt that rebuilds this reel end to end from the
already-authored `beat_sheet.json`. Run from the `brutalist.art` toolkit root —
the reel lives in the book, not the toolkit (CLAUDE.md rule 3).

```
Reel: D:\ai1-cli-main\youtube\2026-09-29-claude-summary

0. Windows note — set UTF-8 for EVERY python step below:
   export PYTHONUTF8=1
   And run `./art scene-index` (not build_scene_index.py directly) if you ever
   add a component — the script resolves Root.tsx relative to CWD.

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. If not PASS, stop.
   CHECKS-REPORT.md must show 0 PUNT-flagged before any render (PROOF GATE).

2. NO CODE TO RUN. This reel measures nothing. Every figure in B02-B04 is the
   source reel's own component with that reel's measured data passed verbatim.
   If you change a number here, you have desynchronised it from the video it
   came from — go and read that reel's beat sheet instead.

   Source reels, and the beat each one feeds:
     2026-09-22-claude-cli-rag-pipeline          -> B02 (FaultSignatureTable)
     2026-09-22-claude-rag-prompt-construction   -> B03 (GroundingDrift)
     2026-09-29-claude-cli-rag-reranking         -> B04 (ShortlistReorder)

3. Audio (only if narration changed — it is the master clock):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   Add --only <BEAT_ID> for a single beat. NEVER hand-edit actual_duration_s.

3b. *** RE-SYNC beatSeconds AFTER ANY AUDIO CHANGE ***
   B02, B03, B04 and B05 stage every reveal as a fraction of their measured
   duration. remotion_scenes.py renders at the REGISTERED length (900f/30s)
   then truncates with ffmpeg -t, so keying to durationInFrames loses late
   reveals silently. For each of those four beats, copy actual_duration_s into
   shot.remotion.props.beatSeconds:

     patterns to sync: FaultSignatureTable, GroundingDrift, ShortlistReorder,
                       EvidenceTiers

   Do this while NO render is running — remotion_scenes.py rewrites the sheet on
   completion and will clobber a mid-flight edit. Read it back afterwards.

4. Visuals:
   python runtime/scripts/remotion_scenes.py <REEL>
   --force to re-render after an edit; --only <BEAT_ID> for one.
   *** --only takes ONE id. Passing two is an argparse error — loop instead. ***

   ZERO new components. Every beat reuses something that already exists:
     B00, BHTF  ClaudeComposerAsk
     B01        BrutalistHesitantWriter
     B02        FaultSignatureTable   (from the Ch. 7 reel)
     B03        GroundingDrift        (from the Ch. 8 reel)
     B04        ShortlistReorder      (from the Ch. 9 reel)
     B05        EvidenceTiers         (from the Ch. 8 reel, new content)
     BVDT       ClaudeVerdictArtifact
     BOUT       TitleOutroChannel

   BOUT must stay TitleOutroChannel. Do NOT swap to ClaudeTitleOutro: it is
   locked to claude-liam-* slugs (OUTRO-LOCK.md section Scope), hardcodes
   @NikBearBrown, and renders no subline — silently dropping the signature.

5. Assemble at 4K:
   python runtime/scripts/compile.py <REEL> --height 2160
   Explicit --height 2160 — compile.py's bare default is NOT 4K.

6. Visual QC — MANDATORY. ffprobe is a FILE check, never QC:
   ffmpeg -i <REEL>/claude-rag-every-fix-has-a-ceiling.mp4 -vf fps=2 <REEL>/_qc/frames/%05d.png
   Read the PNGs, audit the 9-point rubric. Watch especially:
     B01 — CHECK THE LAST LINE FINISHED TYPING. See the trap below.
     B02, B04 — verify every cell against the source reel's beat sheet
     B05 — the two evidence bars must read as visibly unequal
   Log defects in _qc/REPORT.md. Fix ROOT CAUSES in scene source, re-render.

7. Confirm resolution:
   ffprobe -v error -select_streams v:0 -show_entries stream=width,height \
     -of csv=p=0 <REEL>/claude-rag-every-fix-has-a-ceiling.mp4   -> 3840,2160

8. Never publish.
```

## The trap this build hit — a third B01 condition the law does not name

EXECUTIVE-SUMMARY LAW says to verify, after rendering, that the beat's media is
at least 8s and that the correction is on screen before the cut. This build
passed both and was still wrong: at 10.7s of an 11.2s beat the third line read
`Each one st|`. The thesis sentence never finished.

`BrutalistHesitantWriter` is a seeded PERFORMANCE — typos, mid-word pauses and
the correction's own 1-1.5s hesitation all consume time, and how much varies by
seed. A text that fits comfortably under one seed can overrun under another.

**So verify three things on any hesitant-writer beat, not two:**

1. media at least 8s,
2. the correction is on screen before the cut,
3. **the final line has finished typing.**

Fix by lengthening the NARRATION (audio is the master clock) rather than editing
a duration, with `charMs` as a secondary lever. Here: 32 words to 42 words
(11.16s to 13.95s) and `charMs` 52 to 46.

Also inherited from the Ch. 8 build: the trigger must be a SINGLE whitespace-
delimited token. `buildActs` matches `triggers.indexOf(core)`, so a phrase never
matches and fails silently, leaving the misconception on screen.

## What's already done (as of this build)

- `beat_sheet.json` — 9 beats, audio generated (Kokoro `am_onyx`, $0.00),
  `beatSeconds` synced.
- `PEDAGOGY.md` (VERDICT: PASS) / `SOURCES.md` / `CHECKS-REPORT.md`
  (9 SHOW / 0 HOLD / 0 PUNT) / `_qc/REPORT.md`.
- Master: 3840x2160, 24fps, 147.76s (2:28), 9.8 MB.

## If re-running after a content edit

- **Do not introduce a new measurement.** A summary that adds fresh numbers is
  not summarising. If a claim needs new evidence, it belongs in a new chapter
  reel, not here.
- **Do not drop B05.** Two of the three source reels ran a declared stand-in at
  the centre of their demo. This beat is the only thing stopping the recap from
  promoting both to facts, and it is the reason this reel is worth making.
- **Do not tidy the Ch. 9 null.** "0 promoted, 0 demoted" is the finding.
- **If a source reel's numbers change, this reel is stale.** The figures are
  copies, not live references — re-read the source beat sheet and update B02-B04.
- **4K is a hard requirement**: step 5 passes `--height 2160`, step 7 confirms.

## Deriving the 9:16 Short

Every component here already registers a `916` twin. The ai-explainer spine has
no revision cycle to drop, so a short is a length decision — drop one act, not
the BLUF or the verdict:

```
python runtime/scripts/shorts.py <REEL> --drop B02 B03 --keep BHTF \
       --handle "@VedanshuDaxeshPatel" \
       --next "Full video: three fixes, three ceilings."
python runtime/scripts/compile.py <REEL>/short --height 3840
```

**Whatever you drop, rewrite BVDT and B05.** BVDT names all three chapters line
by line, and B05's second tier names Ch. 7 and Ch. 9 explicitly — both assert
things a shortened cut may no longer show.

Four Windows notes: pre-copy `mp3/beat-*.mp3` into `short/mp3/` (`shorts.py`
symlinks them, needing privileges Windows withholds — `OSError 1314`);
regenerate the endcard at 2160x3840 with a font from `runtime/fonts/` (its
`find_serif()` probes only macOS/Linux paths and falls back to an ~11px bitmap);
hand-write the rewritten outro narration; and re-check B01's portrait type size,
since `BrutalistHesitantWriter` scales by the WIDTH ratio in portrait.

### As built (the short exists — `short/claude-rag-every-fix-has-a-ceiling-short.mp4`)

2160x3840, 24fps, 124.39s (2:04), 8 beats, `am_onyx`, $0.00. Full record in
`short/_qc/REPORT.md`. Five things a rebuild must repeat:

1. **The parent is already under the cap, so the short needs a real cut.** At
   2:28 against 3:00 the whole reel would fit re-banded — which would be the
   same video in a different aspect, not a derivative. This drops B02 and B03
   and keeps one concrete case (B04).
2. **Rewrite BVDT — the warning above fired exactly as written.** Its first two
   lines asserted Ch. 7's and Ch. 8's findings, both of which this edit cuts.
   The shipped version claims only Ch. 9 (shown) and points at the other two as
   the full video. Six lines to five.
3. **B05 was checked against that same warning and kept unchanged.** Its claim
   is about the three source VIDEOS, which B00's output lines still name — not
   about beats in this cut. Do not drop it: it is the stand-in declaration and
   the reason the summary exists.
4. **B01 needed no font bump, and that was measured not assumed.** Portrait
   usually renders parent-sized hesitant-writer type undersized (Ch. 4 and Ch. 8
   shorts both needed one). Here: 1616px against a 1858px `maxWidth` — 87% fill,
   because this reel's corrected line is 41 chars against Ch. 8's 35. Measure
   before changing it. All three B01 conditions passed, including the final-line
   check this reel's parent added.
5. **Compile clean and portrait-4K:** `compile.py <REEL>/short --height 3840`.
   Not `--review --height 1920` as `shorts.py`'s own "next steps" suggests.
