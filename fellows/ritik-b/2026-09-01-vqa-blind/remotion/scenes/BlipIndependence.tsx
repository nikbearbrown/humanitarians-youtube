import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, Stage, clamp, ease, remap, useGeo, useP } from './ReelKit';

/**
 * BlipIndependence — the EDGE-CASE beat, and the reel's sharpest receipt.
 *
 * BLIP finetunes the captioner and the filter INDIVIDUALLY off the same pre-trained
 * model. Table 4 asks what happens if you let them share parameters instead, the way
 * the encoder and decoder do during pre-training: the filter's rejection rate collapses
 * from 25% to 8% — it stops recognising its twin's mistakes — and every downstream
 * number falls with it. That is confirmation bias, measured.
 *
 * Every number on this beat is published and cited in the same frame. The deltas are
 * COMPUTED from the two columns rather than authored, so they cannot drift from the
 * numbers they describe.
 *
 * The ONE terracotta moment is the decoupled design — the column that wins.
 *
 * Responsive: the two rejection figures stay side by side in both orientations (two
 * short numbers fit the 972px short axis); the table's label column shrinks.
 */
export const blipIndependenceSchema = z.object({
  spark: z.string().default('Who filters the filter?'),
  heading: z.string().default('Let the judge share the writer’s weights'),
  leftLabel: z.string().default('Shared parameters'),
  rightLabel: z.string().default('Decoupled'),
  leftNoise: z.number().default(8),
  rightNoise: z.number().default(25),
  noiseCaption: z.string().default('of the captioner’s output rejected'),
  metrics: z.array(z.object({
    label: z.string(),
    left: z.number(),
    right: z.number(),
  })).default([]),
  closing: z.string().default(''),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(13),
});
export type BlipIndependenceProps = z.infer<typeof blipIndependenceSchema>;

export const BlipIndependence: React.FC<BlipIndependenceProps> = ({
  spark, heading, leftLabel, rightLabel, leftNoise, rightNoise, noiseCaption,
  metrics, closing, source,
}) => {
  const p = useP();
  const { portrait, safe } = useGeo();
  const head = ease(remap(p, 0.02, 0.10, 0, 1));
  const nLeft = ease(remap(p, 0.10, 0.26, 0, 1));
  const nRight = ease(remap(p, 0.22, 0.38, 0, 1));
  const rowIn = (i: number) => ease(remap(p, 0.40 + i * 0.075, 0.58 + i * 0.075, 0, 1));
  const deltaIn = ease(remap(p, 0.70, 0.84, 0, 1));
  const closeIn = ease(remap(p, 0.82, 0.95, 0, 1));

  // value + delta columns are sized from the safe box, never from a px guess
  const VAL_W = Math.round(safe.w * (portrait ? 0.20 : 0.11));
  const DEL_W = Math.round(safe.w * (portrait ? 0.13 : 0.075));

  const Big: React.FC<{ label: string; pct: number; o: number; accent: boolean }> = ({ label, pct, o, accent }) => (
    <div style={{ flex: '1 1 0', minWidth: 0, opacity: o }}>
      <div style={{
        fontFamily: SANS, fontSize: portrait ? 29 : 31, fontWeight: 700, letterSpacing: 1.2,
        color: accent ? CLAUDE.SPARK : CLAUDE.INK_SOFT, textTransform: 'uppercase',
      }}>{label}</div>
      <div style={{
        fontFamily: MONO, fontSize: portrait ? 104 : 112, fontWeight: 700, lineHeight: 1,
        color: accent ? CLAUDE.SPARK : CLAUDE.INK, marginTop: 2,
      }}>{Math.round(pct * o)}%</div>
    </div>
  );

  return (
    <Stage spark={spark} source={source}>
      <div style={{
        // `minWidth: 0` is a STRUCTURAL GUARD. A flex item's automatic minimum width is
        // its min-content width, so one unshrinkable child (a `nowrap` label, a
        // content-sized row) can widen this whole column past the safe box — and then
        // every paragraph in it wraps at the wrong width and gets clipped by the stage.
        // That is exactly how B06's axis labels clipped its closing line.
        flex: 1, minWidth: 0, display: 'flex', flexDirection: 'column',
        justifyContent: 'space-between', gap: portrait ? 20 : 16, minHeight: 0,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 50 : 56, fontWeight: 700, color: CLAUDE.INK,
          opacity: head, flex: '0 0 auto', lineHeight: 1.1,
        }}>{heading}</div>

        {/* the rejection rates — the mechanism failing, in one pair of numbers */}
        <div style={{ flex: '0 0 auto', minWidth: 0 }}>
          <div style={{ display: 'flex', gap: portrait ? 24 : 34, minWidth: 0 }}>
            <Big label={leftLabel} pct={leftNoise} o={nLeft} accent={false} />
            <Big label={rightLabel} pct={rightNoise} o={nRight} accent />
          </div>
          <div style={{
            fontFamily: SANS, fontSize: portrait ? 27 : 28, color: CLAUDE.INK_SOFT,
            opacity: nRight, marginTop: 4,
          }}>{noiseCaption}</div>
        </div>

        {/* what it costs downstream */}
        <div style={{
          flex: '1 1 auto', minHeight: 0, minWidth: 0, display: 'flex', flexDirection: 'column',
          justifyContent: 'stretch',
        }}>
          {metrics.slice(0, 5).map((m, i) => {
            const o = clamp(rowIn(i), 0, 1);
            const d = m.right - m.left;
            return (
              <div key={m.label} style={{
                flex: '1 1 0', minHeight: 0, minWidth: 0, display: 'flex', alignItems: 'center',
                gap: portrait ? 12 : 18, opacity: o,
                borderTop: `2px solid ${CLAUDE.BORDER}`,
              }}>
                <div style={{
                  flex: '1 1 auto', minWidth: 0, fontFamily: SANS,
                  fontSize: portrait ? 28 : 30, color: CLAUDE.INK, lineHeight: 1.16,
                }}>{m.label}</div>
                <div style={{
                  width: VAL_W, flex: '0 0 auto', textAlign: 'right', fontFamily: MONO,
                  fontSize: portrait ? 33 : 35, color: CLAUDE.INK_SOFT,
                }}>{m.left.toFixed(1)}</div>
                <div style={{
                  width: VAL_W, flex: '0 0 auto', textAlign: 'right', fontFamily: MONO,
                  fontSize: portrait ? 33 : 35, fontWeight: 700, color: CLAUDE.SPARK,
                }}>{m.right.toFixed(1)}</div>
                <div style={{
                  width: DEL_W, flex: '0 0 auto', textAlign: 'right', fontFamily: MONO,
                  fontSize: portrait ? 26 : 27, color: CLAUDE.GHOST, opacity: deltaIn,
                }}>{d >= 0 ? '+' : '−'}{Math.abs(d).toFixed(1)}</div>
              </div>
            );
          })}
        </div>

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
