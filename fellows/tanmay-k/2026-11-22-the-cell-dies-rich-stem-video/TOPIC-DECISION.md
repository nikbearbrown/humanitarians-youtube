# Week 32 — Topic selection (2026-11-23)

**Rule:** the topic comes from a `claude-for-<topic>/<topic>` folder in `humanitarians-youtube`, and is available only if no fellow (including us) has covered it.

## Method (read-only)
- Branch heads: 97 on GitHub against 104 local refs; 30 branches had moved or were new since the earlier sweep. Their trees were read with GitHub API GET requests only; nothing was fetched, checked out, pushed or written in the shared repository. Unchanged branches came from the previous week's path listing.
- Pool: 2,193 `claude-for-*/<topic>` folders. With variant prefixes stripped (nbb-, claude-liam-, medhavy-vox-, vox-, cli-, hai-) they give 1,220 topic keys.
- "Taken": a key word of five letters or more appears in any `fellows/*/*` folder name (1,266 folders), or in our own Weeks 15 to 31 angle, README and topic-decision notes. Excluded by hand rules: lectures, chapters, volumes, numbered series, person profiles, political words, demos. 452 keys were taken by fellows, 259 by our notes, 231 excluded and 97 had no usable word, which left **181 candidates** (`stationary-phase`, rejected last week, removed).
- Draw: six names from `random.SystemRandom`: abraxane-solvent, oncolytic-virotherapy, lnp-endosomal-escape, mir-deletion, schrodinger-i, **brownout**.

## Chosen: `claude-for-computer-science/cli-brownout` (library film "A Battery Can Be Full and Still Crash Your Device")
Why it over the other five: it can be simulated end to end from public physical constants and our own code, it carries no medical or health claim (four of the other five are cancer or drug topics), and it has no politics or third-party media.

## Uniqueness checks
- Fellow folder names: no match for brownout, battery, coin cell, internal resistance, capacitor or Thevenin.
- Fellow file contents: a read of `fellows/` on every local remote ref for brownout, internal resistance, coin cell and CR2032 found nothing. For the 30 moved branches, the changed files since the earlier refs were listed with the GitHub compare API and the 4,140 text files dated October and November were fetched with redirects followed (0 failed): no hits for the same terms. An earlier pass that did not follow redirects returned empty bodies, so its "no hits" meant nothing and was discarded.
- Our own Weeks 15 to 31 narration, beat sheets, scripts and angles (349 files): no battery, resistance, capacitor, sag, hold-up or stranded-energy language. The one "brownout" hit is the string `NikBearBrownOutro`.
- Library: one film plus variants (`cli-`, `claude-liam-cli-`, `nbb-cli-`); no fellow variant.

## What the library film states (read before forming an angle)
A full coin cell, a device that resets anyway. CR2032, 3 V, a round 1000 ohm internal resistance, an 8 mA inference burst, a 2 V reset line, V = V_oc minus I times R. A 100 uF capacitor flattens the sag. Summary: energy versus instantaneous delivery. Next steps it leaves open: find the threshold in the datasheet, measure the burst, size the cap.

## Angle (chosen by Tanmay, 2026-11-23): A, "The Cell Dies Rich"
A coin cell is finished for a device when its internal resistance crosses (V_open minus V_reset) divided by the burst, not when its charge runs out. Our simulation of a CR2032-class cell, fitted to two manufacturers' published graphs, measures the share left unspent at the first reset: it depends on the burst. The other two candidates were B, "Two Loads Tell You the Battery" (measuring resistance from two load points; kept as the film's viewer exercise in a different form) and C, hold-up time and capacitor sizing (it closes the library film's own hand-off, so the weakest on originality). After the first measurements Tanmay chose to **keep the title and state the dependence**: the film says how rich depends on the burst, and where it stops being true (8 mA never fails). Boundaries are in `ANGLE.md`.
