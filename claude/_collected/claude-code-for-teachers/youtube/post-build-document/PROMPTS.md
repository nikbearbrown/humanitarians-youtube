# PROMPTS — post-build-document

## B02 — Generate five-section post-build document
```
claude "Generate post-build document for sorting simulator.
  Five sections:
  (1) What was built (artifact + deployed path)
  (2) Surface-routing (Claude tasks vs human-only)
  (3) Delegation log (gate checks run, errors caught)
  (4) Verification evidence (checks passed, fixes)
  (5) Reflection (one concrete change next build)"
```

## B05 — Score delegation log on four dimensions
```
claude "Score the delegation log on four dimensions:
  task routed, gate check run,
  error corrected, verification evidence.
  Does the log score all four?"
```
