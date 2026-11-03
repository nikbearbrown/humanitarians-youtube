import React from 'react';
import { CLAUDE } from '../../tokens/claude';
import { hash } from '../../lib/cueKit';

/**
 * diffusionKit — shared drawing for the image-diffusion reel.
 *
 * Every picture these helpers draw comes from `toyData.ts`, which is GENERATED
 * from a real run of a toy diffusion model (train_toy_diffusion.py in the reel
 * folder). Nothing here invents a pixel: the helpers decode, blend between two
 * recorded snapshots, and paint. The one exception is `StaticField`, the
 * full-frame TV static, which is decorative house noise (cueKit `hash`) and is
 * never presented as model output.
 */

/** A dark screen with cream light — the pictures read as a little TV. */
export const SCREEN_DARK = '#221F1A';
export const SCREEN_LIGHT = '#F6F0E3';

const DR = 0x22, DG = 0x1f, DB = 0x1a;
const LR = 0xf6, LG = 0xf0, LB = 0xe3;

/** hex string (2 chars per pixel, 0–255) -> number[] */
export const decode = (hex: string): number[] => {
  const out: number[] = new Array(hex.length / 2);
  for (let i = 0; i < out.length; i++) out[i] = parseInt(hex.substr(i * 2, 2), 16);
  return out;
};

const memo = new Map<string, number[]>();
export const px = (hex: string) => {
  let v = memo.get(hex);
  if (!v) { v = decode(hex); memo.set(hex, v); }
  return v;
};

export const shade = (v: number) => {
  const t = Math.min(1, Math.max(0, v / 255));
  return `rgb(${Math.round(DR + (LR - DR) * t)},${Math.round(DG + (LG - DG) * t)},${Math.round(DB + (LB - DB) * t)})`;
};

/**
 * The DDPM noise schedule, computed exactly as the toy model used it:
 * beta linear from 1e-4 to 0.02 over 1000 steps (Ho et al. 2020, §4),
 * alpha-bar_t = prod (1 - beta_s). Index t = 1..1000; index 0 means "clean".
 */
export const ABAR: number[] = (() => {
  const T = 1000;
  const out = [1];
  let acc = 1;
  for (let i = 0; i < T; i++) {
    const beta = 1e-4 + (0.02 - 1e-4) * (i / (T - 1));
    acc *= 1 - beta;
    out.push(acc);
  }
  return out;
})();

/** The forward process on real numbers: x_t = sqrt(abar) x0 + sqrt(1 - abar) eps. */
export const forwardMix = (x0: number[], eps: number[], t: number): number[] => {
  const k = Math.max(0, Math.min(1000, Math.round(t)));
  const a = Math.sqrt(ABAR[k]);
  const b = Math.sqrt(1 - ABAR[k]);
  return x0.map((v, i) => {
    const x = v / 127.5 - 1;
    const y = Math.max(-1, Math.min(1, a * x + b * eps[i]));
    return (y + 1) * 127.5;
  });
};

/**
 * One 16×16 picture as a grid of squares. `a`/`b` + `mix` cross-fade between two
 * recorded snapshots (so a reverse run animates between its real keyframes).
 */
export const PixelTile: React.FC<{
  a: number[]; b?: number[]; mix?: number; size: number; side?: number;
  radius?: number; frameColor?: string; frameWidth?: number; gap?: number;
  style?: React.CSSProperties;
}> = ({ a, b, mix = 0, size, side = 16, radius, frameColor, frameWidth = 0, gap = 0.06, style }) => {
  const cell = size / side;
  const inner = cell * (1 - gap);
  const off = (cell - inner) / 2;
  const rects: React.ReactNode[] = [];
  for (let i = 0; i < side * side; i++) {
    const v = b ? a[i] + (b[i] - a[i]) * mix : a[i];
    const x = (i % side) * cell + off;
    const y = Math.floor(i / side) * cell + off;
    rects.push(<rect key={i} x={x} y={y} width={inner} height={inner} rx={inner * 0.12} fill={shade(v)} />);
  }
  return (
    <div style={{
      width: size, height: size, borderRadius: radius ?? size * 0.04, overflow: 'hidden',
      background: SCREEN_DARK, boxShadow: frameWidth ? `0 0 0 ${frameWidth}px ${frameColor ?? CLAUDE.INK}` : undefined,
      ...style,
    }}>
      <svg width={size} height={size} style={{ display: 'block' }}>{rects}</svg>
    </div>
  );
};

/**
 * Pick the two recorded snapshots around a step and how far between them.
 * `frames[0]` is step 1000, the last is step 0; snapshots are `every` steps apart.
 */
export const snapshotAt = (frames: readonly string[], step: number, every = 20) => {
  const n = frames.length - 1;
  const pos = Math.max(0, Math.min(n, (1000 - step) / every));
  const i = Math.min(n - 1, Math.floor(pos));
  return { a: px(frames[i]), b: px(frames[i + 1]), mix: pos - i };
};

/**
 * Full-frame TV static — decorative house noise (deterministic `hash`, redrawn
 * every other frame). Used only to set the scene; the model's own starting
 * static is always drawn from toyData.
 */
export const StaticField: React.FC<{
  cols: number; rows: number; w: number; h: number; frame: number; opacity?: number;
}> = ({ cols, rows, w, h, frame, opacity = 1 }) => {
  const cw = w / cols, ch = h / rows;
  const seed = Math.floor(frame / 2);
  const cells: React.ReactNode[] = [];
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const v = hash(c + seed * 13.1, r + seed * 7.7) * 255;
      cells.push(<rect key={r * cols + c} x={c * cw} y={r * ch} width={cw + 0.5} height={ch + 0.5} fill={shade(v)} />);
    }
  }
  return <svg width={w} height={h} style={{ display: 'block', opacity }}>{cells}</svg>;
};
