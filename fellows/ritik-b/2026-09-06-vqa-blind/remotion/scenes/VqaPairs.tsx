import React from 'react';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { MONO, SANS, SERIF, SceneGlyph, VqaStage, clamp, ease, remap, useGeo, useP } from './VqaKit';

/**
 * VqaPairs — the FIX, and the scaffold the viewer steals: for every question, find a
 * second image where the honest answer is different. A model answering from a language
 * prior can only get one of the two right, so the pair is a falsifiability test the
 * viewer can run without any new modelling.
 *
 * SIDE-BY-SIDE RULE: both images, the shared question, and both answers are on screen
 * together for the whole beat — never stated once in voiceover and gone.
 *
 * The scenes are DRAWN (REBUILD LAW): they illustrate the procedure, not the paper's
 * photographs, and say so on screen. The two paired accuracy columns ARE published and
 * carry their citation in the footer.
 */
export const vqaPairsSchema = z.object({
  spark: z.string().default('Find the mirror image.'),
  heading: z.string().default('The fix — complementary pairs'),
  question: z.string().default('Is the umbrella red?'),
  answerA: z.string().default('yes'),
  answerB: z.string().default('no'),
  procedure: z.string().default('Workers pick, from 24 nearest neighbours, an image where the answer is different. Not possible for 22% of questions.'),
  rows: z.array(z.object({
    label: z.string(),
    before: z.number(),
    after: z.number(),
  })).default([]),
  colBefore: z.string().default('unbalanced v1'),
  colAfter: z.string().default('balanced v2'),
  honesty: z.string().default('Scenes redrawn (illustrative) — the procedure, not the paper’s photographs.'),
  source: z.string().default(''),
  /** Beat length in seconds. calculateMetadata (Root.tsx) turns this into
   *  durationInFrames, and every ramp below is a fraction of p, so the scene
   *  RE-TIMES to the measured audio instead of animating early and freezing. */
  durationS: z.number().default(12),
});
export type VqaPairsProps = z.infer<typeof vqaPairsSchema>;

