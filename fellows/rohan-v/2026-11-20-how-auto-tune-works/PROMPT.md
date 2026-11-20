# PROMPT — "How Auto-Tune Works"

The brief, and how each constraint was resolved.

## Constraints given

Rohan V., for the week of 16–20 Nov: two STEM explainers on audio. He chose the topics: how Auto-Tune works (this
one) and how Bluetooth audio works. He chose HyperFrames with three.js again for both videos, as in week 12.

Hours for the week: 20, across both videos (Rohan's figure). Built 19 Nov.

## How each constraint was resolved

| Constraint | Resolution |
|---|---|
| A STEM topic, audio-related | how software finds the pitch of a sung note (slide a copy of the wave along itself), how far off a singer is (cents), how correction pulls each moment to the nearest note (retune speed), how a pitch is moved without moving the vowel (resampling, the patent's repeated cycles, PSOLA), and where it came from |
| Required opening line, AI disclosure | B00, verbatim; disclosure on screen |
| Executable evidence | `autotune.py` synthesises a singer, detects its pitch with YIN, corrects it at two retune speeds with PSOLA using the detected pitch only, and measures the corrected audio again; every measured number in B01–B04 is the run's; B05 plays the run's three takes |
| Antares' code is not public | the run is labelled "my detector", "my singer", "in my test", "my version"; Antares is credited only with the 1997 release and with what its patent describes; the "patent's way" in the run is my reconstruction from the patent's text, and the docs say so |
| The inventor and the song's producers are not named (fellows-repo rule) | B06 says "an engineer who had used similar maths to read seismic data for oil"; no name on screen, in the narration or in these docs |
| HyperFrames + three.js, both videos | B01–B06 are HyperFrames compositions with three.js stages; B00, B07, B08 stay on the channel's Remotion cards; three.js 0.187.0 (MIT, the version Rohan approved in week 12) is vendored in `week-13/_vendor` and ships in `hyperframes/assets/` with its licence |
| A listening clip people can actually hear | `mix_listen.py` appends the three takes (as sung, gentle, retune speed zero) to B05's narration, unedited and level-matched only, in stereo at 48 kHz (the mono takes play in both ears) |
| No person drawn | the singer is a wave and a pitch track on a piano roll, never a person |
| Western test material (standing preference for STEM evidence) | an original seven-note phrase in C major (E4 G4 A4 G4 E4 D4 C4), sung on "ah" |
| Nothing on C: (standing rule) | HyperFrames' temporary frames go to `D:/Rohan/Claude/HyperFrames/tmp` (`hfkit.py`) |
| Typeset math | none on screen: numbers only; the arithmetic is in FACTCHECK |
| 4K, both aspects, native 9:16 | 3840×2160 and 2160×3840; every HyperFrames beat has its own portrait composition |
| Phone layout (Rohan's week-11 rule) | no overlapping panels or text on the phone; where it didn't fit, text was removed from the bottom (B01's closing note, B03's "Believe" card) and the room used to space the panels |
| LOGO LAW | Antares is named on screen (B06) without its mark: no Antares logo is in the toolkit, and downloading one needs Rohan's OK (FEEDBACK) |
| No recordings | no real singer and no song is played; "Believe" is named, not heard; everything on screen is drawn from the run |
| No surname | "Row-Haan" in narration, "Rohan V." on screen; the only person named is Cher, as the artist of "Believe" |
