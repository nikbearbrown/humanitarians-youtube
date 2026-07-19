# Pedagogy audit — cli-distill

## Structure check
- B00 INTRO: brand open
- B01 PROBLEM: stakes before CLI -- one-hot label discards signal; teacher soft distribution carries relative mistakes; hard label throws away the 5% dog signal
- B02 ASK: terminal command for distill_demo.py
- B03 CODE: temperature divides logits, mixed loss controls trade-off
- B04 OUTPUT: 10-class bar chart, temperature sweep T=1 to T=3 to T=6 showing wrong-class signal emerging
- B05 CHANGE: pair with pruning, distill pruned student against float teacher
- B06 OUTPUT (revised): two accuracy bars, distilled student +3% over hard label
- B07 SUMMARY: hard labels discard dark knowledge; soft labels transfer it
- B08 NEXT STEPS: sweep T on your teacher logits, run distillation training
- B09 OUTRO: brand close

## Voice check
- No forbidden phrases
- Problem stated first (B01) before CLI
- Concrete numbers: 85% cat, 5% dog, T=1/3/6, +3% accuracy gain, 10 classes
- Honest about what requires real training ("2-5% only if you actually train")

## CLI loop check
- At least one revision: YES (B05 CHANGE -> B06 revised output)
- SUMMARY and NEXT STEPS present: YES

VERDICT: PASS
