# PEDAGOGY — claude-liam-web-artifacts-builder

Skill: `web-artifacts-builder` · Modifier: `skill-teardown`

## PREDICT (viewer question before watching)
"Can't Claude just write a single HTML file? Why does a claude.ai artifact need its own scaffold?"

## What the viewer will learn
1. The skill is for COMPLEX artifacts — state management, routing, shadcn/ui components — not simple single-file HTML/JSX; it provides a full React 18 + TypeScript + Tailwind + shadcn/ui stack provisioned in one command
2. The 4-step pipeline: init-artifact.sh → develop → bundle-artifact.sh → share bundle.html (single self-contained file with all JS/CSS/deps inlined)
3. One explicit design mandate: avoid "AI slop" — no excessive centered layouts, no purple gradients, no uniform rounded corners, no Inter font

## CONFIRM (what the reel reveals)
- TRIGGER: complex artifacts needing state management / routing / shadcn/ui components (NOT simple single-file HTML)
- init-artifact.sh: React 18+TS+Vite, Tailwind 3.4.1, 40+ shadcn/ui components, path aliases, Parcel config — all in one command
- bundle-artifact.sh: installs parcel + html-inline, builds, inlines everything → bundle.html
- Anti-slop rule: avoid centered layouts, purple gradients, uniform rounded corners, Inter font
- Testing is explicitly optional and deferred: build first, test later on request

## LAWS CHECKED
- ✅ TRIGGER is clear: "complex artifacts / state management / routing / shadcn/ui" (NOT simple HTML)
- ✅ SELF-DEMO: B02 shows design mandate and bundle anatomy verbatim from SKILL.md
- ✅ HANDOFF LAW: BHTF narration reads prompt aloud AND explains what to watch for
- ✅ ILLUSTRATE LAW: UI only at B00 and BHTF bookends
- ✅ ASK→RESULT law: B00 shows ask + TRIGGER + result

## VERDICT: PASS
