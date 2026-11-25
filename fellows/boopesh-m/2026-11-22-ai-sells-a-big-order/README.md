# How an AI Sells a Big Order

**Boopesh M. · Humanitarians AI Fellow · Brutalist team** · weekly STEM explainer (AI in finance) · 2026-11-22
Narration: AI voice (Kokoro `am_onyx`) · 16:9 3840×2160 + native 9:16 2160×3840 Short

**Status: rendered and verified.** The 16:9 runs 2:12.9 and the Short 0:46.3. Both passed `./art final`
(GATE T, then the final frame check). Delivery files are normalized to −14.1 LUFS with a −1.0 dBTP true peak.

## What it is
Selling 10,000 shares at once pushes the price against you (market impact). Selling slowly lets
the price drift while you wait. A tabular Q-learning agent, trained in a **synthetic market**,
learns how to split the order over 10 time steps. It lands close to the Almgren & Chriss
closed-form schedule. One idea: impact versus risk.

## Key numbers (code/results.json, synthetic market, 20,000 held-out simulated days)
| Strategy | Avg cost | Spread (std) | Bad day (95th pct) |
|---|---|---|---|
| All at once | 100.0 bps ($5,000) | 0 | 100.0 bps |
| Equal slices (TWAP) | 9.9 bps | 33.7 bps | 65.4 bps |
| Q-learning agent | 13.3 bps | 24.5 bps | 53.6 bps |
| Almgren–Chriss closed form | 13.2 bps | 24.1 bps | 52.7 bps |

Learned schedule: 2500 · 1500 · 1000 · 1000 · 1000 · 750 · 750 · 500 · 500 · 500 shares.
Cost + risk penalty: agent 22.42 bps vs closed form 22.05 bps (+1.7%), TWAP 27.10, dump 100.
40,000,000 practice runs. The code was run twice with identical output (`code/determinism.txt`).

## Watch and review
| File | Link | Duration | SHA-256 |
|---|---|---|---|
| 16:9 master `landscape/ai-sells-a-big-order-master.mp4` (+ `.verified.json`) | (Drive link: TBD) | 132.92 s | `ddd243f334269ecc87008d039debaa6cc26574a5a160cec77d8dc9fa3171ceac` |
| 16:9 delivery `landscape/AISellsABigOrder_BoopeshM.mp4` (−14.1 LUFS, TP −1.0) | (Drive link: TBD) | 133.00 s | `87a45baa0dd5633cbb7c88fd4e935e8acc668590e3af1f77553b5fdf7a3a2cec` |
| 9:16 master `vertical/ai-sells-a-big-order-short-master.mp4` (+ `.verified.json`) | (Drive link: TBD) | 46.25 s | `cf0282bb3456f946b6926a438aa30ad2bde6e28ff127a829f611fcae7af78652` |
| 9:16 delivery `vertical/AISellsABigOrder_BoopeshM.mp4` (−14.1 LUFS, TP −1.0) | (Drive link: TBD) | 46.30 s | `78e15fd0e6cb7a4e24726fa66c13dbd60becb661322a027bc9d29e7c4e3e9a44` |

The files live in `/home/user/weekly-submission/`. The delivery files carry the master's video stream unchanged
(stream copy) and a two-pass `loudnorm` audio track (I −14, TP −1, LRA 11, linear requested; ffmpeg used
dynamic mode because +10 dB of linear gain would have pushed the true peak past −1), AAC 320k, faststart.

## How to rebuild
```bash
export PATH=/opt/brut/bin:$PATH
python3 code/execution_rl.py            # ~100 s; writes code/results.json + code/run.log
python3 code/make_formula.py; python3 make_sheet.py
# metadata.approvals.voice holds Boopesh's human approval of am_onyx (make_sheet.py keeps it)
cd /home/user/nikbearbrown/brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py <reel>; python3 <reel>/make_sheet.py   # durations -> props
python3 runtime/scripts/remotion_scenes.py <reel> --only B00   # then B10, B80 (Short: B00)
./art run <reel>; python3 runtime/scripts/type_check.py <reel>
./art final <reel> --height 2160 --out /home/user/weekly-submission/landscape
```
The same steps apply to `<reel>/short` (with `--height 3840`, output to `vertical/`).

Files: `beat_sheet.json`, `scenes.py`, `make_sheet.py`, `code/`, `assets/`, `short/`, FACTCHECK.md,
SHOTLIST.md, PROMPTS.md, PROOF.md, FRICTIONAL.md, BUILD-LOG.md, description.txt.
