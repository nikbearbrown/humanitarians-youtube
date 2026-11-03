import React from 'react';
import { AbsoluteFill, Img } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { SHZ, PhoneBaseline, Chip, histBars } from './shazam/shzKit';

/**
 * ShazamOffsetVote — B03 of "How Shazam Finds a Song."
 *
 * The 2003 paper's own picture: every hash the noisy clip shares with Song C, plotted as
 * (time in the clip, time in the song). Hashes that truly come from this moment of the song
 * fall on one diagonal (song time = clip time + 12.00 s); chance matches scatter. The offset rule
 * and a real matching pair from the run are typeset (typeset_math.py), and the histogram of
 * offsets (the votes) shows the spike. All points and counts are the run's.
 *
 *   search    "To search"                plot + all matching hashes
 *   chance    "by chance"                off-diagonal points named
 *   timing    "The trick is timing"      axes captions light
 *   subtract  "subtract the time"        the rule, typeset
 *   agree     "the answers agree"        worked pair + diagonal
 *   spike     "one tall spike"           offset histogram grows
 *   scattered "Chance matches are scattered"
 */

export const shazamOffsetVoteSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Let the Timing Vote'),
  sparkLine: z.string().default("A real match lines up. Chance doesn't."),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type ShazamOffsetVoteProps = z.infer<typeof shazamOffsetVoteSchema>;

