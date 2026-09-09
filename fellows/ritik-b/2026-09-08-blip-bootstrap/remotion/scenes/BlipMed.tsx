import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, Stage, clamp, ease, remap, useGeo, useP } from './ReelKit';

/**
 * BlipMed — the MECHANISM beat: why ONE model can both write captions and judge them.
 *
 * BLIP's multimodal mixture of encoder-decoder (MED) runs the same text transformer in
 * three functionalities, each activating a different loss. The teaching point is the
 * LAST ROW of each card: the encoder and the decoder share every parameter except the
 * self-attention layers, which is exactly why the captioner (a decoder) and the filter
 * (an encoder) can be two cheap finetunes of one pre-trained model.
 *
 * The beat's ONE terracotta moment is the divergence itself — the decoder's causal SA
 * chip and the words "self-attention" in the closing line. Everything shared stays ink.
 *
 * Responsive: three cards across the long axis (row on 16:9, column on 9:16). Card
 * widths come from flex, never from a px number, per the ReelKit corollary.
 */
export const blipMedSchema = z.object({
  spark: z.string().default('One model, three hats.'),
  heading: z.string().default('One transformer, three jobs'),
  hats: z.array(z.object({
    name: z.string(),
    loss: z.string(),
    lossFull: z.string(),
    job: z.string(),
    /** self-attention flavour — "bi-directional" or "causal" */
    sa: z.string(),
    /** does this functionality insert the cross-attention layer? */
    ca: z.boolean(),
  })).default([]),
  /** Which card carries the divergence (its SA chip takes the accent). */
  accentIndex: z.number().default(2),
  closing: z.string().default(''),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(12),
});
export type BlipMedProps = z.infer<typeof blipMedSchema>;

/** One layer of the text transformer block, drawn as a labelled chip. */
const Layer: React.FC<{
  tag: string;
  value: string;
  on: boolean;
  accent: boolean;
  o: number;
  portrait: boolean;
}> = ({ tag, value, on, accent, o, portrait }) => (
  <div style={{
    // `flex: 1 1 0` is load-bearing, not cosmetic: at content height the three chips
    // used ~150px of a ~700px card and left a dead band above the loss footer
    // (FILL-THE-CANVAS LAW). Grown, they read as what they are — a stack of layers.
    flex: '1 1 0', minHeight: 0,
    display: 'flex', alignItems: 'center', gap: 14, opacity: o,
    background: on ? (accent ? CLAUDE.SPARK : CLAUDE.PILL) : 'transparent',
    border: `2px ${on ? 'solid' : 'dashed'} ${on ? (accent ? CLAUDE.SPARK : CLAUDE.BORDER) : CLAUDE.GHOST}`,
    borderRadius: 10, padding: portrait ? '10px 16px' : '10px 15px', minWidth: 0,
  }}>
    <div style={{
      fontFamily: MONO, fontSize: portrait ? 29 : 31, fontWeight: 700, flex: '0 0 auto',
      color: accent && on ? CLAUDE.CARD : (on ? CLAUDE.INK : CLAUDE.GHOST),
    }}>{tag}</div>
    <div style={{
      fontFamily: SANS, fontSize: portrait ? 28 : 30, flex: '1 1 auto', minWidth: 0,
      overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap',
      color: accent && on ? CLAUDE.CARD : (on ? CLAUDE.INK_SOFT : CLAUDE.GHOST),
    }}>{value}</div>
  </div>
);

