# ReAct research and claim ledger

Updated November 15, 2026 for the shorter cut.

The household and shopping values are success rates from separate benchmarks. The question-answering statement refers to HotpotQA exact match. The room example is fictional.

## Claim ledger

| ID | Claim and where it appears | Source and exact location |
| --- | --- | --- |
| R0 | B00, B06 and credit. Intro, AI-narration disclosure, spoken sign-off and channel credit follow the supplied script. | Presenter brief and Nov 7 topic episode for the exact intro format, AI-narration disclosure, closing wording and channel credit. |
| R1 | B00 and B02. ReAct combines a stated thought, an action and an observation returned by the environment. The model receives the observation before choosing its next step. | [Paper, §2 and Figure 1](https://arxiv.org/html/2210.03629v3#S2), especially the setup and definition of the augmented action space. [Google Research, Model Overview and ReAct Prompting](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/) |
| R2 | B01. The reasoning-only baseline omits tool actions and observations. Errors in its assumptions can propagate through later reasoning. “Never checks” refers to external evidence in this comparison. | [Paper, §3.2, Baselines, and §3.3, ReAct vs. CoT](https://arxiv.org/html/2210.03629v3#S3). Figure 1(1b) shows the reasoning-only format. |
| R3 | B01. The acting-only baseline omits written thoughts and can lose track of subgoals. ReAct adds the written thought step and keeps actions and observations. | [Paper, §3.2, Baselines](https://arxiv.org/html/2210.03629v3#S3) and [§4, Results and Appendix D.2](https://arxiv.org/html/2210.03629v3#S4). |
| R4 | B03. The schedule is fictional. Room A is booked, so the agent checks Room B and recommends it after the tool reports availability. | Fictional worked example supplied for this cut. It illustrates the tool-and-observation mechanism in [paper §2 and Figure 1](https://arxiv.org/html/2210.03629v3#S2). |
| R6 | B04. ALFWorld household task success was 71% for ReAct and 45% for Act. Each value is the best prompt result out of six for that method. | [Paper §4, ALFWorld and Table 3](https://arxiv.org/html/2210.03629v3#S4.T3), All column, the best-of-six rows for ReAct and Act. |
| R7 | B04. WebShop success was 40.0% for ReAct and 30.1% for Act. | [Paper §4, WebShop and Table 4](https://arxiv.org/html/2210.03629v3#S4.T4), success-rate column, rows for ReAct and Act. |
| R8 | B03. The written trace lets a reader identify the observation that changed the agent’s recommendation. | [Paper, §1, Figure 1, and §3.3 results analysis](https://arxiv.org/html/2210.03629v3#S1). |
| R9 | B05. The ReAct paper observed cases that repeated thoughts and actions. | [Paper, §3.3, ReAct vs. CoT, and Appendix E.1](https://arxiv.org/html/2210.03629v3#S3). The conclusion, §6, also flags context limits when prompts need more demonstrations. |
| R10 | B04. On HotpotQA, chain-of-thought alone scored 29.4 exact match and plain ReAct 27.4. | [Paper §3.3, Table 1](https://arxiv.org/html/2210.03629v3#S3.T1), HotpotQA exact match for chain-of-thought and ReAct. |
| R11 | B00 and B02. The SDK implements a model/tool/result loop. The analogy is about that feedback pattern. | [OpenAI Agents SDK, The agent loop, steps 1–3](https://openai.github.io/openai-agents-python/running_agents/#the-agent-loop). |
| R12 | B05. Repeated turns can add to the history available to the model. | [Anthropic, Effective context engineering for AI agents, §01](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents#context-engineering-vs-prompt-engineering), paragraphs on multi-turn inference and a limited context window. |
| R13 | B05. In controlled multi-turn tasks, errors left in the history made subsequent errors more likely. | [Sinha et al., The Illusion of Diminishing Returns, §3.2 Result 3 and Figure 5](https://arxiv.org/html/2509.09677#S3.SS2). The experiment supplied the plan and varied errors in the context. |
| R14 | B06. The presenter describes an agent repeatedly responding to a changing world in an RL environment. | Presenter-supplied public wording in the episode brief. |
| R15 | B06 takeaway. Find the observation that justified the next step. | Editorial takeaway drawn from the sequence in [Paper §2, Figure 1](https://arxiv.org/html/2210.03629v3#S2) and the interpretability discussion in [§1](https://arxiv.org/html/2210.03629v3#S1). |
| R16 | B01. Princeton and Google researchers first released the ReAct paper as a preprint in 2022. | [Paper front matter](https://arxiv.org/pdf/2210.03629) and [arXiv version history](https://arxiv.org/abs/2210.03629). V1 was submitted October 6, 2022. [Authors’ project page](https://react-lm.github.io/) gives the ICLR 2023 venue. |
