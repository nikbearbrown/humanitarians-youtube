"""Portrait-only props for ai-content-vs-human-creativity/vertical (same meaning, fewer words per frame)."""
import json, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'beat_sheet.json')  # run after ./art vertical <reel>
d = json.load(open(P, encoding='utf8'))

OVR = {
    'B00': {'largeText': False},
    'B01': {'text': 'AI content\nbeats human\ncreativity.\nOne video\nmakes a\npost.', 'fontSize': 140},
    'B02': {'videoLabel': 'LONG-FORM VIDEO',
            'chapters': [{'label': 'Ideas', 'at': 0.31}, {'label': 'Stories', 'at': 0.365}, {'label': 'Voice', 'at': 0.415}],
            'moments': [{'label': 'Hook', 'pos': 0.167, 'at': 0.85}, {'label': 'Story', 'pos': 0.5, 'at': 0.89},
                        {'label': 'Tip', 'pos': 0.833, 'at': 0.93}],
            'jobLine': 'AI finds the moments. It doesn’t invent them.'},
    'B03': {'largeText': False},
    'B04': {'aiLine': 'AI trims, resizes and drafts captions.'},
    'B05': {'nodes': [{'label': 'Long Video', 'glyph': 'video', 'at': 0.02},
                      {'label': 'Transcript', 'glyph': 'lines', 'at': 0.11},
                      {'label': 'Blog Post', 'glyph': 'doc', 'at': 0.18},
                      {'label': 'Carousel', 'glyph': 'slides', 'at': 0.365}],
            'leaves': [{'label': 'Social Posts', 'glyph': 'bubble', 'at': 0.51},
                       {'label': 'Newsletter', 'glyph': 'mail', 'at': 0.59}],
            'weekLine': 'A whole week of content.'},
    'B06': {'rules': [{'k': 'SOUND', 'v': 'warm, plain', 'at': 0.29}, {'k': 'USE', 'v': 'you, we', 'at': 0.38},
                      {'k': 'NEVER', 'v': 'hacks, hype', 'at': 0.456}],
            'draftTitle': 'Draft post',
            'lines': ['Made from one video.', 'Guaranteed hack!'],
            'badIndex': 1, 'fixed': 'Try this one idea.', 'caption': 'Example — illustrative'},
    'B07': {'rows': [{'label': 'Speed', 'side': 'L', 'at': 0.085}, {'label': 'Volume', 'side': 'L', 'at': 0.115},
                     {'label': 'Format', 'side': 'L', 'at': 0.155}, {'label': 'Idea', 'side': 'R', 'at': 0.305},
                     {'label': 'Story', 'side': 'R', 'at': 0.38}, {'label': 'Final call', 'side': 'R', 'at': 0.422}],
            'leftNote': 'alone: sounds the same', 'rightNote': 'alone: too slow', 'verdict': 'The pair wins.'},
    'B08': {'artifactTitle': 'One page', 'artifactHeading': 'One video, many assets',
            'artifactLines': ['Start with a human original.', 'AI finds moments, cuts clips.',
                              'One transcript, many formats.', 'A voice guide keeps it on-brand.',
                              'A person makes the final call.'],
            'textScale': 2.35, 'largeText': False},
    'B09': {'largeText': False},
    'B10': {'title': 'AI Content vs.\nHuman Creativity:\nWhat Works Better?', 'scale': 0.8},
}
for b in d['beats']:
    o = OVR.get(b['beat_id'])
    if o:
        b['shot']['remotion']['props'].update(o)
    print(b['beat_id'], b['shot']['remotion']['pattern'])
json.dump(d, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=2)
