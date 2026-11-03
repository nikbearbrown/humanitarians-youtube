# PROMPTS.md — hai-4k-five-packages

Beat-prefixed record of what each beat asks for.

**There are no open slots in this reel.** Every beat is machine-renderable —
nine Manim scenes in this folder's own `scenes.py` and two Remotion bookends
using a composition that is already registered. Nothing is owed by a human, and
no beat should resolve to a slate. If one does, it is a render failure rather
than a missing asset, and the cause is in the console output, not here.

No generative image or video prompts are used. Nothing in this reel is
AI-generated media.

## Per beat

**B00** — `ClaudeComposerAsk`, props in the beat sheet. The command reads
`where does the resolution question get answered?` and the three output lines
answer it. `folderLabel` is set to `@HumanitariansAI` rather than left on the
component's default.

**B01** — Manim `B01_FourNumbers`. Draw one question and four answers. Each
height value arrives with the file it came from beneath it, in muted ink. The
two that match the stated targets stay in teal; the two that do not go crimson.
One accent moment only, on the mismatch.

**B02** — Manim `B02_ThreePositions`. A left-to-right spine with three stations.
A marker travels it while a count of how many people are involved rises. No
arrows crossing labels.

**B03** — Manim `B03_StarterKit`. Two stacked cards: the pasted block, then the
checklist with green and red marks. The limit line sits beneath in muted ink,
same size as the rest — not shrunk or rushed.

**B04** — Manim `B04_Standardise`. A write being declined, with the existing
placeholder-card rule shown beside it. The point is the symmetry: the new rule
is a sibling of one already in the toolkit.

**B05** — Manim `B05_DriveReport`. A table filling row by row — fellow, file,
format, resolution, verdict. Then the dependency underneath: the grouping only
works because the name is in the filename.

**B06** — Manim `B06_RealVsStretched`. Show the arithmetic rather than faking a
blur: `1280×720`, doubled to `2560×1440`, then stretched to `3840×2160`, with
the stretch marked. A frame can carry the right dimensions and less picture than
they imply.

**B07** — Manim `B07_SortFolders`. Files routing into two folders. The failing
one carries the corrected value as a note, not just a verdict.

**B08** — Manim `B08_HonestAccounting`. Five package cards collapse into two
build cards and a document.

**B09** — `ClaudeComposerAsk`, greeting `Your turn.` The command is the question
for the viewer; the single output line extends it.

**B10** — Manim `B10_Outro`. Title restate with a terracotta period,
`@HumanitariansAI` beneath. Silent by design — `audio_policy: "silence"` in the
beat sheet, so no narration file is expected for this beat.

## Voice

`am_michael`, set in `metadata.voice_kokoro`. There is no voice lock in this
toolkit — `VOICE-LOCK.md` does not exist, and
`runtime/scripts/generate_audio_kokoro.py:77` sets `am_onyx` only as a
non-fellows fallback, with no rule attached. `am_michael` is present in the
voice pack, confirmed via `--list-voices`.
