# BUILD-LOG — skills--claude-liam-frontend-design

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-frontend-design/beat_sheet.json` (a
Teardown skill-teardown walkthrough of the Anthropic `frontend-design`
Claude Skill, already fully built — no SCRIPT.md; source `beats[*]
.narration_text` served as the locked script). Built entirely fresh this
invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: the
`frontend-design` skill runs a two-pass process (design plan, then a
critique gate, then code) before any CSS is written; the plan has four
parts (color as 4-6 named hex values, type per role, layout via ASCII
wireframes, and a signature element); it names and blocks three AI design
defaults (cream+serif+terracotta, near-black+acid-green, broadsheet
hairline); restraint means spending boldness in one place (the Chanel
rule) and writing in active voice with direct error messages; and the
critique gate's real job is checking whether the plan reads as generic —
not judging whether Claude read the subject well. B00 replaced the
source's `ClaudeComposerAsk` typed-ask cold open with
`BrutalistHesitantWriter` (WRITER LAW: "guess" -> "plan" — the newcomer's
wrong guess that Claude will just guess its way to something that looks
good, corrected toward the actual mechanism: a design plan comes first).
Register re-registered Teardown -> Plain: the source's B05 "what it gets
right / where it bites" list (a 5-item strengths inventory + a 5-item gaps
inventory, baked into the source's own `FrontendDesignTell.tsx` component
as literal on-screen column headers "WHAT IT GETS RIGHT" / "WHERE IT
BITES") was compressed to the single most teachable, general-audience fact
(the critique step catches a generic plan, not bad subject judgment) rather
than kept as a full strengths/gaps inventory — the implementation-level
gaps in the source (no aesthetic-risk formula, unconstrained writing
quality, no CSS-specificity checker) were dropped as assuming a technical
audience simple/hai-simple doesn't target, not as a verdict on the skill's
quality. BVDT's verdict facts were merged into the single BCRY carry-out
sentence rather than kept as a separate bulleted artifact card, per
CARRY-OUT LAW. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**NO-GENAI/NO-PANTRY LAW — one real substitution, not just B00.** The
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`FrontendDesignAnatomy` / `FrontendDesignProcess` / `FrontendDesignRestraint`
/ `FrontendDesignTell` / `ClaudeVerdictArtifact`) — no AI-VIDEO, pantry, or
human-drop beat to replace on that count. But reading the source's four
custom `FrontendDesign*.tsx` components directly (not just their beat_sheet
props) surfaced a real blocker beyond B00: all four hardcode the
Claude-fidelity palette (cream/terracotta `CLAUDE` tokens, not
humanitarians), and `FrontendDesignTell` specifically hardcodes the literal
strings "WHAT IT GETS RIGHT" / "WHERE IT BITES" as on-screen column headers
inside the component — only `sparkLine` is prop-exposed, so no amount of
beat-sheet narration editing could remove that Teardown-judgment text from
the rendered frame, and editing a shared library component to fit one redo
is out of scope (it may be a consumer elsewhere — `art scene-index` lists
it under the general scene registry, not this reel alone). Rather than ship
a Plain-register reel with "WHAT IT GETS RIGHT" burned into a frame, NB01-
NB04 were built as four fresh humanitarians-palette Manim GRAPHIC beats
(this reel's own `scenes.py`/`render_scenes.py`), reusing the same
reusable "chip row" pattern already proven on the
`claude-plugins-official--claude-liam-agent-development` sibling, carrying
the same facts without touching the source components.

**Beat count discipline:** source is 8 beats (B00 composer-ask + B01/B02/B03
anatomy/process/restraint + B05 teardown + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 8-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01->NB01,
B02->NB02, B03->NB03 kept as one beat each; B05's gets-right/bites list
compressed into NB04 (the one fact a general viewer needs and can act on);
BVDT folded into BCRY; BHTF kept, with the source's already-generic,
already-runnable prompt (a ceramic-studio landing page, "Use the
frontend-design skill") carried over unchanged; BOUT kept. Full audit in
SCRIPT.md's six-move audit and beat-count note.

Audio generated fresh (`generate_audio_kokoro.py`, all 8 beats, free/local,
`am_onyx`). B00's on-screen text was written short from the start (63
chars, "Ask Claude for / a landing page. / Will it just guess?") at the
already-proven-safe params from the agent-development sibling's fix
(42ms/char, 4% mistakeRate, 2% hesitateWithin, 8% hesitateBetween) — chosen
deliberately to avoid re-discovering that sibling's original
timing-overflow bug rather than hitting it first and fixing after.
`remotion_scenes.py` (B00/BCRY/BHTF/BOUT) and `render_scenes.py`
(NB01-NB04, Manim) both run in the foreground; the two `remotion_scenes.py`
and `compile.py` invocations exceeded the tool's 120s timeout and were
moved to background by the harness automatically — blocked on each via
`TaskOutput` before proceeding, per the COMPLETION LAW's foreground-render
rule.

B00 verified by frame pull: "guess" sits doomed in terracotta at t~2.5s,
the full corrected question "Ask Claude for a landing page. Will it just
plan?" is settled and legible by t~4.0s, and holds for the remaining ~5s of
the 8.97s clip (extended to 9.0s by the compiler's freeze-hold) — comfortably
past the >=8s TIMING LAW floor.

First `type_check.py` pass was **FAIL, 2 defects**, both fixed at the root
(diagnosed by running the checker's own blob-measurement functions against
the exact failing frames, not guessed):

- **min-size §8.1, NB03** — smallest text run 16px < floor 20px. Root
  cause: the chip label "quiet elsewhere" contains an isolated run of
  x-height-only letters ("sew") sandwiched between the ascenders in "l" and
  "h", which forms its own short connected-component blob distinct from
  the full-word run — a real rendering artifact of that specific letter
  sequence, not a font-size problem. Fixed by rewording the chip to "stay
  quiet" (frequent ascenders/descenders, no isolated x-height-only run);
  also shortened the accented chip "one signature" to "signature" (the
  BOLD weight was forcing extra width-based scale-down on the 4-word
  label). Re-rendered NB03 only.
- **min-size §8.1, BOUT** — smallest text run 36px < floor 41px. Root
  cause, confirmed by cropping the exact flagged bbox: the "@" glyph in
  "@HumanitariansAI" renders visibly shorter than the surrounding cap-height
  letters (a normal optical-sizing property of "@" in most typefaces), and
  it happened to sit far enough from the following "H" to form its own
  isolated, passing-width text-run blob at sub-floor height. Fixed by
  dropping "@" from the eyebrow entirely (`"HUMANITARIANS AI"` instead of
  `"@HumanitariansAI"`) rather than resizing anything — the eyebrow's font
  size is a fixed proportion of frame height in `OutroSeries.tsx` with no
  prop to override.

Second pass surfaced a new, unrelated **§8.9 sweep-gate FAIL**: the fix
text `"FRONTEND DESIGN · HUMANITARIANS AI"` tripped the truncation
heuristic's "≤2-char trailing word on a >30-char string" rule (a false
positive — "AI" is a real word, not a mid-truncation artifact, but the
heuristic can't tell the difference). Fixed the content instead of the
validator: reordered to `"HUMANITARIANS AI · FRONTEND DESIGN"`, which ends
in "DESIGN" (6 chars, no dangling-word match) and also removes the "@"
glyph risk. Re-rendered BOUT, recompiled (`--force`).

`type_check.py` went 2 FAILs -> 1 sweep-gate FAIL -> **PASS, 0 FAILs**.
Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `skills--claude-liam-frontend-design.mp4`, 8/8 beats filled real (no
slate), 158.8s, 3840x2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (8 beats, no violations)
- frame-check: PASS (3840x2160, 8 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (2 root-cause fixes + 1 sweep-gate content fix, see above)
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max -2.7 dB
- ffprobe: video 3840x2160 h264 24fps, audio (aac) present, duration
  158.781s; mp4 mtime (1788542187) newer than beat_sheet.json mtime
  (1788542063)
- Gate V (visual): pulled frames across the full runtime (t=0,5,12,20,30,
  40,50,60,70,80,90,100,110,120,130,140,150,156) plus targeted checks —
  B00 (correction lands and holds), NB01-NB04 (chips legible, no overlap,
  safe insets clean, arrows/captions read correctly post-fix), BCRY
  (carry-out sentence + sparkline "Plan, then check the plan." read clean),
  BHTF (correct topic/title/@HumanitariansAI folder label, paste-ready
  prompt legible), BOUT (OutroSeries: correct eyebrow "HUMANITARIANS AI ·
  FRONTEND DESIGN", correct title restate, crimson underline, no
  truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 8.96s narration, extended to 9.0s by
  the compiler (>=8s requirement met with room to spare); correction lands
  on screen by t~4.0s and stays legible for the remainder of the clip.
- WARNING (non-blocking, expected): `compile.py` flags
  `'remotion' carries 4/8 beats (50%) — over the ~40% pantry cap`. This is
  structural to hai-simple's fixed spine (WRITER LAW mandates REMOTION B00;
  the CLOSE mandates REMOTION carry-out + your-turn handoff + outro), not a
  content defect — the same ratio pattern (4/7 = 57%) occurred on the
  `claude-plugins-official--claude-liam-agent-development` sibling and was
  likewise not treated as blocking.

Metadata file written: `skills--claude-liam-frontend-design.md` (channel
@HumanitariansAI, **Playlist: Claude Basics**). Per `playlists.json`,
SUBJECT.json's family (`skills`) does not `str.startswith`-match any map
prefix (all keys — `claude-skills`, `claude-agent-skills`, `claude-plugins`,
etc. — are longer strings than `"skills"`, so `"skills".startswith(key)` is
false for every key), so per the documented fallback the `hai-simple` skill
key itself is checked next and matches its own map entry exactly
(`"hai-simple".startswith("hai-simple")`), resolving to "Claude Basics" —
the same deterministic algorithm applied on the
`claude-plugins-official--claude-liam-agent-development` sibling (there,
family DID match `claude-plugins` directly). Direct code link per DELIVERY
CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.

## 2026-09-04 — Phase 4, DELIVERED

Master was already born native 3840x2160 (compile.py's 4K LAW), so copied
directly to `skills--claude-liam-frontend-design-4k.mp4` rather than
re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/skills--claude-liam-frontend-design/` (4K master +
description) for the Drive sync. Committed to
`claude-bear/skills--claude-liam-frontend-design/` (README.md = description,
beat_sheet.json, SCRIPT.md, SUBJECT.json, CARRY-OUT.md, QUESTION.md,
BUILD-LOG.md — no mp3/mp4) as commit `8b2f51c5`, pushed clean (no rebase
conflicts).

**Status: DELIVERED.**
