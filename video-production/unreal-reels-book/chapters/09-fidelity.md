# Chapter 9 — Fidelity

## Overview

There are three quality bars, and they are not equal. An expert will forgive a rough visual, a plain slide, a voice that lands a little flat. They will not forgive a false statement. So the bars stack in a fixed order: **accuracy first, no-obvious-errors second, watchability third.** A beautiful lecture that misattributes an equation is worse than an ugly one that gets it right, because the ugliness is cheap to fix by eye and the falsehood is not. Fidelity is the top bar, and this chapter is about the one machine check that guards it.

The key move is to notice *what* we are checking against. Our lecture is not a fresh essay conjured from a model's priors — it sits downstream of a real, authored, already-fact-checked book. The narration expands the chapter's own prose; the figures are the chapter's own figures. So we are not fact-checking against the world. That would be the wrong, expensive, un-winnable task. We are checking something narrower and fully tractable: **did the narration stay faithful to the chapter it was built from?** The book already did the hard part. Our job is to catch the spine drifting away from it.

That reframing is what makes fidelity a *checkable* property rather than an aspiration. A model asked to "be a physicist" produces plausible slop. A model asked to "faithfully stage this physicist's chapter" can be audited line by line, because there is a ground truth sitting right there in `chapter.md`. The grounding check is that audit, run automatically, before render.

What it produces is not a verdict on truth — the machine never decides truth — but a **triage list**. A ten-minute lecture yields a handful of flags, not a transcript to re-read. That handful is what a human expert opens: "here are the four claims I could not verify against your chapter, and the two the commons says are contested." A gate that reviews six flagged items per chapter is a gate that 150 volunteers can actually staff. That is the whole point.

## The two tiers

The grounding check grades every claim-bearing narration sentence on two tiers, cheapest first.

**Tier A — is the claim in the source chapter?** This is the anti-hallucination gate, and it is the one that matters most. For each declarative sentence in the narration, `grounding_check.py` asks whether the source `chapter.md` supports it — a token-overlap-and-prefix-window check against the normalized chapter text. A claim that lives in the chapter is safe. A claim that does *not* is a candidate fabrication: the narration invented something the book never said. Tier A catches exactly the failure that a downstream-of-a-book design is supposed to make impossible, and confirms it stayed impossible.

The claim extractor is deliberately greedy. A missed claim is a missed hallucination, so it treats every declarative sentence as a candidate unless it is clearly a teaching aside — a question, or an imperative framing move like "notice that…" or "imagine…". Over-collecting is safe: a non-claim just matches the chapter and grades as grounded. Under-collecting is not, because an actively-phrased fabrication would slip through silently. Recall first, always, on the anti-hallucination gate.

**Tier B — does the shared fact commons corroborate it?** This is the layer on top. The claim is matched against `facts/<domain>/facts.json` (and the glossary in `terms.json`), and the check reads the fact's *earned* status — it never re-decides it. The table it consults:

A commons status of `verified` or `agreement` means the claim is corroborated by a human sign-off or by two-plus independent sources — safe, and a not-in-chapter claim can even be promoted to a sanctioned `elaboration`. `unverified` is a single-source candidate — weak, noted but not trusted. `conflict` means the commons already knows the claim is contested, which becomes a hard **FLAG** for the expert to adjudicate. And *no match* means the commons is simply silent, so we fall back to Tier A.

The most interesting cell in that table is the one that seems contradictory: a claim that **is in the chapter but is `conflict` in the commons.** That is the case where the book itself may be wrong or dated. The check surfaces it; it does not resolve it. Faithfully staging a chapter that has an error is still faithful staging — but the expert deserves to know the commons disagrees with their source.

## What comes out: grounding.json and the flags list

The check writes `grounding.json` into the lecture folder. It carries a full per-claim verdict table for the record, and — the thing the professor actually opens — a **flags list**: for each flagged claim, its `beat_id`, the offending sentence, the verdict, the reason, and the matched fact. The verdicts partition into `unverifiable`, `contested`, `review`, and `grounded` (plus the promoted `elaboration`).

Only the flags demand attention. `unverifiable` means not in the chapter and no commons match — a possible hallucination. `contested` means the commons marks it a conflict — the expert must adjudicate. `review` means weak or uncertain support — a spot-check. Everything graded `grounded` disappears from view, which is why the list stays a handful and not a transcript.

Those counts feed a **fidelity axis** into `qc_report.json`, weighted above watchability. This is the mechanical enforcement of the priority order: a chapter with unverifiable or contested claims is not "watchable-draft" no matter how clean its render. The verdict reads *"fidelity: N unverified claims, M mechanical errors"* — the professor's actual triage list — rather than the old, weaker "watchable-draft," which scored only whether the thing rendered.

## The commons the check leans on

