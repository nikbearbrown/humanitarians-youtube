import React from 'react';
import { AbsoluteFill, Img } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import {
  useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPRING_SNAP, SPARK_TEXT, PHONE,
} from '../lib/cueKit';
import { TOY } from './diffusion/toyData';
import { PixelTile, forwardMix, px, ABAR } from './diffusion/diffusionKit';

/**
 * DiffuseMixEquation — B03 of "How AI Image Generators Turn Noise Into a Picture."
 *
 * The one equation the reel needs, typeset properly (MATH-TYPESETTING.md): the
 * rows are outlined SVG from runtime/scripts/typeset_math.py — structured
 * radicals, bars and subscripts, never a text string. Each bracket beneath the
 * equation is placed on its term's MEASURED span (export_toy_data.py measures
 * every prefix with matplotlib's MathText parser), so "part picture" points at
 * exactly √ᾱ_t·x₀ and "part noise" at exactly √(1−ᾱ_t)·ε.
 *
 *   rule      "rule for adding the noise"   the equation lands; x_t is named
 *   parts     "part picture, plus part…"    the two term brackets, ink then spark
 *   shrinks   "picture's share shrinks"     live readout: step 0 → 1000, both shares
 *   thousand  "By step one thousand"        √ᾱ₁₀₀₀ ≈ 0.0064, "under one percent"
 *   question  "just one question"           the training loss row
 *
 * The numbers are the model's own schedule (ABAR, computed exactly as trained).
 * Portrait stacks every row full-width inside the safe band.
 */

