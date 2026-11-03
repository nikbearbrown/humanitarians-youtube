# QUESTION

**You keep editing a slide-writing agent's prompt and eyeballing the new deck
against the old one — how do you actually know a given change helped, and
how do you tell a prompt win from a model win?**

Redo source: `anthropics/cwc-workshops/youtube/eval-driven-six-agent-variants`
(Teardown register, workshop-teardown cut of the "Eval-Driven Agent
Development" Code with Claude 2026 workshop). Facts re-grounded directly
against the workshop's own repo at
`/Users/nik/Documents/Cowork/anthropics/cwc-workshops/eval-driven-agent-development`
(README.md, `src/graders/all.ts`, `solutions/01-polish.agent.yaml` through
`04-model-swap.agent.yaml`, `tasks.json`), not trusted from the source
narration.

**Correction made from source, and why:** the source's B06
(`CwcVariantImprovementWaterfall`) narrates a six-step cumulative waterfall
— "naive… ReAct reasoning loop… memory store… critic pass… tool
planning… output formatting constraints" climbing 42% to 81% — none of
which appears anywhere in the workshop repo. The repo is a slide-deck
(PowerPoint) generation agent graded by 7 deterministic code checks
(`src/graders/all.ts`: produced-result, slide-count, slides-with-image,
text-heavy-slides, cluttered-slides, small-font-slides, emoji-count) plus 5
LLM-judge checks (text, image, layout, color, title-body-coherence), run
against a fixed 5-task test set (`tasks.json`), across exactly four solution
rounds on top of a naive baseline — `01-polish` (typography + density +
anti-AI-tell rules), `02-diagram` (+ mandatory real diagram image per
slide), `03-qa-loop` (+ a mandatory rasterize-inspect-fix cycle), and
`04-model-swap` (reverts to the *plain naive prompt*, on a different model —
explicitly described in its own file as testing "the model lever vs the
prompt lever," not another stacked prompt tweak). No run scores exist in the
repo (no `runs/` directory), so the source's specific percentages are
invented, not measured. This redo drops the fabricated waterfall and the
"ReAct/memory/critic/tool-planning" labels entirely and rebuilds the
mechanism from what the repo's own files say. The given title ("Six Agent
Variants…") is kept as the episode's name per the rebuild contract, but no
beat in the body asserts a literal count — the body describes the two-layer
eval and the four real rounds without repeating the source's invented
number.

Name: General viewer (not attributed).
Channel: @HumanitariansAI — Claude Basics series.
