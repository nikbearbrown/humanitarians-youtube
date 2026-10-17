# Frictional log — AI Research Assistant, Stage 2B

## 2026-10-16 — PDFs downloaded, parsed with Docling and saved

- **Drive:** https://drive.google.com/drive/folders/1rca04Q1xJCdidYSC3QelYdoodXrX9G1H
- **Evidence of commit:** [`10d074b`](https://github.com/RishabhHM/AI-Research-Assistant/commit/10d074b4324e2b00eb8546eefcb25f3d12509873)

**What I was working on.** Taking `pending` papers, downloading their PDFs through the shared rate limiter into a cache, parsing them with Docling inside Airflow, and saving the sections, with every failure recorded on its paper.

**What I tried, and what I expected.**
- I expected PDF downloads to reuse the arXiv client's rate limiter and retries.
- I expected a new named volume to just work as the PDF cache in Airflow.
- I planned to benchmark pypdf against Docling on 3–4 real papers before choosing.
- I expected Docling to pick up the models baked into the Airflow image without extra setup.

**Where it resisted, and what I did next.**
- **`Permission denied` on the new volume.** `/opt/airflow/data` didn't exist in the image, so Docker created the mount point as `root`. I created the folder in `airflow/Dockerfile`.
- **"Writable" didn't prove it was a volume.** The Step 5 commit never added the mount line. A typo (`- pdf_cache: /opt/…`) gave `missing a mount target` and exposed the gap. I fixed it and now check with `mount | grep` (`9e1ba6d`).
- **`LocalEntryNotFoundError` with `HF_HUB_OFFLINE=1`.** Docling's models live in its own folder, not the HF cache, so I pass `artifacts_path` (`e3b7bcc`).
- **`Can't locate revision identified by '657e3da8defb'`.** The `migrate` image copies `migrations/` at build time. After adding a migration, I now run `make build` first.
- **Autogenerate missed the CHECK constraint** on `pdf_status`. I added it by hand in the migration (`aaf7f21`).
- **527 papers still `pending` after a run.** The only run was the old DAG version, from before `process_pdfs` existed. Triggering the new version fixed it.

**What Claude contributed, and what I did with it.**
- **Roadmap:** I used Claude to break the week's goal into tasks across the week.
- **Design and refactoring:** Claude helped with the production-grade design: one short transaction per paper, status in the database instead of XCom, and per-paper failure isolation with an attempt count.
- **Reviews:** before each commit, Claude caught a missing import, the missing `PdfStatus` class, a mypy annotation, and `0600` permissions on cached PDFs.
- **Code:** at my request, Claude gave me the full version-aware `upsert_many`. It also wrote `personal/eval/compare_parsers.py`.
- Accepted:
  - **`VARCHAR` + `CHECK` instead of a Postgres `ENUM`.** It's easier to migrate and roll back.
  - **`page_range` to truncate long PDFs instead of rejecting them**, so a 75-page paper keeps its main text.
  - **`HF_HUB_OFFLINE=1`.** It turns a silent 1.4 GB download into a loud failure.
- Rejected:
  - **Running the parser benchmark now.** I chose Docling on the course's evaluation. The script is ready but hasn't been run, so no results are claimed.
  - **Tests for the cache, parser and processing service now.** I verified them live instead.

**What I understand now, and what I still do not.**
- Understood:
  - Copied code needs a rebuild; mounted code doesn't (`migrations/` vs `src/`).
  - **Reversed:** a passing check isn't proof. A write succeeded without any volume, and only `mount | grep` showed the truth.
  - A test that must fail should be run. A fake 404 proved the failure isolation and the "all failed" guard.
  - Docling isn't free. The Airflow image grew from 3.22 GB to 7.54 GB, and at ~30 s per paper one day of cs.AI is ~2–3 hours of CPU.
- Not understood / not verified:
  - No local benchmark of Docling against pypdf.
  - The cache, parser and processing service have no automated tests.
  - CLI-triggered runs have `logical_date = None`. The fetch window in 2C needs a fallback.
