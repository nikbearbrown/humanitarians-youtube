# PEDAGOGY GATE — claude-judged

> Fact-check every claim before ElevenLabs spend. No audio until VERDICT: PASS.

## Checklist

### Core thesis
- [x] "Maximally informed, minimally autonomous."
  **Correct and verifiable.** The pipeline produces QC data, schema validation,
  ffprobe output, and stills — the agent brings all of it. But the publish
  decision is a manual Studio flip. This is not a hypothetical design principle;
  it is the literal workflow described in CLAUDE.md ("Unlisted is unaudited;
  public is a manual Studio flip — the human decides"). The slogan accurately
  describes the system.

### Determinable vs judgeable distinction
- [x] "Determinable: schema valid, duration in bounds, mp4 at path. Agents answer."
  **Correct.** These are computable predicates with boolean answers. Any
  sufficiently specified agent can check them correctly and cheaply.

- [x] "Judgeable: interesting, worth watching, worth publishing. Humans decide."
  **Correct and important.** These require aesthetic judgment, audience
  knowledge, and context that is not formalizable as a schema check. No current
  agent (including Claude) can reliably substitute for this. This is not a claim
  about future capability — it is a claim about the current pipeline design.

### GATE P claim
- [x] "GATE P reads one line: VERDICT: PASS. It does not watch the video."
  **Verifiable in the codebase.** The actual check is:
  `re.search(r'^\s*VERDICT:\s*PASS\b', ped.read_text())`
  in `runtime/scripts/generate_audio.py`. This is precisely what the episode
  claims — cheap, deterministic, correct for its job.

- [x] "Gates are cheap taste-checks before expensive ones."
  **Correct framing.** GATE P costs a file read. The expensive taste-check
  (watching the rendered cut) costs minutes of human time. The gate catches
  obvious failures before incurring the expensive review. This is standard
  fail-fast architecture.

### Season recap accuracy
- [x] "On empty: routed models by tier." — TRUE (E1 established model routing)
- [x] "Unsupervised: scoped the risk before expanding the trust." — TRUE (E2)
- [x] "Taught: froze the judgment into a skill." — TRUE (E5)
- [x] "Scripted: pinned the exact into a script." — TRUE (E6)
- [x] "On average: named what Claude is — a distribution." — TRUE (E7)
- [x] "Steered: loaded the dice with conditioning." — TRUE (E8)
- [x] "Judged: who signs." — TRUE (this episode)

### Determinism boundary claim
- [x] "The determinism boundary IS the human-judgment boundary."
  **Correct and sharp.** The things agents verify are precisely the things that
  can be expressed as deterministic predicates. The things humans judge are
  precisely the things that resist formalization. The boundary is not arbitrary —
  it follows the structure of the problem.

### What we're NOT claiming
- No claim that agents can never judge quality (future capability question).
- No claim that human judgment is infallible.
- No claim about specific model capabilities or benchmarks.

VERDICT: PASS
