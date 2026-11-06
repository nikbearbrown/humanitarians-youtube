# Friction Log: Mixture of Experts — Sparse Activation, Massive Capacity
 
**Type:** STEM Educational Video

**Week:** Week 19, November 1 – 7, 2026
 
---
 
## 1. Date and focus
A video explaining Mixture of Experts (MoE). It covers:
- how MoE replaces one large feed-forward network with several experts and a router
- how only a fraction of the model runs for each word
## 2. What was tried, and what was expected
- **Numbers:** the numbers in the brief were expected to add up.
- **Router:** the brief named the chosen experts (3 and 7), and they were expected to be drawn as given.
- **Ending:** a fade to dark was expected to give a clean finish.
- **Narration:** kept as written, and expected to fit within 45 to 70 words per section.
## 3. Where things got stuck, and what was done next
- **8 × 22 is not 141:** a real model is labelled "8×22B (141B total)", but 8 × 22 = 176. The 141B is correct, because only the feed-forward parts are copied into experts and the rest is shared. The scene now shows both numbers and explains the gap.
- **Router:** the chosen experts are picked from routing probabilities instead of being drawn by hand.
- **Cost bars:** the MoE model and the standard model are drawn from the same value, because their cost per word is identical.
- **Expert limit:** the limit and the overflow are calculated from the load, not chosen to look right.
- **Ending:** the video now ends on the title card instead of an empty screen.
- **Length:** four of the five sections ran over 70 words. All were kept as written.
## 4. What Claude contributed, and what was kept or changed
- **Original work:** concept, brief and main narration.
- **Claude:** assembled the video using the video generation tool created by Humanitarians AI. Claude also wrote the opening, summary, viewer prompt and outro, drafted the pre-recording review, and spotted the 8 × 22 mismatch.
- **Accepted:** showing 176B next to 141B, the calculated figures, and the female voice.
- **Changed from the brief:** the model label, two added colors, and the ending.
- **Kept as written:** all narration.
## 5. What is understood now, and what is still open
**Understood:**
- The concepts in the video: how a router picks experts, why only a fraction of the model runs for each word, how load balancing and an expert limit keep the experts evenly used, and why MoE can match a larger standard model.  

**Open:**
- None
