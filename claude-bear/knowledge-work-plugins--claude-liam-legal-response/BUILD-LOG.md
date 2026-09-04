# BUILD-LOG — knowledge-work-plugins--claude-liam-legal-response

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-legal-response/beat_sheet.json`.

**Source note:** the source sheet's narration already carries real,
specific facts about the Anthropic `legal-response` skill (not an unfilled
placeholder shell) — see QUESTION.md. Facts preserved: the skill generates
a response to a common legal inquiry using configured templates, with
built-in escalation checks for situations that shouldn't use a templated
reply (data subject requests, litigation hold notices, vendor legal
questions, NDA requests, subpoenas); always presents the draft response for
user review before suggesting it be sent; same input → same output every
run; limited to only what the SKILL.md specifies. The `source_skill` path
it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/legal/skills/legal-response/SKILL.md`)
does not exist on this machine (different machine's home directory, same
situation as the `financial-services` sibling redos — e.g.
`claude-liam-kyc-doc-parse`), but no reconstruction was needed.

**The call:** register re-registered Teardown → Plain. Source's BVDT
framed reliability and scope as a verdict recap ("know the limit: only
what the file says") — Teardown language — removed; Plain states only the
mechanism (match to a template, draft, escalation check, hold for review)
and its two failure directions as properties of the practice, never a
verdict on the skill's design. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` per WRITER LAW: "send" →
"draft it for review" — the naive assumption that the skill sends its own
answer, corrected to: it drafts, then waits. Added a wrong-guess beat (B01:
"reads → drafts → sends" pipeline vs. "match → draft → hold for review"
pipeline, falsified by "send it a request that doesn't fit any template —
a subpoena with unusual terms, say — and it doesn't force a reply anyway.
It flags the situation for escalation and stops") and an anchor (B02 → B03:
one data-subject request walked through inquiry / template match / draft
assembled / escalation check / held for review, returning to split into
"ready is not sent" / "flagged is not answered") per this factory's PHASE 1
structure, since the source's Teardown shape carried neither. Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. Kept the
source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT). No source
beat was AI-VIDEO, pantry, or a human-drop slot — every source beat was
already REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no beat replacement
beyond B00 itself.

Built end to end this invocation:

1. `generate_audio_kokoro.py` — 7 beats, free, `am_onyx`, first pass, no
   retries needed. Durations: B00 10.45s, B01 20.20s, B02 15.74s, B03
   17.77s, BCRY 15.55s, BHTF 19.05s, BOUT 4.95s (+1.0s tail).
2. Wrote `scenes.py` (3 Manim scenes, reel-unique names `LGB01Scene` /
   `LGB02Scene` / `LGB03Scene`, adapted from the `kyc-doc-parse` sibling's
   worked-around card-border pattern — TEAL borders, not INK, the
   traveling token fading beside each card, off-card overflow lines) and
   `render_scenes.py`; rendered B01, B02, B03 clean on the first pass.
