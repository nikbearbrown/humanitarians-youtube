# STEM Video: What Is Prompt Injection? — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya from the Mycroft team.
This video is about prompt injection — the attack that topped OWASP's list of the top ten risks in LLM applications in 2025, and hasn't moved since.

## B00 — Cold open
A text file on a webpage. A document a user uploads. An email an agent is asked to summarize. Any of these can carry instructions the model will follow — instructions that weren't put there by the developer.

## B01 — Direct vs indirect
Method: there are two real, distinct forms. Direct injection is when a user types adversarial instructions straight into the interface — "ignore your previous instructions and do this instead." Indirect injection is far more dangerous: the attacker's instructions arrive in external data the model retrieves or processes — a web page, a document, an email — not through any user-facing input at all.

## B02 — Why it's genuinely different from SQL injection
Traditional injection attacks exploit poor input validation in code. Prompt injection is different in kind: the model follows natural language instructions by design. There is no separator between "data" and "instruction" — it's all text, processed together. That's not a bug in a specific model; it's a structural property of how language models work.

## B03 — The real, current scale
This isn't theoretical. <cite index="40-1">Cisco found prompt injection weaknesses in 73% of audited production AI deployments, regardless of model type.</cite> <cite index="40-1">OWASP ranks prompt injection at the top of their 2025 Top 10 for LLM Applications specifically because indirect attacks scale.</cite> <cite index="40-1">HiddenLayer's 2026 report found autonomous agents account for 1 in 8 reported AI breaches.</cite>

## B04 — Why agents make it worse
The real severity scales with what the model can do. A model that can only talk produces text. A model wired to send email, query databases, or execute code — a real agent with real tool access — turns a successful injection into a real-world action. The instruction in the malicious document doesn't just change the response. It takes the action.

## B05 — Handoff
Your turn. If you're building an AI-powered app that reads external content — documents, emails, web pages — ask what the worst instruction that content could contain would do. If the answer is "something you'd never want the app to do," that's the injection surface you need to think about.

## B06 — Outro
What Is Prompt Injection? Built with Claude, for Humanitarians AI.
