# Reproduce Deepa's Accuracy Explainer

Use ai-explainer for the Humanitarians AI channel, with the approved Deepa Shenoy credit and Liam narrating for Deepa. Read README, SHOTLIST, FACTCHECK, SOURCES, PROMPTS and BUILD-LOG in this reel first. Preserve the exact approved script and audio; audio listening was approved explicitly in the conversation. Do not invent any subsequent approval.

The existing custom scene is runtime/remotion/src/scenes/DeepaAccuracy.tsx, registered as DeepaAccuracy and DeepaAccuracy916. Bundle EB Garamond and Montserrat locally. Read mp3/words.json for actual speech anchors. The vertical folder has independent audio and its own beat sheet; never crop generated landscape graphics into portrait.

Use the workspace .venv for Python, system FFmpeg/FFprobe, Node, and Chrome. Render scenes only via runtime/scripts/remotion_scenes.py, in the foreground. Set ART_CHROME to the installed Chrome executable and ART_CHROME_MODE=chrome-for-testing if needed. Do not invoke npx remotion render directly.

Run ./art run on the landscape reel at height 2160 and on vertical/ at height 3840. Check sampled frames, complete decoded output, sound, type checks, the exact 100-item grid and 99/1 arithmetic. Inspect at least 2 fps plus each beat at 15%, 50%, 85%. Repair scene source, regenerate the affected slots and repeat relevant QC. Log source changes and QC findings. Never relax machine gates to obtain a pass.

Mandatory next human gate: watch the complete landscape and vertical review cuts (timing, pacing, beat-to-visual mapping). Stop and present the concrete cuts for Deepa's approval. Do not mark this gate passed yourself.

Only after that approval, run ./art final through its unmodified safety checks, with landscape height 2160 and vertical height 3840. Export to this project's deliverables/landscape and deliverables/vertical. Both files are named AccuracyExplainer_DeepaShenoy.mp4. Preserve their verified receipts and hashes. Inspect actual final frames and audio. Report any remaining limitations; no upload, scheduling or publication.
