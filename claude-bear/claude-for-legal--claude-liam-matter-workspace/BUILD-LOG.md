# BUILD-LOG — claude-for-legal--claude-liam-matter-workspace

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-matter-workspace/beat_sheet.json`
— a 7-beat Teardown skill-explainer (`claude-liam` / @NikBearBrown) about the
legal-ops skill `matter-workspace`.

**Source-fidelity note:** the source SKILL.md
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ai-governance-legal/skills/matter-workspace/SKILL.md`)
does not exist on this machine (confirmed via `find` across the whole
`anthropics/claude-for-legal/` tree — only `youtube/claude-liam-matter-workspace/`
exists locally). Unlike the `matter-briefing` sibling redo, this source's
own beat_sheet.json narration does NOT spell out matter-workspace's
per-matter deliverable — B00 only says "The skill is matter-workspace. A
SKILL.md tells Claude exactly how." The one specific, load-bearing fact the
source states in full is its B03 design tell: "The skill never reads
across matters unless Cross-matter context is on in the practice-level
CLAUDE.md." That sentence is the ground truth for every specific claim
this redo makes about isolation. Nothing about matter-workspace's actual
per-matter output is invented — logged in QUESTION.md and SCRIPT.md too.

**Facts kept unchanged (from the source, where present):** a skill is a
folder Claude reads before it acts; the whole routine lives in one file
(SKILL.md); Claude reads the file's Steps section and executes it in
order, linear, no branching unless a step itself branches; the design
tell — matter-workspace never reads across matters unless cross-matter
context is switched on in the practice-level CLAUDE.md.

