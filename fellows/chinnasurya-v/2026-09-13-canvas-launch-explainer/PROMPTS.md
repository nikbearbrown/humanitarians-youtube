# PROMPTS — How a Canvas Launch Works

No generative-image or generative-video prompts were used, and no AI-generated
footage appears in this reel.

Every frame is drawn deterministically by `scenes/render_scenes.py` using Pillow,
rendered natively at 3840x2160 and encoded at 24 fps. Narration is synthesised
locally with Kokoro (`am_onyx`) from the operator's approved script text; no
narration was written or paraphrased by the renderer.

All beats are tagged `shot.source: "own"`. No archive or AI-sourced media is
slotted, so no desaturation treatment applies.
