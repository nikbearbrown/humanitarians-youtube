# PEDAGOGY — claude-liam-lstm-ops

## What the learner already knows
- LSTMs and CNNs are two model architectures
- Smaller model = fewer parameters (common mental model)
- Latency matters on embedded devices

## What this reel teaches
The distinction between parameter count (storage) and operation count (compute time). The key insight: LSTM runs full computation per time step, so sequence length multiplies ops. 14M MACs/step × 100 steps = 1.4B vs CNN's 17M total. The 82× difference is not about size — it's about the recurrent loop.

## Act structure
- B00 COLD OPEN: hook — LSTM fewer params, 80× slower
- B01 CNN SINGLE PASS: 17M MACs, done, flat counter
- B02 LSTM ACCUMULATE: time-step boxes unfold, counter climbs × 100
- B03 INVERSION: params bar (LSTM smaller) vs ops bar (LSTM 82×) — surprise revealed
- B04 YOUR TURN: ClaudeComposerAsk with architecture comparison prompt
- B05 OUTRO: ClaudeTitleOutro

## Pedagogy checklist
- Problem stated before explanation (B00 hook before B01-B03) ✓
- Root cause named: recurrent loop multiplies total ops ✓
- Mechanism animated: accumulating counter vs flat counter ✓
- Key numbers concrete: 82× ops ratio, 7× params reversed ✓
- No technical term before the beat that created the need for it ✓
- Your Turn prompt is concrete and actionable ✓
- Length: ~77s estimated < 3:00 ✓

VERDICT: PASS
