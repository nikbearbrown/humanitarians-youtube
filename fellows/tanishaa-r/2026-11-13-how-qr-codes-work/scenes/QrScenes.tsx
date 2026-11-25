/**
 * QrScenes.tsx — Remotion components for "How a QR Code Works"
 * (Humanitarians AI fellow explainer, Tanishaa). Registered in Root.tsx under the
 * folder "HowQrCodesWork".
 *
 * Same look as GpsScenes: Claude cream #FAF9F5, ink #3D3929, terracotta #D97757 as
 * the one accent (#AF4B2D when it carries words). 1920x1080 and native 1080x1920
 * <Name>916, 30 fps. Every reveal is a prop cued to Bella's MEASURED word (nothing
 * runs on its own clock). Every QR grid drawn here is the real module matrix from
 * youtube/how-qr-codes-work/demo/qr_demo.py (passed in as props).
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { HaiBug } from './RagScenes';

const BG = '#FAF9F5';
const INK = '#3D3929';
const SOFT = '#6C6959';
const CARD = '#FFFFFF';
const BORDER = '#E5E2D9';
const ACC = '#D97757';
const ACC_TEXT = '#AF4B2D';
const OK = '#3F6B4A';
const SERIF = '"EB Garamond", Georgia, "Times New Roman", serif';
const SANS = '-apple-system, "SF Pro Text", "Segoe UI", "Helvetica Neue", sans-serif';
const MONO = 'ui-monospace, "SF Mono", Menlo, monospace';

const SX = 96;
const PX = 54, PY = 96, PSERIF = 92, PSANS = 72;

const cl = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
let FADE = 0.03;
const rise = (t: number, a: number, len = FADE) => {
  const p = cl(interpolate(t, [a, a + len], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
  return 1 - Math.pow(1 - p, 3);
};
const ramp = (t: number, a: number, b: number) => cl((t - a) / Math.max(1e-6, b - a));
const useT = () => {
  const frame = useCurrentFrame();
  const { durationInFrames, fps } = useVideoConfig();
  FADE = (0.35 * fps) / Math.max(1, durationInFrames);
  return frame / Math.max(1, durationInFrames - 1);
};
const dur = { durationSeconds: z.number().optional() };
const mat = z.array(z.string());

const PBug: React.FC = () => (
  <Img src={staticFile('logos/humanitarians/humanitarians-logo-1.svg')}
    style={{ position: 'absolute', right: PX, bottom: PY, height: 60, opacity: 0.32 }} />
);
const Bug: React.FC<{ portrait: boolean }> = ({ portrait }) => (portrait ? <PBug /> : <HaiBug />);

// --- QR geometry -----------------------------------------------------------
const isFinder = (x: number, y: number, n: number) =>
  (x < 7 && y < 7) || (x >= n - 7 && y < 7) || (x < 7 && y >= n - 7);
const isTiming = (x: number, y: number, n: number) =>
  (y === 6 && x >= 8 && x <= n - 9) || (x === 6 && y >= 8 && y <= n - 9);

type Fill = (x: number, y: number, dark: boolean) => string | null;
/** Draws a real module matrix (quiet zone of `quiet` modules), size px square. */
const QrSvg: React.FC<{ m: string[]; size: number; fill?: Fill; gap?: number; quiet?: number;
  children?: (u: number, q: number) => React.ReactNode }> = ({ m, size, fill, gap = 0, quiet = 2, children }) => {
  const n = m.length;
  const u = size / (n + 2 * quiet);
  const cells: React.ReactNode[] = [];
  for (let y = 0; y < n; y++) {
    for (let x = 0; x < n; x++) {
      const dark = m[y][x] === '1';
      const c = fill ? fill(x, y, dark) : null;
      const color = c ?? (dark ? INK : null);
      if (!color) continue;
      const g = gap * u;
      cells.push(<rect key={`${x}-${y}`} x={(x + quiet) * u + g / 2} y={(y + quiet) * u + g / 2} width={u - g + 0.4} height={u - g + 0.4}
        rx={gap > 0 ? g : 0} fill={color} />);
    }
  }
  return (
    <svg width={size} height={size} style={{ display: 'block' }}>
      <rect x={0} y={0} width={size} height={size} rx={size * 0.03} fill={CARD} />
      {cells}
      {children ? children(u, quiet) : null}
    </svg>
  );
};

