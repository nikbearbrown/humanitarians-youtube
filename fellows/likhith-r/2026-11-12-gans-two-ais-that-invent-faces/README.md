# GANs: Two AIs That Invent Faces

**Fellow:** Likhith R. · **Week:** 2026-11-09 to 2026-11-15 · **Builder:** `ai-explainer` on `claude-hai` · **Voice:** Kokoro `am_onyx` (AI narration)

A 60-second explainer on generative adversarial networks: a forger and a detective trained against each other until the detective can do no better than a coin flip, and why the fakes that came out of that idea call for real caution.

## This week's contribution
- **Question:** How did two AIs competing against each other learn to invent faces, and what should we watch out for?
- **Prediction:** I expected a tiny GAN to settle at 50 % detective accuracy without trouble, and I expected the dangers and cautions to be the hardest part to fit, accurately, into 60 seconds.
- **What I built/tried:** 12 beats: the never-existed face, the 2014 paper, the forger-vs-detective game, the 50 % finish line, StyleGAN and thispersondoesnotexist.com, the danger (scam profiles, forged videos, non-consensual images, the 2024 Hong Kong case) and four cautions (a channel you trust, content credentials, detectors miss fakes, consent). The detective's accuracy curve comes from `evidence/gan_toy.py`: 99.9 % at step 19, falling to a 50.6 % mean over the last 500 steps. Eight custom dual-aspect scenes in `scenes/Gans.tsx`, reading numbers only from `scenes/gansData.ts`.
- **Observed result:** Both cuts render at native 4K (60.0 s). GATE F, L, T (unmodified checker) and V (0 blocker / 0 major) pass on 16:9 and 9:16.
- **Next experiment:** Look at how content credentials (C2PA) are attached to and checked on a real image, and what happens to them when the image is edited or screenshotted.

## Human and AI work
**My decisions, implementation and verification:**
- Chose the topic and wrote the content brief (the points the beats cover), and set the 12-beat / ~60 s / Kokoro `am_onyx` / native 16:9 + 9:16 constraints.
- Set the branding: @HumanitariansAI channel, "Irreducibly Human" kicker, greetings ("Namaskaram, Likhith" on 16:9, "Hey, Likhith" on 9:16) and the required opening line.
- Watched both the 16:9 and 9:16 cuts, checked each claim in `FACTCHECK.md` against the sources, and approved the final masters.

**AI tools/voices used and what they generated:**
- Claude Code (Anthropic) drafted the beat sheet and narration, wrote the custom scenes in `scenes/`, wrote and ran the evidence code, checked claims against `SOURCES.md`, ran the Brutalist pipeline and gates, and fixed layout defects found in visual QC.
- Narration is an AI voice (Kokoro `am_onyx`, local). **It is not a recording of Likhith.**

**What I rejected or corrected:**
- The first training setup (one detective step per forger step) was rejected before any scene was built: the detective never got good, so its "50 %" meant nothing. Both runs' logs are kept in `evidence/`.
- The faces on screen are drawn stand-ins, labelled as such, not GAN output; I didn't want to present a drawing as a real generated face.
- An on-screen footnote says newer deepfakes often use diffusion models and GANs opened the door, instead of implying all deepfakes are GANs.
- The Hong Kong case is shown as "≈ US$25 million · HK$200 million", matching the police figure, and Arup is cited as the company.
- The danger line was reworded twice because the voice dropped the "-ed" endings ("helps / fake videos").

**What remains unverified or failed:**
- The required intro "Hi, I am Likhith…" is spoken by the AI narrator; the AI narration is disclosed on screen (opening beat and outro).
- Detector false-negative rates are described in general terms; the video doesn't cite one detector's numbers.
- A real StyleGAN sample could replace the drawn stand-in face; it hasn't been swapped in.
- YouTube 4K processing check and the professors' publication decision are pending.

## Reproduce
- **Brutalist version/commit:** nikbearbrown/brutalist.art `a187fab` (Remotion 4.0.535 / React 19).
- **Source commit used for this export:** not committed — `a187fab` plus local changes: `Gans.tsx`, `gansData.ts`, `JevExplainer.tsx`, `HaiOutro.tsx` under `runtime/remotion/src/`, each exported component registered in `Root.tsx` twice: under its own name at 1920×1080, and with a `916` suffix at 1080×1920. `type_check.py` is the unmodified toolkit version.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16), `scenes/Gans.tsx`, `scenes/gansData.ts`, `scenes/JevExplainer.tsx`, `scenes/HaiOutro.tsx`.
- **Commands** (toolkit root, Python 3.12 venv, MacTeX on PATH; reel at `youtube/brutalist/claude-hai-gans/`):
  ```bash
  python3 runtime/scripts/generate_audio_kokoro.py <reel> --speed <s>          # speeds used: 1.25
  python3 runtime/scripts/remotion_scenes.py <reel>
  ./art run <reel>                                              # 16:9 review
  ./art vertical <reel>                                         # then restore vertical/beat_sheet.json from this folder
  python3 runtime/scripts/remotion_scenes.py <reel>/vertical
  ./art final <reel>                                            # 16:9 master (GATE T first)
  ./art final <reel>/vertical --height 3840                     # 9:16 master
  ```
- **Input/source links:** [SOURCES.md](SOURCES.md) · executable evidence in [`evidence/`](evidence/)
- **Approvals and checks:** [FACTCHECK.md](FACTCHECK.md) (signed off by Likhith), [TYPECHECK.md](TYPECHECK.md) and [vertical/TYPECHECK.md](vertical/TYPECHECK.md) (GATE T PASS), [BUILD-LOG.md](BUILD-LOG.md).

## Watch and review
- **Landscape** — [Watch `landscape/GANsTwoAIsThatInventFaces_LikhithR.mp4`](https://drive.google.com/file/d/1-cwhciqUIwcXH5yZbZBCkMaZ-W6rTpUv/view?usp=share_link) — 3840×2160 — 60.0 s — SHA-256 `4cdfc91b6e5592a46014d584533ed77cc3d513a9da003e0cf186f5b76ac6ff2c` (final master, `.verified.json` receipt: ready)
- **Vertical** — [Watch `vertical/GANsTwoAIsThatInventFaces_LikhithR.mp4`](https://drive.google.com/file/d/119rc7kndhmZkz5lVO8463AX0X3ilZDvP/view?usp=share_link) — 2160×3840 — 60.0 s — SHA-256 `faa30f0ed614c0fa496b62242ef753b320ddd2cd7934aa1635a1ecce0315ea23` (final master, `.verified.json` receipt: ready)
- Sources/large assets Drive link: none
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Folder contents
- `README.md` — this report · `FRICTIONAL.md` — process log · `description.txt` — video description
- `beat_sheet.json` / `vertical/beat_sheet.json` — 16:9 / 9:16 production plans · `SCRIPT.md` — narration
- `SOURCES.md`, `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `BUILD-LOG.md`, `TYPECHECK.md` (+ `vertical/TYPECHECK.md`) — sources, claims, shots, prompts, build record, type-lock gate
- `BUILD-PROMPT.md` — the build prompt
- `scenes/` — custom Remotion scene code (`JevExplainer.tsx` holds the shared stage helpers; `HaiOutro.tsx` is the outro; `gansData.ts` is generated from the evidence run)
- `evidence/` — the executed code and its real output shown on screen
