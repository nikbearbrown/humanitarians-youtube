# SOURCES — What It Stopped Needing

Week of 2026-09-11 · clauding 1.0.0.

> **Attribution rule for this reel, set by the author: name the project, not the
> person.** On screen and in narration the upstream is `claude-status-bar`, or
> "the original". The upstream author's name appears nowhere in this reel, in
> this file, or in `PEDAGOGY.md` — even though the repository's own `README.md`
> and `ACKNOWLEDGEMENTS.md` credit him by name and link to his work. The reel is
> deliberately more reserved than the repo it documents. This is a different rule
> from 09-11-1, where no collaborator was named at all.

---

## Primary sources

| Source | Used for | Provenance |
|---|---|---|
| `https://github.com/nikhil-kunapareddy/clauding` @ `29b2269` | every claim in the reel | The author's own repository, supplied by him directly, 2026-09-11 |
| `data/commit-29b2269.txt` | B00, B03, B04, B06 — the "why" behind each deletion | The `feat!` commit body, vendored verbatim. **Authorised by the author as this week's raw material in place of dictated bullets.** |
| `data/readme-states.txt` | B01, B02 — the three states and the feature set | `README.md` lines 1–15, vendored verbatim |
| `data/spark.png` | the mark on the B02 plate | The app's own 60×60 alpha mask, extracted from `src/clauding/logo.py` |
| `CHANGELOG.md` 1.0.0 | B03's two piles, B06's verdict lines | The author's own release notes |

---

## Every on-screen figure, and how it was checked

No figure was taken on trust. Each was re-derived from the cloned repository.

| Figure | On screen at | How it was verified |
|---|---|---|
| 46 files, 2,196 insertions, 2,843 deletions | B00, B03, B06 | `git show --stat 29b2269` |
| 1,873 lines of Python added | B01, B06 | `git show --numstat` summed over `*.py` |
| 2,285 lines removed from Swift/JS/shell | not on screen — context only | `git show --numstat` summed over `*.swift *.js *.sh` |
| 10 modules | B01, B06 | `find src/clauding -name '*.py'` |
| 58 tests, replacing 3 | B01, B05, B06 | 46 `def test_` functions + 12 parametrised cases on `test_model_label` (`tests/test_transcript.py:40–58`) = 58. Reconciles exactly with the commit body. |
| 8 KB transcript tail | B05 | `TAIL_BYTES = 8192`, `transcript.py:15` |
| accessory activation policy | B06 | `NSApplicationActivationPolicyAccessory`, `bar.py:229` |
| absolute-path hook commands | B04, B06 | `install.py:37–43`, and its own comment |
| `#d97757` / amber | B02 plate | `BRAND_ORANGE`, `AMBER` — `bar.py:50–51` |
| seven dropped features | B03, B06 | Enumerated in the commit body and `CHANGELOG.md`; counted, not estimated |

---

## What is deliberately NOT on screen

- **No benchmark of any kind.** No CPU, memory, launch-time or battery figure, and
  no timing comparison against the Swift version. None was supplied or measured,
  and a rewrite reel is exactly where an invented performance number would be
  believed. The word "faster" does not appear in the narration.
- **No adoption numbers** — no installs, stars, forks or downloads.
- **No claim that the rewrite is better.** B03 says one pile was a taste call and
  labels it as such; B05 credits the upstream behaviour as hard-won and kept.
- **`POLL_INTERVAL = 0.5`** is verified but stayed off screen: on its own it reads
  as a performance claim, and there is no measurement to back that reading.

## B02 is a rendering, and says so

There is no screenshot of the menu bar in this reel. B02's plate is composed by
`make_plates.py` from the app's own asset and its own colour constants, and the
plate carries the words **"A RENDERING, NOT A SCREENSHOT"** on its own face in
both the landscape and portrait cuts. The three strings are transcribed
character-for-character from `README.md` and from `bar_text()` in `bar.py:58–64`.

If a real screenshot arrives, it should replace the plate — but the plate must not
be quietly relabelled as one.

---

## One thing to confirm

The narration for B04 says the planted-binary hazard was *real* for the original.
That is how the commit body and `CHANGELOG.md` both describe it, and the upstream
did ship a PATH-hardening fix. The reel does not claim the hazard was ever
exploited, and should not start.
