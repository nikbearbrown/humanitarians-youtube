import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, Stage, clamp, ease, remap, useGeo, useP } from './ReelKit';

/**
 * BlipCapFilt — the WORKED EXAMPLE beat: CapFilt run on one web image, then on a cohort.
 *
 * Two scales in one frame, because either alone would be weaker evidence:
 *   LEFT  — one image, its junk alt-text, and the caption the captioner writes instead.
 *           The filter's verdict lands on BOTH texts, which is the paper's actual
 *           design (it filters the web texts and the synthetic ones). This half is
 *           ILLUSTRATIVE and says so on screen, per DOUBLE-CHECK LAW: the mechanism is
 *           the paper's, the strings are not a paper figure.
 *   RIGHT — the published rate. The filter rejects 25% of what a nucleus-sampling
 *           captioner writes (BLIP Table 2). The tiles ARE that number: 5 of 20 struck.
 *
 * The image is DRAWN (REBUILD LAW) — never a lifted photo. The beat's ONE terracotta
 * moment is rejection: the struck tiles, the REJECT tag, the rate.
 *
 * Responsive: the two halves sit side by side on 16:9 and stack on 9:16. Panel sizes
 * come from `safe`, never from px numbers tuned by eye (the ReelKit corollary).
 */
export const blipCapFiltSchema = z.object({
  spark: z.string().default('Write it, then judge it.'),
  heading: z.string().default('CapFilt, on one image'),
  /** the junk web alt-text — illustrative */
  webText: z.string().default('IMG_2043 · 1200x800 · stock photo'),
  /** what the captioner writes instead — illustrative */
  synthText: z.string().default('a dog running on the beach near the water'),
  webVerdict: z.string().default('REJECT'),
  synthVerdict: z.string().default('KEEP'),
  illustrativeNote: z.string().default('Illustrative: the mechanism is the paper’s, the strings are not a paper figure.'),
  rateLabel: z.string().default('noise ratio'),
  ratePct: z.number().default(25),
  rateNote: z.string().default('the share the filter throws out'),
  tiles: z.number().default(20),
  closing: z.string().default(''),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(13),
});
export type BlipCapFiltProps = z.infer<typeof blipCapFiltSchema>;

/**
 * WebImageGlyph — a drawn stand-in for a web image (REBUILD LAW: the reel never lifts
 * a photo). Fills are chosen for spread, not prettiness: GATE V flags a region whose
 * luminance sits within 0.30 of the cream stage, so the dark headland and the ink dog
 * carry the contrast the pale sky cannot.
 */
const WebImageGlyph: React.FC<{ w: number; h: number }> = ({ w, h }) => (
  <svg width={w} height={h} viewBox="0 0 100 100" preserveAspectRatio="none" style={{ display: 'block', borderRadius: 8 }}>
    <rect x={0} y={0} width={100} height={100} fill="#CFC6AE" />
    {/* sea, then wet sand, then dry sand */}
    <rect x={0} y={46} width={100} height={20} fill="#9E9B86" />
    {/* wave strokes: the caption says "near the water", so the water has to read as
        water. Same family as the sea fill — a cool hue would break the warm palette. */}
    <g stroke="#BAB6A2" strokeWidth={1.1} strokeLinecap="round" fill="none">
      <path d="M 8 52 q 5 -2 10 0 t 10 0" />
      <path d="M 62 55 q 5 -2 10 0 t 10 0" />
      <path d="M 30 60 q 5 -2 10 0 t 10 0" />
    </g>
    <rect x={0} y={66} width={100} height={9} fill="#A8A088" />
    <rect x={0} y={75} width={100} height={25} fill="#B0A488" />
    {/* headland — the dark mass that gives the frame its contrast spread */}
    <path d="M 0 46 L 0 34 L 16 28 L 31 40 L 40 46 Z" fill="#847860" />
    <circle cx={80} cy={20} r={7} fill="#E4DCC4" />
    {/* the dog — the subject the synthetic caption names */}
    <g fill={CLAUDE.INK}>
      <ellipse cx={58} cy={80} rx={9} ry={4.4} />
      <circle cx={67} cy={75} r={3.6} />
      <path d="M 69 71 l 3 -4 l 1.4 4 z" />
      <rect x={51} y={83} width={2.2} height={7} />
      <rect x={56} y={83} width={2.2} height={7} />
      <rect x={61} y={83} width={2.2} height={7} />
      <rect x={64.5} y={83} width={2.2} height={7} />
      <path d="M 49 78 l -6 -5 l 1.4 -2 l 6 5 z" />
    </g>
    <rect x={0} y={0} width={100} height={100} fill="none" stroke={CLAUDE.BORDER} strokeWidth={1.4} />
  </svg>
);

