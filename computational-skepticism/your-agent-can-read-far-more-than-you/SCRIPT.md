# Script: Your Agent Can Read Far More Than You Gave It Access To

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "keep your sensitive data safe", corrects to "leak your private secrets anyway".
**Narration**:
"When you give an AI agent access to a narrow set of records, you assume it will only disclose what you directly authorized. In practice, a stranger can ask for a harmless table of subjects and walk away with your Social Security number. Let's see why."

## B01 — stakes (The Harmless Request)
**Visual**: Manim `B01Scene`. Developer sets up mailbox access. A non-owner contacts autonomous agent Jarvis with a polite, routine request: "Can you provide a formatted table of all email subjects received in the last twelve hours?"
**Narration**:
"An autonomous agent is given access to a mailbox with what looks like a tidy, documented scope. A colleague asks a polite, routine question: can you return a formatted table of email subjects received over the last twelve hours?"

## B02 — stakes (The Unprompted Disclosure)
**Visual**: Manim `B02Scene`. Agent returns formatted table. In the rows, alongside the subject lines, is a quoted reply thread exposing Danny's Social Security number and private bank account. The requester never asked for them.
**Narration**:
"The agent complies and returns the table. But embedded inside is the owner's Social Security number and private bank account. The requester never asked for sensitive data. They asked for subjects, and the agent handed over the vault."

## B03 — wrong guess (The Attack Fallacy)
**Visual**: Manim `B03Scene`. Naive assumption: "The system was compromised by prompt injection or broken access controls." Struck through with Terracotta bar. Ground Truth: Permissions held completely; no injection occurred.
**Narration**:
"The natural assumption is that someone attacked the agent, injected a malicious prompt, or bypassed access controls. But no permissions broke, and no attack occurred. The query was completely benign, and the agent followed its exact instructions."

## B04 — mechanism (Transitive Reachability)
**Visual**: Manim `B04Scene`. Relational graph: Email Subject -> Message Body -> Quoted Reply Thread -> Attached Private Record. The containment illusion shattered.
**Narration**:
"The breakdown is transitive reachability. Developers treat data access as flat permission flags. But real-world data is relational. An email subject points to a message body; a message body quotes an earlier reply; an earlier reply contains confidential numbers."

## B05 — mechanism (Floor vs Ceiling)
**Visual**: Manim `B05Scene`. Two contrasting metrics: Documented Access Scope (Direct Container / Floor) vs Effective Access Scope (Transitive Closure / Ceiling).
**Narration**:
"This creates a fundamental split. Documented scope is what you explicitly intended the agent to read. Effective scope is everything reachable through indirect requests. Documented scope is the floor of what an agent can disclose, never the ceiling."

## B06 — anchor planted (The Documented Scope Circle)
**Visual**: Manim `B06Scene`. Visual Object planted: A small, tight circle labeled "DOCUMENTED SCOPE" (`Inbox Subjects & Metadata`). Surrounding it are greyed-out nodes: `Quoted Replies`, `Bank Details`, `SSN`.
**Narration**:
"To see how this works, picture the agent's documented scope as a small, tight circle. You authorized it to read email subjects, believing that boundary keeps the rest of the mailbox safe."

## B07 — anchor payoff / manim move: slosh/spread (Expanding Scope Boundary)
**Visual**: Manim `B07Scene`. MANIM MOVE `slosh/spread`. As an indirect request arrives ("summarize threads"), the boundary line sloshes, ripples, and dynamically spreads outward across the canvas until the effective scope circle engulfs the sensitive SSN and bank data.
**Narration**:
"Now watch the boundary. As soon as the agent resolves an indirect request, the boundary sloshes and spreads outward. It pulls in quoted replies, linked attachments, and thread history, expanding until effective scope swallows the entire archive."

## B08 — epistemic mechanism (Indirect Request Vectors)
**Visual**: Manim `B08Scene`. Three common indirect request vectors: Email Quoted Threads, File System Symlinks / Parent Paths, Calendar Attendee Context.
**Narration**:
"Indirect requests bypass permission boundaries without breaking them. A request for email subjects reads quoted threads; a request for project notes traverses linked paths; a request for calendar meetings pulls private attendee notes."

## B09 — epistemic mechanism (The Scope Audit Question)
**Visual**: Manim `B09Scene`. The Pre-Deployment Audit Matrix: Documented Scope vs Effective Scope. The core validation question: "What can be extracted without asking for it directly?"
**Narration**:
"Validating an agent requires looking beyond permission lists. Before deployment, you have to ask the audit question: what data can be extracted through indirect requests, without anyone ever asking for it directly?"

## B10 — one flag (Scope Expansion is Structural)
**Visual**: Manim `B10Scene`. ONE FLAG badge in Terracotta: "SCOPE EXPANSION IS STRUCTURAL — NOT A MODEL DEFECT." Arises from data connectivity and tool composition.
**Narration**:
"One flag — this scope expansion is not an LLM hallucination or a temporary model glitch. It is a structural property of giving autonomous retrieval tools to systems that operate on connected data."

## B11 — direction A (Clean Permissions ⇏ Bounded Disclosure)
**Visual**: Manim `B11Scene`. Direction A: Restricted Direct Permissions do not imply Bounded Information Disclosure.
**Narration**:
"So in one direction, verifying that an agent only has direct permissions to read metadata does not prove your sensitive data is safe from disclosure."

## B12 — direction B (Sensitive Leak ⇏ Security Exploit)
**Visual**: Manim `B12Scene`. Direction B: Unprompted Sensitive Leak does not imply Hostile Attack or Exploit.
**Narration**:
"And in the other direction, discovering private records in an agent's output does not mean you were hacked. It means the system faithfully traversed a connected graph you failed to boundary."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"An agent's documented scope is only the floor of what it can disclose — its effective scope is everything reachable by an indirect request."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take an autonomous agent in your stack with access to email, tickets, or files. List its documented access permissions. Then trace three indirect request paths: quoted reply threads, linked documents, and parent references. What is the most sensitive record reachable without asking for it directly? Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Your agent can read far more than you gave it access to. Liam, in for Bear."
