# Beat Sheet (APPROVED — Gate P, 2026-09-17): "The Link That Pointed Nowhere"

**Creator:** Sai Pranavi J. | Weekly work report
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Phase:** 2 — approved for narration lock / audio generation. FACTCHECK items resolved
2026-09-17: B04 gets an added on-screen "reverse-engineered, not official" caveat label; B07's
two honest limitations kept exactly as drafted, no softening. See `FACTCHECK.md`.
**Format note:** first video built under the toolkit's new submission spec
(`brutalist/docs/FELLOWS-SUBMISSION.md`) — `ProjectName_VolunteerName.mp4` naming, separate
landscape/vertical deliverable folders, and a true 4K 2160x3840 full-length vertical companion
via `./art vertical` instead of the old 1080x1920 Shorts-style cut.

---

## Premise

**What this covers:** the fifth report in the Layer 1 hardening series, and the one previously
flagged as "a bigger scrape-based task, not a quick fix": every Google News item's stored link was
a useless opaque redirect, because the regex-based URL extractor expected a `url=` query parameter
that modern Google News redirect links don't carry anymore. The fix required reverse-engineering
how Google News's own web page resolves the real article URL (a signed request to an internal
endpoint) — and along the way, a subtle ordering bug was caught before deployment that would have
silently undone two previous weeks' classification fixes.

**Why this one is different:** this isn't just "found a bug, fixed a bug." It's a three-part story:
(1) a real technical investigation (why a simple regex/redirect-follow doesn't work here), (2) a
near-miss regression caught by reasoning about execution order before it ever shipped, and (3) a
fix that fails safely by design — if it ever breaks again, the pipeline won't silently degrade,
it'll show up in a log line.

**What this deliberately leaves out:** whether the fellow's actual n8n instance supports the
`fetch`/top-level-`await` Code node features this relies on is flagged as unverified, not assumed —
this video states that limitation honestly rather than implying full production certainty. The
added latency/request-volume cost (~400 extra requests per run) is also named as a real, accepted
tradeoff, not glossed over.

**Source status:** Real engineering work. Every number and code snippet below traces to
`/Users/pranavijs/mycroft/scripts/regulatory-intel/B3-VERIFICATION.md` (2026-08-31). See
`SOURCES.md` for the full claim → source mapping.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated |
| B03 Setup | The failing regex (`url=([^&]+)`) next to a real modern Google News link that has no `url=` param | Both shown together — the mismatch is the point |
| B04 Discovery | The real resolution mechanism: redirect page → signed id/timestamp/signature → POST to the internal endpoint → real URL | Shown as a real flow diagram, not narration-only |
| B05 Near-miss | The classification-ordering bug: `identifySource()` keys off `news.google.com`, called AFTER unwrapping would break it | The before/after call order shown side by side |
| B06 Proof | The live verification counts (100% across 3 escalating test rounds) plus the final 6/6 end-to-end result | All 3 rounds visible, not just the best one |
| B07 Honest limits | The 2 named unverified/accepted-tradeoff items | Framed as flagged limitations, not glossed over |
| B09 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Link That Pointed Nowhere" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:20)**
VO: "Hi, I'm Sai Pranavi J.. This video is about a link that looked like a real article URL
but wasn't — every Google News item in this pipeline was storing a dead-end redirect — and the fix
that had to reverse-engineer how Google News resolves its own links."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:20–0:35)**
VO: "Every item this pipeline pulls from Google News stores a link. Click it, and it doesn't take
you to the article. It takes you back to Google. The link was never real to begin with."
Visual: a feed item card, a link, a click animation landing back on a Google News icon instead of
an article.

**B03. Setup (~0:35–0:55)**
VO: "The code that was supposed to fix this looked for a `url=` parameter in the link and pulled
the real address out of it. That trick used to work. It doesn't anymore — modern Google News links
don't carry that parameter at all. The regex had nothing to match, so it silently did nothing,
every single time."
Visual: the regex `url=([^&]+)` next to a real link
(`news.google.com/rss/articles/<opaque-id>?oc=5`) with the missing parameter highlighted as absent.
*[Source: B3-VERIFICATION.md "The bug"]*

**B04. Discovery (~0:55–1:25)**
VO: "Following the redirect doesn't help either — it just bounces back to the same address. The
only way to get the real URL is the way the Google News page itself gets it: the page embeds a
signed id, timestamp, and signature, and posts them to an internal Google endpoint, which hands
back the real article link."
Visual: a flow diagram — redirect page → extract id/timestamp/signature → POST to internal
endpoint → real URL returned. Small on-screen caveat label directly on the diagram: "reverse-
engineered — not a documented/official API."
*[Source: B3-VERIFICATION.md "Why it's not a simple regex/302 fix" and "The fix". Caveat label
added per FACTCHECK.md item #1 — resolved.]*

**B05. The near-miss (~1:25–1:50)**
VO: "Here's the catch that almost shipped. The step that labels each item by regulator checks the
link's domain — 'news.google.com' means Google News. The old code checked that BEFORE trying to
unwrap the link, which never mattered, because unwrapping never actually worked. The moment
unwrapping started working, checking the domain afterward would've broken that labeling for every
single item — quietly undoing two weeks of fixes. Caught before it ever shipped, by classifying on
the original link first."
Visual: two call-order diagrams side by side — old (classify AFTER unwrap, now broken) vs. fixed
(classify BEFORE unwrap, using the unwrapped link only for display).
*[Source: B3-VERIFICATION.md "Critical ordering fix, caught before deploying"]*

**B06. Proof (~1:50–2:15)**
VO: "I tested this three times, each closer to the real system. First a script: twenty out of
twenty links resolved. Then the exact code, ported: sixteen out of sixteen. Then the actual updated
node, run the way the real pipeline runs it: six real Google News items, all six resolved to real
working articles — and all six still correctly labeled, proving the ordering fix works too."
Visual: three-round results, escalating: 20/20 → 16/16 → 6/6, with the final round's real resolved
URLs shown.
*[Source: B3-VERIFICATION.md "Live verification"]*

**B07. Honest limits (~2:15–2:35)**
VO: "Two things I'm not claiming. I haven't verified this exact code runs the same way on the
fellow's actual n8n instance — only on the workflow file. And this adds real cost: about four
hundred extra requests per run, spread out on purpose so it doesn't look like a burst. If Google
changes how this works, the pipeline won't go quiet about it — it logs exactly how many links
resolved and how many fell back."
Visual: two limitation cards — "not yet verified on live n8n" and "adds ~400 requests/run,
by design not parallelized" — plus the visibility log line
(`Google News links seen: N, unwrapped: M, fell back: N-M`).
*[Source: B3-VERIFICATION.md "Visibility, not silent degradation" and "What's NOT verified"]*

**B08. Takeaway (~2:35–2:50)**
VO: "A fix that works today isn't finished until you've asked what happens the day it stops
working — and made sure you'll actually notice."
Visual: statement card.

**B09. Sign-off (~2:50–2:55)**
VO: "Fixed with Claude Code, verified across three escalating rounds before it ever touched
production."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B03's regex and the real failing link both shown together, not narration-only
- [ ] B05's call-order diagrams show BOTH the broken-if-shipped version and the fixed version
- [ ] B06 shows all 3 verification rounds, not just the strongest one
- [ ] B07's two limitations are named as real, not smoothed over or omitted
- [ ] Silent title card present; brand/fellow sign-off card present

**Estimated runtime:** ~2:55 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-09-17. Both FACTCHECK open items
resolved (see `FACTCHECK.md`). Cleared to generate Kokoro audio and proceed to previz.
