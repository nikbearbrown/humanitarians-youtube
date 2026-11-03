"""Single source of truth for the Muse intro film: narration + on-screen text.

Content follows the presenter's brief (Yeshwanth Balaji, Humanitarians AI fellows
playlist). Capabilities are stated as described in that brief. Terminology rule: never "model"
alone -- "AI model" for the AI, "3D model" for the mesh, "Muse" for the agent.
"""
SLUG = 'claude-liam-meet-muse'
TITLE = "Meet Muse: What It Is and Why It's Useful"
PRESENTER = 'Yeshwanth Balaji'
HANDLE = '@HumanitariansAI'

TERMS_A = [
    ('Agent', 'AI software that takes a goal and carries out the steps, not just answers.'),
    ('Token', 'A small chunk of text. AI use is measured, and limited, in tokens.'),
    ('MCP', 'Model Context Protocol: a standard way to connect an AI to tools and data.'),
]
TERMS_B = [
    ('Headless', 'A program running with no window on screen.'),
    ('Asset', 'Any file a game uses: a 3D model, a texture, a sound.'),
    ('Virtual machine', 'A complete computer simulated in software, often in the cloud.'),
]

BEATS = [
 dict(id='B00', kind='composer',
  narration=("Hi. I'm Liam, an AI voice, presenting for Yeshwanth Balaji. This video is about Muse: what it is, "
             "what it can do, and why it's useful for building games and 3D assets.")),
 dict(id='B01', kind='writer', lead=0.8, tail=1.5,
  narration=("Muse is a cloud AI agent. You give it a goal, and it works through the steps on its own computer in "
             "the cloud. That makes it useful for long, heavy jobs, like building 3D assets, that would otherwise "
             "tie up your own machine.")),
 dict(id='B02', kind='terms', terms=TERMS_A,
  cues=['An agent', 'A token', 'MCP'],
  narration=("Six terms first. An agent is AI software that takes a goal and carries out the steps, instead of "
             "just answering. A token is a small chunk of text; AI use is measured, and limited, in tokens. MCP, "
             "the Model Context Protocol, is a standard way to connect an AI to tools and data.")),
 dict(id='B03', kind='terms', terms=TERMS_B,
  cues=['Headless', 'An asset', 'a virtual machine'],
  narration=("Headless means a program runs with no window on screen. An asset is any file a game uses: a 3D "
             "model, a texture, a sound. And a virtual machine is a complete computer simulated in software, "
             "often in the cloud.")),
 dict(id='B04', kind='problem',
  cues=['A chatbot', 'Building a game', 'Install a tool', 'your own computer'],
  narration=("Here's the problem. A chatbot answers a question, and stops. Building a game or a 3D asset is "
             "different. It's long, multi-step work. Install a tool, write a script, run it, check the output, "
             "fix it, run it again. And while all that runs, your own computer is busy.")),
 dict(id='B05', kind='flow',
  cues=['give it a goal', 'makes a plan', 'checks in', 'Blender and Godot', 'a result'],
  narration=("Muse is a cloud AI agent. You give it a goal. It makes a plan, works through the steps, and checks "
             "in with you before anything consequential. Its tools are real programs, like Blender and Godot. "
             "What comes back is a result you can inspect.")),
 dict(id='B06', kind='versus',
  cues=['your own', 'its own virtual machine', 'none of your', 'around the clock', 'token allowance'],
  narration=("The big difference is where the work happens. A tool on your own computer uses your memory and "
             "disk. Muse runs on its own virtual machine in the cloud, so it uses none of your computer's memory or "
             "disk. And it keeps working around the clock, until its token allowance runs out.")),
 dict(id='B07', kind='muse_ui',
  cues=['the idea', 'state a goal', 'a plan', 'stops and asks'],
  narration=("Here's the idea, as an illustration. You state a goal. Muse lays out a plan. And before a "
             "consequential step, it stops and asks you first.")),
 dict(id='B08', kind='blender',
  cues=['Blender', 'headless', 'a script', '3D models'],
  narration=("Muse can install and run Blender, the free 3D tool. It can also run Blender headless, with no "
             "window at all, driven by a script. That's how it makes 3D models and art.")),
 dict(id='B09', kind='godot',
  cues=['Godot', 'game prototypes', 'Unity and Unreal'],
  narration=("It can run Godot too, the open-source game engine, and build simple game prototypes. Unity and "
             "Unreal may be possible as well.")),
 dict(id='B10', kind='compare',
  cues=['Claude Code', 'Muse works', 'not Sonnet or Opus', 'simpler tasks'],
  narration=("How does it compare with Claude Code? Claude Code works on your own machine and uses its resources. "
             "Muse works in the cloud. Muse's underlying AI model is not Sonnet or Opus, so it's best suited to "
             "simpler tasks.")),
 dict(id='B11', kind='uses',
  cues=['Offload', 'overnight', 'first-draft', 'pair it'],
  narration=("So how could you use it? Offload heavy jobs to the cloud. Run long tasks overnight. Get quick "
             "first-draft prototypes and assets, then refine them by hand. And pair it with other tools, for "
             "example Brutalist, for making videos.")),
 dict(id='B12', kind='cautions',
  cues=['verified', 'too much access', 'what the AI did'],
  narration=("Three cautions. AI output must be verified by a person. An agent that runs code can be risky if it "
             "has too much access, so give it only what the job needs. And say what the AI did. You should be "
             "able to explain every part of your work.")),
 dict(id='B14', kind='recap',
  cues=['Muse is', 'It can run', 'Use it'],
  narration=("Recap, in three lines. Muse is a cloud AI agent that works the steps on its own virtual machine. "
             "It can run Blender, even headless, and Godot, and make 3D models, prototypes and art. Use it for "
             "heavy, long or first-draft work, then refine and check it yourself.")),
 dict(id='B15', kind='handoff',
  narration=("Your turn. Paste this into Claude: I'm a game engineering student. Give me three small, low-risk "
             "tasks I could hand to a cloud AI agent: one in Blender, one in Godot, and one asset step. For each, "
             "tell me exactly how I'd check the result by hand. That last part is the point: if you can't say how "
             "you'd check it, don't hand it off. Liam, for Yeshwanth Balaji.")),
 dict(id='B16', kind='outro', tail=1.0, narration=f'{TITLE}. Yeshwanth Balaji, at Humanitarians AI.'),
]