const Points: React.FC<{ items: { text: string; o: number; color?: string; size?: number; mono?: boolean }[]; portrait: boolean;
  style: React.CSSProperties }> = ({ items, portrait, style }) => (
  <div style={{ position: 'absolute', ...style }}>
    {items.map((it, i) => (
      <div key={i} style={{ fontFamily: it.mono ? MONO : SERIF, fontSize: it.size ?? (portrait ? PSERIF : 68), lineHeight: 1.15,
        marginBottom: portrait ? 34 : 30, color: it.color ?? INK, opacity: it.o, transform: `translateY(${(1 - it.o) * 20}px)`, whiteSpace: 'pre-line' }}>{it.text}</div>
    ))}
  </div>
);

/** Layout: landscape = code left, text right; portrait = code top, text below. */
const lay = (portrait: boolean) => portrait
  ? { code: 860, cx: (1080 - 860) / 2, cy: PY + 40, text: { left: PX, right: PX, top: PY + 40 + 860 + 70 } as React.CSSProperties }
  : { code: 820, cx: SX + 40, cy: 130, text: { left: SX + 40 + 820 + 90, right: SX, top: 200 } as React.CSSProperties };

// ===========================================================================
// QrHook — a real code; a sticker covers its middle; it still reads.
// ===========================================================================
export const qrHookSchema = z.object({
  matrix: mat, cover: z.number(),
  points: z.array(z.object({ text: z.string(), at: z.number(), accent: z.boolean().default(false) })),
  coverAt: z.number(), readAt: z.number(),
  ...dur,
});
const HookScene: React.FC<{ p: z.infer<typeof qrHookSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const L = lay(portrait);
  const co = rise(t, p.coverAt), ro = rise(t, p.readAt);
  const n = p.matrix.length;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: L.cx, top: portrait ? L.cy : L.cy - 30, borderRadius: 24, boxShadow: '0 4px 30px rgba(61,57,41,0.12)',
        outline: `${ro * 8}px solid ${OK}` }}>
        <QrSvg m={p.matrix} size={L.code + (portrait ? 0 : 40)} quiet={1}>
          {(u, q) => {
            const s = p.cover * co;
            const o = (q + (n - s) / 2) * u;
            return <rect x={o} y={o} width={s * u} height={s * u} rx={u * 0.6} fill="#EDE9DF" stroke={SOFT} strokeWidth={4}
              strokeDasharray="14 10" opacity={co} />;
          }}
        </QrSvg>
      </div>
      <Points portrait={portrait} style={L.text}
        items={p.points.map((pt) => ({ text: pt.text, o: rise(t, pt.at), color: pt.accent ? OK : INK, size: portrait ? PSERIF + 10 : 92 }))} />
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const QrHook: React.FC<z.infer<typeof qrHookSchema>> = (p) => <HookScene p={p} portrait={false} />;
export const QrHook916: React.FC<z.infer<typeof qrHookSchema>> = (p) => <HookScene p={p} portrait />;

