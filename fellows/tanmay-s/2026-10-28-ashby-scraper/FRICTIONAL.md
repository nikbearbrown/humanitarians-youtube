# Frictional Log — Ashby ATS Scraper

## Week of 2026-10-21 to 2026-10-28
**Subject:** Ashby ATS scraper using public job-board API

**Attempted:** Hit Ashby public API (no auth) to find open roles at funded startups. Derive company slug from name in master CSV, write jobs CSV + per-company summary CSV. Expected clean slug derivation for most companies.

**Resistance:** Company name to Ashby slug mapping is not 1:1 — many use abbreviated or rebranded slugs. Fuzzy fallback logic required. Some companies on Ashby but no open roles return 404 vs empty list; handled both cases.

**Next steps taken:** Added --resume flag. Tested on 20 companies. PR submitted on branch tanmay/feature-ashby-scraper. Awaiting Nik review.

**Collaborator contributions:** Claude scaffolded retry logic; modified to match project rate-limiter pattern from Saurabh's shared utilities.

**Current understanding:** Ashby is a Tier 1 ATS. Scraper is functional and ready to run at scale once PR merges.

**Artifacts:** [Open PR](https://github.com/nikbearbrown/80-Days-to-Stay/tree/tanmay/feature-ashby-scraper)
