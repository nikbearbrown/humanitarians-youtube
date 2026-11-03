Last week the promise was "real precision and recall, from the model, before the meeting." This week those numbers exist — and they ship inside the application that uses them.

This weekly progress reel opens the first packaged build of Gavia, a loon detector for field and drone photographs, and checks the promise against what actually arrived. Not a demo: the DMG is mounted, the bundle is read, and the backend is run. Inside Gavia.app there is a Rust desktop shell, a Python service, the onnx runtime and a 36 MB detector — loon_v1.onnx, YOLO11s, trained 100 epochs at 640 pixels. It is 84 megabytes to download, 176 installed, Apple silicon, macOS 10.15 and up. Nothing in that list reaches for a server. The backend binds loopback and its own help text says, in as many words, that it is not a network service. Detection ran on CPU in about an eighth of a second, and the history page keeps earlier checks in a SQLite file on your own disk.

The numbers are read straight off the model card in the bundle, not recomputed and not estimated: precision 0.930, recall 0.800, mAP50 0.894, mAP50-95 0.614. The reel then does the arithmetic those first two imply. Precision divides the true finds by everything the model called a loon; recall divides the same true finds by every loon that was actually there. The two definitions differ by exactly one term in the denominator — FP becomes FN — and that single substitution is the whole trade. Their harmonic mean is F₁ = 0.860, which the card does not print; it is computed here and labelled as computed.

And the reel does not end on the good numbers. Recall 0.800 has a plain meaning: roughly one loon in five, the model says nothing about. There is a dial for it — the shipped confidence threshold of 0.25 — but dropping it finds more birds and more reed beds. That is a decision to make, not a bug to fix, and the app already asks a researcher to review every result.

One thing worth stating plainly: the 82% visible in the app's result screen is the confidence on one box in one photograph. It is not a model metric, and it is not the 89.4% mAP50. The reel keeps those apart on purpose.

Try it yourself: if you have a model that only works in a notebook, put it in something a colleague can open with no terminal and no account — then make the build write the model's own numbers into the bundle. If you cannot state recall on the way out the door, it is not shipped yet.

Chapters:
0:00 Last week's promise, and an application
0:14 What shipped — inside the bundle
0:32 One image in, one box out
0:48 The card the promise was about
1:04 Two definitions that differ by one term
1:21 One loon in five
1:37 Verdict — promise kept, one number open
1:51 Your turn
2:07 Outro

Hosted by Sai. Voice: Kokoro am_onyx — free, local, no account. AI-generated narration. Motion graphics built with Remotion; equations typeset locally as outlined SVG. The application screens on camera are the author's own unretouched captures of Gavia 0.1.0 — no bounding box, label, percentage or footer was redrawn, retouched or repositioned. Every figure quoted comes from the shipped model card, the bundle's Info.plist, or the backend's own recorded output. No human-performed audio or video in this production.

Humanitarians AI — https://humanitarians.ai
Musinique — https://musinique.com
Medhavy AI — https://medhavy.com

#AI #ComputerVision #ObjectDetection #YOLO #ConservationAI #WildlifeAI #HumanitariansAI #WeeklyUpdate

TAGS

loon detection, Gavia, LoonNet, National Loon Center, conservation AI, wildlife detection, object detection, YOLO, YOLO11, computer vision, ONNX, onnxruntime, edge inference, on-device AI, offline AI, desktop application, Tauri, model card, precision and recall, mean average precision, confidence threshold, model evaluation, model packaging, MLOps, Humanitarians AI, weekly progress

HASHTAGS

#AI #ComputerVision #ObjectDetection #YOLO #ConservationAI #WildlifeAI #HumanitariansAI #WeeklyUpdate
