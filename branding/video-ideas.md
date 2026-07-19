# Bear's Doodles — Branding and AI Video Ideas

slate cut 

## Candidate 01 — Why the students who aced AI-assisted practice failed the real exam
- Source: `books/branding-and-ai/chapters/97-fundamental-themes.md`
- Production mode: Mixed
- Hook: The students who leaned on AI aced every practice problem — then scored 17 points LOWER on the test they had to take alone.
- Core idea: Bastani's finding — students using AI freely during math practice scored 48% higher in practice but 17 percentage points lower on the unassisted exam. The mechanism is neurobiological, not moral: friction (prediction error) triggers dopamine → BDNF → synapse strengthening → durable memory. Remove the friction and you remove the trigger. The fluency of AI output feels exactly like mastery; the artifact was fine, the brain was unchanged.
- Visual object: Two performance lines on one axis — an "AI practice" line soaring +48% and an "exam" line crashing −17pts — crossing, with a brain behind them whose synapses light on the friction path and stay dark on the AI shortcut.
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: None (everyone understands practice vs. test).
- Exclusions: Cut the Kosmyna EEG "55% connectivity" second study — one number, one mechanism. Do not explain BDNF biochemistry in detail; name friction→memory in one beat. Skip the causal-parrot and metacognition themes from this chapter entirely — they are separate videos (see Candidate on self-audit, which we cut for scope).
- Score: 10/10

slate cut 

## Candidate 02 — Why a 90%-accurate AI agent is wrong 98% of the time
- Source: `books/branding-and-ai/chapters/22-shipit-ai-intelligence-and-multiagent-systems.md`
- Production mode: Manim visualization
- Hook: Give an AI a 90%-accurate brain and forty steps to think, and it will be right about 1 time in 65.
- Core idea: Compounding error. A 10% per-step error rate means an error-free chain is 0.9^10 ≈ 35% after ten steps, ~12% after twenty, and ~1.5% after forty. This is not a model failure — it is an architecture failure: autonomous agents check whether a step COMPLETED, not whether it was CORRECT. Orchestrated systems insert validation between steps and stay reliable.
- Visual object: A probability bar starting near 100% decaying down a staircase of steps — annotated 35% at step 10, 12% at step 20, 1.5% at step 40.
- Manim move: drain
- Short-form fit: Strong
- Prerequisites: Basic sense that AI agents chain multiple steps.
- Exclusions: Do NOT teach the full orchestration-vs-autonomy taxonomy or the AutoGPT-vs-Cursor story (that is Candidate 14's cousin — kept separate). Skip the archetype-shadow-in-code idea. One number, one staircase. No probability notation beyond the multiplication shown.
- Score: 9/10

slate cut 

## Candidate 03 — How one pricing change handed a solo developer a $20-million-a-year bill
- Source: `books/branding-and-ai/chapters/21-shipit-pipelines-and-workflow-on-madison.md`
- Production mode: Mixed
- Hook: This app was flawless — then a single API price change handed its one-person team a $20-million-a-year bill overnight.
- Core idea: Reddit's new API pricing ($0.24 per 1,000 calls) times Apollo's ~7 billion monthly requests equalled roughly $20M/year, delivered with three months' notice to a shop earning hundreds of thousands. Apollo's code was excellent; what killed it was the contract. Reframe: a pipeline is a chain of contracts, each owned by someone else, each changeable without your consent.
- Visual object: A clean humming pipeline of nodes; the one edge labeled "Reddit API" flips its price tag, and the whole downstream product goes dark.
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: Loose idea that apps depend on other companies' APIs.
- Exclusions: Cut the "damage flows downhill" asymmetry (Candidate 19 territory — keep it separate) and the RSS-vs-API stability heuristic. Do not list Twitter/Heroku parallel cases; one collapse, one bill. No discussion of Selig's later projects.
- Score: 9/10

slate cut 

## Candidate 04 — How one wrong bullet point cost Google $100 billion
- Source: `books/branding-and-ai/chapters/23-shipit-interface-and-deployment.md`
- Production mode: Mixed
- Hook: A chatbot got one fact wrong in a promo video — and the interface around it turned that into a $100 billion loss.
- Core idea: Bard's demo answered a JWST question with three confident bullets; the third falsely claimed JWST took the first exoplanet image (it was the ESO's Very Large Telescope, 2004). Alphabet lost ~$100B in market cap that day. The error was not the cause — the interface was: a polished, Google-branded video presented Bard's output as authoritative in a domain anyone could fact-check. The market priced the gap between the promise and the system.
- Visual object: Three confident bullets on a glossy branded slide beside a market-cap counter; the false bullet gets fact-checked and the counter craters by $100B.
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: Awareness that Bard/Bard-era chatbots can be confidently wrong.
- Exclusions: Do NOT walk the full "three ways an interface lies" framework (confidence/capability/tone) or the Tay and Snapchat cases — those are a separate video. Skip Streamlit-vs-Gradio entirely. One bullet, one number, one crater.
- Score: 9/10

slate cut 

## Candidate 05 — Why a milkshake's real competitor is a banana
- Source: `books/branding-and-ai/chapters/04-the-brand-audience.md`
- Production mode: Doodle
- Hook: A milkshake's real competitor turned out to be a banana — once someone asked the right question.
- Core idea: A chain wanted more milkshake sales; demographic and psychographic segmentation found nothing actionable. Christensen's team asked what JOB customers hire the milkshake to do. Observation showed most were bought at 7am by lone commuters — the job was "make my boring commute tolerable and keep me full till lunch without a mess." The competitor was a banana, a bagel, a granola bar. Design flips instantly: thicker (lasts), wider straw, faster to dispense.
- Visual object: A demographic grid of age/income cells that dissolves and re-forms into one 7am highway scene with a one-handed commuter; the straw widens and the shake thickens on cue.
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: None.
- Exclusions: Cut the general "segmentation dimensions" tour and the Spence signaling "for everyone" thread (that is its own idea we chose not to run). Do not define jobs-to-be-done as a framework — just show the reframe happen. No second example.
- Score: 9/10

slate cut 

