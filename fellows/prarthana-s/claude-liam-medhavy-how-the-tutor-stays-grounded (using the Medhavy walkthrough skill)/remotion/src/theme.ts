// Reel-local theme for "How the Tutor Stays Grounded in Your Textbook".
// Values mirror brutalist.art's Claude fidelity palette (runtime/remotion/src/tokens/claude.ts)
// so these local scenes sit beside the library bookends without a visual seam.
import { continueRender, delayRender, staticFile } from 'remotion';

export const C = {
  PAGE: '#FAF9F5',
  CARD: '#FFFFFF',
  BORDER: '#E5E2D9',
  FOOTER: '#F1EFE7',
  INK: '#3D3929',
  INK_SOFT: '#73705F',
  GHOST: '#A9A491',
  SPARK: '#D97757', // the one accent
} as const;

export const SERIF = '"EB Garamond", Georgia, serif';
export const SANS = '"Inter", "Helvetica Neue", Arial, sans-serif';

// Fonts come from the toolkit's runtime/fonts via the public/fonts symlink (read only).
let loaded = false;
export const loadFonts = () => {
  if (loaded || typeof document === 'undefined') return;
  loaded = true;
  const handle = delayRender('fonts');
  const faces = [
    new FontFace('EB Garamond', `url(${staticFile('fonts/EB_Garamond/static/EBGaramond-Regular.ttf')})`, { weight: '400' }),
    new FontFace('EB Garamond', `url(${staticFile('fonts/EB_Garamond/static/EBGaramond-Medium.ttf')})`, { weight: '500' }),
    new FontFace('Inter', `url(${staticFile('fonts/Inter/static/Inter_28pt-Regular.ttf')})`, { weight: '400' }),
    new FontFace('Inter', `url(${staticFile('fonts/Inter/static/Inter_28pt-Medium.ttf')})`, { weight: '500' }),
  ];
  Promise.all(faces.map((f) => f.load().then((ff) => document.fonts.add(ff))))
    .then(() => continueRender(handle))
    .catch(() => continueRender(handle));
};
