import React from 'react';
import { CLAUDE } from '../../tokens/claude';
import { HAI_TYPE, SPARK_TEXT, clamp } from '../../lib/cueKit';
import { TMP } from './tempoData';

export { Chip, listening } from '../pitch/pitchKit';
export { PhoneBaseline, Stat } from '../shazam/shzKit';
export { TMP };

/**
 * tmpKit — shared drawing for "How Apps Find a Song's Tempo."
 *
 * Everything drawn here is a column of `tempoData.ts`, GENERATED from a real run of tempo.py
 * (mel-band spectral flux, windowed autocorrelation, a preference near 120 BPM, a dynamic-
 * programming beat tracker) on 40 synthetic Western drum grooves. The worked example is the
 * test set's own rock groove at 120 BPM; its 40 mel bands are a pre-rendered image.
 *
 * Colour: small or line-like marks that carry meaning (beat ticks, peaks, the chosen curve) are
 * SPARK_TEXT, never SPARK: GATE T §8.3 reads small #D97757 marks as accent text.
 */

export const EX = TMP.example;
export const SHOW_S: number = EX.show_s;

/** librosa's default tempo preference: a bell on log2(BPM), centred at 120, one octave wide. */
export const prior = (bpm: number) => Math.exp(-0.5 * Math.pow(Math.log2(bpm / 120), 2));

/** SVG path of a 0..1 series across w x h (top = 1), optionally only the first `reveal` share. */
export const seriesPath = (ys: number[], w: number, h: number, reveal = 1, area = false) => {
  const n = Math.max(2, Math.round(ys.length * clamp(reveal, 0, 1)));
  const pts = ys.slice(0, n).map((v, i) => `${((i / (ys.length - 1)) * w).toFixed(1)},${(h - clamp(v, 0, 1) * h).toFixed(1)}`);
  if (!area) return `M${pts.join(' L')}`;
  return `M0,${h} L${pts.join(' L')} L${(((n - 1) / (ys.length - 1)) * w).toFixed(1)},${h} Z`;
};

/** Seconds ticks under a w-wide strip spanning `secs` seconds. */
export const TimeAxis: React.FC<{ w: number; y: number; size: number; secs: number[]; span: number; opacity: number; unit?: string }> = ({ w, y, size, secs, span, opacity, unit = 'S' }) => (
  <g opacity={opacity} fontFamily={HAI_TYPE.sans} fontWeight={700} fontSize={size} fill={CLAUDE.INK_SOFT}>
    {secs.map((s) => (
      <text key={s} x={(s / span) * w} y={y + size * 1.3} textAnchor={s === 0 ? 'start' : s === span ? 'end' : 'middle'}>{s} {unit}</text>
    ))}
  </g>
);

/** Waveform envelope as mirrored bars (the groove's own peaks). */
export const Waveform: React.FC<{ w: number; h: number; env: number[]; color?: string; opacity?: number }> = ({ w, h, env, color = CLAUDE.INK_SOFT, opacity = 1 }) => {
  const bw = w / env.length;
  return (
    <g opacity={opacity}>
      {env.map((v, i) => {
        const bh = Math.max(1.5, v * h * 0.92);
        return <rect key={i} x={i * bw} y={h / 2 - bh / 2} width={Math.max(1, bw * 0.72)} height={bh} fill={color} />;
      })}
    </g>
  );
};

/** Caps label used throughout the reel. */
export const Caps: React.FC<{ size: number; color?: string; style?: React.CSSProperties; children: React.ReactNode }> = ({ size, color = CLAUDE.INK_SOFT, style, children }) => (
  <div style={{ fontFamily: HAI_TYPE.sans, fontSize: size, fontWeight: 800, letterSpacing: 1.2, color, whiteSpace: 'nowrap', ...style }}>{children}</div>
);

export { SPARK_TEXT };
