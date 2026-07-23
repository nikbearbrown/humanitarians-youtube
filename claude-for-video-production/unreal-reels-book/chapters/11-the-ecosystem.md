# Chapter 11 — The Ecosystem

## Overview

Until now this book has treated Unreal Reels as a thing you point at a chapter to get a video. That framing is useful, and it is incomplete. The video pipeline is one organ inside a larger body — a factory that writes books, keeps facts, and makes films, all governed by a single philosophy. Once you see the whole animal, the reels stop looking like a clever standalone toy and start looking like the last stage of an assembly line whose earlier stages have already done most of the hard work.

That philosophy is stated the same way everywhere it appears. Be deterministic where you can. Treat the model as a low-tier proposer, never an authority — it drafts, it suggests, it stubs, but it does not decide. Keep a human as the sole authority, the one who signs. And put provenance on everything, so that any artifact can tell you where it came from and who vouched for it. This is not three principles bolted onto three projects. It is one sentence that the whole factory recites — in the book generator, in the fact commons, and in the video spine alike.

Three systems chain together to make that sentence true. **AI+1** (the `ai1-cli` tool) writes the book through seven human-gated phases. **`facts/`** is the shared truth spine that every phase queries and every book carries. **Unreal Reels** makes the video from finished chapters. They are joined at the seams by small bridges — a fact dictionary synced into each book, a `vids/_chapters.json` manifest that nominates chapters for video, a sidecar format that lets a lecture pass the same gates a chapter does.

The realization worth carrying out of this chapter is quiet but load-bearing: a lecture spine sits *downstream* of a chapter that has already passed fact-check. So the video's burden is not truth. Truth was settled upstream. The video's only job is fidelity — did the narration stay faithful to a chapter someone already verified. That is a smaller, more checkable task, and it is what makes turning 150 books into videos a governable operation rather than a hope.

## AI+1 writes the book, and the +1 is a person

`ai1-cli` builds a book through seven phases, each ending in a gate that a human signs before the next phase may begin: **Blueprint → Research → Draft → Human Rewrite → Fact Check → Images → Check-Images.** A drafted-but-unresearched chapter is worse than no chapter, so the gates are hard stops, in order, never waved through.

The name is the mechanism. "AI+1" means one human plus AI agents making a book neither could make alone. The AI does the typing — research, drafting, fact-lookup, figure generation, builds, audits. The "+1," the human, does what cannot be delegated: deciding what the book *is*, rewriting it until it carries their voice, and signing every gate. The +1 is not a reviewer bolted onto a pipeline. The +1 is the reason the output is a book and not a pile of fluent text.

One gate makes this concrete. **GATE 3 — Human Rewrite — can never be signed by an agent.** No exceptions, no autonomous mode, no "the model was confident." An agent may assist the rewrite, but the attestation that a human made the book theirs is an attestation only a human can honestly give. This is the hinge the whole factory turns on: agents propose, humans dispose, and the dividing line is drawn in signatures.

## facts/ is the shared truth spine

Every phase that touches a claim goes through `facts/` first. It is a fact dictionary — canonical, atomic statements with tiered sources, derived consensus, and a human sign-off flag — and the rule is that you check it *before* any external lookup. A claim never ships from the model's memory. New facts enter as `verified: false` and stay unauthoritative until a human signs them; a `verified: true` entry is never overwritten, only appended to; and conflicting sources are a hard block that only a human resolves.

The clever part is how `facts/` lives. The same code — `facts.py`, `extract-facts.py`, `facts-sources.yaml` — exists standalone *and* is synced into every AI+1 book, so each book stays self-contained while sharing one matcher, one consensus rule, one commons. Phase 1 (Research) populates it; Phase 4 (Fact Check) queries it before reaching for the web. By the time a chapter clears GATE 4, its claims have been checked against this spine and the checkable ones are sourced or removed.

## Unreal Reels makes the video, and the bridge is thin on purpose

The video system consumes finished chapters. The bridge between book and film is deliberately small: `higgsfield/` topic-scans chapters using the **FIELD** framework — Focus, Image, Exclusions, Load, Drive — and `vids/_chapters.json` records which chapters deserve a video and in which mode. Not every chapter earns a lecture; FIELD is the scorer that decides, so production effort lands where it pays.

