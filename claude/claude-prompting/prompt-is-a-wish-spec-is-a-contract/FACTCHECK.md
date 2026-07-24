# FACTCHECK — prompt-is-a-wish-spec-is-a-contract

---

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Seth types "write me a login function," Claude responds in ~11 seconds | ✓ illustrative | Chapter 04, Seth's attempt one — labeled composite |
| B01 | Output: MD5 hash, global dict, accepts empty strings, 12 lines | ✓ illustrative | Chapter 04: "hashes the password with MD5... global dict called USERS... twelve lines, clean" |
| B01 | "approximately the worst login function a real codebase has ever shipped" | ✓ editorial | Chapter 04 paraphrase |
| B03 | MD5 is the dominant hash pattern in training distribution | ✓ editorial | Chapter 04: "MD5 — an algorithm considered cryptographically broken for password storage for over a decade" — accurate |
| B04 | MD5 considered broken for password storage for over a decade | ✓ | Chapter 04, widely documented in security literature |
| B05 | Specification names invariants, files in scope, format, boundary | ✓ | Chapter 04: "names the invariants... the fields the code may touch... the boundary the code may not cross" |
| B06 | Six spec sentences: bcrypt, db.py helper, empty credentials error, token+expiry, no schema.sql, pytest 5 cases | ✓ illustrative | Chapter 04 spec verbatim (condensed) — labeled |
| B07 | Claude asks: should the token be stored or just returned? | ✓ illustrative | Chapter 04: "it asks one clarifying question Seth hadn't thought to ask" |
| B07 | Second attempt: ~30-line function, all five test cases | ✓ illustrative | Chapter 04 |
| B08 | Tomas: prompt → plaintext dict; spec → defensible function | ✓ illustrative | Chapter 04 example seed from card — labeled composite |
| B09 | "The prompt is what you say to Claude before you have decided what you want" | ✓ | Chapter 04 verbatim |
| B09 | "The specification is what you say to Claude after. The decision is the work." | ✓ | Chapter 04 verbatim |
| B11 | Second attempt: 20 minutes start to finish; first: 6 seconds | ✓ illustrative | Chapter 04: "maybe twenty minutes start to finish, against six seconds for the first" |
| B12 | "The prompt is what you wish for. The specification is what you contract for." | ✓ | Chapter 04 verbatim |

---

## Illustrative Numbers

- Seth's 11 seconds / 12 lines — illustrative composite (chapter 04)
- Tomas's 8 minutes / study tracker — illustrative from card example seed
- Second attempt: 20 minutes — illustrative (chapter 04)

---

## Terms Table

| Term | Debut beat | Prior beat creates need |
|------|-----------|------------------------|
| prompt | B01 (implicit) | B01 (the failure IS the prompt) |
| specification | B05 | B03 (prompt-as-wish failure established) |
| invariants | B05 | B05 (spec definition beat) |
| boundary | B05 | B05 (spec definition beat) |
| handoff condition | B10 | B09 (decision-is-the-work established) |
| boondoggle | B11 | B11 (prompt result named) |

---

## Exclusions Confirmed

- NO OAuth flows ✓
- NO full security audit methodology ✓
- NO prompt engineering tricks or jailbreaks ✓
- NO history of password-hashing algorithms (MD5 mentioned only as what Claude wrongly chose) ✓
- NO Brooks / Mythical Man-Month citation in narration ✓ (excluded per scope)
