# BUILD-LOG — skills--claude-liam-web-artifacts-builder

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-web-artifacts-builder/beat_sheet.json` — a
fully-built, Teardown-register skill explainer (7 beats: B00, B01, B02, B05, BVDT,
BHTF, BOUT; `claude-liam` / @NikBearBrown, no SCRIPT.md on the source). Its
`beats[*].narration_text` served as the locked narration per the redo contract. Never
touched the source reel's folder. Only `SUBJECT.json` was present on pickup;
everything else was built fresh this invocation.

**Facts kept unchanged:** the four-step pipeline (init-artifact.sh provisions React 18
+ TypeScript via Vite, Tailwind CSS 3.4.1 with shadcn/ui theming, path aliases, 40+
shadcn/ui components with Radix UI, Parcel for bundling → develop by editing generated
code → bundle-artifact.sh installs Parcel and html-inline, builds, inlines everything
into bundle.html → share bundle.html; testing is step five, explicitly optional,
deferred unless issues arise or the user asks); the anti-slop design mandate's four
named patterns (excessive centered layouts, purple gradients, uniform rounded corners,
Inter font) as a negative-only rule with no positive design system; the bundle's
contents (React/ReactDOM, Tailwind utility classes, shadcn/ui component styles, every
Radix UI primitive, imported deps); the two hard requirements for bundling to succeed
(Node 18+, an index.html in the project root); the routing gap (the skill's
description mentions routing support, but init-artifact.sh does not install
react-router).

**Register: Teardown -> Plain.** The source's B05 (`WebArtifactsTell` — a hardcoded
two-column "WHAT IT GETS RIGHT" / "WHERE IT BITES" judgment card) and BVDT ("Verdict",
`ClaudeVerdictArtifact`) explicitly rank the design's trade-offs. Plain states the
identical mechanics and requirements as fact (this reel's B03: "the architectural
insight is that init-artifact.sh and bundle-artifact.sh solve two separate problems at
once... two things worth knowing before you rely on it...") and lands the source's own
framing — bootstrapping and bundling solved together, one file at the end that is
compiled rather than handwritten — as the carry-out (BCRY) instead of a verdict
artifact or gets-right/bites card.

**B00 WRITER LAW:** the natural newcomer misreading of "Claude builds a shareable
dashboard artifact" is that Claude is still just typing one HTML file by hand, the way
it would for a simple page — exactly the misconception the source's own B00
pre-empted ("It is not for simple single-file HTML"). Typed text: "Ask for a complex
dashboard / with tabs and charts — it just / handwrites one HTML file. / Wait — what's
actually built first?", trigger "handwrites" -> replacement "bundles". B00 audio
measured 10.99s + `lead_silence_s` 0.8 = 11.79s window (TIMING LAW's >=9s floor
cleared with margin), narration 35 words. Verified across frames at t=6.0s and
t=6.8s: at t=6.0s the writer has typed the doomed word in terracotta ("...it just /
handwrites|"); by t=6.8s the correction has resolved ("...it just / bundles|") — well
inside the 11.0s beat, and by t=9.5s the writer has moved on to the fixed closing
line ("Wait|"), confirming the correction settles with wide margin before the beat
ends.

**B05 (`WebArtifactsTell`) + BVDT (`ClaudeVerdictArtifact`) -> B03
(`SkillTeardownMechanism`) + BCRY (`WantQuote`):** the source's two judgment-carrying
beats collapse into one factual mechanism beat (provision-then-bundle framing, the two
hard requirements) and the bare carry-out sentence, matching `simple`'s law that the
verdict-recap position becomes the carry-out line in Plain register. `WebArtifactsTell`
was NOT reused for B03 even though it renders (confirmed via `./art scenes --check`)
because its "gets right"/"bites" columns are hardcoded into the component's pixels —
reusing it would keep a Teardown-judgment visual on screen no matter how the narration
was rewritten, so `SkillTeardownMechanism` (a generic, judgment-free heading+body card
already in the library, confirmed RENDERABLE, reused from the `skill-creator` sibling
build) was used instead. Same beat count (7 -> 7), renumbered sequentially (B00, B01,
B02, B03, BCRY, BHTF, BOUT vs. source's B00, B01, B02, B05, BVDT, BHTF, BOUT).

**B01/B02 reused as-is:** `WebArtifactsAnatomy` and `WebArtifactsDesign` render the
4-step pipeline, tech stack, anti-slop mandate, and bundle anatomy with no baked-in
judgment — pure fact, so they carry over from the source unchanged (props: `sparkLine`
only; content is fixed in the component). Confirmed renderable via `./art scenes
--check` before use (GATE L).

**BHTF:** kept the source's note-taking-app handoff prompt near-verbatim — already a
real, paste-ready Claude prompt a general viewer can run today, and it drills the exact
wrong guess (assuming raw output instead of a bundled artifact) B00 opened with, via
the same four watch-for gates the source specified (init script runs first, shadcn/ui
reused not reinvented, bundle.html shared not index.html, anti-slop patterns avoided).

**Close:** BOUT's `ClaudeTitleOutro` (`@NikBearBrown`) -> `OutroCTA` (Humanitarians AI
skin, `@HumanitariansAI`), per hai-simple's channel-skin law. Voice/persona unchanged —
Liam, Kokoro `am_onyx`, "in for Bear."

**No AI-VIDEO, pantry, or human-drop beats existed in the source** — every source beat
was already a registered Remotion component. No NO-GENAI/NO-PANTRY substitution was
needed beyond B00 (mandatory writer-open swap), B03 (mandatory judgment-card swap), and
BOUT (mandatory HAI-skin swap).

## Build

- GATE T (`type_check.py`): PASS, 7/7 beats, 0 FAILs.
- Audio: `generate_audio_kokoro.py` — 7/7 beats, $0.00, Kokoro `am_onyx`. B00 measured
  10.99s.
- Remotion: `remotion_scenes.py --only <BEAT_ID>` per beat, in the foreground, each run
  to completion before starting the next (per the loop's lesson on render timeouts).
  All 7 beats succeeded on the first attempt.
- Compile: `compile.py` — 7/7 filled, content-check PASS, frame-check PASS
  (3840x2160), lane-check PASS, GATE AUDIO PASS (mean_volume -24.0 dB, max -2.8 dB).
  Output: `skills--claude-liam-web-artifacts-builder.mp4`, 155.0s, 3840x2160 (4K
  master — `compile.py` forces 4K by default).
- Gate V (frame pulls + read): B00 at t=6.0s/6.8s/9.5s confirms the "handwrites" ->
  "bundles" correction lands and settles well inside the beat. Mid-beat pulls at
  t=30s (B01), t=65s (B02), t=90s (B03), t=110s (BCRY), t=130s (BHTF), t=152s (BOUT) —
  all confirmed legible, no text overlap, safe insets clear, humanitarians palette on
  B00/BCRY/BHTF/BOUT (no @NikBearBrown anywhere — BOUT and BHTF both show
  @HumanitariansAI), B01/B02/B03 confirmed judgment-free (facts and two hard
  requirements only, no gets-right/bites framing). No defects found; no re-render
  needed.
- Audio presence: `ffmpeg -af volumedetect` on the compiled master — mean_volume -24.0
  dB, max -2.8 dB, well above the -40 dB floor.
- mtimes: `skills--claude-liam-web-artifacts-builder.mp4` (2026-09-04T17:20) newer
  than `beat_sheet.json` (2026-09-04T17:18, last touched by the compile build stamp)
  — cut is current, not stale.

**Result: review cut PASSES every gate.** `skills--claude-liam-web-artifacts-builder.mp4`
exists, is newer than `beat_sheet.json`, carries audible narration audio, and is a 4K
master (3840x2160) — not a 1080p slate. Playlist: "Extending Claude — Skills, Plugins &
Connectors" — family `skills` has no literal `playlists.json` prefix match; resolved by
direct content match on the reel's actual subject (an Anthropic Agent Skill's pipeline
and stack), matching the override already established by every other
`skills--claude-liam-*` sibling in this batch (`pdf`, `brand-guidelines`,
`canvas-design`, `doc-coauthoring`, `docx`, `internal-comms`, `mcp-builder`, `pptx`,
`frontend-design`, `claude-api`, `skill-creator`, `slack-gif-creator`) per
`HAILOOP-LOG.md`.
