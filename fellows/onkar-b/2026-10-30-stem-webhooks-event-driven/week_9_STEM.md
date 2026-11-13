# Week 9: Webhooks & Event-Driven Architecture

**Series:** STEM AI Explainer
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A cartoonish server repeatedly taps another server on the shoulder, asking "Are you done yet? Are you done yet? Are you done yet?" The second server looks exhausted.
**ON SCREEN:** `THE POLLING PROBLEM`
**VO:**
Hi, I am Onkar Bhujbal. If you have two software systems that need to talk to each other, the worst thing you can do is have one constantly ask the other for updates. This is called Polling, and it wastes massive amounts of computing power. Today, we are looking at Event-Driven Architecture, and why AI applications rely on the "Don't call us, we'll call you" approach known as Webhooks.

### SCENE 2 — PUSH VS PULL
**VISUAL** — The scene splits. Left side (Pull): Server A sends 10 requests to Server B; 9 return empty, 1 returns data. Right side (Push): Server A does nothing. Server B suddenly pushes a payload to Server A.
**VO:**
In a traditional polling model, a client pulls data by repeatedly pinging a server to see if a task is finished. But AI models can take thirty seconds, or even several minutes, to generate an answer. If your app is polling the server the entire time, you will exhaust your network limits. A Webhook flips this into a push model. You give the server a URL and say, "Take your time. Send a POST request to this address when you finish."

### SCENE 3 — THE ANATOMY OF A WEBHOOK
**VISUAL** — A minimalist HTTP POST request materializes. It highlights the Target URL, the Headers (including Auth), and the JSON Body containing the event data.
**VO:**
A webhook is incredibly simple. It is just an automated HTTP POST request triggered by an event. The sender doesn't care what the receiver does with the data; it just fires the payload at a predetermined URL and forgets about it. This allows systems to remain completely decoupled. 

### SCENE 4 — AUTOMATION ENGINES
**VISUAL** — A webhook payload flies into an n8n node. It instantly branches out to three different icons: a Slack logo, an Email logo, and a Database logo.
**VO:**
Webhooks are the backbone of modern automation. When you pair event-driven webhooks with orchestration tools like n8n or Zapier, one simple POST request can trigger a cascading workflow that alerts your team on Slack, emails a client, and updates a database—all asynchronously, without slowing down your primary application.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`TASK: Stop polling. Start pushing.`
**VO:**
Stop wasting compute on empty requests. Build your systems to react to events, not wait for them.
Liam, for Onkar Bhujbal and Humanitarians AI.