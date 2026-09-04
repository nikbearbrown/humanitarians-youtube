# What Happens Inside a Financial Chatbot

**Skill:** ai-explainer · **Voice:** af_bella (Anjana) · **Duration:** ~223s (16:9) / ~170s (9:16 short) · **Status:** rendered (both orientations, final cut + slate)
**Companion to:** `/attention-finance` and `/temperature-finance` — same NLP-internals territory, same dark-stage treatment, different single idea.
**Destination:** `anjana-s/2026-09-04-inside-a-financial-chatbot`
**Delivery:** rendered at 4K in both 16:9 (`financial-chatbot.mp4`, 3840×2160) and 9:16 (`short/financial-chatbot-short.mp4`, 2160×3840).

## About this video

You ask a financial chatbot whether a company raised guidance, and two seconds later you get an answer with three citations from real filings. It looks like the model simply knows things. It doesn't — and the gap between those two explanations is the whole video. There are four steps between the question and the answer, and the model only shows up for the third one.

Step one is that your question never reaches the language model in the form you typed it. An embedding model converts it into a 384-dimensional vector — a coordinate in what the video calls meaning space, where questions about revenue guidance land near other revenue-guidance text and questions about margin pressure land somewhere else entirely. Step two is the search, and it is not a keyword search: the question's vector is compared against thousands of stored chunk vectors, which is why "revenue guidance" in your question can match "top-line outlook" in a filing despite sharing no words at all. The top three to five chunks come back ranked by similarity, each carrying its metadata — company, quarter, section, speaker.

Only then does the model get involved, and it receives three things at once: a system instruction telling it to answer only from what it's given, the retrieved chunks as context, and your original question. It isn't recalling anything from training. It's reading documents that were fetched seconds earlier and pasted in front of it, which is exactly why it can tag every claim with a citation pointing back to the specific chunk that claim came from. The video's payoff visual is those citation lines drawing backward through the pipeline — the difference between a model that says so and a model that shows its source.

That's retrieval augmented generation, and the closing argument is the practical one: the model didn't have to guess, so its answer is anchored to a document you can go read yourself.

## File structure

```
financial-chatbot/
├── README.md, PEDAGOGY.md   — build notes and sign-off
├── script.md, beat_sheet.json, beats.json — narration script and beat config
├── narration/, visuals/     — per-beat TTS text and visual briefs
├── mp3/, clips/, media/     — narration audio and rendered per-beat video (16:9)
├── financial-chatbot-slate.mp4 — 16:9 review cut
├── financial-chatbot.mp4    — 16:9 final master (3840×2160)
└── short/                   — 9:16 derivative cut (via runtime/scripts/shorts.py)
    ├── PEDAGOGY.md           — sign-off for the derivative cut
    ├── beat_sheet.json       — aspect_ratio 9:16, beats dropped to fit the Shorts cap
    ├── mp3/, media/          — regenerated outro audio + portrait Remotion renders
    ├── financial-chatbot-short-slate.mp4 — 9:16 review cut
    └── financial-chatbot-short.mp4       — 9:16 final master (2160×3840)
```

Five body-beat illustrations (`ChatbotHook`, `ChatbotEmbed`, `ChatbotRetrieve`,
`ChatbotGenerate`, `ChatbotClose`) plus their portrait `916` counterparts are
registered in `runtime/remotion/src/Root.tsx`, under
`runtime/remotion/src/illustrations/financial-chatbot/`. `ChatbotHook` also
exports the shared `ChatFrame` used by the later beats — the chat interface
persists as a corner thumbnail through B02–B03 and returns full-size in B04,
closing the loop the reel opens with.

## Rebuilding this video

```bash
cd brutalist.art

# 16:9 (4K, 3840×2160)
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-04-inside-a-financial-chatbot
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-04-inside-a-financial-chatbot
./art final anjana-s/2026-09-04-inside-a-financial-chatbot

# 9:16 derivative (4K vertical, 2160×3840)
python3 runtime/scripts/shorts.py anjana-s/2026-09-04-inside-a-financial-chatbot
python3 runtime/scripts/generate_audio_kokoro.py anjana-s/2026-09-04-inside-a-financial-chatbot/short
python3 runtime/scripts/remotion_scenes.py anjana-s/2026-09-04-inside-a-financial-chatbot/short
./art final anjana-s/2026-09-04-inside-a-financial-chatbot/short --height 3840
```

GATE P is signed for both the parent (`PEDAGOGY.md` — `VERDICT: PASS`) and
the short derivative (`short/PEDAGOGY.md` — `VERDICT: PASS`).