export const VqaPairs: React.FC<VqaPairsProps> = ({
  spark, heading, question, answerA, answerB, procedure, rows, colBefore, colAfter, honesty, source,
}) => {
  const p = useP();
  const { portrait, safe } = useGeo();
  const head = ease(remap(p, 0.02, 0.11, 0, 1));
  const aIn = ease(remap(p, 0.08, 0.20, 0, 1));
  const bIn = ease(remap(p, 0.22, 0.36, 0, 1));   // the mirror slides in
  const qIn = ease(remap(p, 0.34, 0.44, 0, 1));
  const rowIn = (i: number) => ease(remap(p, 0.54 + i * 0.10, 0.74 + i * 0.10, 0, 1));

  // FILL-THE-CANVAS: the panels are sized FROM the safe box, never a magic number.
  // Portrait puts both panels across the full safe width; landscape gives the pair the
  // left ~46% and hands the rest to the table.
  const panelW = portrait ? (safe.w - 30) / 2 : (safe.w * 0.46 - 46) / 2;
  const glyphS = panelW;

  const Panel: React.FC<{ o: number; umbrella: string; answer: string; tag: string; accent: boolean }> =
    ({ o, umbrella, answer, tag, accent }) => (
      <div style={{
        flex: '0 0 auto', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 8,
        opacity: clamp(o, 0, 1), transform: `translateY(${(1 - clamp(o, 0, 1)) * 16}px)`,
      }}>
        <div style={{ fontFamily: SANS, fontSize: 27, fontWeight: 700, letterSpacing: 3, color: CLAUDE.INK_SOFT }}>{tag}</div>
        <SceneGlyph umbrella={umbrella} w={glyphS} h={glyphS * 0.76} />
        <div style={{
          fontFamily: MONO, fontSize: 40, fontWeight: 700,
          color: accent ? CLAUDE.CARD : CLAUDE.INK, background: accent ? CLAUDE.SPARK : CLAUDE.PILL,
          border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 10, padding: '6px 26px',
        }}>{answer}</div>
      </div>
    );

  return (
    <VqaStage spark={spark} source={source}>
      <div style={{
        flex: 1, display: 'flex', flexDirection: 'column',
        justifyContent: 'space-between', gap: portrait ? 20 : 14, minHeight: 0,
      }}>
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 62 : 62, fontWeight: 700, color: CLAUDE.INK,
          opacity: head, flex: '0 0 auto', lineHeight: 1.08,
        }}>{heading}</div>

        {/* the shared question, then the two images that disagree about it */}
        <div style={{
          fontFamily: SERIF, fontSize: portrait ? 48 : 48, color: CLAUDE.INK, opacity: qIn, flex: '0 0 auto',
        }}>{question}</div>

        <div style={{
          flex: portrait ? '0 0 auto' : '1 1 auto', minHeight: 0,
          display: 'flex', alignItems: portrait ? 'flex-start' : 'center',
          justifyContent: portrait ? 'space-between' : 'flex-start', gap: portrait ? 30 : 46,
        }}>
          <Panel o={aIn} umbrella={CLAUDE.SPARK} answer={answerA} tag="IMAGE A" accent />
          <Panel o={bIn} umbrella={CLAUDE.INK} answer={answerB} tag="IMAGE B" accent={false} />

          {/* the paired-accuracy table shares the row on 16:9 */}
          {portrait ? null : (
            <div style={{ flex: '1 1 auto', minWidth: 0, display: 'flex', flexDirection: 'column', gap: 22, alignSelf: 'stretch', justifyContent: 'center' }}>
              <TableHead before={colBefore} after={colAfter} />
              {rows.slice(0, 3).map((r, i) => (
                <TableRow key={r.label} row={r} o={rowIn(i)} />
              ))}
            </div>
          )}
        </div>

        {/* on 9:16 the table takes its own band below the pair */}
        {portrait ? (
          <div style={{ flex: '1 1 auto', minHeight: 0, display: 'flex', flexDirection: 'column', gap: 20, justifyContent: 'space-evenly' }}>
            <TableHead before={colBefore} after={colAfter} />
            {rows.slice(0, 3).map((r, i) => (
              <TableRow key={r.label} row={r} o={rowIn(i)} />
            ))}
          </div>
        ) : null}

        <div style={{ flex: '0 0 auto' }}>
          <div style={{
            fontFamily: SANS, fontSize: portrait ? 31 : 31, color: CLAUDE.INK,
            opacity: clamp(rowIn(0), 0, 1), lineHeight: 1.28,
          }}>{procedure}</div>
          <div style={{
            fontFamily: SANS, fontSize: 25, color: CLAUDE.INK_SOFT, fontStyle: 'italic', marginTop: 6,
            opacity: clamp(rowIn(0), 0, 1),
          }}>{honesty}</div>
        </div>
      </div>
    </VqaStage>
  );
};

const TableHead: React.FC<{ before: string; after: string }> = ({ before, after }) => (
  <div style={{ display: 'flex', alignItems: 'baseline', gap: 14, borderBottom: `2px solid ${CLAUDE.BORDER}`, paddingBottom: 6 }}>
    <div style={{ flex: '1 1 auto', minWidth: 0 }} />
    <div style={{ width: 200, flex: '0 0 auto', fontFamily: SANS, fontSize: 27, color: CLAUDE.INK_SOFT, textAlign: 'right' }}>{before}</div>
    <div style={{ width: 200, flex: '0 0 auto', fontFamily: SANS, fontSize: 27, fontWeight: 700, color: CLAUDE.SPARK, textAlign: 'right' }}>{after}</div>
  </div>
);

const TableRow: React.FC<{ row: { label: string; before: number; after: number }; o: number }> = ({ row, o }) => {
  const g = clamp(o, 0, 1);
  const drop = row.before - row.after;
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', gap: 14, opacity: g }}>
      <div style={{ flex: '1 1 auto', minWidth: 0, fontFamily: SANS, fontSize: 32, color: CLAUDE.INK, lineHeight: 1.2 }}>
        {row.label}
      </div>
      <div style={{ width: 200, flex: '0 0 auto', fontFamily: MONO, fontSize: 36, color: CLAUDE.INK_SOFT, textAlign: 'right' }}>
        {row.before.toFixed(2)}
      </div>
      <div style={{ width: 200, flex: '0 0 auto', textAlign: 'right' }}>
        <span style={{ fontFamily: MONO, fontSize: 36, fontWeight: 700, color: CLAUDE.SPARK }}>{row.after.toFixed(2)}</span>
        <div style={{ fontFamily: MONO, fontSize: 26, color: CLAUDE.SEND }}>{`−${drop.toFixed(2)}`}</div>
      </div>
    </div>
  );
};
