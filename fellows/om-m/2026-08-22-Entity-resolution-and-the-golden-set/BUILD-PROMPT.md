# BUILD-PROMPT — entity-resolution-and-the-golden-set

The single paste-ready Claude Code prompt that rebuilds this reel end to end.
Run from the `brutalist.art` toolkit root. Free/local — no API key, no spend.

---

```
Rebuild the reel at
D:/study_other/humanitarians-youtube/fellows/om-mali/2026-08-22-Entity-resolution-and-the-golden-set

Skill: ai-explainer, channel claude-hai. Read skills/make/ai-explainer/SKILL.md in full first.
Use the .venv interpreter and put .venv/Scripts on PATH so run.sh resolves python3 to it.

0. THE DATA IS THE SOURCE OF TRUTH
   figdata_week4.json is queried from the built data at render time in the Mycroft repo. Every
   on-screen number is a prop read from it. Never type a number into a scene or beat sheet.
   The injection asserts, and MUST keep asserting:
       len(universe_rows) == 7      # NOT "top 7 by spelling count"
       sum(names) == 128
       watchlisted_total == 24
   The worklog records the source figure failing exactly this check: it showed xAI and
   Perplexity (watchlisted, unpublished) instead of Cerebras and Figure AI. Keep the assertion.

1. GATE CHECK
   - FACTCHECK.md: 20 rows. Read rows 2, 12 and 16 before anything else — the universe filter,
     the hardest-cases precision LOSS, and the "not LEI-confirmed" correction.
   - PEDAGOGY.md must contain "VERDICT: PASS". If it says PENDING, STOP and tell the human what
     they are being asked to sign. Do not sign it. Do not pass --no-gate for a final.
   - CHECKS-REPORT.md must exist before the first compile.

2. AUDIO — the master clock
   python3 runtime/scripts/generate_audio_kokoro.py <reel>
   Kokoro am_onyx — the fellow's persistent voice across the series. Never change it silently.
   Then write each measured actual_duration_s into shot.remotion.props.durationInSeconds.

3. RENDER
   python3 runtime/scripts/remotion_scenes.py <reel> --only <BID>
   Twelve beats, all Remotion, zero slates. The eight reel-local scenes are in
   runtime/remotion/src/EntityResolutionGoldenSet.tsx (registered in Root.tsx). Never
   hand-roll `npx remotion render`. Render in small foreground batches — a full-reel
   background run gets killed part-way.

4. COMPILE
   ./art run <reel> --height 1080      # review cut + GATE L + GATE V
   ./art final <reel>                  # clean 4K master, only once GATE P reads PASS

5. VISUAL QC — LOOK at frames, never trust the mp4 probe
   Sample each beat at ~55% and ~92%, actually Read the PNGs, audit the 9-point rubric.
   GATE V PASSING IS NOT THE END OF QC. It checks edge bleed, canvas fill and contrast — it
   does NOT check overlap. On this reel it missed B02's total block overprinting the haystack
   line, because both elements were individually inside the safe area. Look for text-on-text.

6. REPORT — never publish. The master stays in the reel folder.

Laws that bind hardest on this reel:
- DOUBLE-CHECK LAW — this episode's whole point is that the author was wrong. Do not soften
  B04 (the matcher LOSES on precision), B06/B07 (an approved label overturned, both scores
  published) or B08 (a limit no threshold fixes). The script's own note forbids claiming a
  precision win; obey it literally.
- REBUILD LAW — pantry/w4-*.png and .svg are REFERENCE ONLY. Never slot them as media.
  Do not put them back in images/ — run.sh writes compile output there.
- ILLUSTRATE LAW — the Claude UI appears at B00, B09, B10, B11 only. Eight body beats, eight
  different visual schemes.
- SHOW-DON'T-TELL — B02's haystack counter, B03's fork, B05's empty dot slot, B06's anchor row
  dropping in at the identical price, and B08's cut-off failing are the reel's five arguments.
  They must MOVE.
```

---

## Series context

Week 1: `../2026-08-08-Verifying-Private-AI-Valuations`. Week 2:
`../2026-08-15-Bulk-ingestion-at-scale`. **There is no week 3 episode.** All three reels share a
channel, a voice, a palette and a spine; their scene files are deliberately independent so any
one can be re-rendered without touching the others.
