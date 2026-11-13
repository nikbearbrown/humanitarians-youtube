# Frictional Log — Graph Databases and Cypher

> Append dated entries as you go; never rewrite an earlier one.

## 2026-10-02 — Build a 60-second explainer on graph databases and Cypher, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I expected the contrast with SQL to be mostly about speed. I wanted the tables, queries and answers on screen to be real, so the same toy network was loaded into a graph engine and into SQLite and both were queried.

- **Where it resisted, and what I did next:**
  My first draft ran about 81 seconds, so I trimmed it. The fact-check pushed back on my simple speed claims, so I changed the line to "every hop adds a join". When I watched Beat 2, the voice and the screen seemed to contradict each other, so I had the line rewritten to name the misconception first.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes, ran both databases for the evidence, and fixed the layout issues found in frame checks. I accepted dropping the speed claim and adding the "tables still win for plain rows" limit to the verdict.

- **What I understand now, and what I still do not:**
  I understand that a graph database stores relationships so it can follow them, rather than rebuilding them with joins. I haven't measured performance on a real dataset.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
