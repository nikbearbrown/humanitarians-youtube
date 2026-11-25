# Read-aloud: Ask Whether, Never What: Checking a Pipeline's Keys Without Reading Them

Long film, 16:9. 667 words, about 4.1 minutes at 2.7 words a second. Starts with Tanmay's introduction and ends with the sign-off. Numbers are in words; the key's name is spelled the way it will be said.

**B00 Introduction**

Hi, this is Tanmay Kulkarni, for Humanitarians AI. This week I contributed to Mycroft, a public repository where work is written as recipes that an agent can run and a person can read.

**B00b Six steps, nothing touched**

One command. Six steps run in order, and the last line says: all six steps completed. In all that time, nothing was contacted, and no key's value was kept. How does a pipeline get ready to run without touching anything it needs?

**B01 What this is**

The recipe is a stress test: hand it an invented set of holdings and a market fall, and it adds up the damage. I have built five of its six steps in earlier weeks. This week is step two, which comes right after the provenance check: before any request is checked or any tool runs, it lists what the pipeline would reach for.

**B02 Three facts, not one**

A pipeline that reaches outside depends on things: a service to call, a key to call it with. About each one there are three different facts. Is it there? Who has to say yes? And what is the value? They feel like one question. They are three.

**B03 One row**

The workflow names four sources. Let me follow one: the model call. It gets a row. A name, the Groq chat model, an AI model hosted by a company. A status: approval required. And a reason, in plain words: a live model call, and sample mode, the practice mode with invented data, never makes one.

**B04 Is it there**

Now the first fact. The row carries the key's name, on screen now, and the script asks the program's settings, the environment, one question: is a variable with this name set? The answer is a yes or a no. Here it is no. The value is never stored, and never written to a file.

**B04b Why a yes or a no**

Why so careful? A value can end up in a log, a report, a screenshot, a message. A yes or a no cannot. Whatever the page says, there is nothing in it to copy.

**B05 Who says yes**

The second fact. Approval record: none. Approved for live action: false. Live call performed: false. The page does not decide anything. It records that a person has not yet said yes, because saying yes is a person's act.

**B06 The other three**

Beside it, the other sources. The webhook is available: twenty-two invented requests, each with a fingerprint recorded when the set was fixed, checked before each one is kept as it was. Twelve are clean, ten are faulty, none rejected. Chat is skipped, with a reason. The other live service is approval required, like the first. Every source lands in one of those states, with a reason.

**B07 The puzzle**

Then a small puzzle. To prove the script never leaks a key, the test needs a key. A made-up key typed into a test file can look, to a reader or a scanner, like a real one that leaked. So the test builds two dummy values while it runs, from pieces, and they exist only until it ends.

**B07b The hard case**

Now the hard case: set both keys. The page says yes, twice, and the values appear in no file the step writes and not on the screen. And every question the script puts to the environment is a yes or a no. Thirty-seven checks pass, this among them. To test a promise to keep a secret, I first had to make one that was safe to lose.

**B08 What you get**

And what you get is simple. Clone the repository, run the command, and read one page that says what a live run would need, with nothing contacted.

**B09 Your turn**

So here is a small exercise. Take one thing your own pipeline reaches for. Write three lines: is it there, who has to say yes, what is the value. Fill in the first two. Then design the third so that nothing downstream ever needs it.

**B10 Close**

The recipe stays a draft by design. Going live is the next piece, and that is a person's call. Step two arrived in pull request eighty five, and it is merged.

**B11 Sign-off**

Tanmay Kulkarni, for Humanitarians AI, signing off.