3. Rendered the Remotion beats via `remotion_scenes.py`. **B00 defect
   found and fixed before compile:** the first draft's `triggerWords`
   ("send the reply") was a 3-word phrase, but `BrutalistHesitantWriter`
   matches `triggerWords` against a single whitespace-split token (see
   `BrutalistHesitantWriter.tsx` line 130: `triggers.indexOf(core.toLowerCase())`
   on each token) — a multi-word trigger silently never matches, so the
   first render typed the naive question and never corrected it (confirmed
   by pulling frames at t=2s through t=10.3s, all showing the uncorrected
   "send the reply?"). Fixed by rewriting the naive text to end on a
   single-token trigger ("just send?") with `triggerWords: "send"` →
   `replacementWords: "draft it for review"`, giving a grammatically clean
   final question ("...just draft it for review?"). Re-rendered B00 only;
   confirmed at t=6.5s the trigger word "send" in terracotta pre-deletion,
   and at t=9s the corrected final question legible. A second render
   attempt was truncated to 4.47s by my own diagnostic `timeout 110`
   wrapper (signal 15 mid-stitch, per the COMPLETION LAW's "run in the
   foreground and wait on exit code" — the wrapper's shorter cap was my
   error, not the render's); deleted the truncated file and re-ran with no
   artificial cap, landing the correct 10.47s clip. Also mid-build, the
   full remotion_scenes.py invocation for all 4 Remotion beats exceeded the
   tool's 120s auto-backgrounding threshold; per COMPLETION LAW / ONE-SHOT
   warning, did not end the turn — located the running PID and blocked on
   it in the foreground (`while kill -0 <pid>; do sleep 5; done`) until it
   exited, then confirmed all 4 beats present.
4. First `compile.py` pass → 7/7 real (no slate), 3840×2160, mean_volume
   -24.0 dB, motion histogram remotion:4 graphic:3.
5. GATE T (`type_check.py`) → **FAIL on first pass**: B03 smallest text run
   18px < floor 20px, traced to the top-row pipeline labels using
   `font_size=26` before the `row.animate.scale(0.55)` shrink (the
   `kyc-doc-parse` sibling's working value for the equivalent shrunk row
   was `font_size=34`, pre-emptively noted in that sibling's own comments
   as the fix for this exact defect class — I had copied the pattern but
   used a smaller value). Bumped to `font_size=34`, re-rendered B03 only,
   recompiled, re-ran GATE T → **PASS**, 0 FAILs.
6. Gate V (visual, manual): pulled 14 frames every 8s across the full
   104.7s runtime and read every one directly. B00's correction ("send" →
   "draft it for review") lands legibly and reads as a grammatically clean
   final question; B01's struck "reads → drafts → sends" pipeline and lit
   "match → draft → hold for review" pipeline read cleanly, including the
   off-card "no template fits — flagged for escalation, not forced" line;
   B02's five-stage anchor (with the fading "DATA-SUBJECT REQUEST" token
   beside each card) is legible at every step; B03's anchor-return and
   both-directions split ("ready is not sent" / "flagged is not answered")
   read cleanly, including the strike-through on "SENT?"; BCRY's carry-out
   quote, BHTF's Your Turn composer card, and BOUT's title outro all render
   legibly with no text overlap or contrast issues. The five pipeline-stage
   cards in the shrunk B03 top row sit edge-to-edge with zero gap (by
   design — `card_w` equals the spacing between `xs` centers, inherited
   unchanged from the `kyc-doc-parse` sibling's identical layout, which
   shipped and passed the same manual Gate V read); no text is clipped or
   overlapping. No defects found.
7. Audio presence: `ffprobe` + `ffmpeg -af volumedetect` on the final
   master → mean_volume **-24.0 dB**, max -2.6 dB. Master mtime (03:44:31)
   is newer than beat_sheet.json mtime (03:40:03).

**Noted, not a defect introduced here:** `OutroCTA` renders on flat white
rather than the humanitarians cream ground — same shared-component
behavior already logged unremarked in sibling reels in this loop (e.g.
`financial-services--claude-liam-kyc-doc-parse`).

**Gates (final state):**
- content-check: PASS (7 beats, no violations)
- frame-check: PASS (3840×2160, 7 beats, no violations)
- lane-check: PASS (no lane violations, cut=master)
- GATE T: PASS (0 FAILs), second pass (B03 min-size fix)
- Gate V: PASS, first pass after the B00/B03 fixes — no defects found
- GATE AUDIO: PASS — mean_volume **-24.0 dB** (ffmpeg volumedetect), max
  -2.6 dB
- ffprobe: duration 104.7s; mp4 mtime newer than beat_sheet.json mtime

**Playlist resolution:** family `knowledge-work-plugins` matches the
`knowledge-work-plugins` prefix key in
`skills/make/hai-simple/loop/playlists.json` directly → **Extending
Claude — Skills, Plugins & Connectors**.

Metadata file written: `knowledge-work-plugins--claude-liam-legal-response.md`
(channel @HumanitariansAI, Playlist: **Extending Claude — Skills, Plugins &
Connectors**, plus the direct code link per the DELIVERY CONTRACT format).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to
Phase 4 (4K render + deliver.py) in this same invocation.
