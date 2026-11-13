# Beat Sheet (APPROVED — Gate P, 2026-10-02): "Tokenization: Why AI Can't Count the Letters in Its Own Words"

**Creator:** Sai Pranavi J. | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly work report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as this fellow's
prior STEM videos)
**Phase:** 2 — approved for narration lock / audio generation. Worked example kept fully generic.
See `FACTCHECK.md`.

---

## Premise

**What this covers:** a reusable 3-question rubric — "Is it a whole-word task? / Does it need
character-level detail? / Would spelling it out first help?" — for predicting when a language
model will struggle with a task, built on one real, well-known mechanism: models don't read text
letter by letter, they read it in chunks called tokens, and a single word is often split into
several tokens that don't line up with its actual letters. Teaches the mechanism before any
example, walks it through the famous "how many r's in strawberry"-style worked example, stress-
tests it against a case where the same model handles character-level detail just fine (when asked
to spell the word out first), and closes on a concrete task the viewer can run today.

**What this deliberately avoids:** this is not a report of the fellow's own engineering work, and
does not benchmark or name any specific real model's tokenizer. The worked example illustrates a
widely-known, generic class of behavior, not a claim about one product's current performance
(tokenizers and model behavior change between versions).

**Source status:** general AI/STEM topic explainer. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B03 Mechanism | A word visibly split into token chunks that don't match its letters | Must be shown as a real segmentation, not just asserted |
| B04 Worked example | The word broken into its actual token pieces, each piece's letters tallied separately, vs. the real total | Both the token-level tally and the true answer visible together |
| B05 Falsifiability | The same word spelled out letter-by-letter first, then counted correctly | Visibly different resolution from B04 — the fix, not just the bug |
| B06 Task | The 3 questions restated as a checklist | Actionable, not just a restatement of the framework |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "Tokenization: Why AI Can't Count the Letters in Its Own Words" +
@HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:20)**
VO: "Hi, I'm Sai Pranavi J.. This video is about why AI models mess up tasks like counting
letters or finding rhymes, even though they can write whole essays correctly, and the one
mechanism that explains it."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:20–0:34)**
VO: "Ask a language model how many times the letter R appears in a word, and it'll often get it
wrong. Ask it to write a convincing essay on the same topic, and it's fine. Same model. Wildly
different reliability."
Visual: two task cards side by side — "Count letters: often wrong" and "Write an essay: reliable."

**B03. Mechanism (~0:34–1:00)**
VO: "Here's why. The model doesn't read text one letter at a time. It reads chunks called tokens —
sometimes a whole word, sometimes a word broken into a few pieces. A long or unusual word can get
split in a way that has nothing to do with where its letters actually fall. The model sees the
chunks. It never directly sees the letters inside them."
Visual: a word visibly split into 2-3 colored token blocks, with a caption: "model sees these
chunks, not the letters inside."

**B04. Worked example (~1:00–1:28)**
VO: "Take a word broken into three token chunks. Ask the model to count a specific letter across
the whole word, and it has to reconstruct the letters from chunks it never saw as individual
characters. It's not lazy. It's working from the wrong unit entirely, and the count comes out
wrong."
Visual: the word's real token split shown, with the model's (incorrect) tallied count next to the
true, correct count — the mismatch visible side by side.

**B05. Falsifiability case (~1:28–1:50)**
VO: "Now the fix that proves the mechanism. Ask the same model to first spell the word out, one
letter at a time, separated by dashes. Now every letter is its own token. Ask it to count again,
and it gets it right. Nothing about the word changed. Only the unit it was working in did."
Visual: the same word, now spelled letter-by-letter with dashes between each character, the count
now matching the true total — a green checkmark replacing B04's red mismatch.
*[Stress-tests the mechanism — same model, same word, different token granularity, different
reliability.]*

**B06. Scaffolded task (~1:50–2:10)**
VO: "Here's something to try today. Pick a long or unusual word. Ask an AI model to count a letter
in it directly. Then ask it to spell the word out first, one letter at a time, and count again. If
the second answer is more reliable than the first, you just watched tokenization in action."
Visual: the 3 questions restated as a checklist card (whole-word task? / needs character-level
detail? / would spelling it out help?).

**B07. Takeaway (~2:10–2:24)**
VO: "A model that writes fluent paragraphs and a model that can't count letters in a word aren't
contradicting each other. They're the same system, working at the wrong resolution for the task
you gave it."
Visual: statement card.

**B08. Sign-off (~2:24–2:29)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] Mechanism (B03) shown as a real token split, not just asserted in narration
- [ ] B04's token-level tally and the true count both visible together, mismatch clear
- [ ] Falsifiability case (B05) uses the same word, same model, only the spelling-out changes —
      not a different, easier word
- [ ] Scaffolded task (B06) is a concrete action, not a restatement of B03
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] No specific real model/vendor named or benchmarked

**Estimated runtime:** ~2:29 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — not yet run, pending this beat sheet's approval).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-10-02. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
