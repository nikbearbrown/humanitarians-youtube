# Branding and AI — CLI Video Ideas ("X with Claude")

Lane: BUILD + RESEARCH (quantitative brand signal analysis, archetype classification, pipeline resilience, measurement design — BUILD; brand strategy analysis, signaling theory, case-study synthesis — RESEARCH)
Source book: `branding-and-ai/`
Generated: 2026-07-12

---

## Card 01 — Build a Signal Collapse Detector with Claude

**Source:** Chapter 1 (The Creative Engineer — Spence signaling theory, pooling equilibrium, Peng et al. 56%)
**Lane:** BUILD
**Hook:** A GitHub repo used to be a separating signal. Now 82% of developers use AI tooling, and the signal has pooled — everyone produces it, so it stops sorting.
**The artifact:** A CLI tool that takes a professional credential or portfolio artifact (e.g., "GitHub repo," "CS degree," "LinkedIn certification"), asks Claude to score it on signal strength across three dimensions — Cost to fake (1–5), Population saturation (1–5), Still separating vs. pooling (Separating/Pooling/Collapsed) — then plots a 3×3 signal health matrix and recommends the next costly signal that would restore separation.
**Prompt seed:** "You are a signaling theory analyst using Spence's model. Given this credential or portfolio artifact: [ARTIFACT] in this professional context: [FIELD/YEAR]. Score on: (1) Cost to fake (1=trivially cheap, 5=requires months of genuine effort), (2) Population saturation (1=rare signal, 5=produced by 80%+ of candidates), (3) Status: Separating (still reliably distinguishes high-productivity candidates) / Pooling (everyone produces it, signal noisy) / Collapsed (the credential provides essentially no employer information). Then recommend one costly signal in this field that is still separating, with a rationale grounded in Spence's mechanism."
**Read / check:** Run with "GitHub repo" in software engineering 2024. Verify: Cost to fake scores ≤2 (AI tooling reduced it dramatically), Population saturation scores 5 (82% from Stack Overflow), Status = Collapsed — matching the Ch. 1 analysis and the Peng et al. result.
**Human supplies:** Their own credentials/portfolio artifacts from their field; context on the current year and hiring market they are in.
**Output medium:** Screen-rec mp4 — artifact in, signal health matrix printed as an ASCII table, recommendation printed below.
**The change:** Before: investing in credentials that feel prestigious but have pooled. After: an explicit signal-health score that shows which artifacts still separate and where to invest instead.
**Teardown angle:** The separating-vs-pooling equilibrium — a signal works only as long as its cost-structure holds; when AI tooling collapses the cost of producing it, the signal stops sorting and the candidate is back to guessing.
**Exclusions:** Do not frame specific credentials as universally "bad" — signal value is context-specific and changes over time; the tool is a diagnostic, not a verdict.
**Score:** 9/10

---

## Card 02 — Build a Brand Archetype Classifier with Claude

**Source:** Chapter 5 (Brand Archetypes as a System — 12 archetypes, shadows, forcing function)
**Lane:** BUILD
**Hook:** An archetype is not a style guide — it is the constraint that makes every downstream brand decision decidable. Without it, every choice is arbitrary.
**The artifact:** A five-input archetype classifier: the user provides (1) a mission statement, (2) three adjectives their audience uses to describe them, (3) one product decision they are proud of, (4) one headline/tone example from their own work, (5) their primary competitor. Claude maps these to the Mark & Pearson 12-archetype system, selects the primary archetype and one shadow risk, explains the forcing function (how the archetype makes downstream decisions decidable), and flags any archetype drift signals from the five inputs.
**Prompt seed:** "You are a brand archetype analyst using the Mark and Pearson 12-archetype system (Innocent, Sage, Explorer, Hero, Outlaw, Magician, Everyman, Lover, Jester, Caregiver, Creator, Ruler). Given: Mission = [MISSION], Audience adjectives = [ADJ1, ADJ2, ADJ3], Product decision they are proud of = [DECISION], Tone example = [HEADLINE], Primary competitor = [COMPETITOR]. Identify: (1) Primary archetype with a one-sentence rationale grounded in at least two of the five inputs. (2) Shadow risk: the specific failure mode embedded in this archetype and one example of a brand that drifted into it. (3) Forcing function: name three downstream decisions (copy tone, visual palette, feature prioritization) that this archetype now makes decidable. (4) Drift signals: flag any of the five inputs that point toward a different archetype, indicating mixed identity."
**Read / check:** Run with Tropicana's inputs. Verify the classifier identifies Innocent archetype, shadow = denial of bad news, and flags the 2009 packaging redesign as archetype drift — matching the Ch. 5 analysis.
**Human supplies:** The five inputs from their own brand or a brand they are analyzing — must be real, not hypothetical, so the drift signals are grounded in actual behavior.
**Output medium:** Screen-rec mp4 — five inputs entered interactively, archetype classification + shadow + forcing function + drift signals printed in a structured four-section report.
**The change:** Before: vague brand identity that produces inconsistent copy, visuals, and product decisions. After: a committed archetype that makes every downstream choice a filter — does this fit the archetype? — instead of an open debate.
**Teardown angle:** The Tropicana case from Ch. 5 — the recognition asset is invisible until it is destroyed; archetype drift is how well-funded companies accidentally destroy what was working.
**Exclusions:** Do not present the classification as fixed or permanent — archetypes can evolve with deliberate repositioning; the classifier is a current-state diagnostic, not a permanent label.
**Score:** 9/10

---

## Card 03 — Build a Brand Metrics vs. Performance Metrics Dashboard Plan with Claude

**Source:** Chapter 13 (Measuring Brand Equity — brand vs. performance metrics split, the patience gap, NPS limits)
**Lane:** BUILD
**Hook:** A discount campaign looks like a success on Monday's dashboard and looks like margin erosion in the brand tracking study six months later — because the two metric families answer different questions and most teams only watch one.
**The artifact:** A measurement plan generator: the user describes a brand (stage, audience, recent marketing activity), Claude produces a dual-track measurement plan — (1) Brand metrics track (unaided awareness, consideration, preference, association strength, sentiment — each with measurement method, cadence, and the question it answers), (2) Performance metrics track (conversion, CAC, ROAS, retention — each with measurement method, cadence, and the question it answers) — plus a "patience gap" estimate (when to expect brand investment to convert to performance movement) and three specific NPS limitations that apply to this brand.
**Prompt seed:** "You are a brand measurement architect. Given this brand: [BRAND DESCRIPTION] (stage, audience, recent marketing). Design a dual-track measurement plan: (1) Brand metrics: for each of unaided awareness / aided awareness / consideration / preference / association strength / sentiment — name: measurement method (survey type, panel size, frequency), what question it answers, and what movement in this metric means for brand equity. (2) Performance metrics: for conversion / CAC / ROAS / retention — name: measurement source, what question it answers, and one case where this metric moves in the wrong direction without reflecting brand damage. (3) Patience gap: estimate how many months before brand investment in this stage/category should produce measurable performance movement. (4) NPS limits: name three specific ways NPS would mislead this brand."
**Read / check:** Run on a mid-stage DTC brand that recently ran a deep-discount campaign. Verify the plan flags the discount as a brand-metric risk (price premium erosion, loyalty-to-sale training) even if performance metrics showed short-term conversion lift — matching Ch. 13's explicit warning.
**Human supplies:** A two-paragraph description of their brand (or a brand they are advising) — stage, audience, recent campaign type, and current measurement setup.
**Output medium:** Screen-rec mp4 — brand description in, dual-track plan printed with clear section headers, patience gap estimate highlighted, NPS limits as a numbered list.
**The change:** Before: weekly dashboard shows performance metrics only; brand metrics are tracked "when we have time." After: a formal dual-track plan with separate cadences, where each metric is named alongside the question it actually answers.
**Teardown angle:** The Pepsi/Kendall Jenner case from Ch. 13 — awareness went up, favorability went down, consideration fell; any single number extracted from a multidimensional brand asset answers one question while leaving the others open.
**Exclusions:** Do not present brand tracking as requiring a large budget — unaided awareness and consideration can be measured with small panel surveys; the plan should include a low-budget implementation option.
**Score:** 9/10

