# Frictional log — AI Research Assistant, Stage 2A

## 2026-10-09 — real arXiv metadata into Postgres

- **Drive:** https://drive.google.com/drive/folders/1TcLfQncfg-LSAnTao7RW7xvedUpr2oOB
- **Evidence of commit:** [`22f9c6b`](https://github.com/RishabhHM/AI-Research-Assistant/commit/22f9c6b39ff163efd52be7e7d4a6892f5bb2aefc)

**What I was working on.** Getting real cs.AI paper metadata from the arXiv API into Postgres, through a script and a manually triggered Airflow DAG, with Alembic managing the schema.

**What I tried, and what I expected.**
- I expected a quick Postgres volume reset to apply the Stage 1 model changes.
- I expected the pre-commit hook and `make lint` to catch the same problems.
- I planned to leave Alembic until the schema actually changed.
- I expected the Stage 1 per-paper `upsert()` to be enough for ingestion.

**Where it resisted, and what I did next.**
- `no such volume`: **Docker had no volumes at all**. I ran `make reset` instead.
- `\d papers` showed **no defaults on `created_at` / `updated_at`**, because columns declared on `Paper` replaced the ones from the mixin. I deleted them and re-seeded (`511c15d`).
- **`.gitignore` ignored `test_*.py`**, so Stage 1's tests and `test_dag.py` were never committed. I removed the rule and committed them (`3039e2d`).
- **Pre-commit passed a mypy error that `make lint` caught.** The hook's isolated mypy couldn't see pydantic. I switched to local `uv run` hooks (`ec3c8d9`).
- **A logged request gap of 2.79 s** looked like a rate-limit violation. It wasn't: httpx logs when the response arrives, not when the request is sent.

**What Claude contributed, and what I did with it.**
- **Roadmap:** I used Claude to break my weeks goal into concrete tasks.
- **Refactoring:** Claude helped bring my code up to industry standard: error handling, retries, logging, and splitting the parser from the HTTP client.
- **XML parsing:** I didn't know much about working with XML. Claude helped me parse arXiv's Atom feed, including its namespaces (`src/services/arxiv/parser.py`).
- **Tests and tooling:** Claude wrote the parser tests and their fixture (`tests/test_arxiv_parser.py`, `tests/fixtures/arxiv_feed.xml`) and the pre-commit config.
- Accepted:
  - **`model_validate` instead of committing with mypy errors.** Keeping `make lint` green matters more than one commit.
  - **Nested settings as `BaseModel`.** Claude's test showed `BaseSettings` silently reads stray env vars.
  - **Alembic in 2A**, after I questioned it. Wiping the database gets expensive once Docling runs in 2B.
- Rejected:
  - **Claude's first fixture.** It used a paper newer than the commit date and a **made-up** date and author. It was replaced with real arXiv entries.
  - **Client tests now.** I verified the client live instead (243 papers, 3 requests).

**What I understand now, and what I still do not.**
- Understood:
  - Check the database (`\d papers`), not only the code.
  - Store `arxiv_id` without its version, or revisions create duplicate rows.
  - **Reversed:** a single `INSERT … ON CONFLICT DO UPDATE` beats a per-paper loop. It's atomic and idempotent: Sep 1 run twice still gave 243 rows.
- Not understood / not verified:
  - The arXiv client has no automated tests yet, and `upsert_many` has none either.
  - The rate limit only holds within one process.
