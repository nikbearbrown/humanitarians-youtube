# FACTCHECK — What It Stopped Needing

Every claim the reel makes, where it comes from, and how far it can be pushed.
Three tiers: **AUTHOR'S PROSE** (he wrote it, in the commit body or CHANGELOG),
**VERIFIED IN REPO** (re-derived by running commands against the clone at
`29b2269` — not taken on trust), and **EDITORIAL** (a judgment the voice makes
that the repository does not state).

---

## AUTHOR'S PROSE — his own words, authorised as this week's report

| Claim | Where it appears | Status |
|---|---|---|
| clauding is a Python/PyObjC rewrite of a Swift/AppKit menu bar app | B00, B01, B06 | AUTHOR'S PROSE |
| A plain process with an accessory activation policy can own an `NSStatusItem` | B03, B06 | AUTHOR'S PROSE — and verified at `bar.py:229` |
| Therefore the bundle, codesigning, notarization, DMG and Homebrew cask all go | B03, B06 | AUTHOR'S PROSE, stated as a consequence in the commit body |
| The feature set is three states and nothing else | B00, B01, B02 | AUTHOR'S PROSE |
| Seven named features were dropped | B03, B06 | AUTHOR'S PROSE — enumerated in both the commit body and CHANGELOG; counted, not estimated |
| "waiting for input" now covers the idle notification too; Swift filtered it out | not on screen — context only | AUTHOR'S PROSE |
| State moved to `~/.claude/clauding/` so a stale old install can't feed it | not on screen | AUTHOR'S PROSE |
| The PATH-ordering hazard: a planted `clauding-hook` could be found first | B04, B06 | AUTHOR'S PROSE — and verified at `install.py:37–43` |
| The test for that property survived and now asserts the real hook ran | B04 ghostText | AUTHOR'S PROSE, verbatim from the commit body |
| Process liveness, interrupt recovery and the mtime-gated tail were carried over as hard-won | B05 | AUTHOR'S PROSE — "Carried over because it was hard-won" |
| Model and effort come from the transcript; no hook payload carries them | B01, B02 | AUTHOR'S PROSE |
| No network requests of any kind | B01 | AUTHOR'S PROSE — README and PRIVACY.md both |

---

## VERIFIED IN REPO — re-derived, with the command that produced it

| Claim | On screen at | Command |
|---|---|---|
| 46 files changed, 2,196 insertions, 2,843 deletions | B00, B03, B06 | `git show --stat 29b2269` |
| 1,873 lines of Python added | B01, B06 | `git show --numstat` summed over `*.py` |
| 10 modules under `src/clauding/` | B01, B06 | `find src/clauding -name '*.py'` |
| 58 tests, replacing 3 Node ones | B01, B05, B06 | 46 `def test_` + 12 parametrised cases (`tests/test_transcript.py:40–58`) = 58 — reconciles exactly with the commit body |
| 8 KB transcript tail | B05 | `TAIL_BYTES = 8192`, `transcript.py:15` |
| `#d97757` and the amber | B02 plate | `BRAND_ORANGE`, `AMBER` — `bar.py:50–51` |
| The three state strings | B02 plate | `bar_text()`, `bar.py:58–64`, and `README.md` lines 7–11 |
| The spark is a 60×60 alpha mask tinted at runtime | B02 plate | `logo.py` docstring + `_tinted()`, `bar.py:68` |
| MIT, then and now | B05 | `LICENSE`, unchanged by the rewrite |

**2,285 lines removed from Swift/JS/shell** was also verified (`git show --numstat`
over `*.swift *.js *.sh`) but is **not on screen** — the reel quotes the total
deletion figure instead, which needs no language breakdown to be true.

---

## EDITORIAL — the voice's judgment, not the repository's

These are the reel's arguments. They are flagged in `PEDAGOGY.md`'s review
checklist because they are the parts a human should sign off on.

| Claim | Where | Note |
|---|---|---|
| The deletions divide into two kinds by *cause* — "stopped needing" vs "chose to drop" | B03, the ONE idea | The repository lists both groups but never contrasts them. The split is the reel's framing. |
| The seven dropped features were a *taste call* | B03 track 2, B06 line 3 | The commit body says "deliberately" and "on purpose", which supports this; the word "taste" is the reel's. |
| Deleting a hazard's conditions is better than hardening against it | B04 resolver | The commit body states the property factually. Calling it the better answer is editorial. |
| "A rewrite is where subtle behaviour goes to die" | B05 caption | The reel's line entirely. |
| The near-constant width across states is deliberate | B02 narration | Supported — the commit body says "the text that remains is stable within a session, so the item's width barely moves." |

---

## Claims deliberately NOT made

- **Nothing about speed, memory, CPU or battery.** No benchmark was supplied or
  run. The narration never says "faster", "lighter" or "more efficient". A
  rewrite reel is exactly where such a number would be believed without evidence.
- **No adoption figures** — no installs, stars, forks, downloads.
- **No claim the hazard was ever exploited.** B04 says it was real and that the
  installer hardened against it. It does not go further, and should not.
- **`POLL_INTERVAL = 0.5`** is verified but stayed off screen: alone it reads as
  a performance claim, and there is no measurement behind that reading.
- **The upstream author is not named**, anywhere, by the author's instruction —
  even though his own README credits him.