---

## Card 04 — Build a Pipeline Contract Resilience Audit with Claude

**Source:** Chapter 21 (Pipelines and Workflow — Apollo/Reddit case, chain of contracts, three survival disciplines)
**Lane:** BUILD
**Hook:** Apollo wasn't a bad pipeline — it was excellent. What killed it was not the code. It was the contract. And damage flows downhill: the smallest, most dependent party absorbs everything.
**The artifact:** A pipeline dependency audit tool: the user lists all external services/APIs their product depends on, Claude maps each as a contract with four fields — Shape (input/output format), Cost (pricing model), Rate Limit, Terms of Service governance — classifies each as LOW / MEDIUM / HIGH dependency risk, flags any with a single-dependency failure mode (like Apollo's single Reddit API dependency), and writes a fallback "degraded mode" design for the two highest-risk contracts.
**Prompt seed:** "You are a pipeline resilience auditor. Given this list of external services/APIs my product depends on: [SERVICE LIST]. For each service: (1) classify the contract terms — Shape (fixed vs. versioned API), Cost (fixed/usage-based/ad valorem), Rate Limit (generous/constrained/restrictive), ToS Governance (stable open terms vs. discretionary/frequently revised). (2) Rate dependency risk: LOW (easily replaced, stable terms), MEDIUM (replaceable but costly, moderate term volatility), HIGH (no good substitute, terms can change with short notice). (3) Flag any single-dependency failure mode — if this service changes its terms, does your product fail completely? (4) For the top two HIGH-risk services: write a 'degraded mode' design — what does the product do when this contract breaks, and how does the user experience change?"
**Read / check:** Run on a product with the Reddit API as a core dependency (replicate the Apollo scenario). Verify: Reddit API classified as HIGH risk (no viable substitute at scale, pricing change with 90-day notice), single-dependency failure mode flagged, degraded mode = read-only cached content with no new post ingestion — matching Ch. 21's analysis.
**Human supplies:** A list of 5–10 external services/APIs their product uses (real product preferred); must include at least one service they have never built a fallback for.
**Output medium:** Screen-rec mp4 — service list in, dependency audit table printed (service × four contract fields × risk rating), two degraded-mode designs printed below.
**The change:** Before: "our pipeline works, we reviewed the code." After: an explicit contract map where each external dependency has a risk rating and the two highest-risk dependencies have a named fallback before the service breaks.
**Teardown angle:** The Apollo asymmetry from Ch. 21 — damage flows to the smallest party; Reddit absorbed diffuse reputational spread, Apollo absorbed concentrated product-killing damage. The builder's job is to survive the day the upstream party changes its terms.
**Exclusions:** Do not present the degraded mode design as a substitute for contractual negotiation where possible — for high-revenue products, negotiating rate caps or enterprise API agreements is preferable to designing around a failure that negotiation could prevent.
**Score:** 9/10

---

## Card 05 — Build a Madison Multi-Agent Architecture Mapper with Claude

**Source:** Chapter 3 (The AI Toolchain — four meanings of agent, five Madison roles, mega-agent vs. specialized-roles comparison)
**Lane:** BUILD
**Hook:** Same frontier model, opposite products: Cursor makes senior developers faster, Devin runs tasks while you sleep. The difference isn't the model — it's where the seams are.
**The artifact:** A CLI architecture mapper: the user describes an AI product they are building or evaluating, Claude maps it against the four agent meanings (function-with-prompt / ReAct loop / autonomous-over-horizon / specialized-role-in-pipeline), classifies which meaning(s) it instantiates, then applies the five Madison role model — identifying which of the five roles (Intelligence / Content / Research / Experience / Performance) the product instantiates and which are absent — and outputs a failure-locatability assessment (can you find where the failure is when the system gives wrong output?).
**Prompt seed:** "You are an AI system architecture analyst. Given this AI product description: [PRODUCT DESCRIPTION]. Step 1: classify which of the four agent meanings this product instantiates: (A) function-with-prompt, (B) LLM with tools and a ReAct loop, (C) autonomous over a multi-step horizon, (D) specialized role in a larger pipeline — or a combination. Step 2: map the product against Madison's five roles — Intelligence, Content, Research, Experience, Performance — noting which roles are present, which are absent, and whether absent roles create blind spots. Step 3: failure-locatability assessment — when the system produces wrong output, can you identify which component failed? Rate: HIGH (failure is localized, named, fixable), MEDIUM (failure requires investigation across 2–3 components), LOW (failure is in a mega-agent and the location is structurally unknowable). Step 4: recommend one architectural seam that would improve failure locatability."
**Read / check:** Run on a description of a single-model marketing automation system with no separated roles. Verify: classified as meaning A/B, zero Madison roles explicitly present (all merged), failure-locatability rated LOW with the mega-agent rationale from Ch. 3 — matching the chapter's three-failure-mode analysis (token costs, failure blur, no distinct thing to sell).
**Human supplies:** A description of an AI product they are building or evaluating — must include what it does, what external data it accesses, and how the output is used.
**Output medium:** Screen-rec mp4 — product description in, four-step analysis printed with failure-locatability rating highlighted and the seam recommendation in a final block.
**The change:** Before: "we built an agent that does X." After: explicit architecture classification showing which meanings and roles are instantiated, where failure locatability is weak, and one seam to add that would make failures findable.
**Teardown angle:** The Cursor vs. Devin comparison from Ch. 3 — same capability, opposite products, opposite brand positions, because architecture is a branding decision: the seam decides what customers can see, name, trust, and buy.
**Exclusions:** Do not present the five Madison roles as the only valid architecture — they are a specimen, not a universal template; the goal is to teach the skill of reading any multi-agent system for its seam placement and failure-locatability.
**Score:** 8/10

---

## Card 06 — Build a Four-Verb Career Signal Audit with Claude

**Source:** Chapter 1 (The Creative Engineer — Ideate / Build / Brand / Ship framework, the cheapened Build verb)
**Lane:** BUILD
**Hook:** Generative tools are excellent at producing solutions. Given a specification, they will build it. What they cannot do is decide whether the specification is worth building — and that is the verb that still carries career value.
**The artifact:** A four-verb portfolio self-audit: the user describes their three most recent projects, Claude scores each project on the four verbs (Ideate: did they identify the problem independently? Build: is the technical artifact present? Brand: is there a named, positioned identity? Ship: did it reach real users with a feedback loop?) — scores 0–3 per verb per project — then aggregates a personal verb profile showing which verb is strongest, which is weakest, and what type of next project would shift the profile toward all four.
**Prompt seed:** "You are a four-verb portfolio auditor using the Creative Engineer framework (Ideate / Build / Brand / Ship). Given these three projects: [PROJECT 1], [PROJECT 2], [PROJECT 3]. For each project and each verb: score 0 (absent), 1 (partial), 2 (present), or 3 (strong evidence) based on the project description. Rationale for each score in one sentence. Aggregate a verb profile: total score per verb across three projects (max 9). For the lowest-scoring verb: name one specific next project type that would produce a 2 or 3 score on that verb."
**Read / check:** Run on a portfolio of three AI projects where all three are technically implemented GitHub repos with no user testing and no named brand identity. Verify: Build scores 2–3 per project, Ideate / Brand / Ship score 0–1, and the lowest-verb recommendation is a project that requires talking to real users before writing any code — matching Ch. 1's explicit failure mode ("students pick a technology, build around it, then try to retrofit a user need").
**Human supplies:** Real descriptions of their three most recent projects (or portfolio items) — must include what problem it solved, how they decided to build it, and whether it reached real users.
**Output medium:** Screen-rec mp4 — three project descriptions in, per-project verb scorecard printed as a table, aggregate verb profile as a total-score bar, lowest-verb next-project recommendation in a final block.
**The change:** Before: a portfolio that demonstrates Build fluently but signals nothing about Ideate or Ship. After: an explicit verb profile that shows the gap between technical execution and the costly signals that still separate candidates.
**Teardown angle:** The signal collapse from Ch. 1 — Build is the cheapened verb; the costly signals that still separate are in Ideate (deciding what's worth building) and Ship (reaching real users with real feedback loops), neither of which can be prompted away.
**Exclusions:** Do not score Build at zero for AI-assisted projects — the verb is still present even if cheapened; the audit is about profile balance, not about penalizing AI use.
**Score:** 8/10

---

## Card 07 — Research: Archetype Drift Case Study — When a Brand Leaves Its Identity

**Source:** Chapter 5 (Brand Archetypes — Tropicana, Gap, New Coke failure cases, archetype drift mechanism)
**Lane:** RESEARCH
**Hook:** Tropicana didn't lose its recipe. Gap didn't close its stores. New Coke wasn't bad product. They lost their recognition asset — and that asset is invisible until it is destroyed.
**The artifact:** A comparative case study document: Claude synthesizes the three canonical archetype-drift cases (Tropicana 2009, Gap 2010, New Coke 1985) into a structured analysis — what archetype each brand held, exactly what changed (the triggering action), the customer response timeline, the revenue/equity impact, and the recovery move (if any) — then produces an abstracted "drift signature" framework: four warning signs that appear before a brand's recognition asset is destroyed.
**Prompt seed:** "Research the three canonical brand archetype-drift cases: Tropicana 2009 (packaging redesign), Gap 2010 (logo redesign), New Coke 1985 (formula change). For each: (1) What archetype did the brand hold before the change? (2) What specifically changed and how did it violate the archetype's recognition pattern? (3) What was the customer response timeline (days/weeks to public backlash, duration of crisis)? (4) What was the measurable equity impact (sales drop %, recovery timeline, brand tracking movement if data available)? (5) What was the recovery move — did the brand return to the original archetype or attempt repositioning? Then abstract a four-item 'drift signature' framework: the early-warning signals that appear before recognition asset destruction, applicable to any brand."
**Read / check:** Verify that the Tropicana analysis identifies the Innocent archetype and names the new packaging's departure from the orange-and-straw recognition cue as the triggering action — matching the Ch. 5 analysis of recognition assets.
**Human supplies:** No unique data required — Claude synthesizes from training data on three well-documented cases; human reviews the drift-signature framework against their own brand for applicability.
**Output medium:** Screen-rec mp4 — three-case comparison table printed, drift-signature framework as a numbered list, with the teardown angle (the invisible asset) as the closing frame.
**The change:** Before: brand changes made by executives who "know what they're doing" with no structured analysis of recognition asset risk. After: a four-item drift signature that makes the warning signs visible before the recognition asset is destroyed.
**Teardown angle:** The recognition asset is invisible until it is destroyed — the brand metric that captures it (association strength in tracking studies) moves slowly, which is why archetype drift is not caught by performance dashboards until the damage is already done.
**Exclusions:** Do not frame "returning to the original archetype" as always the right move — the recovery analysis must account for whether the original archetype is still relevant to the current audience.
**Score:** 8/10

---

## Card 08 — Research: The Attribution Problem — Why a Brand Metric Moving Proves Nothing

**Source:** Chapter 13 (Measuring Brand Equity — the attribution problem, patience gap, correlation vs. causation)
**Lane:** RESEARCH
**Hook:** A number that moved is not a verdict. It is a question. And the question "did our brand work cause this?" almost always has an honest answer of "we cannot tell."
**The artifact:** A research synthesis on the attribution problem in brand measurement: Claude produces a structured analysis of three documented cases where correlation between brand investment and performance movement was claimed as causation — explains the confound in each case (media spend increase, seasonality, competitor withdrawal) — then derives a five-question attribution checklist that any brand team should answer before attributing a performance metric movement to brand work.
**Prompt seed:** "Research the attribution problem in brand measurement: find three documented cases where a brand claimed their marketing investment caused a performance metric improvement, but an alternative explanation (media spend increase, seasonality, competitor withdrawal, economic tailwind) was at least as plausible. For each case: (1) What improvement was claimed? (2) What brand investment was cited as the cause? (3) What alternative explanation was available but not considered? (4) What would have been needed (control group, holdout test, time-lagged regression) to establish causation rather than correlation? Then derive a five-question attribution checklist: the minimum questions a brand team must answer before claiming their work caused a metric movement."
**Read / check:** Verify the synthesis names at least one case with a plausible seasonality or competitor-withdrawal confound — these are well-documented in brand measurement literature and should appear in Claude's training data.
**Human supplies:** Their own brand's most recent claimed success ("we ran this campaign and X metric improved") — optional input to run the five-question checklist against their specific case after the general synthesis.
**Output medium:** Screen-rec mp4 — synthesis printed as three case blocks, attribution checklist as a numbered list, optional user-case application at the end.
**The change:** Before: "we ran the campaign and NPS went up 3 points, so it worked." After: a five-question attribution checklist that separates "a metric moved" from "our work caused it."
**Teardown angle:** The Pepsi/Kendall Jenner case from Ch. 13 — awareness went up and favorability went down simultaneously; the instinct to find one number and declare it the verdict is precisely what the attribution checklist is designed to resist.
**Exclusions:** Do not suggest that absence of causal proof means brand work has no effect — the attribution checklist is a discipline for making honest claims, not an argument that brand investment is ineffective.
**Score:** 8/10

---

## Card 09 — Build a Brand Voice Consistency Auditor with Claude

**Source:** Chapter 10 (Brand Voice and Storytelling), Chapter 5 (Archetypes — forcing function for copy decisions)
**Lane:** BUILD
**Hook:** A committed archetype makes every copy decision a filter — does this fit the archetype? — instead of an open debate. The auditor makes the drift visible before it ships.
**The artifact:** A brand voice consistency pipeline: the user provides (1) their brand's archetype and three adjectives that define their voice, (2) five samples of their recent copy (social posts, web headlines, email subject lines). Claude scores each sample on archetype alignment (1–5), flags the specific word or phrase that drifts furthest from the archetype's voice, and rewrites the lowest-scoring sample in the correct archetype register.
**Prompt seed:** "You are a brand voice auditor. Given: Archetype = [ARCHETYPE], Voice adjectives = [ADJ1, ADJ2, ADJ3], and these five copy samples: [SAMPLE 1–5]. For each sample: (1) score archetype alignment 1 (strong drift) to 5 (fully consistent), (2) flag the specific word or phrase that drifts most from the archetype's expected register, (3) give a one-sentence rationale citing the archetype's core motivation or shadow. Then: rewrite the lowest-scoring sample in the correct archetype register, keeping the same informational content. Return: scoring table, then the rewrite."
**Read / check:** Run with Innocent archetype and a copy sample that includes urgency or scarcity language ("last chance," "only 3 left"). Verify the auditor flags urgency language as drift — the Innocent archetype's shadow is denial and naivety, but its voice should be warmth and simplicity, not manufactured scarcity.
**Human supplies:** Their brand's archetype (from the classifier in Card 02, or their own choice), three voice adjectives, and five real copy samples from their own recent marketing.
**Output medium:** Screen-rec mp4 — archetype + samples in, scoring table printed, lowest-scoring sample rewritten in the correct register below.
**The change:** Before: brand voice is "try to sound consistent" with no explicit standard to check against. After: a per-sample alignment score with the specific drifting phrase flagged and an in-register rewrite to compare against.
**Teardown angle:** The archetype as forcing function from Ch. 5 — the constraint is cheap to enforce once chosen; every copy decision is now a binary ("does this fit Innocent?") rather than an open aesthetic debate.
**Exclusions:** Do not present the alignment score as an absolute truth — brand voice exists on a spectrum and deliberate tonal variation is sometimes intentional; the auditor surfaces unintentional drift, not all variation.
**Score:** 8/10

---

## Card 10 — Research: The Creative Engineer's Market — How AI Is Repricing Professional Value

**Source:** Chapter 1 (The Creative Engineer — labor market evidence, $206K AI engineering base, 30–50% specialist premium, the costly signal shift)
**Lane:** RESEARCH
**Hook:** The market is repricing. AI engineering base salaries average $206,000 with specialists pulling 30–50% above generalists at the same seniority. The question is what the market is paying for now that it wasn't paying for before.
**The artifact:** A labor market analysis document: Claude synthesizes available evidence on the AI-era repricing of professional value — the specialist premium across software engineering, marketing, and design, the skills commanding the premium (Ideate / Brand / Ship rather than Build), and the structural mechanism (Spence signaling theory applied to AI-compressed credentials). Ends with a field-by-field table showing what used to be the separating signal, what has pooled, and what is currently separating.
**Prompt seed:** "Research the labor-market evidence for the 'Creative Engineer' repricing hypothesis: that AI tooling has collapsed the signal value of code-production credentials while increasing the premium on product judgment, audience positioning, and shipping to real users. Include: (1) the Peng et al. (2023) GitHub Copilot RCT results and their market-structure implications; (2) available data on AI engineering salary premiums (specialist vs. generalist, judge vs. producer roles); (3) evidence from adjacent fields (design, marketing, writing) where automation has shifted which skills command premium; (4) a Spence signaling mechanism explanation of why these specific skills are currently separating. End with a field-by-field table: [Field | Old separating signal | Now pooled | Currently separating]."
**Read / check:** Verify the synthesis includes the 56% task-completion reduction from Peng et al. and the $206K base / 30–50% specialist premium from Ch. 1 — both are specific enough to verify against training data and signal that Claude is grounding the synthesis in the book's evidence base rather than generic claims.
**Human supplies:** Their own field and current credential set — optional input to apply the field-by-field table to their specific context after the general synthesis.
**Output medium:** Screen-rec mp4 — research synthesis printed as three evidence sections, field-by-field table at the end, teardown close with the signaling mechanism as the explanatory frame.
**The change:** Before: "learn to code" as the universal career advice. After: a field-specific map of which signals have pooled and which are currently separating — the foundation for deciding where to invest professional development effort.
**Teardown angle:** The Spence mechanism from Ch. 1 — the signal works only as long as its cost-structure holds; AI tooling is the largest single-year cost-structure collapse in the history of professional credentials, and the repricing is still underway.
**Exclusions:** Do not present the specialist premium data as fixed or permanent — labor market pricing is dynamic; the synthesis should note that currently-separating signals will be the next signals to pool as AI tooling advances.
**Score:** 8/10

---

<!-- DELTA PASS 2026-07-17 — new BUILD/RESEARCH cards not covered by Cards 01–10. -->

## Card 11 — Build a Boondoggle Score Calculator with Claude

**Source:** Chapter 97 (Fundamental Themes — The Boondoggling Argument, the Boondoggle Score)
**Lane:** BUILD
**Hook:** Point at any task on your plate and the tool tells you whether you've split it right — AI on the pattern-work, you on the judgment — or handed the machine the part it was never good at.
**The artifact:** A CLI tool that takes a task description, asks Claude to decompose it into sub-steps, tag each step as AI-does-best (pattern / volume / reformatting / retrieval) or human-conducts (judgment / taste / accountability / sign-off), and compute a Boondoggle Score = fraction of steps correctly placed, flagging any judgment step currently assigned to the AI as a misplacement to fix.
**Prompt seed:** "Decompose this task into concrete sub-steps: [TASK]. For each step, tag it AI-DOES-BEST (pattern recognition, high-volume drafting, reformatting, retrieval) or HUMAN-CONDUCTS (judgment, taste, causal reasoning, accountable sign-off), with a one-line reason. Then compute a Boondoggle Score (0–100) = share of steps whose current owner matches its correct owner, and list every judgment step that should NOT be delegated to the model."
**Read / check:** Run on "write and approve our brand's crisis statement." Verify Claude tags drafting as AI-does-best but tags approval/claim-clearing as HUMAN-CONDUCTS, and that delegating the sign-off drops the score — matching the Ch. 97 separation principle.
**Human supplies:** Their own real task, and the final call on whether a step is genuinely a judgment step.
**Output medium:** Screen-rec mp4 — task in, two-lane split table + Boondoggle Score printed, misplaced judgment steps flagged in red.
**The change:** Before: "use AI for everything" or "use AI for nothing." After: an explicit seam that shows exactly which steps to delegate and which to keep.
**Teardown angle:** Most AI failures are seam failures — the machine did pattern-work fine and was blamed for a judgment it was never handed correctly.
**Exclusions:** Do not present the score as a safety guarantee; a well-placed seam still needs the human to actually exercise the judgment at the gate.
**Score:** 8/10

---

## Card 12 — Build a Self-as-Project Brand Runner with Claude

**Source:** Chapter 3 (The AI Toolchain — the Self-as-Project thread) + Introduction (AI+1)
**Lane:** BUILD
**Hook:** Run your own career through the same pipeline the book runs a brand through — archetype, position, voice, portfolio — with the agent drafting each stage and you signing it off.
**The artifact:** A CLI that walks the Self-as-Project thread: it prompts Claude to draft, for the user, a candidate archetype, a one-line position, a voice sample, and a portfolio thesis — each as a DRAFT with an explicit "+1 sign-off required" gate, and writes an accountability log recording which drafts the human approved, edited, or rejected.
**Prompt seed:** "Act as the drafting agent for a Self-as-Project brand build. Given this person's background: [BACKGROUND] and target field: [FIELD], draft four artifacts, each clearly labeled DRAFT — pending +1 sign-off: (1) a Jungian archetype with its shadow, (2) a one-sentence position, (3) a 3-sentence voice sample, (4) a portfolio thesis. After each, state the specific human judgment required to approve it and the evidence the +1 should check before signing."
**Read / check:** Run on a sample background. Verify every output is labeled a DRAFT with a named sign-off, and that the tool refuses to mark anything "final" without a recorded human approval — matching the AI+1 / phase-gate discipline.
**Human supplies:** Their real background, the target field, and every accountable approval (the +1 owns each decision).
**Output medium:** Screen-rec mp4 — background in, four gated drafts printed, an accountability log written as the human approves/edits each.
**The change:** Before: asking AI to "build my personal brand" and pasting whatever it says. After: a gated pipeline where AI drafts and the human owns every committed decision.
**Teardown angle:** The AI+1 thesis made operational — the agent drafts, the +1 decides, and the log proves which was which.
**Exclusions:** Do not let the tool auto-finalize any artifact; the whole point is that the sign-off is human. No résumé-writing or job-application automation — this is brand artifacts, not applications.
**Score:** 8/10

---

<!-- DELTA PASS 2026-07-18 — 10 new BUILD/RESEARCH cards from chapters 02, 04, 06, 08, 09, 15, 16, 20, 22, 23. These chapters were unread in the 2026-07-12 and 2026-07-17 passes. -->

## Card 13 — Build a PRD Scope Decision Record with Claude

- **Source:** `branding-and-ai/chapters/20-shipit-product-requirements-and-scope.md` (LLM Exercise 4 — CLI Exercise)
- **Lane:** BUILD (Claude Code)
- **Hook:** The "$100,000 no" is the highest-leverage decision in a product — the feature you refused to ship. Linear's entire brand identity is built from explicit, documented refusals. A PRD that has no NOT-LIST is not a PRD; it is a wish list with a deadline.
- **The artifact:** A `your-tool/prd.md` document with two mandatory sections: (1) WILL-BUILD — a numbered list of features, each with a one-sentence user-facing rationale and the testable criterion for "done"; (2) WILL-NOT-BUILD — a numbered NOT-LIST, each entry with a one-sentence reason it was declined and the condition under which it would be reconsidered. The tool computes a scope discipline score = WILL-NOT-BUILD count / (WILL-BUILD + WILL-NOT-BUILD) and flags any PRD where the score falls below 0.25 (i.e., fewer than one refusal per three features).
- **Prompt seed:** `"You are a PRD scope auditor. Given this product description and feature list: [PRODUCT + FEATURES]. Generate two sections: (1) WILL-BUILD — format each as 'Feature: [name] | Rationale: [one sentence, user-facing, not implementation-focused] | Done when: [observable, testable criterion].' (2) WILL-NOT-BUILD — for each feature explicitly not in scope, format as 'Declined: [feature] | Reason: [one sentence — why this doesn't belong in v1] | Reconsidered if: [the specific condition that would change the decision].' Then compute: scope_discipline_score = NOT-LIST count / total feature count. If below 0.25, print: 'WARNING: PRD lacks explicit refusals — add NOT-LIST entries before approving.'"`
- **Read / check:** Run on a tool with ten features and zero NOT-LIST entries. Verify the score prints below 0.25, the WARNING fires, and the generated NOT-LIST includes at least one multi-user feature and one analytics dashboard — the two most common v1 scope creep categories from Ch. 20's worked example.
- **Human supplies:** The real feature list and product description for their tool. The human must supply every NOT-LIST acceptance decision — Claude generates candidates, the founder approves which refusals are real.
- **Output medium:** Screen-rec mp4 — feature list in, WILL-BUILD and WILL-NOT-BUILD sections printed, scope discipline score animated as a gauge growing toward 0.25.
- **The change:** Before: a PRD that lists everything the product might do, with no documented decision about what it will not do. After: an explicit NOT-LIST that makes every scope-creep request a named trade-off against a documented refusal.
- **Teardown angle:** Linear built its identity on refusals — the product is what it declines as much as what it ships. The "$100,000 no" is the highest-leverage brand statement a product team makes, and it is almost never written down before pressure arrives.
- **Exclusions:** Do not present the NOT-LIST as permanent — Ch. 20 explicitly requires the "reconsidered if" field; a refusal without a revision condition is a wall, not a decision.
- **Score:** 9/10

---

## Card 14 — Build an AI Architecture Autonomy Classifier with Claude

- **Source:** `branding-and-ai/chapters/22-shipit-ai-intelligence-and-multiagent-systems.md` (Agent Specification section + LLM Exercise 4)
- **Lane:** BUILD (Claude Code)
- **Hook:** AutoGPT cost $80 and delivered nothing. Cursor works reliably enough that professional developers trust it with production code. Same underlying model capability — different architecture decision about where the AI is allowed to decide and where it is not.
- **The artifact:** A CLI tool that takes a product description and outputs: (1) which of four autonomy patterns the product instantiates — A: prompt-wrapper (AI assists, human executes every step), B: ReAct loop (AI acts + observes + retries within a session), C: horizon-autonomous (AI plans and executes across hours without a checkpoint), D: specialized role in a pipeline (AI owns one deterministic slot with bounded inputs and outputs); (2) a failure-locatability rating — HIGH (failure isolated to one named component), MEDIUM (investigation needed across 2–3 components), LOW (mega-agent, failure structurally unknowable); (3) a written agent specification for each AI role: Role name | Inputs (typed) | Outputs (typed) | Permitted actions | Forbidden actions | Escalation condition.
- **Prompt seed:** `"You are an AI architecture classifier. Given this product description: [PRODUCT]. Step 1: classify which of the four autonomy patterns this product instantiates — A (prompt-wrapper), B (ReAct loop), C (horizon-autonomous), D (specialized pipeline role) — or a combination, with a one-sentence rationale. Step 2: failure-locatability rating — HIGH/MEDIUM/LOW with rationale. Step 3: for each AI role, write a specification: Role name | Inputs (with types) | Outputs (with types) | Permitted actions | Forbidden actions | Escalation condition. If failure-locatability is LOW, add: 'ARCHITECTURAL WARNING — recommend inserting a seam between [role A] and [role B].'"`
- **Read / check:** Run on a single-model marketing automation system with no separated roles (replicating Ch. 22's mega-agent anti-pattern). Verify: classified as Pattern C, failure-locatability = LOW, ARCHITECTURAL WARNING fires with a recommended seam. Then run on Cursor's architecture description; verify HIGH locatability.
- **Human supplies:** A description of the AI product they are building — must include what external data it accesses, what actions it takes autonomously, and what the failure mode looks like from the user's perspective.
- **Output medium:** Screen-rec mp4 — product description in, four-pattern classification + locatability rating printed, agent specifications as a formatted table, ARCHITECTURAL WARNING highlighted if triggered.
- **The change:** Before: "we built an agent that does X" with no account of where decisions are made. After: explicit autonomy classification, locatability rating, and written agent specifications that bound what each role may and may not do.
- **Teardown angle:** The AutoGPT vs. Cursor distinction from Ch. 22 — architecture is a trust decision, not just an engineering decision. The seam placement decides what customers can verify, name, and blame when things go wrong, which decides whether they trust the product at all.
- **Exclusions:** Do not present Pattern C (horizon-autonomous) as inherently wrong — the chapter identifies it as appropriate for tasks that genuinely require it; the classifier surfaces the locatability cost, not a prohibition.
- **Score:** 9/10

---

## Card 15 — Build a Trademark Strength Screener with Claude

- **Source:** `branding-and-ai/chapters/08-naming-trademark-and-brand-protection.md` (LLM Exercise 3 + Exercise 4 — CLI Exercise)
- **Lane:** BUILD (Claude Code)
- **Hook:** A great name you cannot own is a liability with good marketing. The same property that makes a name immediately understandable — it describes what the product does — is precisely what makes it hardest to protect legally.
- **The artifact:** A `your-brand/naming.md` table screening 15 candidate names against the Abercrombie trademark-strength spectrum. For each: name | spectrum class (generic / descriptive / suggestive / arbitrary / fanciful) | one-sentence rationale | memorability 1–5 | cross-language risk (meaning in Spanish, Mandarin, French, German) | .com availability [VERIFY] | protectability 1–5 | recommended action (ADVANCE / SCREEN / DROP). Final block: top-3 shortlist of ADVANCE candidates. Every legal/availability note tagged `[VERIFY WITH SEARCH + COUNSEL]`.
- **Prompt seed:** `"Generate 15 name candidates for this brand: [BRAND DESCRIPTION + ARCHETYPE]. For each: (1) Spectrum class: generic/descriptive/suggestive/arbitrary/fanciful — one-sentence rationale. (2) Memorability 1–5. (3) Cross-language risk: harmful/embarrassing meaning in Spanish, Mandarin, French, or German? (4) .com availability [VERIFY]. (5) Protectability 1–5 (5 = fanciful). (6) Action: ADVANCE, SCREEN, or DROP. Final block: top-3 ADVANCE shortlist. TAG EVERY LEGAL OR AVAILABILITY ASSERTION [VERIFY WITH SEARCH + COUNSEL] — do not claim any name is legally available.'"`
- **Read / check:** Include "AI Writer" as one of the 15 inputs. Verify it is classified as descriptive/generic, rated DROP, and protectability score is 1–2 — matching Ch. 8's analysis that descriptive marks are the weakest.
- **Human supplies:** Brand description and archetype. The human takes the shortlist through actual USPTO search and trademark counsel — the card cannot substitute for clearance.
- **Output medium:** Screen-rec mp4 — brand description in, 15-candidate table printed with spectrum classes, top-3 shortlist highlighted, every legal note tagged [VERIFY WITH SEARCH + COUNSEL].
- **The change:** Before: founders generate one name they love and build six months of brand around it before discovering a prior registration. After: 15 candidates classified by protectability, shortlisted by archetype fit, every legal claim explicitly flagged.
- **Teardown angle:** The legibility-versus-exclusivity trade-off from Ch. 8 — the more immediately understandable a name is, the less exclusively yours it can be; fanciful names feel opaque at first and become the most defensible assets once meaning is taught.
- **Exclusions:** Every legal and availability claim is `[VERIFY WITH SEARCH + COUNSEL]`. Do not present the shortlist as cleared. Route clearance to a trademark attorney.
- **Score:** 9/10

---

## Card 16 — Build an SCCT Crisis Triage Tool with Claude

- **Source:** `branding-and-ai/chapters/16-crisis-and-reputation-management.md` (The Playbook section + LLM Exercise 4)
- **Lane:** BUILD (Claude Code)
- **Hook:** United Airlines lost the first day of the narrative without saying anything at all. The difference between a handled crisis and a compounded one is written in the playbook before the fire starts, not during it.
- **The artifact:** A crisis triage CLI that takes a crisis description and outputs: (1) SCCT classification — Victim (low public responsibility), Accidental (moderate), or Preventable (high) — with a rationale citing specific facts; (2) recommended response strategy — Deny/Bolster, Diminish, or Rebuild/Mortification — plus a STRATEGY MISMATCH WARNING if the user's instinct conflicts with the classified type; (3) a holding statement draft calibrated to the SCCT type (accidental: acknowledge + investigate + promise update; preventable: accept responsibility without qualification); (4) escalation path — who decides, who speaks, whether legal review is required.
- **Prompt seed:** `"You are an SCCT crisis classifier. Given: [CRISIS DESCRIPTION]. Step 1: classify as Victim (low responsibility), Accidental (moderate), or Preventable (high) — with rationale citing specific facts. Step 2: strategy — Victim → Deny/Bolster; Accidental → Diminish; Preventable → Rebuild/Mortification. If the description contains language suggesting the user wants a lower-responsibility strategy on a higher-responsibility crisis, print: 'STRATEGY MISMATCH WARNING: applying [lower strategy] to a [higher type] crisis compounds damage.' Step 3: draft holding statement calibrated to type. Step 4: escalation recommendation — primary and backup decision-maker, approval chain, whether legal review is required (always yes for Preventable).'"`
- **Read / check:** Run on a description matching the BP Deepwater Horizon pattern — safety concerns overridden for cost. Verify: classified as Preventable, recommends Rebuild/Mortification, fires STRATEGY MISMATCH WARNING if Diminish is suggested, holding statement accepts responsibility without equivocation — matching Ch. 16's J&J vs. BP contrast.
- **Human supplies:** The real crisis description. The human makes every decision about what actually gets posted; legal review is required for preventable crises before any public statement.
- **Output medium:** Screen-rec mp4 — crisis description typed in, SCCT classification printed, holding statement displayed, STRATEGY MISMATCH WARNING highlighted in red if triggered.
- **The change:** Before: crisis response improvised live, wrong strategy applied under pressure. After: a triage tool that classifies the crisis type, surfaces the SCCT mismatch, and produces a type-calibrated holding statement within the first hour.
- **Teardown angle:** The Tylenol vs. BP contrast from Ch. 16 — same high-pressure situation, opposite strategy choices, opposite recovery trajectories. Correct triage at the first hour is worth a decade of goodwill.
- **Exclusions:** The holding statement is a draft, not a post. Legal review is mandatory for preventable crises. Do not model the tool as replacing counsel.
- **Score:** 9/10

---

## Card 17 — Build an Aaker Dimension Weakness Finder with Claude

- **Source:** `branding-and-ai/chapters/02-what-a-brand-is-equity.md` (The Equity Audit section + LLM Exercise 4)
- **Lane:** BUILD (Claude Code)
- **Hook:** The diagnostic move Aaker gives you: map your brand on all four dimensions and find the weakest one. Intervening on a strong dimension produces little; intervening on the weak one produces the most lift. Most brand audits gather sentiment and skip this step entirely.
- **The artifact:** A `your-brand/equity-audit.md` mapping public signals for a named brand across all four Aaker dimensions — Awareness (unaided recall, top-of-mind), Perceived Quality (gap between functional and perceived quality), Associations (coherence of the association network), Loyalty (behavioral vs. attitudinal distinction). Each signal tagged [CONFIRMED-SOURCE] or [UNVERIFIED]. Produces: a signal-per-dimension table; a weakness assessment naming the lowest-scoring dimension; one specific intervention recommendation. The Keller pyramid level column is left blank for the human to fill — that judgment is the +1 the model cannot make.
- **Prompt seed:** `"You are a brand equity analyst. Using public sources, assemble a brand-equity baseline for [BRAND NAME]. For each Aaker dimension — (1) Awareness: unaided-recall and top-of-mind evidence; (2) Perceived Quality: gap between functional quality (reviews, test data) and perceived quality (pricing power, premium paid); (3) Associations: coherence of the association network in public discourse; (4) Loyalty: behavioral loyalty (repurchase) vs. attitudinal loyalty (commitment even when alternatives improve). Tag each evidence item [CONFIRMED-SOURCE] or [UNVERIFIED]. Do NOT assign an overall equity score. Leave the Keller pyramid level column blank — mark it '[YOUR CALL]'. End with: weakest-dimension paragraph + one specific intervention recommendation.'"`
- **Read / check:** Run on a brand with strong behavioral loyalty but known attitudinal fragility (cable/telecom). Verify the tool identifies Loyalty as weakest, specifically flags the behavioral-vs-attitudinal split, and leaves the Keller level blank — matching Ch. 2's equity audit discipline.
- **Human supplies:** The brand name. The human grades signals against the Keller pyramid — the equity-level verdict is the judgment the model cannot make.
- **Output medium:** Screen-rec mp4 — brand name in, four-dimension table printed with source tags, weakest dimension paragraph shown, Keller level column visibly blank with "[YOUR CALL]" placeholder.
- **The change:** Before: audits that conflate "positive associations exist" with "resonance-level equity." After: a structured four-dimension audit that finds the weakest lever and leaves the equity verdict to the human who understands what each level requires.
- **Teardown angle:** Ch. 2's separation of equity from sentiment — a brand can have net-positive sentiment at the salience level and no resonance whatsoever. The Aaker diagnostic finds the gap; the Keller grading is the judgment the model cannot make.
- **Exclusions:** Tag every factual claim [CONFIRMED-SOURCE] or [UNVERIFIED]. Do not generate valuation numbers — Interbrand/Kantar methodology requires proprietary data Claude does not have.
- **Score:** 8/10

---

## Card 18 — Build a JTBD Audience Segment Generator with Claude

- **Source:** `branding-and-ai/chapters/04-the-brand-audience.md` (Jobs To Be Done section + AI+1 Exercise 3)
- **Lane:** BUILD (Claude Code)
- **Hook:** The milkshake study worked because Christensen's team stopped guessing at motives and watched what commuters actually did at 7 a.m. The JTBD reframe cuts across demographics in a way demographics cannot cut across themselves — a 22-year-old graduate student and a 55-year-old executive can be the same segment.
- **The artifact:** A `your-brand/audience.md` generating 3 candidate segments defined by job-to-be-done (not demographics): for each — segment name (a phrase naming the job) | the specific job this person hires the brand to do | the cultural tension this group lives with that no brand in the space is currently resolving | one verifiable behavior (observable, evidence-tied) | evidence status (CONFIRMED / NEEDS-EVIDENCE / INFERRED). Every demographic descriptor auto-flagged [DEMOGRAPHIC — CONVERT TO JOB].
- **Prompt seed:** `"You are an audience analyst using Jobs-to-Be-Done. Given: [ARCHETYPE + DATA]. Generate 3 candidate segments. For each: (1) Segment name — a phrase naming the JOB, not age/income/occupation. Flag any segment that leads with a demographic as [DEMOGRAPHIC — CONVERT TO JOB]. (2) The job: what does someone in this segment hire this brand to do? Specific occasion + outcome. (3) Cultural tension: what contradiction does this group feel that no brand in this space is resolving? (4) Verifiable behavior: one specific, observable thing members actually do — not an inferred motive. (5) Evidence status: CONFIRMED / NEEDS-EVIDENCE / INFERRED.'"`
- **Read / check:** Supply an archetype where the obvious segment is demographic (e.g., "professional women 28–40 in tech"). Verify the tool converts it to a job-level segment, fires [DEMOGRAPHIC — CONVERT TO JOB], and produces a cultural tension that is specific and non-generic.
- **Human supplies:** Their brand archetype and any qualitative data (interview quotes, forum threads, support tickets). The human makes the strategic decision on which segment to target.
- **Output medium:** Screen-rec mp4 — archetype + data in, three segments as a structured table, CONFIRMED/NEEDS-EVIDENCE/INFERRED tags shown, [DEMOGRAPHIC — CONVERT TO JOB] warnings highlighted.
- **The change:** Before: audience defined as a demographic descriptor that predicts nothing about what those people need. After: three job-level segments with explicit cultural tensions, verifiable behaviors, and clear evidence status.
- **Teardown angle:** The milkshake commuter from Ch. 4 — same product, completely different competitive set (granola bars, not milkshakes), completely different design implication (thicker, slower-consuming), because the job was the actual segment. Demographics would have missed everything that mattered.
- **Exclusions:** Do not accept any segment defined primarily by demographic descriptor — fire the flag on every one. Invent no statistics or market-size numbers.
- **Score:** 8/10

---

## Card 19 — Build a Brand Negative Space Mapper with Claude

- **Source:** `branding-and-ai/chapters/06-brand-strategy-and-positioning.md` (Negative Space section, Stripe worked case)
- **Lane:** BUILD (Claude Code)
- **Hook:** Stripe's brand identity is more legible in what it has refused — consumer billing UIs, point-of-sale hardware, small-business onboarding — than in what it has shipped. The refusals are sustained, and a fifteen-year pattern of documented declines is the clearest brand statement a company makes.
- **The artifact:** A `your-brand/negative-space.md` mapping a brand's documented refusals across two dimensions: (1) TACTICAL NEGATIVE SPACE — specific features, product lines, or markets the brand has declined (each tagged [VERIFIED-PUBLIC] or [INFERRED-FROM-PATTERN]); (2) STRATEGIC NEGATIVE SPACE — the audience or use case the brand structurally cannot serve without contradicting its identity. Plus: a negative-space profile paragraph synthesizing what the refusals collectively signal; a draft positioning sentence derived from the refusal pattern; a consistency check flagging any contradictions between documented refusals.
- **Prompt seed:** `"You are a brand positioning analyst. For: [BRAND NAME OR DESCRIPTION]. Step 1 — Tactical Negative Space: list specific features, categories, or segments this brand has demonstrably declined to build. Tag each [VERIFIED-PUBLIC] or [INFERRED-FROM-PATTERN]. Step 2 — Strategic Negative Space: who would this brand have to stop being to serve them? Step 3 — Negative Space Profile: 2-sentence synthesis of what the refusals collectively signal. Step 4 — Draft Positioning Sentence: derived from the refusal pattern, not from the brand's own marketing copy. Step 5 — Consistency Check: do the refusals form a coherent identity, or are there contradictions? Format contradictions as: REFUSAL A implies [X], REFUSAL B implies [not X].'"`
- **Read / check:** Run on Stripe. Verify tactical negative space includes consumer billing and point-of-sale (publicly documented), strategic negative space names small-business-first products, and the positioning sentence is derived from refusals rather than from Stripe's own "help businesses make and move money" copy.
- **Human supplies:** Their own brand's archetype and any record of decisions to not build something. For a personal brand: professional opportunities turned down.
- **Output medium:** Screen-rec mp4 — brand name in, two-column negative-space table printed, profile paragraph and positioning sentence displayed, consistency contradictions flagged.
- **The change:** Before: positioning derived from a feature list and audience claims. After: positioning derived from a pattern of consistent refusals — a harder-to-copy identity signal.
- **Teardown angle:** The Stripe inversion from Ch. 6 — the clearest picture of the brand emerges from what Stripe has refused to build across fifteen years, not from what it has shipped.
- **Exclusions:** Tag every claimed refusal [VERIFIED-PUBLIC] or [INFERRED-FROM-PATTERN] — do not present inferred absences as documented decisions. The positioning sentence is a draft; the human decides if it captures the actual brand identity.
- **Score:** 8/10

---

## Card 20 — Build an Interface-Brand Alignment Checker with Claude

- **Source:** `branding-and-ai/chapters/23-shipit-interface-and-deployment.md` (Three Faces of Misalignment + LLM Exercise 4)
- **Lane:** BUILD (Claude Code)
- **Hook:** On February 8, 2023, Alphabet lost approximately $100 billion in market capitalization because a promotional video showed Bard answering a factual question incorrectly. The interface is not a finishing layer — it is a promise the user re-checks every session.
- **The artifact:** A `your-brand/interface-audit.md` evaluating a tool's interface copy against three alignment dimensions: (1) VOICE ALIGNMENT — does the copy register match the brand archetype? (2) CLAIM ALIGNMENT — does the interface make any implicit claim the system cannot reliably fulfill? (3) FAILURE STATE ALIGNMENT — does the error message, empty state, and "I don't know" response hold the archetype under pressure, or does the brand voice collapse when something goes wrong? For each: rating (ALIGNED / PARTIAL / MISALIGNED) | specific element causing drift | rewrite.
- **Prompt seed:** `"You are an interface-brand alignment auditor. Given: archetype = [ARCHETYPE], voice adjectives = [ADJ1, ADJ2, ADJ3], and interface elements — (A) Hero copy: [COPY], (B) CTA text: [CTA], (C) Error message: [ERROR], (D) Empty state text: [EMPTY], (E) Uncertain-response text: [UNCERTAIN]. For each of three dimensions: (1) Voice Alignment — ALIGNED/PARTIAL/MISALIGNED; flag the specific word or phrase drifting furthest from archetype register; provide rewrite. (2) Claim Alignment — does any copy imply a capability the tool cannot reliably fulfill? ALIGNED/PARTIAL/MISALIGNED; identify claim; provide honest version. (3) Failure State Alignment — does error/empty/uncertain response hold the archetype's voice or collapse to generic? Rate and rewrite.'"`
- **Read / check:** Provide a Sage-archetype tool with error message "Oops! Something went wrong. Try again." Verify the tool rates Failure State MISALIGNED, flags "Oops!" as inconsistent with Sage register (which is precise and explanatory, not colloquially apologetic), and rewrites to something like "This query produced no results. Try narrowing the search term or specifying a date range."
- **Human supplies:** Actual interface copy from their deployed tool — hero copy, CTA, error message, empty state, uncertain-response text. The human decides whether to implement rewrites.
- **Output medium:** Screen-rec mp4 — interface elements pasted in, three-dimension table printed, MISALIGNED items highlighted, rewrites displayed below each flagged element.
- **The change:** Before: interface copy written last, under deadline, by whoever has time — resulting in voice that doesn't match the brand when users need it most. After: an alignment audit that surfaces every voice drift and claim mismatch, with failure states explicitly checked.
- **Teardown angle:** The Bard $100B case from Ch. 23 — the interface IS the contract; a claim the interface makes that the system cannot reliably fulfill is a brand-destruction event waiting for the first public test.
- **Exclusions:** This card audits static interface copy only (text the team controls), not model-generated answers in response outputs, which is a separate QA problem.
- **Score:** 8/10

---

## Card 21 — Build a Brand Palette Accessibility Auditor with Claude

- **Source:** `branding-and-ai/chapters/09-visual-identity-systems.md` (Color Palette — Construction and Accessibility section + Exercise 4 — CLI Exercise)
- **Lane:** BUILD (Claude Code)
- **Hook:** A palette that fails WCAG AA cannot be read by some fraction of your audience. A color combination below 4.5:1 contrast ratio for normal text is not a stylistic choice — it is a documented barrier to access, and shipping it signals you did not think carefully about users.
- **The artifact:** A `your-brand/qa-report.md` taking a brand palette (hex codes) and intended text-on-background pairings, computing WCAG contrast ratios via the relative luminance formula, rating each pairing (PASS-AAA ≥7:1 / PASS-AA ≥4.5:1 normal / PASS-AA-large ≥3:1 for 18pt+ / FAIL), and for every FAIL proposing a corrected hex within the same hue family that achieves at least AA — with the corrected ratio shown.
- **Prompt seed:** `"You are a WCAG accessibility auditor. Given palette: [HEX CODES WITH LABELS]. Test these text-on-background pairings: [PAIRING LIST]. For each: (1) compute relative luminance (L = 0.2126 R + 0.7152 G + 0.0722 B on linearized channels). (2) contrast ratio = (L_lighter + 0.05) / (L_darker + 0.05). (3) rate: PASS-AAA (≥7:1), PASS-AA-normal (≥4.5:1), PASS-AA-large (≥3:1), or FAIL. (4) for every FAIL: nearest hex in the same hue achieving AA, with corrected ratio. Output: table (pairing | ratio | rating | fix-if-fail), then summary: N/M pairings pass AA for normal text.'"`
- **Read / check:** Include warm-clay (#A89068) on white (#FFFFFF). Verify ratio ≈3.1:1, rated FAIL for normal text, PASS-AA-large, and proposed corrected alternative near #7A6045 achieving ≥4.5:1 — the pattern Ch. 9 identifies as the most common accessibility failure for warm accent palettes.
- **Human supplies:** Actual brand palette hex codes and intended text-on-background pairings. The human decides which corrected alternatives to adopt; the palette belongs to the brand strategy.
- **Output medium:** Screen-rec mp4 — hex codes and pairings in, contrast ratio table printed, FAIL rows highlighted, corrected alternatives displayed beside each failing pair, summary count at the bottom.
- **The change:** Before: palette chosen for aesthetic coherence, deployed with no accessibility check, discovered to fail WCAG AA after a screen reader user reports the issue. After: a systematic audit surfacing every failing pairing before deployment, with specific corrected alternatives that stay within the archetype's visual system.
- **Teardown angle:** Ch. 9's accessibility principle applied to brand work — a palette that fails contrast is not just legally risky; it is a signal about who you designed for. The correction is almost always minor (darkening/lightening 15–20%), and the failure is always avoidable.
- **Exclusions:** The contrast formula applies to text elements; non-text elements (icons, decorative graphics) fall under a different 3:1 threshold. Route complex multi-state UI accessibility to a professional accessibility audit.
- **Score:** 8/10

---

## Card 22 — Build a Greenwashing Claims Risk Checker with Claude

- **Source:** `branding-and-ai/chapters/15-brand-ethics-purpose-and-sustainability.md` (EU ECGT Directive section + LLM Exercise 4)
- **Lane:** BUILD (Claude Code)
- **Hook:** As of 27 September 2026, "eco-friendly" without documented substantiation is not a marketing choice — it is a regulatory violation under EU law. Every generic green claim is now a liability with good typography.
- **The artifact:** A `your-brand/claims-proof-map.md` auditing a list of ethical/sustainability/purpose claims against the EU ECGT Directive and FTC Green Guides. For each claim: type classification (generic environmental / specific attribute / carbon-climate neutral / ESG metric / social impact) | ECGT flag ([ECGT-RISK] if matching banned categories: generic green claims without substantiation, or offset-based carbon neutral) | risk rating (HIGH-REGULATORY / MEDIUM / LOW) | evidence required to substantiate | current status (HAVE / NEED / CANNOT-SUBSTANTIATE) | for HIGH and MEDIUM: revised compliant version.
- **Prompt seed:** `"You are a greenwashing risk analyst. Given these public-facing claims: [CLAIM LIST]. For each: (1) Classify: generic environmental / specific attribute / carbon-climate neutral / ESG metric / social impact. (2) ECGT Flag: does this match any banned category under the EU ECGT Directive (effective 27 Sept 2026) — specifically: generic green claims without recognized substantiation ('eco-friendly,' 'sustainable,' 'green,' 'climate-smart'), or product-level climate neutral/net zero claims based primarily on offsets? Mark [ECGT-RISK]. (3) Risk rating: HIGH-REGULATORY / MEDIUM / LOW. (4) Evidence required to substantiate. (5) Status: HAVE / NEED / CANNOT-SUBSTANTIATE. (6) For HIGH and MEDIUM: revised compliant version or removal recommendation.'"`
- **Read / check:** Include "Our platform is eco-friendly and carbon neutral through our offset program." Verify: tagged [ECGT-RISK] on both components (generic eco-friendly banned; offset-based carbon neutral specifically targeted), rated HIGH-REGULATORY, and revised to require documented value-chain reduction methodology — matching Ch. 15's explicit treatment of offset-based claims.
- **Human supplies:** Actual public-facing claims from marketing site, about page, and investor materials. The human must produce actual evidence for every NEED item — the tool audits claims, it does not generate evidence.
- **Output medium:** Screen-rec mp4 — claim list in, claims-proof map printed, [ECGT-RISK] tags highlighted, HIGH-REGULATORY rows shown with revised versions, HAVE/NEED/CANNOT-SUBSTANTIATE status per row.
- **The change:** Before: sustainability copy written by marketing without legal review, containing generic claims that were standard practice before 2026. After: a risk-classified claims map identifying every potentially non-compliant claim, with a compliance path for each.
- **Teardown angle:** The backlash asymmetry from Ch. 15 — a values claim you cannot substantiate erodes trust faster than making no claim at all. The ECGT Directive makes this not just a reputational risk but an enforceable legal one.
- **Exclusions:** Confirm ECGT effective date and scope before relying on it (`[verify: EU law subject to amendment]`). This audit is a pre-screen; actual regulatory compliance requires qualified legal review in the relevant jurisdiction.
- **Score:** 8/10
