# BUILD-LOG — claude-for-legal--claude-liam-infringement-triage

## 2026-08-30 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/claude-for-legal/youtube/claude-liam-infringement-triage/beat_sheet.json`.

**Source-gap finding (logged, not asked — see QUESTION.md for full detail):**
the source sheet is fully "built" (7 beats, all marked VIDEO/filled, dated
2026-07-25) but its narration text carries literal, never-filled template
placeholders (`>`) at every point where the actual skill-specific fact
should be: `"The skill is infringement-triage. >."`, `"Claude's job: >."`,
`"The SKILL.md is the spec — >."`, `"I want to >."` Its `source_skill`
field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ip-legal/skills/infringement-triage/SKILL.md`
— `/Users/bear/Documents/CoWork` does not exist at all on this machine, and
a full-tree search found no `ip-legal` folder or `infringement-triage`
SKILL.md anywhere. So there were no real facts to carry over from the
source, only a topic (INFRINGEMENT-TRIAGE, an Anthropic skill for IP legal
practice) and a shape (Teardown skill-teardown format, 7 beats: cold open,
anatomy, pipeline, design tell, verdict, handoff, outro). Same defect class
already logged on sibling `claude-for-legal--*` redos in this factory
(`-ai-inventory`, `-ai-tool-handoff`, `-amendment-history`, `-board-minutes`,
`-dsar-response`).

**The call:** rather than block on a missing human answer, reconstructed the
evident subject into a generic, defensible account of what triaging an
incoming infringement claim/letter means and why sorting comes before
responding — described generically per the fresh-script Phase 1 rule ("when
in doubt, describe behavior generically") rather than inventing specific
tool names, UI, or product claims. No fact in the resulting script is
Claude-specific or unverifiable.

Register re-registered Teardown -> Plain: the source's B03 framed "Claude's
job" and "what it gets right / where it bites" as a design-tell verdict —
Teardown language. Plain instead states the mechanism (four triage checks)
and its failure modes (checked is not valid; bare today is not ignorable
forever) as properties of the practice, never a verdict on any specific
skill's design. Source's BVDT verdict recap folded into a dedicated BCRY
carry-out beat per CARRY-OUT LAW. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"respond" -> "triage" — the naive assumption that the first move is to
respond, corrected to the fact that the first move is to triage). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Added an
anchor (B02 -> B03: the packaging-infringement letter, all exclamation
points and no attachments, then run through the same four checks as
everything else and found to be the real one) and a both-directions beat
(B03) per this factory's PHASE 1 structure requirement — the source (being
unfilled) carried neither.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`. Durations: B00
   8.75s, B01 20.48s, B02 16.06s, B03 23.25s, BCRY 9.79s, BHTF 20.42s,
   BOUT 4.65s.
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `INFTRGB01Scene` /
   `INFTRGB02Scene` / `INFTRGB03Scene`) and `render_scenes.py`; rendered all
   three in the foreground.
3. Rendered B00/BCRY/BHTF/BOUT via `remotion_scenes.py`. The process
   exceeded the shell's 120s inline timeout and the harness moved it to a
   tracked background task; per the COMPLETION LAW for one-shot
   invocations, blocked on that task's own completion via `TaskOutput`
   rather than ending the turn — confirmed exit code 0 (all 4 beats "ok")
   before proceeding.
4. **B00 TIMING LAW failure caught and fixed before first compile:** the
   first B00 draft text ("An infringement letter\njust landed in the
   inbox.\nDo we need\nto respond right now?") never reached its own
   trigger word inside the 8.8s beat — pulled frames at t=3/4.5/6/7.5/8.6s
   and read them directly: at t=8.6s (near the very end) the writer had
   only reached "Do we need" with the cursor mid-typing, the correction
   never appearing. Same failure class the skill's SKILL.md names from the
   2026-08-27 pilot. Root-caused to too much preamble before the trigger
   word for the beat's actual (shorter, 8.75s) narration window. Shortened
   the writer text to "Do we need\nto respond\nright now?" (trigger
   "respond" -> "triage"), re-rendered B00 alone. Re-verified: correction
   already complete and visible by t=4.5s, full corrected question legible
   by t=8.6s — well inside the beat.
5. First `compile.py` pass -> 7/7 real (no slate), 3840x2160 (THE 4K LAW),
   mean_volume -24.0 dB (already passing GATE AUDIO).

**GATE T (type_check.py) — one finding, fixed (real defect, not a false
positive this time):**

- First pass: FAIL (1 pixel beat). B02's "THE ANCHOR" label, colored in the
  humanitarians CRIMSON accent (#E4572E) directly on the cream ground,
  measured ~3.1:1 contrast — below the 4.5:1 WCAG floor the checker
  enforces (computed independently: sRGB relative luminance of #E4572E on
  #F3EBDD is ~3.12:1). Fixed per the checker's own suggested remedy:
  recolored the label to INK. Re-rendered B02, recompiled.
- Second pass: **PASS (0 FAILs)**.

**Gate V (visual) — first pass found two real defects, both fixed:**

Pulled frames every 5s across the full 104.4s runtime and read them
directly. Found a genuine Manim `Text()` rendering bug — not a design
issue — in two unrelated multi-word caption strings:
1. **B01**: `Text("waits in the same line", ..., slant=ITALIC)` rendered
   with the inter-word spaces silently collapsed for "the same line",
   reading as "waits in thesameline" on screen (confirmed by cropping and
   zooming the exact frame — the words were genuinely merged, not just
   tightly kerned).
2. **B03**: `Text("bare today is not ignorable forever", ..., weight=BOLD)`
   (non-italic, different font) showed the identical collapse:
   "baretodayisnotignorableforever".
Root-caused to Manim/Pango dropping inter-word spacing on longer
single-`Text()` prose strings (observed only on the two longest free
strings in the file; shorter multi-word strings and strings built through
`_fit_text` were unaffected). Fixed both by rebuilding each caption as a
`VGroup` of per-word `Text()` mobjects arranged with `.arrange(RIGHT,
buff=...)` instead of one string — this guarantees explicit inter-word
spacing regardless of the underlying text-shaping quirk. Re-rendered B01
and B03, recompiled, re-ran GATE T (still PASS, no regression), and
re-pulled all 21 frames across the full runtime: both captions now read
correctly, and every other beat (B00, B02, BCRY, BHTF, BOUT) was already
clean on the first pass — legible, safe inset respected, no overlap.

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component behavior
already logged unremarked in sibling reels in this family.

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840x2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs) after the B02 contrast fix above
- Gate V: PASS after fixing the two Manim text-spacing defects above
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.9 dB
- ffprobe: duration 104.417s; mp4 mtime (1788088349) newer than
  beat_sheet.json mtime (1788087822)

**Non-blocking warning (compile.py):** motion histogram remotion:4
graphic:3 — remotion at more than half of beats. Structural, not a defect:
hai-simple's mandated shape is B00 (writer) + BCRY + BHTF (Your Turn) + BOUT
(outro) all REMOTION by skill contract, against 3 GRAPHIC body beats for
this 7-beat reel — same disposition as every other short hai-simple reel in
this family.

**Playlist resolution:** family `claude-for-legal` does not match any
prefix key in `skills/make/hai-simple/loop/playlists.json`. Per the map's
documented fallback ("match SUBJECT.json's family, or the hai-simple
prefix"), fell through to matching the skill name itself: `hai-simple` is a
literal key in the map, resolving to **Claude Basics**.

Metadata file written: `claude-for-legal--claude-liam-infringement-triage.md`
(channel @HumanitariansAI, Playlist: **Claude Basics**, plus the direct
code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
