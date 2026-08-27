import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {SparkLine, STAGE, clamp, remap, ease, useP} from '../illustrations/kit';

/**
 * GemmaExecSummary — the "why you are watching this" beat.
 *
 * Sits second, right after the ASK. Names the presenter, states the thesis in one
 * sentence, and lays out the three things the reel will do. That last part is an
 * advance organizer: telling a viewer the structure up front lowers the cost of
 * following it, which is the whole reason this beat exists rather than jumping
 * straight into the exhibit.
 *
 * Not a UI beat, so it does not spend the ILLUSTRATE LAW budget (UI is reserved
 * for ASK / VERDICT / HANDOFF / OUTRO).
 */

export const gemmaExecSummarySchema = z.object({
  sparkLine: z.string().default('What this is, and why.'),
  eyebrow: z.string().default('COMPUTATIONAL SKEPTICISM'),
  title: z.string().default('Gemma 4, Unified?'),
  presenter: z.string().default('with Ritik'),
  thesis: z.array(z.string()).default([
    'Google shipped a Gemma 4 that deletes the parts',
    'which let a model see and hear.',
  ]),
  roadmap: z.array(z.object({
    label: z.string(),
    body: z.string(),
  })).default([]),
  /** The roadmap cards quote real figures, so this beat carries its source too. */
  sourceNote: z.string().default(''),
});
export type GemmaExecSummaryProps = z.infer<typeof gemmaExecSummarySchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;

const COL_X = [112, 700, 1288];
const CARD_W = 520;
const CARD_Y = 566;
const CARD_H = 338;

export const GemmaExecSummary: React.FC<GemmaExecSummaryProps> = ({
  sparkLine, eyebrow, title, presenter, thesis, roadmap, sourceNote,
}) => {
  const p = useP();
  const head = ease(remap(p, 0.02, 0.13, 0, 1));
  const who = ease(remap(p, 0.08, 0.2, 0, 1));
  const th = (i: number) => ease(remap(p, 0.16 + i * 0.06, 0.32 + i * 0.06, 0, 1));
  const card = (i: number) => ease(remap(p, 0.4 + i * 0.09, 0.6 + i * 0.09, 0, 1));

  return (
    <AbsoluteFill style={{background: STAGE, overflow: 'hidden'}}>
      <svg width={1920} height={1080} style={{position: 'absolute', inset: 0}}>
        {/* eyebrow + title */}
        <g opacity={head}>
          <text x={112} y={172} fontFamily={SANS} fontSize={28} fontWeight={700} fill={CLAUDE.SPARK} letterSpacing={4}>
            {eyebrow}
          </text>
          <text x={112} y={258} fontFamily={SERIF} fontSize={78} fontWeight={700} fill={CLAUDE.INK}>
            {title}
          </text>
        </g>

        {/* presenter */}
        <g opacity={who}>
          <text x={112} y={318} fontFamily={SANS} fontSize={34} fill={CLAUDE.INK_SOFT}>
            {presenter}
          </text>
        </g>

        {/* the one-sentence thesis */}
        {thesis.map((line, i) => (
          <text
            key={i}
            x={112}
            y={412 + i * 58}
            fontFamily={SERIF}
            fontSize={46}
            fill={CLAUDE.INK}
            opacity={clamp(th(i), 0, 1)}
          >
            {line}
          </text>
        ))}

        {/* source for the figures quoted on the cards below */}
        {sourceNote ? (
          <text
            x={112}
            y={968}
            fontFamily={CLAUDE_FONT.mono}
            fontSize={26}
            fill={CLAUDE.INK_SOFT}
            opacity={clamp(card(2), 0, 1)}
          >
            {sourceNote}
          </text>
        ) : null}

        {/* what the reel does, in order */}
        {roadmap.slice(0, 3).map((r, i) => {
          const o = clamp(card(i), 0, 1);
          const x = COL_X[i];
          return (
            <g key={r.label} opacity={o}>
              <rect
                x={x}
                y={CARD_Y}
                width={CARD_W}
                height={CARD_H}
                rx={20}
                fill={CLAUDE.CARD}
                stroke={CLAUDE.BORDER}
                strokeWidth={3}
              />
              <rect x={x} y={CARD_Y} width={CARD_W} height={8} rx={4} fill={CLAUDE.SPARK} />
              <text
                x={x + 34}
                y={CARD_Y + 82}
                fontFamily={SERIF}
                fontSize={54}
                fontWeight={700}
                fill={CLAUDE.SPARK}
              >
                {i + 1}
              </text>
              <text x={x + 34} y={CARD_Y + 148} fontFamily={SANS} fontSize={31} fontWeight={700} fill={CLAUDE.INK}>
                {r.label}
              </text>
              {/* body wraps by explicit newline — SVG has no flow text */}
              {r.body.split('\n').slice(0, 4).map((ln, j) => (
                <text
                  key={j}
                  x={x + 34}
                  y={CARD_Y + 202 + j * 40}
                  fontFamily={SANS}
                  fontSize={28}
                  fill={CLAUDE.INK_SOFT}
                >
                  {ln}
                </text>
              ))}
            </g>
          );
        })}
      </svg>

      <SparkLine text={sparkLine} pos="top" />
    </AbsoluteFill>
  );
};
