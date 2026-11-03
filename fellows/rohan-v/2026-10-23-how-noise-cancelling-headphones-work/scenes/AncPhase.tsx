import React from 'react';
import { AbsoluteFill, Img } from 'remotion';
import { z } from 'zod';
import { CLAUDE } from '../tokens/claude';
import { useChoreo, op, clamp, BeatHead, SparkLine, HAI_TYPE, SPARK_TEXT, PHONE } from '../lib/cueKit';
import { ANC, PhoneBaseline, Caps, Stat, Chip } from './anc/ancKit';

/**
 * AncPhase — B03 of "How Noise-Cancelling Headphones Work."
 *
 * The timing-error rule, on two tones and one fixed error of 0.1 ms (anc.py's check): each panel draws the
 * tone (ink), the anti-noise arriving 0.1 ms late (terracotta, dashed), and what is left (ink, bold). At
 * 100 Hz the error is 3.6° and the sum nearly vanishes (−24 dB); at 2 kHz it is 72° and the sum is LOUDER
 * than the tone (+1.4 dB). The rule and both worked cases are typeset (typeset_math.py).
 *
 *   late / error / hundred / drops / two / adds / sixty
 */

export const ancPhaseSchema = z.object({
  eyebrow: z.string().default('HUMANITARIANS AI · AUDIO CONCEPTS'),
  title: z.string().default('Late Matters More at High Pitch'),
  sparkLine: z.string().default('Same delay, bigger mistake at high pitch.'),
  durationSeconds: z.number().optional(),
  cues: z.record(z.string(), z.number()).optional(),
});
export type AncPhaseProps = z.infer<typeof ancPhaseSchema>;

const TAU = 1e-4;

