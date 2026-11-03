# Medhavy Hub: One Sign-In, Every Textbook

The hub does not hand your students a password for each book. They sign in once. For every textbook they are entitled to, the hub mints a twenty-four-hour token, and the textbook site checks it back against the hub. Three roles: student, instructor, admin. Today we walk the admin side.

Observed on the live admin: a registry with three statuses, user roles with the admin lock, classes, concept-map sessions, an empty request queue, and PostHog analytics. Not shown: the student library, the request flow, and the invite join. Those need a second account. Also not shown: the textbook handoff. All three textbook sites bounced back to the hub with a localhost redirect. That is a bug to fix, not a demo to fake.

---

## Chapters

0:00 Intro
0:16 One sign-in
0:31 Admin overview and registry
0:45 View All Textbooks
0:56 Users and roles
1:07 Admins and Classes
1:25 Concept Maps
1:36 Requests
1:44 Analytics
2:12 Settings
2:19 Verdict
2:41 Your Turn

---

## YOUR TURN

Paste into Claude Code from the medhavi-hub repo:

```
Read docs/creating-a-new-textbook.md in medhavi-hub. Register one textbook as private, protect its site, and grant one student. Then sign in as that student and open it.
```

One book, one student, one comparison. Then ask a person to use it.

---

Real screen capture of the live Medhavy Hub admin, driven by a scripted browser. Every student name, email and invite code was masked in the page before recording. Narration: Liam, in for Bear (Kokoro). Built with the brutalist.art `medhavy-walkthrough` skill; no paid generation.

**@NikBearBrown**

#MedhavyHub #OpenTextbooks #EdTech #Clerk #Supabase #NextJS #Claude #ClaudeCode #NikBearBrown

---

*Sources: the medhavi-hub repository (README, DEVELOPER.md, docs/) at commit efcc3f5; see the reel's SOURCES.md.*
