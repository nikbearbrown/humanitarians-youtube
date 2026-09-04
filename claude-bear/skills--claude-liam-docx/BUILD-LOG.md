# BUILD-LOG — skills--claude-liam-docx

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/skills/youtube/claude-liam-docx/beat_sheet.json` (Teardown
source examining Anthropic's `docx` skill, already fully built, 8 filled
beats). Built entirely fresh this invocation — only SUBJECT.json existed on
pickup.

Question, facts, and body argument carried over unchanged: the two paths
(create with docx-js, edit by unpack/XML-edit/repack); the quick reference
mapping five task types to whichever path fits; the five docx-js rules
(U.S. Letter must be set explicitly — docx-js defaults to A4; no `\n`
line-break characters, use separate Paragraph elements; no unicode bullets,
use LevelFormat.BULLET with a numbering config; tables need dual DXA widths
on the table and every cell; never WidthType.PERCENTAGE, which silently
breaks tables in Google Docs); the three-step edit workflow (unpack.py,
Edit-tool str_replace on the XML — not Python scripts, pack.py repack +
validate); and the XML pitfalls (tracked changes replace the whole `<w:r>`
element, not just its text; `w:pPr` element order is fixed). The source's
Teardown "ZIP insight + gets right/bites" teardown beat was split into this
reel's WRONG-GUESS (guess → break) and BOTH-DIRECTIONS beats instead of one
lumped verdict beat, per Plain register.

B00 replaced the source's `ClaudeComposerAsk` cold open (not a puppet ask —
already REMOTION, so NO-GENAI/NO-PANTRY LAW required no substitution there)
with `BrutalistHesitantWriter`: WRITER LAW correction "install" → "unzip" —
the newcomer's wrong guess that editing a Word file needs installing
something (a library), corrected toward "unzip it instead," which
foreshadows the reel's central ZIP-of-XML insight. B00 audio rendered
9.90s, clearing the ≥9s TIMING LAW window on the first pass; correction
verified on screen at t=4.5s ("to unzip") and the complete final question
legible at t=9s ("Do you need to unzip something to edit a docx?").

Source's four `Docx*.tsx` components (Anatomy, Create, Edit, Tell) were NOT
reused: direct read of each .tsx file (not just `./art scenes --check`,
which reports RENDERABLE regardless of palette) confirmed they `import {
CLAUDE, CLAUDE_FONT } from '../tokens/claude'` directly with no
ink/accent/bg props, so they render in the Claude fidelity skin, not the
humanitarians palette — the identical seam already logged on the
`skills--claude-liam-claude-api` sibling for its own `ClaudeApi*.tsx` set
(built the same day), and on `skills--claude-liam-brand-guidelines` before
that. Built fresh instead as 11 GRAPHIC (Manim) chip-row beats (NB01-NB11)
by copying the `claude-liam-claude-api` sibling's proven generic template
(`scenes.py`/`render_scenes.py`/`build_beat_sheet.py`) and swapping in docx
content, carrying the same facts in the humanitarians palette
(#F3EBDD/#2F2A26/#E4572E). Chip labels used hyphens instead of internal
spaces from the start (e.g. "DXA-NOT-PERCENT"), applying the space-glyph-
collapse fix the claude-api sibling had to discover mid-build — no rework
needed here. One concrete ANCHOR added beyond the source's implied-but-
never-carried-through example: the ask "a one-page memo, U.S. Letter, with
a two-column table and page numbers" (lifted from the source's own BHTF
handoff line), planted at NB02, paid off at NB09 with U.S. Letter set
explicitly and DXA widths applied. Landing at 15 beats total: B00 + 11
GRAPHIC body + BCRY + BHTF + BOUT (source's 8 beats grew to 15 to give
WRONG-GUESS/BREAK and BOTH-DIRECTIONS their own dedicated beats and to
carry the anchor plant/payoff — see SCRIPT.md's "Beat-count note").

**Fact-currency note:** the source skill file logged in the source sheet's
metadata (`../anthropics/skills/skills/docx/SKILL.md`) no longer exists at
that path as of this build — the skills tree has been reorganized since the
source reel's 2026-07-18 build. Per the redo contract, facts are carried
over unchanged from the locked source script rather than re-verified
against a live file that could no longer be located.

`generate_audio_kokoro.py` (15 beats, $0.00) clean, first pass.
`render_scenes.py` (11 GRAPHIC beats, foreground) clean, first pass.
`remotion_scenes.py` (B00/BCRY/BHTF/BOUT, foreground) clean, first pass.

**Gate T (type_check.py), one real defect found and root-caused on the
first run:**

NB03's title "SAME LIBRARY EITHER WAY?" tripped a §8.6b bbox-overlap FAIL —
direct frame inspection confirmed a genuine (not false-positive) glyph
collision: the space between "LIBRARY" and "EITHER" collapsed to near-zero
width at this title's 32pt EB Garamond rendering, the two words' bounding
boxes touching. This is the same space-glyph-collapse class the
`skills--claude-liam-claude-api` sibling hit in its small chip labels
(18-26pt), but reproducing here in a 32pt *title* — a size the sibling's
own build log described as "unaffected." Root cause is evidently
letter-pair-specific (the "Y"-"E" boundary), not purely font-size-driven.
Fixed by inserting a comma: "SAME LIBRARY, EITHER WAY?" — a printable glyph
with its own advance width breaks the collapse, verified by direct
re-render + frame crop showing clean, fully separated word-spacing before
recompiling. `beat_sheet.json`'s NB03 title fields and `build_beat_sheet.py`
/ `scenes.py` sources were updated to match (measured `actual_duration_s`
untouched). Re-ran `type_check.py` after the fix: **GATE T: PASS, 0 FAILs**
on the very next run — no new false positives surfaced (unlike the
claude-api sibling's two-round chase).

Compiled clean on the final `compile.py --force` pass: **15/15 beats real**
(no slate), native 4K (3840×2160), **166.317s** (ffprobe-verified,
independent of compile.py's own summary line), mp4 mtime newer than
beat_sheet.json.

**Gates:**
- content-check: PASS (15 beats, no violations)
- frame-check: PASS (3840×2160, 15 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS, 0 FAILs (see the NB03 fix above)
- GATE AUDIO: PASS — mean_volume **-23.9 dB** (independently ffmpeg
  volumedetect-verified), max -2.9 dB
- ffprobe (independent, not compile.py's self-report): video 3840×2160
  h264 @24fps, audio present (aac), duration 166.317s; mp4 mtime newer than
  beat_sheet.json mtime
- Gate V (visual): pulled frames every 8s across the full 166s runtime (21
  frames) plus targeted crops of B00's mid/late correction and the fixed
  NB03 title. No blockers: every chip label legible with normal
  word-spacing, safe inset respected, single accent per beat, B00's
  "install"→"unzip" correction visible on screen by t=4.5s and the complete
  final question legible at t=9s, BCRY/BHTF/BOUT show the correct
  carry-out line, paste-ready prompt, @HumanitariansAI handle, and
  title/subline restate.
- B00 TIMING LAW: `actual_duration_s` 9.90s (≥9s requirement met, just
  clearing it); the "install"→"unzip" correction lands on screen well
  within the clip.

**Non-blocking warning (compile.py):** motion histogram graphic:11
remotion:4 — graphic at 73%, over the ~40% pantry cap in MOTION.md. This is
structural: hai-simple's mandated shape fixes B00/BCRY/BHTF/BOUT as
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
established by the `skills--claude-liam-claude-api`,
`books--claude-liam-support`, and `skills--claude-liam-brand-guidelines`
siblings. Metadata file written: `skills--claude-liam-docx.md` (channel
@HumanitariansAI). Direct code link per DELIVERY CONTRACT format included.

**Status: review cut DONE.** Passed every Phase-3 gate.
