# Weekly Hours: Continuous Integration and Rollback

**Project:** MEDAS Aggregation Frontend — CI/CD & Rollback Pipeline
**Friction Log:** [FICTIONAL.md](FICTIONAL.md)
**Report Week:** Sep 3, 2026
**Total Hours:** 21.0 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Hours |
|---|---|---:|
| **Meetings** | Weekly supervisor check-in | 2.0 |
| **Technical Learning & Research** | Studying the distinction between an automatic/lenient check (CI) and a manual/strict one (Rollback), and why GitHub's Free-plan branch protection limits merge-blocking to public repos | 4.0 |
| **CI Workflow Verification** | Walking the CI workflow's full step sequence (checkout, Node setup, `npm ci`, lint, test, build) and confirming which steps are blocking versus continue-on-error | 7.5 |
| **Rollback Guard Verification & Worked Example** | Walking the Rollback workflow's input-validation and image-exists guards before redeploy, and proving CI's actual non-blocking behavior with a deliberately broken test on PR #2 | 6.0 |
| **Brutalist Video Reel Production** | Scripting `beat_sheet.json` and generating narration for the `medas-ci-rollback` reel | 1.0 |
| **Documentation** | Authoring `README.md` and `FICTIONAL.md` for this folder | 0.5 |
| **Total** | | **21.0** |

---
