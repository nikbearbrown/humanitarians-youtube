# BUILD-PROMPT — leverage-cuts-both-ways

ai-explainer (short) of Chapter 6 — Margin & Short Selling — from
*Computational Finance with Excel, Python, and LLMs* (Nik Bear Brown).

Channel: @HumanitariansAI. Persona: Liam, in for Ameya. Voice: Kokoro am_onyx
(Onyx). 3840×2160 4K. Free pipeline only — no ElevenLabs, no publishing.

Spine (ai-explainer / ILLUSTRATE LAW): B00 cold-open composer (ask answered) →
B01–B05 concept-illustrated Manim body → B06 HANDOFF ("Your turn.") → B07
ClaudeTitleOutro. The Claude UI appears only at B00, B06, B07; the body
illustrates the concept directly.

DOUBLE-CHECK (all from Ch.6 cheat sheet; verified in FACTCHECK.md):
Reg T 50% → $10k cash controls $20k (2:1). −20% stock → equity −40% ($10k→$6k),
margin 37.5%. Maintenance 30% → margin call at $14,286 value. Long loss capped
at −100%; short loss unbounded (short squeeze). Short margin-call PRICE withheld
(source self-inconsistent).

Manim: B01_Leverage, B02_CutsBothWays, B03_MarginCall, B04_ShortSqueeze,
B05_Verdict (scenes.py). B00/B06 = ClaudeComposerAsk; B07 = ClaudeTitleOutro.

## Rebuild (from this folder, with the brutalist.art toolkit on hand)
```
python3 runtime/scripts/generate_audio_kokoro.py <this-reel>     # Kokoro narration (free)
# render Manim scenes at 4K (-r 3840,2160) into manim/<BID>.mp4
# render Remotion beats (ClaudeComposerAsk / ClaudeTitleOutro) into media/<BID>.mp4
python3 runtime/scripts/compile.py <this-reel> --height 2160     # 4K master
```
Rendered media (`media/`, `mp3/`, `manim/`, the `.mp4`) is gitignored; it
regenerates from `beat_sheet.json` + `scenes.py` for $0.00.
