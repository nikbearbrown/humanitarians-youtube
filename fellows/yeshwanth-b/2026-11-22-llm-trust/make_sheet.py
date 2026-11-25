"""Builds beat_sheet.json for claude-hai-llm-trust (ai-explainer, claude-hai: Yeshwanth Balaji, @HumanitariansAI).

    python3 make_sheet.py author    # narration + shots (before Kokoro)
    python3 make_sheet.py finish    # after Kokoro: pad audio, set durations, place cues on the spoken phrases

Cue times are placed proportionally to each phrase's position in the narration over the measured
speech, after the beat's lead silence. Evidence (all run locally, see evidence/):
  B05  evidence/overlap.json   real ROUGE-1 scores of the two Everest answers
  B08  evidence/embed.json     real all-MiniLM-L6-v2 embeddings, PCA to 2-D, cosine similarities
  B02  evidence/boiling.txt    Antoine-equation check of the Everest boiling point (~72 °C)
"""
import json
import math
import subprocess
import sys
from pathlib import Path

REEL = Path(__file__).resolve().parent
SLUG = 'claude-hai-llm-trust'
TITLE = 'Can You Trust Your AI? How We Test Large Language Models'
FPS = 30
HANDLE = '@HumanitariansAI'
LOGO = 'hai-wordmark-outlined.svg'
KICKER = 'Irreducibly Human'
BRAND = dict(handle=HANDLE, logo=LOGO)
PAPER = 'Brown, “Enhancing Trust in LLMs”, arXiv 2406.01943'

OVER = json.loads((REEL / 'evidence/overlap.json').read_text())
EMB = json.loads((REEL / 'evidence/embed.json').read_text())

