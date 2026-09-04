# PROMPTS — The Brand That Didn't Exist

## Open slots: none

Every beat renders from sources inside this folder.

## The ask that mattered most on this one

Not "summarise the project" — that would have reproduced the abstract. The
useful ask was verification:

```
claude "recompute every headline number in this paper's abstract from the
files in results/. Report each one as matches / does not match, with the file
and the derivation."
```

That single pass found seven abstract figures that the shipped data does not
support, and turned the video from a summary into something defensible. The
generalisable rule: **when a project ships both claims and data, check the
claims against the data before narrating either.**

## Reusable spine for an evidence-based topic explainer

```
claude "author an ai-explainer beat sheet: BLUF, then a FRAMEWORK of 2-4 axes
shown as a structure BEFORE any result, then one beat per axis measured on the
same subjects, then a falsifiability beat the framework PREDICTS, verdict,
scaffolded task. Every number must carry its source file on screen."
```
