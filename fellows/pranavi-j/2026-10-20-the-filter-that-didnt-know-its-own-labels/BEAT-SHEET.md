# Beat Sheet (APPROVED — Gate P, 2026-10-20): "The Filter That Didn't Know Its Own Labels"

**Creator:** Sai Pranavi J. | Weekly work video
**Format:** `work-report`, same register as this fellow's prior Project 29 reports
**Phase:** 2 — approved for narration lock / audio generation.

---

## Premise

**What this covers:** a real bug found and fixed this week in Project 29's regulatory
intelligence pipeline (`mycroft`). The `/api/feeds/list` endpoint's `source_feed` query
parameter was typed `Optional[SourceFeed]` — a Python enum of 5 fixed, known source labels. But
the pipeline's own classifier, `identifySource()`, can emit open-ended dynamic labels in the
format `"Federal Register - {creator}"` whenever a Federal Register item comes from an agency
outside SEC/CFTC/FINRA — a real, already-shipping behavior (documented in this same repo's
`UNKNOWN-SOURCE-INVESTIGATION.md`). Any attempt to filter `/api/feeds/list` by one of these
dynamic labels raised a 422 validation error (FastAPI/Pydantic enum validation failure) instead of
filtering — silently making a real, now-common class of source label unfilterable through the
API. The fix: widen the parameter's type to `Optional[str]` and pass it through directly (no
`.value` enum accessor needed, since the CRUD layer and the underlying `Feed.source_feed` column
were already plain strings).

**Continuity note:** this is the exact compatibility gap this fellow's prior weekly report
("The Alert That Waited for a Second Item," 2026-10-15) flagged as an honest limit — "identified,
not yet fixed." This video is the follow-up: it was fixed this week.

**What this deliberately avoids:** no claim that this 422 was ever hit by a real user or the live
frontend in production — the frontend does not currently pass `source_feed` as a query parameter
at all, so this was a latent API defect, not an observed incident. Framed honestly as "found and
closed before it could affect a real caller," not "this broke something in front of a user."

**Source status:** real Project 29 (`mycroft`) engineering fix, commit `565e84e` on branch
`feature/regulatory-intelligence-hardening` (not yet pushed), verified live this session via a
FastAPI `TestClient` with a mocked CRUD layer, confirming the dynamic label now passes validation
and reaches the mocked function — and, separately, that the pre-fix endpoint signature
reproduces the real 422. See `SOURCES.md` and `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Setup | The real fixed 5-label `SourceFeed` enum + the real dynamic label format | Verbatim from `models.py` and `workflow.dev.json`'s `identifySource()`, not paraphrased |
| B04 Discovery/fix | Before/after diff of the real 2-line change in `feeds.py` | Real diff, matches commit `565e84e` exactly |
| B05 Verification | The real before/after TestClient table (422 -> 200) | Real measured results from this session's live harness, not illustrative |
| B06 Honest limits | What this fix does NOT claim | Full weight, no softening |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Filter That Didn't Know Its Own Labels" + @HumanitariansAI. No
narration.

**B01. Exec summary (~0:04–0:22)**
VO: "Hi, I'm Sai Pranavi J.. This video is about an API filter that rejected the exact labels our
own classifier generates — a one-line type fix that closes a gap I flagged, but didn't fix, in
last week's report."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:22–0:38)**
VO: "Our source classifier doesn't just pick from a short list anymore. For Federal Register
items outside the big three regulators, it builds the label on the fly. Our filter endpoint
never got the memo."
Visual: a short list of 5 fixed labels next to a sixth, dynamically-built label, visually flagged
as the odd one out.

**B03. Setup (~0:38–1:06)**
VO: "Here's the real enum, straight from the models file. Five fixed source labels. But the real
classifier — identifySource — builds a sixth kind of label on the fly: Federal Register, dash,
whatever agency actually issued it. Department of Labor, Department of Education, any agency
that isn't SEC, CFTC, or FINRA. That label was never in the enum, and never could be."
Visual: the real 5-value `SourceFeed` enum shown verbatim, next to the real `identifySource()`
template string that builds the dynamic label.

**B04. Discovery and fix (~1:06–1:34)**
VO: "The filter endpoint typed that parameter as the fixed enum. Any dynamic label failed
validation before my own code ever ran — a 422, not a filter. The fix is two lines: widen the
type to a plain string, and stop calling dot-value on an enum that's no longer there. The
database column was always just a string underneath."
Visual: the real two-line diff from commit `565e84e`, both the import line and the parameter/
pass-through line.

**B05. Verification (~1:34–2:04)**
VO: "Before trusting the fix, I mounted the real router behind a FastAPI test client, with the
database layer mocked out, and sent the same dynamic label through both versions. The old
signature: 422, enum validation error, exact label rejected. The new signature: 200, and the
mocked database function received the real string, unchanged. A known fixed label still passed
cleanly both times — no regression."
Visual: the real before/after table from this session's live TestClient run (422 -> 200), with
the fixed-label row shown as unchanged in both.

**B06. Honest limits (~2:04–2:26)**
VO: "Two honest limits. First: nothing shows this 422 ever hit a real user — the frontend doesn't
currently send this parameter at all, so this closes a latent gap, not an observed incident.
Second: this verification mocked the database layer. It confirms the API layer now accepts and
forwards the real label correctly — it doesn't confirm a live query against a database that
actually contains rows with these dynamic labels."
Visual: 2 honest-limit cards, side by side, full weight, no softening language.

**B07. Takeaway (~2:26–2:40)**
VO: "When a classifier is allowed to get smarter, every consumer of its output has to be allowed
to keep up — including the one-line type signature nobody thinks to revisit."
Visual: statement card.

**B08. Sign-off (~2:40–2:45)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B03's enum and dynamic-label format shown verbatim, match the real `models.py` and
      `workflow.dev.json`
- [ ] B04's diff matches the real committed fix exactly (`565e84e`)
- [ ] B05's table uses real measured TestClient results from this session, not illustrative
      numbers
- [ ] B06's honest limits kept at full weight, not softened
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] No claim that this 422 was ever hit by a real caller in production

**Estimated runtime:** ~2:40 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-10-20. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