export const AncPhase: React.FC<AncPhaseProps> = ({ eyebrow, title, sparkLine, cues }) => {
  const { width, height, at, sp } = useChoreo(cues);
  const portrait = height > width;
  const U = portrait ? width / 1080 : height / 1080;
  const PAD_X = width * (portrait ? 0.067 : 0.065);
  const CW = width - PAD_X * 2;
  const T = PHONE(height);

  const tLate = at('late', 0.0), tErr = at('error', 0.1), tHund = at('hundred', 0.22), tDrops = at('drops', 0.35);
  const tTwo = at('two', 0.5), tAdds = at('adds', 0.68), tSixty = at('sixty', 0.85);
  const headIn = sp(0);
  const sRule = sp(tErr), s1 = sp(tHund), sD1 = sp(tDrops), s2 = sp(tTwo), sD2 = sp(tAdds), sSixty = sp(Math.min(tSixty, 0.88));
  const sparkIn = sp(clamp(Math.min(tSixty + 0.04, 0.9), 0, 0.9));
  const lbl = portrait ? T.label * 0.8 : 22 * U;
  const rule = Object.fromEntries((ANC.rule as any[]).map((r) => [r.hz, r]));
  const EQ = ANC.eq as Record<string, { src: string; aspect: number }>;

  const PW = portrait ? CW : CW * 0.42, PH = portrait ? height * 0.085 : height * 0.17;
  const panel = (f: number, cycles: number, o: number, oResid: number) => {
    // draw `cycles` periods; the late copy is shifted by the real phase error
    const N = 240, phi = 2 * Math.PI * f * TAU;
    const pts = (fn: (a: number) => number) => 'M' + Array.from({ length: N + 1 }, (_, i) => {
      const a = (i / N) * cycles * 2 * Math.PI;
      return `${((i / N) * PW).toFixed(1)},${(PH / 2 - fn(a) * PH * 0.3).toFixed(1)}`;
    }).join(' L');
    return (
      <svg width={PW} height={PH} style={{ display: 'block', overflow: 'visible', opacity: o }}>
        <rect x={0} y={0} width={PW} height={PH} fill={CLAUDE.CARD} stroke={CLAUDE.BORDER} strokeWidth={1.5} />
        <path d={pts((a) => Math.sin(a))} fill="none" stroke={CLAUDE.GHOST} strokeWidth={portrait ? 4 : 3 * U} />
        <path d={pts((a) => -Math.sin(a - phi))} fill="none" stroke={SPARK_TEXT} strokeWidth={portrait ? 4 : 3 * U} strokeDasharray="10 8" />
        <path d={pts((a) => Math.sin(a) - Math.sin(a - phi))} fill="none" stroke={CLAUDE.INK} strokeWidth={portrait ? 7 : 6 * U} opacity={oResid} />
      </svg>
    );
  };
  const big = portrait ? T.title * 0.95 : 60 * U;
  const block = (f: number, o: number, oR: number, label: string, eq: { src: string; aspect: number }, accent: boolean) => (
    <div style={{ opacity: o }}>
      <Caps size={lbl} color={CLAUDE.INK} style={{ marginBottom: 8 }}>{label}</Caps>
      {panel(f, 2, 1, oR)}
      <div style={{ display: 'flex', alignItems: 'center', gap: portrait ? 26 : 26 * U, marginTop: portrait ? 12 : 12 * U }}>
        {!portrait ? <Img src={eq.src} style={{ height: 44 * U, width: Math.min(PW * 0.62, 44 * U * eq.aspect), objectFit: 'contain', objectPosition: 'left' }} /> : null}
        <Stat value={`${rule[f].db > 0 ? '+' : ''}${rule[f].db.toFixed(1)} dB`} label={portrait ? `${rule[f].phase_deg}° OFF` : 'LEFT OVER'} size={big} opacity={oR} accent={accent} />
      </div>
    </div>
  );
  const swatch = (c: string, dashed = false) => <span style={{ display: 'inline-block', width: portrait ? 56 : 44 * U, height: 0, borderTop: `${portrait ? 6 : 5 * U}px ${dashed ? 'dashed' : 'solid'} ${c}`, marginRight: 12, verticalAlign: 'middle' }} />;
  const legend = (
    <div style={{ display: 'flex', gap: portrait ? 44 : lbl * 1.1, opacity: op(s1) }}>
      <Caps size={lbl * 0.9} color={CLAUDE.INK_SOFT}>{swatch(CLAUDE.GHOST)}TONE</Caps>
      <Caps size={lbl * 0.9} color={SPARK_TEXT}>{swatch(SPARK_TEXT, true)}{portrait ? 'ANTI-NOISE' : 'ANTI-NOISE, 0.1 MS LATE'}</Caps>
      <Caps size={lbl * 0.9} color={CLAUDE.INK}>{swatch(CLAUDE.INK)}{portrait ? 'LEFT' : 'LEFT OVER'}</Caps>
    </div>
  );
  const sixty = <div style={{ opacity: op(sSixty) }}><Chip text={portrait ? 'PAST 60°: NO CANCELLING' : `PAST 60°: NO CANCELLATION (ABOVE ${(ANC.f60 as number).toLocaleString('en-US')} HZ FOR 0.1 MS)`} size={portrait ? T.label * 0.74 : 22 * U} accent /></div>;
  const rules = (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 14 * U, opacity: op(sRule) }}>
      <Img src={EQ.phase.src} style={{ height: 52 * U, width: Math.min(CW * 0.4, 52 * U * EQ.phase.aspect), objectFit: 'contain', objectPosition: 'left' }} />
      <Img src={EQ.resid.src} style={{ height: 52 * U, width: Math.min(CW * 0.4, 52 * U * EQ.resid.aspect), objectFit: 'contain', objectPosition: 'left' }} />
    </div>
  );

  if (portrait) {
    return (
      <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
        <BeatHead eyebrow="" title={title} inOp={headIn} titleSize={T.title} padX={PAD_X} height={height} width={width} portrait />
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.205, display: 'flex', flexDirection: 'column', gap: height * 0.022 }}>
          {block(100, op(s1), op(sD1), '100 HZ, 0.1 MS LATE', EQ.w100, false)}
          {block(2000, op(s2), op(sD2), '2,000 HZ, 0.1 MS LATE', EQ.w2k, true)}
        </div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.655 }}>{legend}</div>
        <div style={{ position: 'absolute', left: PAD_X, top: height * 0.715 }}>{sixty}</div>
        <PhoneBaseline padX={PAD_X} width={width} height={height} inOp={headIn} />
        <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} portrait top={height * 0.8} fontSize={T.spark * 1.25} />
      </AbsoluteFill>
    );
  }
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, overflow: 'hidden' }}>
      <BeatHead eyebrow={eyebrow} title={title} inOp={headIn} padX={PAD_X} height={height} width={width} />
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.25, display: 'flex', gap: CW * 0.08 }}>
        {block(100, op(s1), op(sD1), 'A 100 HZ HUM, ANTI-NOISE 0.1 MS LATE', EQ.w100, false)}
        {block(2000, op(s2), op(sD2), 'A 2,000 HZ TONE, THE SAME 0.1 MS', EQ.w2k, true)}
      </div>
      <div style={{ position: 'absolute', left: PAD_X, top: height * 0.66 }}>{rules}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.5, top: height * 0.67 }}>{legend}</div>
      <div style={{ position: 'absolute', left: PAD_X + CW * 0.5, top: height * 0.73 }}>{sixty}</div>
      <SparkLine text={sparkLine} inOp={sparkIn} padX={PAD_X} width={width} height={height} />
    </AbsoluteFill>
  );
};
