# BUILD-LOG — skills--claude-liam-claude-api

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-claude-api/beat_sheet.json` (Teardown
source examining Anthropic's `claude-api` skill, already fully built, 9
filled beats). Built entirely fresh this invocation — only SUBJECT.json
existed on pickup.

Question, facts, and body argument carried over unchanged: the TRIGGER
fires pre-scan (before the target file opens, not a post-request lookup);
the three API surfaces (single call / API+tools / managed agent) with the
four-question decision rule (complexity, value, viability, cost of error —
one no means stay simpler); the API drift example (extended thinking's
`budget_tokens` parameter now rejected outright on current models); the
"exact model ID, never a date suffix" rule; and the source's Teardown
"design tell" (TRIGGER architecture right: drift visible before it bites;
costs: 44 pitfalls require knowing they exist, none enforced at call time)
split into this reel's WRONG-GUESS (guess -> break) and BOTH-DIRECTIONS
beats instead of one lumped verdict beat, per Plain register.

B00 replaced the source's `ClaudeComposerAsk` cold open (not a puppet ask —
already REMOTION, so NO-GENAI/NO-PANTRY LAW required no substitution there)
with `BrutalistHesitantWriter`: WRITER LAW correction "know" -> "check" —
the newcomer's wrong guess that Claude already knows its own API by heart,
corrected toward "it checks first." B00 audio rendered 11.05s, clearing the
>=9s TIMING LAW window on the first pass; correction verified on screen at
t=9.5s ("Doesn't Claude already check its own API?").

Source's five `ClaudeApi*.tsx` components (Anatomy, Surfaces, Drift,
Models, Tell) were NOT reused: direct read of each .tsx file (not just
`./art scenes --check`, which reports RENDERABLE regardless of palette)
confirmed they `import { CLAUDE, CLAUDE_FONT } from '../tokens/claude'`
directly with no ink/accent/bg props, so they render in the Claude fidelity
skin, not the humanitarians palette — the identical seam already logged on
the `skills--claude-liam-brand-guidelines` sibling for its own
`BrandGuidelines*.tsx` set (built the same day) and on multiple
`books--claude-liam-*` / `k12-teacher-skills--*` reels besides. Built fresh
instead as 11 GRAPHIC (Manim) chip-row beats (NB01-NB11) on the shared
generic template (`scenes.py`/`render_scenes.py`/`build_beat_sheet.py`,
copied from the brand-guidelines sibling's proven pattern), carrying the
same facts in the humanitarians palette (#F3EBDD/#2F2A26/#E4572E). One
concrete ANCHOR added beyond the source's implied-but-never-carried-through
example: the ask "add extended thinking to a Python app using the Claude
API" (lifted from the source's own B00 line), planted at NB02, paid off at
NB09 with the stale parameter caught and the exact model ID supplied.
Source B01's eight-SDK-coverage fact folded into NB05's narration rather
than kept as a separate beat. Landing at 15 beats total: B00 + 11 GRAPHIC
body + BCRY + BHTF + BOUT (source's 9 beats grew to 15 to give
WRONG-GUESS/BREAK and BOTH-DIRECTIONS their own dedicated beats and to
carry the anchor plant/payoff — see SCRIPT.md's "Beat-count note").

**Fact-currency note:** the source skill file
(`anthropics/skills/skills/claude-api/SKILL.md`) no longer exists at its
logged path as of this build — the skills tree has been reorganized since
the source reel's 2026-07-18 build. Per the redo contract, facts are
carried over unchanged from the locked source script rather than
re-verified against a live file that could no longer be located. The
source's specific model-ID example (`claude-opus-4-8`) was deliberately
NOT repeated in this redo's narration or on-screen chips — this video is
itself about training priors going stale, and asserting a specific
"current default" model name here would risk demonstrating the exact
failure mode it teaches about. The mechanism (trigger timing, decision
tiers, drift-table habit, "exact ID" rule) is carried over; the specific
model name is generalized to "the exact model ID."

`generate_audio_kokoro.py` (15 beats, $0.00) clean, first pass.
`remotion_scenes.py` (B00/BCRY/BHTF/BOUT, foreground) clean, first pass.
`render_scenes.py` (11 GRAPHIC beats, foreground) clean, first pass.

**Gate V (mandatory frame-by-frame read), two real defects found and
root-caused — not caught by GATE T's first pass:**

1. First compile + Gate V frame pull (every 8s across the full runtime)
   found NB04's "400 ERROR" chip rendering as "400ERROR" — the space
   between the numeral and the word visually collapsed to zero width.
   Investigated further: NB05's "NAMES CLAUDE"/"8 LANGUAGES", NB06's
   "ONE API CALL"/"MANAGED AGENT", and NB07's "COST OF ERROR" showed the
   identical defect at settled (non-transition) frames, confirmed by
   closely-spaced frame pulls within each beat (t+3s/6s/9s) to rule out a
   mid-FadeIn-scale transient. This is a systemic space-glyph-collapse
   defect at this component's small chip font sizes (18-26pt EB Garamond
   in this Manim/font environment) — the same font/weight renders normal
   word-spacing fine in the title (32pt) and caption (30pt) text in the
   same file, which are unaffected. Root-caused and fixed by replacing
   every internal space in a chip label with a hyphen (a printable glyph
   with its own advance width, not subject to whatever collapses the
   space glyph at these sizes) across all 11 GRAPHIC beats' chip labels —
   verified by an isolated A/B re-render of NB04 first ("400-ERROR" reads
   cleanly) before applying the fix reel-wide. `beat_sheet.json`'s chip
   metadata and `build_beat_sheet.py`'s source were updated to match
   (without touching the already-measured `actual_duration_s` values).
2. Re-running GATE T after the fix surfaced one new kerning FAIL on NB10
   ("CAUGHT-PRE-WRITE" chip, 184px measured gap vs a 10px threshold).
   Direct frame crop at t=4s showed the chip row rendering completely
   cleanly — "KNOWN-DRIFT", "CAUGHT-PRE-WRITE", "FIXED-FIRST" all legible,
   no overlap. Root cause: the arrow shaft between chips sits in the same
   y-band as the chip text, which the checker's row-based analysis
   misreads as one oversized inter-glyph gap — the identical false-positive
   class already documented for `BDNB01Scene`/`BDNB03Scene`/`BDNB05Scene`
   in `type_check.py`'s own `KERNING_EXEMPT_PATTERNS` (the `BDNB05Scene`
   entry is literally the brand-guidelines sibling's build from earlier the
   same day). Registered `BDNB10Scene` in that same table with a comment
   recording the direct frame verification — the toolkit's own sanctioned
   exemption mechanism for a confirmed structural non-bug, not a validator
   loosening.

`type_check.py` went 0(initial pass before Gate V's manual frame-by-frame
catch)->1(after the hyphen fix, new false-positive)->0 FAILs across three
GATE T runs — the initial 0-FAIL pass on the pre-fix render is the reason
Gate V's own mandatory frame read (not GATE T's pixel heuristics) is what
actually caught the word-fusion defect, consistent with the
brand-guidelines sibling's documented experience the same day. GATE T:
**PASS** (final). Compiled clean on the final `compile.py --force` pass:
**15/15 beats real** (no slate), native 4K (3840x2160), **162.74s**
(ffprobe-verified, independent of compile.py's own summary line), mp4
mtime newer than beat_sheet.json.

**Gates:**
- content-check: PASS (15 beats, no violations)
- frame-check: PASS (3840x2160, 15 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see the two-defect log above)
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (independently ffmpeg
  volumedetect-verified), max -2.9 dB
- ffprobe (independent, not compile.py's self-report): video 3840x2160
  h264 @24fps, audio present (aac), duration 162.738333s; mp4 mtime newer
  than beat_sheet.json mtime
- Gate V (visual): pulled frames across the full runtime (8s spacing) plus
  targeted crops of every GRAPHIC beat's chip row, both defect sites above
  post-fix, and the full B00/BCRY/BHTF/BOUT close block. No blockers after
  fixes: every chip label legible with normal word-spacing, safe inset
  respected, single accent per beat, B00's "know"->"check" correction
  visible on screen (verified at t=9.5s), BCRY/BHTF/BOUT show the correct
  carry-out line, paste-ready prompt, @HumanitariansAI handle, and
  title/subline restate.
- B00 TIMING LAW: `actual_duration_s` 11.05s (>=9s requirement met); the
  "know"->"check" correction lands on screen well within the clip.

**Non-blocking warning (compile.py):** motion histogram graphic:11
remotion:4 — graphic at 73%, over the ~40% pantry cap in MOTION.md. This is
structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as
REMOTION against an 11-beat GRAPHIC body — the ratio follows beat count,
not a choice made in this build. Same disposition as every sibling in
HAILOOP-LOG.md. Logged per the honesty rule rather than reworking beat
count to dodge the warning.

Playlist resolution: SUBJECT.json's family (`skills`) has no literal prefix
match in `playlists.json` (no key equals or prefixes "skills"), and the
skill-name fallback (`hai-simple` -> "Claude Basics") would misfile this —
the reel's actual subject is an Anthropic Agent Skill's anatomy and
mechanism, a direct content match for the map's `claude-skills`/
`claude-agent-skills` prefixes -> **"Extending Claude — Skills, Plugins &
Connectors."** Same override reasoning already established by the
`books--claude-liam-support` and `skills--claude-liam-brand-guidelines`
siblings. Metadata file written: `skills--claude-liam-claude-api.md`
(channel @HumanitariansAI). Direct code link per DELIVERY CONTRACT format
included.

**Status: review cut DONE.** Passed every Phase-3 gate.
