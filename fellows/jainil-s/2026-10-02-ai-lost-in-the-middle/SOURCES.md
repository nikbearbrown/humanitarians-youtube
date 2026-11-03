# SOURCES — ai-lost-in-the-middle

The central finding is published, peer-reviewed and quoted verbatim. No figure
is invented and no magnitude is claimed beyond what the paper states.

| # | Source | Verbatim wording relied on | Supports |
|---|---|---|---|
| S1 | Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). "Lost in the Middle: How Language Models Use Long Contexts." *Transactions of the Association for Computational Linguistics*. [ACL Anthology](https://aclanthology.org/2024.tacl-1.9/) · [arXiv:2307.03172](https://arxiv.org/pdf/2307.03172) | "performance is often highest when relevant information occurs at the **beginning or end** of the input context, and **significantly degrades** when models must access relevant information in the **middle** of long contexts, **even for explicitly long-context models**." | The entire thesis: position inside the context changes whether information is used |
| S2 | Same paper | The effect is characterised as a **U-shaped** performance curve over the position of the relevant document | The shape drawn on screen in B03 |
| S3 | Same paper | Evaluated on **multi-document question answering** and **key-value retrieval** | What the finding was measured on — named on screen so the scope is honest |

## Scope stated on screen

The reel says the finding is about **where** relevant information sits in a long
input, measured on retrieval-style tasks. It does not claim:

- a specific percentage drop for any model
- that every model or every task shows the same curve
- that the effect is unfixable, or that any named current model still exhibits
  it to the degree the paper measured

The paper's own qualifier — "even for explicitly long-context models" — is
spoken, because it is the part that makes the finding surprising.

## Deliberately NOT used

- Any per-model accuracy figure from the paper. They are specific to the models
  and context lengths tested in 2023–24, and quoting them as current would
  misrepresent them.
- The widely circulated claim that models "ignore" the middle entirely. The
  paper says performance *degrades*, not that retrieval fails.
- Vendor blog posts about context-window improvements. Not peer-reviewed and
  not needed for the argument.

## Derived, not cited

The worked illustration — the same answer placed at the start, middle and end
of one long document — is a restatement of S1's experimental design, presented
as an illustration and labelled as such.
