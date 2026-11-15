# FACTCHECK — weekly-recap-real-art

This is a first-person weekly progress update. Every item below is the user's own
self-reported account of the week, taken from the build request; none of it can be
independently verified by this toolkit, and none of it is stated as anything more.
No outside statistics. No real platform logos: the article is a mock header, GitHub is
a generic code-folder icon with a plain-text label. No photos of real animals, shelters
or people: the cat and dog are generic illustrations and the map is a generic panel.

1. **Writing** (B04) — the user published a new Substack article, "Real Art, New
   Light", about how AI can be used to promote real artwork while keeping the original
   at the center. The header on screen is a mock (labeled "mock article header"); its
   two summary lines paraphrase the user's one-sentence description and add nothing.

2. **Video production** (B05) — the user produced four video files with Brutalist, the
   team's video-creation tool, covering two videos (an AI topic video based on the
   article, and this weekly recap), each exported in 16:9 and 9:16. The video says "two
   videos ... four video files" and never "four videos".

3. **Organization** (B06) — the user pushed their files to GitHub so the work is saved
   and easy to share. **This is the user's statement.** When this video was built, this
   week's files (the "Real Art, New Light" video folder and this recap's own folder)
   had not yet been pushed from this toolkit session; the claim becomes true for those
   once they are pushed (see the final note).

4. **A new project** (B07, B08) — the user went through the CatBot and DogBot proposal
   at Humanitarians AI. **It is an early-stage plan**, labeled "Early-stage plan" on
   screen in both beats, and nothing in the video says it is built or agreed:
   - the idea: revive CatBot and add a sibling, DogBot, to help cat and dog shelters
     turn each animal's listing into marketing that helps them get adopted;
   - the first step: a small proof of concept, a tool that drafts a warm bio and
     platform-ready posts from a staffer's quick notes, with a person approving
     everything, plus volunteer photo days for better pictures;
   - what comes next, all stated as plans: the team plans to build the demo, then reach
     out to shelters in Minnesota and the Boston area, aiming for one pilot shelter in
     each region to help shape the next version.
   **The video does not say the demo is built and does not say any shelter has agreed to
   take part.** The "planned" tags on the three steps are on screen. The map is a generic
   panel ("generic map -- not to scale"): two region shapes and one pin each.
   Part four runs about 44 s (the request asked for about 40 s).

## The scripts

`weekly_recap_v1.py` and `weekly_recap_v2.py` are real, runnable Python scripts, both
actually run before the CODE and OUTPUT beats were written; the on-screen output is what
they printed. v2 adds a status to each part (published, produced, saved, planning) and
prints "3 parts done, 1 in planning".
