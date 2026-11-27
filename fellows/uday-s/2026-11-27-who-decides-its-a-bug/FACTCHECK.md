# FACTCHECK — Who Decides It's A Bug?

Commissioned topic: **"Implications/Advantages of using AI as a Beta Tester for
games and other kinds of software"**, retitled.

Three primary sources, read directly. See SOURCES.md for the verbatim quotes.

---

## Every on-screen figure

| Figure | Beat | Source | Status |
|---|---|---|---|
| 13,000 vulnerabilities (over) | B03 | OSS-Fuzz README | ✓ verbatim, shown with "as of May 2025" |
| 50,000 bugs | B03 | OSS-Fuzz README | ✓ verbatim, same qualifier |
| 1,000 projects | B03 | OSS-Fuzz README | ✓ verbatim; same on both official pages |
| "helped identify and fix" (wording) | B03 | OSS-Fuzz README | ✓ the project's own verb, not "found" |
| 30 new bugs/vulnerabilities reported | B04 | OSS-Fuzz-Gen README | ✓ verbatim; table has 30 rows |
| grading metrics: compilability / runtime crashes / coverage | B04 | OSS-Fuzz-Gen README | ✓ verbatim list |
| "generates fuzz targets … with various Large Language Models" | B04 | OSS-Fuzz-Gen README | ✓ verbatim |
| The oracle-problem sentence | B05 | TestGen-LLM §2 | ✓ quoted verbatim, attributed on screen |
| 75% built correctly | B06 | TestGen-LLM abstract | ✓ |
| 57% passed reliably | B06 | TestGen-LLM abstract | ✓ |
| 25% increased coverage | B06 | TestGen-LLM abstract | ✓ |
| 196 of 1,979 classes improved | B06 | TestGen-LLM §4 | ✓ verbatim counts |
| ~10% of classes improved | B06 | TestGen-LLM §4 + intro | ✓ — **not** the abstract's 11.5%; see below |
| 73% accepted | B06 | TestGen-LLM abstract, intro, §4 | ✓ all three agree |
| 10,000 / 36,000, as of August 2023 | B07 | OSS-Fuzz docs index | ✓ verbatim |

---

## The three source problems, all on screen in B07

### 1. The paper's abstract and its body disagree

- **Abstract:** "it improved 11.5% of all classes to which it was applied"
- **Introduction:** "able to improve 10% of all classes to which it was applied"
- **Section 4:** "196 test classes were successfully improved, while the
  TestGen-LLM tool was applied to a total of 1,979 test classes", and
  "approximately 10% of the test classes to which it was applied"

196 / 1,979 = **9.9%** (my arithmetic). The **11.5% figure appears only in the
abstract, with no count or denominator anywhere in the body**, and the paper
does not explain the difference. The abstract's figure is the one most secondary
coverage repeats.

**The reel uses 10% and shows the count.**

### 2. The denominator shifts between sections

For the same 75 / 57 / 25 results:

- **Abstract and introduction:** "75% of TestGen-LLM's test cases built
  correctly" — denominator is **test cases**.
- **Section 3.3** (the results section): "75% of test classes had at least one
  new test case that builds correctly" — denominator is **test classes**, and
  the criterion is **at least one**.
- Figure 2's caption says "as percentages of all test cases".

"75% of cases built" and "75% of classes had at least one case that built" are
different claims. B07 states this on screen. B06 narrates the figures without
asserting which denominator is correct, because the paper does not settle it.

### 3. Two official OSS-Fuzz pages carry different totals

| Page | Date qualifier | Vulnerabilities | Bugs | Projects |
|---|---|---|---|---|
| README | as of May 2025 | over 13,000 | 50,000 | 1,000 |
| Documentation index | as of August 2023 | over 10,000 | 36,000 | 1,000 |

Both are official. The reel uses the newer pair **with its date on screen**, and
B07 shows both.

---

## What the reel deliberately does NOT claim

- **That fuzzing is AI.** B03 says the opposite, in narration and in an on-screen
  chip: classical fuzzing is a loop with a free oracle. Attributing OSS-Fuzz's
  13,000/50,000 to "AI" would be the central error available in this topic, and
  the reel's structure exists to avoid it.
- **That the crash is the sole oracle in OSS-Fuzz-Gen.** The README never says
  how a bug is adjudicated; it has a "Target oracle" column whose values are
  undefined. B04 therefore claims only what is documented: the LLM writes the
  target, and targets are graded on compiling, crashing and coverage.
- **Anything from the November 2024 Google Security Blog.** Its body could not be
  retrieved — the fetch returned only page chrome — so its 26 vulnerabilities,
  its prior-fuzzing-hours claim, its 272 projects / 370,000 lines, and its
  OpenSSL CVE claim are all absent. SOURCES.md records this.
- **That AI replaces beta testers.** The TestGen-LLM paper states "TestGen-LLM is
  a support not a replacement for humans" and "it does not seek to replace
  them." B06 and B08 are consistent with that.
- **Any claim about a specific game, engine, studio or product.** None tested.

---

## The games-specific claim in B08, and its basis

B08 says that for games, much of beta testing has **no oracle at all** — is this
level fun, is this curve cruel, is this tutorial confusing.

This is an argument from the definition of an automatable oracle, not a cited
empirical finding, and it is framed on screen as the third regime in the reel's
own taxonomy rather than as a result from any source. The supporting citation is
the TestGen-LLM sentence in B05: where no automatable oracle exists, the tool
cannot classify a failure. No source is claimed for the game examples themselves.

---

## Scope decision, recorded before anything was built

The brief asked for implications and advantages. A list of advantages would have
been filler and would have aged badly. The reel instead gives the viewer the
distinction that determines every advantage — what decides a result is wrong —
and shows three regimes with real figures in each. That is the more useful answer
and the one the sources support.
