# Script — "What an AI Actually Built."
**Narrator:** Yeshwanth · **Voice:** `am_onyx` (Kokoro, local) · **Channel:** @HumanitariansAI

Full narration, all 12 beats, exactly as synthesized. Audio is the master clock.

## B00 — cold open — the hook
*16:9 scene:* `ClaudeComposerAsk` · *9:16 scene:* `ClaudeComposerAsk916` · *Measured:* 15.53s

> Hi, I'm Yeshwanth. Someone lost a game. Not the idea — the actual game, the thing you could open and play. What was left behind was a folder of leftovers. So we asked an AI assistant to build it again from those leftovers. And the first thing it found was that the game's own name was wrong.

## B01 — the whole idea in one breath
*16:9 scene:* `BrutalistHesitantWriter` · *9:16 scene:* `BrutalistHesitantWriter916` · *Measured:* 14.27s

> Here is the whole thing in one breath, before any of the detail. An AI built this, with a person deciding. It wrote the instructions. A person set the rules. Every automatic check passed. And it was still broken. That last line is what this whole video is about.

*Vertical cut uses a slightly longer version of this beat, so the on-screen writing finishes before the midpoint:*

> Here is the whole thing in one breath, before any of the detail. An AI built this, with a person deciding. It wrote the instructions. A person set the rules. Every automatic check passed. And it was still broken. That last line is what this whole video is about, and everything after it is simply how that happened. It is the difference between working and actually usable.

## B02 — the leftovers
*16:9 scene:* `GodotFreeChips` · *9:16 scene:* `GodotFreeChips916` · *Measured:* 18.86s

> So, the leftovers. When the original was lost, twenty-seven files of instructions survived, and a folder of two hundred and eighty-six pictures. That was everything. No levels. No sound. None of the settings that turn a pile of files into something you can actually open and play. And those pictures were never used, deliberately, because nobody can prove who owns them.

## B03 — the rules, set before any building
*16:9 scene:* `ClaudeComposerAsk` · *9:16 scene:* `ClaudeComposerAsk916` · *Measured:* 16.23s

> Before any of the building started, the person set three rules. Don't touch the original files — read them and leave them alone. Don't invent anything you can't find in the source. And if you can't finish something, write it down where I can see it. Those three rules are the only reason anybody can check this work afterwards.

## B04 — what the AI built
*16:9 scene:* `GodotFreeChips` · *9:16 scene:* `GodotFreeChips916` · *Measured:* 20.33s

> Then it built. Two thousand seven hundred and sixty-nine lines of instructions, across nineteen files, in one sitting. And here is the strange part. A game normally has a file that lays out what goes where. This one has exactly one, and it is six lines long. Everything else is drawn as the game starts. There are no pictures in the folder at all — every monster, every tower, every tile is drawn by the instructions.

## B05 — the real thing, running
*16:9 scene:* `still image` · *9:16 scene:* `— (not in vertical)` · *Measured:* 14.74s

> This is it actually running. Towers sitting along a path, monsters walking down it, little health bars above their heads. You place the towers, the monsters walk, your towers shoot them before they get through. Everything you can see there was drawn by the instructions as the game started.

## B06 — the surprise — the one code shot
*16:9 scene:* `ClaudeCodeBeat` · *9:16 scene:* `ClaudeCodeBeat916` · *Measured:* 21.12s

> Now the surprise. The game is called an elemental tower defense. Fire, ice, poison, storm. But when the AI read the original instructions, the elements were not there. This is the piece that decides what a hit does, and it is the only code I will show you. Take damage. If the monster is already gone, stop. Otherwise subtract. If health hits zero, it dies. Read it again — nothing in there asks what kind of damage it was.

## B07 — what elemental actually means here
*16:9 scene:* `WtDamageCollapse` · *9:16 scene:* `WtDamageCollapse916` · *Measured:* 20.57s

> So what does elemental actually mean in this game? The four monster colours are only colours. They share one pool of health and one speed. The towers do differ, but only in their side effects. Ice slows things down. Poison keeps hurting after the hit lands. Storm jumps across to a nearby target. That is real, and it is worth having. It just isn't a system of strengths and weaknesses, which is what the name promises.

## B08 — the ending, part one — the dead keyboard
*16:9 scene:* `WtCheckGrid` · *9:16 scene:* `WtCheckGrid916` · *Measured:* 26.58s

> And then it was finished. Fifty-six automatic checks — small programs that play part of the game and report whether it behaved — all passing. The game starts and stops cleanly. By every measure available, done. Then a person opened it and pressed a key. Nothing happened. Nothing on the keyboard worked at all. A rewrite had quietly deleted the few lines that tell the game which keys to listen for. Fifty-six checks were green the whole time, because not one of them had ever pressed a key.

## B09 — the ending, part two — playable, and miserable
*16:9 scene:* `WtPacingTable` · *9:16 scene:* `WtPacingTable916` · *Measured:* 27.77s

> They fixed that. Then they played it again, and it worked, and it was miserable. Monsters crawled across the board at forty-four pixels a second. A single wave took twenty-six seconds to sit and watch. The AI had copied the original's timings exactly — but the original measured distance differently, so the very same numbers meant something three times slower here. Scaling the clock fixed it. Forty-four becomes one hundred and thirty-two. Twenty-six seconds becomes eight and a half. Same difficulty, just playable.

## B10 — the honest ending and the handoff
*16:9 scene:* `ClaudeComposerAsk` · *9:16 scene:* `ClaudeComposerAsk916` · *Measured:* 27.75s

> So here is the honest ending. The checks confirmed the game did what it was told. They could not tell anyone it was no fun to play. A person did that, in minutes. And it still isn't finished — the playtest list has twenty-two empty rows, the difficulty is untested, and there is one level. If you take one thing away, take this question, and ask it about anything you build with an AI. What would this have to get wrong for every test to still pass? Sit with that answer for a minute. It is usually the part a person has to go and look at.

## B11 — outro — title restate
*16:9 scene:* `GodotTitleOutro` · *9:16 scene:* `GodotTitleOutro916` · *Measured:* 4.97s

> A working game. Built by an AI. Decided by a person. And not finished yet.

---

**Total:** 228.7s across 12 beats (16:9). The 9:16 cut runs 11 beats.

## What the viewer should be able to say afterwards

1. **What was made** — a working tower-defense game, rebuilt in Godot (the free
   software you build a game inside) from the leftovers of a dead student project.
2. **How** — a person gave an AI a folder of salvaged code and three rules. The
   AI wrote the new game. The person made every decision that mattered.
3. **Where the limit is** — it passed 56 automatic checks and was still broken,
   twice, until a human opened it and pressed a key.

## Difference between the two cuts

The 9:16 drops **B05**, the captured frame of the game running: a landscape
screenshot cannot fill a portrait safe area without crossing its edges. B01 also
runs longer in portrait, because the on-screen writing takes about nine seconds
there and has to finish before the frame is sampled. Every other beat matches,
re-rendered portrait-native rather than cropped.
