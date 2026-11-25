# BUILD-LOG — AI Fluency × Brutalist series

Every failure from building films 1–4 (2026-10-29), in the order it happened.
Shape per entry: **broke · noticed · changed · checked.**
Caught by the toolkit: 4. Caught by a person watching: 7. Total: 11.

## 1 · test build · final cut refused
broke:   `./art final` refused — no FACTCHECK.md
noticed: toolkit (GATE F)
changed: compiled the review cut instead; final left for a human sign-off
checked: review cut played, GATE V 0 blockers

## 2 · film 1 · preview crashed
broke:   `remotion_scenes.py --stills` died: EACCES mkdir ~/node_modules/.remotion
noticed: toolkit (error message)
changed: skipped preflight; previewed with `npx remotion still` from runtime/remotion
checked: stills rendered and were read

## 3 · film 1 · missing series name
broke:   GATE L: topic is None; claude-hai needs kicker "Irreducibly Human"
noticed: toolkit (GATE L — nothing rendered)
changed: metadata.topic + B00 eyebrow set; B00 re-rendered
checked: beat-lint clean

## 4 · film 1 · empty canvas
broke:   GATE V: 8 MAJOR underfill (B12 8%, B01 36%, B09 42%, B06 51%; min 55%)
noticed: toolkit (GATE V)
changed: bigger type, new cards, 4-row search, title-layout outro
checked: compiles 2–4 → MAJOR 1, 2, 0

## 5 · film 1 · placeholder pictures
broke:   B06 stack card showed meaningless ball images
noticed: a person, contact sheet
changed: swapped to a focus card
checked: still rendered and read before re-render

## 6 · film 1 · correction landed late
broke:   B01 still typing the correction at 85% of the beat
noticed: a person, frame at 85%
changed: typing 50 → 35 ms/char, type 84 → 140 px
checked: frame re-read

## 7 · films 2–4 · correction never landed
broke:   B01 beats ran ~10 s; corrections not on screen by 75%
noticed: a person, contact sheets (GATE V passed film 2)
changed: typing 35 → 20 ms/char, fewer pauses
checked: frames at 50% and 90% re-read, all three films

## 8 · film 2 · comma split the fix
broke:   correction read "the whole job." — replacement split on its comma
noticed: a person, frame at 90%
changed: replacement → "a complete description"
checked: re-rendered, frame re-read

## 9 · film 3 · clipped tab labels
broke:   "The gate caugh | Only eyes caug"
noticed: a person, contact sheet
changed: labels → "Gate caught" / "Eyes caught"
checked: frame re-read

## 10 · films 2–4 · wrong code labels
broke:   JSON diff, log and Markdown cards all labeled PYTHON
noticed: a person, contact sheet
changed: language set per card
checked: frames re-read

## 11 · card previews · rejected cards
broke:   dashboard card cropped its number; reveal card showed a placeholder
noticed: a person, preview stills
changed: not used; chart and player used instead
checked: preview grid read

## 12 · films 5–6 · correction still late; B01 under 9 s
broke:   corrections landed at ~85% of B01; film 6 B01 was 8.7 s (skill minimum 9 s)
noticed: a person, frames at 75% and 90% (GATE V passed film 6)
changed: one sentence added to each B01's narration; B01 audio regenerated (13.0 s / 12.0 s)
checked: frames at 50/70/90% — correction on screen by 70%
