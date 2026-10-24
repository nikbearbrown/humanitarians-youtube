# Keep Failures Red — script (final, as shot)

Channel claude-hai · Persona Rishabh · Register Plain · Voice Kokoro `af_sarah`
16:9 long cut: 4:51 (290.9s) · 9:16 Short: 1:10 (69.5s)

Timestamps are measured from the locked audio. This is exactly what is spoken in the final render; on-screen props live in `beat_sheet.json`.

## 16:9 — long cut

### B00 · OPEN (0:00–0:14)
> Bonjour — this is Rishabh for Humanitarians AI. Part six, the last of stage two. The pipeline worked whenever I triggered it. This week it runs itself, every day, and tells the truth about how it went.

### B01 · OPEN (0:14–0:26)
> Here's the whole video. A green run doesn't mean everything worked. It means the last task finished. So my last task checks every other one, and if anything failed, it fails too. Failures stay red.

### B02 · I — The Daily Run (0:26–0:40)
> Here's the finished pipeline. Every day at six UTC: fetch the last five days of metadata, parse a batch of PDFs, prune the cache, and report. The report is the part that keeps the whole run honest.

### B03 · II — Time (0:40–1:00)
> Two facts about time came first. In my Airflow version, a scheduled run's data interval has zero length, so fetching the interval would fetch nothing. And arXiv only shows a paper once it's announced. A paper submitted on Friday afternoon is announced on Monday evening. A run that fetches yesterday misses it, forever.

### B04 · II — Time (1:00–1:19)
> So every run fetches the last five days. The worst normal case is that Friday paper, and a Tuesday run reaches back to Friday. The fifth day is margin for holidays. The overlap costs about forty-five seconds, and it's free in every other way, because the save is already idempotent.

### B05 · III — Limits (1:19–1:38)
> Then the schedule itself. Daily, weekends included, at six UTC, after arXiv announces. One run at a time, so the rate limit stays inside one process. Two retries, half an hour apart. And timeouts, because with one run at a time, a stuck parse would block every run after it.

### B06 · III — Limits (1:38–1:59)
> The first scheduled run exposed a hidden bug. The batch size came from a setting that didn't exist yet. Once the run parameter was empty, every scheduled run would have crashed. No check could see it: mypy only looked at the source folder, and the line sits inside a task. Now mypy checks the DAG code too, and I proved it with a typo.

### B07 · IV — Honesty (1:59–2:14)
> Cached PDFs older than fourteen days are deleted. And the cleanup has to run even when parsing failed. The default rule only runs a task after everything before it succeeded, which would skip the cleanup on exactly the bad days.

### B08 · IV — Honesty (2:14–2:35)
> But that creates a trap. Airflow marks a run green if its last tasks succeeded. A report that always runs, and always succeeds, would turn a failed run green. So the report reads every task's result. A task only returns a value if it succeeded. If any value is missing, the report logs everything, then raises.

### B09 · IV — Honesty (2:35–2:48)
> Here's that logic. Pull each task's result. Any that are missing are the failed tasks. Raise, and the run stays red. Retries are off for the report, because retrying it can't fix a failure upstream.

### B10 · IV — Honesty (2:48–3:02)
> A normal run's report reads like this. The window, the papers saved, what the PDFs did, the cache, and what's left in the queue. Retries exhausted is the number to watch. Those papers will never be retried on their own.

### B11 · V — Proof (3:02–3:21)
> Then the failure run. I broke one paper's PDF link, and chose a paper outside the window. Inside it, the metadata fetch would have repaired the link, and the test would have passed for the wrong reason. Parsing failed. The cleanup ran anyway. The report logged failed, then raised. And the run stayed red.

### B12 · VI — The API (3:21–3:43)
> Last, the API shows the pipeline, and it starts with a route-order trap. The stats route sits above the ID route, or stats would be read as a paper ID. The paper list gains each paper's status, and stays a list, so no client breaks. Sections only come with a single paper, loaded on purpose. And stats reuse the report's queries, so the two can't disagree.

### B13 · VI — The API (3:43–4:00)
> One bug none of my checks could see. The detail route returned sections, but still declared the list response model. FastAPI filters the return value through that model, so the sections vanished, with no error anywhere. Only checking the live response caught it.

### B14 · VII — When Not To (4:00–4:10)
> When is this too much? For a script you run by hand and watch, skip the schedule, the window and the report. They earn their keep when nobody is watching the run.

### B15 · VIII — Verdict (4:10–4:22)
> So that's stage two. Real papers arrive every day on their own, their PDFs become sections, and a failed run stays red. Next, stage three: making all of it searchable.

### B16 · VIII — Verdict (4:22–4:45)
> Your turn. Before you schedule anything, paste this into Claude, with the job underneath. Here is a job I'm about to schedule, below. Don't change it. Tell me which inputs depend on when it runs, what data could arrive late, and whether a failed step could still leave the run green. Then ask me what I'd check first if it silently stopped. Notice what it's not asking for: a fix. You're asking how it can fail quietly.

### B17 · OUTRO (4:45–4:51)
> Green is a claim. Make it earn it. Rishabh, for Humanitarians AI.

## 9:16 — Short

### S00 (0:00–0:10)
> Bonjour — this is Rishabh for Humanitarians AI. My pipeline now runs itself every day. Here's what it took to make it honest about failure.

### S01 (0:10–0:15)
> Every day at six UTC: fetch, parse, prune the cache, and report.

### S02 (0:15–0:23)
> arXiv announces a Friday afternoon paper on Monday evening. A run that fetches yesterday misses it forever.

### S03 (0:23–0:30)
> So every run re-fetches the last five days. The overlap is free, because the save is idempotent.

### S04 (0:30–0:36)
> One run at a time, two retries, and a timeout on every step that can hang.

### S05 (0:36–0:44)
> Here's the trap. Airflow marks a run green if its last task succeeded. A report that always succeeds hides every failure.

### S06 (0:44–0:53)
> So my report checks every task's result. If one is missing, it logs everything, then raises, and the run stays red.

### S07 (0:53–1:00)
> And one bug no check could see: the API quietly dropped sections. Only a live request caught it.

### S08 (1:00–1:09)
> The full version has the schedule, the real report, and a prompt for your next scheduled job. Watch it next. Rishabh, for Humanitarians AI.
