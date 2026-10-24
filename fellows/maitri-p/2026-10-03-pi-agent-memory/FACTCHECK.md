# FACTCHECK — pi-agent-memory

Project update. **No experimental results are claimed** — every forward-looking
statement is framed as planned work (FELLOWS-SUBMISSION: do not fabricate progress).

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | Project studies external memory for a frozen agent across sessions, no weight changes | Author's stated scope | Maitri's project brief |
| 2 | Pi is the agent harness/runtime connecting model, tools, context, sessions, observations | Author's description, not independently verified here | Maitri's project brief |
| 3 | Memory loop: capture → extract → store → retrieve | TRUE — standard framing of trajectory-based agent memory | general literature (see 5–7) |
| 4 | Episodic / semantic / procedural types, with examples | TRUE — standard taxonomy; examples are illustrative, not measured | cognitive-architecture usage in agent papers |
| 5 | Workflow memory reuses routines induced from past tasks | TRUE | Wang, Mao, Fried, Neubig — *Agent Workflow Memory* (2024) |
| 6 | Reflexion stores self-critique between attempts | TRUE | Shinn et al. — *Reflexion* (2023) |
| 7 | MemGPT pages context in and out of external storage | TRUE | Packer et al. — *MemGPT* (2023) |
| 8 | Δ_k = S_k^mem − S_k^base | DEFINITION of the planned metric — no value is shown or implied | this project's plan |

Dated material: paper years only; no model versions, no benchmark scores.
