# FRICTIONAL — Hedging When Trading Isn't Free

_Drafted by Claude (Claude Code) from the build session; Boopesh to read, correct and add his own entries._

## 2026-10-24
- **Tried:** run the PyTorch experiment. **Found:** `pip install torch` pulled multi-GB CUDA wheels and did not
  finish in the build container. **Did:** ported the same experiment to numpy with hand-written backprop through
  time, checked against finite differences (worst relative error 3.8e-7). PyTorch draft kept, marked "not run".
- **Tried:** read the paper. **Found:** arXiv and publisher sites blocked. **Did:** used the first author's code
  README as the primary source; claims only found in abstract summaries are flagged ⚠️ in FACTCHECK.md.
- **Resisted:** the draft line said the deep hedge "holds still, then moves". The plotted test path shows it
  moving smoothly every day, just with smaller steps. Changed to "moves more smoothly, skips the small back-and-forth".
- **Resisted:** the result is not a clean win: the deep hedge's P&L spread is wider ($0.75 vs $0.57). The film says so;
  it wins on average, on the worst 5 %, and on the utility it was trained for.
- **Resisted:** with zero fees the network is close to, but slightly worse than, Black–Scholes (−0.127 vs −0.096).
  Said "nearly", not "exactly".
- **Resisted:** first layouts collided with the header and overflowed the safe area; the Short's end card
  underfilled the frame. Fixed by looking at frames and the fill check.
- **AI contribution:** Claude wrote the code port, script, sheets and scenes. Kokoro `am_onyx` speaks the narration.
- **Still open:** paper-only claims (S&P 500 + Heston tests, affiliations) need a check against the PDF; name
  pronunciation (Buehler, Gonon, Teichmann) set by phonemes, needs a human listen.

---

## 2026-11-24 — Submission note for the week of Oct 18–24 (written later than the week it describes)

**Record provenance:** added on 2026-11-24 by Claude (Claude Code) at Boopesh's request, when this folder was
first committed. The entries above were drafted during the build, in the week of the work.

- **Why this commit is late:** the films and this source were delivered in the week of Oct 18–24. They could not
  be committed then: Boopesh's fork of the repository failed, and push access only arrived on 2026-11-24.
  This folder is restored unchanged from the source archive delivered that week.
- **Who did what:** Boopesh gave the prompts and instructions for the week (the topic direction, and
  the voice approval on 2026-10-24) and reviewed the delivered videos and code. Claude did the research,
  code, scenes, narration script and rendering.
- **Still open:** the Drive link for each film goes in this folder's README; Boopesh to add any notes of
  his own on what he checked, changed or rejected.
