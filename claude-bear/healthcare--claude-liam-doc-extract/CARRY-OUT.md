# CARRY-OUT.md (GATE C)

**Carry-out sentence (BCRY):**
> Turning a document into text, and understanding that text, are two different jobs —
> doc-extract only does the first one.

**Wrong guess it defeats:** a newcomer reading "extract text from a document" assumes
the skill reads the document *for* you — summarizes the contract, answers what's in it.
It doesn't. `doc-extract`'s whole job stops at plain text: PDF/DOCX/XLSX/PPTX/RTF/
text-markdown-HTML in, plain text out. Interpretation is a separate step, done by
Claude (or another skill) *after* extraction, not by this skill.

**Test:** "extracting text and understanding it are two different jobs" survives being
repeated by someone who wasn't paying full attention, and stays true — it compresses
the actual distinction (mechanical format conversion vs. reading comprehension), not
the topic ("this video is about a document skill").
