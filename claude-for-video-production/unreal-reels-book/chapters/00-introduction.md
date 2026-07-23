# Introduction — Books In, Video Out

*What this is, in two pages, before you make anything.*

---

You have a book, or a chapter, or a song, or a topic. You want video: a narrated lecture, a one-minute explainer, a mini-biography, a kids' language-learning music video. You have heard that you can now "just ask an AI" for such things, and you have seen what comes back — fluent, generic, and subtly wrong in ways that would embarrass you in front of a class. This book is about the other way.

**Unreal Reels is a pipeline, not a prompt.** It turns written material into finished short video through a fixed sequence of stages, and it obeys two laws that make the difference between a spine and slop. The first law: **audio is the master clock.** Narration or music is generated and *measured* first, and every downstream duration — how long a clip runs, how long a slide holds, when each caption word lights up — is derived from that real audio, never guessed from a word count. The second law: **the human signs every gate.** The machine does the work; you decide what the thing is, make it yours, and put your name on it at each checkpoint. Neither law is decoration. Together they are why the output is watchable and accurate instead of plausible and hollow.

The through-line you will see in every chapter is a single file, `beat_sheet.json`, where **one beat = one narrated unit = one visual.** Every tool in the system writes to it, reads from it, or hands it forward. That one shared spine is why a text-to-speech script written for sketch videos also narrates a lecture, and why lyric-timing code written for music videos also aligns lecture captions. Learn the beat sheet (Chapter 2) and you have learned the grammar of the whole system.

## The one thing that makes this different

Single-prompt video tools invent content from a model's priors. Nothing anchors them, so they drift into confident error. Unreal Reels is different in one decisive way: **it works downstream of a real book.** When you make a lecture from a chapter, the narration expands *that chapter's own prose*; the figures are *that chapter's own figures*; and if the book came through the AI+1 system, its claims were already fact-checked before a single frame existed. The video's job is not to be right about the world from scratch — it is to stay *faithful* to a source that is already right. That is a smaller, checkable task, and Chapter 9 shows how the pipeline checks it.

This is what lets a book become a *spine*: a high-quality, accurate starting point that an expert opens and — conversationally, in an afternoon — makes their own. Two teachers handed the same lecture spine for the same chapter will quickly diverge into two different courses, each unmistakably theirs. The spine is the eighty percent that is identical for everyone, done well, so all your energy goes to the twenty percent that is yours alone.

## Three ways in

1. **Make one video.** Pick an aspect — Songbird (music), Bios (mini-biography), or Explainer — and follow its walkthrough. You will have a finished clip by the end of the chapter.
2. **Turn a chapter into a lecture.** Run the three-stage lecture pipeline (Chapter 7) on a chapter you already have. This is the highest-value path if you teach.
3. **Do a whole book.** Run silent mode (Chapter 8) over every chapter to get watchable rough drafts, then refine the ones that matter. This is how one person, or a hundred volunteers, turns a library into a course catalog.

## How to read this book

Every chapter opens with a short overview of *why* the pipeline works the way it does, then gives you exercises that each end in an artifact — a beat sheet, a still set, a rendered clip, a fidelity report. Do them in order for the first three chapters; the foundations (the two laws, the beat sheet, the storyboard engine) are assumed everywhere after. You will drive everything either by talking to an agent (Cowork, Claude Code, or Cursor) that reads the pipeline's contract and stops at each gate for you, or by running the engine scripts yourself. Both paths are shown. A ✅ marks anything you can do with only free and open-source tools — and there is more of that than you might expect.

Let's make something.
