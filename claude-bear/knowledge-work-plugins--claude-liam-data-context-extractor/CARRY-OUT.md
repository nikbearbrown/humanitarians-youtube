# CARRY-OUT.md

**Carry-out line:** It doesn't make Claude already know your data — it
writes your data's context into a skill file, once, so every analysis
after that uses your definitions instead of a guess.

**Wrong guess it's built to defeat:** that a "data context extractor"
reads your company's data automatically, the way a live connector or
crawler would — pulling in context on its own, continuously. It doesn't.
It's a skill: a folder with a written instruction file, produced once (from
whatever you tell Claude about your data — your tables, your columns, what
"active customer" or "revenue" actually mean here), and read by Claude
before every future analysis.

**Secondhand test:** "It writes your data's meaning down once, it doesn't
already know it" survives being repeated by someone who wasn't fully
listening, and stays true. It compresses the distinction that matters
(a written, one-time spec vs. automatic built-in knowledge), not the topic
(data analysis in general).
