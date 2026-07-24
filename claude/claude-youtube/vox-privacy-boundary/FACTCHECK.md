# FACTCHECK — vox-privacy-boundary

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | Program manager opened Cowork, pointed at Documents folder, asked for funder report | Illustrative | Ch08 opening scene: "A nonprofit program manager needs to assemble a quarterly report for funders. She decides to use Claude Cowork to pull information from her Documents folder... She grants access to the folder and starts the session." Near-verbatim | — |
| B02 | Folder contained client intake files with names/phones, salary sheets, email exports from dispute, interview transcripts — all in scope | Illustrative | Ch08: "It contains: the client intake files with names and phone numbers, last year's tax records, a spreadsheet of staff salaries, email exports from a fundraising dispute, and interview transcripts from a study she conducted with participant consent for internal use only." Near-verbatim | — |
| B03 | Nothing malicious happened, no data publicly exposed, but access boundary covered everything in folder | ✓ | Ch08: "Nothing malicious happened. No data was publicly exposed. But the access boundary was wrong from the start." — verbatim | — |
| B05 | Privacy for agentic AI is a configuration question — not a platform property; access boundary is what user defines before session; grant covers everything inside boundary | ✓ | Ch08: "Privacy is a configuration question, not a question about whether Claude is trustworthy." + "A grant covers everything inside the boundary, not only what was intended." (spirit) | — |
| B06 | Chat sees what you paste/upload; Code may see code repository; Cowork may see local files, connected apps, browser, scheduled tasks | ✓ | Ch08: "Claude chat — You share text and uploaded files within a conversation... Claude Code — Claude Code may access repository content, read and write files... Claude Cowork — Cowork expands access significantly... may interact with local files and folders, installed apps, browser windows and sessions, scheduled tasks, plugins, MCPs, and across-app data flows." — near-verbatim | — |
| B07 | Nothing excluded by default — only what you explicitly exclude | ✓ | Ch08: "Name forbidden files, actions, and apps. When configuring Cowork permissions, explicitly name what Claude should not touch. Do not assume exclusion by silence." — verbatim (spirit) | — |
| B08 | Dedicated working folder with grant materials only vs broad Documents folder grant | Illustrative | Constructed from Ch08 practice: "Use a dedicated working folder... that contains only materials appropriate for this session. Do not grant access to your main Documents folder or your Desktop." | None needed |
| B09 | Three pre-session steps: create dedicated folder, copy only what task needs, name what to exclude | ✓ | Ch08: "Use a dedicated working folder... Prefer copies to originals... Name forbidden files, actions, and apps." — verbatim (three separate principles combined) | — |
| B11 | Privacy is not about whether Claude is trustworthy; it is about what folder/files/actions you configured | ✓ | Ch08: "The most important reframing in this chapter: privacy is not a question about whether Claude is trustworthy. It is a question about what your specific account, plan, product configuration, retention setting, and organizational agreement actually govern." — verbatim | — |
| B14 | Trust your folder preparation, not just the platform | ✓ | Ch08: "This chapter is about setting that boundary before the workflow begins, not after something goes wrong." (spirit) + the whole chapter's practical thrust | — |

## Terms Table
| Term | Debut beat | Prior beat |
|---|---|---|
| access boundary | B05 | B01-B03 established the folder grant covered unintended files; viewer wants a frame for why |
| configuration question | B05 | Same — viewer wants to know what determines what AI can see |

## Exclusion Confirmation
- NO HIPAA/FERPA compliance detail: PASS (health and education data mentioned only as categories, no regulatory mechanics)
- NO extended legal analysis of data governance: PASS (no legal frameworks cited in narration)
- NO enterprise-vs-personal-plan comparison beyond one spoken aside: PASS (surfaces mentioned by capability, not by plan tier)

## Illustrative Examples
- B01-B03: Program manager + Documents folder grant + unintended files in scope — ILLUSTRATIVE (directly from Ch08 opening scene, nearly verbatim; labeled as illustrative)
- B08: Before (Documents folder) vs After (dedicated working folder) — ILLUSTRATIVE (constructed from Ch08 practice section)
