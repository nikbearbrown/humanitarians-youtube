import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, STAGE, Stage, clamp, ease, remap, useGeo, useP } from './ReelKit';

/**
 * BlipLadder — the ABLATION beat: the fourth axis of the audit, run on BLIP itself.
 *
 * Table 1's 14M block is the cleanest ablation in the paper — same images, same
 * ViT-B/16 backbone, only the bootstrap changes. The ladder climbs 78.4 -> 79.1
 * (filter alone) -> 79.7 (captioner alone) -> 80.6 (both). Then a fifth bar changes
 * the question: 129M images with no bootstrap at all reaches 79.6, SHORT of the
 * bootstrapped 14M. Nine times the web data loses to cleaning up a ninth of it.
 *
 * TWO HONESTY DEVICES, both required rather than decorative:
 *  1. The axis is TRUNCATED (a 2.2-point spread is invisible on 0-100), so a real axis
 *     strip with a break glyph and both tick values is drawn under the bars. A chart
 *     that hides its own floor is the sin this series exists to name.
 *  2. The exception is on screen next to the claim. On COCO CAPTIONING the raw 129M
 *     edges the bootstrapped 14M (CIDEr 130.1 vs 129.7). The thesis holds for
 *     retrieval, not everywhere, and the beat says so in the same frame.
 *
 * The reference line is COMPOSED FROM THE ROWS — each row draws its own segment inside
 * its own bar track. An absolutely-positioned line over a flex column drifts the moment
 * row heights change; this cannot.
 */
export const blipLadderSchema = z.object({
  spark: z.string().default('Turn the bootstrap off.'),
  heading: z.string().default('The ablation'),
  bars: z.array(z.object({
    label: z.string(),
    sub: z.string().default(''),
    value: z.number(),
    accent: z.boolean().default(false),
  })).default([]),
  /** the value the dashed reference line marks (the bootstrapped result) */
  refValue: z.number().default(80.6),
  floor: z.number().default(77),
  ceil: z.number().default(81.5),
  axisNote: z.string().default('COCO 5K test · TR@1 · ViT-B/16'),
  exception: z.string().default(''),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(14),
});
export type BlipLadderProps = z.infer<typeof blipLadderSchema>;

