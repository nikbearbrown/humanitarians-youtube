Open GPT-2 and you can count every one of its 124,439,808 weights. Nobody can read them yet. Part 2 of a look inside the black box.

Part 1 showed that a neural net is simple parts and that nobody writes its weights. Part 2 follows Stephen Wolfram's "What Is ChatGPT Doing … and Why Does It Work?" (2023) into trained nets, using his own figures.

Looking inside. In a net trained to tell cats from dogs, the first layer still shows things you can name: "the cat without its background", "the outline of the cat". By the tenth layer, Wolfram writes, "it's harder to interpret what's going on". The net picks out features, "maybe pointy ears", but mostly ones we have no names for.

GPT-2, opened. ChatGPT can't be downloaded, but GPT-2, the small model Wolfram uses for his examples, can. We read its weights file on a Mac:

- 12 attention blocks, with 12 heads in each
- 768 numbers per token, 50,257 tokens, 1,024 positions
- 124,439,808 weights in all

A forward pass written out in plain NumPy reproduces Wolfram's first figure exactly. After "The best thing about AI is its ability to", the next word is learn 4.5%, predict 3.5%, make 3.2%, understand 3.1%, do 2.9%.

Every weight, counted. N = Vd + Pd + L(12d² + 13d) + 2d. Each block holds 12d² + 13d = 7,087,872 weights: four d × d matrices for attention, two d × 4d matrices for the feed-forward layer, plus 13d of biases and layer-norm scales. With V = 50,257, P = 1,024, d = 768 and L = 12, the total is exactly 124,439,808, the same as the count from the file.

Still unread. Words become lists of numbers, and related words land near each other: alligator beside crocodile. GPT-2's attention heads each look back over the text in their own pattern. One 768 × 768 weight matrix looks like static; smoothed, some structure appears, and what it encodes, Wolfram writes, "is quite unknown". He calls ChatGPT's success a scientific discovery: an honest way of saying nobody has a theory for why it works.

Try it yourself: load the smallest GPT-2 (it's free and runs on a laptop), count its weights and plot one of its weight matrices. Then ask an assistant what that picture tells you about what the model knows, and what it can't tell you.

Chapters:
0:00 Part 2: opening a trained net
0:13 Looking inside a vision net
0:31 GPT-2, opened on this Mac
0:50 Every weight, counted
1:09 Inside GPT-2: embeddings, attention, weights
1:32 Verdict
1:48 Your turn: open one yourself
2:04 Outro

Sources:
Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?" (Feb 14, 2023) — https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/
GPT-2 (smallest), openai-community/gpt2 on Hugging Face — https://huggingface.co/openai-community/gpt2

Figures (all by Stephen Wolfram, from the essay above, © Stephen Wolfram, LLC, CC BY-NC-SA 4.0 — https://creativecommons.org/licenses/by-nc-sa/4.0/):
A cat in a trained net's first layer — https://content.wolfram.com/sites/43/2023/02/sw021423img56.png
The same cat at the tenth layer — https://content.wolfram.com/sites/43/2023/02/sw021423img57.png
Words laid out by an embedding — https://content.wolfram.com/sites/43/2023/02/sw021423img78.png
Attention patterns of GPT-2's 12 first-block heads — https://content.wolfram.com/sites/43/2023/02/sw021423img89A.png
A 768 × 768 weight matrix from GPT-2 — https://content.wolfram.com/sites/43/2023/02/sw021423img90A.png
The same matrix after 64 × 64 moving averages — https://content.wolfram.com/sites/43/2023/02/sw021423img91.png

License of this video: because it adapts CC BY-NC-SA 4.0 material, this video is released under CC BY-NC-SA 4.0 and is not monetized.

Hosted by Sai. Voice: Kokoro am_onyx, free and local, no account. AI-generated narration. Motion graphics were built with Remotion, and the equation was typeset locally as outlined SVG. Every GPT-2 number comes from a script run for this video: it reads openai-community/gpt2's model.safetensors with NumPy 1.24.4 on a MacBook Pro (M2 Pro) and counts the tensors. The total and the formula were checked against each other. The word map is Wolfram's embedding example, not GPT-2's own. Wolfram's figures are shown whole and scaled on a cream background; nothing was redrawn or generated. No human-performed audio or video in this production.

Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Stephen Wolfram, What Is ChatGPT Doing, ChatGPT, GPT-2, neural networks, black box, interpretability, how ChatGPT works, embeddings, word embeddings, attention heads, transformer, weight matrix, parameter count, LLM, AI explained, Humanitarians AI, Computational Skepticism, weekly

#AI #ChatGPT #GPT2 #NeuralNetworks #StephenWolfram #Interpretability #HumanitariansAI #ComputationalSkepticism
