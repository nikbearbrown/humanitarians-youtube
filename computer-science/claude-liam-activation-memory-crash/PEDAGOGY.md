# PEDAGOGY — claude-liam-activation-memory-crash

## What the learner already knows
- Embedded devices have limited RAM and flash
- Model size is measured in parameters or bytes
- The model "fitting" is a go/no-go decision before flashing

## What this reel teaches
The distinction between parameter count (storage) and activation peak (runtime RAM constraint). The learner sees why naive parameter math misleads, how buffer pileup creates crashes, how buffer reuse collapses peak, and what flash vs SRAM split means for architecture.

## Act structure
- B00 COLD OPEN: hook — 180 KB model in 256 KB SRAM, crashes at 40 ms
- B01 NAIVE COUNT: 180 KB in flash, activations in SRAM — "it fits" annotation
- B02 NAIVE ALLOCATION: layer buffers pile up, peak 150 KB — crash
- B03 BUFFER REUSE: only live tensors occupy RAM, peak drops to 60 KB — runs
- B04 FLASH vs SRAM SPLIT: architectural lesson — weights safe in flash, activations constrained in SRAM
- B05 YOUR TURN: ClaudeComposerAsk with layer-sizes prompt
- B06 OUTRO: ClaudeTitleOutro

## Pedagogy checklist
- Problem stated before solution (B01-B02 before B03) ✓
- Root cause named: peak activation RAM, not parameter count ✓
- Mechanism animated: buffer pileup vs reuse comparison ✓
- Concrete numbers: 150 KB naive vs 60 KB reuse ✓
- No technical term before the beat that created the need for it ✓
- Your Turn prompt is concrete and actionable ✓
- Length: ~89s estimated < 3:00 ✓

VERDICT: PASS
