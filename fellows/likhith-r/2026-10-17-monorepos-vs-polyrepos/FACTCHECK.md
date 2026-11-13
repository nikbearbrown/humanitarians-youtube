# FACTCHECK — Monorepos vs. Polyrepos

Status: claims checked by Claude Code against the primary sources in SOURCES.md. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

Sign-off: I, Likhith, reviewed the 16:9 and 9:16 review cuts and approve the claims above as spoken and shown. I'm signing off for the final master.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Google keeps billions of lines from thousands of engineers in one repo (≈2.0B lines, 25k+ developers) | PASS (dated) | Potvin & Levenberg 2016, Jan 2015 snapshot | "Jan 2015" on screen |
| 2 | B03 | Polyrepo: one repo per project/service; independence, clear ownership | PASS | definition | repo/team names illustrative |
| 3 | B04 | Monorepo: everything in one repo, one history, one toolset | PASS | definition; Potvin & Levenberg (single trunk, shared tooling) | — |
| 4 | B05 | One commit updates a library and all its users | PASS | evidence: commit a8f51ce touches 3 projects | — |
| 5 | B05 | Dependencies stay in sync | PASS (softened) | one version of each internal lib per commit | "automatically" dropped |
| 6 | B06 | At huge scale, plain git checkouts and builds crawl without special tooling | PASS | Potvin & Levenberg (custom Piper/CitC/Blaze needed) | bars illustrative |
| 7 | B07 | Sparse checkout downloads only the folders you need (102 of 403 files) | PASS | evidence/mono_demo.out.txt; git docs | toy repo, labelled |
| 8 | B08 | Remote build caching reuses earlier builds; only what changed rebuilds | PASS | evidence/build_cache_toy.py; Bazel docs | "what changed" = the edited target + its dependents (shown) |
| 9 | B09 | No universal winner; independence vs. tight coordination | EXEMPT | judgment (requester's close) | — |