// ===========================================================================
// QrGrid — the code separates into its grid of squares; one dark = 1, one light = 0.
// ===========================================================================
export const qrGridSchema = z.object({
  matrix: mat, sizeLabel: z.string(),
  gridAt: z.number(), bitAt: z.number(), darkAt: z.number(), lightAt: z.number(), historyAt: z.number(), nameAt: z.number(),
  history: z.string(), name: z.string(),
  ...dur,
});
const GridScene: React.FC<{ p: z.infer<typeof qrGridSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const L = lay(portrait);
  const go = rise(t, p.gridAt, FADE * 3), bo = rise(t, p.bitAt), dko = rise(t, p.darkAt), lo = rise(t, p.lightAt);
  const ho = rise(t, p.historyAt), no = rise(t, p.nameAt);
  // pick a dark and a light data module near the middle
  const n = p.matrix.length;
  const mid = Math.floor(n / 2);
  let dk = [mid, mid + 3], lt = [mid, mid + 3];
  for (let x = mid + 3; x < n - 9; x++) { if (p.matrix[mid + 3][x] === '1') { dk = [x, mid + 3]; break; } }
  for (let x = dk[0] + 1; x < n - 8; x++) { if (p.matrix[mid + 3][x] === '0') { lt = [x, mid + 3]; break; } }
  const fill: Fill = (x, y, dark) => {
    if (x === dk[0] && y === dk[1] && dko > 0.5) return ACC;
    return null;
  };
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: L.cx, top: L.cy }}>
        <QrSvg m={p.matrix} size={L.code} fill={fill} gap={0.16 * go}>
          {(u, q) => (
            <>
              {[dk, lt].map(([x, y], i) => {
                const o = i === 0 ? Math.max(bo * 0.6, dko) : lo;
                return <rect key={i} x={(x + q) * u - 5} y={(y + q) * u - 5} width={u + 10} height={u + 10} rx={6} fill="none"
                  stroke={ACC} strokeWidth={9} opacity={o} />;
              })}
            </>
          )}
        </QrSvg>
      </div>
      <Points portrait={portrait} style={L.text} items={[
        { text: p.sizeLabel, o: go },
        { text: 'dark = 1', o: dko, color: ACC_TEXT, mono: true, size: portrait ? PSANS + 10 : 60 },
        { text: 'light = 0', o: lo, color: ACC_TEXT, mono: true, size: portrait ? PSANS + 10 : 60 },
        ...(portrait ? [] : [{ text: p.history, o: ho, size: 54, color: SOFT }]),
        { text: p.name, o: no, size: portrait ? PSERIF : 64 },
      ]} />
      {portrait ? null : null}
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const QrGrid: React.FC<z.infer<typeof qrGridSchema>> = (p) => <GridScene p={p} portrait={false} />;
export const QrGrid916: React.FC<z.infer<typeof qrGridSchema>> = (p) => <GridScene p={p} portrait />;

// ===========================================================================
// QrFinders — the code arrives tilted in a camera frame; the three finder squares
// light up; it straightens on "angle"; the timing lines glow.
// ===========================================================================
export const qrFindersSchema = z.object({
  matrix: mat, findAt: z.number(), findersAt: z.number(), angleAt: z.number(), timingAt: z.number(),
  ...dur,
});
const FinderScene: React.FC<{ p: z.infer<typeof qrFindersSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const L = lay(portrait);
  const fo = rise(t, p.findAt), fio = rise(t, p.findersAt), ao = rise(t, p.angleAt, FADE * 3), to = rise(t, p.timingAt);
  const n = p.matrix.length;
  const rot = -16 * (1 - ao);
  const code = L.code - 80;
  const fill: Fill = (x, y, dark) => {
    if (dark && isFinder(x, y, n) && fio > 0.5) return ACC;
    if (isTiming(x, y, n) && to > 0.5) return dark ? OK : '#CFE0D3';
    return null;
  };
  const corner = (k: number) => {
    const s = 70, w = 10;
    const pos = [[0, 0], [1, 0], [0, 1], [1, 1]][k];
    return <div key={k} style={{ position: 'absolute', width: s, height: s, left: pos[0] ? undefined : 0, right: pos[0] ? 0 : undefined,
      top: pos[1] ? undefined : 0, bottom: pos[1] ? 0 : undefined,
      borderTop: pos[1] ? undefined : `${w}px solid ${SOFT}`, borderBottom: pos[1] ? `${w}px solid ${SOFT}` : undefined,
      borderLeft: pos[0] ? undefined : `${w}px solid ${SOFT}`, borderRight: pos[0] ? `${w}px solid ${SOFT}` : undefined }} />;
  };
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: L.cx, top: L.cy, width: L.code, height: L.code, opacity: fo }}>
        {[0, 1, 2, 3].map(corner)}
        <div style={{ position: 'absolute', left: 40, top: 40, transform: `rotate(${rot}deg) scale(${1 - 0.2 * (1 - ao)})` }}>
          <QrSvg m={p.matrix} size={code} fill={fill} />
        </div>
      </div>
      <Points portrait={portrait} style={L.text} items={[
        { text: 'finder patterns', o: fio, color: ACC_TEXT },
        { text: 'where it is, which way up', o: ao, size: portrait ? PSERIF - 6 : 56 },
        { text: 'timing lines → the grid', o: to, color: OK },
      ]} />
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const QrFinders: React.FC<z.infer<typeof qrFindersSchema>> = (p) => <FinderScene p={p} portrait={false} />;
export const QrFinders916: React.FC<z.infer<typeof qrFindersSchema>> = (p) => <FinderScene p={p} portrait />;

