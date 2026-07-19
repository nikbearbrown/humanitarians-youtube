# PEDAGOGY — claude-liam-radio-eats-battery

## What the learner already knows
- Embedded AI systems run inference on sensor nodes
- Battery life depends on total power consumption
- Optimizing the model should help battery life

## What this reel teaches
Radio transmission dominates the energy budget of most IoT sensor nodes. One LoRa TX (38 mA × 100 ms = 3.5 mA·s) costs 10× one inference (15 mA × 22 ms = 0.33 mA·s). Weeks of model optimization move the needle less than reducing transmit frequency. The oscilloscope trace makes the dominance visible.

## Act structure
- B00 COLD OPEN: hook — weeks of model optimization, battery life barely moved
- B01 SLEEP FLOOR: sleep current baseline (~5 µA) — the floor
- B02 INFERENCE BURST: 15 mA × 22 ms spike — small, narrow, 0.33 mA·s
- B03 RADIO ENVELOPE: 38 mA × 100 ms — tall, wide, dominant, terracotta
- B04 ENERGY COMPARISON: daily budget bar chart — radio wins at 100 tx/day
- B05 YOUR TURN: ClaudeComposerAsk with IoT energy budget prompt
- B06 OUTRO: ClaudeTitleOutro

## Pedagogy checklist
- Problem stated before data (hook before traces) ✓
- Root cause named: transmit schedule, not model size ✓
- Mechanism animated: oscilloscope-style trace with growing components ✓
- Concrete numbers: 10× ratio per event, daily budget comparison ✓
- No technical term before the beat that created the need for it ✓
- Your Turn prompt is concrete and actionable ✓
- Length: ~96s estimated < 3:00 ✓

VERDICT: PASS
