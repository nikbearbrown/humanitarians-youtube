# GATE P — Lookup, Not Training

**Reel:** `claude-hai-lookup-not-training` · ai-explainer · claude palette (fidelity)
**Channel:** claude-hai · @HumanitariansAI · Bella (`af_bella`) · Pragmatist
**Beats:** 14 (B00–B13) · estimated ~3:50
**Reviewer:** Chaitanya (author)
**Date:** 2026-10-01

> Nothing downstream of this file runs until it reads `VERDICT: PASS`.
> `generate_audio_kokoro.py` refuses without it.

---

## 1. The one idea

**The tutor was never trained on the textbook. The book is searched at the moment
a question is asked, and the passages ride along with the question — which is why
a content fix fixes the tutor, why it can cite, and why it costs cents.**

The author flags this as the highest-value video in the set for a non-engineering
audience, because the training assumption is common and it changes how people judge
the whole system. The reel is built to replace that one assumption and nothing else.

## 2. Structure — the mandatory ai-explainer spine, intact

| Beat | Act | Surface |
|---|---|---|
| B00 | ASK | Claude composer, cold open, **ask lands answered** |
| B01–B10 | BODY | concept illustrations (the author's 5 scenes) |
| B11 | VERDICT | Claude artifact page |
| B12 | HANDOFF | Claude composer, "Your turn.", prompt read aloud and discussed |
| B13 | OUTRO | title restate, terracotta period, handle beneath |

Scene → beat map. Scenes were split, never cut, so each beat carries one idea.

| Source scene | Beats | Words |
|---|---|---|
| 1 · The assumption | B01, B02 | 49 + 42 |
| 2 · How it actually works | B03, B04 | 37 + 45 |
| **3 · Why this is better** | **B05, B06, B07** | 42 + 36 + **36** |
| 4 · The one catch | B08, B09 | 37 + 48 |
| 5 · Close | B10 | 54 |

**Scene 3 is deliberately three beats, one per reason, so the cost comparison owns
B07 alone.** That is what makes it protectable: it can be `--keep`-pinned in the
short and trimmed around, never through. The author's instruction was that this is
the detail people repeat afterwards.

## 3. Does each beat teach, or just say?

Every body beat has a `show` block of ordered visual events keyed to spoken phrases.
The PPT test:

- **B01** the assumption is drawn *first*, then struck — the viewer watches the guess
  get refuted rather than hearing that it is wrong.
- **B02** the question physically stalls against the model card, then is redirected to
  the book. The beat's own question gets answered on screen.
- **B03** a search sweep runs the page; passage cards lift off it.
- **B04** question and passages merge into one envelope and open *inside* the model
  card — "in front of it, not inside it" is the whole distinction, enacted.
- **B05** one edit to the chapter propagates down into the tutor's answer card.
- **B06** the left answer's line reaches a named section; the right one dead-ends.
- **B07** the self-host bar runs off the edge of the frame and does not stop.
- **B08** entries flow from book to index cabinet; the probe returns instantly.
- **B09** the healthy in-step state is shown first, then drifts; the confidence meter
  runs to full while the answer goes stale, and the error/warning slots stay blank.
- **B10** the loop lights stage by stage.

No two consecutive body beats share a visual scheme.

## 4. Register check (Pragmatist)

Same flag as the two prior claude-hai reels: hai's usual spine question ("when to use
AI and when NOT to") does not apply — this is a systems explainer. Pragmatist is kept
as a delivery tone plus the register's mandatory "where it fails", which is carried in
three places and is not softened:

- **B08/B09** are the entire failure mode — a stale index answering confidently with no
  error and no warning. The author's Scene 4, intact.
- **B07** prices the alternative honestly rather than strawmanning it.
- **B12** hands the viewer the sharper version of the problem: a lookup system that
  quietly falls back on the model's own prior knowledge looks exactly like one working.

## 5. The author's constraints — how each is met

| Constraint | Status |
|---|---|
| Never say "RAG", "embeddings", "vector search", "retrieval-augmented" | Zero instances anywhere in the sheet — narration, props, card text, metadata. The mechanism is "looking things up" / "searching the book" throughout |
| Land "open-book exam, not a study session" once, clearly, undressed | Spoken exactly **once**, as its own closing sentence in B04, with nothing added. "open-book" occurs once in the entire reel. The episode title was chosen as "Lookup, Not Training." precisely so the outro's title restatement cannot dilute it |
| "By default" if the reindex trigger is configurable | **"By default"** is in B08's narration *and* set in terracotta on screen. See §6.1 — this is the one item that could not be confirmed in code |
| State no unverified count | No count of passages, steps or checks is stated or implied. B03/B04 draw three passage cards **plus a trailing ellipsis** so the group reads as "a handful" — the only thing the source supports. Full count audit in `SOURCES.md` |
| Protect Scene 3's cost comparison | Owns B07 alone, flagged `protected` in the sheet, `--keep`-pinned for the short |
| QC near t=0 for every scene | Every body beat's `show` block **opens with an explicit non-empty t=0 state**, authored for this constraint — see §6.3 |

## 6. Flagged for the reviewer

### 6.1 The reindex trigger could not be confirmed against code — hedged, not guessed

The author asked for code-level confirmation *before* narration was finalised. It was
attempted first and could not be completed: the book repos are **not on this machine**,
only their documentation. No `package.json` could be read to see whether `index:build`
is an unconditional `prebuild`/`predev` hook.

Three documents say the index rebuilds "automatically during `npm run dev` and
`npm run build`"; the same source hedges with "in normal use", notes that drift happens
"when a deploy ships without re-running the build step", and physics-vol-1's
ARCHITECTURE.md states only the *requirement*, not an automatic guarantee.

So narration says **"By default, that index is rebuilt whenever the book is built"** —
correct whichever way the hook is wired, and the author's own stated fallback.

### 6.2 One factual correction to the script

Scene 2's "before that question goes anywhere near the AI" is **not true in all
configurations** — in the hybrid search mode the question is sent to OpenAI once before
the search runs, to be turned into numbers for matching. Narration now reads **"before
that question reaches the model that writes the answer"**, which is true in both modes
and preserves the script's point intact. Logged in `SOURCES.md`.

### 6.3 Every beat opens dressed, by construction

The author asked that QC sample near t=0 for every scene, not just mid and end — the
defect that hunts for is a scene that opens on an empty or half-built frame. So this
was designed in rather than discovered: **every body beat's `show` block begins with an
explicit "OPENING STATE IS NOT EMPTY" event** naming what is already drawn at t=0.
B09 is the clearest case — the healthy, in-step state is fully established before it
drifts, which is both the anti-empty-open measure and better teaching.

### 6.4 The requested sign-in line conflicts with the skill's structure — flagged

COLD OPEN LAW puts B00 on the Claude composer with the greeting `[cue], HAI`; there is
no presenter-intro slot, and a synthetic voice must not claim to be a named person.
This is the identical conflict the author resolved on this channel on 2026-09-21, so
that precedent is applied rather than re-litigated: B00 narrates **"Hi — this is Bella,
for Chaitanya."** followed by the author's topic clause verbatim ("…how the AI tutor
actually knows the textbook — through lookup, not training"), and the Chaitanya credit
is restated on the outro. Say so if you want it handled differently this time.

### 6.5 Nine new Remotion components are specified and do not exist yet

`TrainedAssumption`, `OffTheShelf`, `PassagePull`, `HandedTogether`, `FixTheChapter`,
`CiteOrNot`, `CostCompare`, `IndexAhead`, `StaleIndex`, `ShortVersion` — each with a
9:16 sibling, all registered at 1920×1080 / 1080×1920 so `--scale=2` yields true
3840×2160 at source. Built after this gate passes.

### 6.6 Runtime ~3:50

Duration is an output. No target was set for this reel; the prior one in this series
landed 3:28. Say so now if you want it tighter — the lever is word count per beat, and
the order of sacrifice is: the handoff's discussion, then Scene 1, then Scene 5.
**Scene 3's cost beat is not on that list.**

## 7. Full narration, in order

**B00 · ASK** (40 words) — Hi — this is Bella, for Chaitanya. This video is about how the AI tutor actually knows the textbook — through lookup, not training. Almost everyone guesses wrong about this, and the guess changes how you judge the whole system.

**B01 · THE ASSUMPTION** (49) — When people hear there's an AI tutor inside a textbook, they assume we fed the book to the AI and it learned it. That is not what happens. Nothing is trained on the textbook. There is no training run, and no model of our own anywhere in this project.

**B02 · OFF THE SHELF** (42) — The model we use is OpenAI's, off the shelf — the same one anybody can rent. It never changes. It doesn't know our books, and it never will. So how does it answer a question about chapter twelve? It looks it up.

**B03 · THE SEARCH** (37) — Here's the real sequence. A student asks a question. Before that question reaches the model that writes the answer, the system searches the textbook and pulls out the handful of passages most relevant to what was asked.

**B04 · OPEN BOOK** (45) — Then it sends both things together: the question, and those passages. So the model isn't remembering the book. It's handed the relevant pages at the moment it's asked, and it answers from what's in front of it. It's an open-book exam, not a study session.

**B05 · YOU CAN FIX IT** (42) — This sounds like a workaround. It's actually the better design, for three reasons. First: you can fix things. Correct a mistake in chapter twelve and the tutor is corrected too. If it had been trained, you would have to train it again.

**B06 · IT CAN CITE** (36) — Second: it can cite. Because the answer came from specific passages, the tutor can point at the section it got them from. A trained model can't. It just knows things, and you can't check where from.

**B07 · THE COST** (36) **[PROTECTED — the detail people repeat]** — Third: it's dramatically cheaper. Renting a model per question costs about a cent. Running our own would need a GPU server on all day — hundreds of dollars a month, before anyone asked a single question.

**B08 · THE CATCH** (37) — There is one catch worth knowing. That search only works because the textbook was indexed ahead of time — catalogued, so it can be searched quickly. By default, that index is rebuilt whenever the book is built.

**B09 · THE SILENT FAILURE** (48) — But if the content changes and the index doesn't get rebuilt, the tutor keeps answering from the old version. Confidently. With no error and no warning. So if a tutor ever seems to be describing a chapter that no longer exists — that's the first thing to check.

**B10 · CLOSE** (54) — So, the short version: nothing is trained. The tutor searches the book, takes the relevant pages, and answers from those. Which means it stays correct as the book changes, it can show you where it got something, and it costs cents instead of hundreds. That's the trade we made, and it's the right one.

**B11 · VERDICT** (45) — Let's recap with Claude. Nothing is trained on the textbook. The system searches the book and hands the model the relevant passages along with the question. That's why a fix to the content fixes the tutor, why it can cite, and why it costs cents.

**B12 · HANDOFF** (98) — Your turn. Take this into Claude: My product answers questions about a document set by looking passages up at question time instead of training on them. Walk me through what that buys me and what it costs — especially how I stop the search index drifting out of step with the content, and how I'd tell whether an answer came from my documents or from the model's own prior knowledge. That second half is the one worth pushing on. A lookup system that quietly falls back on what the model already knew looks exactly like one that's working.

**B13 · OUTRO** (8) — Lookup, Not Training. For Chaitanya and Humanitarians AI.

**Total:** 617 words · estimated 230s (~3:50) at Bella's measured 2.68 words/sec.
Real measured durations replace this at audio lock.

---

## VERDICT

Reviewed by the author (Chaitanya) on 2026-10-01 against the narration in §7 and the
flags in §6. Signed as written — the 16:9 keeps its ~3:50 runtime, with one instruction
attached:

> *"sign it and make short below 3 min"*

The 9:16 short is therefore built to land **under 180s** (YouTube's Shorts cap is itself
3:00, so this is the cap with headroom, not a looser target). Scene 3's cost beat (B07)
is `--keep`-protected in that cut and is not a candidate for dropping.

Open item 6.1 (the reindex trigger, unconfirmable against code on this machine) was put
to the author and closed with the conservative phrasing: narration keeps **"by default"**,
and the open item stays logged in `SOURCES.md` for re-check if a book repo becomes
available.

VERDICT: PASS
