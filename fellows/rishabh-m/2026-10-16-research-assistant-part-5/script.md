# The Queue Is A Query — script (final, as shot)

Channel claude-hai · Persona Rishabh · Register Plain · Voice Kokoro `af_sarah`
16:9 long cut: 4:51 (290.9s) · 9:16 Short: 1:20 (80.4s)

Timestamps are measured from the locked audio. This is exactly what is spoken in the final render; on-screen props live in `beat_sheet.json`.

## 16:9 — long cut

### B00 · OPEN (0:00–0:15)
> Hola — this is Rishabh for Humanitarians AI. Part five of building a research assistant. Last time, real paper metadata went in. This week, the PDFs: downloaded, parsed, and saved, one paper at a time.

### B01 · OPEN (0:15–0:29)
> Here's the idea. One bad PDF should fail one paper, not the whole day. So every paper keeps its own status in the database. The work queue becomes a simple query, and retrying a failure is automatic.

### B02 · I — The Goal (0:29–0:41)
> The goal for this part: every pending paper gets its PDF downloaded, parsed by Docling, and saved as sections. And every failure is recorded on the paper it belongs to.

### B03 · II — Download (0:41–0:59)
> Downloads go through the same rate limiter as everything else. Then two checks. The size, against a cap. And the first bytes. arXiv can answer with status two hundred and send an HTML page instead of a PDF. So unless the file starts with percent PDF, it is not cached.

### B04 · II — Download (0:59–1:20)
> The cache is one file per paper version, so a revised paper gets a fresh download. Every write goes to a temp file in the same folder, then one rename. A crash never leaves half a PDF under the real name. And reading real output found a surprise: the temp files were owner-only, so the mode is set explicitly.

### B05 · III — Parse (1:20–1:40)
> Docling only goes where it runs. No endpoint parses PDFs, so the API image stays at four hundred twenty-one megabytes. The Airflow image carries Docling and its models, baked in at build time. And an offline flag means a missing model fails loudly. It did: Docling was looking in the wrong folder.

### B06 · III — Parse (1:40–1:59)
> The parser walks the document in reading order, and tables come along as Markdown. On BERT: sixteen pages, thirty-one sections, six with tables, in about twenty-eight seconds. I chose Docling because it's built for structured documents. I haven't benchmarked it locally yet, but the comparison script is ready.

### B07 · IV — Status (1:59–2:22)
> The status lives in the database, not in one run's memory. Every paper is pending, parsed, failed, or skipped. A failure is retried up to three times. Too large is skipped, because it will never succeed. So the work queue is just a query: pending, or failed with attempts left. And the migration's default queued all five hundred twenty-seven papers at once.

### B08 · IV — Status (2:22–2:39)
> The migration taught me two things. Autogenerate doesn't detect check constraints, so I added that one by hand. And the migrate container had copied the old migrations at build time, so it couldn't find the new revision, and nothing started. The rule: copied code needs a rebuild.

### B09 · V — One Paper At A Time (2:39–3:02)
> Then the loop. Each paper gets its own try, and no database session stays open while a PDF parses. Too large means skipped. Anything else is recorded as failed, with its error, and the loop moves on. A broad except is right here, and only here: it's the line between items. But if every paper in a run fails, the task raises. That's a system problem, not bad PDFs.

### B10 · V — One Paper At A Time (3:02–3:20)
> One more case. arXiv publishes a new version of a paper. The upsert compares the stored PDF link with the incoming one. If it changed, the paper goes back to pending, with its attempts reset. Otherwise a revised paper would keep the old version's sections.

### B11 · VI — Proof (3:20–3:39)
> Then I ran it both ways. With a limit of three, the run parsed the three newest papers, in about a minute and a half. Then I pointed one paper at a PDF that doesn't exist. The run failed, as it should. The row says failed, one attempt, HTTP four oh four. A test that must fail should be run.

### B12 · VI — Proof (3:39–3:54)
> The real cost: thirty to forty-five seconds per paper. A day of AI papers is about two hundred fifty, so two to three hours of CPU. That's why the batch size is a parameter for now. The daily schedule decides it next.

### B13 · VII — When Not To (3:54–4:07)
> When is this too much? If you only need abstracts, skip the PDFs entirely. The metadata already has them. Per-paper status earns its keep when items fail on their own, and the batch runs again tomorrow.

### B14 · VIII — Verdict (4:07–4:20)
> So, stage two, part two. Every pending paper can now be downloaded, parsed and saved, and every failure says why. Next: the daily schedule, and showing the data through the API.

### B15 · VIII — Verdict (4:20–4:44)
> Your turn. Before you write your next batch job, paste this into Claude, with the code underneath. Here is a batch job I'm writing, below. Don't fix the code. For each step, tell me what happens to the other items when one fails, where its progress is recorded, and how a rerun knows what's left. Then ask me which failures should never be retried. Notice what it's not asking for: a fix. You're asking where failure goes, before it happens.

### B16 · OUTRO (4:44–4:50)
> If the queue is a query, a retry is just the next run. Rishabh, for Humanitarians AI.

## 9:16 — Short

### S00 (0:00–0:12)
> Hola — this is Rishabh for Humanitarians AI. Five hundred twenty-seven papers needed their PDFs parsed. Here's how one bad PDF stays one bad PDF.

### S01 (0:12–0:17)
> Every pending paper: download it, parse it with Docling, and save it as sections.

### S02 (0:17–0:27)
> arXiv can answer with status two hundred and send an HTML page. So nothing is cached unless it starts with percent PDF.

### S03 (0:27–0:34)
> Every write goes to a temp file in the same folder, then one rename. A crash never leaves half a PDF.

### S04 (0:34–0:44)
> Docling and its models live only in the Airflow image. An offline flag makes a missing model fail loudly, and it caught Docling looking in the wrong folder.

### S05 (0:44–0:53)
> Each paper keeps its own status in the database. So the queue is just a query: pending, or failed with attempts left.

### S06 (0:53–1:02)
> One paper failing is recorded, and the loop moves on. Every paper failing raises, because that's a system problem, not bad PDFs.

### S07 (1:02–1:10)
> Then I pointed one paper at a PDF that doesn't exist. The run failed, as it should. A test that must fail should be run.

### S08 (1:10–1:20)
> The full version has the real code, the migration gotchas, and a prompt for your next batch job. Watch it next. Rishabh, for Humanitarians AI.
