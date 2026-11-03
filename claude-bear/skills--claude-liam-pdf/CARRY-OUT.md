# CARRY-OUT.md (GATE C)

**Carry-out sentence (BCRY):**
> There's no do-everything PDF library. The skill's job is routing each task —
> move, read, or build — to the tool built for it.

**Wrong guess it defeats:** a newcomer assumes one PDF library should handle any PDF
task — merge, extract, create, all with the same tool. It doesn't work that way.
`pypdf` moves pages around (merge, split, rotate, encrypt), `pdfplumber` reads what's
already on the page (text, tables), and `reportlab` builds new pages from scratch.
The skill's whole architecture is picking the right one for the job in front of it,
never reaching for a single default.

**Test:** "there's no do-everything PDF library — the job is routing each task to
the tool built for it" survives being repeated by someone who wasn't paying full
attention, and stays true — it compresses the actual distinction (task-based
routing across three separate library domains), not the topic ("this video is
about a PDF skill").
