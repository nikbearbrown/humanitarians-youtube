# BUILD-LOG — skills--claude-liam-skill-creator

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of `anthropics/skills/youtube/claude-liam-skill-creator/beat_sheet.json`
— a fully-built, Teardown-register skill explainer (7 beats: B00, B01, B02, B05, BVDT,
BHTF, BOUT; `claude-liam` / @NikBearBrown, no SCRIPT.md on the source). Its
`beats[*].narration_text` served as the locked narration per the redo contract. Never
touched the source reel's folder. Only `SUBJECT.json` was present on pickup; everything
else was built fresh this invocation.

**Facts kept unchanged:** the five-stage loop (capture intent → interview/research →
write SKILL.md, description as primary trigger, deliberately pushy since Claude
undertriggers → test and grade via parallel with-skill/baseline runs + eval viewer →
improve and repeat); the eval loop architecture (parallel spawn in the same turn, draft
assertions while running, capture timing immediately since tokens/duration only exist
in the task notification, grade → aggregate → analyst pass → generate the viewer
BEFORE self-evaluation, viewer's two tabs — Outputs qualitative, Benchmark
quantitative); the separate description-optimization phase (20 trigger eval queries,
human review, `run_loop.py`, best description applied); progressive disclosure
(metadata → SKILL.md body → bundled resources); the two environment limits (Claude.ai
has no subagents so runs degrade to serial with no baseline; description optimization
needs the Claude CLI, so Claude Code only); the eval-set-overfit risk if test prompts
aren't representative.