Here the downstream realization does its work. When the lecture spine builds narration from a chapter, it is not fact-checking a video against the world. It is checking that the narration stayed faithful to an already-verified chapter. Truth was established at GATE 4; the video's job is fidelity. The grounding check's **Tier A** does exactly this — narration against source chapter — and its **Tier B** reuses the same `facts/` helpers, which is just AI+1's Phase 4 logic pointed at a script instead of a chapter. One commons, applied twice.

## Verified artifacts tie it together, and modes answer "how"

The glue is the sidecar. For any artifact `foo.md`, a `foo.md.verified.json` sits beside it recording whether a human has signed off, by whom, when, and — optionally — a sha256 of the artifact at signing so silent edits can be caught. The routing logic is uniform across the factory: verified sidecar → use the artifact, never regenerate; unverified sidecar → stop and say so; no sidecar → generate, stub the sidecar as `verified: false`, and stop for sign-off. Generation is the fallback, never the default.

Unreal Reels' `silent_run.py` now emits sidecars in exactly this AI+1 format, plus a lecture-local `STATUS.md` gate table. That single alignment is what promotes a lecture from a side pipeline to a first-class AI+1 artifact — it passes the same gates a chapter does. And crucially, the agent *authors* the plan and narration but **never signs**; a human runs `verify.py sign`, exactly as GATE 3 is human-only. Agents stub, humans sign.

That leaves one question: at fleet scale, who fills the LLM slots? The **three modes** answer it. In **agent** mode the agent is the model and fills the slot inline. In **API** mode the slot is emitted as a request for a keyed call. In **handoff** mode it is emitted as a prompt a human pastes elsewhere. The deterministic bookkeeping is identical in all three; only the LLM slot's plumbing changes. Finally, `SOURCE-MANIFEST.md` plus `sync-to-book.sh` propagate the canonical tooling downstream to all 150 books — canonical flows down, never back — so shipping silent-mode and grounding as canonical tooling deploys them across the whole fleet at once.

## Worked example — trace one claim, book to commons to video, and sign a gate

Follow a single claim through the factory. In Phase 1, a research pass adds a fact to `facts/facts.json` — say a physical constant with two Tier-A sources that agree. It enters `verified: false`, `consensus: "agreement"`. A human reads the evidence and signs it: `verified: true`. That is the commons doing its job.

In Phase 2 the chapter is drafted using that fact, not the model's memory of it. Phase 4 re-checks the drafted claim against `facts.json`, finds the verified entry, and uses it directly — no external lookup. The human signs **GATE 4**. The chapter now carries a `chapter.md.verified.json` marking it fact-checked.

Now the video. FIELD scores the chapter into `vids/_chapters.json` as a lecture candidate. `silent_run.py` drafts the narration, and the grounding check's Tier A confirms the narration's version of the claim is faithful to the verified chapter — same number, same claim, no drift. It stubs `narration.md.verified.json` as `verified: false` and **stops**. The agent has gone as far as it may. You, the human, read the narration against the chapter, confirm fidelity, and run `verify.py sign`. The sidecar flips to `verified: true`, and only now may the pipeline proceed to stills and video. You have traced one claim through three systems and signed the gate the agent could not.

## Exercises

**Exercise 11.1 — Map your own claim.** Pick one factual claim in a chapter you are turning into video. Write the path it takes: which `facts/` entry backs it, which gate verified it (GATE 4), and which grounding tier would check the narration against it. One paragraph, three named stages. (Artifact: a claim-trace paragraph naming the fact_id and the gate.)

**Exercise 11.2 — Read a sidecar and decide.** Given a `narration.md.verified.json` with `verified: false` and no `verified_by`, state what the pipeline must do next and why an agent may not sign it. Then given the same sidecar with a sha256 that no longer matches the file, state what that mismatch means. (Artifact: two short rulings, one per sidecar state.)

**Exercise 11.3 — Sign a gate.** Take a stubbed lecture artifact, read the narration against its source chapter for fidelity (not truth — truth was settled at GATE 4), and either sign it with `verify.py sign` or refuse and say what would have to change first. Write one sentence attesting what you verified. (Artifact: a signed sidecar or a written refusal, plus your one-sentence attestation.)
