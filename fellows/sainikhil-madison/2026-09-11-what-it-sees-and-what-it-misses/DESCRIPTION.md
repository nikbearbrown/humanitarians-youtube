Does the first LoonNet work? Wrong question — seven failures on one sheet are not seven copies of one problem.

This weekly progress reel walks through the first iteration of LoonNet, a loon detector trained on 106 images and tested against 26 it had never seen. Instead of opening the metrics, it opens the prediction sheet and goes frame by frame. Nineteen of the twenty-six frames came back clean — the bird found once, boxed, nothing invented. The seven that failed split into four distinct causes: one bird counted three times by overlapping boxes, a reed bed boxed as a loon, a duck beside it called a loon at 0.3 confidence, and two loons in fog where the model returned nothing at all. The reel refuses to average those into a single score, because they do not share a fix.

The takeaway: double-counting is not a data problem. It is a threshold — one setting governing how hard overlapping boxes get merged — and more images will not touch it. The fog frame and the reed bed are data problems. Pull both levers at once and you learn nothing about either. One more line that matters: these are hand counts read off the validation sheets, not a validation run. Real precision and recall come from the model, before the team meeting. The reel also orders seven proposed application features by effort against impact — detection, counting, blurring, the acoustic classifier, then the three habitat models that need data nobody has collected yet — and takes one item off the list entirely: we already annotate in CVAT, so we should not be building an annotation tool of our own.

Try it yourself: if you have a first detector of your own, don't open the metrics. Open the prediction sheet and sort every mistake into piles by cause — not by how bad it looked. Then count the piles. That number is how many problems you actually have, and it is almost never one.

Chapters:
0:00 A hundred and six images, twenty-six held back
0:14 The set — four capture paths, two classes
0:31 What came back — 0.3 at the low end, 0.9 at the high
0:48 Nineteen clean, seven not
1:04 Four frames, four different failures
1:21 Threshold or data — which lever first
1:37 Seven features, in the order I'd build them
1:59 Verdict — a hand audit, not a validation run
2:17 Your turn

Hosted by Sai. Voice: Kokoro am_onyx — free, local, no account. AI-generated narration. Motion graphics built with Remotion. The prediction sheets on screen are the project's own YOLO validation output, composed unmodified — no bounding box, label or confidence value was redrawn, retouched or repositioned. No human-performed audio or video in this production.

Humanitarians AI — https://humanitarians.ai
Musinique — https://musinique.com
Medhavy AI — https://medhavy.com

#AI #ComputerVision #ObjectDetection #YOLO #ConservationAI #WildlifeAI #HumanitariansAI #WeeklyUpdate

TAGS

loon detection, LoonNet, National Loon Center, conservation AI, wildlife detection, object detection, YOLO, computer vision, false positives, duplicate detections, non-maximum suppression, model evaluation, validation set, drone imagery, aerial imagery, small object detection, dataset curation, CVAT, annotation, prediction sheet review, error analysis, first iteration model, Humanitarians AI, weekly progress

HASHTAGS

#AI #ComputerVision #ObjectDetection #YOLO #ConservationAI #WildlifeAI #HumanitariansAI #WeeklyUpdate
