import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, Stage, clamp, ease, remap, useGeo, useP } from './ReelKit';

/**
 * BlipDiversity — the FRICTION beat: the tension the viewer has to resolve.
 *
 * Table 2 puts two measures on the captioner's decoding strategy that a viewer expects
 * to move in OPPOSITE directions, and they don't. Nucleus sampling produces captions
 * the filter rejects MORE often (25% vs beam search's 19%) and downstream retrieval
 * gets BETTER (80.6 vs 79.6 TR@1). Noisier data, better model.
 *
 * The graphic is a butterfly: noise grows to the left, accuracy grows to the right,
 * and both wings get longer as you go down. The paradox is the SHAPE, not a caption
 * about it — nothing here needs the voice to explain what the viewer is looking at.
 *
 * HONESTY: the accuracy wing is on a TRUNCATED axis (a 78.4-to-80.6 spread is invisible
 * on 0-100), so the axis floor is stated on screen and the wing is drawn from a visible
 * origin rule. A truncated axis that hides its own floor is the exact sin this series
 * is about.
 */
export const blipDiversitySchema = z.object({
  spark: z.string().default('Noisier, and better.'),
  heading: z.string().default('How the captioner writes'),
  rows: z.array(z.object({
    label: z.string(),
    sub: z.string().default(''),
    /** percent the filter rejects; negative means "not applicable" (no synthetic text) */
    noise: z.number().default(-1),
    /** COCO TR@1 */
    score: z.number(),
  })).default([]),
  accentIndex: z.number().default(2),
  noiseMax: z.number().default(30),
  scoreFloor: z.number().default(77),
  scoreCeil: z.number().default(81),
  noiseAxis: z.string().default('NOISE RATIO — 0 to 30%'),
  scoreAxis: z.string().default('COCO TR@1 — axis starts at 77'),
  closing: z.string().default(''),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(13),
});
export type BlipDiversityProps = z.infer<typeof blipDiversitySchema>;