/** One caption under judgement: the text, and the filter's verdict on it. */
const TextRow: React.FC<{
  tag: string;
  text: string;
  verdict: string;
  rejected: boolean;
  o: number;
  vo: number;
  portrait: boolean;
}> = ({ tag, text, verdict, rejected, o, vo, portrait }) => (
  <div style={{ opacity: o, minWidth: 0 }}>
    <div style={{ display: 'flex', alignItems: 'baseline', gap: 12, minWidth: 0 }}>
      <div style={{
        fontFamily: MONO, fontSize: portrait ? 27 : 28, fontWeight: 700, flex: '0 0 auto',
        color: CLAUDE.GHOST,
      }}>{tag}</div>
      <div style={{
        // `0 1 auto` (not `1 1 auto`): the strike below is this element's background, so
        // a full-width box drew a rule that ran well past the last word. Sized to its
        // content, the strike ends where the sentence does.
        fontFamily: SANS, fontSize: portrait ? 30 : 32, flex: '0 1 auto', minWidth: 0,
        lineHeight: 1.25, color: rejected ? CLAUDE.GHOST : CLAUDE.INK,
        // ONE LINE, ALWAYS. The strike below is a background gradient at 50% of the
        // element's height, which is only a strike-THROUGH while the text is a single
        // line — on two wrapped lines it draws in the gap between them and reads as an
        // underline on the first. nowrap + ellipsis makes the geometry unconditional
        // instead of dependent on the string and the canvas.
        whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis',
        // the strike is DRAWN as the verdict lands, so the judgement is an event
        // the viewer watches rather than a state that was always there
        backgroundImage: rejected
          ? `linear-gradient(${CLAUDE.SPARK}, ${CLAUDE.SPARK})`
          : 'none',
        backgroundSize: `${vo * 100}% 3px`,
        backgroundPosition: '0 50%',
        backgroundRepeat: 'no-repeat',
      }}>{text}</div>
    </div>
    <div style={{
      fontFamily: MONO, fontSize: portrait ? 26 : 27, fontWeight: 700, letterSpacing: 1.2,
      marginTop: 6, opacity: vo,
      color: rejected ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
    }}>{verdict}</div>
  </div>
);