BEATS = [
 dict(id='B00', act='ASK', pattern='ClaudeComposerAsk',
  narration=("Ciao, this is Yeshwanth Balaji. AI can write an answer that sounds perfect and is completely wrong. "
             "So how do engineers decide whether a model can be trusted? Let's open the toolbox researchers use to test it."),
  props=dict(greeting='Ciao, Yeshwanth', topic=KICKER, segment='Can You Trust Your AI?',
             command='How do researchers decide whether a large language model can be trusted?',
             runningText='answer drawn from a survey paper · illustrative',
             output=['Measure it: score answers, run benchmarks, test for bias.',
                     'Look inside it: embeddings, attention, explanations.',
                     'Keep people in the loop: human evaluation.'],
             folderLabel=HANDLE, modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B01', act='BLUF', pattern='BrutalistHesitantWriter', lead=0.8, tail=1.5,
  narration=("Trusting an AI isn't a feeling. It's something you measure: with scores, with bias tests, by looking "
             "inside the model, and by asking people. Each one catches something the others miss."),
  props=dict(text="Trusting an AI\nis a feeling.\nEngineers test it four ways,\nand people check the rest.",
             triggerWords='is a feeling', replacementWords='is something you measure',
             fontSize=92, lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
             seed='llm-trust-2026-11', ink='#3D3929', accent='#D97757', bg='#FAF9F5', face='serif',
             align='center', brandLabel=HANDLE)),
 dict(id='B02', act='BODY', pattern='TrustHallucination', tail=0.8,
  narration=("Start with the problem. Ask a model what temperature water boils at on top of Mount Everest. "
             "It answers: one hundred degrees, the same as at sea level. Fluent, confident, and wrong. "
             "Up there the air is thinner, so water boils at about seventy. A confident answer that isn't true "
             "is called a hallucination."),
  props=dict(question='What temperature does water boil at on top of Mount Everest?',
             answer='Water boils at 100 °C up there, the same as at sea level.',
             truth='About 70 °C: thinner air, lower boiling point.',
             note='Illustrative answer, not from a specific model · boiling point checked: evidence/boiling.txt', noteShort='Illustrative answer'),
  cues=['Ask a model', 'It answers', 'and wrong', 'Up there']),
 dict(id='B03', act='BODY', pattern='TrustThreeProblems', tail=0.8,
  narration=("Hallucination is one of three reasons we can't take an output on faith. Bias: models can learn unfair "
             "patterns from their training data. And the black box: billions of numbers, and no easy way to see why "
             "the model said what it said. You wouldn't hire someone because they sound confident. You'd check their work."),
  props=dict(title='Three Reasons to Check', analogy='Confidence isn’t evidence. Check the work.', items=[
      {'label': 'Hallucination', 'detail': 'confident answers that aren’t true', 'icon': 'hallucination'},
      {'label': 'Bias', 'detail': 'unfair patterns learned from data', 'icon': 'bias'},
      {'label': 'Black box', 'detail': 'no easy way to see why', 'icon': 'blackbox'}]),
  cues=['Hallucination is one', 'Bias', 'And the black box', "You wouldn't hire"]),
 dict(id='B04', act='BODY', pattern='TrustToolbox', tail=0.8,
  narration=("So how do you check the work? Researchers use a toolbox. Metrics that score answers against reference "
             "answers. Benchmarks: one test for every model. Head-to-head comparisons. Bias tests. Ways to look inside "
             "the model. And human review. Nik Bear Brown's survey paper collects most of these. Let's open them."),
  props=dict(title='The Evaluation Toolbox',
             footnote='Five of the six are covered in the survey; head-to-head A/B testing is common industry practice.',
             tools=[{'label': 'Metrics', 'detail': 'score against reference answers'},
                    {'label': 'Benchmarks', 'detail': 'the same test for every model'},
                    {'label': 'A/B tests', 'detail': 'two versions, same prompts'},
                    {'label': 'Bias tests', 'detail': 'change one detail, compare'},
                    {'label': 'Interpretability', 'detail': 'look inside the model'},
                    {'label': 'Human review', 'detail': 'people judge what scores miss'}]),
  cues=['Metrics that score', 'Benchmarks', 'Head-to-head', 'Bias tests', 'Ways to look', 'And human review',
        "Nik Bear Brown's"]),
 dict(id='B05', act='BODY', pattern='TrustOverlap', tail=1.0,
  narration=("First, metrics. Scores like BLEU and ROUGE count the words an answer shares with a reference answer. "
             "Here's a real calculation. The wrong answer, one hundred degrees, scores zero point eight seven. "
             "A correct answer in different words scores zero point two five. The score measured overlap, not truth. "
             "The survey notes these metrics often track human judgment poorly."),
  props=dict(title='Scoring Against a Reference', metric='ROUGE-1 · shared words',
             reference=OVER['reference_tokens'],
             rows=[dict(label='The wrong answer', tokens=OVER['results']['wrong']['tokens'],
                        matched=OVER['results']['wrong']['matched'], score=OVER['results']['wrong']['f1'], verdict='wrong'),
                   dict(label='A right answer, other words', tokens=OVER['results']['right']['tokens'],
                        matched=OVER['results']['right']['matched'], score=OVER['results']['right']['f1'], verdict='right')],
             lesson='It measured overlap, not truth.',
             quote='these metrics have been found to have low correlation with human judgment',
             quoteSource=f'{PAPER}, §5',
             note='Real scores, computed locally: evidence/overlap.py'),
  cues=['count the words', 'The wrong answer', 'scores zero point eight', 'A correct answer', 'scores zero point two',
        'The score measured']),
 dict(id='B06', act='BODY', pattern='TrustBenchAB', tail=1.0,
  narration=("Benchmarks solve a different problem: comparing models fairly. Every model takes the same test, scored "
             "the same way, and a leaderboard ranks them. A-B testing does the same for two versions of one model: "
             "same prompts, side by side, and you count which answers people prefer. But the survey warns that chasing "
             "a leaderboard can mean over-optimizing for the test. One score never tells the whole story."),
  props=dict(title='Same Test, Fair Comparison',
             quote='over-optimization for specific benchmarks', quoteSource=f'{PAPER}, §13',
             note='Illustrative bars and choices · no real models or scores', noteShort='Illustrative'),
  cues=['comparing models fairly', 'Every model takes', 'a leaderboard', 'A-B testing', 'you count', 'But the survey']),
 dict(id='B07', act='BODY', pattern='TrustCounterfactual', tail=1.0,
  narration=("Now fairness. One simple test: keep the prompt the same, and swap one sensitive detail, like a name, a "
             "gender, or a region. Write a reference letter for Emily, a nurse. Then the same request for Jamal. "
             "Compare the two answers. If the quality shifts with who it's about, that's a bias signal. The survey "
             "calls this a counterfactual: change one thing, and watch the output."),
  props=dict(title='Swap One Detail', names=['Emily', 'Jamal'],
             checks=[{'label': 'Length', 'a': 'about the same', 'b': 'about the same', 'same': True},
                     {'label': 'Skills named', 'a': 'clinical skill, leadership', 'b': 'punctual, friendly', 'same': False},
                     {'label': 'Tone', 'a': 'warm', 'b': 'warm', 'same': True}],
             verdict='Same request, different quality: a bias signal.',
             source='counterfactuals · survey §21',
             note='Illustrative comparison: how the test works, not a real model’s output', noteShort='Illustrative'),
  cues=['keep the prompt the same', 'Then the same request', 'Compare the two', 'If the quality', 'The survey calls']),
 dict(id='B08', act='BODY', pattern='TrustEmbedding', tail=1.0,
  narration=("Next, looking inside. A model turns words into points in a space with hundreds of dimensions. These are "
             "called embeddings. This is a real one: a small open model, sixteen words, flattened to two dimensions. "
             "Similar ideas cluster: animals, fruit, sports, music. Add kitten, and it lands next to cat. Engineers "
             "use maps like this to check what a model has grouped together, and what it shouldn't have."),
  props=dict(title='Words as Points in Space', points=EMB['points'],
             labelSide={'kitten': 'below', 'cat': 'left', 'dog': 'right', 'rabbit': 'above', 'horse': 'right', 'football': 'above', 'soccer': 'right', 'basketball': 'left', 'tennis': 'left', 'banana': 'left', 'mango': 'below', 'apple': 'right', 'cherry': 'below', 'guitar': 'left', 'violin': 'right', 'piano': 'above', 'drums': 'right'},
             groupLabels={'animals': 'animals', 'fruit': 'fruit', 'sports': 'sports', 'music': 'music'},
             query=EMB['query'], neighbour=EMB['nearest_to_query'][0], far=next(x for x in EMB['farthest_from_query'] if x['word'] == 'guitar'),
             note='Real embeddings · all-MiniLM-L6-v2 run locally · 384 dims → 2 (PCA)', noteShort='Real model, run locally'),
  cues=['This is a real one', 'Similar ideas cluster', 'Add kitten', 'it lands next to cat']),
 dict(id='B09', act='BODY', pattern='TrustReasoning', tail=1.0,
  narration=("Another way in: ask the model to explain its reasoning. Back on Everest, the explanation shows the faulty "
             "step. It assumed water always boils at one hundred degrees. Now you can see where it went wrong, and "
             "fix it. That turns the black box into a glass box, at least partly. One caution from the survey: an "
             "explanation isn't proof. What a model attends to isn't always what caused its answer."),
  props=dict(title='Ask It to Show Its Work', steps=[
      {'text': 'The question is about Mount Everest.'},
      {'text': 'Water always boils at 100 °C.', 'bad': True, 'fix': 'Thinner air lowers the boiling point.'},
      {'text': 'So it boils at 100 °C on the summit.', 'bad': True, 'fix': 'So about 70 °C on the summit.'}],
             glassLabel='black box → glass box',
             quote='High attention does not always equate to causal importance', quoteSource=f'{PAPER}, §20',
             note='Illustrative explanation', noteShort='Illustrative'),
  cues=['ask the model to explain', 'Back on Everest', 'the faulty', 'It assumed', 'That turns the black box', 'One caution']),
 dict(id='B10', act='BODY', pattern='AgentFitSort', tail=1.0,
  narration=("So why do people still matter? Metrics are good at overlap with a reference, and at running the same "
             "test thousands of times. But they miss tone, context, and subtle errors. People judge whether an answer "
             "is coherent, helpful, and fits the real situation. The survey calls human evaluation indispensable. "
             "The strongest evaluations combine both."),
  props=dict(title='What Scores Catch, What People Catch', leftLabel='Metrics can check', rightLabel='Needs a person',
             tasks=[{'text': 'Overlap with a reference', 'why': 'fast and repeatable', 'side': 'left'},
                    {'text': 'The same test, thousands of times', 'why': 'consistent at scale', 'side': 'left'},
                    {'text': 'Tone and context', 'why': 'does it fit the situation?', 'side': 'right'},
                    {'text': 'Subtle errors', 'why': 'right words, wrong meaning', 'side': 'right'},
                    {'text': 'Helpful in the real world', 'why': 'would someone act on it?', 'side': 'right'}],
             **BRAND),
  cues=['Metrics are good', 'running the same', 'they miss tone', 'subtle errors', 'fits the real']),
 dict(id='B11', act='BODY', pattern='AgentChecklist', tail=1.0,
  narration=("Here's your checklist before you trust an AI answer. One: can I verify this from another source? Two: "
             "would the answer change if I reworded the question? Three: is it explaining its reasoning, and does that "
             "reasoning hold up? Four: is this a high-stakes decision that needs a human check?"),
  props=dict(title='Your Trust Checklist', tone='practice', items=[
      {'label': 'Can I verify it?', 'detail': 'from another, independent source', 'mark': '1'},
      {'label': 'Does rewording change it?', 'detail': 'ask the same question another way', 'mark': '2'},
      {'label': 'Does the reasoning hold?', 'detail': 'read the steps, not just the answer', 'mark': '3'},
      {'label': 'Are the stakes high?', 'detail': 'then a person checks it', 'mark': '4'}], **BRAND),
  cues=['One:', 'Two:', 'Three:', 'Four:']),
 dict(id='B12', act='BODY', pattern='TrustCredit', tail=1.0,
  narration=("This video follows Enhancing Trust in LLMs, by Nik Bear Brown. It's a survey of evaluation techniques, "
             "so it reports no experiments of its own. The examples here are ours, built to show how each one works."),
  props=dict(kicker='Based on', paper='Enhancing Trust in LLMs: Algorithms for Comparing and Interpreting LLMs',
             author='Nik Bear Brown', id='arXiv 2406.01943 · June 2024',
             kind='A survey of evaluation techniques. The examples in this video are ours.'),
  cues=['This video follows', 'by Nik Bear Brown', "It's a survey", 'The examples']),
 dict(id='B13', act='VERDICT', pattern='ClaudeVerdictArtifact',
  narration=("Recap. Trust in AI isn't a feeling. It's measured: with performance metrics, bias tests, "
             "interpretability, and human review. Each one catches what the others miss."),
  props=dict(artifactTitle='Recap', artifactHeading='Trust is measured, not felt', brandLabel=HANDLE,
             artifactLines=['Metrics and benchmarks: how often it’s right.',
                            'Bias tests: whether it’s fair.',
                            'Interpretability: why it said what it said.',
                            'Human review: what the scores miss.'])),
 dict(id='B14', act='HANDOFF', pattern='ClaudeComposerAsk',
  narration=("Your turn. Paste this into Claude: Here's an answer an AI gave me. Before I rely on it, list every factual "
             "claim it makes, tell me how I could check each one against an independent source, give me two "
             "rewordings of my original question to test whether the answer holds, and tell me whether this decision "
             "needs a human expert. Watch the list of claims: the ones with no source to check against are where you "
             "start. The smarter AI gets, the more it matters to test it. Don't just ask whether an answer sounds "
             "right. Ask how you'd know."),
  props=dict(greeting='Your turn.', topic=KICKER, segment='Check One Answer',
             command=("Here's an answer an AI gave me: [paste it]. Before I rely on it, list every factual claim it makes, "
                      "tell me how I could check each one against an independent source, give me two rewordings of my "
                      "original question to test whether the answer holds, and tell me whether this decision needs a "
                      "human expert."),
             runningText='paste this into Claude…',
             output=['Look for: claims with no source to check against.',
                     'Look for: whether the rewordings change the answer.'],
             folderLabel=HANDLE, modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B15', act='OUTRO', pattern='ChannelTitleOutro', tail=1.0,
  narration=f'{TITLE} Humanitarians AI.',
  props=dict(title=TITLE, handle=HANDLE, logo=LOGO)),
]

SHOW = {
 'B00': 'Claude composer types the question; three answer lines summarize the survey (labelled illustrative)',
 'B01': 'hesitant writer types the overview and corrects "is a feeling" → "is something you measure"',
 'B02': 'question bubble; the confident wrong answer types; red HALLUCINATION stamp slams on; the true value lands',
 'B03': 'three icon cards light on their spoken names (hallucination, bias, black box); the hiring analogy line',
 'B04': 'six toolbox tiles light in the spoken order; the survey credit and the A/B footnote',
 'B05': 'reference words; the wrong answer\'s shared words fill in ink and its bar runs to 0.87; the right answer\'s to 0.25; lesson + §5 quote',
 'B06': 'benchmark panel: same test, three model bars grow and rank; A/B panel: prompts get A or B votes; §13 warning quote',
 'B07': 'prompt with the name slot; Emily → Jamal swap; two letter cards; comparison rows tick or flag; verdict line',
 'B08': 'sixteen real embedding points fly in; cluster outlines and labels; kitten appears and links to cat; similarity cards',
 'B09': 'three reasoning steps; the faulty steps flagged and corrected; the black cube turns to glass; §20 caution quote',
 'B10': 'five chips sort into "Metrics can check" and "Needs a person" on the spoken words',
 'B11': 'four numbered checklist cards land on "One / Two / Three / Four"',
 'B12': 'credit card: paper title, Nik Bear Brown, arXiv 2406.01943, "the examples are ours"',
 'B13': 'recap artifact page: the four ways trust is measured',
 'B14': 'Your Turn composer types the suggested prompt',
 'B15': 'title-restate outro with the Humanitarians AI wordmark and @HumanitariansAI',
}

QC_WRITER = {'sparse_by_design': True, 'sparse_reason': ('Hesitant writer: the overview is typed over the narration, so '
             'mid-beat samples legitimately show a partial page. The finished text holds for the last 1.5 s.')}

NEW_SCENES = {'TrustHallucination', 'TrustThreeProblems', 'TrustToolbox', 'TrustOverlap', 'TrustBenchAB',
              'TrustCounterfactual', 'TrustEmbedding', 'TrustReasoning', 'TrustCredit'}


def probe(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(path)],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def author():
    beats = []
    for spec in BEATS:
        props = dict(spec['props'])
        if spec['pattern'] in NEW_SCENES:
            props.update(BRAND)
        b = {'beat_id': spec['id'], 'act': spec['act'], 'narration_text': spec['narration'],
             'voice': 'am_onyx', 'engine': 'kokoro',
             'estimated_duration_s': round(len(spec['narration'].split()) / 2.6, 1),
             'shot': {'type': 'GRAPHIC', 'source': 'remotion',
                      'remotion': {'pattern': spec['pattern'], 'props': props},
                      'show': [{'at': 0.0, 'event': SHOW[spec['id']]}]}}
        if spec['pattern'] == 'BrutalistHesitantWriter':
            b['qc'] = QC_WRITER
        if spec['act'] == 'OUTRO':
            b['kind'] = 'outro_voice'
            b['tail_silence_s'] = 1.0
        if spec.get('lead'):
            b['lead_silence_s'] = spec['lead']
        beats.append(b)
    sheet = {'metadata': {
        'slug': SLUG, 'title': TITLE, 'topic': KICKER, 'skill': 'ai-explainer',
        'channel': 'claude-hai', 'brand': 'claude-hai', 'persona': 'Yeshwanth Balaji', 'in_for_bear': False,
        'voice': 'am_onyx', 'voice_kokoro': 'am_onyx', 'speed': 0.95, 'engine': 'kokoro', 'palette': 'claude',
        'register': 'Plain', 'fps': FPS, 'width': 3840, 'height': 2160, 'aspect_ratio': '16:9', 'fit': 'crop',
        'captions': False, 'caption_policy': 'none', 'greeting_language': 'Italian (Ciao)',
        'pronounce': {'Yeshwanth': 'jˈɛʃwənθ', 'Balaji': 'bəlˈɑːʤi'},
        'audience': 'students and early-career engineers who use AI tools daily but have never thought about how they are evaluated',
        'source': 'Nik Bear Brown, "Enhancing Trust in LLMs: Algorithms for Comparing and Interpreting LLMs", arXiv 2406.01943 (v1, 4 Jun 2024)',
        'note': ('ai-explainer film from a supplied script, fact-checked against the paper. B05 and B08 show real '
                 'computations (evidence/); B02, B06, B07 and B09 are labelled illustrative. No paid calls, no upload.'),
        'tags': ['LLM evaluation', 'hallucination', 'bias', 'interpretability', 'embeddings', 'human evaluation', 'Kokoro'],
    }, 'beats': beats}
    (REEL / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print(f'authored {len(beats)} beats, {sum(len(b["narration_text"].split()) for b in beats)} words')


def place(narration, phrase, lead, speech):
    pos = narration.find(phrase)
    if pos < 0:
        raise SystemExit(f'cue phrase not in narration: {phrase!r}')
    return round(lead + speech * pos / len(narration), 2)


def pad(src, out, lead, total):
    ms = int(round(lead * 1000))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(src), '-af',
                    f'adelay={ms}|{ms},apad,atrim=0:{total:.6f}', '-ar', '48000', '-ac', '2',
                    '-c:a', 'pcm_s16le', str(out)], check=True)


def finish():
    sheet_path = REEL / 'beat_sheet.json'
    sheet = json.loads(sheet_path.read_text())
    specs = {s['id']: s for s in BEATS}
    (REEL / 'audio').mkdir(exist_ok=True)
    for b in sheet['beats']:
        spec = specs[b['beat_id']]
        mp3 = REEL / f"mp3/beat-{b['beat_id']}.mp3"
        speech = probe(mp3)
        lead = spec.get('lead', 0.0)
        total = math.ceil((lead + speech + spec.get('tail', 0.0) + (0.4 if spec['act'] == 'VERDICT' else 0.3)) * FPS) / FPS
        pad(mp3, REEL / f"audio/beat-{b['beat_id']}.wav", lead, total)
        b['kokoro_audio_file'] = f"mp3/beat-{b['beat_id']}.mp3"
        b['kokoro_duration_s'] = round(speech, 3)
        b['audio_file'] = f"audio/beat-{b['beat_id']}.wav"
        b['actual_duration_s'] = total
        props = b['shot']['remotion']['props']
        props['durationSeconds'] = total
        if 'cues' in spec:
            props['cues'] = [place(spec['narration'], ph, lead, speech) for ph in spec['cues']]
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    for b in sheet['beats']:
        print(f"{b['beat_id']:4} {b['act']:8} {b['actual_duration_s']:7.2f}s  speech {b['kokoro_duration_s']:6.2f}s")
    print('total', round(sum(b['actual_duration_s'] for b in sheet['beats']), 1), 's')


if __name__ == '__main__':
    {'author': author, 'finish': finish}[sys.argv[1]]()
