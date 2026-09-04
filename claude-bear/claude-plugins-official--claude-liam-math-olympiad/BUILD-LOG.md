# BUILD-LOG — claude-plugins-official--claude-liam-math-olympiad

## 2026-08-31 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-plugins-official/youtube/claude-liam-math-olympiad/beat_sheet.json`
(a Teardown skill-teardown walkthrough of the math-olympiad Claude Code
Skill, already fully built — no SCRIPT.md; source `beats[*].narration_text`
served as the locked script). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup. Followed the `claude-plugins-official--
claude-liam-access` sibling's proven pattern (same source shape: B00
composer-ask + B01/B02 anatomy/design + B05 teardown + BVDT verdict + BHTF
handoff + BOUT outro) beat-for-beat.

Question, facts, and full body argument carried over unchanged: an
interpretation check runs before any solving (most past errors were the
wrong reading, not bad math); eight to twelve solvers work the intended
reading in parallel, each internally iterating solve/self-check/revise up
to five rounds with no calculator or code; before any proof reaches a
verifier, the thinking trace — every false start, every scratch note — is
stripped, leaving only the finished argument; fresh adversarial verifiers
attack that bare proof against a pattern checklist with an asymmetric vote
(four clean checks confirm, two flagged holes refute); and the concrete
reason the trace-stripping matters — a verifier that reads visible
reasoning tends to nod along with it, right or wrong, where a blind
verifier has to find the gap on its own. B00 replaced the source's
`ClaudeComposerAsk` typed-ask cold open with `BrutalistHesitantWriter`
(WRITER LAW: "everything" -> "just the proof" — the newcomer's wrong guess
that showing the checker the full reasoning trail would help it decide,
corrected toward the actual mechanism: the checker only ever sees the
finished proof). Register re-registered Teardown -> Plain: the source's
B05 "gets it right / where it bites" list (dual context isolation, the
grounded 50/63 interpretation-error figure, VERBATIM solver-prompt
fragility, missing cost guidance, missing label-recovery path) was
compressed to the single most teachable, general-audience fact (a visible
reasoning trail biases a verifier toward agreement) rather than kept as a
full strengths/gaps inventory. BVDT's verdict facts (asymmetric vote
numbers, calibrated abstention) were merged into the single BCRY
carry-out sentence rather than kept as a separate bulleted artifact card,
per CARRY-OUT LAW. Close re-skinned to @HumanitariansAI (`OutroSeries`).

**Beat count discipline:** source is 7 beats (B00 composer-ask + B01/B02
anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn +
BOUT outro). This redo kept the same 7-beat shape: B00 carries the
wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01's two
halves (interpretation check + parallel solving; context isolation +
adversarial verify + asymmetric vote) kept as one beat each, NB01 and
NB02, with B02's asymmetric-vote detail folded into NB02 rather than
opening a fourth body beat; B02's remaining "four patterns" content
(label every agent in batch mode, deep mode before abstention, the
presentation pass) and B05's teardown list compressed into NB03; BVDT
folded into BCRY; BHTF kept, with the source's olympiad-specific
instructions replaced by a concrete, paste-ready prompt that needs no
competition-math background so it's actually runnable by any viewer
today; BOUT kept. Full audit in SCRIPT.md's "Beat-count note (redo)"
section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`MathOlympiadAnatomy` / `MathOlympiadDesign` / `MathOlympiadTell` /
`ClaudeVerdictArtifact`), so NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's mandated cold-open swap.

**B00 WRITER LAW defect found and fixed (real bug, not a wording
preference):** `BrutalistHesitantWriter` tokenizes its `text` prop on
whitespace (`text.split(/(\s+)/)`) and matches `triggerWords` against a
single token's core word only (see `buildActs` in
`BrutalistHesitantWriter.tsx`). The first authored version used
`triggerWords: "my reasoning"` (two words) — this can never match a
single token, so the correction silently never fired; the writer just
typed the naive line verbatim with no strike-through and no replacement.
Caught by direct frame pulls of `media/B00.mp4` at t=1.5/2.5/4/8s (no
"about to be deleted" terracotta ever appeared). Fixed by re-authoring the
naive/corrected pair so the swapped word is a single self-contained direct
object: "everything" -> "just the proof" (mirrors the access sibling's
"Discord" -> "the terminal" pattern). Re-verified by frame pulls at
t=1.0/1.8/2.5/3.5/5/7/9s: "everything" renders in terracotta
(about-to-be-deleted) at t≈1.8s, mid-correction by t≈2.5s, settled on "If
I show the checker just the proof, does that work?" by t≈5s and holds
through t≈9s (clip is 9.71s, meeting the >=8s TIMING LAW window).