// ===========================================================================
// QrReadPath — the reading path snakes up and down from the bottom-right, two
// columns at a time; 8 bits → a byte; the bytes spell the link; mask overlay.
// ===========================================================================
export const qrReadPathSchema = z.object({
  matrix: mat, text: z.string(), startAt: z.number(), byteAt: z.number(), spellAt: z.number(), maskAt: z.number(),
  ...dur,
});
const zigzag = (n: number) => {
  const pts: [number, number][] = [];
  let up = true;
  for (let right = n - 1; right > 0; right -= 2) {
    if (right === 6) right = 5;
    const ys = Array.from({ length: n }, (_, i) => (up ? n - 1 - i : i));
    for (const y of ys) for (const x of [right, right - 1]) pts.push([x, y]);
    up = !up;
  }
  return pts;
};
const ReadScene: React.FC<{ p: z.infer<typeof qrReadPathSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const L = lay(portrait);
  const n = p.matrix.length;
  const so = rise(t, p.startAt), bo = rise(t, p.byteAt), spo = rise(t, p.spellAt), mo = rise(t, p.maskAt);
  const prog = ramp(t, p.startAt, p.spellAt);
  const path = zigzag(n).slice(0, n * 2 * 3);
  const shown = Math.max(2, Math.floor(path.length * prog));
  const firstByte = p.text.charCodeAt(0).toString(2).padStart(8, '0');
  const fill: Fill = (x, y, dark) => (isFinder(x, y, n) ? (dark ? '#8A8676' : null) : null);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: L.cx, top: L.cy }}>
        <QrSvg m={p.matrix} size={L.code} fill={fill}>
          {(u, q) => (
            <>
              <polyline points={path.slice(0, shown).map(([x, y]) => `${(x + q + 0.5) * u},${(y + q + 0.5) * u}`).join(' ')}
                fill="none" stroke={ACC} strokeWidth={u * 0.28} strokeLinejoin="round" strokeLinecap="round" opacity={0.9 * so * (1 - 0.75 * mo)} />
              <circle cx={(n - 1 + q + 0.5) * u} cy={(n - 1 + q + 0.5) * u} r={u * 0.7} fill={ACC} opacity={so} />
              {mo > 0 ? Array.from({ length: n * n }, (_, i) => {
                const x = i % n, y = Math.floor(i / n);
                if (isFinder(x, y, n) || isTiming(x, y, n) || (x + y) % 2) return null;
                return <rect key={i} x={(x + q) * u} y={(y + q) * u} width={u} height={u} fill={OK} opacity={0.35 * mo} />;
              }) : null}
            </>
          )}
        </QrSvg>
      </div>
      <Points portrait={portrait} style={L.text} items={[
        { text: 'start bottom-right, zigzag', o: so, size: portrait ? PSERIF - 6 : 58 },
        { text: `${firstByte} → "${p.text[0]}"`, o: bo, mono: true, color: ACC_TEXT, size: portrait ? PSANS : 52 },
        { text: portrait ? p.text.replace('https://www.', '').replace('/', '/\n') : p.text.replace('https://www.', ''), o: spo, mono: true, size: portrait ? PSANS + 4 : 44 },
        { text: 'mask: no big blank patches', o: mo, color: OK, size: portrait ? PSERIF - 6 : 58 },
      ]} />
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const QrReadPath: React.FC<z.infer<typeof qrReadPathSchema>> = (p) => <ReadScene p={p} portrait={false} />;
export const QrReadPath916: React.FC<z.infer<typeof qrReadPathSchema>> = (p) => <ReadScene p={p} portrait />;