COMPOSER = dict(greeting='Hi, Yeshwanth', topic='HUMANITARIANS AI · FELLOWS', segment='Meet Muse',
                command=("Explain Muse to a game engineering class that has never used an AI agent: what it is, "
                         "what it can do, and how they could use it."),
                runningText='an introduction for game engineers',
                output=['Muse: a cloud AI agent for games and 3D.', 'What it is · what it can do · how to use it.'],
                folderLabel='@HumanitariansAI', modelLabel='Opus 5.5', effortLabel='High')
WRITER = dict(text='Muse is a smarter chatbot.\nYou give it a goal.\nIt works.',
              triggerWords='a smarter chatbot', replacementWords='a cloud AI agent',
              fontSize=120, lineSpacing=1.4, charMs=30, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
              seed='claude-liam-meet-muse-2026-10', ink='#3D3929', accent='#D97757', bg='#FAF9F5',
              face='serif', align='center', brandLabel='@HumanitariansAI')
WRITER_916 = dict(WRITER, fontSize=150, lineSpacing=1.5)
RECAP = ['A cloud AI agent that works the steps on its own virtual machine.',
         'Runs Blender (even headless) and Godot; makes 3D models, prototypes, art.',
         'Use it for heavy, long or first-draft work; refine and check it yourself.']
HANDOFF = dict(greeting='Your turn.', topic='CLAUDE · YOUR TURN', segment='Three Safe First Tasks',
               command=("I'm a game engineering student. Give me three small, low-risk tasks I could hand to a cloud "
                        "AI agent: one in Blender, one in Godot, and one asset step. For each, tell me exactly how "
                        "I'd check the result by hand."),
               runningText='paste this into Claude…',
               output=["Look for: a way to check each task by hand.", "If you can't check it, don't hand it off."],
               folderLabel='@HumanitariansAI', modelLabel='Opus 5.5', effortLabel='High')
