# Video Report: What Distributed Training Actually Looks Like

**Type:** STEM Educational Video
**Week:** Week 18, October 25 – 31, 2026

---

## Summary

This video explains how large AI models are trained across many GPUs. It shows what is actually being split between the GPUs, and where the time goes. The main takeaway is that the biggest limit is moving data between GPUs, not raw computing power.



## What the Video Covers

1. **Opening:** what usually gets left out when distributed training is explained.
2. **Why one GPU isn't enough:** how much memory a 7-billion-parameter model really needs.
3. **Copying the model:** each GPU gets a full copy and its own share of the data. The results are averaged after every step.
4. **Sharing results:** passing data around a ring of GPUs avoids the slowdown of sending everything to one place.
5. **Splitting the model:** a model can be split within each layer or by groups of layers. Splitting by layers creates idle time, which smaller batches help reduce.
6. **Putting it together:** real training uses all of these at once, and communication between machines is the main limit.
7. **Closing summary,** key takeaways, and a prompt for viewers to try.

## Main Ideas

- **The model itself is the small part.** For a 7B model, the weights take 28 GB. The optimizer and gradients bring the total to 112 GB, more than one 80 GB GPU can hold.
- **Copying the model is the easy option,** but the GPUs have to sync after every step.
- **The ring method keeps syncing fast,** because each GPU moves about the same amount of data however many GPUs there are.
- **Splitting the model makes room for bigger models,** at the cost of some idle time.
- **Real training balances three things:** computing power, memory and the speed of data transfer.



## Links

- **Video:**
  - GitHub: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-30-distributed-training-explainer
  - Drive: https://drive.google.com/drive/folders/1KzVPPTFcm3LRt-pdS2RzfmoMEkXQ6ofM

## Status

Complete