# Script: Why a sepsis alarm in hundreds of hospitals learned to wait for the doctor

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "predicts sepsis before doctors notice", corrects to "fires after doctors already suspect".
**Narration**:
"When an AI early-warning system clears hospital validation with high accuracy, we assume it predicts sepsis before doctors notice. In reality, it learned to wait for the doctor. Let's see why."

## B01 — stakes (The Deployment)
**Visual**: Manim `B01Scene`. Hospital monitoring dashboard, "Proprietary Sepsis Model", 100+ Hospitals, time-to-treatment stakes.
**Narration**:
"A proprietary sepsis early-warning model was deployed across hundreds of hospitals. Sepsis is deadly and hours matter, so a machine learning model forecasting deterioration promised to save lives."

## B02 — stakes (The External Validation)
**Visual**: Manim `B02Scene`. Internal Validation (passed) vs External Validation (Wong et al., 2021). The disconnect revealed.
**Narration**:
"The model cleared internal testing with flying colors. But when independent researchers evaluated it across thousands of hospitalizations — Wong et al. in 2021 — it missed most sepsis cases and flooded wards with alerts."

## B03 — anchor planted (The Hospital Timeline)
**Visual**: Manim `B03Scene`. THE ANCHOR: Linear clinical timeline from admission to bedside care, showing vital checks, labs, and interventions.
**Narration**:
"To see why the metrics collapsed, look at the sequence of care. A patient is admitted. Over hours and days, doctors and nurses observe vital signs, notice subtle deterioration, and decide when to act."

## B04 — wrong guess (Independent Forecaster)
**Visual**: Manim `B04Scene`. Naive mental model: AI observes raw vitals and warns hours before any human clinician suspects.
**Narration**:
"The naive mental model assumes the AI acts as an independent forecaster, spotting hidden physiological signals in raw vitals hours before bedside clinicians notice anything wrong."

## B05 — break it (Looking Inside Features)
**Visual**: Manim `B05Scene`. Falsification: Peeling back the feature inputs. Vitals (temperature, pulse) vs Clinical Workflow Orders.
**Narration**:
"That assumption breaks when you examine what features the model was actually using. Alongside temperature and pulse, the algorithm drank in clinical workflow orders."

## B06 — mechanism (The Clinician's Action)
**Visual**: Manim `B06Scene`. Clinician suspicion forms at bedside -> immediate order: Diagnostic Blood Culture.
**Narration**:
"Here is how hospital medicine works. When an experienced physician suspects sepsis, their immediate next step is to order diagnostic lab work — specifically, a blood culture."

## B07 — mechanism: trace (The Trace in Data)
**Visual**: Manim `B07Scene`. MANIM MOVE `trace`: Blood-culture order timestamped into the patient record; model's feature vector traces the new entry and spikes risk score.
**Narration**:
"That order enters the digital record. The model's algorithm traces that sudden new event, recognizes a strong statistical correlation with sepsis, and its internal risk score spikes."

## B08 — anchor payoff (The Suspicion Loop)
**Visual**: Manim `B08Scene`. THE SUSPICION LOOP: Doctor suspects sepsis → orders blood culture → model reads order feature → model fires alert → alert lands back on the doctor.
**Narration**:
"The result is the suspicion loop. The doctor suspects sepsis, so the doctor orders blood cultures. The model sees the order, fires an urgent sepsis alert, and sends it straight back to the doctor who already suspected it."

## B09 — anchor payoff (Why Internal Metrics Passed)
**Visual**: Manim `B09Scene`. Automated scoring script: Alert timestamp matches Sepsis diagnosis → labeled "True Positive" with high accuracy.
**Narration**:
"To an automated scoring script, this looks like brilliant performance. The model alerted, and the patient indeed had sepsis. But the alert was downstream of the human judgment it claimed to anticipate."

## B10 — one flag (The Data-World Frame)
**Visual**: Manim `B10Scene`. THE ONE FLAG: The Data-World Boundary. Inside data frame: feature correlation. Outside data frame: clinical intent.
**Narration**:
"One flag — no machine learning model can detect this flaw from inside its own training data. The data contains the culture order, but not the clinical intent that created it."

## B11 — direction A (Accuracy ≠ Early Warning)
**Visual**: Manim `B11Scene`. HIGH PREDICTIVE ACCURACY ≠ EARLY WARNING LEAD TIME. Struck through with terracotta.
**Narration**:
"In one direction, high predictive accuracy in the training log is not proof of an early warning. A model that echoes human decisions can look mathematically perfect while offering zero forecasting lead time."

## B12 — direction B (Not a Math Bug)
**Visual**: Manim `B12Scene`. The statistical engine functioned as designed; the failure was epistemic framing.
**Narration**:
"In the other direction, the algorithm did not calculate incorrectly. It found the strongest statistical pattern in the data. The failure was mistaking a trace of clinician suspicion for an independent discovery."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"An early-warning model cannot warn you about an event if its strongest feature is the trace of you already reacting to it."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Audit a predictive model in your workflow. Which of its top input features are actually traces of human decisions responding to the outcome it claims to predict? Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"Why a sepsis alarm in hundreds of hospitals learned to wait for the doctor. Liam, in for Bear."
