import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, SceneGlyph, VqaStage, clamp, ease, remap, useGeo, useP } from './VqaKit';

/**
 * VqaAttend — MOVE 2, and the reel's WORKED EXAMPLE. One token ("color") is used as a
 * query, it scores all 196 patch keys, and softmax turns those scores into a weighted
 * read of the image. The viewer watches the normalisation SHARPEN the field onto the
 * region the question names — that is the reasoning step, not the conclusion.
 *
 * The weight field is a deterministic Gaussian around the umbrella's centre in the
 * SceneGlyph viewBox, raised to a low power before the softmax step and a high power
 * after, so the sharpening is visible. It is labelled ILLUSTRATIVE on screen: this
 * shows the SHAPE of an attention read, never measured weights from a real model.
 */
export const vqaAttendSchema = z.object({
  spark: z.string().default('Every word queries every patch.'),
  heading: z.string().default('Move 2 — fuse by attention'),
  queryToken: z.string().default('color'),
  formula: z.string().default('softmax( q Kᵀ / √d ) V'),
  readout: z.string().default('a weighted read of the image, conditioned on the question'),
  honesty: z.string().default('Illustrative attention field — the shape of the read, not measured weights.'),
  families: z.array(z.object({ name: z.string(), body: z.string() })).default([]),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(12),
});
export type VqaAttendProps = z.infer<typeof vqaAttendSchema>;

const GRID = 14;

/** Deterministic weight field: Gaussian falloff from the umbrella centre (54, 40). */
const rawWeight = (c: number, r: number) => {
  const cx = ((c + 0.5) / GRID) * 100;   // cell centre in the glyph's 0-100 viewBox
  const cy = ((r + 0.5) / GRID) * 100;
  const d2 = Math.pow((cx - 54) / 13, 2) + Math.pow((cy - 34) / 10, 2);
  return Math.exp(-d2);
};

