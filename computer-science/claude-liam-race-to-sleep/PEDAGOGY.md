# PEDAGOGY — claude-liam-race-to-sleep

## What the learner already knows
- Higher clock = more power consumption
- Battery life depends on current draw
- Inference takes time on embedded devices

## What this reel teaches
Energy is area under the current-vs-time curve, not peak current. A taller but narrower active burst can have less total area than a shorter but wider one, because sleep current is three orders of magnitude lower than active. The "race to sleep" principle: finishing fast and dropping to deep sleep saves energy even at higher active current.

## Act structure
- B00 COLD OPEN: hook — 75% more current, longer battery life
- B01 SLOW CLOCK TRACE: 8 mA × 22 ms pulse, shaded area = 0.176 mA·s
- B02 FAST CLOCK TRACE: 14 mA × 11 ms pulse, shaded area = 0.154 mA·s — 12% less
- B03 RACE TO SLEEP: fast finishes at t=11, drops to µA; slow still active — the mechanism
- B04 YOUR TURN: ClaudeComposerAsk with crossover analysis prompt
- B05 OUTRO: ClaudeTitleOutro

## Pedagogy checklist
- Problem stated before explanation (hook before traces) ✓
- Root cause named: energy = area; sleep current negligible ✓
- Mechanism animated: current-vs-time traces with shaded area ✓
- Concrete numbers: 0.176 vs 0.154 mA·s, 12% savings, 5 µA sleep ✓
- No technical term before the beat that created the need for it ✓
- Your Turn prompt is concrete and actionable ✓
- Length: ~74s estimated < 3:00 ✓

VERDICT: PASS
