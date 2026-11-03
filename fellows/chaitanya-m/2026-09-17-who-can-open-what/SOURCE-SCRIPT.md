# Video Script — "Who Can Open What"

**Topic:** the one function that decides which textbooks a person can open (`getUserAccess`)
**Length:** ~2 min 45 sec · ~410 words
**Audience:** anyone — no technical background assumed
**Verified against:** `lib/textbook-manager.ts` on `main`

---

## SCENE 1 · THE QUESTION · 0:00–0:25

> **Visual:** a student clicking a textbook cover. Freeze the moment of the click.

"Every time a student clicks a textbook, something has to decide: are you allowed to open this?

It sounds simple. It isn't — because there are several different ways a person can end up with permission. They might have been given it directly. They might have it because of a class they joined. Or they might just be staff, and get everything.

So the system asks one question, in one place. Here's what it does."

---

## SCENE 2 · THREE KINDS OF PEOPLE · 0:25–1:15

> **Visual:** three stacked rows appearing one at a time — ADMIN / INSTRUCTOR / STUDENT.

"There are three kinds of people here, and the answer depends on which one you are.

**If you're an admin** — you run the place — you get every textbook. No exceptions, nothing to set up.

**If you're an instructor**, you get every textbook too, with one exception: anything marked *hidden*. Hidden is the setting for books still being built, still being tested. Instructors don't see those. But notice — nobody has to grant an instructor anything. Permission comes automatically with the role.

**If you're a student**, it's different. Students don't get anything by default. Every book a student can open, someone decided they could."

---

## SCENE 3 · TWO WAYS IN · 1:15–1:55

> **Visual:** two arrows converging into one list.

"And there are exactly two ways a student gets that permission.

The first is direct. An admin grants them a specific book — usually because the student asked for it and the request was approved.

The second is through a class. An instructor assigns textbooks to their class, and every student enrolled in it gets those books automatically. Join the class, get the books. No separate approval.

Those two lists get added together, duplicates removed. That's a student's shelf.

One detail worth knowing: if a class gets archived — say the semester ends — the books that came with it stop working. Access came from the class, so it leaves with the class."

---

## SCENE 4 · THE IDEA · 1:55–2:35

> **Visual:** two different moments — clicking to open, and the book checking back — both pointing at the same box.

"Now the part that's actually interesting.

This question gets asked at two completely different moments. Once when the student clicks to open a book. And again a moment later, when the textbook itself checks back with the hub to confirm the person really is allowed in.

Two different moments, two different pieces of the system — asking the same question, in the same place, and getting the same answer.

That matters more than it sounds. If those two checks had their own separate logic, they could disagree. You'd get a book that opens and then locks you out. Or worse, one that lets in someone it shouldn't.

Because the decision lives in exactly one place, they can't drift apart."

---

## SCENE 5 · CLOSE · 2:35–2:50

> **Visual:** one box. One list.

"So: admins get everything. Instructors get everything that's finished. Students get what they were given, plus whatever their classes came with.

One question, asked in one place, answered the same way every time. And if someone ever adds a new way to get access — a whole department buying a licence, say — it gets added here once, and every door in the system already knows about it."

---

## Notes for filming

- **Don't say the function's name on camera** if this is for a general audience — "the access check" or "one place" carries it fine. Save `getUserAccess` for a developer version.
- The strongest 20 seconds is Scene 4. If you have to cut for time, protect it and trim Scene 2 instead.
- Good visual for Scene 3: literally two arrows merging into one list, with a duplicate visibly dropping out.
- **Don't show a real dashboard with real student names.** Use placeholder names if you screen-record.
- If you want the animated brutalist deck for this one like the Memory API video, say so — the scenes above are already shaped for it.

## Source, if you want to check anything

`lib/textbook-manager.ts` — the `getUserAccess` function. Roughly 45 lines, and it reads top to bottom in the same order as this script: admin, instructor, direct grants, class enrollments, combine.
