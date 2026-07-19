# PEDAGOGY — package-hallucination-scanner

## Concept

Package hallucination scanner / slopsquatting prevention: how to catch a hallucinated package name before it becomes a security risk.

## Question

How do you catch a hallucinated package name before it becomes a security risk?

## Answer

Query the registry API for every import name before running pip install. A 404 response means the package doesn't exist on PyPI — and a package that doesn't exist today is a potential slopsquatting target tomorrow. The scanner converts a subjective judgment ("does this package sound real?") into a machine-checkable fact (HTTP 404 or 200).

## Key Concept: The slopsquatting attack surface

1. Model hallucinates a plausible package name (requests_oauth_helper)
2. Name doesn't exist on PyPI — yet
3. Attacker mines model outputs, finds recurring hallucinated names
4. Attacker registers the name with malicious payload
5. Student runs pip install — malicious code executes

The scanner catches step 1 before step 5 is possible.

## Source

Chapter 05: Five Supervisory Capacities (Plausibility Auditing section) — claude-code-for-students
Spracklen et al. 2024-25 USENIX Security: slopsquatting characterization
