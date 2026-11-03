# Production Log

## User authorization

Deepa explicitly stated: “I approve the complete planning packet for Video 1.” She authorized narration, scenes, both aspect renders and QC, with stops only at mandatory human gates; no upload/publication. This records actual conversation evidence. It is not an agent signature on behalf of a human.

## Scope and identity

AI Explainer on claude-hai, not the fellows source-report wrapper. No source report and no Professor Bear notes exist; their specialized approval gates do not apply. Narration remains the approved script verbatim. Kokoro am_onyx implements the approved Liam identity. HAI channel, Deepa credit and Liam narrating for Deepa remain locked.

## Next mandatory gate

skills/make/explainer/SKILL.md, Workflow step 3: “audio — Kokoro per beat (free, local), measure, lock. GATE: hear it.” The heading says each gate is the user's. Generate the full narration and provide a listenable review file before stopping. Audio approval remains pending; do not treat plan approval as listening approval. No visual production or rendering before this gate.

## Beat sheet

Created beat_sheet.json with nine approved narration beats extracted directly from SHOTLIST.md. All scene implementation is explicitly pending. This sheet is usable for narration generation, not declared render-ready. B01 records its required 0.8-second lead silence, which must be incorporated into measured audio because the supplied generator does not implement that field itself.

## Environment

Bundled Kokoro model and voices are present. The workspace .venv imports kokoro_onnx successfully. This directory has no Git HEAD; no version provenance is invented. Production is continuing in the approved planning folder; no external destination or account used.

## Audio generation and checks

- Generated all nine narration MP3s with the repository generate_audio_kokoro.py and bundled Kokoro assets; no paid calls or installation.
- Initial attempt found no ffmpeg on PATH. Retried using Remotion's bundled executables; supplying their DYLD_LIBRARY_PATH resolved the dynamic-library lookup. The successful generator completed with exit code 0.
- Bundled FFmpeg omits volumedetect and raw s16le output. Used supported WAV decoding and Python PCM measurements instead; did not claim unavailable LUFS checks.
- prepare_audio_review.py applied B01's 0.8-second lead once, remeasured all audio, and joined decoded PCM into the review WAV.
- Full narration review: 98.315 seconds. Nine clips and review WAV decode; non-silence and sample-peak checks pass. Human auditory review remains PENDING.
- Stopped before visual implementation/rendering at the mandatory hear-it gate. See AUDIO-REVIEW.md. No final MP4 or video QC result exists.

## Audio approved; visual production
Deepa explicitly approved voice, pronunciation and pacing after listening to the complete review. No regeneration of spoken text. All nine beats aligned with faster-whisper; zero fallback beats. Installed FFmpeg with tool approval. Implemented DeepaAccuracy/DeepaAccuracy916 with native layouts and reused ClaudeComposerAsk and BrutalistHesitantWriter. The writer performs a word-level correction (reveals → can hide), preserving the approved final message; its component cannot replace a multiword trigger. Vertical has independent media/audio files.