// ===========================================================================
// QrRecovery — our link at the highest level, as codewords: message vs recovery.
// Then the four levels L 7% · M 15% · Q 25% · H 30%.
// ===========================================================================
const cw = z.object({ version: z.number(), data: z.number(), recovery: z.number() });
export const qrRecoverySchema = z.object({
  low: cw, high: cw, levels: z.array(z.object({ name: z.string(), pct: z.number() })),
  msgAt: z.number(), recAt: z.number(), rsAt: z.number(), levelsAt: z.number(), lowAt: z.number(), highAt: z.number(),
  ...dur,
});
const RecoveryScene: React.FC<{ p: z.infer<typeof qrRecoverySchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const mo = rise(t, p.msgAt), ro = rise(t, p.recAt), rso = rise(t, p.rsAt), lvo = rise(t, p.levelsAt);
  const loO = rise(t, p.lowAt), hiO = rise(t, p.highAt);
  const total = p.high.data + p.high.recovery;
  const cols = portrait ? 14 : 23;
  const box = portrait ? 58 : 54, gapB = portrait ? 10 : 10;
  const left = portrait ? PX : SX;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left, top: portrait ? PY : 80, fontFamily: SANS, fontSize: portrait ? PSANS : 40, color: SOFT, opacity: mo }}>
        {portrait ? `highest level: ${total} bytes` : `Our link at the highest level: ${total} codewords (bytes)`}</div>
      <div style={{ position: 'absolute', left, top: portrait ? PY + 110 : 150, width: cols * (box + gapB), display: 'flex', flexWrap: 'wrap', gap: gapB }}>
        {Array.from({ length: total }, (_, i) => {
          const isMsg = i < p.high.data;
          const o = isMsg ? mo : ro;
          return <div key={i} style={{ width: box, height: box, borderRadius: 8, background: isMsg ? INK : ACC, opacity: 0.12 + 0.88 * o }} />;
        })}
      </div>
      <div style={{ position: 'absolute', left, right: portrait ? PX : SX, top: portrait ? 1060 : 560, display: 'flex',
        flexDirection: portrait ? 'column' : 'row', gap: portrait ? 10 : 60, fontFamily: SERIF, fontSize: portrait ? PSERIF : 60 }}>
        <span style={{ color: INK, opacity: mo }}>■ {p.high.data} message</span>
        <span style={{ color: ACC_TEXT, opacity: ro }}>■ {p.high.recovery} recovery</span>
      </div>
      <div style={{ position: 'absolute', left, right: portrait ? PX : SX, top: portrait ? 1300 : 670, fontFamily: SERIF,
        fontSize: portrait ? PSERIF - 6 : 52, lineHeight: 1.1, color: SOFT, opacity: rso }}>
        {portrait ? 'Reed–Solomon (like CDs)' : 'Reed–Solomon math · the same idea as scratched CDs'}</div>
      <div style={{ position: 'absolute', left, right: portrait ? PX : SX, top: portrait ? 1470 : 780, display: 'flex', gap: portrait ? 18 : 40,
        opacity: lvo }}>
        {p.levels.map((l, i) => {
          const hot = (i === 0 && loO > 0.5 && hiO < 0.5) || (i === p.levels.length - 1 && hiO > 0.5);
          return (
            <div key={i} style={{ flex: 1, textAlign: 'center', borderRadius: 18, padding: portrait ? '18px 0' : '16px 0',
              border: `4px solid ${hot ? ACC_TEXT : BORDER}`, background: CARD, fontFamily: SERIF, color: hot ? ACC_TEXT : INK }}>
              <div style={{ fontSize: portrait ? PSERIF : 64, lineHeight: 1 }}>{l.name}</div>
              <div style={{ fontSize: portrait ? PSERIF - 10 : 48, lineHeight: 1.2 }}>{l.pct}%</div>
            </div>
          );
        })}
      </div>
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const QrRecovery: React.FC<z.infer<typeof qrRecoverySchema>> = (p) => <RecoveryScene p={p} portrait={false} />;
export const QrRecovery916: React.FC<z.infer<typeof qrRecoverySchema>> = (p) => <RecoveryScene p={p} portrait />;