export const BlipLadder: React.FC<BlipLadderProps> = ({
  spark, heading, bars, refValue, floor, ceil, axisNote, exception, source,
}) => {
  const p = useP();
  const { portrait, safe } = useGeo();
  const head = ease(remap(p, 0.02, 0.10, 0, 1));
  const grow = (i: number) => ease(remap(p, 0.11 + i * 0.095, 0.36 + i * 0.095, 0, 1));
  const refIn = ease(remap(p, 0.62, 0.76, 0, 1));
  const axIn = ease(remap(p, 0.14, 0.26, 0, 1));
  const excIn = ease(remap(p, 0.80, 0.94, 0, 1));

  const LABEL_W = Math.round(safe.w * (portrait ? 0.36 : 0.25));
  const VAL_W = Math.round(safe.w * (portrait ? 0.15 : 0.085));
  const frac = (v: number) => clamp((v - floor) / (ceil - floor || 1), 0, 1);
  const refFrac = frac(refValue);

  return (
    <Stage spark={spark} source={source}>
      <div style={{
        // `minWidth: 0` is a STRUCTURAL GUARD. A flex item's automatic minimum width is
        // its min-content width, so one unshrinkable child (a `nowrap` label, a
        // content-sized row) can widen this whole column past the safe box — and then
        // every paragraph in it wraps at the wrong width and gets clipped by the stage.
        // That is exactly how B06's axis labels clipped its closing line.
        flex: 1, minWidth: 0, display: 'flex', flexDirection: 'column',
        justifyContent: 'space-between', gap: portrait ? 16 : 12, minHeight: 0,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 54 : 60, fontWeight: 700, color: CLAUDE.INK,
          opacity: head, flex: '0 0 auto',
        }}>{heading}</div>

        {/* the ladder */}
        <div style={{
          flex: '1 1 auto', minHeight: 0, minWidth: 0, display: 'flex', flexDirection: 'column',
          justifyContent: 'stretch',
        }}>
          {bars.slice(0, 6).map((b, i) => {
            const g = clamp(grow(i), 0, 1);
            const on = b.accent;
            const col = on ? CLAUDE.SPARK : CLAUDE.INK;
            return (
              <div key={b.label} style={{
                flex: '1 1 0', minHeight: 0, minWidth: 0, display: 'flex', alignItems: 'center',
                gap: portrait ? 12 : 18, opacity: g,
              }}>
                <div style={{ width: LABEL_W, flex: '0 0 auto', textAlign: 'right' }}>
                  <div style={{
                    fontFamily: SANS, fontSize: portrait ? 29 : 31, fontWeight: on ? 700 : 400,
                    color: on ? CLAUDE.SPARK : CLAUDE.INK, lineHeight: 1.14,
                  }}>{b.label}</div>
                  {b.sub ? (
                    <div style={{
                      fontFamily: SANS, fontSize: portrait ? 23 : 24, color: CLAUDE.INK_SOFT, lineHeight: 1.18,
                    }}>{b.sub}</div>
                  ) : null}
                </div>
                <div style={{
                  flex: '1 1 auto', minWidth: 0, height: portrait ? 50 : 52, position: 'relative',
                  background: CLAUDE.PILL, borderRadius: 6, overflow: 'hidden',
                }}>
                  <div style={{
                    width: `${frac(b.value) * g * 100}%`, height: '100%', borderRadius: 6, background: col,
                  }} />
                  {/* this row's segment of the reference line */}
                  <div style={{
                    position: 'absolute', left: `${refFrac * 100}%`, top: 0, bottom: 0, width: 3,
                    opacity: refIn,
                    backgroundImage: `repeating-linear-gradient(${CLAUDE.SEND} 0 9px, transparent 9px 17px)`,
                  }} />
                </div>
                <div style={{
                  width: VAL_W, flex: '0 0 auto', fontFamily: MONO,
                  fontSize: portrait ? 33 : 36, fontWeight: 700, color: col,
                }}>{(floor + (b.value - floor) * g).toFixed(1)}</div>
              </div>
            );
          })}
        </div>

        {/* the axis, drawn rather than assumed — break glyph, both ticks, what is measured */}
        <div style={{
          flex: '0 0 auto', display: 'flex', alignItems: 'center', gap: portrait ? 12 : 18, opacity: axIn,
          minWidth: 0,
        }}>
          <div style={{
            // ellipsis, not a bare clip: this box is LABEL_W wide and a longer note
            // silently lost its tail mid-token ("ViT-B/1"). Degrading visibly is the
            // difference between a caption you can trust and one you cannot.
            width: LABEL_W, flex: '0 0 auto', textAlign: 'right', fontFamily: MONO,
            fontSize: portrait ? 22 : 23, color: CLAUDE.INK_SOFT,
            overflow: 'hidden', whiteSpace: 'nowrap', textOverflow: 'ellipsis',
          }}>{axisNote}</div>
          <div style={{ flex: '1 1 auto', minWidth: 0, position: 'relative', height: 44 }}>
            <div style={{ position: 'absolute', left: 0, right: 0, top: 8, height: 2, background: CLAUDE.GHOST }} />
            {/* The break glyph: this axis does NOT start at zero, and says so. Drawn at
                the same weight as the axis rule and on its own cream patch, because at
                18x16 it read as a stray mark and collided with the floor tick — a
                disclosure nobody can see is not a disclosure. */}
            <svg width={30} height={26} viewBox="0 0 30 26"
              style={{ position: 'absolute', left: -4, top: -4 }}>
              <rect x={6} y={0} width={16} height={26} fill={STAGE} />
              <path d="M 6 22 L 16 2 M 14 22 L 24 2" stroke={CLAUDE.INK_SOFT} strokeWidth={2.6} fill="none" />
            </svg>
            <div style={{
              position: 'absolute', left: 30, top: 16, fontFamily: MONO, fontSize: portrait ? 23 : 24,
              color: CLAUDE.INK_SOFT,
            }}>axis {floor.toFixed(0)}</div>
            <div style={{
              position: 'absolute', right: 0, top: 16, fontFamily: MONO, fontSize: portrait ? 23 : 24,
              color: CLAUDE.INK_SOFT,
            }}>{ceil.toFixed(1)}</div>
          </div>
          <div style={{ width: VAL_W, flex: '0 0 auto' }} />
        </div>

        {/* where the claim does NOT hold — in the same frame as the claim */}
        <div style={{
          flex: '0 0 auto', opacity: excIn, borderLeft: `5px solid ${CLAUDE.SEND}`,
          paddingLeft: 18, minWidth: 0,
        }}>
          <div style={{
            fontFamily: SERIF, fontSize: portrait ? 32 : 35, color: CLAUDE.INK, lineHeight: 1.26,
          }}>{exception}</div>
        </div>
      </div>
    </Stage>
  );
};
