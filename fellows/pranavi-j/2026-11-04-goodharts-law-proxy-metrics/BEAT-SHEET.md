# Beat Sheet (APPROVED — Gate P, 2026-11-04): "Goodhart's Law: When the Proxy Stops Being the Target"

**Creator:** Sai Pranavi J. | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly project-update report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as this fellow's
prior STEM videos: hallucination, tokenization, lost-in-the-middle, chain-of-thought
faithfulness, calibration, in-context learning limits)
**Phase:** 2 — approved for narration lock / audio generation. Fully generic worked example, no
real company/vendor benchmarked — see `FACTCHECK.md`.

---

## Premise

**What this covers:** a reusable 3-question test — "Name the Target / Find the Lever / Watch the
Coupling" — for telling when and why a proxy metric (a measurable stand-in, chosen because it once
correlated with a real target) diverges from that real target. Teaches the test before any
example, walks it through a worked example (a textbook-level call-center illustration: average
handle time, gamed, while the real target — problems actually resolved — quietly worsens
unwatched), stress-tests it against a falsifiability case designed to show the rubric isn't "every
optimized proxy always fails" (the identical scenario, under the identical pressure, but with a
tracked counterbalancing check added — the same worsening is now caught immediately instead of
hiding), and closes on a concrete audit task the viewer can run today against any metric they
already track.

**What this deliberately avoids:** this is not a report of the fellow's own engineering work, and
does not name or benchmark any specific real company, vendor, or product. This is also a distinct
topic from this fellow's six earlier videos: not hallucination (fabrication), not tokenization (how
text is chunked before any reasoning happens), not lost-in-the-middle (where in a long context a
fact sits), not chain-of-thought faithfulness (whether a stated reasoning trace caused an answer),
not calibration (whether a stated confidence number tracks real accuracy for a single prediction),
and not in-context learning (what a prompt alone can teach a model with no weight updates). This
video is specifically about a different question: when a system tracks a number as a stand-in for
what it actually cares about, under what conditions does that number stop meaning what everyone
assumes it means — and how would you actually tell? The worked example and its falsifiability case
are both generic and hypothetical, matching the pattern used in this fellow's prior STEM videos.

**Real-world tie-in (brief, generic, per the house rule):** this week's companion project-update
video separately covers a real bug where two related numbers — a 0-10 dashboard proxy and the
operational label used everywhere else — were assumed to move together and silently drifted apart
once one of them started being corrected independently. That specific incident is not named or
described anywhere in this video; B06 carries one brief, fully generic sentence acknowledging the
pattern is not unique to any one system. See `FACTCHECK.md`.

**Source status:** general AI/STEM topic explainer. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Framework | All 3 tests shown together as a checklist, before any example | Framework-first, per the pattern that scored well on prior STEM videos |
| B04 Worked example | The tracked proxy and the real (untracked) target shown together, before/after values resolving, tagged "DIVERGED" | The proxy, the target, and the gap between them must all be visible together so the mechanism is legible, not just asserted |
| B05 Falsifiability | The identical panel, numbers, and pressure, with the target now flagged "ON THE SCOREBOARD," tagged "CAUGHT — STAYS HONEST" | Visibly different resolution from B04 — a held-honest tag, not a divergence tag |
| B06 Task | The 3 tests restated as a concrete, runnable checklist | Actionable, not just a restatement of the framework |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "Goodhart's Law: When the Proxy Stops Being the Target" + @HumanitariansAI.
No narration.

**B01. Exec summary (~0:04–0:18)**
VO: "Hi, I'm Sai Pranavi J. This video is about Goodhart's Law — when a measure becomes a target,
it stops being a good measure — and three questions that test whether a proxy you're tracking
still tracks what you actually care about."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:18–0:38)**
VO: "A number on a dashboard climbs every week, and everyone treats that as good news. But a proxy
is never the target itself — it's a stand-in, chosen because it used to move together with what
you actually care about. Nothing guarantees it still does. The number can keep climbing long after
it's stopped meaning what everyone assumes it means."
Visual: a generic dashboard metric panel ticking up week over week, then an overlay posing the real
question: proxy up — target up too?

