> Production status: Deepa explicitly approved this complete planning packet in the conversation. Original draft-state labels below describe the earlier planning stage. Audio listening remains pending; see AUDIO-REVIEW.md.

# Fact-Check — Draft for Human Review

Automated research/arithmetic assessment only. Human approval: PENDING. Nothing here certifies a script, voice, visual, render or publication as approved.

Source IDs refer to SOURCES.md. The proposed script and on-screen copy are in SHOTLIST.md; proposed prompts are in PROMPTS.md.

| ID | Claim / planned occurrence | Assessment | Source or derivation | Required wording / limit |
|---|---|---|---|---|
| C1 | Accuracy counts correct classifications across all examples; B01–B03 | Supported | S2; matches S1 | Unweighted binary classification in this example |
| C2 | 99 ordinary emails and one spam email; B03 | Constructed assumption, not empirical fact | D1, approved topic brief | Spoken disclosure and persistent “Hypothetical teaching example” label |
| C3 | Always predicting ordinary gives 99 correct, one miss, 99% accuracy; B03/B06 | Independently computed | TN=99, FP=0, FN=1, TP=0; 99/100 × 100 | Applies to the specified constructed data only |
| C4 | Spam recall is the fraction of actual spam detected; B02/B05 | Supported | S3; spam is the positive class | TP/(TP+FN), not denominator of all emails |
| C5 | 99% accuracy can coexist with 0% spam recall; B01/B05/B06 | Supported and computed | D1: 0/(0+1) × 100 = 0; S1 contextual guidance | Counterexample to treating accuracy alone as spam-detection success; not evidence all high-accuracy models fail |
| C6 | Relevant evaluation depends on class counts, error types and task costs; B06 | Supported | S1 | Do not imply recall alone is sufficient |
| C7 | Viewer exercise should return denominators 100 and 1, scores 99% and 0%; B07 | Independently computed | Same D1 computation | Review the AI answer against these known counts |
| C8 | Deepa Shenoy is the credited volunteer; Liam narrates for Deepa; B00/B08 | User-supplied production identity | Conversation | AI voice is disclosed on screen; do not imply a human voice recording exists |

## Independent numerical verification

Executed locally as an inline Python calculation, without writing a script file, installing dependencies, training a model or generating media. Python 3.13.2; standard library only. Exit code 0, no stderr. No randomness. This is an arithmetic check of constructed inputs, not an experiment on real emails.

Exact code executed:

```python
import sys,json,hashlib
truth=[0]*99+[1]
pred=[0]*100
counts={'TN':sum(t==0 and p==0 for t,p in zip(truth,pred)),'FP':sum(t==0 and p==1 for t,p in zip(truth,pred)),'FN':sum(t==1 and p==0 for t,p in zip(truth,pred)),'TP':sum(t==1 and p==1 for t,p in zip(truth,pred))}
print(sys.version.split()[0])
print(json.dumps(counts,sort_keys=True))
print('accuracy_pct=',100*sum(t==p for t,p in zip(truth,pred))/len(truth))
print('spam_recall_pct=',100*counts['TP']/(counts['TP']+counts['FN']))
print('input_sha256=',hashlib.sha256(json.dumps({'truth':truth,'pred':pred},sort_keys=True,separators=(',',':')).encode()).hexdigest())
```

Observed stdout:

```text
3.13.2
{"FN": 1, "FP": 0, "TN": 99, "TP": 0}
accuracy_pct= 99.0
spam_recall_pct= 0.0
input_sha256= 33d8b266abc076cd9db9ebf2afd9a7cf6f5844fbb91765eead4b4c645cd4625b
```

Independent hand derivation: all 99 ordinary emails match the ordinary prediction; the one spam email does not. Thus 99 matches among 100 emails. No predicted spam means no true positives; the one actual spam is a false negative. Thus 0 caught among 1 actual spam email. The four confusion counts sum to 100.

## Pending checks

- Deepa's review of claim wording, example, script and branding.
- Recheck this ledger if any counts, labels, narration or prompts change.
- Later verify the rendered grid has exactly 100 items with exactly one spam item; predictions remain distinct from true labels.
- Later verify counters and equations match these results. Use structured mathematical layout for any fractions; inspect the actual output frames.
- Later verify every factual visual has its source or constructed-example attribution, and review audio pronunciation and pacing.
- No render, typography, audio, duration, native-4K or mobile-legibility check has yet been run.
