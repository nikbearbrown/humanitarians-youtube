# Cinematic and portrait sources

Root.tsx registers STEMwide (1920×1080), STEMtall (1080×1920), and Progresstall (1080×1920), at 24 fps. The two JSON sheets retain the original narration and sentence-level caption timing. Portrait layouts are independently reflowed.

The STEM browser, code, test runner, workbook, and GIF panels are illustrative animations, not recordings of Claude execution. Existing progress landscape is reused unchanged.

Install the pinned package dependencies. Run node render.cjs for preview frames, or node render.cjs --render for the three new silent compositions. Run finalize.py using Python with NumPy and FFmpeg installed to mux the audio. The completed progress landscape is copied byte-for-byte from its original MP4. Rendered compositions are silent: mux the existing project narration/master audio at time zero, trimming to exactly 4265/24 seconds (STEM) or 5660/24 seconds (progress). Narration must not be regenerated. The final STEM exports also include quiet, locally synthesized transition tones.

Original scripts, narration, captions, source projects, YouTube descriptions, and archived STEM remain preserved. Human final-video approval is not inferred from technical QC.