**B03. Framework (~0:38–1:07)**
VO: "Here's the test, before any example: three questions. One, name the target: what's the real
thing this number stands in for, and could you actually say it out loud? Two, find the lever: is
anyone, or anything, being scored, rewarded, or optimized on this number itself? Three, watch the
coupling: has anything changed in how the number gets produced, or who's incentivized by it, since
you first started trusting it? A proxy chosen honestly can still go stale — not because it broke,
but because something around it changed."
Visual: checklist card, all 3 tests shown together (Name the Target / Find the Lever / Watch the
Coupling).

**B04. Worked example (~1:07–1:35)**
VO: "Here's how it actually works. A call center tracks average handle time — how fast each call
wraps up — as a stand-in for efficient service. Reward agents for shorter calls, and handle time
drops right on schedule. The proxy looks great. But the real target was never 'short calls' — it
was problems actually solved. Push handle time down hard enough, and agents start rushing or ending
calls early. The number improves. The thing it was supposed to represent gets worse."
Visual: a proxy metric (average handle time) and the real target (problems actually resolved)
shown side by side inside one panel, both values updating together — proxy improves, target
worsens — tagged "DIVERGED."

**B05. Falsifiability case (~1:35–2:02)**
VO: "Now the case that would break this test if it were sloppy: the same call center, the same
handle-time proxy, under the same pressure to go faster — this time paired with one more number,
tracked right alongside it: first-call resolution, whether the problem actually got fixed without a
repeat call. Rush a call now, and the repeat-call rate jumps right along with it. The shortcut that
used to pay off stops paying off, because the one number it could hide behind is being watched
too."
Visual: the identical panel, numbers, and pressure as B04, with the real target now flagged "ON THE
SCOREBOARD," tagged "CAUGHT — STAYS HONEST" instead of a divergence tag.
*[Stress-tests the framework against a naive "every optimized proxy always diverges" over-trigger
— the only variable changed from B04 is whether the real target is being tracked.]*

**B06. Scaffolded task (~2:02–2:30)**
VO: "Here's something to try today, on any system you track. Pick one number you already trust —
a dashboard count, a rating, a score. Say out loud what it's actually supposed to stand in for.
Then ask: has anything changed about how that number gets produced, or who's rewarded by it, since
you started trusting it? If no second number would catch the shortcut, that's worth a closer look —
this isn't unique to any one system; it happens anywhere a number gets tracked instead of the thing
it was meant to represent."
Visual: the 3 tests restated as a checklist card.

**B07. Takeaway (~2:30–2:47)**
VO: "Goodhart's Law isn't about bad metrics. It's about good metrics in changed conditions. A proxy
is correlated with the target under the conditions where it was chosen — change the incentive or
how it's produced, and it can look just as reliable while quietly stopping being what you wanted."
Visual: statement card.

**B08. Sign-off (~2:47–2:49)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J.

---

## Production Gate Self-Check (pre-review)

- [x] Framework (B03) shown fully, before any example
- [x] B04's proxy, real target, and the gap between them all visible together, mechanism
      legible without narration alone
- [x] Falsifiability case (B05) uses a genuinely different, counterbalancing-check case — not a
      strawman — and is visibly distinct from B04's divergence resolution
- [x] Scaffolded task (B06) is a concrete, runnable action, not a restatement of B03
- [x] Silent title card present; brand/fellow sign-off card present
- [x] Worked example and stress-test case are clearly generic/illustrative, not naming a real
      company, vendor, or benchmark
- [x] Real-world tie-in (this week's companion project-update bug) acknowledged only in one brief,
      fully generic sentence (B06) — no specific project/company/bug named

**Runtime:** 169.06s raw (Kokoro audio + silent B00) — **Final render confirmed:** landscape
3840x2160 and vertical 2160x3840, both 169.25s (frame-rounded), both GATE V clean (0 BLOCKER / 0
MAJOR) on the true final candidates — see `BUILD-LOG.md` for the full build/bug history and
`README.md` for the production-state summary.

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-11-04. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
