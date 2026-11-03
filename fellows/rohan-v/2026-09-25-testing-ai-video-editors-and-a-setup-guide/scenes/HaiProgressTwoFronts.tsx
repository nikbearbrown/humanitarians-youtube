import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, exclusive, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';

/**
 * HaiProgressTwoFronts — B01 of "Testing AI Video Editors, and a Setup Guide
 * for New Fellows." (HAI weekly progress)
 *
 * One cause, two symptoms. A week that ran on two threads is easy to present as
 * two unrelated lists; this beat's claim is that both threads answer the SAME
 * problem. So the frame opens on the shared cause — a clock face whose hand is
 * sweeping — and only then splits into two fronts. Each front is a card with
 * its TODAY state on top and its GOAL underneath; when the narration reaches
 * "if an agent could take on the editing", the goal rows arrive and the today
 * rows go quiet (struck to ghost), so the change reads as a direction, not two
 * bullet points.
 *
 *   time        "which is time"                 the clock lands, hand sweeping
 *   editing     "built scene by scene"          front 1's TODAY row
 *   onboarding  "ask around"                    front 2's TODAY row
 *   agent       "an agent could take on…"       both GOAL rows, left then right
 *   faster      "whole team moves faster"       the spark line
 *
 * Portrait stacks the two fronts vertically under the clock (THE ONDA CHECK) —
 * the same content re-laid for a tall frame, not a crop.
 * `durationSeconds` sizes the composition to the measured narration.
 */

export const haiProgressTwoFrontsSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · WEEKLY PROGRESS'),
  title: z.string().default('Two Things Slowing the Team Down'),
  fronts: z.array(z.object({
    label: z.string(), today: z.string(), goal: z.string(),
  })).default([
    { label: 'EDITING', today: 'every tutorial built scene by scene, by hand', goal: 'an AI agent takes on the editing' },
    { label: 'ONBOARDING', today: 'new fellows ask around to get into the tools', goal: 'one written guide takes on the setup' },
  ]),
  sparkLine: z.string().default('Same problem, twice: time.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type HaiProgressTwoFrontsProps = z.infer<typeof haiProgressTwoFrontsSchema>;

export const HaiProgressTwoFronts: React.FC<HaiProgressTwoFrontsProps> = ({
  eyebrow, title, fronts, sparkLine, cues,
}) => {
  const { frame, width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;

  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CONTENT_W = width - PAD_X * 2;

  const tTime = at('time', 0.04);
  const tEdit = at('editing', 0.18);
  const tOnb = at('onboarding', 0.40);
  const tAgent = at('agent', 0.62);
  const tFast = at('faster', 0.86);

  const headIn = sp(0);
  const sClock = sp(tTime, SPRING_SNAP);
  /* SHELL, not content: both cards frame the page from the clock onward, so the
     ink's bounding box covers the safe area at every Gate V sample; the rows
     that fill them still wait for their own phrases. */
  const sShell = sp(Math.max(0, tTime - 0.02));
  const sToday = [sp(tEdit), sp(tOnb)];
  const sGoal = [sp(tAgent), sp(clamp(tAgent + 0.05, 0, 0.97))];
  const sparkIn = sp(clamp(tFast, 0, 0.97));
  const [hEdit, hOnb] = exclusive([sToday[0], sToday[1], sGoal[0]]);
  const hot = [hEdit, hOnb];

  // ── the clock: the shared cause ─────────────────────────────────────
  const CLOCK_R = (portrait ? 46 : 78) * U;
  const CLOCK_CX = PAD_X + CLOCK_R;
  const CLOCK_CY = portrait ? height * 0.252 : height * 0.30 + CLOCK_R * 0.1;
  const hand = (frame / 30) * 60 * (1 - op(sGoal[1]) * 0.85);   // slows once the goals land

  // ── the two fronts ──────────────────────────────────────────────────
  const CARD_TOP = portrait ? height * 0.297 : height * 0.425;
  const CARD_GAP = portrait ? height * 0.015 : CONTENT_W * 0.035;
  const CARD_W = portrait ? CONTENT_W : (CONTENT_W - CARD_GAP) / 2;
  const CARD_H = portrait ? height * 0.19 : height * 0.40;

  const front = (i: number) => {
    const f = fronts[i];
    if (!f) return null;
    const x = portrait ? PAD_X : PAD_X + i * (CARD_W + CARD_GAP);
    const y = portrait ? CARD_TOP + i * (CARD_H + CARD_GAP) : CARD_TOP;
    const k = op(sShell);
    const kt = op(sToday[i]);
    const kg = op(sGoal[i]);
    const lit = hot[i] > 0.3;
    const TXT = (portrait ? 36 : 40) * U;
    return (
      <div key={i} style={{
        position: 'absolute', left: x, top: y + (1 - k) * 30 * U,
        width: CARD_W, height: CARD_H, opacity: k,
        background: CLAUDE.CARD, borderRadius: 18 * U,
        border: `${lit ? 3 : 1.5}px solid ${lit ? CLAUDE.SPARK : CLAUDE.BORDER}`,
        boxShadow: '0 10px 30px rgba(61,57,41,0.07)',
        padding: `${30 * U}px ${36 * U}px`, boxSizing: 'border-box',
        display: 'flex', flexDirection: 'column', gap: (portrait ? 11 : 18) * U,
      }}>
        <div style={{
          fontFamily: HAI_TYPE.sans, fontSize: 24 * U, fontWeight: 700,
          letterSpacing: 3, color: lit ? SPARK_TEXT : CLAUDE.INK_SOFT,
        }}>
          {String(i + 1).padStart(2, '0')} · {f.label}
        </div>
        {/* TODAY */}
        <div style={{ opacity: kt, transform: `translateY(${(1 - kt) * 18 * U}px)` }}>
          <div style={{
            fontFamily: HAI_TYPE.sans, fontSize: 19 * U, fontWeight: 700,
            letterSpacing: 2, color: CLAUDE.GHOST, marginBottom: 6 * U,
          }}>TODAY</div>
          <div style={{
            fontFamily: HAI_TYPE.serif, fontSize: TXT, lineHeight: 1.22,
            color: kg > 0.5 ? CLAUDE.GHOST : CLAUDE.INK,
            textDecoration: kg > 0.5 ? 'line-through' : 'none',
            textDecorationColor: CLAUDE.SPARK, textDecorationThickness: 3 * U,
          }}>{f.today}</div>
        </div>
        {/* the arrow between them */}
        <svg width={40 * U} height={34 * U} style={{ opacity: kg, marginLeft: 4 * U }}>
          <path d={`M ${20 * U} 2 L ${20 * U} ${30 * U} M ${8 * U} ${19 * U} L ${20 * U} ${31 * U} L ${32 * U} ${19 * U}`}
            stroke={CLAUDE.SPARK} strokeWidth={4 * U} fill="none" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
        {/* GOAL */}
        <div style={{ opacity: kg, transform: `translateY(${(1 - kg) * 18 * U}px)` }}>
          <div style={{
            fontFamily: HAI_TYPE.sans, fontSize: 19 * U, fontWeight: 700,
            letterSpacing: 2, color: SPARK_TEXT, marginBottom: 6 * U,
          }}>THE GOAL</div>
          <div style={{
            fontFamily: HAI_TYPE.serif, fontSize: TXT, lineHeight: 1.22,
            fontWeight: 600, color: CLAUDE.INK,
          }}>{f.goal}</div>
        </div>
      </div>
    );
  };

  const kc = op(sClock);
  /* ── PORTRAIT (phone): PHONE type scale — less text, larger. The clock sits
     beside the title; each card holds ONE line at a time — TODAY strikes out and
     THE GOAL takes its place — so two fronts fit at phone size. Short strings
     come from the vertical sheet. */
  if (portrait) {
    const T = PHONE(height);
    const CR = 64;
    const CX = width - PAD_X - CR, CY = height * 0.125 + CR + 10;
    const CAUSE_Y = height * 0.245;
    const C_Y = CAUSE_Y + T.label * 1.5;
    const C_H = height * 0.19, C_G = height * 0.016;
    const card = (i: number) => {
      const f = fronts[i];
      if (!f) return null;
      const y = C_Y + i * (C_H + C_G);
      const kt = op(sToday[i]), kg = op(sGoal[i]);
      const lit = hot[i] > 0.3;
      return (
        <div key={i} style={{
          position: 'absolute', left: PAD_X, top: y, width: CONTENT_W, height: C_H,
          boxSizing: 'border-box', background: CLAUDE.CARD, borderRadius: 18,
          border: `${lit ? 4 : 3}px solid ${lit ? CLAUDE.SPARK : CLAUDE.GHOST}`,
          padding: '22px 30px', opacity: op(sShell),
        }}>
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1,
            color: lit || kg > 0.5 ? SPARK_TEXT : CLAUDE.INK_SOFT }}>
            {String(i + 1).padStart(2, '0')} · {kg > 0.5 ? 'THE GOAL' : f.label}
          </div>
          <div style={{ position: 'relative', marginTop: 8 }}>
            <div style={{ position: 'absolute', left: 0, top: 0, width: '100%',
              fontFamily: HAI_TYPE.serif, fontSize: T.body, lineHeight: 1.12, color: CLAUDE.INK,
              opacity: kt * (1 - kg), textDecoration: kg > 0.2 ? 'line-through' : 'none',
              textDecorationColor: CLAUDE.SPARK, textDecorationThickness: 5 }}>{f.today}</div>
            <div style={{ position: 'absolute', left: 0, top: 0, width: '100%',
              fontFamily: HAI_TYPE.serif, fontSize: T.body, lineHeight: 1.12, fontWeight: 700,
              color: CLAUDE.INK, opacity: kg, transform: `translateY(${(1 - kg) * 16}px)` }}>{f.goal}</div>
          </div>
        </div>
      );
    };
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width - CR * 2 - 20} portrait />
        <svg width={CR * 2 + 8} height={CR * 2 + 8} style={{ position: 'absolute', left: CX - CR - 4, top: CY - CR - 4, opacity: op(sClock) }}>
          <g transform={`translate(${CR + 4} ${CR + 4})`}>
            <circle r={CR} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={5} />
            <line x1={0} y1={0} x2={0} y2={-CR * 0.5} stroke={CLAUDE.INK} strokeWidth={7} strokeLinecap="round" transform={`rotate(${hand / 12})`} />
            <line x1={0} y1={0} x2={0} y2={-CR * 0.74} stroke={CLAUDE.SPARK} strokeWidth={5} strokeLinecap="round" transform={`rotate(${hand})`} />
            <circle r={8} fill={CLAUDE.SPARK} />
          </g>
        </svg>
        <div style={{ position: 'absolute', left: PAD_X, top: CAUSE_Y, opacity: op(sClock),
          fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1, color: SPARK_TEXT }}>
          SHARED CAUSE: TIME
        </div>
        {card(0)}
        {card(1)}
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
          height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn}
        padX={PAD_X} height={height} width={width} portrait={portrait} />

      {/* ══ the shared cause ═════════════════════════════════════════ */}
      <svg width={CLOCK_R * 2 + 8} height={CLOCK_R * 2 + 8} style={{
        position: 'absolute', left: CLOCK_CX - CLOCK_R - 4, top: CLOCK_CY - CLOCK_R - 4,
        opacity: kc, transform: `scale(${0.7 + 0.3 * kc})`,
      }}>
        <g transform={`translate(${CLOCK_R + 4} ${CLOCK_R + 4})`}>
          <circle r={CLOCK_R} fill={CLAUDE.CARD} stroke={CLAUDE.INK} strokeWidth={4 * U} />
          {Array.from({ length: 12 }).map((_, i) => {
            const a = (i / 12) * Math.PI * 2;
            return <line key={i} x1={Math.sin(a) * CLOCK_R * 0.78} y1={-Math.cos(a) * CLOCK_R * 0.78}
              x2={Math.sin(a) * CLOCK_R * 0.9} y2={-Math.cos(a) * CLOCK_R * 0.9}
              stroke={CLAUDE.INK_SOFT} strokeWidth={(i % 3 === 0 ? 4 : 2) * U} />;
          })}
          <line x1={0} y1={0} x2={0} y2={-CLOCK_R * 0.5} stroke={CLAUDE.INK} strokeWidth={6 * U}
            strokeLinecap="round" transform={`rotate(${hand / 12})`} />
          <line x1={0} y1={0} x2={0} y2={-CLOCK_R * 0.74} stroke={CLAUDE.SPARK} strokeWidth={4 * U}
            strokeLinecap="round" transform={`rotate(${hand})`} />
          <circle r={7 * U} fill={CLAUDE.SPARK} />
        </g>
      </svg>
      <div style={{
        position: 'absolute',
        left: CLOCK_CX + CLOCK_R + 28 * U,
        top: portrait ? CLOCK_CY - 34 * U : CLOCK_CY - 48 * U,
        width: CONTENT_W - CLOCK_R * 2 - 28 * U,
        opacity: kc,
      }}>
        <div style={{
          fontFamily: HAI_TYPE.sans, fontSize: 21 * U, fontWeight: 700,
          letterSpacing: 3, color: SPARK_TEXT,
        }}>THE SHARED CAUSE</div>
        <div style={{
          fontFamily: HAI_TYPE.serif, fontSize: (portrait ? 38 : 50) * U, fontWeight: 600,
          color: CLAUDE.INK, marginTop: 4 * U,
        }}>Time — and two places it goes.</div>
      </div>

      {front(0)}
      {front(1)}

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
        height={height} portrait={portrait}
        top={portrait ? height * 0.718 : undefined} />
    </AbsoluteFill>
  );
};