Tier B is only as good as the commons behind it, so it is worth knowing how that commons earns trust — because the same discipline governs where a model is allowed to act anywhere in this system.

The extraction is **deterministic**: ordinary Python parses a source dump with regular expressions, so the same input yields byte-identical output. No language model writes any fact. Sources are **tiered** — `trusted` (OpenStax, vetted textbooks), `solid` (PubMed, journals, Wikipedia), and `low` (general web, and *every* AI model). AI is permanently low-tier: a candidate, never an authority, by construction rather than by policy we hope holds. Consensus is **derived, never declared**: one source is `unverified`, two-plus independent sources are `agreement`, any refutation is `conflict`. "Independent" is enforced — a `same_publisher` flag stops two OpenStax books from counting as two votes. And **only a human reaches `verified: true`**, by signing off with a SHA-256 hash over the exact canonical text. Edit the fact and the hash no longer matches, so the signature auto-invalidates; an expert's name never rides on content they did not approve.

The same rule confines the model inside the grounding check. Matching a paraphrase to a fact is recall-hard, and lexical similarity under-recalls, so the deterministic pass does the cheap high-precision work and emits a **near-miss band** (roughly `0.45 ≤ score < 0.62`) for an *optional* LLM adjudicator. That adjudicator **flags, never decides.** The model is a proposer and a flagger, everywhere and always. It is never in the seat of authority.

## Correction writeback: the loop that builds a commons

Here is the part that turns a chore into infrastructure. When the professor triages a flag and fixes a claim — "that definition is wrong, it's X" — the edit is not just local text. `record_correction.py` writes it back to the commons as **trusted-tier, human-authored, signable evidence** (through the same `facts.py` helpers, so there is one source of truth for matching and consensus).

Two cases. If the correction *refutes an existing fact*, the script appends a `REFUTES` record to the old fact — recomputing it to `conflict` and pushing it onto the review queue — and enters the corrected canonical as a trusted candidate. If it is a *novel claim* the commons lacked, it enters straight from the book with the expert as source. Either way, because a human authored it, it can be signed: `verified: true`, hash-pinned. Every writeback records provenance — expert id, book, chapter, and the `beat_id` that triggered it — so any fact traces back to the lecture edit that produced it.

The consequence is quietly large. The 150 experts refining 150 lectures are, as a byproduct, building a signed, cross-referenced fact commons. The spine reads the commons to catch its own drift; the expert's fixes flow back as verified evidence; the next lecture's Tier B is a little stronger. And the model never touches this path — corrections are human acts, by construction.

## Worked example

Take a physics lecture folder with a `beat_sheet.json` and run the check against the physics commons:

```bash
python skills/shared/grounding/scripts/grounding_check.py reels/relativity-ch3 \
    --facts-dir /path/to/facts --domain physics --chapter chapter.md
```

Suppose the narration has three claim-bearing sentences. Two are textbook definitions lifted faithfully from the chapter; the check finds them in `chapter.md` (Tier A) and matches real facts at score 1.0 in the commons (Tier B) — both grade `grounded+corroborated` and never surface. The third says something like "warp fields let matter exceed lightspeed." It is absent from the chapter, and its best commons match scores 0.27 — a miss. Verdict: `unverifiable — possible hallucination`. It lands on the flags list with its `beat_id`.

The professor opens `grounding.json`, sees one flag, and adjudicates it: the chapter never claimed that; the narration invented it. They cut the sentence — and if the corrected framing is worth keeping in the commons, they run `record_correction.py` with `--sign`, and the fix becomes signed evidence carrying the `beat_id` that triggered it. One flag reviewed, one hallucination caught, one signed fact added. That is the gate working as designed: cheap, sharp, and never fully automated.

## Exercises

**Exercise 9.1 — Run the grounding check.** Take any lecture folder with a `beat_sheet.json` and a source `chapter.md`, and run `grounding_check.py` against a matching domain in `facts/`. Report the four fidelity counts and how many claims were checked. (Artifact: the generated `grounding.json` plus the printed summary line.)

**Exercise 9.2 — Judge a flag.** Pick one flagged claim from your `grounding.json` and adjudicate it as the professor would: is it a real hallucination, a heavy paraphrase of a true chapter claim that lexical Tier A missed, or an in-chapter claim the commons marks contested? Say what you would do — cut it, keep it, or write a correction. (Artifact: the flag, your verdict, and one sentence of reasoning.)

**Exercise 9.3 — Trace the writeback.** Read `record_correction.py` and describe, for a correction that refutes an existing fact, exactly what changes in `facts.json`: what happens to the old fact, what the new fact looks like, and what the SHA-256 signature is computed over. Explain in one line why editing a signed fact later invalidates the signature. (Artifact: your trace of the two-fact change plus the one-line signature explanation.)
