# FACTCHECK — Week 24 topic-video (Gardner's multiple intelligences vs. machines)

Base topic: `claude-for-design/introducing-theoristai` (see `TOPIC-DECISION.md`).

Every claim proposed for the script, with its verification state. **Nothing enters a beat
until its row reads ✅.** Rows marked ⚠️ or ❌ stay in this file so they don't creep back in later.

Verification levels:
- **primary read**: the author's own text was retrieved and read (Gardner's blog, his co-authored
  paper, his co-authored handbook chapter, or a verbatim interview transcript)
- **citing-source read**: a source that quotes or closely paraphrases the primary was read directly
- **metadata**: bibliographic record only (Crossref / OpenAlex). This confirms the paper exists and
  its citation, **not** its findings
- **search-summary**: confirmed only through search-engine synthesis. Must be upgraded before scripting

Status as of 2026-09-26.

---

## Part 0 — What the base topic actually claims

The source folder's substance is three lines (beats `YTV01`, `B01`–`B03` of its `beat_sheet.json`,
credited to Nik Bear Brown, Founder, Humanitarians AI):

| # | Source claim | Verdict | Why |
|---|---|---|---|
| 0.1 | Theorist.ai reframes AI as "not obsolescence — its opposite" | **OPINION, attributed** | This is the article's thesis. It can be quoted as Nik Bear Brown's framing. It is not a factual claim to check |
| 0.2 | "The forklift does not make the human obsolete" | **ANALOGY, attributed** | The source's own argument. It can't be scripted as fact. See Part 5 for how Gardner's own later word ("optional") sits against it |
| 0.3 | Gardner's 1983 framework "did not need to ask which intelligences were endangered by technology, because technology — in 1983 — was not yet a serious competitor to any of them" | **QUALIFY** | (a) Gardner himself later asked exactly this question, repeatedly (Part 3). (b) His own 2024 account says the 1956 Dartmouth-era programs already "carried out mathematical and logical operations which, if carried out by human beings, might have been considered intelligent" (3.4). So "not a competitor to *any*" is too strong for logical-mathematical. (c) The framework was stated in information-processing terms from the start (1.4, 1.5). The defensible version: *in 1983 it was "by no means clear" machines could converse or win strategy games* (Gardner's own phrase, 3.4) |

