# PROMPT — "How Bluetooth Audio Works"

The brief, and how each constraint was resolved.

## Constraints given

Rohan V., for the week of 16–20 Nov: two STEM explainers on audio. He chose the topics: how Bluetooth audio works
(this one) and how Auto-Tune works. He chose HyperFrames with three.js again for both videos, as in week 12.

Hours for the week: 20, across both videos (Rohan's figure). Built 19 Nov.

## How each constraint was resolved

| Constraint | Resolution |
|---|---|
| A STEM topic, audio-related | why the music has to be squeezed (CD data rate against the link), the radio (79 hopping channels, Wi-Fi, adaptive hopping), codecs, the buffer and why it causes lag, lip sync (delay reporting), and LE Audio |
| Required opening line, AI disclosure | B00, verbatim; disclosure on screen |
| Executable evidence | `bluetooth.py` encodes a synthetic pop track with ffmpeg's SBC, aptX, aptX HD and AAC encoders and measures the data rate from the encoded bytes, then simulates an A2DP link (hopping, Wi-Fi, body blocking, re-sends, the headphone buffer); every measured number in B01, B02 and B04 is the run's; B04 plays the track through the simulated link |
| A simulation, not a measurement of real earbuds | the run is labelled "my test track" and "my simulation"; the radio, Wi-Fi and buffer settings are mine; no codec quality ranking (no listening test, and a waveform match is unfair to perceptual codecs); company claims are attributed ("The Bluetooth SIG says…") |
| HyperFrames + three.js, both videos | B01–B06 are HyperFrames compositions with three.js stages; B00, B07, B08 stay on the channel's Remotion cards; three.js 0.187.0 (MIT, the version Rohan approved in week 12) is vendored in `week-13/_vendor` and ships in `hyperframes/assets/` with its licence |
| A listening clip people can actually hear | `mix_listen.py` appends the same 4 s of the track through the link with a 50 ms buffer, then a 200 ms buffer, to B04's narration, unedited and level-matched only, in stereo at 48 kHz |
| No person drawn | the earbuds, phone, reservoirs and channels are drawn; no person |
| Western test material (standing preference for STEM evidence) | a synthetic pop track: drums, bass, piano chords and a lead |
| Nothing on C: (standing rule) | HyperFrames' temporary frames go to `D:/Rohan/Claude/HyperFrames/tmp` (`hfkit.py`) |
| Typeset math | none on screen: numbers only (B01's landscape note spells the CD sum in words and numbers); the arithmetic is in FACTCHECK |
| 4K, both aspects, native 9:16 | 3840×2160 and 2160×3840; every HyperFrames beat has its own portrait composition |
| Phone layout (Rohan's week-11 rule) | no overlapping panels or text on the phone; where it didn't fit, text was removed from the bottom (B01's CD sum, B03's measurement note, B04's closing note) and the room used to space the panels |
| LOGO LAW | Apple, Android and ffmpeg are shown with their marks from the toolkit (B01, B03); Sony (B03) and the Bluetooth SIG (B06) are named without a mark, and Qualcomm (aptX) is not named: none of those logos was in the toolkit, and downloading needs Rohan's OK (FEEDBACK) |
| No recordings | no footage or screenshots; everything is drawn from the run |
| No surname | "Row-Haan" in narration, "Rohan V." on screen; no person named |
