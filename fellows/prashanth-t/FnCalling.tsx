/**
 * FnCalling.tsx — components for the reel `llm-function-calling`
 * ("How LLM Function Calling Works", @HumanitariansAI, Plain register).
 *
 * WHY THIS FILE EXISTS
 * --------------------
 * GATE L was run before authoring (see TEMPLATE-MISSES.md). Three needs had no
 * renderable home in the library:
 *
 *  1. FnCallLoop — a FOUR-STAGE ROUND TRIP where the last stage feeds back into
 *     the first, with a payload label landing on each stage. The structural
 *     family cannot express this: `SourceFlow` is one-directional (source →
 *     destination, no return leg) and `LayerStack` is a static stack. The two
 *     closest leads, `CodingAgentsFig1Loop` and `HaiBrutalistE01Pipeline`, are
 *     reel-local with hardcoded content and only a `sparkLine` prop. This is a
 *     genuinely new SHAPE, so per the ILLUSTRATIONS.md starter-template contract
 *     it becomes its own component rather than a fork of an existing one.
 *
 *  2. FnCallPredictCard — the existing `PredictCard` is only registered as
 *     `Illu-PredictCard`, a Studio preview with sample props baked in. This is
 *     the parameterized wrapper, following the `ClaudeScienceIllu.tsx` precedent
 *     exactly (wrapper takes `sparkLine` + the component's own props).
 *
 *  3. FnCallTitleOutro — `ClaudeTitleOutro` hardcodes `@NikBearBrown` and always
 *     renders a mascot, both locked by OUTRO-LOCK.md. That lock is scoped to
 *     claude-liam / @NikBearBrown reels and states other channels have their OWN
 *     outros and never get that card, handle, or mascot. This reel is
 *     @HumanitariansAI, so it needs its own: same poster-serif title restate with
 *     the terracotta terminal period (OUTRO LAW), a parameterized handle, and no
 *     mascot and no subline.
 *
 * LAWS KEPT
 * ---------
 *  • Pure functions of the audio clock via useP() — no timers, no CSS
 *    transitions, no Math.random(). Seeking any frame renders identically.
 *  • ONE terracotta accent per beat (CLAUDE.SPARK) — the focal/active item only.
 *  • Wrapped in <IlluStage spark="…"> so SPARK-LINE LAW is satisfied.
 *  • 1280×720 stage geometry, matching the structural family. render_beat renders
 *    at --scale=2 and compile conforms to the 1920×1080 reel canvas; the scale is
 *    uniform so composition and type proportions are preserved.
 */
import React from 'react';
import { z } from 'zod';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { CLAUDE, CLAUDE_FONT } from './tokens/claude';
import { IlluStage, SERIF, SANS, MONO, clamp, remap, ease, useP } from './illustrations/kit';
import { PredictCard } from './illustrations/structural';

/* ==================================================================== *
 * FnCallLoop — the four-stage tool-use round trip.                      *
 * -------------------------------------------------------------------- *
 * WHAT: four stages on a ring, drawn in narration order, each carrying  *
 *   a title, a short sub, and an optional PAYLOAD chip. The arc from    *
 *   stage 4 back to stage 1 is the return leg — the thing that makes    *
 *   this a loop and not a pipeline.                                     *
 * WHEN: the beat enumerates the steps of a request/response cycle and   *
 *   the RETURN is part of the claim.                                    *
 * PROPS:                                                                *
 *   stages [{title, sub, payload?}]  — exactly 4; index of `active`     *
 *          gets the terracotta accent                                   *
 *   active?   which stage is focal (-1 = none, the framework pass)      *
 *   caption?  one-line clarifier under the ring                         *
 *   showPayloads?  false on the framework pass, true on the worked      *
 *          example — same figure, so the example visibly USES the       *
 *          framework (nopunt: WORKED EXAMPLE must use it, not sit       *
 *          beside it)                                                   *
 * ADAPT: change the stage list. Geometry and motion math are fixed.     *
 * ==================================================================== */
export const fnCallLoopSchema = z.object({
  /** Beat length. calculateMetadata turns this into durationInFrames so every
   *  ramp (a fraction of useP()) RE-TIMES to the beat instead of truncating at
   *  the registered length. Default matches the registered 900f/30s. */
  durationInSeconds: z.number().default(30),
  sparkLine: z.string().default('Four steps.'),
  stages: z.array(z.object({
    title: z.string(),
    sub: z.string(),
    payload: z.string().optional(),
  })).default([]),
  active: z.number().default(-1),
  caption: z.string().optional(),
  showPayloads: z.boolean().default(false),
});
export type FnCallLoopProps = z.infer<typeof fnCallLoopSchema>;

