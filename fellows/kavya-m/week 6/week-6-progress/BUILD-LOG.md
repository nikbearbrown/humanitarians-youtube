# BUILD-LOG — CabStream — Week 3 Progress (Kavya)

"CabStream — Week 3 Progress" — personal project, presenter Kavya Mehta,
voice `am_onyx` (Kokoro), palette `claude`. Third in the CabStream series,
after `kavya-cabstream-week1-progress` and `kavya-cabstream-week2-progress`.

## Structural decisions

- Built fresh with the submission-compliant treatment from the start —
  required intro line, AI disclosure, no NikBearBrown branding, no gap to
  retrofit.
- Register continues the series' honesty pattern: week 1 distinguished
  "shape built" from "scale verified"; week 2 distinguished "defined" from
  "deployed"; week 3 is the payoff — the scale finally arrives — but the
  reel is still careful to distinguish "what my commit message says" from
  "what this reel independently verified." The 1.57B/252.3M figures are
  Kavya's own documented claim, not something this build re-ran.

## Grounding method

`git log --all --format="%ad %h %s" --date=short` against the CabStream
repo, filtered to the week-3 window (2026-06-23 through 2026-06-29). Four
commits found, all on 06-29 — confirmed via `git show --stat` on each.
`databricks/01_bronze_ingestion.py`'s actual committed text was read
directly to confirm the Jan-2023 known-good test anchor (3,066,766 rows)
cited in B04 — the one figure in this reel independently verified from the
code itself rather than taken from a commit message.

## CRITICAL FIX applied from the start: correct compile resolution

Every reel built earlier this session (Brutalist weeks 1–3, CabStream
weeks 1–2) was compiled at the wrong resolution — `compile.py --height`
defaults to 720, and `--height 1920` was used for vertical instead of the
correct `--height 3840`. Full root-cause account:
`kavya-ontologies-observability-scale/BUILD-LOG.md`. This reel is the
second one built with the fix already in place (after
`kavya-ontologies-observability-scale`): landscape compiled with
`--height 2160`, vertical with `--height 3840`, both verified via
`ffprobe` before delivery (3840×2160 / 2160×3840).

## Infra / pipeline notes

One transient issue: the first landscape compile attempt exited with code
4 and no output; a second, identical invocation completed cleanly. Same
one-off process/lock-contention pattern already seen once in week 2's
portrait render — not reproduced on retry, not a code bug.

## Fellows-submission compliance notes

Built to the same standard as every Kavya-branded reel this session:
required intro line verbatim in B00, AI-narration disclosed in the same
beat, native 16:9 (3840×2160) and 9:16 (2160×3840) renders verified via
`ffprobe`, README following the submission guide's template.