export const BlipDiversity: React.FC<BlipDiversityProps> = ({
  spark, heading, rows, accentIndex, noiseMax, scoreFloor, scoreCeil,
  noiseAxis, scoreAxis, closing, source,
}) => {
  const p = useP();
  const { portrait, safe } = useGeo();
  const head = ease(remap(p, 0.02, 0.10, 0, 1));
  const axIn = ease(remap(p, 0.08, 0.18, 0, 1));
  const grow = (i: number) => ease(remap(p, 0.18 + i * 0.13, 0.48 + i * 0.13, 0, 1));
  const closeIn = ease(remap(p, 0.78, 0.94, 0, 1));

  // every width derives from the safe box — a px number tuned on one canvas is wrong
  // on the other, and always fails the same way (ReelKit corollary)
  const MID_W = Math.round(safe.w * (portrait ? 0.30 : 0.21));
  const NUM_W = Math.round(safe.w * (portrait ? 0.13 : 0.075));
  // the wings ARE the argument, so they get real weight — at 48px in a ~200px row
  // slot the chart read as three thin lines floating in air
  const BAR_H = portrait ? 62 : 68;

  return (
    <Stage spark={spark} source={source}>
      <div style={{
        // `minWidth: 0` is a STRUCTURAL GUARD. A flex item's automatic minimum width is
        // its min-content width, so one unshrinkable child (a `nowrap` label, a
        // content-sized row) can widen this whole column past the safe box — and then
        // every paragraph in it wraps at the wrong width and gets clipped by the stage.
        // That is exactly how B06's axis labels clipped its closing line.
        flex: 1, minWidth: 0, display: 'flex', flexDirection: 'column',
        justifyContent: 'space-between', gap: portrait ? 16 : 14, minHeight: 0,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 54 : 60, fontWeight: 700, color: CLAUDE.INK,
          opacity: head, flex: '0 0 auto',
        }}>{heading}</div>

        {/* the two axes, declared before the bars land */}
        <div style={{
          flex: '0 0 auto', display: 'flex', alignItems: 'flex-end', gap: 12,
          opacity: axIn, minWidth: 0,
        }}>
          {/* These WRAP rather than clip. As `nowrap` they lost their tails at the
              portrait cell boundary ("COCO TR@1 — axis start"), and an axis disclosure
              that is cut off mid-word is not a disclosure. Two short lines cost nothing
              here and read identically on both canvases. */}
          <div style={{
            flex: '1 1 0', minWidth: 0, textAlign: 'right', fontFamily: MONO,
            fontSize: portrait ? 22 : 24, color: CLAUDE.INK_SOFT, letterSpacing: 0.6,
            lineHeight: 1.25,
          }}>{noiseAxis}</div>
          <div style={{ width: MID_W, flex: '0 0 auto' }} />
          <div style={{
            flex: '1 1 0', minWidth: 0, fontFamily: MONO,
            fontSize: portrait ? 22 : 24, color: CLAUDE.INK_SOFT, letterSpacing: 0.6,
            lineHeight: 1.25,
          }}>{scoreAxis}</div>
        </div>

        {/* the butterfly */}
        <div style={{
          flex: '1 1 auto', minHeight: 0, minWidth: 0, display: 'flex', flexDirection: 'column',
          justifyContent: 'space-around',
        }}>
          {rows.slice(0, 4).map((r, i) => {
            const g = clamp(grow(i), 0, 1);
            const on = i === accentIndex;
            const col = on ? CLAUDE.SPARK : CLAUDE.INK;
            const noiseFrac = r.noise >= 0 ? clamp(r.noise / noiseMax, 0, 1) : 0;
            const scoreFrac = clamp((r.score - scoreFloor) / (scoreCeil - scoreFloor || 1), 0, 1);
            return (
              <div key={r.label} style={{
                display: 'flex', alignItems: 'center', gap: 12, minWidth: 0, opacity: g,
              }}>
                {/* left wing — noise ratio, growing outward from the centre */}
                <div style={{
                  width: NUM_W, flex: '0 0 auto', textAlign: 'right', fontFamily: MONO,
                  fontSize: portrait ? 30 : 32, fontWeight: 700, color: r.noise >= 0 ? col : CLAUDE.GHOST,
                }}>{r.noise >= 0 ? `${Math.round(r.noise * g)}%` : '—'}</div>
                <div style={{
                  flex: '1 1 0', minWidth: 0, height: BAR_H, background: CLAUDE.PILL,
                  borderRadius: 6, display: 'flex', justifyContent: 'flex-end', overflow: 'hidden',
                }}>
                  <div style={{ width: `${noiseFrac * g * 100}%`, height: '100%', background: col, borderRadius: 6 }} />
                </div>

                {/* the centre spine — which decoding strategy this row is */}
                <div style={{
                  width: MID_W, flex: '0 0 auto', textAlign: 'center', padding: '0 8px',
                  boxSizing: 'border-box',
                }}>
                  <div style={{
                    fontFamily: SANS, fontSize: portrait ? 31 : 33, fontWeight: 700,
                    color: on ? CLAUDE.SPARK : CLAUDE.INK, lineHeight: 1.12,
                  }}>{r.label}</div>
                  {r.sub ? (
                    <div style={{
                      fontFamily: SANS, fontSize: portrait ? 23 : 24, color: CLAUDE.INK_SOFT, lineHeight: 1.18,
                    }}>{r.sub}</div>
                  ) : null}
                </div>

                {/* right wing — accuracy, growing outward from the same centre */}
                <div style={{
                  flex: '1 1 0', minWidth: 0, height: BAR_H, background: CLAUDE.PILL,
                  borderRadius: 6, overflow: 'hidden', borderLeft: `3px solid ${CLAUDE.BORDER}`,
                  boxSizing: 'border-box',
                }}>
                  <div style={{ width: `${scoreFrac * g * 100}%`, height: '100%', background: col, borderRadius: 6 }} />
                </div>
                <div style={{
                  width: NUM_W, flex: '0 0 auto', fontFamily: MONO,
                  fontSize: portrait ? 30 : 32, fontWeight: 700, color: col,
                }}>{(scoreFloor + (r.score - scoreFloor) * g).toFixed(1)}</div>
              </div>
            );
          })}
        </div>

        <div style={{ flex: '0 0 auto', opacity: closeIn }}>
          <div style={{ height: 5, borderRadius: 3, background: CLAUDE.SPARK, width: `${closeIn * 100}%` }} />
          <div style={{
            fontFamily: SERIF, fontSize: portrait ? 33 : 37, color: CLAUDE.INK,
            marginTop: 11, lineHeight: 1.26, maxWidth: '100%', overflowWrap: 'break-word',
          }}>{closing}</div>
        </div>
      </div>
    </Stage>
  );
};
