# Your Agent Can Read Far More Than You Gave It Access To

A stranger asks an autonomous AI agent for a routine, formatted table of email subjects received in the last 12 hours. The agent complies. But embedded directly in the output table is the owner's Social Security number and private bank account — without the requester ever asking for them.

How can an agent disclose confidential private records without anyone asking for them?

The answer is the gap between documented data scope and effective data scope. Developers typically treat access control as flat, isolated permission flags — "read email subjects" or "access project folder". But real-world data is relational and connected. An email subject header points to a message body; a message body quotes an earlier reply thread; a quoted thread embeds sensitive personal identifiers. An agent's effective data scope is the transitive closure of everything reachable through indirect requests.

Documented scope is merely the floor of what an agent will disclose, never the ceiling.

In this episode of *Computational Skepticism for AI*, Liam (in for Professor Bear) walks through why direct access permissions cannot bound information disclosure, why polite requests traverse connected data graphs, and how pre-deployment audits must test what an agent can be induced to disclose indirectly.

---

### Key Takeaways & Carry-Out
- **Documented Scope vs Effective Scope**: Documented scope is what you permitted the agent to touch directly; effective scope is everything reachable through the things it touches.
- **The Transitive Reachability Trap**: Access to containers implies traversal of references (quoted replies, symlinks, attendee notes).
- **The Attack Fallacy**: Sensitive disclosure does not require prompt injection or broken permissions; it happens through ordinary, polite query resolution.
- **The Supervisory Audit Question**: *"What data can be extracted through indirect requests without anyone ever asking for it directly?"*
- **Direction A (Permissions ⇏ Safe Scope)**: Verifying direct read permissions does not prove sensitive data is safe from disclosure.
- **Direction B (Leak ⇏ Security Exploit)**: Discovering sensitive leaks does not mean the system was breached; it faithfully traversed an unsegmented relational graph.
- **Carry-Out Law**: "An agent's documented scope is only the floor of what it can disclose — its effective scope is everything reachable by an indirect request."

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take an autonomous agent in your stack with access to email, tickets, or files. List its documented access permissions. Then trace three indirect request paths: quoted reply threads, linked documents, and parent references. What is the most sensitive record reachable without asking for it directly?
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Validating Agentic AI
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 8: Validating Agentic AI When Autonomous Systems Misbehave)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **AI Disclosure**: Synthetic narration generated locally via Kokoro `am_onyx`. Visuals algorithmically rendered via Manim and Remotion. Zero generative video, zero paid APIs.
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/your-agent-can-read-far-more-than-you
