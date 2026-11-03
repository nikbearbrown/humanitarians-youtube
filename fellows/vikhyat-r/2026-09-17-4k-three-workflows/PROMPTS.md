# PROMPTS.md — hai-4k-three-workflows

Beat-prefixed record of what each beat asks for.

**There are no open slots in this reel.** Eight Manim scenes in this folder's
own `scenes.py`, two Remotion bookends on a composition that is already
registered. Nothing is owed by a human, and no beat should resolve to a slate.
If one does it is a render failure, not a missing asset, and the cause is in the
console output rather than here.

No generative image or video prompts are used. Nothing here is AI-generated
media.

## Per beat

**B00** — `ClaudeComposerAsk`. The command asks how the five packages fit
together; the three output lines answer it with the three verbs. `folderLabel`
set to `@HumanitariansAI` rather than the component default.

**B01** — Manim `B01_ThreeNamed`. Three lanes. Name, then role, then the verb
each one owns. The verbs land last and stay.

**B02** — Manim `B02_WorkflowA`. Flow left to right: paste, build, render,
check. The check refuses and loops back to build; that return path is the whole
scene. The upload node only fills once the loop is satisfied.

**B03** — Manim `B03_WorkflowB`. A funnel, drawn wide to narrow. The top band
is the metadata pass over the whole folder; the narrow band below is the frame
check on survivors only. The width difference carries the cost argument without
a number.

**B04** — Manim `B04_WorkflowC`. B's verdict arrives already settled, then
routes into two folders. The move log runs as a rail beneath both, because
traceability is the answer to the obvious objection.

**B05** — Manim `B05_WhatSeparates`. Three rows, one sentence each, nothing
else. The restraint is deliberate: this is the beat where the viewer should be
reading, not watching.

**B06** — Manim `B06_TheOrder`. A single vertical spine with A, B, C on it —
never three parallel columns, because parallel columns would say "choose one",
which is the misreading this beat exists to prevent.

**B07** — Manim `B07_YouTubeCaveat`. Two halves. What stays is drawn first and
does not move. What goes is drawn second and leaves. One accent moment, on the
leaving.

**B08** — `ClaudeComposerAsk`, greeting `Your turn.` The command is the
question for the viewer; the single output line sharpens it.

**B09** — Manim `B09_Outro`. Title restate, terracotta period against the final
word, `@HumanitariansAI` beneath. Silent by design — `audio_policy: "silence"`
in the beat sheet, so no narration file is expected.

## Voice

`am_michael`, set in `metadata.voice_kokoro`, matching the companion reel. There
is no voice lock in this toolkit: `VOICE-LOCK.md` does not exist, and
`runtime/scripts/generate_audio_kokoro.py:77` sets `am_onyx` only as a
non-fellows fallback with no rule attached.
