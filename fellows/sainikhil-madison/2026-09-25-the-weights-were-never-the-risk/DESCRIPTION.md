Gavia rewrote its whole detection backend from Python to Rust and kept the exact same model file. That proves nothing about whether it still finds the same loons.

This weekly progress reel opens Gavia 0.2.0, a free, offline desktop app that finds common loons in field photographs. Last week it was a frozen Python server bundled inside a Rust shell, and it talked to that server over a local port with a token. This week the Python is gone. Detection runs in a Rust core inside the app, the interface calls it directly, and there is no server, port or token left. The Mac download went from 84 MB to 45 MB, and every change now builds installers for macOS, Windows and Linux in CI.

The model file did not change: the ONNX weights hash to the same sha-256 before and after. So it is tempting to say the answers did not change either. They are not guaranteed to match, because the network only sees what the decoder and the resizer hand it, and the model's accuracy was measured on Pillow's pixels. One example: before resizing, Pillow shrinks a JPEG inside the decoder by the largest of 1, 2, 4 or 8 that keeps both sides at least 640 pixels, r = min(⌊w/640⌋, ⌊h/640⌋), f = max{d ∈ {1,2,4,8} : d ≤ r}. A 5568 × 3712 Nikon frame from the validation set gets f = 4. The Rust JPEG decoder's own shortcut picks 8. Run on all 26 validation photos, it would have picked a different reduction on 15 of them. So the port rebuilt Pillow's resampling, rounding and JPEG reduction, and froze every box the Python pipeline found into a test fixture before the Python was deleted.

Both pipelines were re-run for this video on the same 26 photos. Python found 32 boxes above the shipped 0.25 threshold. Rust finds all 32, in the same places, with confidences at most 0.0151 apart. Precision (0.9062) and recall (0.8788) agree to four decimals. AP@0.5 moved from 0.8921 to 0.8910. It also scores the faintest guesses, and there Rust has 90 to Python's 89.

Also a correction to last week. Recall now reads 0.879, where last week it was 0.800. The model did not improve, because the weights are byte-identical. The ruler changed. 0.800 is the training framework's own validator, recorded in the checkpoint and still printed on the model card. 0.879 is the app itself at its shipped threshold: 29 of 33 labelled loons found, 4 missed.

The README now says what Gavia is for, as six required features. Detection is shipped. Counting is partly done, with per-photo counts contributed this week by Swara Joshi. A loon call classifier, shoreline and wetland change detection, an underwater habitat classifier and an invasive vegetation classifier have not been started. Survey counting comes next: check a whole folder, get one total, export one CSV.

Try it yourself: before you port a model's inference code to another language, write down what to freeze while the old code still runs. That means its outputs on real inputs, every step that touches pixels before the network does, and the one metric you expect to move. If you cannot say why that metric moves, you are not done.

Gavia, the project in this reel: https://github.com/nikhil-kunapareddy/gavia

Chapters:
0:00 A rewrite has one job: find the same loons
0:16 What was removed — 84 MB to 45 MB, three systems
0:34 Same weights, so the same answers?
0:51 The JPEG draft rule — 15 of 26 photos would differ
1:11 Python against Rust: 32 of 32 boxes
1:32 Recall 0.800 or 0.879 — same weights, different ruler
1:51 Six required features
2:11 Verdict — the weights were never the risk
2:24 Your turn
2:41 Outro

Hosted by Sai. Voice: Kokoro am_onyx, free and local, no account. AI-generated narration. Motion graphics built with Remotion. Equations are typeset locally as outlined SVG, with real fraction bars and floor brackets, not text cards. Every number on screen was re-measured for this video and not copied from the changelog. The parity test and the evaluator were run at the release commit, the deleted Python evaluator was run at its last commit with its pinned dependencies, and Pillow's own draft() and jpeg-decoder's own scale() were run on every validation photo. The README's "43 MB" is not repeated, because the released DMG measures 45.0 MiB. No speed, adoption or download figure appears, because none was measured. No human-performed audio or video in this production.

Gavia: https://github.com/nikhil-kunapareddy/gavia
Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

#AI #ComputerVision #Rust #OpenSource #Conservation #MachineLearning #Reproducibility #HumanitariansAI #WeeklyUpdate

TAGS

Gavia, loon detection, common loon, wildlife detection, conservation technology, YOLO11, ONNX Runtime, Rust, Tauri, desktop app, Python to Rust, rewrite, porting, parity testing, regression testing, Pillow, JPEG decoding, image preprocessing, letterbox, precision, recall, average precision, model evaluation, cross-platform, macOS, Windows, Linux, continuous integration, computational skepticism, open source, Humanitarians AI, weekly progress

HASHTAGS

#AI #ComputerVision #Rust #OpenSource #Conservation #MachineLearning #Reproducibility #HumanitariansAI #WeeklyUpdate
