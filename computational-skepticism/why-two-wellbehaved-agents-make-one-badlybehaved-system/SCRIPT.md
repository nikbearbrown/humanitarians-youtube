# Script: Why Two Well-Behaved Agents Make One Badly-Behaved System

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "5% of the time?", corrects to "a third of its runs?".
**Narration**:
"Agent A errs two percent of the time. Agent B errs three percent. Naturally, we expect their combined pipeline to fail about five percent of the time. But in practice, it can fail on a third of its runs. Let's see why."

## B01 — stakes (The Isolated Benchmark)
**Visual**: Manim `B01Scene`. Benchmark test cards: Agent A (98% accuracy) and Agent B (97% accuracy) running isolated unit tests.
**Narration**:
"Suppose you build an autonomous pipeline. You test Agent A alone on ten thousand records: ninety-eight percent accuracy. You test Agent B alone: ninety-seven percent accuracy. Both benchmarks look pristine."

## B02 — stakes (The Deployment Shock)
**Visual**: Manim `B02Scene`. Chained pipeline: Agent A extracts data → Agent B plans action → 30% system failure rate in terracotta.
**Narration**:
"You chain them together in production. Agent A extracts data from raw files, and Agent B formulates actions from those summaries. But when you monitor the live system, nearly thirty percent of customer tasks fail."

## B03 — anchor planted (The Relay Chain)
**Visual**: Manim `B03Scene`. THE ANCHOR: A three-stage relay chain [Agent A] → [Handoff Document] → [Agent B] → [System Output].
**Narration**:
"To understand this collapse, look at the pipeline as a relay chain. Agent A passes an intermediate document to Agent B, which passes an execution plan to the world. The entire system hinges on what happens during that handoff."

## B04 — wrong guess (The Addition Fallacy)
**Visual**: Manim `B04Scene`. Naive independent probability model: P(fail) ≈ 2% + 3% = 5%. 95% green success bar.
**Narration**:
"Intuition tells us errors should simply add. If Agent A has a two percent chance of slipping, and Agent B has a three percent chance, independent probability says about ninety-five percent of runs should succeed."

## B05 — break it (Falsifying Independent Coin-Flips)
**Visual**: Manim `B05Scene`. Striking down the addition model: Agent B's input is NOT clean ground truth; it is conditioned on Agent A's output.
**Narration**:
"That arithmetic assumes agents are independent coin flips on clean, isolated inputs. But Agent B is not acting on clean input. Agent B receives Agent A's output as its unverified reality."

## B06 — mechanism: accumulate (The Subtle Upstream Seed)
**Visual**: Manim `B06Scene`. MANIM MOVE `accumulate`: Document created by Agent A. One single red error block: "Delivery: Friday -> Sunday".
**Narration**:
"Watch what happens inside the handoff document. On two percent of runs, Agent A makes a minor, plausible error—say, shifting a delivery date or dropping a constraint. To Agent A, it is one misplaced token."

## B07 — mechanism: accumulate (Downstream Conditioning)
**Visual**: Manim `B07Scene`. MANIM MOVE `accumulate`: Agent B reads the document. 3 new red error blocks spawn from the single premise error.
**Narration**:
"Now Agent B takes over. Agent B has no memory of the original source text and no reason to doubt the document. It conditions on Agent A's error as absolute ground truth, actively reasoning around the false premise."

## B08 — mechanism: accumulate (Error Cascades)
**Visual**: Manim `B08Scene`. MANIM MOVE `accumulate`: Errors snowball into 7 red blocks: wrong schedule, cancelled orders, false alerts.
**Narration**:
"The error multiplies. From that single false date, Agent B generates conflicting schedule bookings, cancels valid orders, and issues false emergency alerts. One minor upstream slip accumulates into complete downstream chaos."

## B09 — anchor payoff (The Interaction Term)
**Visual**: Manim `B09Scene`. THE ANCHOR PAYOFF: Isolated Benchmark (98% / 97%) vs Relay System (30% Failure). "The Interaction Term".
**Narration**:
"This is why per-agent benchmarks are blind. In isolation, each agent was tested on pristine, valid data. In the relay chain, Agent B operates in an out-of-distribution state created by Agent A. Per-agent validation cannot see the interaction term."

## B10 — one flag (Deterministic Schemas vs Generative Context)
**Visual**: Manim `B10Scene`. THE ONE FLAG: Schema validation (exception thrown, stops cascade) vs Generative context (rationalization, accelerates cascade).
**Narration**:
"One flag—how rapidly errors compound depends on the interface. In rigid pipelines with typed schemas, an invalid upstream value throws an immediate exception. But in generative agent workflows, downstream models hallucinate plausible justifications for bad premises, supercharging the cascade."

## B11 — direction A (Isolation Guarantees Nothing)
**Visual**: Manim `B11Scene`. Direction A: "99% PER-AGENT ACCURACY" struck through in terracotta → "UNCHECKED RELAY COLLAPSE".
**Narration**:
"So validating individual agents to ninety-nine percent accuracy guarantees almost nothing about the safety of their pipeline, if intermediate handoffs pass unchecked natural language."

## B12 — direction B (Boundary Invariants Protect)
**Visual**: Manim `B12Scene`. Direction B: "BOUNDARY INVARIANTS" between nodes. Verifying contracts against ground truth.
**Narration**:
"And yet the fix is not to abandon agent chains. It is to place explicit boundary invariants between them—validating handoff contracts against ground truth rather than trusting the upstream agent's word."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"Downstream agents treat upstream outputs as ground truth, so errors do not add—they compound."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take a multi-agent workflow in your stack where Agent B acts on Agent A's output. Inject a subtle, plausible error into Agent A's handoff document—a shifted date, a flipped polarity, or an omitted constraint. Run Agent B on that corrupted input. Does Agent B flag the anomaly, or does it elaborate on the false premise? Audit how your pipeline handles upstream errors before chaining your next agent. Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Why Two Well-Behaved Agents Make One Badly-Behaved System. Liam, in for Bear."
