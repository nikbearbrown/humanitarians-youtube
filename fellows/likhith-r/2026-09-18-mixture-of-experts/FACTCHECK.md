# FACTCHECK — Mixture of Experts

Status: claims checked by Claude Code against the primary sources in SOURCES.md. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

Sign-off: I, Likhith, reviewed the 16:9 and 9:16 review cuts and approve the claims above as spoken and shown. I'm signing off for the final master.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Models hold hundreds of billions of parameters (671B shown) | PASS | DeepSeek-V3: "671B total parameters" | Source labelled on screen |
| 2 | B03 | Dense models run every parameter per token; double size ≈ double cost | PASS | Dense transformer forward compute ∝ parameter count | Qualitative bars, no numbers |
| 3 | B04 | MoE splits each layer into many smaller experts | CORRECTED | Mixtral: "each layer is composed of 8 feedforward blocks (i.e. experts)" | Framed as the feed-forward block inside each layer |
| 4 | B05 | A router scores experts per token and picks two of eight | PASS | Mixtral: "a router network selects two experts" per token per layer | Scores labelled illustrative |
| 5 | B06 | Only the chosen experts run; the rest sit idle for that token | PASS | Shazeer 2017: "sparse combination of these experts … for each example" | Routing labelled illustrative |
| 6 | B07 | Mixtral: 47B parameters, ~13B used per token; DeepSeek-V3 671B / 37B | PASS | Mixtral + DeepSeek-V3 abstracts | Sources on screen |
| 7 | B08 | Every expert must stay loaded in memory | PASS | Derivation: any token may route to any expert, so all 47B must be resident | — |
| 8 | B09 | Capacity grows without per-token compute growing proportionally | PASS | Follows from 6 | — |
