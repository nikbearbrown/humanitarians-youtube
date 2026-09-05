# BUILD-LOG — behind-the-model--claude-liam-vox-self-check-loop

## 2026-09-05 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/youtube/behind-the-model/claude-liam-vox-self-check-loop/beat_sheet.json`
(a Teardown vox-explainer, already fully built — no SCRIPT.md; source
`beats[*].narration_text` served as the locked script). Built entirely
fresh this invocation — only SUBJECT.json existed on pickup.

Question, facts, and full body argument carried over unchanged: an agent
compiling a competitive analysis from five source reports actually reads
two and drafts the rest from training data, then runs an internal
consistency check that finds "no contradictions" because everything came
from the same mind — self-checking and independent verification are
categorically different because a system reviewing its own output shares
the same context, sources, assumptions, and blind spots as the step that
produced it, so it cannot catch an error the generation step already
baked in; Jae's anchor case (an agent misreads 15% as 50% in a source
table, then "verifies" by comparing to its own recollection of that
table, which also says 50%, so the check passes — Jae opens the actual
PDF and finds 15%); independent verification means comparing to the real
source, not the agent's memory of it; practical takeaway: open at least
two cited sources yourself after any agent task, especially any the agent
skipped. Beat count kept: cold open + 9 content beats + your-turn + outro
(source's B00 cold open + B01-B09 body + YOURTURN + OUTRO = 12; the
source sheet also carried BVDT/BHTF/BOUT "BOOKEND" stub beats with empty
narration_text and `status: SLATE`, never filled by the source's own
build — confirmed dead scaffold, not part of the source's actual 11-beat
built reel, and not carried into this redo).

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's B00 was already REMOTION `ClaudeComposerAsk`, so NO-GENAI/
NO-PANTRY LAW required no substitution beyond the mandatory WRITER LAW
cold-open swap. B00 → `BrutalistHesitantWriter`: naive framing "Claude
re-checked its own answer. So it's [verified]. Right?" → corrected to
"self-checked" (triggerWords/replacementWords), the newcomer's actual
wrong assumption that a model re-checking its own answer amounts to
verification. Register re-registered Teardown→Plain — the source
narration was already close to fact-first/Plain in tone (no explicit
verdict language to strip); this pass tightened wording and word counts
per beat rather than removing judgment that wasn't there. Close re-skinned
to @HumanitariansAI (`OutroSeries` + `OutroCTA`, title restate, "…Liam,
in for Bear.").

**B00 TIMING LAW — one real defect caught and fixed, not a QC-sampling
trap.** First render (narration 9.45s, `BrutalistHesitantWriter` at
default typing-speed props) ran out of its window: verified by a frame
pull at the clip's exact last frame — the writer had only reached "so
it's|" with the caret mid-word; the trigger-word correction ("verified"→
"self-checked") never started. Root cause: default `charMs`/hesitation
rates against the chosen text summed to ≈9.3-9.4s against a 9.45s budget
— effectively zero margin. Fixed by shortening the text (four short lines
instead of one long run-on) and speeding the performance (`charMs` 50→38,
`mistakeRate` 10→4, `hesitateWithin` 3→2, `hesitateBetween` 20→8,
`jitter` 30→20) — re-rendered B00 only. Reverified by frame pull at 4fps:
the correction settles fully by ≈t=7.0s of the 9.4s clip and holds through
the end, well past the ≥8s TIMING LAW floor.