**Manim chip-label space-collapse defect found and fixed (separate,
non-obvious font-shaping bug):** two chip labels rendered with the
inter-word space collapsed to zero width — "check reading" ->
"checkreading" (NB01) and "nods along" -> "nodsalong" (NB03, bold/accented)
— caught by direct frame pulls, not by `type_check.py` (a pixel-geometry
gate that doesn't parse rendered word content). Isolated the cause with a
throwaway Manim `Text()` test harness (deleted after use, not committed):
the collapse is a font-shaping quirk in this environment's EB Garamond
fallback — NOT consistently tied to bold weight or any single letter pair
("no calculator" and "blind trust" render fine; most other two-word bold
pairs, and even non-bold "check reading"/"check problem", collapse; safe
three-word "X the Y" phrases were consistently fine). Fixed by: (1)
single-word label for the bold/accented NB03 chip ("agrees" — a single
token can't exhibit an internal space bug), and (2) a three-word "X the Y"
label for NB01's first chip ("read the trap", replacing the collapsing
"check reading"/"check problem" candidates) sized to match its neighbors'
font bucket. Documented the finding as a code comment in `scenes.py` next
to `BEAT_CONTENT` so future reels reusing this chip-row template don't
rediscover it blind. Re-verified all three chips render with clean visible
spaces by frame pull before recompiling.

**GATE T flakiness explained (not actually flaky):** an intermediate
`type_check.py` run reported NB01 min-size FAIL at exactly 16px both
before and after a chip-label edit that looked unrelated; traced to font-
bucket mismatch — "read the problem" (16 chars) fell into a smaller
`fs=22` bucket than its neighbors "8-12 solvers"/"no calculator" (`fs=26`,
<=14 chars), forcing extra scale-down below the 20px floor. Not a checker
bug: re-running `type_check.py` 3x unchanged was consistently FAIL, and 3x
after the "read the trap" (13 chars, matching bucket) fix was consistently
PASS. Lesson for this chip-row template: keep same-row chip labels within
one length bucket (<=14 / 15-22 / 23+ chars) to avoid an uneven
scale-down on the longest label.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/local,
`am_onyx`; B00 regenerated once after the trigger-word fix, 9.71s);
B00/BCRY/BHTF/BOUT rendered via `remotion_scenes.py` (first call exceeded
the tool's 120s timeout and was moved to background by the harness
automatically — blocked on it via `TaskOutput` before proceeding, per the
COMPLETION LAW's foreground-render rule; the B00-only re-render after the
trigger-word fix completed within the foreground timeout); NB01-NB03
rendered via `render_scenes.py` (foreground throughout). `type_check.py`
went through the two real defects above, then PASS x3 stable. Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-plugins-official--claude-liam-math-olympiad.mp4`, 7/7
beats filled real (no slate), 108.2s, 3840x2160 (native 4K —
`compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (stable across 3 consecutive re-runs post-fix)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (ffmpeg volumedetect), max -2.9 dB
- ffprobe: video 3840x2160 h264, audio (aac) present, duration 108.18s; mp4
  mtime (1788162158) newer than beat_sheet.json mtime (1788161907)
- Gate V (visual): pulled frames every 6s across the full runtime plus
  targeted checks of B00 (t=1.0/1.8/2.5/3.5/5/7/9s — correction confirmed
  on screen), NB01-NB03 (all three chips legible, evenly sized, clean
  spaces post-fix, one accent moment each), BCRY (carry-out quote reads
  clean), BHTF (correct topic/title/@HumanitariansAI handle, paste-ready
  prompt legible), and BOUT (OutroSeries: correct eyebrow "MATH OLYMPIAD ·
  @HumanitariansAI", correct title restate, crimson underline, no
  truncation). No blockers.
- B00 TIMING LAW: `actual_duration_s` 9.71s (>=8s requirement met); the
  "everything" -> "just the proof" correction lands on screen by t≈5s,
  well inside the clip.

Metadata file written: `claude-plugins-official--claude-liam-math-olympiad.md`
(channel @HumanitariansAI, **Playlist: Extending Claude — Skills, Plugins
& Connectors**). Per `playlists.json`, SUBJECT.json's family
(`claude-plugins-official`) matches the map's `"claude-plugins"` prefix
(a `str.startswith` match), which resolves to "Extending Claude — Skills,
Plugins & Connectors" — same resolution as the `claude-liam-access`
sibling. Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
