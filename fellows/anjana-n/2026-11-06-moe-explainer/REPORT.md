# Video Report: Mixture of Experts — Sparse Activation, Massive Capacity

**Type:** STEM Video

**Week:** Week 19, November 1 – 7, 2026

---

## Summary
Mixture of Experts (MoE) replaces one large feed-forward network with several smaller experts and a router. For each word, the router picks only a few experts, so the model can be very large while only a fraction of it runs at a time.

---

## Main Ideas
- **More capacity at the same cost per word:** eight experts of 6.5B each make 52B in total, but with two active, only 13B runs for each word.
- **Balance needs managing:** without a fix, a few experts end up doing most of the work.
- **A model's name is not its size:** "8×22B" is 141B, not 176B, because only the feed-forward parts are copied.
- **It works in practice:** a 141B model with 39B active can match a 70B standard model at roughly half the processing cost.

---

## Links
- **GitHub:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-06-moe-explainer
- **Drive:** https://drive.google.com/drive/folders/1uyryieZQ6wX4oC7eCjpFrt3nNW86yCSc

---

## Status
Complete