export const BlipMed: React.FC<BlipMedProps> = ({
  spark, heading, hats, accentIndex, closing, source,
}) => {
  const p = useP();
  const { portrait } = useGeo();
  const head = ease(remap(p, 0.02, 0.11, 0, 1));
  const col = (i: number) => ease(remap(p, 0.12 + i * 0.13, 0.34 + i * 0.13, 0, 1));
  const layer = (i: number, j: number) => ease(remap(p, 0.20 + i * 0.13 + j * 0.035, 0.40 + i * 0.13 + j * 0.035, 0, 1));
  const closeIn = ease(remap(p, 0.78, 0.94, 0, 1));

  return (
    <Stage spark={spark} source={source}>
      <div style={{
        // `minWidth: 0` is a STRUCTURAL GUARD. A flex item's automatic minimum width is
        // its min-content width, so one unshrinkable child (a `nowrap` label, a
        // content-sized row) can widen this whole column past the safe box — and then
        // every paragraph in it wraps at the wrong width and gets clipped by the stage.
        // That is exactly how B06's axis labels clipped its closing line.
        flex: 1, minWidth: 0, display: 'flex', flexDirection: 'column',
        justifyContent: 'space-between', gap: portrait ? 22 : 18, minHeight: 0,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 54 : 60, fontWeight: 700, color: CLAUDE.INK,
          opacity: head, flex: '0 0 auto',
        }}>{heading}</div>

        <div style={{
          flex: '1 1 auto', minHeight: 0, minWidth: 0, display: 'flex',
          flexDirection: portrait ? 'column' : 'row', gap: portrait ? 16 : 22,
        }}>
          {hats.slice(0, 3).map((h, i) => {
            const o = clamp(col(i), 0, 1);
            const isAccent = i === accentIndex;
            return (
              <div key={h.name} style={{
                flex: '1 1 0', minWidth: 0, minHeight: 0, opacity: o,
                transform: `translateY(${(1 - o) * 14}px)`,
                display: 'flex', flexDirection: 'column', gap: portrait ? 9 : 10,
                background: CLAUDE.CARD, border: `3px solid ${CLAUDE.BORDER}`,
                borderRadius: 18, padding: portrait ? '16px 20px' : '20px 22px',
              }}>
                {/* which hat */}
                <div style={{
                  fontFamily: SANS, fontSize: portrait ? 31 : 32, fontWeight: 700,
                  color: CLAUDE.INK, lineHeight: 1.14,
                }}>{h.name}</div>

                {/* the three layers of the text block, top to bottom */}
                <div style={{
                  flex: '1 1 auto', minHeight: 0, minWidth: 0,
                  display: 'flex', flexDirection: 'column', gap: portrait ? 10 : 11,
                }}>
                  <Layer tag="SA" value={h.sa} on accent={isAccent}
                    o={clamp(layer(i, 0), 0, 1)} portrait={portrait} />
                  <Layer tag="CA" value={h.ca ? 'cross-attention' : 'not inserted'} on={h.ca} accent={false}
                    o={clamp(layer(i, 1), 0, 1)} portrait={portrait} />
                  <Layer tag="FFN" value="feed forward" on accent={false}
                    o={clamp(layer(i, 2), 0, 1)} portrait={portrait} />
                </div>

                {/* the loss this functionality activates, and what it is for */}
                <div style={{
                  flex: '0 0 auto', paddingTop: 10, borderTop: `2px solid ${CLAUDE.BORDER}`,
                  opacity: clamp(layer(i, 3), 0, 1), minWidth: 0,
                }}>
                  <div style={{ display: 'flex', alignItems: 'baseline', gap: 10, minWidth: 0 }}>
                    <div style={{
                      fontFamily: MONO, fontSize: portrait ? 36 : 38, fontWeight: 700, color: CLAUDE.INK,
                      flex: '0 0 auto',
                    }}>{h.loss}</div>
                    <div style={{
                      fontFamily: SANS, fontSize: portrait ? 23 : 24, color: CLAUDE.GHOST,
                      flex: '1 1 auto', minWidth: 0, overflow: 'hidden', whiteSpace: 'nowrap',
                      textOverflow: 'ellipsis',
                    }}>{h.lossFull}</div>
                  </div>
                  <div style={{
                    fontFamily: SANS, fontSize: portrait ? 28 : 29, color: CLAUDE.INK_SOFT,
                    lineHeight: 1.26, marginTop: 5,
                  }}>{h.job}</div>
                </div>
              </div>
            );
          })}
        </div>

        {/* the sharing rule — the reason two of these can be finetuned off one model */}
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