**Register: Teardown -> Plain.** The source's B05 (`SkillCreatorTell` — a hardcoded
two-column "WHAT IT GETS RIGHT" / "WHERE IT BITES" judgment card) and BVDT ("Verdict",
`ClaudeVerdictArtifact`) explicitly rank the design's trade-offs. Plain states the
identical mechanics and limits as fact (this reel's B03: "on Claude dot ai there are no
subagents, so runs happen one at a time... description optimization needs the Claude
command line tool, so it only runs inside Claude Code") and lands the source's own "key
rule" — generate the viewer before evaluating inputs yourself — as the carry-out (BCRY)
instead of a verdict artifact or gets-right/bites card.

**B00 WRITER LAW:** the natural newcomer misreading of "ask Claude to build a skill" is
that one good prompt should do it — exactly the question PEDAGOGY.md's own PREDICT line
named for the source build ("Isn't creating a skill just writing a good prompt? Why
does it need its own workflow?"). Typed text: "Making a skill is / just writing a
prompt. / Wait — how does / the skill creator actually decide?", trigger "prompt" ->
replacement "test loop". B00 audio measured 9.73s + `lead_silence_s` 0.8 = 10.53s
window (TIMING LAW's >=9s floor cleared), narration 34 words. Verified across frames at
t=4s and t=8.5s: at t=4s the writer is still mid-typing the doomed word in terracotta
("just writing a pr|"); by t=8.5s the correction has fully resolved ("just writing a
test loop. / Wait — how does / the skill|") — correction lands with margin inside the
9.7s beat.

**B05 (`SkillCreatorTell`) + BVDT (`ClaudeVerdictArtifact`) -> B03
(`SkillTeardownMechanism`) + BCRY (`WantQuote`):** the source's two judgment-carrying
beats collapse into one factual mechanism beat (empirical-loop framing, progressive
disclosure, the two environment limits) and the bare carry-out sentence, matching
`simple`'s law that the verdict-recap position becomes the carry-out line in Plain
register. `SkillCreatorTell` was NOT reused for B03 even though it renders (confirmed
via `./art scenes --check`) because its "gets right"/"bites" columns are hardcoded into
the component's pixels — reusing it would keep a Teardown-judgment visual on screen no
matter how the narration was rewritten, so `SkillTeardownMechanism` (a generic,
judgment-free heading+body card already in the library, confirmed RENDERABLE) was used
instead. Same beat count (7 -> 7), renumbered sequentially (B00, B01, B02, B03, BCRY,
BHTF, BOUT vs. source's B00, B01, B02, B05, BVDT, BHTF, BOUT).

**B01/B02 reused as-is:** `SkillCreatorAnatomy` and `SkillCreatorEvalLoop` render the
five-stage loop and the eval architecture with no baked-in judgment — pure fact, so
they carry over from the source unchanged (props: `sparkLine` only; content is fixed
in the component). Confirmed renderable via `./art scenes --check` before use (GATE L).

**BHTF:** kept the source's meeting-transcript skill-building prompt near-verbatim —
already a real, paste-ready Claude prompt a general viewer can run today, and it drills
the exact wrong guess (skip the test loop) B00 opened with, via the same four
watch-for gates the source specified.

**Close:** BOUT's `ClaudeTitleOutro` (`@NikBearBrown`) -> `OutroCTA` (Humanitarians AI
skin, `@HumanitariansAI`), per hai-simple's channel-skin law. Voice/persona unchanged —
Liam, Kokoro `am_onyx`, "in for Bear."

**No AI-VIDEO, pantry, or human-drop beats existed in the source** — every source beat
was already a registered Remotion component. No NO-GENAI/NO-PANTRY substitution was
needed beyond B00 (mandatory writer-open swap), B03 (mandatory judgment-card swap), and
BOUT (mandatory HAI-skin swap).

## Build

- GATE T (`type_check.py`): PASS, 7/7 beats, 0 FAILs (no-wordy-card checked on
  card-bearing beats; B03's `body` prop kept to 9 words — under the 12-word budget).
- Audio: `generate_audio_kokoro.py` — 7/7 beats, $0.00, Kokoro `am_onyx`. B00 measured
  9.73s.
- Remotion: `remotion_scenes.py --only <BEAT_ID>` per beat, in the foreground, each run
  to completion before starting the next — a whole-reel single pass and my first
  170s-per-beat attempt both exceeded the render's true wall-clock (bundling +
  1020-frame render at scale=2 takes ~90-100s per beat with normal margin), which
  printed `FAIL: <pattern>` with only a Remotion version-mismatch banner in the
  captured stderr tail (the process was killed by timeout, not a real component
  error). Confirmed by a raw manual `npx remotion render` of the same composition,
  which completed clean in ~100s. Re-ran each beat individually with a 280s timeout;
  all 7 succeeded.
- Compile: `compile.py` — 7/7 filled, GATE AUDIO PASS (mean_volume -24.0 dB, max -2.9
  dB), content-check PASS, frame-check PASS, lane-check PASS. Output:
  `skills--claude-liam-skill-creator.mp4`, 174.5s, 3840x2160 (4K master — `compile.py`
  forces 4K by default).
- Gate V (frame pulls + read): B00 at t=4s/8.5s confirms the correction lands well
  inside the beat. Mid-beat pulls at t=2s (B00), t=30s (B01), t=75s (B02), t=115s
  (B03), t=138s (BCRY), t=155s (BHTF), t=172s (BOUT) — one genuine defect found and
  fixed: BHTF's `topic` prop ("SKILL CREATOR · ANTHROPIC SKILL · YOUR TURN") wrapped to
  two lines and its second line ("TURN") visually touched the "SKILL CREATOR" segment
  heading directly below it. Shortened `topic` to "SKILL CREATOR · YOUR TURN" (fits one
  line), re-rendered BHTF only, recompiled (same GATE AUDIO -24.0 dB, 7/7 fill), and
  re-pulled the frame — confirmed clean separation, no overlap. All other beats
  confirmed legible, non-overlapping type inside safe insets, humanitarians palette
  throughout (no @NikBearBrown anywhere); B03 confirmed judgment-free (heading + short
  body, no gets-right/bites framing); BOUT confirmed HAI skin (@HumanitariansAI,
  no @NikBearBrown).
- Audio presence: `ffmpeg -af volumedetect` on the compiled master — mean_volume -24.0
  dB, max -2.9 dB, well above the -40 dB floor.
- mtimes: `skills--claude-liam-skill-creator.mp4` (2026-09-04T16:20) newer than
  `beat_sheet.json` (2026-09-04T16:18, last touched by the BHTF fix + recompile stamp)
  — cut is current, not stale.

**Result: review cut PASSES every gate.** `skills--claude-liam-skill-creator.mp4`
exists, is newer than `beat_sheet.json`, carries audible narration audio, and is a 4K
master (3840x2160) — not a 1080p slate. Playlist: "Extending Claude — Skills, Plugins &
Connectors" — family `skills` has no literal `playlists.json` prefix match; resolved by
direct content match on the reel's actual subject (an Anthropic Agent Skill's anatomy
and eval architecture), matching the override already established by every other
`skills--claude-liam-*` sibling in this batch (`pdf`, `brand-guidelines`,
`canvas-design`, `doc-coauthoring`, `docx`, `internal-comms`, `mcp-builder`, `pptx`,
`frontend-design`, `claude-api`) per `HAILOOP-LOG.md`.

## Phase 4 — delivery

Master was born natively 3840x2160 via `compile.py`'s 4K LAW, so no separate 4K
re-render was needed — copied directly to `skills--claude-liam-skill-creator-4k.mp4`.
