# STEM Video: Schema Drift — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video is about schema drift — why the same field can mean something different depending on where it's coming from, and why that quietly breaks real pipelines.

## B00 — Cold open
A supplier adds one new column to a CSV. Overnight, real dashboards start showing blank numbers for key metrics. Nobody changed the dashboard. The data underneath it just changed shape.

## B01 — What schema drift actually is
Method: schema drift is any unplanned change in a data source's structure — a field added, removed, renamed, or its meaning quietly shifted — that a downstream system wasn't built to expect. It's especially common wherever multiple systems or vendors feed into one pipeline, since nobody upstream is obligated to warn you before they change something.

## B02 — A real, documented case
A real Azure Data Factory pipeline broke this way: a supplier added a field called Lot Batch Notes to their CSV. The ingestion job wasn't built to expect it, and downstream Power BI dashboards started showing nulls for key numbers — not because the data was wrong, but because the shape it arrived in had quietly changed.

## B03 — The same pattern, at the field level
Drift doesn't have to change the schema's shape to still break things. Sometimes a field stays exactly where it's supposed to be, but what counts as empty changes underneath you. One real system returned an empty string for a missing value. A check written to look for a missing value expected null instead. The field never changed position — what it meant when it was empty did.

## B04 — Why this matters more as pipelines get longer
The more systems a piece of data passes through, the more chances there are for one of them to quietly redefine what a value means. A pipeline can run clean for months and still be carrying an assumption nobody's checked lately.

## B05 — Handoff
Your turn. Pick a field in a pipeline you rely on, and check what it actually returns when the value is missing — not what you assume it returns. The gap between those two answers is exactly where schema drift hides.

## B06 — Outro
Schema Drift. Built with Claude, for Humanitarians AI.
