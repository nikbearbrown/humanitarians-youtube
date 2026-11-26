import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, VqaStage, clamp, ease, remap, useGeo, useP } from './VqaKit';

/**
 * VqaDecide — MOVE 3. The fused sequence is pooled to one vector, a linear head scores
 * it, and softmax picks an answer from a FIXED vocabulary of the most frequent training
 * answers. That last clause is the load-bearing one: standard VQA is scored as
 * classification, not free generation, which is exactly what makes the blind test in the
 * next beat cheap to run.
 *
 * The probabilities are labelled ILLUSTRATIVE on screen — they show the shape of a
 * softmax over an answer vocabulary, never a measured model output.
 */
export const vqaDecideSchema = z.object({
  spark: z.string().default('Classification, not generation.'),
  heading: z.string().default('Move 3 — pool, then decide'),
  stages: z.array(z.string()).default(['fused sequence', 'pooled vector', 'linear head']),
  answers: z.array(z.object({ label: z.string(), prob: z.number() })).default([]),
  vocabNote: z.string().default('softmax over a FIXED answer vocabulary — the most frequent training answers'),
  honesty: z.string().default('Illustrative distribution — the mechanism, not a measured model output.'),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(12),
});
export type VqaDecideProps = z.infer<typeof vqaDecideSchema>;

export const VqaDecide: React.FC<VqaDecideProps> = ({
  spark, heading, stages, answers, vocabNote, honesty, source,
}) => {
  const p = useP();
  const { portrait } = useGeo();
  const head = ease(remap(p, 0.02, 0.12, 0, 1));
  const stage = (i: number) => ease(remap(p, 0.10 + i * 0.09, 0.26 + i * 0.09, 0, 1));
  const bar = (i: number) => ease(remap(p, 0.44 + i * 0.06, 0.68 + i * 0.06, 0, 1));
  const noteIn = ease(remap(p, 0.76, 0.92, 0, 1));

  return (
    <VqaStage spark={spark} source={source}>
      <div style={{
        flex: 1, display: 'flex', flexDirection: 'column',
        justifyContent: 'space-between', gap: portrait ? 18 : 16, minHeight: 0,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 54 : 60, fontWeight: 700, color: CLAUDE.INK,
          opacity: head, flex: '0 0 auto',
        }}>{heading}</div>

        <div style={{
          flex: '1 1 auto', minHeight: 0, display: 'flex',
          flexDirection: portrait ? 'column' : 'row', gap: portrait ? 24 : 44,
          alignItems: portrait ? 'stretch' : 'center',
        }}>
          {/* the collapse: sequence -> one vector -> a head */}
          <div style={{
            flex: '0 0 auto', display: 'flex',
            flexDirection: portrait ? 'row' : 'column',
            alignItems: 'center', justifyContent: 'center', gap: portrait ? 20 : 16,
          }}>
            {/* stage 0 — the sequence */}
            <div style={{ opacity: clamp(stage(0), 0, 1), textAlign: 'center' }}>
              <div style={{ display: 'flex', gap: 3, height: portrait ? 40 : 34, width: portrait ? 250 : 250 }}>
                {Array.from({ length: 22 }, (_, i) => (
                  <div key={i} style={{ flex: 1, borderRadius: 3, background: i < 5 ? CLAUDE.INK : CLAUDE.GHOST }} />
                ))}
              </div>
              <Tag text={stages[0] ?? ''} />
            </div>
            <Chevron o={stage(1)} portrait={portrait} />
            {/* stage 1 — pooled to one vector */}
            <div style={{ opacity: clamp(stage(1), 0, 1), textAlign: 'center' }}>
              <div style={{
                width: portrait ? 58 : 52, height: portrait ? 132 : 120, borderRadius: 8, background: CLAUDE.INK, margin: '0 auto',
              }} />
              <Tag text={stages[1] ?? ''} />
            </div>
            <Chevron o={stage(2)} portrait={portrait} />
            {/* stage 2 — the linear head */}
            <div style={{ opacity: clamp(stage(2), 0, 1), textAlign: 'center' }}>
              <div style={{
                width: portrait ? 160 : 165, height: portrait ? 80 : 74, borderRadius: 10,
                border: `3px solid ${CLAUDE.SPARK}`, background: CLAUDE.CARD,
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontFamily: MONO, fontSize: 30, color: CLAUDE.SPARK,
              }}>W · h</div>
              <Tag text={stages[2] ?? ''} />
            </div>
          </div>

          {/* the answer distribution */}
          <div style={{ flex: '1 1 auto', minWidth: 0, display: 'flex', flexDirection: 'column', gap: portrait ? 16 : 14, justifyContent: 'space-evenly' }}>
            {answers.slice(0, 5).map((a, i) => {
              const g = clamp(bar(i), 0, 1);
              const top = i === 0;
              return (
                <div key={a.label} style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
                  <div style={{
                    fontFamily: MONO, fontSize: 34, color: top ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
                    fontWeight: top ? 700 : 400, width: portrait ? 150 : 168, textAlign: 'right', flex: '0 0 auto',
                  }}>{a.label}</div>
                  <div style={{ flex: '1 1 auto', minWidth: 0, height: portrait ? 56 : 52, background: CLAUDE.PILL, borderRadius: 6, overflow: 'hidden' }}>
                    <div style={{
                      width: `${a.prob * 100 * g}%`, height: '100%', borderRadius: 6,
                      background: top ? CLAUDE.SPARK : CLAUDE.GHOST,
                    }} />
                  </div>
                  <div style={{
                    fontFamily: MONO, fontSize: 33, color: top ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
                    width: 100, flex: '0 0 auto',
                  }}>{(a.prob * g).toFixed(2)}</div>
                </div>
              );
            })}
          </div>
        </div>

        <div style={{ flex: '0 0 auto', opacity: noteIn }}>
          <div style={{ fontFamily: SANS, fontSize: portrait ? 30 : 32, color: CLAUDE.INK, lineHeight: 1.28 }}>{vocabNote}</div>
          <div style={{ fontFamily: SANS, fontSize: 25, color: CLAUDE.INK_SOFT, fontStyle: 'italic', marginTop: 6 }}>{honesty}</div>
        </div>
      </div>
    </VqaStage>
  );
};

const Tag: React.FC<{ text: string }> = ({ text }) => (
  <div style={{ fontFamily: SANS, fontSize: 25, color: CLAUDE.INK_SOFT, marginTop: 8, whiteSpace: 'nowrap' }}>{text}</div>
);

const Chevron: React.FC<{ o: number; portrait: boolean }> = ({ o, portrait }) => (
  <svg width={30} height={30} viewBox="0 0 30 30" style={{ opacity: clamp(o, 0, 1), flex: '0 0 auto' }}>
    <path d={portrait ? 'M 8 6 L 22 15 L 8 24' : 'M 6 8 L 15 22 L 24 8'}
      fill="none" stroke={CLAUDE.INK_SOFT} strokeWidth={3} strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);
