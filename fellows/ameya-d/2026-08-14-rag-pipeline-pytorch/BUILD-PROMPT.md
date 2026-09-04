# BUILD-PROMPT — rag-pdf-pytorch

cli-explainer: build a RAG pipeline in PyTorch that answers questions from a PDF
and cites the page.

Channel: @HumanitariansAI. Persona: Liam, in for Ameya. Voice: Kokoro am_onyx
(Onyx). 3840×2160 4K. Free pipeline only — no ElevenLabs, no publishing.

Spine (cli-explainer, required revision cycle): B00 INTRO → B01 PROBLEM → [c1]
B02 ASK → B03 CODE (real embed) → B04 OUTPUT (Manim embed) → [c2/revision] B05
CHANGE → B06 CODE (real retrieve) → B07 OUTPUT (Manim retrieve) → B08 SUMMARY →
B09 NEXT STEPS → B10 OUTRO.

ACTUAL-CODE LAW: B03/B06 show real PyTorch (sentence-transformers `model.encode`
→ tensor; `torch.nn.functional.normalize`; `q @ emb.T`; `torch.topk`; grounded
prompt). Verified in FACTCHECK.md. 2D vector space is a captioned simplification.

Manim: B04_Embed, B07_Retrieve (scenes.py). B00/B02/B05/B09 = ClaudeComposerAsk;
B03/B06 = ClaudeCodeBeat; B10 = ClaudeTitleOutro.

## Rebuild (from this folder, with the brutalist.art toolkit on hand)
```
python3 runtime/scripts/generate_audio_kokoro.py <this-reel>     # Kokoro narration (free)
# render Manim scenes at 4K (-r 3840,2160) -> manim/<BID>.mp4
# render Remotion beats -> media/<BID>.mp4
python3 runtime/scripts/compile.py <this-reel> --height 2160     # 4K master
```
Rendered media is gitignored; it regenerates from `beat_sheet.json` + `scenes.py`.