export const ShazamOffsetVote: React.FC<ShazamOffsetVoteProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp, ramp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tSearch = at('search', 0.02), tChance = at('chance', 0.16), tTiming = at('timing', 0.24), tSub = at('subtract', 0.33);
  const tAgree = at('agree', 0.55), tSpike = at('spike', 0.7), tScat = at('scattered', 0.82);
  const headIn = sp(0);
  const sPlot = sp(tSearch), reveal = ramp(tSearch, tSearch + 0.1), sChance = sp(tChance), sTiming = sp(tTiming);
  const sSub = sp(tSub), sAgree = sp(tAgree), diag = ramp(tAgree, tAgree + 0.08), grow = ramp(tSpike, tSpike + 0.08), sScat = sp(tScat);
  const sparkIn = sp(clamp(tScat + 0.05, 0, 0.97));

  const winner = SHZ.ranked[0];
  const off: number = winner.offset_s;
  const pts = ((SHZ.pairs as Record<string, number[][]>)[winner.song]);
  const on = (p: number[]) => Math.abs(p[1] - p[0] - off) < 0.012;
  const nOn = pts.filter(on).length;

  const LAB = portrait ? 100 : 80 * U;
  const PW = portrait ? CW - LAB : CW * 0.5 - LAB;
  const PH = portrait ? height * 0.215 : height * 0.52;
  const PX = PAD_X + LAB, PY = portrait ? height * 0.235 : height * 0.27;
  const lbl = portrait ? T.label * 0.78 : 22 * U;
  const X = (s: number) => (s / 5) * PW, Y = (s: number) => PH - (s / 40) * PH;
  const R = portrait ? 8 : 6.5 * U;

  const plot = (
    <>
      <svg width={PW} height={PH} style={{ position: 'absolute', left: PX, top: PY, overflow: 'visible', opacity: op(sPlot) }}>
        <rect x={0} y={0} width={PW} height={PH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
        {[0, 10, 20, 30, 40].map((s) => (
          <g key={s}>
            <line x1={0} x2={PW} y1={Y(s)} y2={Y(s)} stroke={CLAUDE.BORDER} strokeWidth={1} />
            <text x={-14} y={Y(s) + lbl * 0.35} textAnchor="end" fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{s}</text>
          </g>
        ))}
        {[0, 1, 2, 3, 4, 5].map((s) => (
          <text key={s} x={X(s)} y={PH + lbl * 1.35} textAnchor={s === 0 ? 'start' : s === 5 ? 'end' : 'middle'} fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={lbl} fill={CLAUDE.INK_SOFT}>{s}</text>
        ))}
        <line x1={X(0)} y1={Y(off)} x2={X(5 * diag)} y2={Y(off + 5 * diag)} stroke={SPARK_TEXT} strokeWidth={4} opacity={0.55 * op(sAgree)} />
        {pts.map((p, i) => {
          const k = clamp(reveal * pts.length - i, 0, 1);
          const good = on(p);
          return <circle key={i} cx={X(p[0])} cy={Y(p[1])} r={R * (good ? 1 + 0.35 * op(sAgree) : 1)}
            fill={good && op(sAgree) > 0.3 ? SPARK_TEXT : CLAUDE.INK_SOFT} opacity={k * (good ? 1 : 0.55 + 0.35 * op(sChance) * (1 - op(sAgree)))} />;
        })}
      </svg>
      <div style={{ position: 'absolute', left: PX, top: PY - lbl * 1.7, opacity: op(sTiming), fontFamily: HAI_TYPE.sans, fontSize: lbl,
        fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>↑ TIME IN THE SONG (S)</div>
      <div style={{ position: 'absolute', left: PX + PW, top: PY + PH + lbl * 2.3, transform: 'translateX(-100%)', opacity: op(sTiming), fontFamily: HAI_TYPE.sans, fontSize: lbl,
        fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>TIME IN YOUR CLIP (S) →</div>
    </>
  );

  const HW = portrait ? CW : CW * 0.4, HH = portrait ? height * 0.055 : height * 0.15;
  const bars = histBars(winner.hist as number[], HW, HH, Math.max(...(winner.hist as number[])), grow);
  const hist = (
    <div style={{ opacity: op(sp(tSpike)) }}>
      <svg width={HW} height={HH} style={{ overflow: 'visible', display: 'block' }}>
        <line x1={0} x2={HW} y1={HH} y2={HH} stroke={CLAUDE.INK_SOFT} strokeWidth={2} />
        {bars.map((b, i) => <rect key={i} x={b.x} y={HH - b.h} width={b.w} height={b.h} fill={b.v === Math.max(...(winner.hist as number[])) ? SPARK_TEXT : CLAUDE.INK_SOFT} />)}
      </svg>
      <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: SPARK_TEXT, marginTop: 10 }}>
        {winner.score} VOTES AT {off.toFixed(2)} S{portrait ? '' : ' · OFFSETS FROM −2 TO 40 S'}
      </div>
    </div>
  );
  const eqH = portrait ? T.title * 1.1 : 58 * U;
  const eqs = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: portrait ? 26 : 26 * U }}>
      <div style={{ opacity: op(sSub) }}>
        <Img src={SHZ.eq.rule.src} style={{ height: eqH, width: eqH * SHZ.eq.rule.aspect, maxWidth: portrait ? CW : CW * 0.4, objectFit: 'contain', objectPosition: 'left' }} />
      </div>
      <div style={{ opacity: op(sAgree) }}>
        <div style={{ fontFamily: HAI_TYPE.sans, fontSize: lbl, fontWeight: 800, letterSpacing: 1.2, color: CLAUDE.INK_SOFT, marginBottom: 8 }}>ONE REAL MATCH</div>
        <Img src={SHZ.eq.worked.src} style={{ height: eqH * 0.9, width: eqH * 0.9 * SHZ.eq.worked.aspect, maxWidth: portrait ? CW : CW * 0.4, objectFit: 'contain', objectPosition: 'left' }} />
      </div>
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        {plot}
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.555 }}>{eqs}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.69 }}>{hist}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      {plot}
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.57, top: PY }}>{eqs}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.57, top: PY + PH - HH - 30 * U }}>{hist}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.57, top: PY + PH + 14 * U, opacity: op(sScat) }}>
        <Chip text={`${pts.length - nOn} CHANCE MATCHES, SCATTERED`} size={22 * U} />
      </div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
