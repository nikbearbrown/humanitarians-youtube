/**
 * SqlPredictCard — the commit-before-the-reveal card for this reel (B05).
 *
 * WHAT      A thin props wrapper over the library `PredictCard`, seated on the
 *           library `IlluStage` so SPARK-LINE LAW is satisfied by the stage.
 * WHEN      A beat that asks the viewer to commit to an answer before the next
 *           beat reveals it.
 * ADAPTED-FROM
 *           runtime/remotion/src/illustrations/structural.tsx  (PredictCard)
 *           runtime/remotion/src/illustrations/kit.tsx          (IlluStage)
 *
 * WHY THIS FILE EXISTS: `PredictCard` is only registered in Root.tsx as
 * `Illu-PredictCard`, whose props are BAKED INTO the preview wrapper
 * (illustrations/previews.tsx) and cannot be set per beat. ILLUSTRATIONS.md is
 * explicit that this is the intended path — "copy the props block into a real
 * reel and edit the data" — so this is a props adaptation, not a new pattern.
 * The motion math is untouched, per the starter-template contract.
 * Logged in brutalist.art/TEMPLATE-MISSES.md #2.
 *
 * REEL-LOCAL. Register per remotion-src/REGISTER.md before rendering.
 */
import React from 'react';
import { AbsoluteFill, useVideoConfig } from 'remotion';
import { z } from 'zod';
import { IlluStage } from '../illustrations/kit';
import { PredictCard } from '../illustrations/structural';
import { HandleChip } from './ClaudeCodeBeat';

export const sqlPredictCardSchema = z.object({
  /** Overlaid spark line. Top by default; the card owns the centre. */
  sparkLine: z.string().default('Commit before the reveal.'),
  question: z.string(),
  commit: z.string().default('commit — the answer is one beat away'),
  /** FILL-THE-CANVAS: grows the question block about the frame centre. Omitted → 1
   *  (the legacy render). The library card's motion math is untouched. */
  scale: z.number().min(0.5).max(2.5).optional(),
  /** Moves the question block down by this fraction of the frame height (the library
   *  card seats it in the upper half). Omitted → 0. */
  shiftY: z.number().min(-0.5).max(0.5).optional(),
  /** Lower-right author handle chip (e.g. "Supriya"). Omitted → no chip. */
  handle: z.string().optional(),
});
export type SqlPredictCardProps = z.infer<typeof sqlPredictCardSchema>;

export const SqlPredictCard: React.FC<SqlPredictCardProps> = ({
  sparkLine, question, commit, scale, shiftY, handle,
}) => {
  const { width: W, height: H } = useVideoConfig();
  const k = scale ?? 1;
  const dy = (shiftY ?? 0) * 100;
  const tf = [dy ? `translateY(${dy}%)` : '', k !== 1 ? `scale(${k})` : ''].filter(Boolean).join(' ');
  return (
    <AbsoluteFill>
      <IlluStage spark={sparkLine} sparkPos="top">
        <AbsoluteFill style={{ transform: tf || undefined, transformOrigin: '50% 50%' }}>
          <PredictCard question={question} commit={commit} />
        </AbsoluteFill>
      </IlluStage>
      <HandleChip handle={handle} fontSize={H * (H > W ? 0.016 : 0.024)} right={W * 0.07}
        bottom={H * (H > W ? 0.06 : 0.055)} opacity={0.9} />
    </AbsoluteFill>
  );
};
