# Backpropagation, One Error at a Time

- **Status:** final — delivered (4K master, gates passed)
- **Series:** STEM AI explainer series · Film 2 (sequel to *Gradient Descent, One Step at a Time*)
- **Channel:** @NikBearBrown (claude-liam brand) · **Voice:** Kokoro `am_onyx` (Liam, in for Bear) · **Greeting:** "Hola, Liam"
- **Long:** 3840×2160 · 3:17 · 11 beats — `claude-liam-backpropagation.mp4`
- **Last updated:** 2026-11-22

## Subject

How a network gets the slope for every weight at once. A four-step network (z = w₁x, h = tanh z, y = w₂h, L = (y − t)²) is run forward and then backward on executed numbers: the chain rule multiplies local slopes to ∂L/∂w₁ = 2.2783, a finite-difference check agrees to 8 decimal places, and ten sigmoid layers show the gradient shrinking to 3.483e-7 by the first layer.

## Notes

- ai-explainer format from the start: cold open in the Claude composer → hesitant-writer summary → six Manim scenes → Verdict recap → Your Turn → title outro.
- Every on-screen number is read from `demo/evidence.json`, written by `demo/bp_demo.py`.
- Kokoro read "tanh" as "tan", and whisper heard "backpropagation" as "back repugation"; both are pinned in `metadata.pronounce`.
- Known cosmetic issue, not fixed: the locked `ClaudeTitleOutro` wraps the title as "…at a / Time.", as in film 1.
