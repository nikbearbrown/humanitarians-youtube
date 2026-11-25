# Why Neural Networks Need a Bend

- **Status:** final — delivered (4K master, gates passed)
- **Series:** STEM AI explainer series · ai-explainer format
- **Channel:** @NikBearBrown (claude-liam) · **Voice:** Kokoro `am_onyx` (Liam, in for Bear) · **Greeting:** "Jambo, Liam"
- **Long:** 3840×2160 · 4:12 · 14 beats — `claude-liam-nonlinearity.mp4`
- **Last updated:** 2026-11-23

## Subject

Why every neural network puts a bend between its layers. Two straight layers multiply out to one matrix, ten layers do the same, and no straight map can solve XOR; one ReLU bend with two hidden units solves it exactly. The film then tests the claim: trained from 100 seeds the bend finds XOR 18 times (91 with eight units), and a ReLU network is made of straight pieces.

## Notes

- Built in the ai-explainer format from the start: cold open in the Claude composer, hesitant-writer summary, nine Manim scenes, verdict recap, Your Turn, title outro.
- Every on-screen number comes from `demo/nonlinearity_demo.py` (pure Python + numpy, about 60 s); the collapse matrices use seed 0.
- Four words are pinned in IPA for Kokoro: ReLU, XOR, numpy, Jambo.
- The B02 bottom strip (`x → W₁ → bend → W₂ → y`) was removed at my request; the word "bend" is boxed in ink instead.