export const VqaAttend: React.FC<VqaAttendProps> = ({
  spark, heading, queryToken, formula, readout, honesty, families, source,
}) => {
  const p = useP();
  const { portrait, safe } = useGeo();

  const head = ease(remap(p, 0.02, 0.12, 0, 1));
  const qIn = ease(remap(p, 0.08, 0.20, 0, 1));
  const scores = ease(remap(p, 0.16, 0.36, 0, 1));   // raw scores appear (flat, diffuse)
  const soft = ease(remap(p, 0.38, 0.62, 0, 1));     // softmax sharpens onto the umbrella
  const readIn = ease(remap(p, 0.62, 0.76, 0, 1));
  const famIn = (i: number) => ease(remap(p, 0.76 + i * 0.08, 0.92 + i * 0.08, 0, 1));

  // Sized FROM the safe box. Portrait gives the field ~74% of its narrow width;
  // landscape caps on the height it actually has after the header and footer bands.
  const gridS = Math.round(portrait ? safe.w * 0.74 : Math.min(safe.h * 0.62, safe.w * 0.33));

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
          flex: '1 1 auto', minHeight: 0, display: 'flex',
          flexDirection: portrait ? 'column' : 'row',
          gap: portrait ? 22 : 40, alignItems: portrait ? 'stretch' : 'center',
        }}>
          {/* the image, under its attention field */}
          <div style={{ position: 'relative', width: gridS, height: gridS, flex: '0 0 auto', alignSelf: 'center' }}>
            <SceneGlyph umbrella={CLAUDE.INK_SOFT} w={gridS} h={gridS} />
            <svg width={gridS} height={gridS} style={{ position: 'absolute', inset: 0 }}>
              {/* a light scrim so the heat reads as weight. Kept SHALLOW (0.14): at 0.30 it
                  desaturated the scene enough to fail GATE V's contrast floor, and the whole
                  point of the beat is that the attention lands on a picture you can still see. */}
              <rect x={0} y={0} width={gridS} height={gridS} fill={CLAUDE.PAGE} opacity={0.14 * scores} />
              {Array.from({ length: GRID * GRID }, (_, k) => {
                const c = k % GRID, r = Math.floor(k / GRID);
                const w = rawWeight(c, r);
                // raw scores: diffuse. after softmax: peaked. `soft` blends the exponent.
                const shaped = Math.pow(w, 0.45 + soft * 3.2);
                // QUANTISED to 6 steps. A continuous field renders as one smooth blush,
                // which hides the thing this beat is teaching: the query scores every
                // patch INDIVIDUALLY. Stepping the alpha makes the cells read as cells.
                const stepped = Math.round(shaped * 6) / 6;
                const a = stepped * scores;
                const s = gridS / GRID;
                // the attended cells get a crisp edge once the softmax has landed
                const edge = stepped > 0.45 ? soft : 0;
                return (
                  <rect key={k} x={c * s + 1.5} y={r * s + 1.5} width={s - 3} height={s - 3} rx={2}
                    fill={CLAUDE.SPARK} opacity={clamp(a, 0, 1) * 0.92}
                    stroke={CLAUDE.SEND} strokeWidth={2.5} strokeOpacity={edge} />
                );
              })}
              {Array.from({ length: GRID - 1 }, (_, i) => {
                const t = ((i + 1) / GRID) * gridS;
                return (
                  <g key={i} opacity={0.5 * scores}>
                    <line x1={t} y1={0} x2={t} y2={gridS} stroke={CLAUDE.INK} strokeWidth={1} />
                    <line x1={0} y1={t} x2={gridS} y2={t} stroke={CLAUDE.INK} strokeWidth={1} />
                  </g>
                );
              })}
            </svg>
            <div style={{
              position: 'absolute', left: 0, right: 0, bottom: -36,
              fontFamily: SANS, fontSize: 25, color: CLAUDE.INK_SOFT, textAlign: 'center', opacity: scores,
            }}>196 patch keys</div>
          </div>

          {/* the query, the operation, the result */}
          <div style={{ flex: '1 1 auto', minWidth: 0, display: 'flex', flexDirection: 'column', gap: portrait ? 16 : 20, justifyContent: 'center' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 16, opacity: qIn }}>
              <div style={{
                fontFamily: SANS, fontSize: 25, fontWeight: 700, letterSpacing: 3.4, color: CLAUDE.INK_SOFT,
              }}>QUERY</div>
              <div style={{
                fontFamily: MONO, fontSize: 34, color: CLAUDE.CARD, background: CLAUDE.SPARK,
                borderRadius: 10, padding: '8px 18px',
              }}>{queryToken}</div>
            </div>

            <div style={{
              fontFamily: MONO, fontSize: portrait ? 42 : 46, color: CLAUDE.INK,
              opacity: soft, letterSpacing: 0.6,
            }}>{formula}</div>

            <div style={{
              fontFamily: SERIF, fontSize: portrait ? 36 : 38, color: CLAUDE.INK,
              lineHeight: 1.26, opacity: readIn,
            }}>{readout}</div>

            {/* the two fusion families — the design choice, honestly named */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginTop: 4 }}>
              {families.slice(0, 2).map((f, i) => {
                const o = clamp(famIn(i), 0, 1);
                return (
                  <div key={f.name} style={{
                    display: 'flex', flexDirection: portrait ? 'column' : 'row',
                    alignItems: portrait ? 'flex-start' : 'baseline', gap: portrait ? 2 : 14,
                    opacity: o, transform: `translateY(${(1 - o) * 10}px)`,
                    borderLeft: `4px solid ${CLAUDE.BORDER}`, paddingLeft: 14,
                  }}>
                    <div style={{ fontFamily: SANS, fontSize: 30, fontWeight: 700, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{f.name}</div>
                    <div style={{ fontFamily: SANS, fontSize: 28, color: CLAUDE.INK_SOFT, lineHeight: 1.26 }}>{f.body}</div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        <div style={{
          fontFamily: SANS, fontSize: 25, color: CLAUDE.INK_SOFT, opacity: clamp(soft, 0, 1),
          flex: '0 0 auto', fontStyle: 'italic',
        }}>{honesty}</div>
      </div>
    </VqaStage>
  );
};
