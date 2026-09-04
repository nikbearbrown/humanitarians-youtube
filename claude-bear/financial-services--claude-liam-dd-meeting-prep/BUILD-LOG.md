# BUILD-LOG — financial-services--claude-liam-dd-meeting-prep

## 2026-09-01 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/financial-services/youtube/claude-liam-dd-meeting-prep/beat_sheet.json`
(7-beat Teardown "skill-teardown" sheet for the Anthropic `dd-meeting-prep`
skill, private-equity vertical plugin, brand `claude-liam`, @NikBearBrown).

**Source note:** the source sheet's narration already carries real,
specific facts about the skill — prepare for due diligence meetings:
management presentations, expert network calls, customer references, and
advisor sessions; generates targeted question lists, benchmarks to
reference, and red flags to probe; used before any diligence meeting or
call; triggers on "prep for management meeting", "diligence call prep",
"expert call questions", "customer reference questions", "meeting prep for
[company]" — see QUESTION.md. The `source_skill` path it names (private-equity
vertical plugin `SKILL.md`) does not exist on this machine, but no
reconstruction was needed.

**The call:** register re-registered Teardown -> Plain. Source's B03 framed
"what it gets right / where it bites" as a design-tell verdict — Teardown
language — removed; Plain states only the mechanism (read the meeting
type, match its template, build the question list + benchmarks + red
flags) and its two failure directions as properties of the practice, never
a verdict on the skill's design. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER
LAW: "instinct" -> "the file" — the naive assumption that the sharp
diligence questions come from Claude's own feel for a deal, corrected to:
it reads the meeting type against a file. Added a wrong-guess beat (B01:
private instinct vs. meeting-type-to-outputs procedure, falsified by "ask
it to prep a meeting type the file doesn't cover and it has nothing
tailored to reach for") and an anchor (B02 -> B03: an expert network call
about a staffing company, a "same-store margin trend" question traveling
drafted -> benchmarked -> asked -> flagged when the answer leans on one
large client, then paid off into "run twice, same questions" / "a
regulator sit-down has nothing tailored to reach for") per this factory's
PHASE 1 structure requirement — the source's Teardown shape (anatomy /
pipeline / design-tell / verdict) carried neither. Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. Kept the source's
7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT). No source beat was
AI-VIDEO, pantry, or a human-drop slot — every source beat was already
REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no beat replacement
beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. B00 landed at 10.33s (clear of the >=9s TIMING LAW
   floor) on the first narration draft (34 words + `lead_silence_s: 0.8`).
   Durations: B00 10.33s, B01 30.12s, B02 20.74s, B03 22.95s, BCRY 13.14s,
   BHTF 19.26s, BOUT 4.39s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `DDMB01Scene` /
   `DDMB02Scene` / `DDMB03Scene`, ported from the `dd-checklist` sibling's
   already-fixed TEAL-border card convention) and `render_scenes.py`;
   rendered B01/B02/B03 clean on the first pass, foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`, foreground. First
   invocation hit the shell's 120s default timeout mid-run (B00 and BCRY
   completed; BHTF's `extend_clip_to_duration` step crashed with a
   `FileNotFoundError` on its own intermediate file, leaving a stale
   `media/BHTF.mp4` from the interrupted run) — re-ran with an explicit
   590s tool timeout per the one-shot COMPLETION LAW (never end the turn on
   a backgrounded render), after deleting the stale BHTF output; it
   rendered clean on the retry, and BOUT (which had actually completed
   during the timed-out run) was correctly detected as already filled.
   Confirmed BHTF's explicit `folderLabel: "@HumanitariansAI"` override
   rendered correctly.
4. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.1 dB (GATE AUDIO pass on the first compile). B01's
   30.1s beat (longer than its ~11.4s raw Manim render) required a 2.64x
   slowdown to fill — noted for Gate V review, no legibility issue found.
5. GATE T (`type_check.py`) PASSED clean on the first pass — 0 FAILs
   across all 7 beats. The TEAL-border convention carried over from
   `scenes.py`'s docstring guidance (never TERRA/INK borders on small
   cards) avoided the contrast false-positive documented on the
   `accrual-schedule` / `dd-checklist` sibling reels.
6. Gate V (visual, manual): pulled 12 frames across the full 121.9s
   runtime at settled (not mid-animation) points and read every one
   directly. B00's correction ("instinct" -> "the file") is fully typed
   and settled by t=9.5s of a 10.3s beat; B01's struck instinct figure and
   lit meeting-type procedure card read cleanly, including the "meeting
   type not listed — no template" caption outside the card border; B02's
   four-stop anchor (with the traveling "SAME-STORE MARGIN" token beside
   each TEAL-bordered card) is legible at every step, landing on "leans on
   one large client"; B03's anchor-return and both-directions split (with
   the struck-through "TAILORED?" fully rendered by t=82s) read cleanly;
   BCRY's carry-out quote, BHTF's Your Turn composer card (confirmed
   `@HumanitariansAI`, not the hardcoded default), and BOUT's title outro
   (confirmed `@HumanitariansAI`, no Claude mascot) all render legibly
   with no overlap, no clipping, no contrast issues. No defects found.
7. Audio presence: independently verified with `ffprobe` (h264 3840x2160 +
   aac streams present) and `ffmpeg -af volumedetect` on the final master
   -> mean_volume **-24.1 dB**, max -2.8 dB. Master mtime (1788285352) is
   newer than beat_sheet.json mtime (1788285249).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), first pass
- Gate V: PASS, first pass — no defects found
- GATE AUDIO: PASS — mean_volume **-24.1 dB** (ffmpeg volumedetect), max
  -2.8 dB
- ffprobe: duration 121.9s; mp4 mtime newer than beat_sheet.json mtime

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) +
BOUT (outro) all REMOTION by skill contract, against 3 GRAPHIC body beats
for this 7-beat reel — same disposition as every other short hai-simple
reel in this family.

**Playlist resolution:** family `financial-services` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is
a literal key in the map, resolving to **Claude Basics** — same resolution
as the `dd-checklist`, `accrual-schedule`, and `3-statement-model` sibling
reels in this same family.

Metadata file written:
`financial-services--claude-liam-dd-meeting-prep.md` (channel
@HumanitariansAI, Playlist: **Claude Basics**, plus the direct code link
per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
