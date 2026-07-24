# PEDAGOGY — notion-api

## Skill summary
notion-api provides Notion workspace integration via the Notion API (v2025-09-03). Bundled scripts (notion_search.sh, notion_read_page.sh) handle pagination and type-aware extraction. Content model: page=block (shared ID space), database → data sources → schema. Critical distinction: data source ID ≠ database ID for queries.

## What Claude will learn
- Content model: page is a block, database has data sources, row is a page with data_source parent
- Notion-Version: 2025-09-03 required on every request (400 missing_version otherwise)
- Data source ID ≠ database ID — queries and schema reads take data_source_id
- 404 = almost always sharing, not bad ID — check Connections
- Bundled scripts handle pagination, title extraction, depth-first block recursion
- File URLs in block payloads expire after ~1 hour
- Filter conditions keyed by property type — schema read mandatory before writing a filter
- Pagination: has_more + next_cursor, guard against error envelope in loop

## Pedagogical assessment
Concrete operation recipes, clear content model explanation, explicit gotcha documentation (data source ID distinction, sharing requirement, version pinning). The 10 core operations are well-organized. Bundled scripts reduce hand-rolling risk.

## VERDICT: PASS
