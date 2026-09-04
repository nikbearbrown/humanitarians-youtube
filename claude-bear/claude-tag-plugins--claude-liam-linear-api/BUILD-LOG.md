# BUILD-LOG — claude-tag-plugins--claude-liam-linear-api

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-tag-plugins/youtube/claude-liam-linear-api/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the `linear-api` Skill, already
fully built — no SCRIPT.md; source `beats[*].narration_text` plus
PEDAGOGY.md served as the locked script). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

Question, facts, and body argument carried over unchanged: Linear's API is
a single GraphQL endpoint (`POST api.linear.app/graphql`, no REST paths);
two ID systems coexist (UUID for every API operation, human-readable
identifier like ENG-123 for reads only — a mutation given an identifier
fails with INVALID_INPUT); the Authorization header carries the key with
no "Bearer" prefix; HTTP 200 does not mean success (GraphQL puts real
errors in the body under `.errors`); workflow patterns — sanity-check with
`viewer`, look up team/state UUIDs before mutating, Markdown for
description/comment bodies, check the mutation's own `success` boolean
too, and connections have no `totalCount` except search endpoints; and the
gap PEDAGOGY.md itself names as the key one — rate limiting returns HTTP
400 with code RATELIMITED, not the standard 429, so a 429-only retry loop
never fires, and the reset time is in epoch milliseconds, not seconds.

