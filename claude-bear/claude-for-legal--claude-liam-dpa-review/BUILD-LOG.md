# BUILD-LOG — claude-for-legal--claude-liam-dpa-review

## 2026-08-29 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-dpa-review/beat_sheet.json`
(a Teardown skill-teardown walkthrough of a hypothetical Anthropic
`dpa-review` legal Skill). Built entirely fresh this invocation — only
SUBJECT.json existed on pickup (two prior worker attempts, logged in
`skills/make/hai-simple/loop/.filmloop/filmloop.log`, hit the session
limit before any file existed).

**Content-gap found and resolved (see SCRIPT.md's "Content-gap note" for
full detail):** the source `beat_sheet.json` was NOT a complete locked
script — four of its seven beats (B00, B03, BVDT, BHTF) contain a literal
unresolved `>` character where skill-specific content belongs (e.g. B03:
"Claude's job: >. What it gets right: repeatable results."), and the
sheet's `source_skill` pointer
(`/Users/bear/.../privacy-legal/skills/dpa-review/SKILL.md`) does not
exist on this machine — confirmed by direct `find` across the whole
`books/` tree. The generic skill-anatomy narration (B01/B02: a Skill is a
folder holding one instruction file, read linearly) was real and is
carried over unchanged, matching the redo contract. The genuinely missing
skill-specific fact (B03's "design tell", BHTF's paste-ready scenario) was
authored fresh using well-established GDPR Article 28(3) DPA-review
practice — named sub-processors and end-of-contract deletion/return are
the two clauses most commonly missing from a real vendor DPA, contrasted
with the judgment call (security adequacy) a checklist can't make. This
follows the precedent set by the `claude-for-legal--claude-liam-cease-
desist` sibling (same source batch, same 7-beat shape, built 2026-08-29),
which likewise authored/carried a skill-specific fact for its own design-
tell beat — the difference here is the source supplied no real fact at
all to carry over, only an unfilled placeholder.

**Register/skin changes (per redo contract):** B00 replaced the source's
`ClaudeComposerAsk` puppet-handoff cold open with `BrutalistHesitantWriter`
(WRITER LAW: "approve" → "check clauses" — the newcomer's wrong guess that
Claude exercises approval judgment over the DPA, corrected toward the
actual mechanism: a fixed checklist, followed step by step). Register
re-registered Teardown→Plain: the source's "design tell"/"deliberate
trade-off" framing was re-expressed as a plain mechanism description with
no judgment on whether the checklist's scope was well designed. BVDT's two
verdict facts (reliable execution, checklist-only limit) were merged into
the single BCRY carry-out sentence rather than kept as a separate
bulleted artifact card, per CARRY-OUT LAW. Close re-skinned to
@HumanitariansAI.

**Beat count:** kept the source's 7-beat shape exactly — B00 (hesitant
writer) + NB01/NB02/NB03 (anatomy / pipeline / checklist) + BCRY
(carry-out, folding BVDT) + BHTF (your turn) + BOUT (outro). Full audit in
SCRIPT.md's "Beat-count note" section.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION, with B00 as the puppet
host (REMOTION `ClaudeComposerAsk`, not AI-VIDEO). NO-GENAI/NO-PANTRY LAW
required no substitution beyond B00's mandated cold-open swap.

All 3 GRAPHIC beats (NB01–NB03) built on the shared generic "chip row"
Manim template (`scenes.py`/`render_scenes.py`, one title + up to 5
labeled chips + optional arrows/accent/strike + caption), copied verbatim
(mechanism, colors, GATE T exemption notes) from the `claude-for-legal--
claude-liam-cease-desist` sibling.

Audio generated fresh (`generate_audio_kokoro.py`, all 7 beats, free/
local, `am_onyx`; total narration ≈83s). B00/BCRY/BHTF/BOUT rendered via
`remotion_scenes.py` (foreground); NB01–NB03 rendered via
`render_scenes.py` (foreground, Manim).

## Three defects found and fixed (Gate T + Gate V, before the review cut)

