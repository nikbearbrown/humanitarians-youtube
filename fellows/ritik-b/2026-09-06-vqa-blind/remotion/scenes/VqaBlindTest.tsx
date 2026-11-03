import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, VqaStage, clamp, ease, remap, useGeo, useP } from './VqaKit';

/**
 * VqaBlindTest — MOVE 4, the FALSIFIABILITY beat, and the reel's load-bearing receipt.
 *
 * Every number here is published and cited on screen (the `source` slot renders under
 * the artwork, so the claim and its citation are legible in the same frame — the
 * production gate this reel is held to). Nothing is illustrative on this beat.
 *
 * The bracket between the blind bar and the sighted bar is the whole argument: it is
 * drawn, labelled with the arithmetic difference, and held for the rest of the beat.
 */
export const vqaBlindTestSchema = z.object({
  spark: z.string().default('Hide the image.'),
  heading: z.string().default('Move 4 — the blind test'),
  bars: z.array(z.object({
    label: z.string(),
    value: z.number(),
    note: z.string().default(''),
    accent: z.boolean().default(false),
  })).default([]),
  /** Indices of the two bars the bracket spans, and the label on it. */
  bracketFrom: z.number().default(1),
  bracketTo: z.number().default(2),
  bracketLabel: z.string().default('+8.99 pts — everything the image was worth'),
  callout: z.string().default('On yes/no questions the blind model scores 78.20%.'),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(12),
});
export type VqaBlindTestProps = z.infer<typeof vqaBlindTestSchema>;

const AXIS_MAX = 100;

export const VqaBlindTest: React.FC<VqaBlindTestProps> = ({
  spark, heading, bars, bracketFrom, bracketTo, bracketLabel, callout, source,
}) => {
  const p = useP();
  const { portrait } = useGeo();
  const head = ease(remap(p, 0.02, 0.11, 0, 1));
  const grow = (i: number) => ease(remap(p, 0.12 + i * 0.09, 0.38 + i * 0.09, 0, 1));
  const brack = ease(remap(p, 0.56, 0.74, 0, 1));
  const callIn = ease(remap(p, 0.76, 0.90, 0, 1));

  const LABEL_W = portrait ? 300 : 340;
  const VAL_W = portrait ? 118 : 132;

  return (
    <VqaStage spark={spark} source={source}>
      <div style={{
        flex: 1, display: 'flex', flexDirection: 'column',
        justifyContent: 'space-between', gap: portrait ? 18 : 14, minHeight: 0,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 54 : 60, fontWeight: 700, color: CLAUDE.INK,
          opacity: head, flex: '0 0 auto',
        }}>{heading}</div>

        <div style={{
          flex: '1 1 auto', minHeight: 0, display: 'flex', flexDirection: 'column',
          justifyContent: 'stretch', gap: 0,
        }}>
          {bars.slice(0, 5).map((b, i) => {
            const g = clamp(grow(i), 0, 1);
            const on = b.accent;
            // The bracket is COMPOSED FROM THE ROWS — each row in [from..to] draws its
            // own segment in a trailing gutter. An absolutely-positioned bracket over a
            // flex column drifts the moment row heights change (it did: it spanned all
            // four bars instead of blind -> sighted). This cannot drift.
            const inSpan = i >= bracketFrom && i <= bracketTo;
            const isEnd = i === bracketFrom || i === bracketTo;
            return (
              <div key={b.label} style={{ display: 'flex', alignItems: 'center', gap: 16, flex: '1 1 0', minHeight: 0 }}>
                <div style={{ width: LABEL_W, flex: '0 0 auto', textAlign: 'right' }}>
                  <div style={{
                    fontFamily: SANS, fontSize: portrait ? 31 : 33, fontWeight: on ? 700 : 400,
                    color: on ? CLAUDE.SPARK : CLAUDE.INK, lineHeight: 1.16,
                  }}>{b.label}</div>
                  {b.note ? (
                    <div style={{ fontFamily: SANS, fontSize: 25, color: CLAUDE.INK_SOFT, lineHeight: 1.2 }}>{b.note}</div>
                  ) : null}
                </div>
                <div style={{
                  flex: '1 1 auto', minWidth: 0, height: portrait ? 60 : 62,
                  background: CLAUDE.PILL, borderRadius: 7, overflow: 'hidden',
                }}>
                  <div style={{
                    width: `${(b.value / AXIS_MAX) * 100 * g}%`, height: '100%', borderRadius: 7,
                    background: on ? CLAUDE.SPARK : CLAUDE.INK,
                  }} />
                </div>
                <div style={{
                  width: VAL_W, flex: '0 0 auto', fontFamily: MONO,
                  fontSize: portrait ? 35 : 38, fontWeight: 700,
                  color: on ? CLAUDE.SPARK : CLAUDE.INK,
                }}>{(b.value * g).toFixed(2)}</div>
                {/* bracket gutter */}
                <div style={{
                  width: 26, flex: '0 0 auto', alignSelf: 'stretch', position: 'relative',
                  opacity: brack,
                }}>
                  {inSpan ? (
                    <div style={{
                      position: 'absolute',
                      top: i === bracketFrom ? '50%' : 0,
                      bottom: i === bracketTo ? '50%' : 0,
                      right: 0, width: 3, background: CLAUDE.SEND,
                    }} />
                  ) : null}
                  {isEnd ? (
                    <div style={{
                      position: 'absolute', top: '50%', right: 0, width: 16, height: 3,
                      marginTop: -1.5, background: CLAUDE.SEND,
                    }} />
                  ) : null}
                </div>
              </div>
            );
          })}
        </div>

        {/* the bracket label + the yes/no callout */}
        <div style={{ flex: '0 0 auto' }}>
          <div style={{
            fontFamily: SERIF, fontSize: portrait ? 38 : 42, color: CLAUDE.SEND, opacity: brack, lineHeight: 1.24,
          }}>{bracketLabel}</div>
          <div style={{
            fontFamily: SANS, fontSize: portrait ? 30 : 32, color: CLAUDE.INK, opacity: callIn, marginTop: 8, lineHeight: 1.26,
          }}>{callout}</div>
        </div>
      </div>
    </VqaStage>
  );
};
