# Playlist Architecture as Product Strategy — @HumanitariansAI

A Humanitarians AI fellow reel by **Sanjana Rao**, built with the `brutalist.art`
toolkit (Claude fidelity skin, Kokoro `af_bella` voice — free, local; Remotion 4K).
Nothing here is published to YouTube — these are review masters for you to post.

## Deliverables

| File | Format | Use |
|---|---|---|
| `playlist-architecture/playlist-architecture.mp4` | 16:9 · 3840×2160 (4K) | The main YouTube video (~3:45) |
| `playlist-architecture-short/playlist-architecture-short.mp4` | 9:16 · 1080×1920 | The YouTube Short (~1:20) |
| `PROMPT.md` | — | The copyable Claude clustering prompt (the "Your Turn" scaffold) |
| `SOURCE-brief.md` | — | The original brief this was built from |

Each reel folder also holds `beat_sheet.json` (the editable script + timing),
`mp3/` (per-beat narration), `media/` (per-beat rendered clips), and `clips/`
(conformed timeline + `qc-sheet.png`).

## What's in the cut

Cold open (Claude composer) → executive summary → **the hook** ("playlists aren't
folders") → **the reframe** (folder vs product) → **the framework** (3 questions) →
AI-as-co-strategist header → **3 methods** (cluster / journey-map / gap-analysis) →
**worked example** (one library → two products) → takeaway → **Your Turn** handoff →
title outro. Every beat carries the `@HumanitariansAI` bug and one terracotta accent.

## Built from your REAL playlists

Per your screenshot, the concrete scenes use the channel's actual playlists:

- **Clustering** re-groups the real playlists by *viewer intent*:
  - *For beginners* — React · Lyrical Literacy · 80 Days to Stay · Claude
  - *For practitioners* — Mycroft Financial AI · NeuroVEP · RAMAN Effect · Popper
  - *For decision-makers* — HAI Fellows · Madison · Medhavy · HAI
- **Reframe** shows the current "folder" instinct — filing by project (Mycroft,
  NeuroVEP, RAMAN) — vs an intent-based product journey.
- **Gap analysis** contrasts what you HAVE (HAI 141, Fellows 32, Mycroft 20) with the
  three products hiding inside them that you're MISSING (HAI Tools That Shipped ·
  Learn AI for Good · AI Explained).
- **Worked example** splits the 141-video `HAI` pile into its three real content
  types — **HAI Tools That Shipped · Learning Topics · Explainer Videos** — one
  library, three products, each for a different viewer.

> These clusters and "missing" playlists are *proposals* (the point of the video),
> not claims about what's inside each playlist. Rename them to taste in the beat sheet.

## Self-review (PROOF)

`FEEDBACK.md` holds the skeptical self-assessment: **clear-for-public, teaching 11/12,
production gate PASS**. The one soft spot (falsifiability) and a couple of optional
[EDIT] polishes are noted there.

## Re-render / edit

Edit narration or on-screen text in `beat_sheet.json`, then (from the toolkit root,
using `python`, since `python3` is a broken shim on this machine):

```bash
python runtime/scripts/generate_audio_kokoro.py "<reel folder>"        # re-voice
python runtime/scripts/remotion_scenes.py "<reel folder>" --force      # re-render beats
python runtime/scripts/compile.py "<reel folder>" --height 2160        # 4K master (use 1920 for the Short)
```

Scene components live in `runtime/remotion/src/scenes/PlaylistArchitecture.tsx`
(registered in `Root.tsx`). They are responsive — one component backs both the 16:9
and 9:16 cuts.
