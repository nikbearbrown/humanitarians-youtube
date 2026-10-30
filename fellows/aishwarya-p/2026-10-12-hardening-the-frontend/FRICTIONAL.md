# Frictional Log — hardening-the-frontend (Video 10)

Written 2026-10-29 from this folder's records.

## 2026-10-12 — Errors that say what went wrong

- **Work and expectation:** the frontend should tell a user why a request failed. The original showed one generic "Failed to fetch" for every failure.
- **Where it resisted, and what was done next:** three different failures looked identical: a wrong publication number (404), a server crash (500), and an unreachable backend.
  - A `classifyError` function now gives each one its own message.
  - The 404 message includes a real example of a valid number.
  - The 500 message points at the API key as the likely cause.
  - The network-failure message says to check that the backend is running.
- **Contributions:** **TODO (Aishwarya):** who or what helped, and what was accepted, changed or rejected.
- **Understood and open:** the three messages cover the three most likely failures. Other failure modes are not handled separately.
- **Record:** [mycroft 00d3baa](https://github.com/nikbearbrown/mycroft/commit/00d3baa65e13b17ba8bb660b0fdef58df52b2bc1) (`App.jsx`), `NARRATION.md` B01.

## 2026-10-12 — A slow path that looked frozen

- **Work and expectation:** the classify path (a BigQuery fetch plus a Claude API call) can take several seconds. The UI should show that it is working.
- **Where it resisted, and what was done next:** the original only disabled the button and said "Reading…".
  - Added a visible spinner.
  - Added a hint explaining why classify is slow.
  - Disabled the inputs during a fetch, so nothing can be resubmitted mid-flight.
- **Contributions:** **TODO (Aishwarya).**
- **Record:** [mycroft 00d3baa](https://github.com/nikbearbrown/mycroft/commit/00d3baa65e13b17ba8bb660b0fdef58df52b2bc1), `NARRATION.md` B02.

## 2026-10-12 — Classify off by default

- **Work and expectation:** the free path (claims reading plus citation lineage, no Claude API cost) should be the default.
- **What was done:** `useState(false)` for classify, so classification is now opt-in.
- **Understood and open:** this choice trades the scope reading for zero API cost on every default request.
- **Record:** [mycroft 00d3baa](https://github.com/nikbearbrown/mycroft/commit/00d3baa65e13b17ba8bb660b0fdef58df52b2bc1), `NARRATION.md` B03.

## 2026-10-12 — Keeping the video to what was built

- **Where it resisted:** deployment was an open item, and it would have been easy to imply it was further along than it was.
- **What was done:** the video covers only the error and loading states and the classify default, all of which match the same day's commit.
- **Record:** `PEDAGOGY.md`, Friction protected.

## Process note

The code was committed and merged the same day ([PR #65](https://github.com/nikbearbrown/mycroft/pull/65)), and so was the video folder ([PR #244](https://github.com/nikbearbrown/humanitarians-youtube/pull/244)). This log was not written at that time, so it is late.
