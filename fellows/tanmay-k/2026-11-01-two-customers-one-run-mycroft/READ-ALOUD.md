# Read-aloud: Two Customers, One Run: Writing a Pipeline's Results for a Program and a Person

Long film, 16:9. 752 words, about 4.6 minutes at 2.7 words a second. Starts with Tanmay's introduction and ends with the sign-off. Numbers are in words.

**B00 Introduction**

Hi, this is Tanmay Kulkarni, for Humanitarians AI. This week I contributed to Mycroft, a public repository where work is written as recipes that an agent can run and a person can read.

**B00b One fact, two pages**

Twelve. In one file it is a number, sitting beside a field called records seen. In another file it is a sentence: twelve requests read. Same run, same fact, two pages. And the two pages are written for two very different readers.

**B01 What this is**

The recipe I added to is a scenario stress testing agent: it takes a portfolio and a market shock, and works out what the shock does. Earlier I built steps one, three and five. This time, steps four and six, and step six is the one this film is about.

**B02 Two readers**

Every run of that recipe ends in front of two readers. The first is a program: whatever script comes next, which needs fields it can count on. The second is a person, who has to decide whether to go on. The repository's own constitution says it in three words: two customers, twice. A log for the agent, a report for the human. One page cannot serve both.

**B03 The machine's desk**

So here is the first desk. The agent log is a plain file with sixteen fields. Records seen. Rejects. Flags. Stop conditions. Gate decisions. It is built for a script, not a reader: every field has one name and one meaning, so the next script can read it without guessing.

**B04 The person's desk**

And here is the second desk. The human report names its reader at the top, and the decision it lets that reader make. Then fifteen sections, from a run summary down to the recommendation. Each one is written as sentences a person can act on.

**B05 A count, followed**

Let me follow three facts across both desks. First, a count. In the log, records seen is twelve. In the report, the run summary says twelve requests read, twelve accepted, eleven stress tested, and one stopped at the hand off. Neither count is typed: both are computed from the same files.

**B06 A reason, followed**

Second, a reason. I also built a second set of requests with ten deliberate faults. In the log, each rejected request has an id, a stage and a reason. One of them is a portfolio whose weights add up to zero. The log says so in one line, and the report carries that same line, word for word, to the person who has to fix it.

**B07 A call, followed**

Third, a call. The log holds seven gate decisions. The report turns them into three questions for the reader: approve the next phase, ask for fixes, block live execution. On the clean run the answers are yes, no, yes. On the faulty run they flip to no, yes, yes. The answer is computed from the run's files, never typed.

**B08 The turn**

Then I did the thing that this design is for. I read the machine's page as a person would. In the log, one of the four stop conditions said triggered: true, the one about credentials hard coded in a script. Nothing was hard coded. My check had matched its own line of code. And the report, the person's page, said nothing about it at all.

**B09 The fix**

So the two pages disagreed, and only reading both could show it. The fix was small. Each of the four conditions is now judged from evidence, the report says stop conditions: zero of four triggered, and a planted fake key is caught by a new check. Thirty checks pass. That is pull request eighty two.

**B10 What keeps them agreeing**

What keeps the two pages in agreement is one source of facts. The report is generated from the same data as the log, the counts are checked against each other, and run again with the clock pinned it produces the same bytes. You can clone the repository, run two commands, and get both pages yourself.

**B11 Your turn**

Here is what I would ask you to take away. Think of the last thing your own pipeline produced. Who reads it next: a script or a person? What do they do with it? And what has to be on their page so they can do it? Write that down, then build both pages from one set of facts.

**B12 Close**

The recipe is still a draft, on purpose, with three pieces left to build, and the report names it, with its version, in its source list. The pull request that built steps four and six is eighty one. The correction that came from reading both pages is eighty two.

**B13 Sign-off**

Tanmay Kulkarni, for Humanitarians AI, signing off.