// Stage box geometry on the 1280×720 stage. Two rows of two, read left→right,
// top row then bottom row, so the return leg sweeps under the ring.
const BOX = { w: 430, h: 132 };
const SLOTS = [
  { x: 118, y: 188 }, // 1 — you describe the tools
  { x: 732, y: 188 }, // 2 — the model requests
  { x: 732, y: 388 }, // 3 — your program runs it
  { x: 118, y: 388 }, // 4 — the result goes back
];

export const FnCallLoop: React.FC<FnCallLoopProps> = ({ sparkLine, stages, active, caption, showPayloads }) => {
  const p = useP();
  const list = stages.slice(0, 4);
  return (
    <IlluStage spark={sparkLine} sparkPos="top">
      {/* connectors, drawn before the boxes so boxes sit on top */}
      <svg width={1280} height={720} style={{ position: 'absolute', left: 0, top: 0 }}>
        {[0, 1, 2, 3].map((i) => {
          // each connector appears just after its SOURCE stage has landed
          const t0 = 0.12 + i * 0.16;
          const lp = ease(remap(p, t0 + 0.07, t0 + 0.16, 0, 1));
          if (lp <= 0) return null;
          const a = SLOTS[i], b = SLOTS[(i + 1) % 4];
          const isReturn = i === 3; // stage 4 → stage 1, the return leg
          // right edge → left edge for the top leg; vertical for the sides
          let d: string;
          if (i === 0) {
            const y = a.y + BOX.h / 2;
            d = `M ${a.x + BOX.w} ${y} L ${a.x + BOX.w + (b.x - a.x - BOX.w) * lp} ${y}`;
          } else if (i === 1) {
            const x = a.x + BOX.w / 2;
            d = `M ${x} ${a.y + BOX.h} L ${x} ${a.y + BOX.h + (b.y - a.y - BOX.h) * lp}`;
          } else if (i === 2) {
            const y = a.y + BOX.h / 2;
            d = `M ${a.x} ${y} L ${a.x - (a.x - b.x - BOX.w) * lp} ${y}`;
          } else {
            const x = a.x + BOX.w / 2;
            d = `M ${x} ${a.y} L ${x} ${a.y - (a.y - b.y - BOX.h) * lp}`;
          }
          return (
            <path key={i} d={d} stroke={isReturn ? CLAUDE.SPARK : CLAUDE.INK_SOFT}
              strokeWidth={isReturn ? 5 : 3} fill="none"
              strokeDasharray={isReturn ? '10 8' : undefined} strokeLinecap="round" />
          );
        })}
      </svg>

      {list.map((s, i) => {
        const t0 = 0.12 + i * 0.16;
        const lp = ease(remap(p, t0, t0 + 0.12, 0, 1));
        if (lp <= 0) return null;
        const isActive = i === active;
        const slot = SLOTS[i];
        return (
          <div key={i} style={{
            position: 'absolute', left: slot.x, top: slot.y + (1 - lp) * 22,
            width: BOX.w, minHeight: BOX.h, opacity: lp,
            background: CLAUDE.CARD, border: `1px solid ${CLAUDE.BORDER}`,
            borderLeft: `10px solid ${isActive ? CLAUDE.SPARK : CLAUDE.INK}`,
            borderRadius: 14, padding: '16px 22px',
            boxShadow: '0 8px 24px rgba(61,57,41,0.10)',
            boxSizing: 'border-box',
          }}>
            <div style={{ display: 'flex', alignItems: 'baseline', gap: 12 }}>
              <div style={{ fontFamily: SANS, fontSize: 20, color: CLAUDE.GHOST }}>{i + 1}</div>
              <div style={{ fontFamily: SERIF, fontSize: 31, color: CLAUDE.INK, lineHeight: 1.1 }}>{s.title}</div>
            </div>
            <div style={{ fontFamily: SANS, fontSize: 18, color: CLAUDE.INK_SOFT, marginTop: 5, maxWidth: BOX.w - 60 }}>{s.sub}</div>
            {showPayloads && s.payload && (
              <div style={{
                fontFamily: MONO, fontSize: 17, color: CLAUDE.INK,
                marginTop: 9, background: CLAUDE.PILL, border: `1px solid ${CLAUDE.BORDER}`,
                borderRadius: 8, padding: '5px 10px', display: 'inline-block',
                maxWidth: BOX.w - 44, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap',
                opacity: ease(remap(p, t0 + 0.10, t0 + 0.18, 0, 1)),
              }}>{s.payload}</div>
            )}
          </div>
        );
      })}

      {caption && (
        <div style={{
          position: 'absolute', bottom: 58, left: 0, right: 0, textAlign: 'center',
          fontFamily: SANS, fontSize: 23, color: CLAUDE.INK_SOFT,
          opacity: remap(p, 0.76, 0.86, 0, 1), padding: '0 140px',
        }}>{caption}</div>
      )}
    </IlluStage>
  );
};

