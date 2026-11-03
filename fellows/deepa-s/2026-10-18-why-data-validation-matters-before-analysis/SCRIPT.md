# Script — Why Data Validation Matters Before Analysis

Narrator: Liam / Kokoro `am_onyx`, speed 1.0. New revision; human narration review pending.

## B00 — Check before you calculate

A chart can look polished even when its inputs are wrong. This is Liam, narrating for Deepa. Before analysis, data validation asks whether records follow the structure and rules needed for the task. It helps us decide what can be analyzed, what needs investigation, and what uncertainty must remain visible.

## B01 — Missing is not zero

Consider a fictional customer table with an empty monthly-spend field. Empty might mean not collected, not applicable, or unavailable. It does not automatically mean zero spending. Count missing values, check their meaning, and document how they are handled. The method can change both the summary and the population it represents.

## B02 — Types and formats matter

A numeric column can contain text such as unknown, or amounts stored with incompatible separators. A date like zero three slash zero four is ambiguous without a format convention. Check field types, valid parsing, date formats, and units before calculating or joining records. Keep parsing failures visible instead of silently dropping them.

## B03 — Know what one row means

Duplicate and inconsistent records need context. If a table should contain one row per customer, a repeated customer key can double-count someone. In a transaction table, repeated customers can be entirely legitimate. Define the record key, check duplicates against it, and normalize categories only with a documented rule.

## B04 — Rules should fit the task

Range checks can flag a negative age. Cross-field rules can flag an end date before a start date. Allowed-category checks can reveal inconsistent labels. But an unusually large purchase is not automatically wrong. Investigate the source and business meaning before correcting or excluding an observation.

## B05 — Bad inputs change the answer

Here is a fictional units error. Two purchases are ten dollars and twenty dollars, but the second arrives as two thousand cents. Treating both numbers as dollars gives a total of two thousand ten dollars. Applying the documented units correctly gives thirty dollars. The arithmetic worked in both cases; the interpretation did not.

## B06 — Validate, investigate, recheck

Start with expected columns and row counts. Check types, formats, missingness, keys, categories, ranges, and relationships between fields. Retain the original data. Record each correction, conversion, or exclusion and why it was justified, then rerun the checks. Automated flags guide investigation; they cannot replace domain knowledge or source verification.

## B07 — Trust has conditions

Validation improves trust by making assumptions and failures visible. Passing a rule set does not prove that every value is true or that a dataset represents the right population. Why Data Validation Matters Before Analysis: inspect the inputs before trusting the output. Liam, narrating for Deepa, for Humanitarians AI.
