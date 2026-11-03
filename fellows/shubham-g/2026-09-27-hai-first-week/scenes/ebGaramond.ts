// ebGaramond.ts — load the bundled EB Garamond (the effective Claude serif, see
// tokens/claude.ts) from public/fonts so every composition renders the house
// face without relying on an OS font install. Headless Chrome on Windows does
// not see per-user fonts, and a machine without the font silently falls back
// to Georgia. Imported once for its side effect by Root.tsx.
import {continueRender, delayRender, staticFile} from 'remotion';

const FACES: Array<[file: string, weight: string, style: string]> = [
  ['EBGaramond-Regular.ttf', '400', 'normal'],
  ['EBGaramond-Medium.ttf', '500 900', 'normal'],
  ['EBGaramond-Italic.ttf', '400 900', 'italic'],
];

if (typeof document !== 'undefined' && typeof FontFace !== 'undefined') {
  const handle = delayRender('Loading EB Garamond');
  Promise.all(
    FACES.map(([file, weight, style]) =>
      new FontFace('EB Garamond', `url(${staticFile(`fonts/${file}`)}) format('truetype')`, {weight, style})
        .load()
        .then((face) => document.fonts.add(face)),
    ),
  )
    .catch((err) => console.warn('[ebGaramond] font load failed, falling back:', err))
    .finally(() => continueRender(handle));
}