/* ==================================================================== *
 * FnCallPredictCard — parameterized wrapper for the library PredictCard.*
 * Follows the ClaudeScienceIllu.tsx wrapper precedent.                  *
 * ==================================================================== */
export const fnCallPredictCardSchema = z.object({
  durationInSeconds: z.number().default(30),
  sparkLine: z.string().default('Commit first.'),
  question: z.string().default(''),
  commit: z.string().default('commit to an answer before the next beat'),
});
export type FnCallPredictCardProps = z.infer<typeof fnCallPredictCardSchema>;

export const FnCallPredictCard: React.FC<FnCallPredictCardProps> = ({ sparkLine, question, commit }) => (
  <IlluStage spark={sparkLine}>
    <PredictCard question={question} commit={commit} />
  </IlluStage>
);

/* ==================================================================== *
 * FnCallTitleOutro — title-restate outro for a NON-@NikBearBrown        *
 *   channel. OUTRO-LOCK.md scopes its locked card to claude-liam /      *
 *   @NikBearBrown reels and states other channels have their own outro  *
 *   and never get that card, handle, or mascot — so this one carries a  *
 *   parameterized handle, no mascot, and no subline, while keeping      *
 *   OUTRO LAW's poster serif + terracotta terminal period.              *
 *   Polarity stays slug-seeded and deterministic.                       *
 * ==================================================================== */
export const fnCallTitleOutroSchema = z.object({
  durationInSeconds: z.number().default(10),
  title: z.string().default('⚠ SET IN BEAT SHEET'),
  handle: z.string().default('@HumanitariansAI'),
  slug: z.string().default(''),
});
export type FnCallTitleOutroProps = z.infer<typeof fnCallTitleOutroSchema>;

function seedHash(s: string): number {
  return Array.from(s || 'default').reduce((acc, c) => acc + c.charCodeAt(0), 0);
}

export const FnCallTitleOutro: React.FC<FnCallTitleOutroProps> = ({ title, handle, slug }) => {
  const frame = useCurrentFrame();
  const o = clamp(interpolate(frame, [0, 14], [0, 1]), 0, 1);

  const _pm = title.match(/^([\s\S]*?)\s*([.?!…]+)\s*$/);
  const titleBody = _pm ? _pm[1] : title;
  const titlePunct = _pm ? _pm[2] : '.';

  const seed = seedHash(slug || title);
  const isDark = seed % 2 === 1;
  const bg = isDark ? CLAUDE.INK : CLAUDE.PAGE;
  const fg = isDark ? CLAUDE.PAGE : CLAUDE.INK;
  const fgSend = isDark ? CLAUDE.PAGE : CLAUDE.SEND;

  return (
    <AbsoluteFill style={{
      background: bg, alignItems: 'center', justifyContent: 'center',
      flexDirection: 'column', opacity: o,
    }}>
      {/* QC fill anchors, same placement as ClaudeTitleOutro */}
      <div style={{ position: 'absolute', left: 96, top: 54, width: 3, height: 3, background: '#D4D4D4' }} />
      <div style={{ position: 'absolute', right: 96, bottom: 123, width: 3, height: 3, background: '#D4D4D4' }} />

      <div style={{
        fontFamily: CLAUDE_FONT.serif, fontWeight: 700, fontSize: 72, color: fg,
        letterSpacing: '-0.02em', textAlign: 'center', lineHeight: 1.08,
        maxWidth: 1080, padding: '0 60px',
      }}>
        {titleBody}
        <span style={{ color: fgSend }}>{titlePunct}</span>
      </div>

      <div style={{
        fontFamily: CLAUDE_FONT.serif, fontSize: 52, color: fg,
        marginTop: 28, opacity: 0.9,
      }}>{handle}</div>

      {/* NO mascot, NO subline — this is not the @NikBearBrown locked card. */}
    </AbsoluteFill>
  );
};
