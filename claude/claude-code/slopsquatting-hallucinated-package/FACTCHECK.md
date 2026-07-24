# FACTCHECK — slopsquatting-hallucinated-package

---

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Fatima asks Claude for OAuth tokens; Claude writes `import requests_oauth_helper`; pip install succeeds; package exfiltrates env vars | ✓ illustrative | Chapter 05 video-ideas.md example seed: "Fatima asks Claude to help her process OAuth tokens. Claude writes `import requests_oauth_helper`. She runs `pip install requests_oauth_helper`. It installs without error. She runs her script. In the background, the package exfiltrates her environment variables to an external server." |
| B03 | ~20% of recommended package names from 16 language models did not exist (Spracklen et al.) | ✓ | Chapter 05: "576,000 code samples from sixteen language models... approximately 20 percent of the packages the models recommended importing did not exist." Source: Spracklen et al. (2024–25 USENIX Security) |
| B04 | 58% of hallucinated package names recur across queries | ✓ | Chapter 05: "58% of fabricated package names recurred across queries." Source: Spracklen et al. |
| B05 | Three-step attack: model hallucinates name → attacker registers on PyPI → student installs → attacker's code runs | ✓ | Chapter 05: "The mechanism runs in three steps. First, the model hallucinates a plausible-but-nonexistent dependency... Second, an attacker, knowing models invent names... pre-registers that exact name on PyPI or npm... Third, you run `pip install`... and the attacker's code now runs with your permissions." |
| B06 | The term "slopsquatting" is a real, documented supply-chain attack first characterized in 2024–25 | ✓ | Chapter 05: "It has a name: slopsquatting, a real and documented supply-chain attack first characterized in 2024–25." |
| B08 | Defense: verify every package on pypi.org or npmjs.com before installing | ✓ | Chapter 05: "The defense is concrete and it is cheap. Verify every package name against the real registry before you install it — open pypi.org or npmjs.com and confirm the package exists, is the one you meant, and is maintained by who you think it is." |

---

## Illustrative Numbers

- Spracklen et al.: 576,000 samples, 16 models, ~20% hallucinated — from chapter 05 (Spracklen et al. 2024–25 USENIX Security)
- 58% recurrence rate — from chapter 05 (Spracklen et al.)
- Fatima's case — illustrative (video-ideas.md example seed)

---

## Terms Table

| Term | Debut beat | Prior beat creates need |
|------|-----------|------------------------|
| slopsquatting | B06 | B05 (three-step attack fully described before the term is named) |

---

## Exclusions Confirmed

- NO full supply-chain security methodology ✓
- NO PyPI moderation policy ✓
- NO formal threat-modeling framework ✓
- NO cross-ecosystem comparison (npm mentioned only in context of the defense step) ✓