1. **min-size §8.1, NB01 (16px < 20px floor):** the isolated dot of the
   lowercase "i" in "review" (chip label "FOLDER: dpa-review") detached
   from its stem — the same fragment class the `cease-desist` sibling
   documented for other beats, but here the word itself (unlike
   "cease-desist", which has no letter "i") produces the fragment.
   Verified by direct pixel crop via `type_check.py`'s own
   `extract_frame`/`visible_text_mask`/`labeled_blobs`/`text_run_bboxes`
   functions, confirmed a genuine dot-of-"i" isolate, not a broader
   legibility defect. First fix (shortening the label to "dpa-review",
   dropping the "FOLDER:" prefix to move to the larger font bucket) only
   raised it to 19px — still 1px under floor, same root cause persisting
   at a larger scale. Root-caused properly by uppercasing the label to
   "DPA-REVIEW" (removing the lowercase "i" dot entirely, since uppercase
   "I" has no separate glyph component) — re-rendered, re-measured, PASS.
2. **B00 content bug — leftover word after trigger-word replacement.**
   `BrutalistHesitantWriter`'s `triggerWords` prop only matches a single
   word, not a phrase: an initial fix attempt set
   `triggerWords: "approve it"` to close a grammar gap, which silently
   broke the correction mechanism entirely (verified by full frame-by-
   frame pull of the raw B00 clip: the writer typed "does it approve it?"
   and the beat ended with the wrong guess never corrected on screen — a
   WRITER LAW violation that would have shipped invisibly, since the
   earlier `triggerWords: "approve"` version produced the openly wrong
   but easy-to-miss "does it check clauses **it**?" instead). Root-caused
   by editing the base `text` prop to remove the redundant trailing "it"
   ("does it approve?" instead of "does it approve it?") so a single-word
   swap ("approve" → "check clauses") produces grammatically correct text
   in both the pre- and post-correction states. Re-rendered and verified
   by direct frame-by-frame pull: the correction ("approve" → "check
   clauses", terracotta mid-type) now lands cleanly, settled text reads
   "When Claude reviews a vendor's DPA, does it check clauses?" — the
   actual intended question, no leftover word.
3. Both fixes were applied to `build_beat_sheet.py` (source of truth),
   `scenes.py` (NB01's `BEAT_CONTENT`), and directly to `beat_sheet.json`
   (to avoid re-running the full audio/measured-duration pass for a
   props-only change), keeping all three in sync before the final
   recompile — per COMPLETION LAW, no beat_sheet.json edit after this
   point.

`type_check.py` went FAIL (1)→**PASS, 0 FAILs** after the NB01 fix (the
B00 defect was found by direct Gate V frame inspection, not GATE T — GATE
T has no check for "does the correction actually land," only pixel-level
legibility). Compiled:

```
python3 runtime/scripts/compile.py <REEL_DIR> --force
```

Result: `claude-for-legal--claude-liam-dpa-review.mp4`, 7/7 beats filled
real (no slate), 83.25s, 3840×2160 (native 4K — `compile.py`'s 4K LAW).

**Gates:**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see defect #1 above)
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max -3.0 dB
- ffprobe: video 3840×2160 h264, audio present, duration 83.25s; mp4
  mtime (1788060749) newer than beat_sheet.json mtime (1788060594)
- Gate V (visual): full contact sheet pulled at 6s intervals across the
  entire 83s runtime (reviewed twice — before and after the B00 fix),
  plus a dedicated frame-by-frame pull (0.5s steps) of the full B00 clip
  to directly verify the hesitant-writer correction lands on screen (see
  defect #2). No blockers remain: no text overflow, no unsafe inset, no
  overlap, correct @HumanitariansAI handle on BHTF, correct topic/title
  throughout.
- B00 TIMING LAW: `actual_duration_s` 10.4s (≥8s requirement met, and
  ≥9s WRITER LAW window); narration is 34 words (within the 20-35 word
  band); the "approve" → "check clauses" correction lands on screen by
  t≈8.5s, well before the clip ends at 10.4s.

Metadata file written: `claude-for-legal--claude-liam-dpa-review.md`
(channel @HumanitariansAI, **Playlist: Claude Basics**). Per
`playlists.json`, SUBJECT.json's family (`claude-for-legal`) matches no
map prefix; falling through to the `hai-simple` skill-key match (→
"Claude Basics") per the literal instruction, consistent with the same
reasoning already logged on the `claude-for-legal--claude-liam-cease-
desist` and `claude-for-legal--claude-liam-case-brief` siblings (same
family, same fallback, same playlist — no per-family override convention
established for `claude-for-legal` beyond this skill-key default). Direct
code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate. COMPLETION LAW
satisfied: `claude-for-legal--claude-liam-dpa-review.mp4` exists, is newer
than `beat_sheet.json`, carries audible audio (verified by ffprobe +
volumedetect), 7/7 beats real (no slate needed).
