# PEDAGOGY — claude-liam-jira-api

## Skill
jira-api (claude-tag-plugins / jira)

## Learning objective
Understand the two Jira Cloud API families (Platform REST v3 + Agile REST v1), Atlassian Document Format for body fields, and the three distinct pagination schemes.

## Prior knowledge assumed
Knows what Jira is; has done REST API work; unfamiliar with Jira Cloud specifics.

## Key concepts
1. Two API families: Platform REST v3 (issues/projects/search) vs Agile REST v1 (boards/sprints)
2. ADF (Atlassian Document Format) — description and comment bodies are JSON trees, not plain text
3. Transitions: can't set status directly — must list transitions and POST by ID
4. Three pagination schemes: nextPageToken (JQL search), offset+isLast (most lists), nested key (comments)
5. 404 not 403 for issues you can't browse — silent access control

## VERDICT: PASS

The skill covers the critical mechanics. Key gap: three pagination schemes in one API
with no consistent "here's how to auto-detect which scheme applies."
