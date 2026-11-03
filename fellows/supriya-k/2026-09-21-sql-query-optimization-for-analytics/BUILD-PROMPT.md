# BUILD-PROMPT — "SQL, Read Fewer Rows."

The single paste-ready Claude Code prompt that takes this scaffold to a finished
master. Run it **from the toolkit root** (`brutalist.art/`) — `remotion_scenes.py`,
`compile.py`, and `generate_audio_kokoro.py` all resolve their project paths
relative to it.

**Do not run this until `PEDAGOGY.md` and `NARRATION-GATE-P.md` both read
`VERDICT: PASS`.** GATE P binds (brutalist `CLAUDE.md` rule 3). It is a quality
gate, not a cost gate — audio here is free.

> **On `--dangerously-skip-permissions`:** the `claude-debunked` exemplar suggests
> it, and its build ran entirely inside the toolkit repo. This reel writes into a
> *different* repo (`humanitarians-youtube`), so the seatbelt argument
> ("git-tracked, regenerable outputs") does not transfer cleanly. Supriya's call —
> the prompt below works either way.

```text
Build the finished master for the ai-explainer reel "SQL, Read Fewer Rows."

REEL = /Users/supriyakushwaha/Documents/humanitarians-youtube/fellows/supriya-k/2026-09-16-sql-query-optimization-for-analytics
Run from: /Users/supriyakushwaha/Documents/ai1-cli/brutalist.art

Ground truth, read all of it before touching anything:
1. $REEL/beat_sheet.json — the master. 10 beats, af_bella, claude-hai.
2. $REEL/PEDAGOGY.md and $REEL/NARRATION-GATE-P.md — the gates. Both must read
   "VERDICT: PASS". If either is unsigned, STOP and say so. Do not sign them yourself.
3. $REEL/FACTCHECK.md — per-claim verdicts. Open item L2 must be resolved first.
4. $REEL/SHOTLIST.md — the work order and the seven named QC watch items (Q1-Q7).
5. $REEL/remotion-src/REGISTER.md — the two reel-local scenes and how to register them.
6. $REEL/demo/RESULTS.md — the executable evidence behind every number on screen.
7. skills/make/ai-explainer/SKILL.md + CLAUDE-BRAND.md + CLAUDE.md — the laws.
8. CLAUDE-CODE-VISUAL-QC-CHECK.md — the 9-point frame rubric for step 5.

GATE CHECK (do this first, and stop if it fails):
- grep "VERDICT: PASS" in PEDAGOGY.md and NARRATION-GATE-P.md. Both, or stop.
- FACTCHECK.md L2 and L5 are CLOSED - nothing to decide, just verify the reel
  matches: B07's narration and artifactLines must name exactly three functions
  (strftime, CAST, UPPER) and must NOT mention date_trunc. If date_trunc appears
  in either, the sheet is stale - stop and tell me.
- NARRATION-GATE-P.md is at rev 2. Confirm the signature block says the signed
  revision is rev 2, not rev 1. A rev-1 signature does not cover B07's edited line.
- Confirm PEDAGOGY.md open item 1 (LOGO LAW) has a decision recorded.

STEP 1 - SYNC AND REGISTER THE TWO REEL-LOCAL SCENES
COPY the scenes into the shared project (do NOT symlink - see below), then make
sure Root.tsx registers them:

    TOOLKIT=/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art
    cp "$REEL"/remotion-src/SqlPlanBeat.tsx    "$TOOLKIT"/runtime/remotion/src/scenes/
    cp "$REEL"/remotion-src/SqlPredictCard.tsx "$TOOLKIT"/runtime/remotion/src/scenes/

Run this cp EVERY build. The reel's remotion-src/ is the source of truth; the
copies in the toolkit are disposable build artifacts. Skipping the cp after
editing a scene renders the OLD scene silently.

WHY NOT A SYMLINK: webpack resolves a symlink to its realpath before resolving
relative imports, so `../tokens/claude` gets looked up next to the REEL folder
and fails with "Module not found". tsc does not do this, so a symlink typechecks
clean and then fails at bundle time. Copies are the correct placement.

Root.tsx already carries both <Composition> blocks (ids SqlPlanBeat and
SqlPredictCard, registered next to ClaudeComposerAsk). If they are missing, the
exact blocks are in $REEL/remotion-src/REGISTER.md.

Then verify:
    cd "$TOOLKIT"/runtime/remotion
    npx tsc --noEmit
    npx remotion compositions src/index.ts | grep -E 'SqlPlanBeat|SqlPredictCard'
Both ids must print. Expect exactly 2 pre-existing tsc errors at Root.tsx
LabelChip/QuoteCard - those are untracked work unrelated to this reel. Any error
naming SqlPlanBeat or SqlPredictCard IS ours: stop and fix it.

IF THE BUNDLE ERROR MENTIONS A PATH THAT NO LONGER EXISTS, it is the webpack
cache, not your code:
    rm -rf "$TOOLKIT"/runtime/remotion/node_modules/.cache/webpack/remotion-production-*
Clear it after any scene file move/rename, or you will chase a phantom.

STEP 2 - REGENERATE THE EVIDENCE (cheap, proves the numbers still hold)
    cd $REEL/demo && python3 build_demo.py && python3 timing.py
build_demo.py is self-asserting: it compares each pair's full result sets and
EXITS NON-ZERO on any non-equivalent rewrite. A zero exit plus the final line
"all pairs verified" is the check. Then confirm against demo/RESULTS.md:
  400,000 rows · 11,369 matching January · 4,459 groups · 2.84% selectivity
  pair 1 wrapped -> "|--SCAN postings" + "USE TEMP B-TREE FOR GROUP BY"
  pair 1 bare    -> "SEARCH postings USING INDEX idx_postings_posted_at"
  pair 2 (CAST on branch_id) and pair 3 (UPPER on account_ref) -> SCAN vs SEARCH
B03's props quote pair 1's two captures VERBATIM. If either capture's text moved,
stop and tell me - do not silently re-sync the props, because the narration
describes that exact text and would need re-gating.
Timings will differ from RESULTS.md by a millisecond or two; that is expected and
is why B06's on-screen notes read "~60 ms" / "~15 ms". Do not chase them.
Do NOT add an index on account_id: it rewrites pair 1's plan to "SCAN postings
USING INDEX idx_postings_account_id", which prints USING INDEX on the scan side
and makes B03 contradict the narration. See demo/RESULTS.md for why.

STEP 3 - AUDIO (the master clock; free, local, Kokoro only)
    python3 runtime/scripts/generate_audio_kokoro.py $REEL
Voice af_bella for every beat. Then ffprobe each mp3/beat-*.mp3 and write the real
duration into each beat's actual_duration_s (currently null). Do not hand-time
anything, and do not touch narration to change a duration.
Then run the advisory pacing check and REPORT it, do not act on it unasked:
    python3 skills/make/duration-planner/scripts/pace_check.py $REEL
Report the measured total runtime as an OUTPUT. If it lands over ~3:00, that is
expected - PEDAGOGY.md "Duration is an OUTPUT" names B04 and B05 as the cut
candidates. Ask me before cutting a beat.

STEP 4 - VISUALS
    python3 runtime/scripts/remotion_scenes.py $REEL
Renders each beat's shot.remotion.pattern to media/<BID>.mp4 at --scale=2 and
freeze-extends to actual_duration_s. Never hand-roll npx remotion render
(CLAUDE.md rule 5). Expect 10 of 10 slots filled and ZERO slates - this reel has
no human-media slots. If a slate appears, a pattern id is wrong; fix the id.
Then assemble:
    python3 runtime/scripts/compile.py $REEL --height 2160
No caption burn-in. metadata.captions is false and MOTION.md's caption policy is
an SRT SIDECAR, not pixels.

STEP 5 - VISUAL QC (this is the step that is actually load-bearing)
VISUAL QC LAW: the ffprobe duration/frame-count check is a FILE check and does
NOT count. Follow CLAUDE-CODE-VISUAL-QC-CHECK.md:
    ffmpeg -i <master.mp4> -vf fps=2 $REEL/_qc/frames/%05d.png
plus a -ss grab at ~15%, 50% and 85% of every beat's span from beat_sheet.json.
Then actually READ the PNGs and audit all 9 rubric points, with specific attention
to the seven pre-identified risks in SHOTLIST.md "QC watch list":
    Q1 B03 plan text clipping  - ClaudeCodeBeat-lineage layout uses
       whiteSpace:'pre' + overflow:hidden, so long lines clip SILENTLY. Read the
       B03 frames FIRST. Fix by re-wrapping props.right.code - never by editing
       the captured plan's content.
    Q2 B06 track-label collision
    Q3 legibility floor (mono at height*0.0205)
    Q4 B01 dot-field density
    Q5 LOGO LAW - the brand bug
    Q6 1280x720 library patterns vs 1920x1080 Claude scenes: softness/letterbox
    Q7 B03 language chip must read "sql", not "python"
Write $REEL/_qc/REPORT.md: every defect with frame, timestamp, beat, rubric #,
and root cause. Rank BLOCKER > MAJOR > MINOR.
Fix root causes in the SCENE SOURCE - for B03/B05 that is
$REEL/remotion-src/*.tsx (ours to change). Do NOT patch a shared library scene to
suit this one reel; if a library scene is genuinely wrong, add it to
TEMPLATE-MISSES.md and raise it with me. Re-render only affected beats, re-sample,
re-audit. Repeat until zero BLOCKER and zero MAJOR.

STEP 6 - CONTACT SHEET AND STOP
Build $REEL/qc-sheet.png (a frame per beat, labelled) so the whole reel is
reviewable at a glance. Then report:
  - measured per-beat and total durations (as an output)
  - slots filled vs slated (expect 10/10 filled)
  - defects found by severity, fixes applied, whether the re-check is clean
  - the final master path
and STOP.

HARD LIMITS:
- NEVER publish. There is no publishing machinery in this toolkit and ./art post
  does not exist. The master stays in the reel folder.
- Do not touch git remotes. Do not push. Commit only if I ask.
- No paid service, no API key, no credential, at any step. If a step appears to
  need one, that is a toolkit bug (CLAUDE.md rule 7) - stop and tell me.
- Build into $REEL, never into the toolkit folder (CLAUDE.md rule 4). The only
  toolkit edits allowed are the two Root.tsx registrations in STEP 1.
- Do not sign a gate file. Do not edit narration without re-opening GATE P.
```

## After the master exists (all separate, human-triggered, none of it automatic)

| Want | Command | Note |
|---|---|---|
| Review cut with burn-in | `./art run <REEL>` | timecode + beat id + slot status |
| Clean master | `./art final <REEL>` | `--height 2160` is the default |
| 9:16 Short | `./art shorts <REEL>` | **`./art vertical` does not exist** — the subcommand is `shorts`. Re-band layouts vertically; never scale the 16:9 down |
| Beat ledger | `./art todo <REEL>` | which beats need filling, and how |
| Dependency check | `./art doctor` | wraps `./setup` |
| Publish | — | **no such command.** `./art --list` has no publish target and `./art post` does not exist |
