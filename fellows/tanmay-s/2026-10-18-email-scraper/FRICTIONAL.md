# Frictional Log — Email Scraper

## Week of 2026-10-13 to 2026-10-18
**Subject:** Playwright-based email scraper for Issue #9

**Attempted:** Build a scraper that visits funded startup homepages + /contact /about /team pages, extracts emails from mailto: links and visible text, writes to CSV in real time, supports --resume. Expected ~50% hit rate.

**Resistance:** Many pages use obfuscated emails or load contacts via JS after page load. Playwright with wait-for-load-state solved the JS issue. False positives (noreply@, support@) required regex filtering.

**Next steps taken:** Added domain-matching filter. Tested on 20 companies — 25% hit rate. Merged to nikbearbrown/80-Days-to-Stay main.

**Collaborator contributions:** Claude helped draft the regex filter pattern; accepted with minor modification. Nik confirmed Ashby + SmartRecruiters as Tier 1 priorities (Oct 21).

**Current understanding:** 25% hit rate is real — many startups don't publish emails publicly. Full 1K dataset should yield 200–250 emails. Script is production-ready.

**Artifacts:** [Merged PR](https://github.com/nikbearbrown/80-Days-to-Stay/tree/main/ATS_Scripts/scrapers/email_scraper)
