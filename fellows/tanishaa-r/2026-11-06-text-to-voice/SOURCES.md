# SOURCES — How a Computer Turns Text into a Voice

- demo/tts_demo.py → demo/tts_output.json and demo/*.wav: real Kokoro-82M v1.0 output (kokoro-onnx 0.6.1, espeak-ng phonemizer) on four sentences in af_bella and am_michael, with faster-whisper transcripts.
- brutalist.art/runtime/scripts/generate_audio_kokoro.py: the engine and model files that narrate the video.
- General TTS pipeline (text normalization, grapheme-to-phoneme, prosody, waveform generation): standard description; Kokoro is built on the StyleTTS 2 / iSTFTNet design.
