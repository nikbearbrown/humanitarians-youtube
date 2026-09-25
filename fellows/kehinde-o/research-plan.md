# Research Plan

**Fellow:** Kehinde Obidele
**Project:** Medhavy Cancer Textbook Fact-Checking
**Group:** Brutalist team
**Last updated:** 2026-09-25

## Research Question

How reliably does AI-generated medical education content reproduce verifiable biomedical facts, and what systematic process can catch and correct the errors before publication?

## Methodology

Every flagged claim in the Medhavy cancer textbook is verified through a structured review process:

1. Read the flagged sentence and its AI-assigned verdict (TRUE, FALSE, or FLAGGED).
2. Locate the cited source using PubMed, PMC, FDA databases, or other authoritative references.
3. Confirm whether the citation is real, the authors are correct, and the claim is supported.
4. Record a Reviewer Decision (Approved, Needs Revision, or Rejected), Reviewer Comments with source URLs, and a Suggested Phrase with corrected text.
5. Build an Evidence Document (Word format) with the full source chain for every claim checked.
6. Submit text corrections as a pull request against the medhavi-cancer repository in exact .mdx format.

## Verification Sources

| Source | What it covers | URL |
|---|---|---|
| PubMed / PMC | Clinical and biological claims | pubmed.ncbi.nlm.nih.gov |
| FDA Orange Book | Small-molecule drug approvals | accessdata.fda.gov/scripts/cder/ob/ |
| FDA Purple Book | Biologic drug approvals | purplebooksearch.fda.gov |
| NCI SEER | Cancer epidemiological data | seer.cancer.gov |
| CDC | Public health statistics | cdc.gov |
| WHO | International health data | who.int |

## Scope

The Medhavy cancer textbook contains 38 chapters plus 4 appendices. Each chapter has an Excel workbook with flagged claims across multiple tabs (main chapter, AI-Only, Editorial). The goal is to review every chapter systematically and submit corrections for publication.
