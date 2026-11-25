# PROMPT — "How Spatial Audio Works"

The brief, and how each constraint was resolved.

## Constraints given

Rohan, for the week of 9–13 Nov: two STEM explainers, this one audio-related, the other on how Netflix streams.
He asked for an audio topic and chose how spatial audio works, the AirPods kind. He chose HyperFrames for both of
the week's videos, then asked for three.js and

> beautiful motion designs

Hours for the week: 20, across both videos (Rohan's figure, given 2026-11-09). Built 9–10 Nov.

## How each constraint was resolved

| Constraint | Resolution |
|---|---|
| A STEM topic, audio-related | how two ears find a sound (timing, the head's shadow, the outer ear), the filters that rebuild it (HRTFs), head tracking, personalisation |
| Required opening line, AI disclosure | B00, verbatim; disclosure on screen |
| Executable evidence | `spatial.py` renders sound through a textbook spherical head and measures timing, loudness and front/back; every measured number in B01–B03 is the run's; B04 plays the run's own clip, with the outer-ear cue on its behind half |
| Apple's method is unpublished | the run is labelled "my model" / "my head model"; Apple is credited only with what it has said (head tracking, 2020; Personalized Spatial Audio, iOS 16); the docs never say Apple uses HRTFs |
| HyperFrames for both videos | B01–B06 are HyperFrames compositions; B00, B07, B08 stay on the channel's Remotion cards |
| three.js, beautiful motion | Claude recommended three.js for the 3D stage with the HUD kept in HTML; Rohan approved downloading three.js 0.187.0 (MIT), vendored in `week-12/_vendor` and shipped in `hyperframes/assets/` with its licence; the "listening room at night" look (PROMPTS) |
| A listening clip people can actually hear | `mix_listen.py` appends `circle.wav` to B04's narration in stereo at 48 kHz; the description and B04 say to wear headphones |
| No person drawn | the listener is the textbook sphere with two ears and a nose; ears in B06 are point clouds |
| Western test material (standing preference for STEM evidence) | a plucked-string melody on an A minor pentatonic line, made in `spatial.py` |
| Nothing on C: (standing rule) | HyperFrames' temporary frames go to `D:/Rohan/Claude/HyperFrames/tmp` (`hfkit.py`) |
| Typeset math | none on screen: numbers only; the formulas are in FACTCHECK |
| 4K, both aspects, native 9:16 | 3840×2160 and 2160×3840; every HyperFrames beat has its own portrait composition |
| Phone layout (Rohan's week-11 rule) | no overlapping panels or text on the phone; where it didn't fit, text was removed from the bottom and the room used to space the panels |
| LOGO LAW | Apple is named on screen with Apple's mark (B05, B06) |
| No recordings | no footage or screenshots; everything is drawn from the run |
| No surname | "Row-Haan" in narration, "Rohan V." on screen; no researcher named except Lord Rayleigh |