**New content added to meet hai-simple's spine (not in the source, but not
invented legal-specific fact either):** the source has no explicit
wrong-guess, anchor, or both-directions beat. Added: B01 (stakes — "a
matter-workspace skill" sounds like every matter folds into one shared
pool), B02 (wrong guess broken with a falsifying case — open a brand-new
matter, ask about a different case, nothing is there because it was
walled off), B06 (anchor payoff — restates the isolation design tell
against the named anchor), B07 (both directions — staying inside one
matter proves nothing about whether the cross-matter switch is on; a
missed detail proves nothing about whether isolation is working). B03/B04/
B05 carry the source's anatomy/pipeline/design-tell facts forward, with
B03 serving as the anchor plant (matter-workspace's single SKILL.md).

**Beat-count note:** source is 7 beats (B00, B01 anatomy, B02 pipeline, B03
design tell, BVDT verdict, BHTF your-turn, BOUT outro) — the same compact
skill-teardown shape as the `matter-briefing` sibling. Result here: B00 + 7
body beats (B01-B07) + BCRY/BHTF/BOUT = 11 beats — the identical-shape
expansion used on that sibling and the `case-brief`/`gaps` redos.

**B00 WRITER LAW — defect found and fixed:** first pass used
`triggerWords: "every matter"` (a two-word phrase). `BrutalistHesitantWriter`
(`runtime/remotion/src/scenes/BrutalistHesitantWriter.tsx`) tokenizes the
typed text on whitespace and matches each trigger against a SINGLE TOKEN's
core word (punctuation-stripped) — a multi-word trigger can never equal a
single token, so the correction silently never fires. Confirmed by pulling
frames from the first compiled master: at t=7.8s the writer had typed the
full WRONG sentence ("Claude already sees every matter I have. Is that
right?") straight through, no hesitation, no accent, no correction —
violating the WRITER LAW's whole point. Fixed by rewording to a
single-word trigger: text "Claude already knows\nevery matter I
have.\nIs that right?", `triggerWords: "every"` → `replacementWords: "just
this one"`. Regenerated B00's audio only (narration updated to match:
"...it stays inside just this one..."), re-rendered B00 only via
`remotion_scenes.py --only B00 --force`, verified via frame pulls at t=5.5s
and t=7.5s inside the new media/B00.mp4 that the correction resolves to
"just this one" and the full question types out to "Is that right?" before
the beat ends — then recompiled the whole master and reconfirmed the same
on the compiled cut (frame at t=7.5s). Updated SCRIPT.md's audit table and
CARRY-OUT.md's wrong-guess description to match the real trigger word.
Audio 8.70s (Remotion extended to 8.7s) — clears the ≥8s WRITER LAW floor.

**Body beats (B01-B07):** all Manim GRAPHIC scenes, reusing the generic
"chip row" / "chip stack" renderer verbatim from the `matter-briefing`
sibling, adapted in this reel's own `scenes.py` with matter-workspace-
specific chip labels and narration (avoiding hyphens and isolated
single-letter words in SANS chip labels per that sibling's logged GATE T
lessons; MONO-font path labels like `matter-workspace/` and `CLAUDE.md`
keep their literal characters, matching precedent). Anchor pair: B03
plants `matter-workspace/` + `SKILL.md` as two plain chips; B06 returns
the identical composition with `SKILL.md` accented.

**GATE T:** PASS on first run, no fix pass required (0 FAILs across all 11
beats, both before and after the B00 fix and recompile).

Built end to end this invocation: QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json (11 beats), `scenes.py`, `render_scenes.py`. Ran
`generate_audio_kokoro.py` (11/11 beats, am_onyx, $0.00) — measured
durations became the clock. Rendered 7 Manim beats (foreground,
`render_scenes.py`, exit 0) and 4 Remotion beats via `remotion_scenes.py`
(foreground, exit 0) — plus one targeted B00 re-render after the trigger
fix (foreground, exit 0). No backgrounding was left unattended: two
commands were auto-moved to background by the harness on a 120s timeout,
and both were blocked on synchronously via `TaskOutput(block=true)` in the
same turn before proceeding, per the COMPLETION LAW.

**Compile:** `compile.py` forced a clean 3840×2160 master directly (no
declared slates — all 11 beats real media), twice (once before the B00
fix, once after). Final:
`claude-for-legal--claude-liam-matter-workspace.mp4`, 112.2s. One
non-blocking WARNING carried through compile: GRAPHIC beats are 7/11
(63%), over the toolkit's ~40% "pantry cap" motion-diversity guidance
(MOTION.md) — noted, not treated as a gate; this reel is legitimately
diagram-heavy (a skill's anatomy/mechanism/isolation argument reads
naturally as labeled-chip diagrams) and every GRAPHIC beat is original,
locally-rendered Manim, not pantry/stock footage.

**Gate V (visual QC):** pulled one representative frame per beat from the
compiled 4K master and read each by hand — all legible, correct chip
content, safe insets, no overlapping text, the B03→B06 anchor pair
visually identical as intended, B07's vertical-stack layout reads cleanly,
BHTF's `folderLabel` correctly shows `@HumanitariansAI`, BOUT carries the
HAI subscribe skin. B00's correction frame reconfirmed on the final
compiled master at t=7.5s: "just this one" resolved, full question typed
out ("Is that right?"), cursor blinking, well before the beat ends.

**Audio presence:** `ffmpeg -af volumedetect` on the final compiled
master: mean_volume **−24.1 dB**, max_volume −2.9 dB — comfortably clears
the −40 dB floor. Confirmed via `ffprobe` the master carries both a video
stream (3840×2160) and an audio stream, duration 112.2s.

**Master vs. beat_sheet.json:** final master mtime (18:27) is newer than
beat_sheet.json's last content edit (18:25, the B00 fix); beat_sheet.json
was NOT touched after the final recompile, per the "never touch
beat_sheet.json after compile" law.

**Playlist resolution:** `SUBJECT.json`'s family `"claude-for-legal"`
matches no prefix in `loop/playlists.json`'s map directly; fell through to
the `"hai-simple"` prefix (this reel's own `skill` field / parent
directory), which resolves to **"Claude Basics."** Not the bare "Claude,"
per the PLAYLIST LAW.

**Status: DONE.** Review cut passes every gate (content-check,
frame-check, lane-check, GATE AUDIO, GATE T, Gate V by eye, WRITER LAW
correction verified on the compiled master after the trigger-word fix).
Source-fidelity note logged above and in QUESTION.md/SCRIPT.md/the
description's "Deliberately not claimed" section — nothing about
matter-workspace's actual per-matter output beyond the source's own stated
facts is asserted anywhere in this reel.