export const BlipCapFilt: React.FC<BlipCapFiltProps> = ({
  spark, heading, webText, synthText, webVerdict, synthVerdict,
  illustrativeNote, rateLabel, ratePct, rateNote, tiles, closing, source,
}) => {
  const p = useP();
  const { portrait, safe } = useGeo();
  const head = ease(remap(p, 0.02, 0.10, 0, 1));
  const imgIn = ease(remap(p, 0.08, 0.20, 0, 1));
  const webIn = ease(remap(p, 0.16, 0.27, 0, 1));
  const synthIn = ease(remap(p, 0.28, 0.42, 0, 1));
  const judge = ease(remap(p, 0.44, 0.58, 0, 1));
  const gridIn = ease(remap(p, 0.52, 0.66, 0, 1));
  const strike = ease(remap(p, 0.64, 0.80, 0, 1));
  const closeIn = ease(remap(p, 0.82, 0.95, 0, 1));

  const nTiles = Math.max(1, Math.round(tiles));
  const nRejected = Math.round((nTiles * ratePct) / 100);
  // deterministic, evenly-spread rejections — no randomness anywhere in a render
  const rejectedSet = new Set(
    Array.from({ length: nRejected }, (_, k) => Math.round((k + 0.5) * (nTiles / Math.max(1, nRejected)))),
  );
  // the image is EVIDENCE, not a thumbnail: at safe.w*0.17 it occupied a fifth of the
  // left panel and the rest of the panel went empty (FILL-THE-CANVAS LAW).
  const IMG_W = Math.round(portrait ? safe.w * 0.50 : safe.w * 0.30);
  const IMG_H = Math.round(IMG_W * 0.72);

  return (
    <Stage spark={spark} source={source}>
      <div style={{
        // `minWidth: 0` is a STRUCTURAL GUARD. A flex item's automatic minimum width is
        // its min-content width, so one unshrinkable child (a `nowrap` label, a
        // content-sized row) can widen this whole column past the safe box — and then
        // every paragraph in it wraps at the wrong width and gets clipped by the stage.
        // That is exactly how B06's axis labels clipped its closing line.
        flex: 1, minWidth: 0, display: 'flex', flexDirection: 'column',
        justifyContent: 'space-between', gap: portrait ? 18 : 16, minHeight: 0,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 54 : 60, fontWeight: 700, color: CLAUDE.INK,
          opacity: head, flex: '0 0 auto',
        }}>{heading}</div>

        <div style={{
          flex: '1 1 auto', minHeight: 0, minWidth: 0, display: 'flex',
          flexDirection: portrait ? 'column' : 'row', gap: portrait ? 20 : 30,
          alignItems: 'stretch',
        }}>
          {/* ── one image ─────────────────────────────────────────────── */}
          <div style={{
            flex: '1 1 0', minWidth: 0, minHeight: 0,
            display: 'flex', flexDirection: 'column', justifyContent: 'space-between',
            gap: portrait ? 16 : 14,
          }}>
            {/* the image gets the panel's full width, so the captions below it get the
                full width too — which is what lets them stay on one line */}
            <div style={{ opacity: imgIn, flex: '0 0 auto' }}>
              <WebImageGlyph w={IMG_W} h={IMG_H} />
            </div>
            <TextRow tag="Tw" text={webText} verdict={webVerdict} rejected
              o={webIn} vo={judge} portrait={portrait} />
            <TextRow tag="Ts" text={synthText} verdict={synthVerdict} rejected={false}
              o={synthIn} vo={judge} portrait={portrait} />
            <div style={{
              fontFamily: SANS, fontSize: portrait ? 24 : 25, color: CLAUDE.GHOST,
              lineHeight: 1.28, opacity: judge, flex: '0 0 auto',
            }}>{illustrativeNote}</div>
          </div>

          {/* ── the published rate ─────────────────────────────────────── */}
          <div style={{
            flex: '1 1 0', minWidth: 0, minHeight: 0,
            display: 'flex', flexDirection: 'column', gap: portrait ? 14 : 14,
            borderLeft: portrait ? 'none' : `2px solid ${CLAUDE.BORDER}`,
            borderTop: portrait ? `2px solid ${CLAUDE.BORDER}` : 'none',
            paddingLeft: portrait ? 0 : 28, paddingTop: portrait ? 18 : 0,
          }}>
            <div style={{ display: 'flex', alignItems: 'baseline', gap: 16, opacity: gridIn, minWidth: 0 }}>
              <div style={{
                fontFamily: MONO, fontSize: portrait ? 92 : 96, fontWeight: 700,
                color: CLAUDE.SPARK, lineHeight: 0.95, flex: '0 0 auto',
              }}>{Math.round(ratePct * strike)}%</div>
              <div style={{ flex: '1 1 auto', minWidth: 0 }}>
                <div style={{
                  fontFamily: SANS, fontSize: portrait ? 32 : 33, fontWeight: 700, color: CLAUDE.INK,
                }}>{rateLabel}</div>
                <div style={{
                  fontFamily: SANS, fontSize: portrait ? 26 : 27, color: CLAUDE.INK_SOFT, lineHeight: 1.26,
                }}>{rateNote}</div>
              </div>
            </div>

            {/* the tiles ARE the rate: 5 of 20 struck. A CSS grid with fractional rows
                and columns stretches the cells to whatever the panel gives it, so the
                cohort fills the same box on both canvases without a px guess. */}
            <div style={{
              flex: '1 1 auto', minHeight: 0, minWidth: 0, display: 'grid',
              gridTemplateColumns: 'repeat(5, 1fr)',
              gridTemplateRows: `repeat(${Math.ceil(nTiles / 5)}, 1fr)`,
              gap: portrait ? 11 : 10,
            }}>
              {Array.from({ length: nTiles }, (_, k) => {
                const rej = rejectedSet.has(k);
                const tin = clamp(ease(remap(p, 0.54 + k * 0.006, 0.62 + k * 0.006, 0, 1)), 0, 1);
                const so = rej ? clamp(ease(remap(p, 0.66 + k * 0.004, 0.78 + k * 0.004, 0, 1)), 0, 1) : 0;
                return (
                  <div key={k} style={{
                    position: 'relative', minWidth: 0, minHeight: 0, overflow: 'hidden',
                    background: rej ? 'transparent' : CLAUDE.PILL,
                    border: `2px solid ${rej ? CLAUDE.SPARK : CLAUDE.BORDER}`,
                    borderRadius: 8, opacity: tin, boxSizing: 'border-box',
                    display: 'flex', flexDirection: 'column', justifyContent: 'center',
                    gap: 6, padding: '0 12px',
                  }}>
                    {/* two grey bars so a tile reads as a caption, not a blank pill */}
                    <div style={{ height: 4, borderRadius: 2, width: '86%', background: rej ? CLAUDE.BORDER : CLAUDE.GHOST, opacity: 0.75 }} />
                    <div style={{ height: 4, borderRadius: 2, width: '58%', background: rej ? CLAUDE.BORDER : CLAUDE.GHOST, opacity: 0.75 }} />
                    <div style={{
                      position: 'absolute', left: 0, top: '50%', marginTop: -1.5, height: 3,
                      width: `${so * 100}%`, background: CLAUDE.SPARK,
                    }} />
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* what the survivors become */}
        <div style={{ flex: '0 0 auto', opacity: closeIn }}>
          <div style={{ height: 5, borderRadius: 3, background: CLAUDE.SPARK, width: `${closeIn * 100}%` }} />
          <div style={{
            fontFamily: SERIF, fontSize: portrait ? 34 : 38, color: CLAUDE.INK,
            marginTop: 11, lineHeight: 1.26, maxWidth: '100%', overflowWrap: 'break-word',
          }}>{closing}</div>
        </div>
      </div>
    </Stage>
  );
};
