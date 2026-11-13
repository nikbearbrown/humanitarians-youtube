# What an AI Actually Built.

**Author:** Yeshwanth B · **Channel:** @HumanitariansAI · **Built:** 2026-09-22
Voice: am_onyx (Kokoro), chosen series voice

Videos (Google Drive): https://drive.google.com/drive/folders/1NssBvB7VNQPvtZwQYGXoV5tCF6s0iY32?usp=drive_link

---

## Subject

A just-under-four-minute explainer for someone who has never opened a game
engine, never written code, and has never heard the word "porting." It answers
three questions in order, and the third one is the ending.

1. **What was made.** A working tower-defense game — you place towers along a
   path, monsters walk it, your towers shoot them — rebuilt in Godot, the free
   software you build a game inside, from the leftovers of a lost student
   project.
2. **How it was made.** A person handed an AI assistant 27 files of salvaged
   instructions and three rules. The AI wrote the new game. The person made
   every decision that mattered.
3. **Where the limit is.** The result passed 56 automatic checks and was still
   broken — twice — until a human opened it and pressed a key.

**Takeaway:** the checks confirmed the game did what it was told. They could not
tell anyone it was no fun to play. A person did that, in minutes.

## Deliverables

| File | What it is |
|---|---|
| `beat_sheet.json` | The 16:9 beat sheet — 12 beats, primary source of the film |
| `beat_sheet_vertical.json` | The 9:16 beat sheet — 11 beats, portrait-native |
| `script.md` | Full narration with measured durations, and the jargon table |
| `src/WalkerTeardown.tsx` | 7 reel-local scenes (4 landscape + 3 portrait) |
| `src/GodotReadable.tsx` | Scenes reused from the previous reel, incl. the outro card |
| `src/ClaudeCodeBeat916.tsx` | Portrait code beat — a gap in the shared 916 family |

Videos go to Google Drive, not this repo: this folder is text only.

## Build notes

Built with the `brutalist.art` toolkit (`ai-explainer` skill, Plain register) at
commit `ba2d0e0f` plus the local additions below. Kokoro TTS, Manim and Remotion
all run locally and free; no paid API was called and nothing was published.

**Both ratios are native.** Each beat renders per-aspect at 4K (3840×2160
landscape; 2160×3840 portrait, downscaled to 1080×1920). The portrait cut is a
separate beat sheet whose every Remotion beat is rewired to a `*916`
composition — stacked instead of side-by-side, retyped for a tall frame. No
cropping at any stage. Both cuts pass GATE V with **zero BLOCKER and zero
MAJOR**, and both masters cleared `final_frame_check`.

### Toolkit changes this video required

1. **Three new portrait components** — `WtDamageCollapse916`, `WtCheckGrid916`,
   `WtPacingTable916`. Their landscape twins existed; the 916 family did not
   have them, so the vertical could not have been portrait-native without them.
2. **Registered-duration fixes.** See the note below — this is the one worth
   reading.

### The render-duration trap

`remotion_scenes.py` renders a beat at the composition's **registered**
`durationInFrames`, then conforms the clip to the narration length by
truncating. But `useP()` normalises against the registered duration. So when

    beat_seconds × 30  <  registered durationInFrames

the animation is cut off part-way and its tail never renders at all.

The symptom is always an `underfill` or a missing element, which looks like a
layout bug and is not. It cost several wasted passes across two reels before the
pattern was clear. In this build it explained the portrait outro appearing
without its handle and subline (registered 480 frames, beat 156 → `p` peaked at
0.33).

**Rule: register short, never long.** A composition shorter than its beat
finishes and freeze-holds the last frame, which is harmless. A composition
longer than its beat is silently truncated.

Durations corrected here: `GodotTitleOutro916` 480 → 150,
`BrutalistHesitantWriter916` 606 → 480.

### Other things worth knowing

- **`BrutalistHesitantWriter` keystrokes are floor-limited to one frame.**
  Lowering `charMs` below ~33ms does nothing. A typing beat that looks sparse at
  its midpoint needs a **longer beat**, not faster typing.
- **`./art final` enforces zero MAJOR.** `ART_STRICT=0` relaxes only the review
  gate, not the master gate. Anything left as an "accepted" MAJOR will refuse
  the master.
- **The outro is not the locked house card.** `ClaudeTitleOutro` hardcodes
  `@NikBearBrown` and `OUTRO-LOCK.md` scopes it to claude-liam reels only, so
  `@HumanitariansAI` uses its own `GodotTitleOutro`. The compiler emits a
  `skin_warnings` line for this; it is intentional.

## Research / fact-check note on the claims

Every factual claim traces to `GAME-BRIEF.md` §10 or Appendix A, or was
re-derived against the game repository, which was **read-only** throughout.

**Verified:** 27 surviving C# files and 286 unused pictures (Appendix A.1,
counted before the original folder was deleted on 21 September); 2,769 lines of
instructions across 19 files, one layout file of 6 lines, and zero image or
audio files in the shipped game (all re-derived with `find` and `wc -l`); the
damage rule at `monster.gd` shown verbatim; 56 checks across three suites, and
the two failures with the full before/after pacing table (§16.3).

**Three corrections applied.** The brief's `take_damage` excerpt is stale — the
live file has a `hit_flash` line added by the pacing fix, so the reel shows the
current file and claims no line count. The brief's commit count is
self-contradictory (13 in three places, 9 in §13; the repo says 14) and its
file count is stale (63 vs 76); neither number appears on screen, because
counts that drift date a video. And the reel says **56** checks throughout, not
65 — 56 is what was passing at the moment the keyboard was found dead; the nine
keyboard checks that make 65 were written afterwards.

**Section 14 audit.** All nine prohibitions were checked line by line against
the final narration. The reel never says the AI built a game from scratch (it
rebuilt someone else's recovered project), never calls it finished (B10 lists
the 22 empty playtest rows, the untested difficulty, the single level), and
never claims it resembles the original (the 286 sprites are named as
deliberately unused, on ownership grounds).

## Media

**No gameplay footage exists.** Godot is not installed on the build machine
(`command -v godot` returns nothing; no `/Applications/Godot*`), so neither
`godot --path godot` nor the repo's `capture_game.gd` could be run and no screen
recording was possible. B05 in the 16:9 cut therefore uses
`evidence/screens/03-wave-in-progress.png` — a real frame the engine drew,
matted inside the safe area — rather than a diagram. If footage is recorded
later it is a one-file swap: drop `media/B05.mp4` into the reel and rebuild.
