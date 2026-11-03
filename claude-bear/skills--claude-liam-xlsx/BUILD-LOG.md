# BUILD-LOG — skills--claude-liam-xlsx

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-xlsx/beat_sheet.json` (Teardown
source examining Anthropic's `xlsx` skill, already fully built, 7 filled
beats). Built entirely fresh this invocation — only SUBJECT.json existed
on pickup.

Question, facts, and body argument carried over unchanged: the two-tool
decision (pandas for analysis/bulk ops, openpyxl for formulas/formatting);
the six-step workflow (choose tool, create/load, modify, save, mandatory
scripts/recalc.py if any formula was written, fix and repeat until clean);
recalc.py's mechanics (opens the file in LibreOffice, recalculates every
formula, scans all four Excel error types — #REF!, #DIV/0!, #VALUE!,
#NAME? — returns JSON with per-error cell addresses); the financial-model
color code (blue=hardcoded input, black=formula, green=cross-sheet link,
red=external link, yellow background=assumption) and number-format rules
(years as text, currency format, dash for zero, one-decimal percentages,
parentheses instead of a minus sign for negatives); the formula mandate
(never calculate a value in Python and hardcode it — write the actual
Excel formula); and the row-offset trap (a DataFrame's row N lands at
Excel row N+1; column 64 is BL, not BK). The source's Teardown
"gets-right / bites" verdict beat was split into this reel's WRONG-GUESS
(guess → break) and BOTH-DIRECTIONS beats instead of one lumped verdict,
per Plain register.

B00 replaced the source's `ClaudeComposerAsk` cold open (already REMOTION,
not a puppet ask, so NO-GENAI/NO-PANTRY LAW required no substitution
there) with `BrutalistHesitantWriter`: WRITER LAW correction "number" →
"formula" — the newcomer's wrong guess that a computed total can just be
typed straight into the cell, corrected toward writing the formula
instead, foreshadowing the reel's central formula-mandate insight.

**One real defect found and fixed during this build (TIMING LAW):** the
first B00 draft placed the trigger word ("number") as the second-to-last
word before the question mark — direct frame inspection at t=9.0s/9.5s
(against a first-pass measured duration of 9.62s) showed the writer still
mid-typing "number" in terracotta with the correction never reached; the
beat ended before its own correction landed on screen, reproducing
exactly the pilot failure this law exists to prevent. Root cause: unlike
the `skills--claude-liam-docx` sibling's "install"→"unzip" swap (trigger
word at ~46% through the string, leaving room to resolve the correction
and finish typing), this draft's trigger sat at ~90% through the string
with almost no runway left. Fixed by rewriting the writer text to
front-load the trigger — "Does Claude just type the number in, once a
total's computed?" places "number" at ~50% through the string, matching
the docx sibling's ratio — and re-narrating B00 to match (`build_beat_sheet.py`,
`beat_sheet.json`, `SCRIPT.md`, `QUESTION.md` all updated). Re-rendered
B00 only (audio re-measured 10.15s, still clearing the ≥9s TIMING LAW
floor) and confirmed by direct frame pull: the correction to "formula"
is legible by t≈5.5s and the complete corrected question ("Does Claude
just type the formula in, once a total's computed?") is legible by
t≈9.8s, well inside the 10.15s beat.

Two Remotion render attempts for the corrected B00 failed with a
transient Puppeteer/DOMWorld seek-to-frame error and a Remotion
package-version-mismatch warning (unrelated to any content in this reel —
pre-existing environment state); the third attempt succeeded and
`media/B00.mp4` (10.17s) was verified present and correctly probed before
moving on. The first `compile.py --force` run was killed mid-write by an
enclosing `timeout` wrapper (a shell-side artifact of this build's
process management, not a script defect) and left a truncated 67s file;
re-run without the wrapper, waited out to its own exit, and it completed
cleanly.

No source beat was ai-video-prompt, pantry, or a human-drop slot —
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00.

Source's two `Xlsx*.tsx` components (`XlsxAnatomy`, `XlsxStandards`) plus
the teardown-only `XlsxTell` were not reused: the same hardcoded-palette
seam already logged on the `skills--claude-liam-docx`,
`skills--claude-liam-claude-api`, and `skills--claude-liam-brand-guidelines`
siblings (these components `import { CLAUDE, CLAUDE_FONT } from
'../tokens/claude'` directly, with no ink/accent/bg props, so they render
in the Claude fidelity skin, not the humanitarians palette). Built fresh
instead as 11 GRAPHIC (Manim) chip-row beats (NB01-NB11) by copying the
`claude-liam-docx` sibling's proven generic template
(`scenes.py`/`render_scenes.py`/`build_beat_sheet.py`), carrying xlsx
content in the humanitarians palette (#F3EBDD/#2F2A26/#E4572E) with the
same hyphenated-chip-label convention that sibling discovered (a literal
space in a chip label collapses to near-zero width at this component's
small font sizes; a hyphen has its own advance width and isn't affected).

One concrete ANCHOR added beyond the source's implied example: the ask "a
three-year SaaS revenue model with a growth-rate assumption and a
computed revenue total each year" (lifted from the source's own BHTF
handoff line), planted at NB02, paid off at NB09 with the total shown as
a live formula and the growth rate colored blue as the input. The
BOTH-DIRECTIONS pair (NB10/NB11) draws on the source's row-offset fact,
reframed as the genuine positive/negative-proof pair the law requires:
recalc.py's four-error scan catches known failures before they ship
(NB10), but a formula pointed at the wrong cell by the row-offset-by-one
trap throws no Excel error at all, so passing the scan is not proof the
cells are right (NB11, this video's one inference flag). The source's
separate `data_only=True` re-save trap (destroys all formulas
permanently) did not fit either direction beat without diluting the
pairing and was not forced into a twelfth beat — documented in SCRIPT.md's
beat-count note rather than invented a beat to carry it.

Landing at 15 beats total: B00 + 11 GRAPHIC body beats (NB01-NB11) + BCRY
+ BHTF + BOUT — same shape as the `skills--claude-liam-docx` sibling.

**Fact-currency note:** the source skill file logged in the source sheet's
metadata (`../anthropics/skills/skills/xlsx/SKILL.md`) no longer exists at
that path as of this build — the skills tree has been reorganized since
the source reel's 2026-07-18 build. Per the redo contract, facts are
carried over unchanged from the locked source script rather than
re-verified against a live skill file that could no longer be located.

`generate_audio_kokoro.py` (15 beats, $0.00) clean, first pass (B00
re-generated once after the writer-text fix, second pass 10.15s).
`render_scenes.py` (11 GRAPHIC beats, foreground) clean, first pass.
`remotion_scenes.py` (B00/BCRY/BHTF/BOUT, foreground): first pass clean;
B00 fix required two re-render attempts (transient Puppeteer error, then
a version-mismatch-warning run that still failed) before a third
succeeded.

**Gate T (type_check.py): PASS, 0 FAILs, clean on the first run** — no
false positives this time (contrast with the docx sibling, which needed
one title fix).

Compiled clean on the final `compile.py --force` pass (after one
truncated attempt from an external `timeout` wrapper, re-run to
completion): **15/15 beats real** (no slate), native 4K (3840×2160),
**184.117s** (ffprobe-verified, independent of compile.py's own summary
line), mp4 mtime newer than beat_sheet.json.

**Gates:**
- content-check: PASS (15 beats, no violations)
- frame-check: PASS (3840×2160, 15 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs
- GATE AUDIO: PASS — mean_volume **-23.8 dB** (independently ffmpeg
  volumedetect-verified), max -2.2 to -2.8 dB across compiles
- ffprobe (independent, not compile.py's self-report): video 3840×2160
  h264 @24fps, audio present (aac), duration 184.117s; mp4 mtime newer
  than beat_sheet.json mtime
- Gate V (visual): pulled frames every 8s across the full 184s runtime
  (23 frames) plus targeted crops of B00's typing/correction timeline and
  the final BOUT frame. No blockers: every chip label legible with normal
  word-spacing, safe inset respected, single accent per beat, B00's
  "number"→"formula" correction visible on screen by t≈5.5s and the
  complete final question legible by t≈9.8s, BCRY/BHTF/BOUT show the
  correct carry-out line, paste-ready prompt, @HumanitariansAI handle,
  and title/subline restate.
- B00 TIMING LAW: `actual_duration_s` 10.15s (≥9s requirement met); the
  "number"→"formula" correction lands well within the clip after the fix
  described above.

**Non-blocking warning (compile.py):** motion histogram graphic:11
remotion:4 — graphic at 73%, over the ~40% pantry cap in MOTION.md. This
is structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as
REMOTION against an 11-beat GRAPHIC body — the ratio follows beat count,
not a choice made in this build. Same disposition as every sibling in
HAILOOP-LOG.md. Logged per the honesty rule rather than reworking beat
count to dodge the warning.

Playlist resolution: SUBJECT.json's family (`skills`) has no literal
prefix match in `playlists.json` (no key equals or prefixes "skills"), and
the skill-name fallback (`hai-simple` → "Claude Basics") would misfile
this — the reel's actual subject is an Anthropic Agent Skill's anatomy and
mechanism, a direct content match for the map's `claude-skills`/
`claude-agent-skills`/`claude-plugins` prefixes → **"Extending Claude —
Skills, Plugins & Connectors."** Same override reasoning already
established by the `skills--claude-liam-docx`,
`skills--claude-liam-claude-api`, and `skills--claude-liam-brand-guidelines`
siblings. Metadata file written: `skills--claude-liam-xlsx.md` (channel
@HumanitariansAI). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
