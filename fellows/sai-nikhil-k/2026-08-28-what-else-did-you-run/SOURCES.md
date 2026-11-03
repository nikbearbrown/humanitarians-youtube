# SOURCES — What Else Did You Run?

Every figure spoken or shown in this reel comes from one place: the blog post
and the seeded notebook behind it. Nothing was rounded, re-derived, or
estimated for the video.

## Primary source

| Source | Where | How it is used |
|---|---|---|
| "How to Lie with Data — and How to Catch It" (blog post, 2026-08-25) | `~/Documents/manipulator/blog/how-to-lie-with-data.md` | The entire reel. Thesis, scenario, every number. |
| `how_to_lie_with_data.ipynb` | `~/Documents/manipulator/` | The computation behind every figure in the post. Seeded `np.random.default_rng(20260825)`, so the numbers are reproducible. |

The post is `draft: true` and the notebook has **no public URL yet** — the post
itself carries a `NOTEBOOK_URL` placeholder. The reel therefore names no link
and shows no repo chip. Nothing to cite until it is published.

## Every on-screen number, traced

| Shown | Value | Source in the post |
|---|---|---|
| True effect | $1,400/yr | §1 The data factory — `TRUE_EFFECT = 1400.0`, built into the generator by hand |
| Dataset size | 12,000 residents | §1 — `N = 12_000`; 4,521 enrolled (38%), 2,435 completed |
| Enrolment gradient | 62% → 12% | §1 — `p_enrol` across the four education tiers |
| Program Office claim | $7,988/yr | §13 The Narrative Machine — graduates vs. non-finishers (27% higher) |
| Alliance claim | $5,647/yr **less** | §13 — participants vs. non-participants |
| Subgroup claim | $3,616/yr | §13 — "especially effective for Bachelor's+", p = 0.001 |
| District claim | $1,081/yr | §13 — "for district = Fairmount" |
| Unemployment fell | 76% (Apr 2020–Aug 2023) | §3 Cherry-picking the window — most flattering fall, -75.7% |
| Unemployment rose | 121% (Sep 2018–Apr 2020) | §3 — most flattering rise, +120.5% |
| Spending up | 66% since 2018; $9.6M/yr | §13 Taxpayers Alliance packet |
| Budget share down | 12%; $1.38/resident/month | §13 Program Office packet |
| Naive specification range | -$6,355 to $7,988 | §14 The antidote — full range across specifications |
| Selection-aware range | $1,496 to $1,963 | §14 — specs that account for selection |
| Pre-registered estimate | $1,817 [95% CI $1,379–$2,255] | §14 — interval covers the true effect |
| Twelve tricks / eleven questions | 12 / 11 | §2–§12 (twelve tricks incl. 12a/12b); §15 The eleven questions |

## Honesty log

- **Rounded on screen: the two cherry-picked window figures.** The post reports
  `-75.7%` and `+120.5%`; the reel shows `76%` and `121%` because that is how
  the post's own §13 press releases quote them. Both forms are in the source.

- **B01 plots magnitudes, and says so.** `ScaleComparison` is a log axis, so it
  cannot render a negative value. The Alliance claim is *negative* — participants
  earn $5,647 **less**. The beat therefore states on screen, in its slide meta,
  that it is showing "SIZE OF EACH PUBLISHED CLAIM, SIGN SET ASIDE", and the
  narration says two of the figures point in opposite directions. A chart about
  misleading charts does not get to quietly drop a sign.

- **`DivergentFates` tone is layout, not endorsement.** The pattern needs an
  "up" track and a "down" track, so the Program Office renders `good` and the
  Alliance renders `warn`. Neither packet is endorsed — both are misleading, and
  the narration and the verdict card both say so outright.

- **No invented figures.** Nothing on screen was computed for the video. The
  reel adds no statistic that is not already in the post.

- **The scenario is fictional and labelled as such.** Meridian and PathUp are
  synthetic. The reel calls the dataset synthetic in B00, because the fact that
  the data is generated is the method, not a caveat — it is the only reason
  ground truth is knowable.

- **Unverified claims: none.** Every factual statement in the narration is about
  the post's own dataset, which is reproducible from the seed.