// ===========================================================================
// QrDemo — real result: same link at L and H; a growing centre sticker.
// L fails at 7×7. H still reads at 17×17 (≈21% of the code).
// ===========================================================================
export const qrDemoSchema = z.object({
  low: mat, high: mat, lowFail: z.number(), lowOk: z.number(), highOk: z.number(), highPct: z.number(),
  setupAt: z.number(), growAt: z.number(), lowAt: z.number(), highAt: z.number(),
  footnote: z.string().default(''), footnoteShort: z.string().default(''),
  ...dur,
});
const DemoScene: React.FC<{ p: z.infer<typeof qrDemoSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const so = rise(t, p.setupAt), lo = rise(t, p.lowAt), ho = rise(t, p.highAt);
  const lowSide = 1 + (p.lowFail - 1) * ramp(t, p.growAt, p.lowAt);
  const highSide = 1 + (p.highOk - 1) * ramp(t, p.growAt, p.highAt);
  const size = portrait ? 560 : 700;
  const sticker = (m: string[], s: number) => (u: number, q: number) => {
    const n = m.length;
    const k = Math.round(s);
    const o = (q + (n - k) / 2) * u;
    return t >= p.growAt ? <rect x={o} y={o} width={k * u} height={k * u} fill="#FFFFFF" stroke={SOFT} strokeWidth={4} strokeDasharray="12 8" /> : null;
  };
  const panel = (label: string, m: string[], s: number, status: React.ReactNode, x: number, y: number) => (
    <div style={{ position: 'absolute', left: x, top: y, opacity: so }}>
      <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF - 6 : 56, color: INK, marginBottom: 14 }}>{label}</div>
      <div style={{ width: size, borderRadius: 20, boxShadow: '0 4px 24px rgba(61,57,41,0.12)' }}><QrSvg m={m} size={size}>{sticker(m, s)}</QrSvg></div>
      <div style={{ marginTop: 18, fontFamily: SERIF, fontSize: portrait ? PSERIF - 6 : 56, lineHeight: 1.1 }}>{status}</div>
    </div>
  );
  const lowStatus = <span style={{ color: ACC_TEXT, opacity: lo }}>✗ fails at {p.lowFail} × {p.lowFail}</span>;
  const highStatus = <span style={{ color: OK, opacity: ho }}>✓ reads at {p.highOk} × {p.highOk} ({portrait ? `${Math.round(p.highPct)}%` : 'about a fifth'})</span>;
  return (
    <AbsoluteFill style={{ background: BG }}>
      {portrait ? (
        <>
          {panel('lowest level (L)', p.low, lowSide, lowStatus, PX + 20, PY)}
          {panel('highest level (H)', p.high, highSide, highStatus, PX + 20, PY + 830)}
        </>
      ) : (
        <>
          {panel('lowest level (L)', p.low, lowSide, lowStatus, SX + 60, 70)}
          {panel('highest level (H)', p.high, highSide, highStatus, 1920 - SX - 60 - size - 60, 70)}
        </>
      )}
      <div style={{ position: 'absolute', left: portrait ? PX : SX, bottom: portrait ? PY : 62, fontFamily: SANS,
        fontSize: portrait ? PSANS : 30, color: SOFT, opacity: so }}>{portrait ? p.footnoteShort || p.footnote : p.footnote}</div>
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const QrDemo: React.FC<z.infer<typeof qrDemoSchema>> = (p) => <DemoScene p={p} portrait={false} />;
export const QrDemo916: React.FC<z.infer<typeof qrDemoSchema>> = (p) => <DemoScene p={p} portrait />;

// ===========================================================================
// QrLogo — a round logo in the middle of the level-H code (tested: it reads);
// "the logo is just damage"; the cost: 37×37 vs 29×29 for the same link.
// ===========================================================================
export const qrLogoSchema = z.object({
  matrix: mat, small: mat, logoModules: z.number(),
  logoAt: z.number(), damageAt: z.number(), fillAt: z.number(), costAt: z.number(),
  ...dur,
});
const LogoScene: React.FC<{ p: z.infer<typeof qrLogoSchema>; portrait: boolean }> = ({ p, portrait }) => {
  const t = useT();
  const lgo = rise(t, p.logoAt), dmo = rise(t, p.damageAt), fio = rise(t, p.fillAt), cso = rise(t, p.costAt);
  const n = p.matrix.length, ns = p.small.length;
  const big = portrait ? 760 : 640;
  const small = big * (ns + 4) / (n + 4);
  const logo = (u: number, q: number) => {
    const c = (q + n / 2) * u, r = (p.logoModules / 2) * u;
    return (
      <g opacity={lgo}>
        <circle cx={c} cy={c} r={r} fill={CARD} />
        <circle cx={c} cy={c} r={r * 0.8} fill={ACC} />
        <text x={c} y={c + r * 0.18} textAnchor="middle" fontFamily={SERIF} fontSize={r * 0.5} fill={CARD}>logo</text>
        <circle cx={c} cy={c} r={r + 6} fill="none" stroke={ACC_TEXT} strokeWidth={6} strokeDasharray="14 10" opacity={dmo * (1 - fio)} />
      </g>
    );
  };
  const bx = portrait ? (1080 - big) / 2 : SX + 40;
  const by = portrait ? PY + 20 : 100;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: bx, top: by, borderRadius: 20, boxShadow: '0 4px 24px rgba(61,57,41,0.12)',
        outline: `${fio * 8}px solid ${OK}` }}>
        <QrSvg m={p.matrix} size={big}>{logo}</QrSvg>
      </div>
      <Points portrait={portrait} style={portrait ? { left: PX, right: PX, top: by + big + 50 } : { left: SX + 40 + big + 90, right: SX, top: 120 }} items={[
        { text: 'the logo = damage', o: dmo, color: ACC_TEXT },
        { text: '✓ recovery fills it in', o: fio, color: OK },
      ]} />
      <div style={{ position: 'absolute', left: portrait ? PX : SX + 40 + big + 90, top: portrait ? 1420 : 500, display: 'flex',
        alignItems: 'flex-end', gap: 40, opacity: cso }}>
        <div>
          <QrSvg m={p.small} size={portrait ? small * 0.5 : small * 0.55} />
          <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF - 6 : 48, color: SOFT, marginTop: 8 }}>{ns} × {ns}, lowest</div>
        </div>
        <div style={{ fontFamily: SERIF, fontSize: portrait ? PSERIF - 6 : 52, color: INK, lineHeight: 1.15, paddingBottom: 10 }}>
          same link,<br />highest level:<br /><span style={{ color: ACC_TEXT }}>{n} × {n}</span></div>
      </div>
      <Bug portrait={portrait} />
    </AbsoluteFill>
  );
};
export const QrLogo: React.FC<z.infer<typeof qrLogoSchema>> = (p) => <LogoScene p={p} portrait={false} />;
export const QrLogo916: React.FC<z.infer<typeof qrLogoSchema>> = (p) => <LogoScene p={p} portrait />;
