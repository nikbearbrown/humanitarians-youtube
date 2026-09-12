# FACTCHECK — Interest Media.

`yatra-interest-media` · @Yatra · narrated by Kokoro `af_bella` ("Bella"), in for Yatra

---

## The standing instruction

Across this whole series the human has asked, repeatedly and in writing, not to invent
statistics or specific findings. For this reel the instruction was sharpened twice:

> "Please credit Gary Vaynerchuk by name as the source of the 'interest media' concept,
> and don't quote him directly — this script is already paraphrased."

Both halves are enforced **structurally**, not by discipline. See below.

---

## 1. Attribution — credited, never quoted

| Where | What appears on screen |
|---|---|
| B02 `ItmSource` | `Gary Vaynerchuk` as the attribution card's heading |
| B02 `ItmSource` | chip: `PARAPHRASED — NOT A QUOTE`, directly beneath the attribution |
| B09 `ItmLimits` | `Framing credited to Gary Vaynerchuk — paraphrased throughout, not quoted, and not a study.` |
| B10 `ClaudeVerdictArtifact` | `Framing credited to Gary Vaynerchuk — paraphrased here, not quoted.` |

**How the refusal is enforced:** `SourceData` in `runtime/remotion/src/scenes/InterestMedia.tsx`
has a field named `claimParaphrase` and **no field named `quote`**. No component in the
`Itm*` family renders quotation marks around attributed words, and there is no prop
through which a verbatim sentence could be attached to a named person. A component that
*can* render a quote will eventually be given one; this one cannot.

The paraphrase rendered on the B02 card —

> Social media, as we knew it, is basically dead — not gone, transformed. What we are in
> now is closer to interest media.

— is the human's own paraphrase from the script they supplied, restated in the reel's
register. It is presented as a paraphrase, under a stamp that says so, and is never
formatted as speech.

**What this reel does NOT claim about the source:** no date, no venue, no publication, no
podcast episode, no link. The human supplied none, so the reel cites none — the credit is
to a person for a framing, which is exactly what was given.

---

## 2. Numbers — none, anywhere

**No figure, percentage, count, date or measurement is claimed anywhere on screen or in
the narration.** This was verified two ways.

*One precise exception, stated so the claim above stays honest:* B10's verdict page is the
shared `ClaudeVerdictArtifact` component, which numbers its lines `1.`–`5.` as list
enumerators. Those digits are list furniture from a component shared across every reel in
this toolkit — they enumerate five sentences, they are not data, and they assert nothing.
No other numeral is rendered by this reel, and no `Itm*` component can render one at all.

**(a) By construction.** Every type in `InterestMedia.tsx` carries only strings that are
rendered verbatim. There is no `value`, `pct`, `count`, `bar`, `stat`, `total` or `share`
prop on any of the eight components, and nothing in the file computes a number and prints
it. The reel is numeral-free the way the Gordy reel was quote-free: by having nowhere to
put one.

Two places where a number could plausibly have leaked, and what stops it:

- **`ItmVolume` (B04)** — its whole subject is *volume*, which is the one idea in this reel
  that invites a statistic ("X million posts per day"). Its marks are **unlabelled and
  uncounted**, and its type has no caption slot a figure could occupy. The band reads
  `more than a network can sort` — an ordering claim, not a measurement. The scene argues
  density; it does not report it.
- **`ItmJob` (B08)** — the row of marks under the new question is a rhythm for the phrase
  "one post at a time", not a tally. No count is rendered beside it.

**(b) By sweep.** Every string in every `shot.remotion.props` block in `beat_sheet.json`
was regex-swept for `\d[\d,.]*\s*%?` before the first render:

```
ON-SCREEN NUMERALS FOUND: 0
```

Re-run it after any edit to the sheet.

---

## 3. Claims made, and where they come from

Every substantive claim in this reel traces to the script the human supplied. Nothing was
researched, extended or embellished.

| Claim on screen / in narration | Source |
|---|---|
| social media has become "interest media" | the human's script, crediting Gary Vaynerchuk |
| feeds surface creators you don't follow | the human's script |
| the signals are what you watched / paused on / searched | the human's script ("what you've been watching, pausing on, or searching for") |
| there is too much content for a personal network to surface the best of it | the human's script |
| platforms stopped asking "who do you know?" and started asking "what do you care about?" | the human's script, near-verbatim in structure |
| the old model gated reach behind an audience you had to build | the human's script ("you needed thousands of followers before anyone saw your content") |
| one well-made post can now reach strangers on match alone | the human's script |
| the question shifted from "more followers" to "earn attention, one post at a time" | the human's script |
| this is changing how Yatra thinks about content for Humanitarians AI | the human's script (closing line) |

**Deliberately NOT carried over:** the script's "thousands of followers" is a round
rhetorical figure, not a measurement. It survives in the narration as the human wrote it
("you needed thousands of followers") because it is their own phrasing of their own point,
but it is **not** rendered on screen as a number — B07's old-model track is labelled
`build an audience first`, with no figure. If even the spoken phrasing should go, change
one line of `narration_text` in B07 and regenerate that beat's audio.

---

## 4. The falsifiability beat (B09)

`ItmLimits` requires both a `provenance` string and a `falsifier` string — neither is
optional in the type, so the beat cannot be authored without telling the viewer how to
check the claim. What it declines to claim, on screen:

- that followers are worthless — the reel says they stopped being the *entry fee*
- that every feed works the same way
- that any of this is measured — "no figures are claimed here"

And the falsifier: **"Test it on your own feed."**

---

## 5. Named people

Gary Vaynerchuk is the only person named in this reel, and only as the source of a
framing. No characterisation of him, his business, his views beyond the credited framing,
or his affiliations appears anywhere. The people in B03's left column ("your cousin",
"your college roommate", "a friend from work") are the viewer's, generic and unnamed by
design — they are the second person, not real individuals.

---

## 6. Voice and identity

The narrator is Kokoro `af_bella`, introduced out loud in B00's first breath as **"Bella,
in for Yatra"** and signed off the same way in B12, per IN-FOR-BEAR LAW in its Yatra form.
The reel never claims Bella is a person, and never claims the first-person "I" of the body
is Bella's own experience: B00 establishes that Bella is *reading Yatra's notes*, which is
what the rest of the reel is. The footer chip stays `@Yatra` throughout, exactly as
`@NikBearBrown` stays the chip on a Liam-narrated reel.