**Channel-skin law, corrected mid-build — a real defect, not a stylistic
choice.** First pass built all 9 body beats (S01-S08, BCRY) by reusing
registered library Remotion components (`FormBCard`, `CwcConceptCard`,
`ClaudeC3TwoColumnState`, `WantQuote`, `StepStream`) — all hardwired to
the CLAUDE brand token set with no palette-override props for base
ink/background colors. Cross-checked against three already-DELIVERED
hai-simple precedents in this same `hai-simple/` directory
(`claude-plugins-official--claude-liam-agent-development` and siblings):
their body-beat Manim scenes are colored `#F3EBDD`/`#2F2A26`/`#E4572E`
(humanitarians cream/ink/crimson), confirming hai-simple's "Channel skin"
row in SKILL.md (`skills/make/hai-simple/SKILL.md`) means the
humanitarians palette applies to the **whole reel**, not just the cold
open and outro — the SKILL.md table's "Channel skin" line is a single
category (palette + outro components together), and the initial reading
that body beats keep the Claude fidelity skin was wrong. Rebuilt all 9
body beats fresh as custom Manim scenes (`scenes.py`/`render_scenes.py`,
following the same per-reel pattern as the precedent reels) in the
humanitarians palette, with TEAL (`#1F4E5F`) reserved for "good/true"
states and CRIMSON (`#E4572E`) for "bad/broken" ones per the palette
table in `skills/make/hai/SKILL.md` (S07's self-check-vs-independent
comparison uses this; S04's shared-flaw comparison uses CRIMSON on both
sides since neither side is a "good" outcome). `BHTF` (Your Turn) kept
`ClaudeComposerAsk` in Claude brand colors deliberately — the HANDOFF LAW
exception ("the composer/Claude UI... appear[s] until the Your Turn
handoff, where simple's HANDOFF LAW applies unchanged"), confirmed by the
same precedent reels. `metadata.palette` corrected from `"claude"` to
`"humanitarians"`, which also cleared two pre-existing SKIN LINT warnings
on B00/outro at compile time (they were a direct symptom of the stale
metadata value, not independent issues).

Audio generated fresh (`generate_audio_kokoro.py`, all 13 beats, free/
local, `am_onyx`; B00 regenerated implicitly unaffected by text-only prop
changes — only the render, not the audio, needed a second pass). Visual
beats: B00/BHTF/BOUT1/BOUT2 via `remotion_scenes.py` (foreground; the
first full-sheet invocation exceeded the tool's 120s timeout and was
moved to background by the harness automatically — blocked on it via
`TaskOutput` before proceeding, per the COMPLETION LAW's foreground-render
rule); S01-S08/BCRY via a fresh per-reel `scenes.py`/`render_scenes.py`
(Manim, foreground, one scene at a time and in batches, per COMPLETION
LAW). First `type_check.py` pass was **FAIL, 2 defects**, both fixed at
the root, not by allowlisting in the shared validator:

- **min-size §8.1, S01** — smallest text run 8px < 20px floor (a
  card_row sub-caption at font_size=20, scaled down for a longer label).
  Fixed by bumping the shared `card_row`/`checklist`/`quote_card` helper
  caption font sizes (20→26, 18→24, 22→28) — cleared S01 immediately.
- **min-size §8.1, BCRY** — smallest text run 8px < 20px floor, persisted
  across three different fixes (font-size bump, splitting the long
  two-sentence quote into independently-scaled lines) before the actual
  cause was isolated by contrast against sibling beat S05 (same
  `quote_card` function, no fail): S05 has no spark-line text; BCRY's
  spark line "Go to the source, not the recall." does, and its comma
  glyph in italic EB Garamond measured under the floor as an isolated
  connected component. Fixed by rephrasing to "Go to the source. Not the
  recall." (no comma) — also removed a decorative curly-quote-mark glyph
  from `quote_card` after confirming it was not the actual root cause
  (ruled out, not left in as unexplained dead code).

`type_check.py` went 2→**PASS, 0 FAILs** — but that PASS was itself
misleading: the checker's `Check summary` table showed `kerning §8.4 | 0 |
0` at that point, meaning **zero beats had reached the kerning tier at
all**, because it only runs once every beat has cleared §8.1 min-size
reel-wide. The next unrelated edit (BHTF's `modelLabel` fix, see below)
triggered a recompile and a re-run of `type_check.py` for verification,
which — with min-size now clear across the board — proceeded into the
kerning tier for the first time and surfaced **4 real, previously-latent
FAILs**: S04, S05, S07, BCRY. Confirmed this was not checker flakiness by
re-running three times unchanged (identical result, identical file MD5)
and by pulling the checker's own exact sample frame (`t=dur*0.5`) for
visual inspection — every frame read as cleanly kerned to the eye, so the
defect was in the checker's row-scanning heuristic, not the typography:
- **S04/S07 (two_column, ~330px gaps):** root-caused by replicating
  `check_kerning_sanity`'s algorithm directly against the frame — it finds
  the single densest ink row in the WHOLE frame and measures gaps within
  that one row only. My side-by-side two-column layout deliberately put
  both halves' state-words at the identical y-coordinate for visual
  symmetry, so the checker's peak-row scan spanned across both columns
  and read "same context" ... "same blind spots" as one badly-kerned
  "word" separated by all the whitespace between the two columns. This is
  a structural blind spot of a row-based scanner against any side-by-side
  design, not a real defect — but per this invocation's instructions to
  fix content, not the validator, `two_column()` was redesigned from
  side-by-side to stacked top/bottom (still the same comparison, same
  divider concept, same content) so the two halves can never share a row.
- **S05/BCRY (quote_card, ~24-26px gaps):** smaller-magnitude, different
  cause — isolated by contrasting against passing sibling beats: these
  two used `slant=ITALIC` (the only italic beats in the reel); EB
  Garamond's italic cuts render thin, cursive-style strokes that
  fragment into many small disconnected ink runs at this render scale,
  which the row-gap scanner misreads as broken kerning. Removed the
  italic slant (now BOLD upright, matching the rest of the reel's type
  treatment) — resolved cleanly.
- **Residual S04/S07 fails after stacking** (12-14px, then 19px min-size
  after a font bump): the stacked layout's non-bold "detail" line
  (font_size 20) hit the same thin-stroke fragmentation class as the
  italic fix above; bumped to font_size 28 with a wider fit-target (11.0
  units) to clear both the kerning gap and the resulting min-size dip in
  one pass.

`type_check.py` re-run 3× consecutively after these fixes: **PASS, 0
FAILs, every time** — the stability check this invocation's earlier
"PASS" was missing.

A stale set of `media/S01.mp4`
… `media/BCRY.mp4` files from the first (wrong-palette) render pass were
found and deleted before the final `type_check.py`/`compile.py` runs —
`type_check.py` was silently re-analyzing those stale Claude-palette
files by the old `media/<id>.mp4` path convention even after
`beat_sheet.json` was repointed at `manim/<id>.mp4`, which is why the
BCRY fail persisted unchanged through two unrelated content edits before
this was caught.

Compiled: `python3 runtime/scripts/compile.py <REEL_DIR>`. Result:
`behind-the-model--claude-liam-vox-self-check-loop.mp4`, 13/13 beats
filled real (no slate), 141.5s, 3840×2160 (native 4K — compile.py's 4K
LAW, Manim source rendered at 1080p24 and upscaled).

**Gates:**
- content-check: PASS (13 beats, no violations)
- frame-check: PASS (3840×2160, 13 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see 2 defects + fixes above)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (ffmpeg volumedetect), max -2.9 dB
- Gate V (visual): pulled frames across the full runtime at 2fps (three
  full passes, one after each recompile) plus a targeted 4fps pull across
  all of B00 (confirming "self-checked" settles and holds well before the
  beat ends). All 13 beats read clean on the final pass: legible type, no
  overlap, correct palette (humanitarians throughout except the
  deliberate BHTF Claude-brand exception, now correctly reading "Opus
  4.8"), correct HAI outro skin (Claude Basics eyebrow, title restate,
  "…Liam, in for Bear.", @HumanitariansAI subscribe CTA). No blockers.
- SKIN LINT: clean (0 warnings) after the `metadata.palette` fix.

Final master (after all fixes): 141.5s, 3840×2160, 13/13 beats real,
GATE AUDIO -23.8 dB / max -2.9 dB, mp4 mtime (11:12:43) newer than
beat_sheet.json mtime (10:45:37).

**One more defect caught by cross-checking sibling BUILD-LOG entries in
`skills/make/hai-simple/loop/HAILOOP-LOG.md`** (not by GATE T or the
frame-pull QC, which don't inspect `ClaudeComposerAsk`'s `modelLabel`
prop): BHTF had no `modelLabel` set, silently defaulting to the
component's demo placeholder "Fable 5" — the same defect logged on at
least three `behind-the-model` sibling reels built earlier the same day.
Fixed (`modelLabel: "Opus 4.8"`), re-rendered BHTF only, recompiled,
re-verified by frame pull ("Opus 4.8" now renders correctly) and GATE
AUDIO (unchanged, -23.8 dB).

Metadata file written:
`behind-the-model--claude-liam-vox-self-check-loop.md` (channel
@HumanitariansAI, **Playlist: Behind the Model** — SUBJECT.json's family
`behind-the-model` is an exact-prefix match in
`skills/make/hai-simple/loop/playlists.json`). Direct code link per
DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
