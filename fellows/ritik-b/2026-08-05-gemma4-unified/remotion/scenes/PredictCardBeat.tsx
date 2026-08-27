import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {PredictCard} from '../illustrations/structural';
import {SparkLine, STAGE, clamp, remap, ease, useP} from '../illustrations/kit';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';

/**
 * PredictCardBeat — the beat-sheet-facing composition for the PredictCard
 * illustration (registered as pattern id "PredictCard").
 *
 * The illustration library draws in 1280×720 stage units (see
 * illustrations/kit.tsx); this wrapper scales that stage onto the 1920×1080
 * reel canvas and adds the SPARK-LINE-LAW chrome on top. Pure function of the
 * beat clock via useP() inside the components — no timers, no state.
 *
 * 2026-08 (gemma4-unified): added `eyebrow` and `options`, both defaulting to
 * empty so existing reels render byte-identically.
 *
 * WHY: PredictCard alone leaves the lower third of the 16:9 canvas empty and
 * measured 47–52% of title-safe — a GATE V underfill MAJOR. It also has a hard
 * layout budget: the question sits at stage y=250 at 62px/1.2 line-height inside
 * 1000px, and the terracotta rule is fixed at y=450, so anything past TWO lines
 * collides with the rule. `options` fills the dead space with the thing a
 * prediction beat actually needs — something to commit TO — and the eyebrow
 * names the move. Keep `question` to ~55 characters.
 */
export const predictCardBeatSchema = z.object({
  sparkLine: z.string().default('Commit before the reveal.'),
  question: z.string().default("What's the most likely failure mode?"),
  commit: z.string().default('commit to an answer before the next beat'),
  /** Small caps label above the question. Empty = omitted. */
  eyebrow: z.string().default(''),
  /** Answer chips the viewer picks between. Empty = omitted. 2–3 read best. */
  options: z.array(z.string()).default([]),
});
export type PredictCardBeatProps = z.infer<typeof predictCardBeatSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

export const PredictCardBeat: React.FC<PredictCardBeatProps> = ({
  sparkLine, question, commit, eyebrow, options,
}) => {
  const p = useP();
  const eo = ease(remap(p, 0.04, 0.14, 0, 1));
  // Chips land BEFORE the commit line (co peaks at p=0.65 inside PredictCard):
  // question (0.05–0.15) → options (0.26–0.45) → rule → "say it out loud". The
  // viewer needs to see what they are choosing between while the question is
  // still being asked, not after being told to answer. This also keeps the frame
  // full across the whole beat — at 0.62 the mid-beat frame had no chips yet and
  // GATE V read it as a 53% underfill.
  const chipIn = (i: number) => ease(remap(p, 0.26 + i * 0.07, 0.45 + i * 0.07, 0, 1));

  return (
    <AbsoluteFill style={{background: STAGE, overflow: 'hidden'}}>
      {eyebrow ? (
        <div style={{
          position: 'absolute', top: 176, left: 0, right: 0, textAlign: 'center',
          fontFamily: SANS, fontSize: 30, fontWeight: 700, letterSpacing: 4,
          color: CLAUDE.SPARK, opacity: eo,
        }}>
          {eyebrow}
        </div>
      ) : null}

      <div style={{position: 'absolute', width: 1280, height: 720, transform: 'scale(1.5)', transformOrigin: 'top left'}}>
        <PredictCard question={question} commit={commit} />
      </div>

      {options.length ? (
        <div style={{
          position: 'absolute', left: 160, right: 160, bottom: 108,
          display: 'flex', justifyContent: 'center', gap: 40,
        }}>
          {options.map((o, i) => (
            <div key={o} style={{
              flex: 1, maxWidth: 520,
              border: `4px solid ${CLAUDE.INK}`, borderRadius: 18,
              background: CLAUDE.CARD,
              padding: '30px 24px', textAlign: 'center',
              fontFamily: SERIF, fontSize: 52, fontWeight: 700, color: CLAUDE.INK,
              opacity: clamp(chipIn(i), 0, 1),
              transform: `translateY(${(1 - clamp(chipIn(i), 0, 1)) * 16}px)`,
            }}>
              {o}
            </div>
          ))}
        </div>
      ) : null}

      <SparkLine text={sparkLine} pos="top" />
    </AbsoluteFill>
  );
};
