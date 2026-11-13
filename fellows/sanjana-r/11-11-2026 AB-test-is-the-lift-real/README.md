# Is The Lift Real? — explainer video

A short **Product Management** explainer made for **Sanjana**, produced with the Brutalist
video toolkit and watermarked **@HumanitariansAI**.

The film teaches the A/B-testing trap every PM hits — calling a lift a win before it's
statistically real — by building a significance check with Claude on screen: the prompt, the
real two-proportion z-test, and the **confidence intervals shrinking as the sample grows**
until the verdict flips from "not yet" to "significant." Narrated by **Liam** (local Kokoro
`am_onyx` voice).

---

## The files

| File | What it is | Use |
|---|---|---|
| `ABtest-IsTheLiftReal-16x9-4K.mp4` | 16:9 landscape master, 3840 × 2160 (4K) | YouTube main video |
| `ABtest-IsTheLiftReal-9x16-4K.mp4` | 9:16 vertical master, 2160 × 3840 (4K) | YouTube Shorts / Reels / TikTok |
| `BEATSHEET-16x9.json` | The 16:9 beat sheet (shot-by-shot script) | Source / re-edit |
| `BEATSHEET-9x16.json` | The 9:16 beat sheet | Source / re-edit |
| `PROOF-REVIEW-RESULTS.md` | Skeptical self-review of both cuts (score /12, gate, punch list) | QA record |
| `README.md` | This file | — |

- **Frame rate:** 24 fps · **Audio:** AAC stereo · **Codec:** H.264 (`yuv420p`, `+faststart`)
- On YouTube, force **2160p** in the quality menu to see true 4K.

## What's in the video

Opening line: *"Hi, this is Liam for Sanjana, and this video is about a trap every product
manager walks into — calling an A/B test a win before it's actually real."* Then:

1. **The trap** — Variant B is up 2 points (+20%); everyone wants to ship. On a small sample
   that gap can be pure noise, and shipping on noise wastes a quarter.
2. **The framework** (before the example) — whether a result is real depends on **lift +
   sample size + noise**; express it as a confidence interval; **overlapping intervals → not a
   result yet.**
3. **Pass 1 — compare** — the prompt → naive code → two bars and "+20%, ship it?" (the trap).
4. **Pass 2 — test** — revise the prompt → the real two-proportion z-test → the confidence
   intervals **shrink as n climbs**, and the verdict flips from "not significant (p=0.15, need
   ~3,835/arm)" to "significant (p=0.005)" only when the intervals separate.
5. **The method + limits** — decide the sample size before you peek; don't optional-stop; and
   significant ≠ important.
6. **Your turn** — a copy-paste prompt to run the z-test on the viewer's own experiment.

Every statistic on screen is **real** — computed by `../src/abtest.py` (run
`python3 -I abtest.py` in `src/` to reproduce the p-values, CIs, and required sample size).

## Branding

- **@HumanitariansAI** in the intro composer, as a low-opacity corner watermark throughout,
  and on the closing title card.
- Visual style: the Claude desktop-app palette (cream, warm ink, one terracotta accent — here
  the variant bar and the "not significant yet" warning).

## Source & reproduction

- `../beat_sheet.json` — the shot-by-shot script
- `../src/abtest.py` — the real z-test / CI / sample-size code (the on-screen numbers)
- `../FACTCHECK.md`, `../SOURCES.md`, `../SHOTLIST.md` — claims, references, shot list
- `../vertical/` — the 9:16 companion's own beat sheet

Credits: two-proportion z-test, confidence intervals, and power/sample-size formulas —
standard inferential statistics.
