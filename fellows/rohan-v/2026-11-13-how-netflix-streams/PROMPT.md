# PROMPT — "How Netflix Streams"

The brief, and how each constraint was resolved.

## Constraints given

Rohan, for the week of 9–13 Nov: two STEM explainers, this one on how Netflix streams, the other on how spatial
audio works. He chose HyperFrames for both videos, then asked for three.js and

> beautiful motion designs

Built 9–10 Nov, for a beginner audience, in plain language.

## How each constraint was resolved

| Constraint | Resolution |
|---|---|
| A STEM topic | the bitrate ladder, a quality score (VMAF), per-title encoding, the player choosing chunk by chunk, servers near you, scale and codecs |
| Required opening line, AI disclosure | B00, verbatim; disclosure on screen |
| Executable evidence | `stream.py` encodes and scores two test clips, simulates three players and models two downloads; every measured number in B01–B05 is the run's |
| Netflix's player and ladder are unpublished today | the narration says "my test card", "I streamed", "in my model"; FACTCHECK lists what is not claimed |
| HyperFrames | B01–B06 are HyperFrames compositions; B00, B07, B08 stay on the channel's Remotion cards |
| three.js, beautiful motion | a three.js 3D stage per beat (`hyperframes/scenes/`), the HUD kept in HTML; Netflix's black and red; camera moves on the word clock |
| Downloads approved by Rohan | three.js 0.187.0 (MIT), shipped in `hyperframes/assets/` with its licence; Netflix's N logo from Wikimedia Commons |
| Phone layout (Rohan, week 11) | no overlapping panels or text; text removed from the bottom to space the panels (BUILD-LOG §5) |
| Nothing on C: (standing rule) | encodes and HyperFrames' temporary frames go to `D:/Rohan/Claude/HyperFrames/tmp` |
| Typeset math | none: the interpolation and the download model are in FACTCHECK |
| 4K, both aspects, native 9:16 | 3840×2160 and 2160×3840; every HyperFrames beat has its own portrait composition |
| LOGO LAW | Netflix is named on screen with Netflix's mark |
| No recordings | no Netflix footage or screenshots; the clips are synthetic, made with ffmpeg |
| No surname; no person icons | "Row-Haan" in narration, "Rohan V." on screen; no person drawn; no researcher named |
