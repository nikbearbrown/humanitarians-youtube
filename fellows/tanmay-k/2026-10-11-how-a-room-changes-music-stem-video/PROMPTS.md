# PROMPTS

No AI-image, AI-video or CLI-explainer beats in this project, and so no prompts to record.

- **Pictures:** every beat is a Remotion scene drawn in code (`RoomVoiceOFL`, `HallTempoOFL`,
  `AskAnswerOFL`, `ClaudeArtifactCardFullOFL`, `ClaudeTitleOutroFullOFL`, and the Short's 916 variants).
  Its content is written into `shot.remotion.props` by `build_beat_sheet.py` / `short/build_short_sheet.py`.
- **Waveforms:** the RoomVoice envelopes are measured from our own DEMO audio (`envelopes/*.json`,
  written by `room_voice.py`), never drawn by hand.
- **Narration:** Kokoro TTS (`am_onyx`, local), voicing the Gate P-signed scripts (`PEDAGOGY.md`),
  with the signed pronunciation overrides (`make_audio.py`).
- **The cathedral:** a synthetic impulse response we generated (`make_ir.py`, seeded, measured T30 4.7 s).
  No third-party recording is used. A measured York Minster IR was cut on licence grounds
  (FACTCHECK §C).