**Upgraded to primary read, 2026-09-26.** The original essay is ["Introducing Theorist.ai"](https://humanitariansai.substack.com/p/introducing-theoristai),
Humanitarians AI Substack, **March 2026** (the page shows Mar 13 or Mar 14 depending on the viewer's timezone, so "March 2026" is used on screen), **byline "Humanitarians AI"**, subtitle **"Knowing Enough to Distrust the Machine"** (the same essay as `essay-video-ideas.md` C27; see the TOPIC-DECISION correction). The repo's `SOURCES.md`
credits Nik Bear Brown. The essay is first-person ("That's why I started Theorist.ai") and search
results name him as its founder, but the page byline is the publication.

| # | Essay, verbatim | Status |
|---|---|---|
| 0.4 | "Not obsolescence — its opposite." | ✅ verbatim |
| 0.5 | "Gardner's framework was built before machines became capable. It did not need to ask which intelligences were endangered by technology, because technology — in 1983 — was not yet a serious competitor to any of them." | ✅ verbatim, so 0.3's QUALIFY is against the essay's actual words |
| 0.6 | Forklift: "The intelligent response to a forklift is not to practice lifting heavier objects." / "…is to learn to operate it, to maintain it, to understand what it can and cannot lift." | ✅ verbatim. **The repo's beat-sheet line "The forklift does not make the human obsolete" is a converter paraphrase and must not be quoted** |
| 0.7 | "Howard Gardner gave us seven — later nine — multiple intelligences" | ⚠️ **conflicts with Gardner's own team**, who list eight (1.2). The ninth is presumably existential, which Gardner never formally added. The film uses Gardner's count and doesn't correct the essay on screen (it isn't the point) |
| 0.8 | Theorist.ai proposes its own seven-tier taxonomy, and argues education over-trains Tier 1 (pattern, retrieval, arithmetic) while Tiers 4, 5, 7 go "unscaffolded" | ✅ but **out of scope**: it's an education argument (the C27 boundary). The film builds on the essay's *Gardner* claim, not its curriculum claim |

**Attribution rule for the script:** "the Humanitarians AI essay introducing Theorist.ai". On screen:
*Introducing Theorist.ai, Humanitarians AI, March 2026*. Don't put a personal name on the byline.

**Consequence.** The base topic's central claim is half right. That makes a better film than a
fully right one: the question it says Gardner never asked, Gardner did go on to ask. And answering it
meant setting aside half of his own original test.

---

## Part 1 — The 1983 framework

| # | Claim | Level | Source | Status |
|---|---|---|---|---|
| 1.1 | Gardner proposed multiple intelligences in *Frames of Mind* (Basic Books, 1983) | primary read | Davis, Christodoulou, Seider & Gardner, "The Theory of Multiple Intelligences" (Harvard Project Zero, [pz.harvard.edu PDF](https://pz.harvard.edu/sites/default/files/Theory%20of%20MI.pdf)), Part 1 | ✅ |
| 1.2 | The 1983 list had **seven** intelligences: linguistic, logical-mathematical, spatial, musical, bodily-kinesthetic, interpersonal, intrapersonal. **Naturalistic** was added as an eighth in the **mid-1990s** | primary read | Davis et al.: "Gardner initially identified seven intelligences. However, in the mid-1990s, Gardner concluded that an eighth intelligence, naturalistic intelligence, met the criteria". Simply Psychology (2026) and Wikipedia both give 1995 | ✅ say "mid-1990s", not a specific year |
| 1.3 | The **eight criteria** for counting something as an intelligence, as listed by Gardner's own team: (1) seen in relative isolation in prodigies, savants, stroke victims or other exceptional populations; (2) distinct neural representation; (3) distinct developmental trajectory; (4) basis in evolutionary biology; (5) capture in symbol systems; (6) psychometric support; (7) distinguishable in experimental psychological tasks; (8) a core information-processing system | primary read | Davis et al., Table 1 (citing Gardner 1983; Kornhaber, Fierros & Veenema 2004) | ✅ |
| 1.4 | **Four of the eight criteria are written in terms of brains, childhoods, species history, or exceptional human populations** (criteria 1–4 above) | primary read (counted from 1.3) | as above | ✅ as a **count**. The inference "so they can't be run on a machine" is **ours**. Say "reads like" / "as I read it", not "Gardner says" |
| 1.5 | Gardner's team describes the theory as positing "several relatively independent **computational** capacities"; in 2026 Gardner calls the mind "a set of relatively independent computational devices" | primary read | Davis et al., Part 2; Gardner, ["The Fate of our Species in an AI-Infused Planet"](https://www.howardgardner.com/howards-blog/the-fate-of-our-species-in-an-ai-infused-planet) (Feb 6, 2026) | ✅ |
| 1.6 | Gardner's widely quoted definition: an intelligence is "a biopsychological potential to process information that can be activated in a cultural setting to solve problems or create products that are of value in a culture" | citing-source read | Simply Psychology cites it as **Gardner 2000 (*Intelligence Reframed*), p. 28**. Wikipedia attributes the same wording to 1983. The two sources conflict | ⚠️ **date conflict.** If used, cite it as *Intelligence Reframed* (1999/2000), never as the 1983 definition. The 1983-era phrasing ("the ability to solve problems, or to create products, that are valued within one or more cultural settings") is search-summary only. **Not scripted** |
| 1.7 | "Only two intelligences — linguistic and logical-mathematical — have been valued and tested for in modern secular schools" | primary read | Davis et al., Part 1 | ✅ but **out of scope**: schooling is the C27 boundary (`TOPIC-DECISION.md`). Not scripted |

---

## Part 2 — The psychometric critique (the caveat the film owes the viewer)

| # | Claim | Level | Source | Status |
|---|---|---|---|---|
| 2.1 | Visser, B. A., Ashton, M. C., & Vernon, P. A. (2006). "Beyond g: Putting multiple intelligences theory to the test." *Intelligence* 34(5), 487–502. doi:10.1016/j.intell.2006.02.004 | metadata | Crossref; OpenAlex | ✅ citation exists |
| 2.2 | Visser et al. gave 200 adults two tests per intelligence. Tests of the "purely cognitive" intelligences loaded substantially on a general factor *g*; bodily-kinesthetic and musical loaded lower | search-summary | search synthesis; abstract blocked at ScienceDirect/ResearchGate/academia.edu, and OpenAlex has no abstract | ⚠️ **not scripted at this level of detail.** Upgrade by reading the abstract, or don't use |
| 2.3 | Gardner replied: "On failing to grasp the core of MI theory: A response to Visser et al." *Intelligence* 34 (2006) 503–505. doi:10.1016/j.intell.2006.04.002. Visser et al. answered: "g and the measurement of Multiple Intelligences: A response to Gardner," doi:10.1016/j.intell.2006.04.006 | metadata | Crossref; OpenAlex | ✅ citations exist (the exchange happened), contents not read |
| 2.4 | Waterhouse, L. (2006) argued MI (with the Mozart effect and emotional intelligence) lacks adequate empirical support and shouldn't be applied in education. Her reply in the same issue: "Inadequate Evidence for Multiple Intelligences, Mozart Effect, and Emotional Intelligence Theories," *Educational Psychologist* 41(4), 247–255, doi:10.1207/s15326985ep4104_5 | citing-source read (OpenAlex abstract of the reply) | [OpenAlex](https://api.openalex.org/works/doi:10.1207/s15326985ep4104_5) | ✅ |
| 2.6 | "Spearman's theory of general intelligence (or g) remains the predominant conception of intelligence" within academic psychology, and it underlies more than 70 IQ tests in circulation | primary read | Davis et al., Part 1 (citing Brody 2004; Deary et al. 2007; Jensen 2008) | ✅ the film uses it for the one-line gloss on *g* |
| 2.5 | **Gardner's own team concedes the key point**: "the description of individuals in terms of several relatively independent computational capacities would seem to put MI theory at odds with g", and notes "the relative lack of empirical studies specifically designed to test the theory as a whole (Visser, Ashton, & Vernon, 2006)" | primary read | Davis et al., Part 2 | ✅ **this is the scripted caveat.** It comes from Gardner's side, so the film can't be accused of strawmanning |

**Consequence for the script.** The film uses MI as **Gardner's map**, not as settled psychology,
and says so once, early, sourced to Gardner's own co-authored concession (2.5). It does not litigate
*g* and does not recite loadings.

---

## Part 3 — Gardner did ask the question

| # | Claim | Level | Source | Status |
|---|---|---|---|---|
| 3.1 | 2019 interview: "For the first time in human history, we have developed machines and approaches (like deep learning and other forms of 'artificial intelligence') which equal or surpass human capacities" and "In some cases, we will not need to draw on certain human intelligences" | primary read | ["Interview: The Hidden Intelligences"](https://www.howardgardner.com/howards-blog/interview-the-hidden-intelligences), howardgardner.com, interview by Dario Ruggiero (Long Term Economy), published July 2019 | ✅ (he doesn't name which intelligences here) |
| 3.2 | Gardner, H., Furuzawa, S., & Stachura, A. "Who Owns Intelligence? Reflections After a Quarter Century," MI Oasis, **Oct 2024**. It revisits Gardner's 1999 *Atlantic* essay "Who Owns Intelligence?" | primary read | [multipleintelligencesoasis.org, 2024-10-22 URL](https://www.multipleintelligencesoasis.org/blog/2024/10/22/who-owns-intelligence) | ✅ say "October 2024" (the URL is dated the 22nd, one summary said the 23rd) |
| 3.3 | 2024 paper: LLMs "clearly exhibit the signs of high logical-mathematical and high linguistic intelligence"; "properly devised and trained," programs "can also demonstrate" **musical, spatial, bodily-kinesthetic, naturalist** intelligence. Then: "So far, computational systems emerge as multiply intelligent! But when it comes to the personal intelligences, one should be more cautious." | primary read | as 3.2, section on computational intelligence | ✅ **load-bearing: 6 of 8, in Gardner's own words** |
| 3.11 | Per-room evidence, verbatim from the 2024 paper's list after "Properly devised and trained, such programs can also demonstrate:". **Musical:** "Recognizing pieces of music, creating credible new ones in distinctive styles, performing standard compositions with appropriate nuances". **Spatial:** "Mastering games like chess or Go, robots remembering and navigating complex terrains" (so the paper files chess and Go under *spatial*, not logical-mathematical). **Bodily-kinesthetic:** "navigating complex terrains, playing instruments, picking up and adroitly manipulating objects of various shapes and sizes, competing successfully in athletic events". **Naturalist:** "Recognizing and grouping members of discrete categories of living entities (plants, animals) as well as human-created entities (commercial products, ranging from thimbles to airplanes…" | primary read (verbatim copy requested from the page) | as 3.2 | ✅ scripted in B08–B11 (draft 2). **Screenshot before audio**, because the text came through a fetch tool, not a raw copy |
| 3.4 | 2024 paper on history: 1956 Dartmouth programs "carried out mathematical and logical operations which, if carried out by human beings, might have been considered intelligent"; but "it was by no means clear" computers could pass the Turing Test or win strategy games; "in the last several years, the dam has decisively been broken" | primary read | as 3.2 | ✅ (the basis of the 0.3 QUALIFY) |
| 3.5 | Interpersonal: "evidence that programs can engage skillfully in exercises that involve diplomacy, salesmanship, gamesmanship, therapeutic interactions". Intrapersonal: invoking it for a program "can be seen as a 'category error'" | primary read | as 3.2 | ✅ **the falsifiability case, see Part 6** |
| 3.6 | For non-human candidates (animals, plants, computers) the 2024 paper proposes **six "symptoms" of intelligence**: solving a problem; creating a product; communicating information; performance improving through practice; training/teaching other members; exhibiting awareness or consciousness. A judge rates each as fulfilled "easily; possibly; fails the criteria; or it is not possible to determine" | primary read | as 3.2 | ✅ |
| 3.7 | The 2024 paper does **not** print a per-symptom verdict table for AI. Its summary: "certainly many computational systems merit the descriptor intelligent. They exhibit a reasonable sample of the aforementioned symptoms." On consciousness: systems "can be trained to testify to or feign consciousness" | primary read | as 3.2 | ✅ **do not invent a scored table and attribute it to Gardner.** A viewer-facing table must be labelled as ours |
| 3.8 | The 2024 paper describes the original criteria as "eight specified criteria ranging from a neurological basis to cross-cultural visibility" | primary read (via page-fetch summary quoting it) | as 3.2 | ✅ |
| 3.9 | The 2024 paper invokes Searle's Chinese Room on the personal intelligences | primary read | as 3.2 | ✅ but **not scripted**: the Chinese Room was this fellow's own Week 23 film. Reusing it would be self-duplication (see `TOPIC-DECISION.md`) |
| 3.10 | Viblio interview (Violena Paci): "I see no problem in AI systems mastering the major intelligences—linguistic, logical-mathematical, musical, bodily-kinaesthetic, spatial" | citing-source read | [viblio.com](https://www.viblio.com/en/interviews-en/howard-gardner-on-artificial-intelligence-and-multiple-intelligences/) | ⚠️ **undated**, so it can't be placed on a timeline. Superseded by 3.3. Not scripted |

---

## Part 4 — Where Gardner draws the line in 2026

| # | Claim | Level | Source | Status |
|---|---|---|---|---|
| 4.1 | Feb 6, 2026: "much of intellectual life and labor will be done better—perhaps immeasurably better—by various forms of artificial intelligence" | primary read (page-fetch summary quoting it) | ["The Fate of our Species in an AI-Infused Planet"](https://www.howardgardner.com/howards-blog/the-fate-of-our-species-in-an-ai-infused-planet) | ✅ |
| 4.2 | Same essay: "Our social, ethical, and moral lives cannot and should not be consigned to any artificial entity" (emphasis on *cannot* and *should not* is Gardner's) | primary read | as 4.1 | ✅ **load-bearing for the SHOULD column** |
| 4.3 | *Five Minds for the Future*, Harvard Business School Press, **2007**: disciplined, synthesizing, creating, respectful, ethical | citing-source read | HBR IdeaCast (Apr 2007); HBR store listing | ✅ say "2007". In 4.4 Gardner calls it "over two decades ago", which is ~19 years. **Don't repeat his phrase** |
| 4.4 | Aug 26, 2026, Education Next (interview by Frederick Hess): for the disciplined, synthesizing and creating minds, "I now believe AI will handle them so well that pursuing them will become optional for our species"; respectful and ethical minds "both need to stay distinctly human" | primary read | ["Keeping an Open—and Optional—Mind About AI"](https://www.educationnext.org/keeping-an-open-and-optional-mind-about-ai-howard-gardner/) | ✅ |
| 4.5 | Same interview: "I was simply trying to pluralize the traditional view of intelligence as a single IQ score" | primary read | as 4.4 | ✅ |
| 4.6 | Same interview's "around age 10… students should be free to pursue their own interests with the help of AI" | primary read | as 4.4 | ✅ but **out of scope** (schools, the C27 boundary). Not scripted |

---

## Part 5 — The base topic against the record

| Base topic says | Record says | Use |
|---|---|---|
| Gardner's framework never had to ask which intelligences technology endangers | He asked in 2019, answered in detail in 2024, and redrew the line in 2026 | The film's opening correction |
| Technology in 1983 wasn't a competitor to *any* intelligence | Gardner's own history puts logical/mathematical machine operation at 1956 | QUALIFY on screen, sourced to 3.4 |
| "Not obsolescence — its opposite" (forklift) | Gardner, 2026: those minds become **optional**, which is a third word, neither obsolete nor its opposite | The closing turn. Both are attributed. The film doesn't decide which is right |

---

## Part 6 — The reusable method (Phase 1 exit, PROOF)

**The claim the film teaches.** When anyone, Gardner included, says a machine *does* or *doesn't*
have an intelligence, the sentence is making one of three kinds of claim, and each needs different
evidence:

| Question | Kind of claim | What would count as evidence |
|---|---|---|
| **CAN IT?** | performance | a task, a result, a comparison to human performance |
| **IS IT?** | inside: understanding, awareness, self-knowledge | Gardner's own rating here is "not possible to determine" or "category error" (3.5, 3.6, 3.7). Performance evidence can't settle it |
| **SHOULD IT?** | values | an argument about what we want, not a measurement (4.2's "should not") |

**Worked example, applied to Gardner's own sentences:**
- "clearly exhibit the signs of high logical-mathematical and high linguistic intelligence" → CAN IT (3.3)
- "invocation of 'intrapersonal intelligence'… a 'category error'" → IS IT (3.5)
- "cannot and should not be consigned to any artificial entity" → one sentence, **two kinds of claim**: *cannot* is about machines (CAN IT or IS IT, and the sentence doesn't say which), *should not* is SHOULD IT (4.2). *Corrected 2026-09-26 during the read-through. Draft 1 filed "cannot" under IS IT alone, which settled an ambiguity the source leaves open.*

**Falsifiability case (the one that doesn't sort cleanly).** Interpersonal intelligence. The 2024
paper offers CAN IT evidence (diplomacy, salesmanship, therapeutic interactions, 3.5), and Gardner
still says "be more cautious". Either the caution is an IS IT claim (does the program *understand*
the other person?), or it's a CAN IT claim waiting on better tests. The paper doesn't say which. The
film leaves that open and hands it to the viewer as the task.

**Why this isn't reverse-engineered.** The three questions don't map one-per-example. 4.2 carries two
of them in one sentence, and interpersonal fits either of two. That's the test PROOF asks for.

---

## Rejected — do not script

| Claim | Why |
|---|---|
| "Gardner defined intelligence in 1983 as a biopsychological potential…" | date conflict, see 1.6 |
| Visser loadings (".50", "below .25", "35% of variance") | search-summary only, 2.2 |
| Any per-symptom AI scorecard attributed to Gardner | the paper has none, 3.7 |
| "Frames of Mind never mentions computers" | not verified either way. We don't have the 1983 text |
| "Gardner has written two decades ago…" re *Five Minds* | his own imprecision, 4.3 |
| Anything about school curricula or age 10 | C27 boundary |
| Chinese Room | Week 23 self-duplication |

## Open items before audio

- [x] ~~Upgrade 2.2~~ **Resolved by not using it.** The film uses 2.5 only (Visser loadings stay unscripted)
- [x] Screenshot the primary pages for on-screen sourcing. **Done 2026-09-26**, see `pantry/PROVENANCE.md`. B04, B05, B16 plates at 3840×2160
- [x] Confirm the Feb 2026 wording (4.2) from the page itself. **Done**, see verification log below

## Verification log — captures, 2026-09-26

Every quotation was checked against the page's raw text (`pantry/crops/*-page-text.txt`) or the
PDF text layer, not a fetch-tool summary. Upgrades and corrections:

| Row | Result |
|---|---|
| 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.11 | **all 25 quoted fragments used in the script match the MI Oasis page text verbatim.** One formatting difference: the page prints “category error” in double quotes; the narration nests it as 'category error' inside a double-quoted quote. Same words |
| 3.2 | the page itself dates the paper **"October 23, 2024"** (the URL path says 10/22). The script says "October 2024", so no change. Note: Gardner's Feb 2026 blog cites this paper as "(Gardner, Furuzawa, Stachura 2025)", presumably a later formal version. Not a conflict for the film |
| 3.1 | page states the interview "was made by Dario Ruggiero and published in July 2019 on www.lteconomy.org". Sentence verbatim: "…machines and approaches (like deep learning and other forms of 'artificial intelligence') which equal or surpass human capacities." ✅ primary |
| 4.2 | verbatim on the page. **The sentence continues** past where the script's quote ends: "…consigned to any artificial entity, no matter how social, how smart, perhaps even how *wise*—this entity appears to be, or claims to be." The continuation reinforces rather than qualifies the quoted part, so ending the quote at "entity" is fair. On the page, *cannot* and *should not* are italicised by Gardner. Year 2026 is established by the page text ("…in 2026"); the page shows only "Feb 6" ✅ primary |
| 0.4–0.6, 4.4 | essay and Education Next quotes checked against page text: all verbatim ("Not obsolescence — its opposite.", the 1983 sentence, both forklift sentences, "…will become optional for our species", "both need to stay distinctly human"). Education Next dated **August 26, 2026** on the page ✅ primary |
| 2.5 | PDF p. 12 prints **"would seem to put MI theory at odds with ‘g’"**, with *g* in quotation marks. Spoken narration unchanged; the on-screen plate shows the page itself. "Relative lack of empirical studies specifically designed to test the theory as a whole (Visser, Ashton, & Vernon, 2006)" is on **p. 9**. **Context:** the chapter raises this while *defending* MI ("In fact, MI theory is based entirely on empirical findings"). The narration's "admits" is fair, since it's stated as a concession ("Noted, too, is…"), but the chapter doesn't present it as a weakness it accepts ✅ primary |