B00 replaced the source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "REST" → "GraphQL" — the newcomer's
wrong guess that Linear has REST-style per-object endpoints, corrected
toward the single-GraphQL-endpoint model; this is the source's own
WRONG-GUESS content from B01 — "no slash-issues, slash-projects... if
you're constructing a URL with object names in the path, stop" —
relocated to the cold open, not invented). Register re-registered
Teardown→Plain: the source's B05 "gets it right / where it bites" list
(five things praised: no-REST-paths note, two-ID-system separation,
HTTP-200-on-errors documentation, Markdown bodies, no-Bearer-prefix flag —
versus five gaps: buried 400-not-429 distinction, missing
totalCount-detection guidance, easy-to-miss epoch-ms footnote, opaque
UUID-required failure mode, never-stated three-layer success checklist)
was compressed to the SINGLE fact PEDAGOGY.md itself calls out as the key
gap ("rate limit HTTP 400 vs 429 distinction is easy to miss for
developers coming from REST APIs") rather than kept as a full
strengths/gaps inventory — the other four gaps were dropped as secondary
per the source's own verdict, not as a judgment call invented for this
redo. BVDT's verdict facts were merged into the single BCRY carry-out
sentence (both-directions: a 200 can still mean failure, a 400 can just
mean rate-limited) rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW. BHTF's admin-workspace-specific task ("list issues
assigned to me in the ENG team...") was replaced by a prompt that asks
Claude to produce and explain the query/mutation shape directly, runnable
by any viewer without an existing Linear workspace or API key. Close
re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01,
B02→NB02 kept as one beat each (with the rate-limit reveal moved OUT of
B02's content into NB03, becoming the compressed stand-in for B05); B05's
full gap list compressed into NB03 (one fact); BVDT folded into BCRY; BHTF
kept with a rewritten, universally-runnable prompt; BOUT kept. Full audit
in SCRIPT.md's six-move/one-flag/beat-count-note sections.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`LinearApiAnatomy` / `LinearApiDesign` / `LinearApiTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`, one title + up to 4
labeled chips + optional arrows/accent/strike + caption) copied from the
`claude-tag-plugins--claude-liam-config-guide` sibling.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`). Rendered GRAPHIC beats via `render_scenes.py` and REMOTION
beats via `remotion_scenes.py` (foreground). **Orphaned-process incident
during B00's render** (worth logging in full per the COMPLETION LAW): the
first `remotion_scenes.py` invocation was killed by the tool's own 120s
default foreground timeout while `npx remotion render` + the post-render
`ffmpeg` trim step for B00/BCRY/BHTF/BOUT were still running — but the
underlying subprocess chain kept running detached past that cutoff
(confirmed after the fact: `ps`/`lsof` showed nothing left running once it
actually finished). A second, immediately-following invocation (with an
explicit 600s tool timeout) raced the still-running first one: it saw
`media/B00.mp4` already exist (written mid-render by process 1) and
skipped it entirely — including skipping the post-render trim step, which
only runs on a fresh render — leaving B00 at its raw, untrimmed
`BrutalistHesitantWriter` composition length (**606 frames @ 30fps = 20.24s
fixed, confirmed in Root.tsx — the component's duration is NOT derived
from typing-performance length despite appearances**), 8x longer than the
beat's 12.05s narration. Left uncorrected, `compile.py`'s
longer-than-target branch would have **center-cut** the clip (trimming
~4.1s off both the head and the tail), which had a real chance of cutting
into the correction before it settled. The second invocation's own
concurrent extend step on BHTF also hit a `FileNotFoundError` racing
against process 1's `_ext_BHTF.mp4` tmp file — resolved by confirming (via
`ps`, `lsof`) that no render process was still active, then re-running
`remotion_scenes.py --only B00 --force` alone, which produced a correctly
206.24s→12.1s trimmed clip. Frame-verified directly: "REST" sits doomed in
terracotta at t≈4.0–4.5s, corrected to "GraphQL" by t≈6s, and the full
corrected question — "How do I call the Linear GraphQL API with Claude?"
— holds through the clip's end (t≈10–11.8s), comfortably inside the
12.1s window (TIMING LAW: ≥8s met with margin).

First `type_check.py` pass was **FAIL, 2 defects** (NB02/NB03 min-size
§8.1, 19px < 20px floor), root-caused by iterating through several
hypotheses before the real one: initial guess (BOLD-weight text width
inflation on the accented chip) was a real, separate contributing factor
and was fixed (switched `_chip()`'s accented-text weight from BOLD to
NORMAL — the terracotta underline alone already carries the accent per the
component's own contract), but NB02 kept failing at the *exact same* 19px
reading regardless of chip-label wording changes across four separate
attempts. Root-caused by directly calling `type_check.py`'s own
`check_min_size`/`visible_text_mask`/`text_run_bboxes` functions against
the rendered frame and dumping every detected blob's bbox — not by
guessing from the image — which found the true culprit: a single 19×32px
isolated glyph fragment inside the word "viewer" (a serif anti-aliasing
artifact where the text-run merge algorithm failed to connect one letter
to its neighbors), present in every attempt because "viewer" was never
touched. Fixed at the root: bumped the chip-label font-size tiers
(26/22/18 → 30/26/20 in `scenes.py`'s `_chip()`) so every glyph's absolute
rendered height clears the floor with margin even if a fragment is
mis-merged — verified NB01/NB03 (previously PASSing) still pass with
comfortable margin (40px/38px) after the bump. `beat_sheet.json`'s
`graphic.production_viz` fields for NB02 (title, chips, arrows) were kept
in sync with `scenes.py` before each recompile, per COMPLETION LAW (no
post-compile sheet edits — every fix here was applied and the beat
re-rendered before the next compile attempt).

`type_check.py` went 2→**PASS, 0 FAILs**. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-tag-plugins--claude-liam-linear-api.mp4`, 7/7 beats filled
real (no slate), 148.9s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (compile.py's ffmpeg
  volumedetect), independently re-verified via a second standalone
  `ffmpeg -af volumedetect` pass: mean -23.8 dB, max -2.8 dB
- ffprobe (self-verified, not just trusted from compile.py's log): video
  3840×2160 h264, audio (aac) present, duration 148.9s; mp4 mtime
  (1788217625) newer than beat_sheet.json mtime (1788217297)
- Gate V (visual): pulled frames every 8s across the full runtime (19
  frames) plus targeted B00 correction-timing pulls (t=3, 4.0, 4.5, 5.5,
  6, 10, 11.8s). B00: "REST" doomed in terracotta t≈4.0–4.5s, corrected to
  "GraphQL" by t≈6s, full corrected question settled and held to end.
  NB01 (four chips + accent underline on "no Bearer" + caption legible),
  NB02 (post-fix: three chips all normal-sized and legible, "success"
  accent underline clean, title "VIEWER FIRST, THEN UUID"), NB03 (three
  chips, "HTTP 429" struck in muted grey, "HTTP 400" accented, caption
  legible), BCRY (carry-out sentence and sparkLine footer read clean),
  BHTF (correct topic/title/@HumanitariansAI handle, paste-ready prompt
  text legible), and BOUT (OutroSeries: correct eyebrow "LINEAR API ·
  @HumanitariansAI", correct title restate, crimson underline, no
  truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 12.1s (≥8s requirement met); the
  "REST" → "GraphQL" correction lands on screen by t≈6s, well inside the
  clip, and the final corrected question is still on screen at the clip's
  end.

Metadata file written: `claude-tag-plugins--claude-liam-linear-api.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`claude-tag-plugins`) does NOT
match any map prefix by `str.startswith`, so resolution fell through to
the `hai-simple` skill-key entry, which resolves to "Claude Basics" — same
fallback used on every other `claude-tag-plugins--*` sibling. Direct code
link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-08-31 — Phase 4, DELIVERED

Master was already born native 3840×2160 (compile.py's 4K LAW), so copied
directly to `claude-tag-plugins--claude-liam-linear-api-4k.mp4` rather than
re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/claude-tag-plugins--claude-liam-linear-api/` (4K master +
description) for the Drive sync. Committed to
`claude-bear/claude-tag-plugins--claude-liam-linear-api/` (README.md =
description, beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md,
QUESTION.md, BUILD-LOG.md — no mp3/mp4) as commit `6239062b`, pushed clean
(no rebase conflicts).

**Status: DELIVERED.**