## Candidate 06 — Why changing one picture on the carton cost Tropicana $30 million in two months
- Source: `books/branding-and-ai/chapters/05-brand-archetypes-as-a-system.md`
- Production mode: Mixed
- Hook: Tropicana swapped one image on the carton and lost $30 million in two months — regular buyers just walked past it.
- Core idea: The recognition asset is the accumulated pattern of touchpoints that lets a shopper's eye snap to your product on a crowded shelf at 8am without conscious thought. Tropicana's 2009 redesign replaced the orange-with-a-straw with a plain glass of juice; sales dropped 20% ($30M+) and the design was rolled back in under two months. The asset is invisible until it is destroyed.
- Visual object: The orange-and-straw carton with shopper eyes snapping to it instantly; it morphs to the glass-of-juice redesign and the eye-snap lines fade as the recognition glow drains away.
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: None.
- Exclusions: Cut the Gap-logo (six-day rollback) and New Coke parallels — one case only. Do not branch into the full archetype system or the "good design, wrong archetype" analysis (Chapter 9's framing). Keep it to eye-snap → redesign → drain.
- Score: 9/10

slate cut 

## Candidate 07 — Why the most important feature is the one you refuse to build
- Source: `books/branding-and-ai/chapters/20-shipit-product-requirements-and-scope.md`
- Production mode: Doodle
- Hook: The most important feature in your product is the one you refuse to build — even when someone waves $100,000 at you.
- Core idea: The "$100,000 no" is not refusing out-of-scope junk (that is free). It is declining a feature a real user asks for, with a real argument, because including it would compromise the core. Example: adding multi-user accounts to a personal-intelligence tool. The day you build multi-user, every later decision — permissions, audit trails, admin — becomes a team-platform decision, and you have stopped building the personal tool. Linear literally declined enterprise contracts to protect this.
- Visual object: An in/out ledger where the "personal tool" stays coherent as a $100K feature is pushed to the "out" column — then, when accepted, the whole product forks into a messier "team platform" with a cascade of new required decisions.
- Manim move: split
- Short-form fit: Strong
- Prerequisites: Rough idea of product scope / feature requests.
- Exclusions: Cut the "coherence compounds into brand identity" trajectory graph (related but a second beat) and the MVP "validated learning" definition. Do not generalize to Stripe's refusal list — one product, one $100K no.
- Score: 9/10

slate cut 

## Candidate 08 — Why people reliably pay more for the identical pill
- Source: `books/branding-and-ai/chapters/02-what-a-brand-is-equity.md`
- Production mode: Doodle
- Hook: Same molecule, same dose — but people reliably pay more for one bottle, and that gap is worth billions.
- Core idea: Take chemically identical acetaminophen — one branded, one generic — price them apart, and a measurable fraction of buyers pay more for the branded one, every time, across categories. That price delta is brand equity made visible. It is an asset because it produces future cash through premium pricing, retention, and forgiveness (benefit of the doubt when something breaks) — none of which comes from a logo.
- Visual object: Two identical pill bottles with price tags; the branded one's price ticks upward and the widening gap fills in, labeled "equity."
- Manim move: split
- Short-form fit: Strong
- Prerequisites: None.
- Exclusions: Do NOT climb the Keller resonance pyramid (separate idea) or define brand-as-asset accounting. Skip "forgiveness/retention" as a list — mention forgiveness in one line only. Two bottles, one widening gap.
- Score: 9/10

slate cut 

## Candidate 09 — Why announcing your values can be more dangerous than staying silent
- Source: `books/branding-and-ai/chapters/15-brand-ethics-purpose-and-sustainability.md`
- Production mode: Manim visualization
- Hook: Announcing your values out loud can hurt you more than saying nothing — here is the math.
- Core idea: A values claim creates a background standard you are later judged against. A brand that claims nothing and then has a supply-chain scandal has a crisis; a brand that claimed to LEAD on supply-chain ethics and has the same scandal has a trust collapse. The claim inflates the expectation; the violation deflates it by the full inflated amount — so the net damage is worse than having said nothing.
- Visual object: Two trust lines on one time axis, both struck at the same scandal event; the silent brand dips and recovers, the values-claiming brand drops further and recovers slower — the gap labeled "the cost of hypocrisy."
- Manim move: split
- Short-form fit: Strong
- Prerequisites: None.
- Exclusions: Cut Patagonia "Don't Buy This Jacket" and the EU greenwashing-ban material (both are separate videos). Do not turn it into a "how to do purpose right" checklist. Two lines, one scandal, one gap.
- Score: 9/10

slate cut 

## Candidate 10 — How the password-reset email exposes your brand's real voice
- Source: `books/branding-and-ai/chapters/11-brand-experience-and-touchpoints.md`
- Production mode: Doodle
- Hook: Your warm, friendly brand voice is a claim — and the cold password-reset email is where customers catch the lie.
- Core idea: A brilliant positioning statement that contradicts the support experience loses to the support experience, every time — people believe what happens to them, not what you claim. A warm marketing voice that turns cold and formal in the reset email creates a seam; customers feel seams before they can name them, and that cold email is the brand's real voice being revealed. The support ticket, cancellation flow, and 2am error message are all brand.
- Visual object: A warm rounded ad on the left morphs into a cold formal support email on the right; a jagged seam tears down the middle where the two voices meet.
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: None.
- Exclusions: Cut the coffee value-ladder and the moments-of-truth spend-allocation ideas from this chapter — separate videos. Do not enumerate every touchpoint; one warm surface, one cold email, one seam.
- Score: 9/10

slate cut 

## Candidate 11 — Why a thousand free blog posts would make you poorer
- Source: `books/branding-and-ai/chapters/12-content-media-and-campaigns.md`
- Production mode: Doodle
- Hook: AI can write you a thousand blog posts for the price of one — and that would make you poorer.
- Core idea: As the cost of a competent paragraph collapses toward zero and everyone floods every channel with fluent generic copy, the scarce thing is no longer content — it is the reason to publish this and the judgment to make it good and true. AI raises the value of exactly what it cannot supply: editorial judgment. Flooding the channel buries you in the same noise as everyone else.
- Visual object: A flood of identical gray post-tiles pouring in and burying the screen; a single human-judgment "filter" lens catches the one true, on-voice piece while the rest wash away.
- Manim move: drain
- Short-form fit: Strong
- Prerequisites: Awareness AI can mass-produce text.
- Exclusions: Cut reach-vs-frequency and the PESO integration model (separate ideas). Do not moralize about AI writing in general — stay on the flood-and-filter economics. One flood, one filter.
- Score: 9/10

slate cut 

## Candidate 12 — Why Pepsi wrote 27 pages to move a stripe a few degrees
- Source: `books/branding-and-ai/chapters/09-visual-identity-systems.md`
- Production mode: Doodle
- Hook: Pepsi wrote a 27-page document invoking Einstein and the Mona Lisa — to justify tilting a stripe a few degrees.
- Core idea: In 2008 the Arnell Group justified a tiny logo tweak with a rationale citing the Golden Ratio, the Mona Lisa, the Parthenon, the Vitruvian Man, relativity, and Earth's gravity. The mechanism: the brand had never committed to an archetype specific enough to make a design choice right or wrong, so designers reached for borrowed authority. The Mona Lisa did not authorize the logo; the logo authorized nothing.
- Visual object: The logo barely tilts in the center while grandiose references (Parthenon, Vitruvian Man, gravity diagram) pile on around it — then all the borrowed authority evaporates, leaving the tiny unchanged stripe.
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: None (the absurdity is self-evident).
- Exclusions: Cut the WCAG contrast-ratio audit and the Tropicana redesign (Candidate 06 owns Tropicana) from this chapter. Do not teach how to pick an archetype; the joke is the emptiness. Pile on, then drain.
- Score: 9/10

slate cut 

## Candidate 13 — Why your brand should be Yoda, not Luke
- Source: `books/branding-and-ai/chapters/10-brand-voice-and-storytelling.md`
- Production mode: Doodle
- Hook: Every founder tells their brand story wrong — they cast themselves as Luke, when they should be Yoda.
- Core idea: Miller's StoryBrand insight is positional: the customer is always the hero, the brand is the guide. Yoda does not go to the Death Star — Luke does. Technical founders default to brand-as-hero stories (we fought hard problems, we built something remarkable) — sometimes fine for raising capital, but weak for selling, because a customer cannot identify with a story whose hero is someone else.
- Visual object: The same product with two story arcs side by side; the "hero" spotlight slides off the brand-figure and onto the customer-figure, the brand shrinking into the guide role.
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: Loose Star Wars familiarity (Luke = hero, Yoda = mentor).
- Exclusions: Cut the Pepsi/Kendall-Jenner three-layer-mismatch case and the cadence-vs-volume idea (both separate). Do not walk the full hero's-journey structure — just the spotlight swap.
- Score: 9/10

slate cut 

## Candidate 14 — How a hiring signal died the moment 82% of people could fake it
- Source: `books/branding-and-ai/chapters/01-the-creative-engineer.md`
- Production mode: Manim visualization
- Hook: This signal used to get you hired — then 82% of people could fake it in an afternoon, and it quietly died.
- Core idea: Spence's signaling theory: a signal only works while it is costly to fake. In 2010, "a working app on GitHub" cost about six weekends of real craft, so recruiters used it like GPA. Then the Peng et al. RCT (control 161 min vs. Copilot 71 min to write an HTTP server — a 56% cut) plus the 2024 Stack Overflow survey (82% of developers now use AI for code) meant the signal did not vanish — it POOLED. A separating equilibrium collapsed into a pooling one: everyone produces it, so it predicts nothing.
- Visual object: Two candidate pools (high/low capacity) on either side of a "GitHub repo" gate; the gate's cost bar drops and both pools slide into one indistinguishable blob.
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: Rough idea of a resume "signal" to employers.
- Exclusions: Cut the Anthropic-vs-OpenAI same-DNA-different-brand story from this chapter (a separate idea). Do not fully teach separating vs pooling equilibria with notation — show the two pools merging. One signal, one gate, one collapse.
- Score: 9/10

slate cut 

## Candidate 15 — Why deleting 1,200 of your own brands makes more money
- Source: `books/branding-and-ai/chapters/07-brand-architecture-and-portfolio.md`
- Production mode: Manim visualization
- Hook: This company deleted 1,200 of its own brands — and made more money per brand.
- Core idea: More brands usually means less total value. Unilever's "Brand Imprint" program cut the portfolio from about 1,600 brands to 400 — and revenue per brand rose. Portfolio bloat splits budget and attention across brands that cannibalize each other, while most of them free-ride on slowly depreciating equity. Pruning concentrates resources on the brands that actually compound.
- Visual object: A dense grid of ~1,600 brand tiles that thins to 400 while a single "value per brand" bar rises as tiles disappear.
- Manim move: drain
- Short-form fit: Strong
- Prerequisites: None.
- Exclusions: Cut branded-house-vs-house-of-brands (Samsung fire) and sub-brand-vs-endorsed-brand from this chapter — separate ideas. Do not name the individual brands cut. Tiles drain, bar rises.
- Score: 9/10

slate cut 

## Candidate 16 — Why the clearest brand name is the one you can't own
- Source: `books/branding-and-ai/chapters/08-naming-trademark-and-brand-protection.md`
- Production mode: Manim visualization
- Hook: The clearer and more descriptive your brand name, the less the law will let you own it.
- Core idea: The Abercrombie spectrum — the property that makes a name instantly understandable is exactly what makes it impossible to own. "Software" (generic) is never protectable; descriptive is weak; protection only really begins at suggestive; arbitrary ("Apple" for computers) and fanciful ("Kodak") are strongest. Apple had to earn its meaning — and now no one else in computing can use it. Legibility and exclusivity are inversely crossed.
- Visual object: A horizontal spectrum Generic → Fanciful with two opposing bars — legibility falling, protectability rising — crossing in an X as marks (Software, Netflix, Apple, Kodak) slide into place.
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: Vague sense that brand names can be trademarked.
- Exclusions: Cut the "domain ≠ trademark, three separate rights" idea and the likelihood-of-confusion search-clearance point (both separate videos). No legal procedure detail — just the crossing curves and four example marks.
- Score: 9/10

slate cut 

## Candidate 17 — How burning $100M and 75% of its market share won the category
- Source: `books/branding-and-ai/chapters/16-crisis-and-reputation-management.md`
- Production mode: Manim visualization
- Hook: They torched $100 million and watched market share fall by 75% on purpose — a year later they owned the category again.
- Core idea: In 1982 Johnson & Johnson pulled 31 million bottles of Tylenol nationwide (a $100M decision no financial model could justify) after cyanide-laced capsules killed seven. Share collapsed from 35% to 8%, then recovered to 30% by 1983 and beyond pre-crisis levels by 1984. The mechanism: action first, then words — the words explaining the irreversible action, not substituting for it — and it worked because the 1943 Credo (customers before shareholders) predated the crisis by nearly forty years.
- Visual object: A single market-share line: 35%, crashing to 8%, then climbing back above the start — with the $100M recall marked at the bottom of the crash.
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: None.
- Exclusions: Cut the SCCT responsibility-matching framework (BP "I'd like my life back") and the United-silence case — both are separate videos. Do not enumerate crisis-response strategy types; one line, one recovery.
- Score: 8/10

slate cut 

## Candidate 18 — Why the Chevy Nova "no va" story in your textbook is a myth
- Source: `books/branding-and-ai/chapters/17-global-and-cross-cultural-branding.md`
- Production mode: Doodle
- Hook: The Chevy Nova didn't flop in Latin America because "no va" means "doesn't go" — that famous story is fake, and it's in your marketing textbook.
- Core idea: The book corrects a misconception taught as fact: many of the most-repeated cross-cultural blunder stories are apocryphal. The GM Nova / "no va" tale is contested — the car actually sold reasonably well, and "nova" is not naturally parsed as "no va" in Spanish. The Coors "Turn It Loose"/diarrhea story has uncertain sourcing. The real principle (test with native speakers before you launch) survives without the invented anecdotes.
- Visual object: A wall of legendary "blunder" case cards, each getting a MYTH stamp as it is inspected — leaving one true principle standing.
- Manim move: reveal
- Short-form fit: Strong
- Prerequisites: Ideally has heard the Nova legend (the video also works as first exposure).
- Exclusions: Cut the translation/localization/transcreation ladder and the McDonald's glocalization rings — separate ideas. Do not debunk more than two myths; stamp, stamp, and land the surviving principle.
- Score: 8/10

slate cut 

## Candidate 19 — How one 2017 portfolio still gets credit on 6,000 sites its author never saw
- Source: `books/branding-and-ai/chapters/18-portfolio-as-product.md`
- Production mode: Mixed
- Hook: She built one portfolio in 2017 — and it is still getting her credit on 6,000 websites she has never seen.
- Core idea: Brittany Chiang's portfolio repo accumulated over 9,000 stars and 6,000 forks; her name traveled into commit histories and footer credits of sites she never touched. A portfolio pays off through three channels — direct hiring (short, visible, where most people stop), indirect reference (someone mentions you months later, invisible to you), and template effects (people fork your design, carrying your name on autopilot). The gap between "adequate" and "designed" is roughly twenty hours; the return differential is a decade.
- Visual object: A single portfolio node fanning into three arrows — a short visible one (hiring), a long dashed one that fires months later (referral), and one that keeps branching by itself (forks carrying her name).
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: Loose idea of GitHub forks / portfolios.
- Exclusions: Cut the "three projects beat ten" negative-space rule and the metric-makes-the-claim case-study idea (both separate). Do not explain what forking is in depth; show the branches multiply on their own.
- Score: 8/10

slate cut 

## Candidate 20 — Why the ugly Airbnb deck raised $600K by making one argument, not ten
- Source: `books/branding-and-ai/chapters/19-professional-presence-and-launch.md`
- Production mode: Doodle
- Hook: This plain, ten-slide deck raised $600,000 — because it only made one argument, not ten.
- Core idea: Most pitches make ten separate pleas. The Airbnb deck made ONE argument where each slide leaned on the previous: problem implied solution, solution implied market, market implied business model, business model implied team. The audience left with one thing in their heads because there was only one thing to hold — plain typography, simple bar charts, no flourishes, and it worked anyway.
- Visual object: Ten slide-boxes connected by "implies" arrows forming one continuous chain — versus ten disconnected boxes each shouting a different plea.
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: Rough idea of a pitch deck.
- Exclusions: Cut the "87 bookings vs strong interest" specificity point and Kawasaki's 30-point-font rule (both separate ideas from this chapter). Do not teach deck design tips; draw the one implication chain link by link.
- Score: 8/10

slate cut 

## Candidate 21 — Why the Same AI Model Built a Developer Tool AND a Developer Replacement
- Source: `branding-and-ai/chapters/03-the-ai-toolchain-cowork-codex-madison.md`
- Topic: BRANDING AND AI
- Hook: Two companies took the same frontier AI model and built completely opposite products — one trusted by developers, one that developers resist.
- Key case: In 2024, Cursor and Devin both launched products built on the same frontier language models for software work. Cursor put AI inside the IDE with the developer approving every suggestion; senior developers trust it with production code. Devin placed AI in an isolated cloud sandbox running autonomously on tasks while the developer moved on. Same capability. Opposite brand positions, opposite user trust profiles.
- The Question: Two products share the same underlying model, the same general task, the same target user. One earns deep trust; one earns skepticism. The capability is identical. Why?
- Core idea: Where you place the human in the loop is a brand decision. Cursor's tight control loop signals "we trust developers"; Devin's loose loop signals "we handle the work so you don't have to." The architecture encodes a theory of risk and a theory of what the human is for — customers feel that theory before they can name it.
- Visual object: A horizontal control spectrum from "user in full control / augmentation" at the left to "system autonomous / delegation" at the right — Cursor at left, Devin at right, Madison left-of-center — each position annotated with brand stance and dominant failure mode
- Manim move: scan (a marker sweeps across the spectrum; each position reveals its brand stance and failure mode)
- Example seed: A solo developer chooses between two tools for a database migration. Product A (augmentation) suggests steps in her IDE; she reviews each. Product B (autonomous) opens a PR forty minutes later — with four architectural decisions she would have made differently, two of which will be expensive to undo. She paid for speed and received work she now has to reverse.
- Length band: 3–5 min
- Still lanes: geo (control-spectrum diagram with annotated positions), c2v (contrasting tool interfaces)
- Prerequisites: Rough awareness that coding assistant tools like Cursor or Copilot exist
- Exclusions: No ReAct loop mechanics; no four-meanings-of-agent taxonomy; no Madison five-layer architecture walkthrough. One spectrum, two endpoints, one principle.
- Score: 9/10

slate cut 

## Candidate 22 — Why Stripe's Most Important Feature Is One They Never Built
- Source: `branding-and-ai/chapters/06-brand-strategy-and-positioning.md`
- Topic: BRANDING AND AI
- Hook: The most recognizable brand in developer infrastructure is defined less by what it built than by fifteen years of deliberate refusals.
- Key case: Stripe declined enterprise sales processes for the first several years of existence. The product was self-serve; developers found it, integrated it, brought it into their companies without a sales call. This single refusal locked out enterprise-sales-first payment competitors who dominated the larger-merchant market — and locked in exactly the developer audience Stripe wanted to serve.
- The Question: Two companies ship identical payment products in 2010. One builds an enterprise sales team, courts large merchants, adds features on request. The other declines a sales team and lets only developers self-serve. Fifteen years later, the second one is more legible and more trusted. How?
- Core idea: Brand coherence is produced by consistency of constraint — what you decline — not by what you produce. Any single Stripe refusal could have been a one-time choice. The pattern of refusals, sustained over fifteen years, is the brand. The no-list is not a limitation; it is the mechanism that converts individual product decisions into a recognizable identity.
- Visual object: Two load-bearing columns — what Stripe built (features, expansions) on the left, what Stripe declined (enterprise sales, rapid product proliferation, competitor-bashing content, marketing claims without documentation support) on the right — the right column shown as equally weight-bearing for brand recognition
- Manim move: accumulate (Stripe's refusals pile up in the right column over time; the pattern becomes visible as brand identity)
- Example seed: A student ships an AI career-intelligence tool. She writes a no-list: no consumer version, no export-to-spreadsheet, no "just ask anything" interface. After eighteen months, a recruiter says "you're the tool that stays in its lane." A reputation built not from what she added but from what she refused.
- Length band: 3–5 min
- Still lanes: geo (two-column accumulation diagram), c2v (developer working with Stripe docs scene)
- Prerequisites: Rough awareness of Stripe as a payment infrastructure company
- Exclusions: No seven-component brand strategy walkthrough; no archetype-shadow analysis; no naming or one-page document methodology. One mechanism — the no-list — shown through one case.
- Score: 9/10

slate cut 

## Candidate 23 — Why the AI Wage Premium Doesn't Go to the People Who Switched Careers to Get It
- Source: `branding-and-ai/chapters/97-fundamental-themes.md`
- Topic: BRANDING AND AI
- Hook: The AI wage premium is doubling every year — and almost everyone is pursuing it in the wrong direction.
- Key case: PwC's 2025 Global AI Jobs Barometer analyzed approximately one billion job ads. AI-skilled workers commanded a 56% wage premium in 2024, doubled from 25% the prior year. The critical specification: the premium goes to AI-fluent domain experts who stayed in their domain — not to lawyers who retrained as engineers, or teachers who pivoted to EdTech.
- The Question: AI is supposed to commoditize domain expertise. The labor market shows AI-skilled workers earning 56% more. The obvious move: become an AI engineer. The data: stay in your field. Why does the premium go to people who didn't switch?
- Core idea: The premium pays for the irreducibly human capacities AI cannot replicate — plausibility auditing, causal reasoning, institutional judgment, accountability. These capacities are built through years of domain practice. A lawyer who switched to engineering left those capacities behind and joined a crowded credential pool. A lawyer who added AI fluency carries both — domain judgment AI cannot fake, plus the tools to execute — and that's what the market is pricing.
- Visual object: Two arrows diverging from "your domain" — the wrong arrow points toward "become a technologist" (dead-ends or narrows for many fields: communications, design, education, healthcare); the right arrow points toward "your domain + AI superpowers" (domain identity preserved, the 56% path)
- Manim move: split (the two arrows diverge from the same origin; the wrong one narrows to a crowded point, the right one widens)
- Example seed: A hospital billing specialist and a CS senior both complete the same AI certification. The billing specialist uses AI to cut claim rejection rates from 18% to 4% — work only she could evaluate. The CS graduate's identical certificate joins a commodity pool of identical credentials. She earns the 56% premium; he explains why his cert should stand out.
- Length band: 2–3 min
- Still lanes: geo (two-arrow diagram), c2v (domain professional working with AI tools)
- Prerequisites: Awareness that AI is changing job markets; basic idea of a wage premium
- Exclusions: No full seven-tier irreducibly human taxonomy; no BDNF/neurobiological learning mechanism; no AI+1 master's program pitch. One data point (56%), one arrow diagram, one principle.
- Score: 9/10

slate cut 

## Candidate 24 — Why Pepsi's Most Expensive Ad Failed on Three Different Levels at Once
- Source: `branding-and-ai/chapters/10-brand-voice-and-storytelling.md`
- Topic: BRANDING AND AI
- Hook: Pepsi pulled a multi-million-dollar ad within 24 hours — and the failure wasn't political. It was architectural.
- Key case: Pepsi's April 2017 Kendall Jenner ad: a Hero's Journey story shape (wrong for the Innocent/Jester brand), borrowed protest and police-confrontation imagery owned by the Outlaw archetype (cultural content Pepsi has no history of earning), and the brand cast as the magical conflict resolver (a Magician role Pepsi hasn't established). Three simultaneous mismatches. Pulled in 24 hours.
- The Question: The ad had professional production, a famous spokesperson, and plausible intentions. It was pulled in 24 hours and became a textbook brand failure. Something made millions of viewers feel it was profoundly wrong before they could articulate why. What?
- Core idea: Archetype-narrative mismatch operates on three levels simultaneously. The Innocent archetype promises uncomplicated joy — it structurally cannot hold social conflict. The Outlaw archetype earns protest imagery through a history of rebellion; borrowed Outlaw content without Outlaw credentials reads as exploitation. Each mismatch independently would have strained; all three made the dissonance overwhelming. Audiences felt the three-layer failure before they could name any one layer.
- Visual object: Three puzzle pieces that don't fit together: (1) story shape attempted — Hero's Journey, (2) brand's archetype — Innocent/Jester, (3) cultural content borrowed from — Outlaw. Placed side by side, the misfit gaps labeled and annotated.
- Manim move: compare (the three layers placed and compared; the gaps between them labeled)
- Example seed: A fintech startup (archetype: Sage, known for technical rigor) runs a social campaign using Rebel energy — "disrupting the outdated banks" — with confrontational copy and an edgy aesthetic. The developer-analyst audience disengages. Not because they dislike disruption, but because the Rebel's confrontational frame is tonally inconsistent with the Sage's evidence-first promise. The campaign needed the wrong archetype to land.
- Length band: 3–5 min
- Still lanes: geo (three-layer comparison diagram), c2v (Innocent brand identity elements vs. Outlaw scene)
- Prerequisites: General awareness of brand archetypes; familiarity with the fact that the 2017 Pepsi ad was controversial
- Exclusions: No Bud Light or Jaguar case analysis (those are Candidates 28 and separate); no full archetype taxonomy; no Miller StoryBrand framework walkthrough. Three layers, one failure, one diagnostic.
- Score: 9/10

slate cut 

## Candidate 25 — How a Wildly Successful Campaign Quietly Destroys What It Was Trying to Build
- Source: `branding-and-ai/chapters/13-measuring-brand-equity-and-impact.md`
- Topic: BRANDING AND AI
- Hook: A deep-discount campaign can turn every number on your marketing dashboard green — while eroding the one asset those numbers are supposed to measure.
- Key case: A brand runs a deep-discount campaign. Conversions spike, CAC drops, revenue for the period looks healthy — every performance metric is green. Meanwhile, the discount trains existing customers to wait for the next sale, degrades price premium, and associates the brand with cost-savings rather than quality. Brand metrics, tracked on their slower six-to-twelve-month cycle, show preference and price premium declining. The dashboard declared success; the brand was bleeding.
- The Question: Every performance metric moved in the right direction. Leadership approved the strategy. Two years later, margin collapsed. The campaign "worked." What happened?
- Core idea: Brand metrics and performance metrics move on different timescales. Performance responds in days to weeks; brand equity moves in months to years. The "patience gap" is the interval between a brand-eroding action and when the damage surfaces in business outcomes. A dashboard measuring only performance metrics turns brand-destroying decisions into apparent wins — until the lag runs out and the equity is gone.
- Visual object: Two lines on a shared 24-month time axis — a performance metric (fast-moving, volatile, spiking at the discount event) and a brand equity metric (slow-moving, smooth, declining after the same event) — diverging over time, the gap between them labeled "the patience gap"
- Manim move: split (the two lines diverge from the discount-campaign event; the performance line spikes while the brand line begins a long slow decline)
- Example seed: A specialty coffee brand with a Sage archetype runs 40%-off flash sales for three Q4s to hit revenue targets. Year four: a repeat customer emails — "I only buy when there's a sale now — is that wrong?" She isn't wrong. The brand trained her. The price premium that was the entire margin thesis has evaporated in the performance dashboard's blind spot.
- Length band: 2–3 min
- Still lanes: geo (two-line diverging time series), c2v (brand campaign / flash-sale scene)
- Prerequisites: Basic idea that businesses track metrics; rough awareness of conversion rates and brand equity
- Exclusions: No attribution modeling; no multi-touch attribution vs. marketing-mix modeling taxonomy; no NPS discussion (Candidate 29). Two lines, one divergence, one mechanism.
- Score: 8/10

slate cut 

## Candidate 26 — Why Changing Your Logo Destroys Something That Wasn't in the Brand Book
- Source: `branding-and-ai/chapters/14-brand-management-governance-and-rebranding.md`
- Topic: BRANDING AND AI
- Hook: Gap replaced its logo and reversed the decision in six days — not because the new design was ugly, but because it destroyed something that never appeared in any brand document.
- Key case: In October 2010, Gap replaced its iconic navy-box Spencerian logo with a minimalist Helvetica wordmark. The internet revolt was immediate. Gap reversed the decision in six days. The new design was professionally executed. What it lacked was twenty-plus years of recognition patterns encoded in millions of customers' minds — patterns that no brand book had ever formally recorded.
- The Question: Gap's new logo was competent. The company rolled it back in six days. Nothing was legally wrong with the new mark. What exactly did it destroy — and where did that thing live?
- Core idea: Brand equity is a property of customer mental models, not of the brand itself. Accumulated recognition cues live in millions of heads. A rebrand doesn't update those heads — it strands the equity encoded in them. The more recognition cues that change simultaneously, the more customers are left with no mental anchor to the new mark. The value of the old logo wasn't in the file — it was in the pattern that two decades of exposure had built in people.
- Visual object: Customer-mind nodes glowing with the recognition pattern of the old logo; the new logo arrives; the glow fades to dark in each node; the equity isn't transferred to the new mark — it's stranded in a mark no one uses anymore
- Manim move: decay (the glow of recognized cues fades from customer-mind nodes as the old mark is withdrawn)
- Example seed: A student renames and redesigns her portfolio site entirely: new URL, new typeface, new color, new name. A professor who was about to recommend her to a hiring manager searches her old URL and hits a 404. The recommendation never happens. The equity — her name in the professor's working memory, connected to her work — was stranded in a URL that no longer exists.
- Length band: 2–3 min
- Still lanes: geo (mind-node glow diagram), c2v (before/after logo pair with recognition cue annotations)
- Prerequisites: Loose awareness of what a brand logo is; vague sense that brands build recognition over time through repeated exposure
- Exclusions: No Tropicana case (Candidate 06 owns it); no three-layer archetype mismatch; no refresh-vs-rebrand decision spectrum overview. One rollback, six days, one mechanism.
- Score: 8/10

slate cut 

## Candidate 27 — Why AI Can Write a Convincing Causal Argument Without Understanding Cause and Effect
- Source: `branding-and-ai/chapters/97-fundamental-themes.md`
- Topic: BRANDING AND AI
- Hook: AI has processed more text containing "because," "caused," and "led to" than any human ever will — and that's exactly why you shouldn't trust its causal claims.
- Key case: A marketing analyst asks an AI to explain why a Q3 campaign outperformed Q2. The AI produces a confident three-paragraph analysis: "the messaging resonated with the target demographic," "this led to higher engagement," "which caused the conversion lift." Every sentence uses causal grammar fluently. None of it distinguishes the campaign's effect from the Q3 seasonal tailwind that also happened that quarter. The analyst presents it. A colleague corrects it in ninety seconds.
- The Question: AI uses causal language — "because," "therefore," "leads to" — correctly in context every time. Expert reviewers say AI cannot reason causally. These seem to contradict each other. Which is right, and why?
- Core idea: AI is a causal parrot. It pattern-matches on the form of causal arguments without performing the inferential work. Genuine causal reasoning requires variable selection, causal-graph orientation, and identifying what to hold constant — none of which are derivable from predicting the next token. AI produces the language of causality; the thought behind that language must come from a human.
- Visual object: An AI output on screen — confident causal prose with "because" and "therefore" connectors. The view then pulls back to reveal what's underneath: an undirected causal graph with question marks on every edge, unmeasured confounders floating beside the prose, and a "variable selection" step that was never performed. The surface is coherent; the inferential structure is empty.
- Manim move: reveal (first the confident causal surface; then the missing inferential structure beneath it)
- Example seed: A student uses AI to write a memo explaining why a DTC brand's churn fell after a new onboarding sequence launched. The memo is confident and specific. Her instructor asks which variables she controlled for — the price reduction, the competitor who exited the market, the seasonal cohort shift that also happened that quarter. The student has no answer. Neither does the AI that wrote the memo.
- Length band: 3–5 min
- Still lanes: geo (causal graph with question marks, surface vs. structure split diagram), c2v (AI screen with confident text overlay)
- Prerequisites: Loose awareness that AI generates text; basic intuition that "because" makes a stronger claim than "is correlated with"
- Exclusions: No Markov equivalence formalism; no Pearl do-calculus notation; no full seven-tier irreducibly human taxonomy. One parrot, one confident claim, one hollow structure beneath it.
- Score: 8/10

slate cut 

## Candidate 28 — Why Bud Light's Attempt to Include More People Left Almost Everyone Out
- Source: `branding-and-ai/chapters/10-brand-voice-and-storytelling.md`
- Topic: BRANDING AND AI
- Hook: Bud Light tried to expand its community — and instead of growing the "us," it fractured it.
- Key case: In April 2023, Bud Light partnered with trans influencer Dylan Mulvaney for a single sponsored can. The Everyman brand — whose entire heritage is "you belong here, as you are," built on mainstream accessibility and shared belonging — had no Magician foundation for a Transformation story. Bud Light lost its position as the best-selling beer in the US in the months that followed.
- The Question: Bud Light made a single, small partnership gesture intended to include more people. Many brands expand their communities successfully. Bud Light lost market leadership. The partnership was one can, not a campaign overhaul. What was architecturally different?
- Core idea: Everyman brands signal membership in a stable "us." Transformation stories require a Magician archetype — demonstrated vision and earned trust. An Everyman brand that attempts a Transformation story without that foundation doesn't expand "us"; it signals that the existing "us" is being replaced, without offering the old members an invitation to whatever comes next. The failure was architectural, not political: wrong story shape, wrong archetype for the shape.
- Visual object: A stable "us" membership circle; a Transformation signal arrives without Magician grounding; the circle doesn't expand — it fractures into a smaller new group and an unmoored original group, neither coherent
- Manim move: split (the circle fractures rather than expanding; the split labeled "wrong story shape for this archetype")
- Example seed: A developer community newsletter (archetype: Everyman — "this is for anyone who builds things") announces a flagship series interviewing only FAANG executives. Instead of elevating the community, the readership interprets it as: this is now for people at those companies. Churn in the next sixty days is the signal that "us" became smaller, not larger.
- Length band: 2–3 min
- Still lanes: geo (membership circle fracture diagram), c2v (inclusive community scene)
- Prerequisites: Basic awareness of the 2023 Bud Light controversy; loose understanding of brand archetypes
- Exclusions: No cultural politics or ideology analysis — the lesson is architectural, not political; no comparison to Pepsi or Jaguar (separate candidates); no full archetype taxonomy. One fracture, one mechanism.
- Score: 7/10

slate cut 

## Candidate 29 — How the "One Number You Need to Grow" Became the One Number That Predicts Nothing
- Source: `branding-and-ai/chapters/13-measuring-brand-equity-and-impact.md`
- Topic: BRANDING AND AI
- Hook: For twenty years, companies have reported NPS to leadership as a growth forecast. The research that justified it doesn't hold up under replication.
- Key case: Fred Reichheld's 2003 Harvard Business Review article introduced NPS as "the one number you need to grow," backed by data showing NPS correlated with revenue growth. Companies adopted it universally. Then Keiningham et al. (2007) tested the claim on a broader dataset — no evidence NPS outperforms other satisfaction metrics as a growth predictor. The metric survived in nearly every corporate dashboard anyway.
- The Question: A metric is launched with a compelling study showing it predicts growth. A rigorous replication finds no evidence of the effect. The metric is still reported to boards as a growth forecast. How does a statistically contested metric dominate an entire field of practice for two decades?
- Core idea: NPS measures willingness to recommend — not actual recommendations, not revenue, not growth. The compression from a 0–10 scale to three buckets discards information. Cultural calibration means a score of 30 in Japan ≠ 30 in the US. The metric survived because organizational processes were built around it — not because the evidence held. A number simple enough for a headline survives the replication crisis that a regression coefficient does not.
- Visual object: A 0–10 survey scale compressed dramatically into three colored zones (detractor/passive/promoter); then an NPS trend line rising confidently on one chart beside a flat or noisy revenue line on another — the gap between the 2003 claim and the 2007 replication labeled
- Manim move: compare (the confident NPS line on one side; the flat growth correlation on the other; the gap between the promise and the evidence)
- Example seed: A startup's brand team reports NPS rose from 24 to 41 after shipping a free feature. Leadership approves a growth initiative. Q2 revenue is flat. The NPS respondents are hobbyist users on the free tier; the paying segment never took the survey. Nobody asked: if NPS rose 20%, what decision would you make differently?
- Length band: 2–3 min
- Still lanes: geo (compression-to-three-zones diagram, two-panel correlation chart), c2v (boardroom presentation scene)
- Prerequisites: Awareness that companies use customer satisfaction surveys; vague idea that surveys produce scoreable metrics
- Exclusions: No attribution modeling or MMM discussion; no full brand tracking methodology; no patience-gap concept (Candidate 25). One metric, one failed replication, one gap between headline promise and evidence.
- Score: 7/10

slate cut 

## Candidate 30 — Why "Eco-Friendly" Is Now Illegal to Say in Europe Without Proof
- Source: `branding-and-ai/chapters/15-brand-ethics-purpose-and-sustainability.md`
- Topic: BRANDING AND AI
- Hook: As of September 2026, printing "eco-friendly" on a product in Europe without documented proof is a regulatory violation.
- Key case: The EU's Empowering Consumers for the Green Transition Directive (ECGT), adopted March 2024, bans two categories of claim from September 27, 2026: generic green claims without substantiation ("eco-friendly," "green," "sustainable," "climate-smart") and product-level "climate neutral" or "net zero" claims based primarily on carbon offsets. A clothing brand that has been printing "sustainable" on its swing tags for five years must now either prove exactly what the word means or remove it.
- The Question: "Eco-friendly" has appeared on products for thirty years. It signals concern without making a specific claim. Now it's a regulatory violation without proof. Why does a vague good-intention word become illegal while the product stays legal?
- Core idea: A generic claim is unverifiable, and an unverifiable claim is now — in EU law — presumptively deceptive. The regulation doesn't require you to be sustainable; it requires that if you claim to be, the claim be specific enough to verify or falsify. "Made with 30% recycled materials, certified by [body]" survives. "Eco-friendly" doesn't. The regulation is the claim-proof discipline written into law — and it applies to AI ethics claims ("responsible AI," "bias-free") on exactly the same logic.
- Visual object: A product tag with "eco-friendly" printed on it beside a claim-proof table with an empty evidence column — then the EU enforcement icon materializes in the evidence cell, with a fine amount where proof should have been
- Manim move: reveal (the claim on the tag; the required proof column expanding beside it; the regulatory consequence appearing at the bottom when proof is absent)
- Example seed: A small American skincare brand launches EU distribution in summer 2026. Their packaging says "naturally sourced, environmentally conscious." Compliance counsel reads the ECGT rules, flags both phrases as generic without certified substantiation, and rewrites the EU-market label. The product is unchanged. The words on the box must be.
- Length band: 2–3 min
- Still lanes: geo (claim-proof table diagram), c2v (product packaging / regulatory document scene)
- Prerequisites: Awareness that brands make environmental marketing claims; basic sense of EU consumer protection regulation
- Exclusions: No Patagonia "Don't Buy This Jacket" analysis (Candidate 09 territory); no backlash dynamics or purpose-washing distinction; no carbon offsetting economics. One banned phrase, one regulation, one mechanism.
- Score: 7/10

slate cut 

<!-- ============================================================= -->
<!-- DELTA PASS 2026-07-17 — new angles the first 30 cards missed. -->
<!-- Focus: 97-fundamental-themes (rich, only 3 of its ideas carded) -->
<!-- and the Introduction (uncarded). No chapter re-covered.        -->
<!-- ============================================================= -->

## Candidate 31 — The Map of What AI Can and Can't Do (Seven Tiers)
- Source: `branding-and-ai/chapters/97-fundamental-themes.md` (The Irreducibly Human Taxonomy)
- Production mode: Manim visualization
- Hook: There's a clean line through every job: machines win the bottom of it, and they're not just weak at the top — they're absent.
- Core idea: The Irreducibly Human Taxonomy sorts cognitive work into tiers. Pattern & association (Tier 1): machines win. Embodied/sensorimotor (Tier 2): constrained by physics. Metacognitive & supervisory (Tier 4): AI is weak. Causal & counterfactual (Tier 5): AI is unreliable. Collective/distributed (Tier 6) and existential/wisdom (Tier 7): AI is absent. The point isn't "AI is bad" — it's that the boundary is PREDICTABLE, and your value concentrates where the machine can't follow.
- Visual object: A vertical ladder of tiers; an "AI capability" fill rises from the bottom and stalls — solid through Tier 1, thinning through 4–5, gone by 6–7 — with the human silhouette owning the top rungs.
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: None
- Exclusions: Do NOT re-teach the friction/memory mechanism (Candidate 01) or the causal-parrot idea in depth (Candidate 27) — name Tier 5 in one beat and move on. One ladder, one boundary.
- Score: 9/10

slate cut 

## Candidate 32 — When Building Got 56% Cheaper, Building Stopped Being the Skill
- Source: `branding-and-ai/chapters/00-introduction.md`
- Production mode: Mixed
- Hook: Microsoft gave 95 developers the same task; half got Copilot. They finished in 71 minutes. The others took 161.
- Core idea: The book's origin experiment. A 56% collapse in the cost of BUILDING means building is no longer the scarce skill — knowing WHAT to build, and making it legible to the people it's for, is. That's a branding problem. The AI+1 division of labor follows: the agent drafts (reformatting, pattern-spotting), the +1 owns the accountable judgment (commit the archetype, approve the voice, clear the claim). Anything the agent generates — a persona, a metric, a citation — is a draft that needs an evidence check.
- Visual object: Two timer bars — 71 min vs 161 min — collapsing to the 56% gap; then the scarce-skill arrow SWINGS from "build" to "what to build," and an AI+1 split shows drafts flowing from the agent while the decision stamp stays in the human's hand.
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: None
- Exclusions: Do NOT reuse the wage-premium angle (Candidate 23) or the hiring-signal-collapse angle (Candidate 14) — this is the build-cost origin + the AI+1 division of labor, nothing about salary or résumés.
- Score: 9/10

slate cut 

## Candidate 33 — Why the Barrier Coming Down Is the Whole Point
- Source: `branding-and-ai/chapters/97-fundamental-themes.md` (The Brutalist Argument)
- Production mode: Mixed
- Hook: For decades the technical barrier decided who got to make things. AI just lowered it — and that's not the threat, it's the liberation.
- Core idea: The Brutalist Argument — when AI removes the technical barrier (the three files, the six principles), the scarce work moves UP to design and judgment. The artist keeps what the tool can't take: taste, the decision of what's worth making, the responsibility for whether it's good. Barrier removal isn't the erasure of craft; it's craft relocating to where it always mattered most.
- Visual object: A wall labeled "technical barrier" lowering; a crowd that couldn't cross now streams over — but a spotlight stays on the one thing the tool didn't hand them: the design decision ("what the artist keeps").
- Manim move: split
- Short-form fit: Strong
- Prerequisites: None
- Exclusions: No deep dive on the three-files/six-principles spec; name it, don't teach it. Do not overlap the AI+1 draft-vs-decide split (Candidate 32) — this is specifically about the BARRIER coming down and what stays scarce.
- Score: 8/10

slate cut 

## Candidate 34 — The Boondoggle Score: Let AI Do What AI Does, and Conduct the Rest
- Source: `branding-and-ai/chapters/97-fundamental-themes.md` (The Boondoggling Argument)
- Production mode: Manim visualization
- Hook: Most "AI failures" aren't the AI failing — they're a human handing the machine the one part it was never good at.
- Core idea: The Boondoggling Argument — separate the work the AI does best from the work the human must conduct, and SCORE the separation. A task with a high boondoggle score is one you've correctly split (AI drafts the pattern-work, you own the judgment); a low score means the seam is in the wrong place. The discipline is the separation itself, not the tool.
- Visual object: A task splitting into two lanes — "AI does best" (pattern, volume, reformatting) and "human conducts" (judgment, taste, sign-off) — with a Boondoggle Score meter that rises as the seam lands correctly and drops when a judgment task is dumped on the model.
- Manim move: split
- Short-form fit: Strong
- Prerequisites: None
- Exclusions: Keep it to the separation principle + the score. No tool-specific (Gru) walkthrough; no overlap with the seven-tier taxonomy (Candidate 31) beyond a one-line nod.
- Score: 8/10

slate cut 

## Candidate 35 — Phase Gates: The Line an Agent Is Not Allowed to Cross
- Source: `branding-and-ai/chapters/97-fundamental-themes.md` (Phase Gates: The Explicit Boundary)
- Production mode: Manim visualization
- Hook: The safest AI workflows all share one feature: an explicit place where the machine stops and waits for a human signature.
- Core idea: Phase Gates make the human-in-the-loop boundary EXPLICIT rather than hoped-for. Work flows autonomously up to a gate — then a named human judgment (approve the archetype, sign off the position, clear the claim) is required before the next phase begins. The gate is what turns "AI drafts" from a risk into a system: nothing consequential ships without the +1's stamp.
- Visual object: A pipeline with a physical gate mid-stream; work accumulates against it, a human stamp drops, the gate opens and flow resumes — versus the no-gate version where an unchecked draft slides straight to "shipped" and turns red.
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: None
- Exclusions: Do not merge with AI+1 (Candidate 32) — that's WHO decides; this is WHERE the decision is forced. One gate, one signature, one pipeline.
- Score: 8/10
