# SOURCE-brief — "How Netflix Streams"

## What was asked for

One of two STEM videos for the week of 9–13 Nov, following the current Brutalist framework (see
[PROMPT.md](./PROMPT.md)), with its motion beats built in HyperFrames and three.js, like this week's other video,
on how spatial audio works.

## Who it is for

Lyrical Literacy fellows and the wider Humanitarians AI audience: people who watch Netflix and have seen the picture
go soft for a moment, or wondered why it rarely stops to load. Nothing technical assumed.

## What it must leave them with

Every show is stored many times at different qualities, and a score tells how good each one looks. Easy pictures
need fewer bits than hard ones, so each title gets its own ladder. The player picks the quality before every
chunk, and watching how much video it has saved up keeps it playing. Servers inside your internet provider make
each chunk's trip short. So: about 5 Mbit/s for Full HD, about 15 for 4K, and a steady connection.

## Evidence the reel stands on

`stream.py` and its outputs in `evidence/`; Netflix's TechBlog, Open Connect pages, Help Center and shareholder
letter for what Netflix does; the 2014 SIGCOMM study for the buffer-based idea. Details in
[SOURCES.md](./SOURCES.md).