export const diffuseMixEquationSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AI CONCEPTS'),
  title: z.string().default('Part Picture, Part Noise'),
  termLabels: z.array(z.string()).default(['the noisy picture', 'part picture', 'part noise']),
  endLabel: z.string().default('less than one percent of the picture is left'),
  lossLabel: z.string().default('TRAINING: guess the noise ε, get scored on how far off you were'),
  sparkLine: z.string().default('Training asks one question: which part is the noise?'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type DiffuseMixEquationProps = z.infer<typeof diffuseMixEquationSchema>;

export const DiffuseMixEquation: React.FC<DiffuseMixEquationProps> = ({
  eyebrow, title, termLabels, endLabel, lossLabel, sparkLine, cues,
}) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CONTENT_W = width - PAD_X * 2;

  const tRule = at('rule', 0.03);
  const tParts = at('parts', 0.2);
  const tShr = at('shrinks', 0.4);
  const tThou = at('thousand', 0.6);
  const tQ = at('question', 0.86);

  const headIn = sp(0);
  const sEq = sp(tRule);
  const sLab = [sp(clamp(tRule + 0.05, 0, 0.97)), sp(tParts), sp(clamp(tParts + 0.07, 0, 0.97))];
  /* SHELL: the readout sits at step 0 (all picture) from the equation's arrival,
     so the lower half is never empty at a Gate V sample; it starts moving on
     "picture's share shrinks". */
  const sLive = sp(Math.max(0, tRule + 0.02));
  const sEnd = sp(tThou, SPRING_SNAP);
  const sLoss = sp(tQ, SPRING_SNAP);
  const sparkIn = sp(clamp(tQ + 0.05, 0, 0.97));

  const step = Math.round(1000 * ramp(tShr, tThou));
  const pic = Math.sqrt(ABAR[step]);
  const noi = Math.sqrt(1 - ABAR[step]);
  const x0 = px(TOY.x0);
  const eps = TOY.eps as unknown as number[];

  const { mix, end, loss, spans } = TOY.eq;

  // ── layout ──────────────────────────────────────────────────────────
  const EQ_W = portrait ? CONTENT_W : CONTENT_W * 0.9;   // Gate V: at 0.66 the 50% frame filled only 44% of the safe area
  const EQ_H = EQ_W / mix.aspect;
  const EQ_X = PAD_X;
  const EQ_Y = portrait ? height * 0.25 : height * 0.265;
  const BR_Y = EQ_Y + EQ_H + 14 * U;

  const LIVE_Y = BR_Y + (portrait ? 150 : 104) * U;
  const TILE = (portrait ? 190 : 200) * U;

  const colours = [CLAUDE.INK_SOFT, CLAUDE.INK, SPARK_TEXT];   // bracket labels are text

  const bracket = (i: number) => {
    const [a, b] = spans[i];
    const x = EQ_X + a * EQ_W, w = (b - a) * EQ_W;
    const k = op(sLab[i]);
    const LW = Math.max(w + 120 * U, 340 * U);
    return (
      <div key={i} style={{ position: 'absolute', left: x, top: BR_Y, width: w, opacity: k }}>
        <svg width={w} height={22 * U} style={{ display: 'block', overflow: 'visible' }}>
          <path d={`M 2 2 L 2 ${12 * U} L ${w - 2} ${12 * U} L ${w - 2} 2`}
            fill="none" stroke={colours[i]} strokeWidth={4 * U}
            strokeDasharray={w * 2} strokeDashoffset={w * 2 * (1 - k)} />
        </svg>
        <div style={{
          position: 'absolute', left: i === 0 ? 0 : (w - LW) / 2, width: LW,
          textAlign: i === 0 ? 'left' : 'center',
          top: (portrait && i === 0 ? 70 : 26) * U,   // portrait: x_t is too narrow to share a line with its neighbour's label
          fontFamily: HAI_TYPE.serif, fontStyle: i === 0 ? 'italic' : 'normal',
          fontWeight: i === 0 ? 400 : 700, fontSize: (portrait ? 30 : 33) * U, color: colours[i],
        }}>{termLabels[i]}</div>
      </div>
    );
  };

  const shareBar = (label: string, v: number, colour: string) => (
    <div style={{ marginBottom: 16 * U }}>
      <div style={{
        display: 'flex', justifyContent: 'space-between',
        fontFamily: HAI_TYPE.sans, fontSize: 19 * U, fontWeight: 700, letterSpacing: 1.6,
        color: CLAUDE.INK_SOFT, marginBottom: 6 * U,
      }}>
        <span>{label}</span>
        <span style={{ fontFamily: HAI_TYPE.mono, color: colour }}>{v.toFixed(4)}</span>
      </div>
      <div style={{ height: 14 * U, background: CLAUDE.FOOTER, borderRadius: 7 * U }}>
        <div style={{ width: `${v * 100}%`, height: '100%', background: colour, borderRadius: 7 * U }} />
      </div>
    </div>
  );

  const END_H = (portrait ? 58 : 64) * U;
  const LOSS_H = (portrait ? 66 : 72) * U;
  const ROW2_X = portrait ? PAD_X : PAD_X + TILE + CONTENT_W * 0.42;
  const ROW2_W = portrait ? CONTENT_W : CONTENT_W - (ROW2_X - PAD_X);
  const END_Y = portrait ? LIVE_Y + TILE + 36 * U : LIVE_Y;
  const LOSS_Y = portrait ? END_Y + END_H + 80 * U : LIVE_Y + END_H + 90 * U;

  /* ── PORTRAIT (phone): PHONE type scale — less text, larger. Short all-caps term
     labels (from the vertical sheet), the live readout, then ONE slot that shows
     the step-1000 note and is taken over by the training question on its cue. */
  if (portrait) {
    const T = PHONE(height);
    const pEQ_W = CONTENT_W, pEQ_H = pEQ_W / mix.aspect;
    const pEQ_Y = height * 0.245;
    const pBR_Y = pEQ_Y + pEQ_H + 12;
    const pLIVE_Y = pBR_Y + T.label * 2.9 + 26;
    const pTILE = CONTENT_W * 0.24;
    const SLOT_Y = pLIVE_Y + Math.max(pTILE, T.label * 1.25 * 3 + 60) + height * 0.02;   // the readout column is taller than the tile
    const kEnd = op(sEnd) * (1 - op(sLoss)), kLoss = op(sLoss);
    const pColours = [CLAUDE.INK_SOFT, CLAUDE.INK, SPARK_TEXT];
    const readout = (label: string, v: number, colour: string) => (
      <div style={{ marginBottom: 12 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
          <span style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 700, letterSpacing: 1, color: CLAUDE.INK_SOFT }}>{label}</span>
          <span style={{ fontFamily: HAI_TYPE.mono, fontSize: T.label, fontWeight: 700, color: colour }}>{v.toFixed(4)}</span>
        </div>
        <div style={{ height: 14, background: CLAUDE.FOOTER, borderRadius: 7, marginTop: 4 }}>
          <div style={{ width: `${v * 100}%`, height: '100%', background: colour === SPARK_TEXT ? CLAUDE.SPARK : colour, borderRadius: 7 }} />
        </div>
      </div>
    );
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title}
          padX={PAD_X} height={height} width={width} portrait />
        <Img src={mix.src} alt={mix.expression} style={{
          position: 'absolute', left: PAD_X, top: pEQ_Y, width: pEQ_W, height: pEQ_H,
          opacity: op(sEq), transform: `translateY(${(1 - op(sEq)) * 16}px)`,
        }} />
        {[0, 1, 2].map(i => {
          const [a, b] = spans[i];
          const x = PAD_X + a * pEQ_W, w = (b - a) * pEQ_W;
          const k = op(sLab[i]);
          const LW = Math.max(w, T.label * 5);
          return (
            <div key={i} style={{ position: 'absolute', left: x, top: pBR_Y, width: w, opacity: k }}>
              <svg width={w} height={44} style={{ display: 'block', overflow: 'visible' }}>
                <path d={`M 2 2 L 2 40 L ${w - 2} 40 L ${w - 2} 2`} fill="none" stroke={pColours[i]} strokeWidth={5} />   {/* text-safe tone: at phone size GATE T reads a tall spark bracket as type */}
              </svg>
              <div style={{
                position: 'absolute', left: i === 0 ? 0 : (w - LW) / 2, width: LW,
                textAlign: i === 0 ? 'left' : 'center', top: i === 0 ? T.label * 1.35 + 46 : 46,
                fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1,
                color: pColours[i], whiteSpace: 'nowrap',
              }}>{termLabels[i]}</div>
            </div>
          );
        })}
        <div style={{ position: 'absolute', left: PAD_X, top: pLIVE_Y, width: CONTENT_W,
          display: 'flex', gap: 28, alignItems: 'center', opacity: op(sLive) }}>
          <div style={{ flexShrink: 0 }}>
            <PixelTile a={forwardMix(x0, eps, step)} size={pTILE} radius={10} />
          </div>
          <div style={{ flex: 1 }}>
            <div style={{ fontFamily: HAI_TYPE.mono, fontSize: T.label, fontWeight: 700, color: CLAUDE.INK, marginBottom: 6 }}>step {step}</div>
            {readout('PICTURE', pic, CLAUDE.INK)}
            {readout('NOISE', noi, SPARK_TEXT)}
          </div>
        </div>
        {/* SHELL: the slot the step-1000 note and the training question will take (Gate V fill) */}
        <div style={{ position: 'absolute', left: PAD_X, top: SLOT_Y - 12, width: CONTENT_W, height: height * 0.13,
          boxSizing: 'border-box', borderRadius: 14, border: `3px dashed ${CLAUDE.GHOST}`,
          opacity: op(sLive) * (1 - Math.max(op(sEnd), op(sLoss))) }} />
        <div style={{ position: 'absolute', left: PAD_X, top: SLOT_Y, width: CONTENT_W, opacity: kEnd }}>
          <Img src={end.src} alt={end.expression} style={{ height: T.body * 0.95, width: T.body * 0.95 * end.aspect }} />
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1, color: SPARK_TEXT, marginTop: 8 }}>{endLabel}</div>
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: SLOT_Y, width: CONTENT_W, opacity: kLoss }}>
          <Img src={loss.src} alt={loss.expression} style={{ height: T.body * 1.05, width: T.body * 1.05 * loss.aspect }} />
          <div style={{ fontFamily: HAI_TYPE.sans, fontSize: T.label, fontWeight: 800, letterSpacing: 1, color: CLAUDE.INK_SOFT, marginTop: 8 }}>{lossLabel}</div>
        </div>
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
          height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }

  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn}
        padX={PAD_X} height={height} width={width} portrait={portrait} />

      {/* ══ the equation ═════════════════════════════════════════════ */}
      <Img src={mix.src} alt={mix.expression} style={{
        position: 'absolute', left: EQ_X, top: EQ_Y, width: EQ_W, height: EQ_H,
        opacity: op(sEq), transform: `translateY(${(1 - op(sEq)) * 16 * U}px)`,
      }} />
      {[0, 1, 2].map(bracket)}

      {/* ══ the shares, live ═════════════════════════════════════════ */}
      <div style={{
        position: 'absolute', left: PAD_X, top: LIVE_Y, opacity: op(sLive),
        display: 'flex', gap: 30 * U, alignItems: 'center',
        width: portrait ? CONTENT_W : TILE + CONTENT_W * 0.38,
      }}>
        <div style={{ flexShrink: 0 }}>
          <PixelTile a={forwardMix(x0, eps, step)} size={TILE} radius={10 * U} />
          <div style={{
            fontFamily: HAI_TYPE.mono, fontSize: 20 * U, fontWeight: 700, color: CLAUDE.INK,
            marginTop: 8 * U, textAlign: 'center',
          }}>step {step}</div>
        </div>
        <div style={{ flex: 1 }}>
          {shareBar("PICTURE'S SHARE", pic, CLAUDE.INK)}
          {shareBar("NOISE'S SHARE", noi, SPARK_TEXT)}
        </div>
      </div>

      {/* ══ step one thousand ════════════════════════════════════════ */}
      <div style={{
        position: 'absolute', left: ROW2_X, top: END_Y, width: ROW2_W, opacity: op(sEnd),
        transform: `translateX(${(1 - op(sEnd)) * 24 * U}px)`,
      }}>
        <Img src={end.src} alt={end.expression} style={{ height: END_H, width: END_H * end.aspect }} />
        <div style={{
          fontFamily: HAI_TYPE.serif, fontSize: (portrait ? 30 : 32) * U, color: SPARK_TEXT,
          fontWeight: 600, marginTop: 8 * U,
        }}>{endLabel}</div>
      </div>

      {/* ══ the training question ════════════════════════════════════ */}
      <div style={{
        position: 'absolute', left: ROW2_X, top: LOSS_Y, width: ROW2_W, opacity: op(sLoss),
        transform: `translateX(${(1 - op(sLoss)) * 24 * U}px)`,
      }}>
        <Img src={loss.src} alt={loss.expression} style={{ height: LOSS_H, width: LOSS_H * loss.aspect }} />
        <div style={{
          fontFamily: HAI_TYPE.sans, fontSize: (portrait ? 19 : 20) * U, fontWeight: 700,
          letterSpacing: 1.2, color: CLAUDE.INK_SOFT, marginTop: 8 * U, lineHeight: 1.4,
        }}>{lossLabel}</div>
      </div>

      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width}
        height={height} portrait={portrait}
        top={portrait ? height * 0.722 : undefined} />
    </AbsoluteFill>
  );
};
