# BUILD-PROMPT — Three Ways To Be Wrong.

Paste-ready Claude Code prompt that builds this reel from the
already-authored `beat_sheet.json` + `scenes.py`. Run from the
`brutalist.art` toolkit root (this reel lives in the book, not the toolkit —
see CLAUDE.md rule 4).

```
Reel: C:\Users\vedan\Downloads\ai1-cli-main\youtube\2026-08-18-claude-rag-the-problem-deep-explainer

1. Gate check — read PEDAGOGY.md. Confirm VERDICT: PASS. ✅ DONE — signed by
   Vedanshu Daxesh Patel, 2026-08-18.
2. Audio (Kokoro, free, voice already set in beat_sheet.json metadata):
   python runtime/scripts/generate_audio_kokoro.py <REEL>
   ✅ DONE — 32/32 beats, ≈6:02 total.
   (--only <BEAT_ID> to regenerate a single beat after a narration edit —
   never hand-edit actual_duration_s; audio is the master clock.)
3. Align — write the word clock:
   python runtime/scripts/align.py <REEL>
   ✅ DONE — mp3/words.json, 32 aligned, 0 fallback.
4. Gate D2 — SHOPPING.md, written AFTER audio lock. ✅ DONE — 8 entries
   (2 runs + 4 singles), all Tier 1, locked durations from actual_duration_s.
5. Gate D1 previz — Manim rendered for real at 4K, Remotion filled, vox
   beats left as labeled slates. ✅ DONE, but NOT via `run.sh`:
   `run.sh`'s `HAS_MANIM` probe embeds the reel path into an inline
   `python3 -c` script assuming a POSIX path (`/c/Users/...`); under this
   Windows/Git-Bash setup that path isn't openable by native Windows
   Python, so `run.sh` fails immediately. Built with the same underlying
   tools directly instead:
     manim -qk --fps 24 -r 3840,2160 scenes.py <ClassName>   # ×8, then
     cp media/videos/scenes/2160p24/<ClassName>.mp4 manim/<BID>.mp4
     python runtime/scripts/remotion_scenes.py <REEL>
     python runtime/scripts/compile.py <REEL> --review --height 2160
   Result: claude-rag-the-problem-deep-explainer-slate.mp4, 3840×2160,
   362.4s, 24/32 filled. (If `run.sh`'s path bug gets fixed upstream, its
   one-command form is equivalent and preferred going forward.)
6. Visual QC on the previz. ✅ DONE — see `_qc/REPORT.md`. Found and fixed
   two defects at the source: 3 Manim scenes (B08, B19, B22) were stretched
   past 3× ("extreme slow-mo") — fixed by lengthening each scene's native
   `wait()`, re-rendered; B28's edge labels overlapped their lines — fixed
   by widening the label buffer, re-rendered. Recompiled; 0 BLOCKER/MAJOR
   remaining on all 24 rendered beats.
7. Report back to Vedanshu: previz is ready to watch; SHOPPING.md lists the
   8 stills needed (all Tier 1 — AI-generate or stock, no rights concern).
   ✅ DONE (this session).
8. Pantry fill (human step, NOT YET DONE) — stills land in pantry/B02.png,
   pantry/B06.png, pantry/B11.png, pantry/B17.png, pantry/B21.png,
   pantry/B27.png (B03/B07 share B02/B06's plate per their run). Then:
     python runtime/scripts/remotion_scenes.py <REEL>   # re-picks up new pantry stills if wired through intake
     python runtime/scripts/compile.py <REEL> --review --height 2160   # re-check
     python runtime/scripts/compile.py <REEL> --height 2160            # final cut once 0 slates remain
   Then VISUAL QC LAW pass again on the final cut.
9. Never publish. Master stays in this reel folder for human review.
```

## What's already done (as of this build)

- `beat_sheet.json` — authored, GATE P signed PASS, audio generated (Kokoro
  `am_onyx`, 32/32 beats, ≈6:02), word clock aligned.
- `scenes.py` — 8 Manim scenes, rendered at 3840×2160; two defects found by
  visual QC and fixed at the source (extreme slow-mo on 3 scenes, a label/
  line collision on 1) — see `_qc/REPORT.md`.
- Two new Remotion components (`DeepActCard`, `ProblemThreeFailuresTeaser`)
  built in `runtime/remotion/src/DeepProblemIllu.tsx`, registered in
  `Root.tsx`, rendered. Seven other REMOTION beats reuse already-registered
  patterns, also rendered.
- `SOURCES.md` / `FACTCHECK.md` (GATE F closed) / `PEDAGOGY.md` (GATE P
  PASS) / `CHECKS-REPORT.md` / `BUILD-LOG.md` / `SHOPPING.md` (Gate D2,
  written after audio lock) / `_qc/REPORT.md` — all written.
- **Gate D1 previz built:** `claude-rag-the-problem-deep-explainer-slate.mp4`
  — 3840×2160, 362.4s, 24/32 filled, 8 VOX beats as labeled slates. Visual
  QC: 0 BLOCKER / 0 MAJOR remaining.
- **Note on tooling:** built via direct `manim` / `remotion_scenes.py` /
  `compile.py` calls rather than `run.sh`, because `run.sh`'s `HAS_MANIM`
  probe breaks on this Windows/Git-Bash setup (embeds a POSIX-style reel
  path into an inline `python3 -c` string that native Windows Python can't
  open). Same tools, same 4K flag, just called directly — see BUILD-LOG.md.
- GATE P: **PASS** — signed by Vedanshu Daxesh Patel, 2026-08-18.
- **Pantry filled (2026-08-19):** all 8 VOX stills sourced as real, licensed
  stock photos (Pexels/Unsplash — no AI image-gen tool was available; see
  `SHOPPING.md` for full credits/licenses). 6 are strong matches; B06/B07
  (the magician's-hat scene) are an honest best-available PARTIAL match — a
  real top hat, correctly licensed, without the "hands reaching in" action
  originally asked for — taken per explicit instruction rather than left as
  a slate. One fill (B21) was caught as a mismatch on review and swapped.
- **FINAL MASTER BUILT:** `claude-rag-the-problem-deep-explainer.mp4` —
  3840×2160, 362.4s, **32/32 filled, zero slates**. Visual QC: 0 BLOCKER /
  0 MAJOR. Never published — stays in this reel folder per house rule.

## If re-running after a content edit

- Edit `narration_text` → step 2 with `--only <ID>` → step 3 (re-align) →
  step 5 with the changed beat's slot cleared → step 6 again. Never fix
  timing by hand.
- If a Manim scene's mechanic changes, edit `scenes.py`; `run.sh` only
  re-renders scenes whose `manim/<BID>.mp4` isn't already present, so
  delete the stale output first.
- 4K is a hard requirement per the original request — `run.sh` already
  defaults `HEIGHT=2160`; step 5's explicit `--height 2160` and step 6's
  frame checks both confirm it. Don't ship a slate cut as if it were final —
  the master only exists once all 8 pantry stills land and `./art final` is
  run (step 8).
