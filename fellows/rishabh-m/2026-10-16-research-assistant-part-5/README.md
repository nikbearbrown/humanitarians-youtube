# The Queue Is A Query

- **Status:** built — awaiting Rishabh's review
- **Series:** Building a Research Assistant · Part 5 (Stage 2B)
- **Channel:** @HumanitariansAI · **Voice:** Kokoro `af_sarah` · **Greeting:** Hola (slug pick)
- **Long:** 3840×2160 · 4:51 · 17 beats — `research-assistant-part-5.mp4`
- **Short:** 2160×3840 · 1:20 · 9 beats — `short/research-assistant-part-5-short.mp4`
- **Last updated:** 2026-10-16

## Subject
Stage 2B, Oct 12–15: pending papers get their PDFs downloaded (rate-limited, byte-checked,
cached atomically by version), parsed by Docling inside Airflow only, and saved as sections.
Per-paper status in the database makes the work queue a query; one failure stays one failure,
and a run where everything fails raises. Proven both ways, including a test that must fail.

## Notes
- First person, build-log framing. No course/reference mentioned; no credit line.
- Parser choice stated honestly: no local benchmark run; the comparison script is ready.
- Omitted for length: the YAML volume typo and `docker compose cp` permissions.
- LOGO LAW: Docling's official mark added to `icons/logos/docling/`.
