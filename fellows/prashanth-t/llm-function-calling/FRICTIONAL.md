# Frictional log — Explainer: How LLM Function Calling Works

2026-09-16 — making "How LLM Function Calling Works"

* Video / Drive: https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link

What I was working on. A ~200-second plain-language explainer on function
calling: how a model that can only produce text ends up using real tools. The
four-step loop, a running Boston-weather example, how the tool result returns as
another message, the failure modes, and the point that this same loop is what an
agent is built from. Fourteen beats, B00–BOUT, on the Brutalist pipeline. This
was the first video of the fellowship, so it also doubled as learning the
pipeline.

What I tried, and what I expected.

* I expected the hard part to be explaining the JSON — the tool schema and the
  request format.
* I expected the scene library to already have something for a request/response
  loop, since the library is large.
* I expected a clean build once the beat sheet was right.

Where it resisted, and what I did next.

* The JSON was not the hard part. The misconception is that the model *runs*
  the tool. It doesn't — it emits a request, and your program runs it. I moved
  that correction into the executive summary so every later beat lands against
  it, and made the cold open an ask that visibly answers itself through a tool
  call.
* The library search came back with no component for a four-stage round trip
  with a return leg. The closest candidates were one-directional or hardcoded
  to another reel. Per the library-first rule a genuine miss is a design card,
  not a licence to slate, so a new component was built for it and registered —
  `FnCallLoop`, which then got reused as the framework figure and again for the
  worked example.
* The first compiled cut passed its gates but was wrong. Every animation was
  truncated around half way through: the illustrations are paced against the
  composition's registered length, but each clip is cut to the measured audio,
  so a 30-second composition in a 15-second beat only ever showed half. The
  framework beat displayed two of four stages. Fixed by making length a prop so
  each composition re-times to its own beat.
* Worse, the executive-summary beat showed the *uncorrected* misconception
  while the narration spoke the corrected version — audio contradicting
  picture on the one beat that exists to frame the whole video. The cause was
  that the on-screen correction is matched one word at a time, and I had given
  it a five-word phrase, which silently matched nothing. No error, no warning.
  Rewritten so a single word carries the swap.
* The verdict page rendered an empty numbered line — a "4." with nothing after
  it — because I had used a blank string as a visual spacer in a list that
  numbers every entry.
* Being on Windows cost real time: a font path broke the video filter, console
  output crashed on non-ASCII characters, and the renderer could not find its
  own toolchain. Each needed a workaround before anything rendered at all.

What Claude contributed, and what I accepted, changed or rejected.

* I set the topic, the content targets and the teaching order; Claude drafted
  the beat sheet and narration from them and built the reel on the pipeline.
* Accepted: searching the scene library before authoring, which is what found
  the genuine gap rather than guessing at one.
* Accepted: building the missing loop component instead of falling back to a
  placeholder slate.
* Accepted: verifying the cut by actually looking at sampled frames rather than
  trusting the automated gates — that is what caught the truncated animations
  and the contradicting summary, both of which passed every gate.
* Changed: rewrote the cold open to open with my own introduction and corrected
  the on-screen handle to @HumanitariansAI, after review feedback.
* Rejected: shipping the first cut. It was watchable and gate-clean, and still
  taught the wrong thing on its most important beat.

What I understand now, and what I still do not.

* Understood: function calling is a request, not an execution. The model writes
  a tool name and arguments; my program runs the tool; the result returns as
  another message and the model runs a second time on the longer conversation.
  One question therefore costs two model turns, and the only thing I control is
  the tool description.
* Understood about the process: a build passing its gates is not evidence the
  video is correct. Both of the worst defects here were invisible to the gates
  and obvious in a single sampled frame.
* Not understood: how far the tool description can be pushed before the model
  starts mis-selecting — I state the failure modes in the video but have not
  measured where the boundary is.
