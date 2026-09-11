import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { Card, SANS, SERIF, VqaStage, clamp, ease, remap, useGeo, useP } from './VqaKit';

/**
 * VqaExecSummary — beat 2, the BLUF (EXECUTIVE-SUMMARY LAW).
 *
 * States the whole idea in one breath for a smart non-technical viewer, names the
 * presenter, and lays out what the reel will do in order. The roadmap is the advance
 * organizer: the viewer holds the shape before any specific lands. Not a UI beat, so
 * it does not spend the ILLUSTRATE LAW budget.
 *
 * Responsive: roadmap cards sit in a row on 16:9 and stack down the long axis on 9:16.
 */
export const vqaExecSummarySchema = z.object({
  spark: z.string().default('What this is, and why.'),
  eyebrow: z.string().default('HUMANITARIANS AI · TRANSFORMERS'),
  title: z.string().default('Visual Question Answering, Blind?'),
  presenter: z.string().default('with Ritik'),
  thesis: z.array(z.string()).default([
    'A transformer answers questions about pictures',
    'in four moves — and the fourth one is the only',
    'reason to believe the other three.',
  ]),
  roadmap: z.array(z.object({ label: z.string(), body: z.string() })).default([]),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(12),
});
export type VqaExecSummaryProps = z.infer<typeof vqaExecSummarySchema>;

export const VqaExecSummary: React.FC<VqaExecSummaryProps> = ({
  spark, eyebrow, title, presenter, thesis, roadmap, source,
}) => {
  const p = useP();
  const { portrait } = useGeo();
  const head = ease(remap(p, 0.02, 0.13, 0, 1));
  const who = ease(remap(p, 0.09, 0.21, 0, 1));
  const th = (i: number) => ease(remap(p, 0.17 + i * 0.055, 0.33 + i * 0.055, 0, 1));
  const card = (i: number) => ease(remap(p, 0.44 + i * 0.085, 0.64 + i * 0.085, 0, 1));

  return (
    <VqaStage spark={spark} source={source}>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: portrait ? 34 : 26, minHeight: 0 }}>
        {/* eyebrow · title · presenter */}
        <div style={{ flex: '0 0 auto' }}>
          <div style={{
            fontFamily: SANS, fontSize: 28, fontWeight: 700, letterSpacing: 4,
            color: CLAUDE.SPARK, opacity: head,
          }}>{eyebrow}</div>
          <div style={{
            fontFamily: SERIF, fontSize: portrait ? 74 : 82, fontWeight: 700, color: CLAUDE.INK,
            lineHeight: 1.06, marginTop: 14, opacity: head,
          }}>{title}</div>
          <div style={{
            fontFamily: SANS, fontSize: 34, color: CLAUDE.INK_SOFT, marginTop: 12, opacity: who,
          }}>{presenter}</div>
        </div>

        {/* the one-breath thesis — one paragraph, wrapped by the box, revealed by clause */}
        <div style={{ flex: '0 0 auto', maxWidth: '100%' }}>
          <div style={{
            fontFamily: SERIF, fontSize: portrait ? 46 : 50, color: CLAUDE.INK,
            lineHeight: 1.26, opacity: clamp(th(thesis.length - 1), 0, 1),
          }}>{thesis.join(' ')}</div>
        </div>

        {/* what the reel does, in order — the advance organizer */}
        <div style={{
          flex: '1 1 auto', minHeight: 0, display: 'flex',
          flexDirection: portrait ? 'column' : 'row', gap: portrait ? 20 : 26,
        }}>
          {roadmap.slice(0, 3).map((r, i) => (
            <Card key={r.label} style={{
              flex: 1, minWidth: 0, minHeight: 0, opacity: clamp(card(i), 0, 1),
              display: 'flex', flexDirection: 'column',
              justifyContent: portrait ? 'center' : 'flex-start',
              padding: portrait ? '30px 32px' : '34px 30px 26px',
              transform: `translateY(${(1 - clamp(card(i), 0, 1)) * 18}px)`,
            }}>
              <div style={{ fontFamily: SERIF, fontSize: 52, fontWeight: 700, color: CLAUDE.SPARK, lineHeight: 1 }}>
                {i + 1}
              </div>
              <div style={{
                fontFamily: SANS, fontSize: 31, fontWeight: 700, color: CLAUDE.INK, marginTop: 12,
              }}>{r.label}</div>
              <div style={{
                fontFamily: SANS, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 10, lineHeight: 1.34,
              }}>{r.body}</div>
            </Card>
          ))}
        </div>
      </div>
    </VqaStage>
  );
};
