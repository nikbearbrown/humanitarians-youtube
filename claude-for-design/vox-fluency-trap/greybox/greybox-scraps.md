# Greybox scraps — Why the Group That Learned Less Was Sure It Learned More

One prompt per cutout/portrait. The leading 3-char id lands in Midjourney's output filename; drop the images into `greybox/scraps/` (keep the id in the filename) and re-run `greybox.py` — each image replaces its stand-in glyph.

Provenance lives in `scraps/sources.json` (`{"<id>": {"source": "generated|archive|user", "url": "..."}}`). A portrait of a real person whose image is generated or unsourced renders with an ink X (STAND-IN) and blocks final packaging — the X is removed by replacing the file, never by editing.

| id | kind | maps to | image | source | status |
|----|------|---------|-------|--------|--------|
| adD | element | B01 | — | — | todo |
| M4E | element | B02 | — | — | todo |
| HUc | element | B04 | — | — | todo |
| S6K | element | B05 | — | — | todo |
| HRV | element | B07 | — | — | todo |
| aTs | element | B12 | — | — | todo |
| ZPZ | element | B13 | — | — | todo |

## Prompts (paste-ready)

```
adD, TITLE — Why the group that learned less was sure it learned more, archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
M4E, PHOTO — engineers at terminals, archival, push-in, archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
HUc, FOOTAGE — clean code assembling itself, check mark, archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
S6K, QUOTE — the quiz question, highlighter on 'understand', archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
HRV, ANNOTATE — terracotta ring around the check mark, archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
aTs, PLATE+ANNOTATE — the break arrives; DUE stamp lands, archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
ZPZ, CARD — endcard — Let it type. Keep the checking., archival documentary photograph, desaturated, high contrast crushed blacks, aged newsprint grain, early 20th-century press-photo tone, clear margins, no modern objects --ar 4:3
```
