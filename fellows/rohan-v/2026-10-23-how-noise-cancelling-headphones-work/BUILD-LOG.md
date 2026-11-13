# BUILD-LOG — "How Noise-Cancelling Headphones Work"

What broke, what it cost, and what changed because of it. Built 2026-10-23 for the week of 19–23 Oct. The
toolkit update (4 upstream commits, clean merge) is logged in the key reel's BUILD-LOG §1.

## 1 — A simulation, and saying so

There is no headphone to measure, so `anc.py` simulates one: a feedforward filtered-x LMS controller at 48 kHz
with an 83 µs acoustic lead and 125 µs of electronic latency. Every number in the video is that model's, and the
narration says "my simulated headphone". The fact-check also found that many commercial headphones use fixed,
pre-tuned filters, so B02 was rewritten: "Many headphones also have a microphone inside… My simulated one uses
it to keep adjusting its filter."

## 2 — Sanity checks on the run

- **The phase rule is checked twice**: computed (2·sin(φ/2)) and simulated with a late copy; they agree to 0.1 dB
  at every frequency tested.
- **Rumble cancels better than the hum** (−31.4 vs −25.5 dB). Checked rather than assumed: band-limited rumble
  below 300 Hz is very predictable over the 2-sample latency gap; the hum is still adapting (its 50-ms trace is
  −23 dB at 2 s and settles lower).
- **Voices at −11 dB** in my model is more than real headphones manage on speech; the model has a perfect
  secondary-path estimate and no acoustic leakage. The video only claims the order (hum and rumble far more
  than voices, clatter not at all) and says it is a simulation.
- **Above 4 kHz it gets slightly louder** (+0.5 to +2.3 dB): the filter trades high-frequency error for low.

## 3 — One clip, one gain

`mix_listen.py` levels each listening clip to the narration's loudness. Levelled separately, the "ANC on" half
would have been raised 25 dB to match "off", hiding the result. The off/on clip is one file with one gain.

## 4 — Layouts and gates on probe stills (before any render)

- **Phone titles wrapped** ("Late Hurts High Pitch", "Get the Most From It"): shortened.
- **B01's residual line drew too late** (it finished after the beat's last word): it now draws with "the
  anti-noise my simulated headphone made".
- **B02's phone boxes were too narrow for their labels** ("OUTSIDE MIC" ran out of its box): "MIC OUT" /
  "MIC IN" on the phone, wider boxes; the noise lines no longer touch the outside mic.
- **B05's "cups" label collided with the stats**: moved inside the shaded band, with a legend under the chart.
- **Gate V edge-bleed**: B04's landscape chip and B03's phone legend ran past the right edge; the chip was
  shortened, and the phone legend became one short row ("LEFT" for "LEFT OVER") below the 2 kHz result.
- **GATE T §8.1 on the phone**: the italic spark lines' x-height ("ncel", "hum") measured 66 px; phone spark
  lines are 1.25× larger (and `HaiApplyCard`'s via `sparkScale`).

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/NoiseCancelling_RohanV.mp4` | 3840×2160 | 142.50 s | `354c809f00b37c6867bcf9eaae191a8472b44044783c8f6cc24f7450d6b36353` |
| 9:16 | `vertical/NoiseCancelling_RohanV.mp4` | 2160×3840 | 142.50 s | `df0b440f0e51acf2a5f29c647ba812ae43f58bdf8bf9960e3d7dac9028a87851` |

Gates on the accepted finals: GATE F pass; GATE T pass, 0 FAILs ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(16 landscape and 16 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png).

Portrait: accepted on the first final. Landscape: the first final was refused by Gate V (B04 underfilled at mid-beat, 41%: the right column was empty until the chips arrived); B04 got taller bars and ghost chips, was re-rendered, and the second final passed. All on 2026-10-23.

Uploaded to Google Drive `2026-10-23/landscape/` and `2026-10-23/vertical/`; md5 of each Drive copy
matches the local master.
