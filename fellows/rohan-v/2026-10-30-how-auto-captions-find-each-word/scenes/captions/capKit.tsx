import React from 'react';
import { Img, staticFile } from 'remotion';
import { CLAUDE } from '../../tokens/claude';
import { HAI_TYPE, SPARK_TEXT } from '../../lib/cueKit';
import { CAP } from './capData';

export { Chip, listening } from '../pitch/pitchKit';
export { PhoneBaseline, LandBaseline, Stat } from '../shazam/shzKit';
export { Caps } from '../tempo/tmpKit';
export { CAP, SPARK_TEXT };

/**
 * capKit — shared drawing for "How Auto-Captions Find Each Word."
 *
 * Everything drawn here is a column of `capData.ts`, GENERATED from a real run of captions.py: faster-whisper
 * base (the model our align.py uses) on 24 sentences built word by word from the narrator's voice, clean and in
 * pink noise. The spectrogram is test sentence 1 as an 80-band log-Mel image, computed the way Whisper's front
 * end does (export_cap_data.py).
 */

/** Whisper is OpenAI's model: LOGO LAW, its maker's mark beside its name. */
export const WhisperTag: React.FC<{ size: number; label?: string }> = ({ size, label = 'WHISPER' }) => (
  <span style={{ display: 'inline-flex', alignItems: 'center', gap: size * 0.4 }}>
    <Img src={staticFile('captions/openai-01.svg')} style={{ height: size * 1.6, width: size * 1.6 }} />
    <span style={{ fontFamily: HAI_TYPE.sans, fontWeight: 800, fontSize: size, letterSpacing: 1.2, color: CLAUDE.INK, whiteSpace: 'nowrap' }}>{label}</span>
  </span>
);

/** Waveform envelope as mirrored bars. */
export const Env: React.FC<{ env: number[]; w: number; h: number; color?: string }> = ({ env, w, h, color = CLAUDE.GHOST }) => {
  const bw = w / env.length;
  return <g>{env.map((v, i) => { const bh = Math.max(1.5, v * h * 0.9); return <rect key={i} x={i * bw} y={h / 2 - bh / 2} width={Math.max(1, bw * 0.7)} height={bh} fill={color} />; })}</g>;
};
