# BUILD-PROMPT — The Silent Thief (The Uncertain Eye S1E01)

Paste-ready. Run from `~/Desktop/` (the parent of both `brutalist.art/` and
`glaucoma-ai/`).

For the permission posture this pipeline is normally run under, see
`skills/make/ai-explainer/SKILL.md` § "Step 6 — The build prompt". The
justification there applies to this reel: git-tracked, every output regenerable,
no paid API calls.

**Never publish. The job ends at a rendered master in the reel folder.**

---

Build `glaucoma-ai/youtube/hai-uncertain-eye-e01-silent-thief` end to end.

1. **Gate check.** Read `beat_sheet.json`, `CHECKS-REPORT.md`, `SOURCES.md`, and
   `DESIGN-CARDS.md` in the reel folder, plus
   `brutalist.art/skills/make/ai-explainer/SKILL.md` in full. Confirm: 11 beats,
   0 PUNTs, teaching arc intact, and — hard constraint — **no performance figure
   anywhere** (no AUROC, no accuracy, no sensitivity). The season's only
   permitted performance number is ~0.85 AUROC and it does not appear until E03.

2. **Library first.** `./art scenes --check <Name>` for every
   `shot.remotion.pattern` before rendering. All eleven must report RENDERABLE.
   If one does not, run `./art scene-index` — the index goes stale when
   components are added to `Root.tsx` without regenerating it. That exact
   failure hid `HaiGlaucomaStakes` during this build.

3. **Audio (the master clock).**

       cd brutalist.art
       python3 runtime/scripts/generate_audio_kokoro.py \
         ~/Desktop/glaucoma-ai/youtube/hai-uncertain-eye-e01-silent-thief

   Kokoro `am_onyx`, free, local. Measured mp3 durations are ground truth.
   Never re-time by hand — change words, regenerate, recompile.
   Target total 2:00-2:45. This build measured **2:21**.

4. **Sync composition durations to measured audio.** The four reel-local
   components in `runtime/remotion/src/UncertainEyeE01.tsx` are registered in
   `Root.tsx` with `durationInFrames` set from measured mp3 seconds x 30fps.
   `remotion_scenes.py` renders at the registered duration and then freeze-holds
   to the beat length — so if narration is re-recorded, update those four
   numbers or reveals drift off their spoken cues.

5. **Render scenes.**

       python3 runtime/scripts/remotion_scenes.py \
         ~/Desktop/glaucoma-ai/youtube/hai-uncertain-eye-e01-silent-thief \
         --now "<iso8601 timestamp>"

   Foreground, via this script only — never hand-roll `npx remotion render`.

6. **Compile.**

       python3 runtime/scripts/compile.py \
         ~/Desktop/glaucoma-ai/youtube/hai-uncertain-eye-e01-silent-thief

7. **VISUAL QC — mandatory, and the mp4 probe does not count.**
   Sample frames at >=2fps into `_qc/frames/`, plus each beat at ~15/50/85% of
   its span, then **actually Read the PNGs** and audit the 9-point rubric from
   `brutalist.art/CLAUDE-CODE-VISUAL-QC-CHECK.md`: edge bleed, title-safe
   margins, container overflow, collision, offscreen anchors, legibility, brand
   bug placement, aspect, and canvas fill. Beat-specific checks:
   - **B01** media >=8s AND the `looking -> pattern` correction visibly completes
     before the cut (EXECUTIVE-SUMMARY LAW timing clause).
   - **B05** holds the two discs **unlabelled for >=2s** — if that hold got
     compressed, the beat no longer makes its own argument.
   - **B03** lost fibers VANISH; they must not blur. The narration says
     "Not a blur. A subtraction."
   - **B07** carries no numbers on the separation strip.
   Log every defect and fix in `_qc/REPORT.md`. Fix root causes in the scene
   source and re-render until zero BLOCKER and zero MAJOR remain.

8. **Report.** Duration, per-beat status, QC verdict. Do not upload anything.

---

## Render target

Per `RENDER-TARGETS.md`: `--out DIR`, else `$ART_OUT`, else
`brutalist.art/renders/`. Any destination works, including a mounted drive.
What happens to the file afterwards is the human's call.

## Known environment note

The reel lives under `~/Desktop`, which is iCloud-synced. If a render fails on a
missing or evicted file, copy the reel to a local scratch dir, build there, and
copy the master back — do not fight the sync in place.
