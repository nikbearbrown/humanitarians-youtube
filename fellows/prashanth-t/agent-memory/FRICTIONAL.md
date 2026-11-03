# Frictional log — Explainer: How Memory Works in an AI Agent

2026-09-28 — making "How Memory Works in an AI Agent"

* Video / Drive: https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link

What I was working on. A ~200-second plain-language explainer on how memory
works in an AI agent: why a model remembers nothing on its own, the difference
between short-term memory (the running conversation inside the context window)
and long-term memory (a store outside the model you write to and retrieve from).
Fourteen beats, B00–BOUT, built on the Brutalist pipeline.

What I tried, and what I expected.

* I expected "memory" to be the hard part to explain, and built the first
  outline around the storage mechanism.
* I expected to be able to reuse the existing illustration components without
  issue, since this was a reuse-only build.
* I expected the render to be straightforward after the first video.

Where it resisted, and what I did next.

* The real misconception isn't *how* memory is stored, it's that the model has
  any memory at all. Each model call is stateless; the program re-sends the
  whole conversation every turn. That reframing changed the spine of the
  video: the point isn't "here's a database," it's "the model forgets
  everything between calls unless you engineer around it." I moved that to the
  cold open and the BLUF so the rest lands against it.
* I had to be careful not to present short-term and long-term memory as two
  features of the model. They aren't the model's — they're both things the
  surrounding program does. Short-term is what you keep in the context you
  re-send; long-term is what you save elsewhere and retrieve back in. I kept
  the narration pointing at the program, not the model.
* The coffee-order running example nearly became decoration. I kept it
  load-bearing: short-term holds the order within one chat, long-term writes
  it to a store and pulls it back next session — the same example carrying
  both halves of the distinction.

What Claude contributed, and what I accepted, changed or rejected.

* Claude built the video on the Brutalist pipeline from my beat sheet.
* I drafted the beat sheet, the teaching arc, and the narration.
* Accepted: reusing existing components rather than authoring new ones, which
  kept the render fast and avoided the portrait-composition gap.
* Accepted: searching the scene library before authoring anything.
* Changed: I reworked the cold open so the narration opens with my own intro
  ("Hi, my name is Prashanth…") and corrected the on-screen handle to
  @HumanitariansAI, per review feedback on the earlier videos.

What I understand now, and what I still do not.

* Understood: a language model call is stateless. Any sense of "memory" is the
  program's doing — short-term by re-sending the conversation (bounded by the
  context window, which drops the oldest turns once it fills), long-term by
  saving to an external store and retrieving the relevant pieces back into the
  next request. The model never remembers; the system around it does.
* Understood, and it connects to my own project: the Madison archetype detector
  will need to pull a brand's real material into context to score it — that's
  the same retrieve-into-context pattern as long-term memory.
* Not understood: where the practical ceiling sits — how retrieval quality and
  context limits trade off in a real agent under load.
