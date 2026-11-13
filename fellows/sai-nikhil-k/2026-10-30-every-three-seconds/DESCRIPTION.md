Until now, Gavia only looked at photos. This week it learned to listen: open a recording, and it marks every three seconds where a loon calls.

This week on Gavia, the offline loon app: Check an audio, new in version 0.4.0. We explain how it hears, then test it the way our own field recordings will, under a drone's propeller noise, using the app's own code.

The screen. Open a recording (WAV, MP3, FLAC, OGG, M4A, or the sound of a video) and Gavia shows a timeline of three-second bars; the red ones hold a loon call. Click a call to hear it, or download every stretch as a CSV. Nothing is sent anywhere.

How it hears, in six steps: decode the file, mix it to mono at 48 kHz, cut it into three-second windows back to back, pass each window through BirdNET 2.4 (the Cornell Lab of Ornithology's bird-sound model), get 1,024 numbers back, and turn them into one probability with a small logistic regression:

- n = 3 s × 48,000 Hz = 144,000 samples per window
- z = ((x − μ) / σ) · w + b, where x is BirdNET's embedding
- P = 1 / (1 + e^(−z)), and Gavia calls it a loon at P ≥ 0.5, which is exactly z ≥ 0

The perfect score. On loonet's validation set the classifier scores 1.000, but those windows were picked by BirdNET's own score (loon above 0.4, the rest below 0.02), so the set is easy by construction. The model card says so.

The test that matters. We rebuilt loonet's drone-noise test (65 validation windows, 28 of them loon, mixed with our drone's propeller noise) and ran it through Gavia 0.5.0's own Rust detector:

- Clean: 28 of 28 loon windows caught
- Drone at 10 dB: 24 of 28
- Drone at 5 dB: 19 of 28
- Drone at 0 dB (as loud as the recording): 13 of 28
- False alarms on the 37 other windows: 0, at every level

Loonet's Python pipeline gives the same table; the two agree to within 0.000004. In the app, a Maine recording shows a loon in 4 of 8 stretches clean (strongest call 88%) and 2 of 8 with the drone mixed in at 5 dB (77%): both calls are still found, but their quieter halves drop below the line.

Limits: BirdNET is licensed CC BY-NC-SA 4.0, so the call model is for non-commercial use, and it can't yet tell a wail from a tremolo, a yodel or a hoot.

Try it yourself: record a minute of sound near water, ask an assistant what a three-second window, an embedding and a 0.5 threshold would each do to it and what could make a call slip through, then open it in Gavia and see which bars turn red.

Gavia, the project in this reel: https://github.com/nikhil-kunapareddy/gavia

Chapters:
0:00 Gavia learns to listen
0:12 Check an audio
0:29 How it hears: six steps
0:49 One window, one probability
1:08 A perfect score, easy by construction
1:28 Under the drone: 28 → 13 of 28
1:47 One recording, clean and under the drone
2:03 Verdict
2:19 Your turn: listen for yourself
2:33 Outro

Sources:
Gavia v0.4.0 (CHANGELOG, call model card, source) — https://github.com/nikhil-kunapareddy/gavia/releases/tag/v0.4.0
BirdNET 2.4, K. Lisa Yang Center for Conservation Bioacoustics, Cornell Lab of Ornithology — https://zenodo.org/records/15050749
loonet's looncall v1 (training data, formula, drone-noise test) — Sai's loonet project

Media:
App screens — Gavia 0.5.0 on a Mac (the audio check is unchanged since 0.4.0), scratch storage folder
Common loon recording, Mount Desert, Maine — iNaturalist, CC0 (no rights reserved)
Drone noise — from our own drone footage

Hosted by Sai. Voice: Kokoro am_onyx, free and local. AI-generated narration; motion graphics built with Remotion; the equation typeset locally as SVG. The app results shown are what Gavia returned on this Mac. The drone-noise counts come from Gavia's own call detector at v0.5.0, run on a MacBook Pro on clips rebuilt from loonet's notebook with its fixed seed. No image or audio was generated. No human-performed audio or video.

Gavia: https://github.com/nikhil-kunapareddy/gavia
Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Gavia, loon, common loon, loon call, bioacoustics, BirdNET, bird sound recognition, audio classification, embeddings, logistic regression, drone noise, signal to noise ratio, conservation technology, offline AI, Rust, Humanitarians AI, weekly progress, Computational Skepticism

#AI #Bioacoustics #Conservation #Birds #Loons #OpenSource #HumanitariansAI #WeeklyUpdate
