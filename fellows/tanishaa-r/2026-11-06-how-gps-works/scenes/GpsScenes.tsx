/**
 * GpsScenes.tsx — Remotion components for "How GPS Knows Where You Are"
 * (Humanitarians AI fellow explainer, Tanishaa). Registered in Root.tsx under the
 * folder "HowGpsWorks".
 *
 * Same look as RagScenes / LbScenes / TtvScenes: Claude cream #FAF9F5, ink #3D3929,
 * terracotta #D97757 as the one accent (#AF4B2D when it carries words).
 * 1920x1080 and native 1080x1920 <Name>916, 30 fps. Every reveal is a prop cued to
 * Bella's MEASURED word (nothing runs on its own clock). B06 numbers are real output
 * of youtube/how-gps-works/demo/gps_demo.py.
 */
import React from 'react';
import { AbsoluteFill, Img, staticFile, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { z } from 'zod';
import { HaiBug } from './RagScenes';

const BG = '#FAF9F5';
const INK = '#3D3929';
const SOFT = '#6C6959';
const GHOST = '#B0AD9A';
const CARD = '#FFFFFF';
const BORDER = '#E5E2D9';
const LAND = '#EDE9DF';
const ACC = '#D97757';
const ACC_TEXT = '#AF4B2D';
const OK = '#3F6B4A';
const SERIF = '"EB Garamond", Georgia, "Times New Roman", serif';
const SANS = '-apple-system, "SF Pro Text", "Segoe UI", "Helvetica Neue", sans-serif';
const MONO = 'ui-monospace, "SF Mono", Menlo, monospace';

const SX = 96;
const SY = 54;
const CW = 1920;
const CH = 1080;

const cl = (v: number, a = 0, b = 1) => Math.min(b, Math.max(a, v));
let FADE = 0.03;
const rise = (t: number, a: number, len = FADE) => {
  const p = cl(interpolate(t, [a, a + len], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
  return 1 - Math.pow(1 - p, 3);
};
const useT = () => {
  const frame = useCurrentFrame();
  const { durationInFrames, fps } = useVideoConfig();
  FADE = (0.35 * fps) / Math.max(1, durationInFrames);
  return frame / Math.max(1, durationInFrames - 1);
};
const dur = { durationSeconds: z.number().optional() };

const Footnote: React.FC<{ text: string; o: number; left?: number; bottom?: number; size?: number }> =
  ({ text, o, left = SX, bottom = SY + 8, size = 28 }) =>
    text ? <div style={{ position: 'absolute', left, bottom, right: left + 120, fontFamily: SANS, fontSize: size, color: SOFT, opacity: o }}>{text}</div> : null;

const PW = 1080, PX = 54, PY = 96, PSERIF = 92, PSANS = 72;
const PIW = PW - 2 * PX;
const PBug: React.FC = () => (
  <Img src={staticFile('logos/humanitarians/humanitarians-logo-1.svg')}
    style={{ position: 'absolute', right: PX, bottom: PY, height: 60, opacity: 0.32 }} />
);

// --- drawn icons (no logos involved: generic objects) ----------------------
const Sat: React.FC<{ x: number; y: number; s?: number; o?: number; color?: string }> = ({ x, y, s = 1, o = 1, color = INK }) => (
  <g transform={`translate(${x} ${y}) scale(${s}) rotate(-20)`} opacity={o}>
    <rect x={-46} y={-11} width={30} height={22} rx={3} fill="none" stroke={color} strokeWidth={4} />
    <line x1={-31} y1={-11} x2={-31} y2={11} stroke={color} strokeWidth={2} />
    <rect x={16} y={-11} width={30} height={22} rx={3} fill="none" stroke={color} strokeWidth={4} />
    <line x1={31} y1={-11} x2={31} y2={11} stroke={color} strokeWidth={2} />
    <line x1={-16} y1={0} x2={16} y2={0} stroke={color} strokeWidth={4} />
    <rect x={-12} y={-14} width={24} height={28} rx={5} fill={CARD} stroke={color} strokeWidth={4} />
  </g>
);
const Phone: React.FC<{ x: number; y: number; s?: number; o?: number; color?: string }> = ({ x, y, s = 1, o = 1, color = INK }) => (
  <g transform={`translate(${x} ${y}) scale(${s})`} opacity={o}>
    <rect x={-22} y={-38} width={44} height={76} rx={9} fill={CARD} stroke={color} strokeWidth={4} />
    <line x1={-7} y1={29} x2={7} y2={29} stroke={color} strokeWidth={4} strokeLinecap="round" />
  </g>
);

// ===========================================================================
// GpsKeyPoints — the beat's key points (not every word), each on its spoken word.
// ===========================================================================
export const gpsKeyPointsSchema = z.object({
  points: z.array(z.object({ text: z.string(), at: z.number(), accent: z.boolean().default(false) })),
  ...dur,
});
export const GpsKeyPoints: React.FC<z.infer<typeof gpsKeyPointsSchema>> = (p) => {
  const t = useT();
  return (
    <AbsoluteFill style={{ background: BG, justifyContent: 'center', padding: `0 ${SX + 80}px` }}>
      {p.points.map((pt, i) => {
        const o = rise(t, pt.at);
        return (
          <div key={i} style={{ fontFamily: SERIF, fontSize: 104, lineHeight: 1.35, color: pt.accent ? ACC_TEXT : INK,
            opacity: o, transform: `translateY(${(1 - o) * 24}px)` }}>{pt.text}</div>
        );
      })}
      <HaiBug />
    </AbsoluteFill>
  );
};
export const GpsKeyPoints916: React.FC<z.infer<typeof gpsKeyPointsSchema>> = (p) => {
  const t = useT();
  return (
    <AbsoluteFill style={{ background: BG, justifyContent: 'center', padding: `0 ${PX}px` }}>
      {p.points.map((pt, i) => {
        const o = rise(t, pt.at);
        return (
          <div key={i} style={{ fontFamily: SERIF, fontSize: PSERIF + 30, lineHeight: 1.12, marginBottom: 60,
            color: pt.accent ? ACC_TEXT : INK, opacity: o, transform: `translateY(${(1 - o) * 24}px)` }}>{pt.text}</div>
        );
      })}
      <PBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GpsSky — a lost phone on Earth; ~30 satellites appear in orbit high above;
// faint signals come down; the altitude is marked. Schematic, not to scale.
// ===========================================================================
export const gpsSkySchema = z.object({
  altitudeLabel: z.string(),
  count: z.number().default(30),
  phoneAt: z.number().default(0.2),
  satsAt: z.number().default(0.6),
  altAt: z.number().default(0.8),
  ...dur,
});
const SkyArt: React.FC<{ p: z.infer<typeof gpsSkySchema>; t: number; W: number; H: number; cy: number; earthR: number; orbitR: number;
  stagger: number; span: number; phoneS: number; satS: number; arrowDeg: number }> =
  ({ p, t, W, H, cy, earthR, orbitR, stagger, span, phoneS, satS, arrowDeg }) => {
  const cx = W / 2;
  const po = rise(t, p.phoneAt), so = 0.55 + 0.45 * rise(t, p.satsAt, FADE * 3), ao = rise(t, p.altAt);
  const phoneY = cy - earthR - 44 * phoneS;
  const a0 = (-90 - span / 2) * Math.PI / 180, a1 = (-90 + span / 2) * Math.PI / 180;
  const sats = Array.from({ length: p.count }, (_, i) => {
    const a = a0 + ((a1 - a0) * i) / (p.count - 1);
    const r = orbitR + (i % 2 ? stagger : -stagger);
    return { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a), d: (i * 0.37) % 1 };
  });
  const arc = `M ${cx + orbitR * Math.cos(a0)} ${cy + orbitR * Math.sin(a0)} A ${orbitR} ${orbitR} 0 0 1 ${cx + orbitR * Math.cos(a1)} ${cy + orbitR * Math.sin(a1)}`;
  const pulse = (t * 6) % 1;
  const ar = (arrowDeg * Math.PI) / 180;
  const e = { x: cx + (earthR + 12) * Math.cos(ar), y: cy + (earthR + 12) * Math.sin(ar) };
  const o = { x: cx + (orbitR - stagger - 40) * Math.cos(ar), y: cy + (orbitR - stagger - 40) * Math.sin(ar) };
  return (
    <svg width={W} height={H} style={{ position: 'absolute', left: 0, top: 0 }}>
      <defs>
        <marker id="ah" markerWidth={10} markerHeight={10} refX={5} refY={5} orient="auto-start-reverse">
          <path d="M0,0 L10,5 L0,10 z" fill={ACC_TEXT} />
        </marker>
      </defs>
      <path d={arc} fill="none" stroke={BORDER} strokeWidth={3} strokeDasharray="12 12" opacity={so} />
      <circle cx={cx} cy={cy} r={earthR} fill={LAND} stroke={GHOST} strokeWidth={3} />
      {sats.map((s, i) => {
        const oo = 0.55 + 0.45 * rise(t, p.satsAt + s.d * 0.1);
        return (
          <g key={i}>
            <line x1={s.x} y1={s.y} x2={cx} y2={phoneY} stroke={ACC_TEXT} strokeWidth={2} strokeDasharray="6 14"
              strokeDashoffset={-pulse * 40} opacity={(oo - 0.55) * 0.55} />
            <Sat x={s.x} y={s.y} s={satS} o={oo} />
          </g>
        );
      })}
      <Phone x={cx} y={phoneY} s={phoneS} o={po} />
      <text x={cx + 36 * phoneS} y={phoneY - 30 * phoneS} fontFamily={SERIF} fontSize={54 * phoneS} fill={ACC_TEXT} opacity={po}>?</text>
      <line x1={e.x} y1={e.y} x2={o.x} y2={o.y} stroke={ACC_TEXT} strokeWidth={5} markerEnd="url(#ah)" markerStart="url(#ah)" opacity={ao} />
    </svg>
  );
};
export const GpsSky: React.FC<z.infer<typeof gpsSkySchema>> = (p) => {
  const t = useT();
  const ao = rise(t, p.altAt);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <SkyArt p={p} t={t} W={CW} H={CH} cy={800} earthR={220} orbitR={600} stagger={40} span={160} phoneS={1.2} satS={0.5} arrowDeg={-20} />
      <div style={{ position: 'absolute', left: 1010, top: 530, fontFamily: SERIF, fontSize: 54, color: ACC_TEXT, opacity: ao }}>{p.altitudeLabel}</div>
      <Footnote text="Schematic, not to scale." o={rise(t, p.satsAt)} />
      <HaiBug />
    </AbsoluteFill>
  );
};
export const GpsSky916: React.FC<z.infer<typeof gpsSkySchema>> = (p) => {
  const t = useT();
  const ao = rise(t, p.altAt);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <SkyArt p={{ ...p, count: 12 }} t={t} W={PW} H={1920} cy={1560} earthR={260} orbitR={800} stagger={30} span={60} phoneS={1.5} satS={0.7} arrowDeg={-72} />
      <div style={{ position: 'absolute', left: PX, right: PX, top: 420, fontFamily: SERIF, fontSize: PSERIF + 8, color: ACC_TEXT, opacity: ao }}>{p.altitudeLabel}</div>
      <PBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GpsTimeDistance — a satellite broadcasts "where" + "when"; a pulse travels to
// the phone while a stopwatch runs; delay × speed of light = distance.
// ===========================================================================
export const gpsTimeDistanceSchema = z.object({
  where: z.string(), when: z.string(), travelS: z.number(), rangeKm: z.number(),
  broadcastAt: z.number(), clockAt: z.number(), arriveAt: z.number(), mathAt: z.number(), resultAt: z.number(),
  ...dur,
});
const td = (p: z.infer<typeof gpsTimeDistanceSchema>, t: number) => {
  const go = rise(t, p.broadcastAt), ck = rise(t, p.clockAt), mo = rise(t, p.mathAt), ro = rise(t, p.resultAt);
  // the pulse leaves on "broadcasts" and lands on "notes when"; the stopwatch reads its share of the real delay
  const travel = cl((t - p.broadcastAt) / Math.max(0.01, p.arriveAt - p.broadcastAt));
  const watch = (p.travelS * travel).toFixed(4);
  return { go, ck, mo, ro, travel, watch };
};
export const GpsTimeDistance: React.FC<z.infer<typeof gpsTimeDistanceSchema>> = (p) => {
  const t = useT();
  const { go, ck, mo, ro, travel, watch } = td(p, t);
  const S = { x: 260, y: 230 }, P = { x: 1500, y: 640 };
  const px = S.x + (P.x - S.x) * travel, py = S.y + (P.y - S.y) * travel;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <svg width={CW} height={CH} style={{ position: 'absolute' }}>
        <line x1={S.x} y1={S.y} x2={P.x} y2={P.y} stroke={BORDER} strokeWidth={4} strokeDasharray="14 12" />
        <line x1={S.x} y1={S.y} x2={px} y2={py} stroke={ACC_TEXT} strokeWidth={6} opacity={go} />
        {travel > 0 && travel < 1 ? <circle cx={px} cy={py} r={16} fill={ACC_TEXT} /> : null}
        <Sat x={S.x} y={S.y} s={2} />
        <Phone x={P.x} y={P.y} s={1.8} />
      </svg>
      <div style={{ position: 'absolute', left: 420, top: 110, background: CARD, border: `2px solid ${INK}`, borderRadius: 18,
        padding: '22px 34px', opacity: go, transform: `translateY(${(1 - go) * 20}px)` }}>
        <div style={{ fontFamily: SERIF, fontSize: 54, color: INK }}>{p.where}</div>
        <div style={{ fontFamily: SERIF, fontSize: 54, color: ck > 0.5 ? ACC_TEXT : INK, marginTop: 6 }}>
          {p.when}<span style={{ fontFamily: SANS, fontSize: 34, color: SOFT, marginLeft: 20, opacity: ck }}>atomic clock</span></div>
      </div>
      <div style={{ position: 'absolute', left: P.x - 170, top: P.y + 100, width: 340, textAlign: 'center', opacity: go }}>
        <div style={{ fontFamily: SANS, fontSize: 32, color: SOFT }}>signal took</div>
        <div style={{ fontFamily: MONO, fontSize: 64, color: INK }}>{watch} s</div>
      </div>
      <div style={{ position: 'absolute', left: SX, top: 760, fontFamily: SERIF, fontSize: 64, color: INK, opacity: mo }}>
        {p.travelS.toFixed(4)} s × speed of light
        <span style={{ color: ACC_TEXT, opacity: ro }}> = {p.rangeKm.toLocaleString('en-US')} km</span></div>
      <HaiBug />
    </AbsoluteFill>
  );
};
export const GpsTimeDistance916: React.FC<z.infer<typeof gpsTimeDistanceSchema>> = (p) => {
  const t = useT();
  const { go, ck, mo, ro, travel, watch } = td(p, t);
  const S = { x: 200, y: 640 }, P = { x: 820, y: 1180 };
  const px = S.x + (P.x - S.x) * travel, py = S.y + (P.y - S.y) * travel;
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: PX, right: PX, top: PY, background: CARD, border: `2px solid ${INK}`, borderRadius: 20,
        padding: '26px 34px', opacity: go }}>
        <div style={{ fontFamily: SERIF, fontSize: PSERIF - 8, lineHeight: 1.1, color: INK }}>{p.where}</div>
        <div style={{ fontFamily: SERIF, fontSize: PSERIF - 8, lineHeight: 1.1, color: ck > 0.5 ? ACC_TEXT : INK }}>{p.when.replace("It's exactly ", '')}</div>
      </div>
      <svg width={PW} height={1920} style={{ position: 'absolute' }}>
        <line x1={S.x} y1={S.y} x2={P.x} y2={P.y} stroke={BORDER} strokeWidth={5} strokeDasharray="16 12" />
        <line x1={S.x} y1={S.y} x2={px} y2={py} stroke={ACC_TEXT} strokeWidth={7} opacity={go} />
        {travel > 0 && travel < 1 ? <circle cx={px} cy={py} r={18} fill={ACC_TEXT} /> : null}
        <Sat x={S.x} y={S.y} s={2.2} />
        <Phone x={P.x} y={P.y} s={2} />
      </svg>
      <div style={{ position: 'absolute', left: PX, top: 1100, fontFamily: MONO, fontSize: PSANS + 8, color: INK, opacity: go }}>{watch} s</div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 1400, fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.1, color: INK, opacity: mo }}>
        × speed of light</div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 1530, fontFamily: SERIF, fontSize: PSERIF + 24, color: ACC_TEXT, opacity: ro }}>
        = {p.rangeKm.toLocaleString('en-US')} km</div>
      <PBug />
    </AbsoluteFill>
  );
};

// --- circle geometry shared by GpsCircles / GpsClockError ------------------
type Pt = { x: number; y: number };
const dist = (a: Pt, b: Pt) => Math.hypot(a.x - b.x, a.y - b.y);
const meet = (a: Pt, ra: number, b: Pt, rb: number): Pt[] => {
  const d = dist(a, b), l = (ra * ra - rb * rb + d * d) / (2 * d), h = Math.sqrt(Math.max(0, ra * ra - l * l));
  const mx = a.x + (l * (b.x - a.x)) / d, my = a.y + (l * (b.y - a.y)) / d;
  return [{ x: mx + (h * (b.y - a.y)) / d, y: my - (h * (b.x - a.x)) / d }, { x: mx - (h * (b.y - a.y)) / d, y: my + (h * (b.x - a.x)) / d }];
};
const geo = (W: number, H: number, portrait: boolean) => {
  // every circle (and the swollen ones in GpsClockError) stays inside the title-safe area
  const P = portrait ? { x: 540, y: 900 } : { x: 960, y: 540 };
  const C = portrait
    ? [{ x: 380, y: 740 }, { x: 720, y: 720 }, { x: 520, y: 1150 }, { x: 720, y: 1120 }]
    : [{ x: 780, y: 410 }, { x: 1150, y: 430 }, { x: 930, y: 740 }, { x: 1180, y: 700 }];
  return { P, C, R: C.map((c) => dist(c, P)) };
};
const Ring: React.FC<{ c: Pt; r: number; grow: number; color?: string; w?: number; dash?: string; o?: number }> =
  ({ c, r, grow, color = INK, w = 4, dash, o = 1 }) =>
    grow > 0 ? (
      <g opacity={o}>
        <circle cx={c.x} cy={c.y} r={Math.max(0.1, r * grow)} fill="none" stroke={color} strokeWidth={w} strokeDasharray={dash} />
        <Sat x={c.x} y={c.y} s={0.9} color={color} />
      </g>
    ) : null;

// ===========================================================================
// GpsCircles — one circle: anywhere on it. Two: two points. Three: one point.
// ===========================================================================
export const gpsCirclesSchema = z.object({
  c1At: z.number(), c2At: z.number(), c3At: z.number(), captionAt: z.number(), meetAt: z.number(),
  caption: z.string(),
  ...dur,
});
const CirclesArt: React.FC<{ p: z.infer<typeof gpsCirclesSchema>; t: number; W: number; H: number; portrait: boolean; label: number }> =
  ({ p, t, W, H, portrait, label }) => {
    const { P, C, R } = geo(W, H, portrait);
    const g = [rise(t, p.c1At, FADE * 3), rise(t, p.c2At, FADE * 3), rise(t, p.c3At, FADE * 3)];
    const two = meet(C[0], R[0], C[1], R[1]);
    const other = dist(two[0], P) < 1 ? two[1] : two[0];
    const mo = rise(t, p.meetAt), pulse = 1 + 0.25 * Math.sin(t * 60) * mo;
    return (
      <svg width={W} height={H} style={{ position: 'absolute' }}>
        {[0, 1, 2].map((i) => <Ring key={i} c={C[i]} r={R[i]} grow={g[i]} />)}
        <circle cx={other.x} cy={other.y} r={16} fill={GHOST} opacity={rise(t, p.c2At + FADE * 3) * (1 - 0.7 * g[2])} />
        <circle cx={P.x} cy={P.y} r={16 * (g[2] > 0.5 ? pulse : 1)} fill={g[2] > 0.5 ? ACC : GHOST} opacity={rise(t, p.c2At + FADE * 3)} />
        <text x={P.x + 30} y={P.y - 26} fontFamily={SERIF} fontSize={label} fill={ACC_TEXT} opacity={mo}>you</text>
      </svg>
    );
  };
export const GpsCircles: React.FC<z.infer<typeof gpsCirclesSchema>> = (p) => {
  const t = useT();
  return (
    <AbsoluteFill style={{ background: BG }}>
      <CirclesArt p={p} t={t} W={CW} H={CH} portrait={false} label={64} />
      <div style={{ position: 'absolute', left: SX, bottom: SY + 6, fontFamily: SERIF, fontSize: 48, color: SOFT,
        background: BG, padding: '4px 12px', opacity: rise(t, p.captionAt) }}>{p.caption}</div>
      <HaiBug />
    </AbsoluteFill>
  );
};
export const GpsCircles916: React.FC<z.infer<typeof gpsCirclesSchema>> = (p) => {
  const t = useT();
  return (
    <AbsoluteFill style={{ background: BG }}>
      <CirclesArt p={p} t={t} W={PW} H={1920} portrait label={PSERIF} />
      <div style={{ position: 'absolute', left: PX, right: PX + 90, bottom: PY, fontFamily: SERIF, fontSize: PSERIF - 4, lineHeight: 1.05,
        color: SOFT, background: BG, opacity: rise(t, p.captionAt) }}>{p.caption}</div>
      <PBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GpsClockError — the clock is off: every circle swells by the same amount and
// the meeting point blurs; a fourth satellite pins it (and the clock) back down.
// ===========================================================================
export const gpsClockErrorSchema = z.object({
  errorLabel: z.string(), meters: z.number(),
  clockAt: z.number(), swellAt: z.number(), fourthAt: z.number(), whereAt: z.number(), whenAt: z.number(),
  ...dur,
});
const ClockArt: React.FC<{ p: z.infer<typeof gpsClockErrorSchema>; t: number; W: number; H: number; portrait: boolean; label: number }> =
  ({ p, t, W, H, portrait, label }) => {
    const { P, C, R } = geo(W, H, portrait);
    const sw = rise(t, p.swellAt, FADE * 3), fx = rise(t, p.fourthAt, FADE * 3);
    const grow = 50 * sw * (1 - fx);
    const blur = sw * (1 - fx);
    return (
      <svg width={W} height={H} style={{ position: 'absolute' }}>
        {[0, 1, 2].map((i) => (
          <g key={i}>
            <circle cx={C[i].x} cy={C[i].y} r={R[i]} fill="none" stroke={GHOST} strokeWidth={2} opacity={blur} strokeDasharray="6 8" />
            <Ring c={C[i]} r={R[i] + grow} grow={1} color={blur > 0.5 ? ACC_TEXT : INK} />
          </g>
        ))}
        <Ring c={C[3]} r={R[3]} grow={fx} color={OK} w={5} dash="16 10" />
        <circle cx={P.x} cy={P.y} r={16 + 60 * blur} fill={blur > 0.05 ? ACC : OK} opacity={0.25 + 0.75 * (1 - blur)} />
        {fx > 0.5 ? <text x={P.x + 30} y={P.y - 26} fontFamily={SERIF} fontSize={label} fill={OK}>you</text> : null}
      </svg>
    );
  };
const clockLabels = (p: z.infer<typeof gpsClockErrorSchema>, t: number) =>
  ({ co: rise(t, p.clockAt), so: rise(t, p.swellAt), wo: rise(t, p.whereAt), no: rise(t, p.whenAt), fx: rise(t, p.fourthAt) });
export const GpsClockError: React.FC<z.infer<typeof gpsClockErrorSchema>> = (p) => {
  const t = useT();
  const { co, so, wo, no, fx } = clockLabels(p, t);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <ClockArt p={p} t={t} W={CW} H={CH} portrait={false} label={60} />
      <div style={{ position: 'absolute', left: SX, top: SY + 10, background: CARD, border: `3px solid ${ACC_TEXT}`, borderRadius: 14,
        padding: '10px 26px', fontFamily: SERIF, fontSize: 50, color: ACC_TEXT, opacity: co }}>{p.errorLabel}</div>
      <div style={{ position: 'absolute', left: SX, top: SY + 110, fontFamily: SERIF, fontSize: 50, color: INK, opacity: so * (1 - fx) }}>
        every distance +{p.meters} m</div>
      <div style={{ position: 'absolute', right: SX, top: SY + 10, textAlign: 'right', fontFamily: SERIF, fontSize: 58, lineHeight: 1.3 }}>
        <div style={{ color: INK, opacity: wo }}>3 satellites → where</div>
        <div style={{ color: OK, opacity: no }}>1 more → when</div>
      </div>
      <HaiBug />
    </AbsoluteFill>
  );
};
export const GpsClockError916: React.FC<z.infer<typeof gpsClockErrorSchema>> = (p) => {
  const t = useT();
  const { co, so, wo, no, fx } = clockLabels(p, t);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <ClockArt p={p} t={t} W={PW} H={1920} portrait label={PSERIF} />
      <div style={{ position: 'absolute', left: PX, right: PX, top: PY, fontFamily: SERIF, fontSize: PSERIF - 4, lineHeight: 1.05, color: ACC_TEXT, background: BG,
        opacity: co * (1 - so) }}>clock off by 0.000001 s</div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: PY, fontFamily: SERIF, fontSize: PSERIF - 4, lineHeight: 1.05, color: INK, background: BG,
        opacity: so * (1 - fx) }}>every distance +{p.meters} m</div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 1560, fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.12, background: BG, padding: '10px 0' }}>
        <div style={{ color: INK, opacity: wo }}>3 → where</div>
        <div style={{ color: OK, opacity: no }}>1 more → when</div>
      </div>
      <PBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GpsDemo — real solver output: four satellites above Boston Common, a clock off
// by 1 µs. Ignore it → 390 m off. Solve for it → on the spot, clock found.
// ===========================================================================
export const gpsDemoSchema = z.object({
  place: z.string(), ranges: z.array(z.number()), travelMs: z.array(z.number()),
  clockUs: z.number(), ignoreM: z.number(), solvedUs: z.number(),
  setupAt: z.number(), ignoreAt: z.number(), solveAt: z.number(), foundAt: z.number(),
  footnote: z.string().default(''), footnoteShort: z.string().default(''),
  ...dur,
});
const Target: React.FC<{ size: number; off: number; color: string }> = ({ size, off, color }) => (
  <svg width={size} height={size}>
    {[0.46, 0.32, 0.18].map((r, i) => <circle key={i} cx={size / 2} cy={size / 2} r={size * r} fill="none" stroke={BORDER} strokeWidth={3} />)}
    <line x1={size / 2 - 14} y1={size / 2} x2={size / 2 + 14} y2={size / 2} stroke={SOFT} strokeWidth={3} />
    <line x1={size / 2} y1={size / 2 - 14} x2={size / 2} y2={size / 2 + 14} stroke={SOFT} strokeWidth={3} />
    <circle cx={size / 2 + off * size * 0.36} cy={size / 2 - off * size * 0.22} r={size * 0.06} fill={color} />
  </svg>
);
export const GpsDemo: React.FC<z.infer<typeof gpsDemoSchema>> = (p) => {
  const t = useT();
  const so = rise(t, p.setupAt), io = rise(t, p.ignoreAt), vo = rise(t, p.solveAt), fo = rise(t, p.foundAt);
  const card: React.CSSProperties = { position: 'absolute', background: CARD, border: `2px solid ${BORDER}`, borderRadius: 20, boxSizing: 'border-box' };
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ ...card, left: SX, top: 110, width: 700, height: 780, padding: '34px 40px', opacity: so }}>
        <div style={{ fontFamily: SERIF, fontSize: 52, color: INK }}>4 satellites above {p.place}</div>
        <div style={{ fontFamily: SANS, fontSize: 30, color: SOFT, marginTop: 24, display: 'flex' }}>
          <span style={{ width: 150 }}>satellite</span><span style={{ width: 230 }}>distance</span><span>signal took</span></div>
        {p.ranges.map((r, i) => (
          <div key={i} style={{ fontFamily: MONO, fontSize: 38, color: INK, display: 'flex', marginTop: 18 }}>
            <span style={{ width: 150 }}>{i + 1}</span><span style={{ width: 230 }}>{r.toLocaleString('en-US')} km</span><span>{p.travelMs[i]} ms</span></div>
        ))}
        <div style={{ marginTop: 50, fontFamily: SERIF, fontSize: 48, color: ACC_TEXT }}>phone clock off by {p.clockUs} µs</div>
      </div>
      <div style={{ ...card, left: SX + 760, top: 110, width: CW - 2 * SX - 760, height: 370, padding: '30px 40px', display: 'flex', gap: 40,
        alignItems: 'center', opacity: io, border: `3px solid ${io > 0.5 ? ACC_TEXT : BORDER}` }}>
        <Target size={250} off={1} color={ACC} />
        <div>
          <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT }}>Ignore the clock</div>
          <div style={{ fontFamily: SERIF, fontSize: 96, color: ACC_TEXT, lineHeight: 1.1 }}>{Math.round(p.ignoreM)} m off</div>
        </div>
      </div>
      <div style={{ ...card, left: SX + 760, top: 520, width: CW - 2 * SX - 760, height: 370, padding: '30px 40px', display: 'flex', gap: 40,
        alignItems: 'center', opacity: vo, border: `3px solid ${vo > 0.5 ? OK : BORDER}` }}>
        <Target size={250} off={0} color={OK} />
        <div>
          <div style={{ fontFamily: SANS, fontSize: 34, color: SOFT }}>Solve for the clock</div>
          <div style={{ fontFamily: SERIF, fontSize: 96, color: OK, lineHeight: 1.1 }}>on the spot</div>
          <div style={{ fontFamily: SERIF, fontSize: 46, color: INK, opacity: fo }}>clock error found: {p.solvedUs.toFixed(6)} µs</div>
        </div>
      </div>
      <Footnote text={p.footnote} o={so} />
      <HaiBug />
    </AbsoluteFill>
  );
};
export const GpsDemo916: React.FC<z.infer<typeof gpsDemoSchema>> = (p) => {
  const t = useT();
  const so = rise(t, p.setupAt), io = rise(t, p.ignoreAt), vo = rise(t, p.solveAt), fo = rise(t, p.foundAt);
  const card: React.CSSProperties = { position: 'absolute', left: PX, width: PIW, background: CARD, borderRadius: 22, boxSizing: 'border-box',
    padding: '30px 40px', display: 'flex', gap: 34, alignItems: 'center' };
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: PX, right: PX, top: PY, fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.08, color: INK, opacity: so }}>
        4 satellites above {p.place}</div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: PY + 230, fontFamily: SERIF, fontSize: PSERIF - 4, lineHeight: 1.08, color: ACC_TEXT, opacity: so }}>
        clock off by {p.clockUs} µs</div>
      <div style={{ ...card, top: 560, height: 470, opacity: io, border: `4px solid ${io > 0.5 ? ACC_TEXT : BORDER}` }}>
        <Target size={300} off={1} color={ACC} />
        <div>
          <div style={{ fontFamily: SANS, fontSize: PSANS, color: SOFT, lineHeight: 1.05 }}>ignore clock</div>
          <div style={{ fontFamily: SERIF, fontSize: PSERIF + 30, color: ACC_TEXT, lineHeight: 1.05 }}>{Math.round(p.ignoreM)} m off</div>
        </div>
      </div>
      <div style={{ ...card, top: 1080, height: 520, opacity: vo, border: `4px solid ${vo > 0.5 ? OK : BORDER}` }}>
        <Target size={300} off={0} color={OK} />
        <div>
          <div style={{ fontFamily: SANS, fontSize: PSANS, color: SOFT, lineHeight: 1.05 }}>solve clock</div>
          <div style={{ fontFamily: SERIF, fontSize: PSERIF + 10, color: OK, lineHeight: 1.05 }}>on the spot</div>
          <div style={{ fontFamily: SERIF, fontSize: PSERIF - 4, color: INK, lineHeight: 1.05, opacity: fo }}>found {p.solvedUs.toFixed(1)} µs</div>
        </div>
      </div>
      <Footnote text={p.footnoteShort || p.footnote} o={so} left={PX} bottom={PY} size={PSANS} />
      <PBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GpsRelativity — the satellite clock gains 38 µs a day (gravity +45, speed −7);
// uncorrected, position drifts ~11 km a day; the fix: set slow before launch.
// ===========================================================================
export const gpsRelativitySchema = z.object({
  net: z.number(), gravity: z.number(), speed: z.number(), driftKm: z.number(),
  clocksAt: z.number(), whyAt: z.number(), driftAt: z.number(), fixAt: z.number(),
  ...dur,
});
const Dial: React.FC<{ size: number; a: number; color: string }> = ({ size, a, color }) => (
  <svg width={size} height={size}>
    <circle cx={size / 2} cy={size / 2} r={size * 0.45} fill={CARD} stroke={color} strokeWidth={6} />
    {Array.from({ length: 12 }, (_, i) => {
      const r1 = size * 0.38, r2 = size * 0.43, an = (i / 12) * 2 * Math.PI;
      return <line key={i} x1={size / 2 + r1 * Math.sin(an)} y1={size / 2 - r1 * Math.cos(an)} x2={size / 2 + r2 * Math.sin(an)} y2={size / 2 - r2 * Math.cos(an)} stroke={SOFT} strokeWidth={3} />;
    })}
    <line x1={size / 2} y1={size / 2} x2={size / 2 + size * 0.34 * Math.sin(a)} y2={size / 2 - size * 0.34 * Math.cos(a)} stroke={color} strokeWidth={7} strokeLinecap="round" />
    <circle cx={size / 2} cy={size / 2} r={8} fill={color} />
  </svg>
);
export const GpsRelativity: React.FC<z.infer<typeof gpsRelativitySchema>> = (p) => {
  const t = useT();
  const co = rise(t, p.clocksAt), wo = rise(t, p.whyAt), dro = rise(t, p.driftAt, FADE * 4), fo = rise(t, p.fixAt);
  const lead = 0.5 * co * (1 - fo);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: SX, top: 100, display: 'flex', gap: 70, opacity: co }}>
        {[{ l: 'Satellite clock', a: t * 20 + lead, c: fo > 0.5 ? OK : ACC_TEXT }, { l: 'Ground clock', a: t * 20, c: INK }].map((d, i) => (
          <div key={i} style={{ textAlign: 'center' }}>
            <Dial size={300} a={d.a} color={d.c} />
            <div style={{ fontFamily: SERIF, fontSize: 46, color: INK, marginTop: 10 }}>{d.l}</div>
          </div>
        ))}
      </div>
      <div style={{ position: 'absolute', left: SX + 770, top: 110, fontFamily: SERIF, fontSize: 96, color: fo > 0.5 ? OK : ACC_TEXT, opacity: co }}>
        {fo > 0.5 ? 'fixed' : `+${p.net} µs a day`}</div>
      <div style={{ position: 'absolute', left: SX + 770, top: 250, fontFamily: SERIF, fontSize: 64, lineHeight: 1.35, color: INK, opacity: wo }}>
        <div>weaker gravity → faster <span style={{ color: ACC_TEXT }}>+{p.gravity}</span></div>
        <div>orbital speed → slower <span style={{ color: ACC_TEXT }}>−{p.speed}</span></div>
      </div>
      <div style={{ position: 'absolute', left: SX, top: 640, width: CW - 2 * SX, opacity: dro > 0 ? 1 : 0 }}>
        <div style={{ height: 8, width: `${80 * dro * (1 - fo)}%`, background: ACC, borderRadius: 4 }} />
        <div style={{ fontFamily: SERIF, fontSize: 58, color: ACC_TEXT, marginTop: 20, opacity: dro * (1 - fo) }}>
          uncorrected: your position drifts ~{p.driftKm} km a day</div>
      </div>
      <div style={{ position: 'absolute', left: SX, top: 830, border: `5px solid ${OK}`, color: OK, fontFamily: SERIF, fontSize: 60,
        padding: '8px 34px', borderRadius: 14, opacity: fo, transform: `scale(${1.3 - 0.3 * fo})`, transformOrigin: 'left center' }}>
        set to tick slightly slow before launch</div>
      <HaiBug />
    </AbsoluteFill>
  );
};
export const GpsRelativity916: React.FC<z.infer<typeof gpsRelativitySchema>> = (p) => {
  const t = useT();
  const co = rise(t, p.clocksAt), wo = rise(t, p.whyAt), dro = rise(t, p.driftAt, FADE * 4), fo = rise(t, p.fixAt);
  const lead = 0.5 * co * (1 - fo);
  return (
    <AbsoluteFill style={{ background: BG }}>
      <div style={{ position: 'absolute', left: PX, top: PY, display: 'flex', gap: 60, opacity: co }}>
        {[{ l: 'Satellite', a: t * 20 + lead, c: fo > 0.5 ? OK : ACC_TEXT }, { l: 'Ground', a: t * 20, c: INK }].map((d, i) => (
          <div key={i} style={{ textAlign: 'center' }}>
            <Dial size={420} a={d.a} color={d.c} />
            <div style={{ fontFamily: SERIF, fontSize: PSERIF - 8, color: INK }}>{d.l}</div>
          </div>
        ))}
      </div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 680, fontFamily: SERIF, fontSize: PSERIF + 20, color: fo > 0.5 ? OK : ACC_TEXT, opacity: co }}>
        {fo > 0.5 ? 'fixed' : `+${p.net} µs a day`}</div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 860, fontFamily: SERIF, fontSize: PSERIF - 4, lineHeight: 1.12, color: INK, opacity: wo }}>
        <div>gravity <span style={{ color: ACC_TEXT }}>+{p.gravity}</span></div>
        <div>speed <span style={{ color: ACC_TEXT }}>−{p.speed}</span></div>
      </div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 1100, fontFamily: SERIF, fontSize: PSERIF, lineHeight: 1.08, color: ACC_TEXT, opacity: dro * (1 - fo) }}>
        uncorrected: ~{p.driftKm} km a day</div>
      <div style={{ position: 'absolute', left: PX, right: PX, top: 1300, border: `6px solid ${OK}`, color: OK, fontFamily: SERIF, fontSize: PSERIF,
        lineHeight: 1.08, padding: '20px 34px', borderRadius: 16, opacity: fo }}>set slow before launch</div>
      <PBug />
    </AbsoluteFill>
  );
};

// ===========================================================================
// GpsTakeaway — the verdict card (same look as ClaudeVerdictArtifact's lecture
// layout), but every line appears on its own spoken words (lineAt). The library
// card shows two lines at once from frame 0, which Tanishaa flagged.
// ===========================================================================
export const gpsTakeawaySchema = z.object({
  artifactTitle: z.string().default(''),
  artifactHeading: z.string(),
  artifactLines: z.array(z.string()),
  lineAt: z.array(z.number()),
  ...dur,
});
export const GpsTakeaway: React.FC<z.infer<typeof gpsTakeawaySchema>> = (p) => {
  const t = useT();
  return (
    <AbsoluteFill style={{ background: '#F2F0E9', padding: '90px 140px' }}>
      <div style={{ border: `3px solid ${INK}`, borderRadius: 24, background: '#FFFEFB', height: 860, padding: '45px 60px', boxSizing: 'border-box',
        fontFamily: SERIF, color: INK }}>
        <div style={{ fontSize: 54, borderBottom: `2px solid ${INK}`, paddingBottom: 25 }}>{p.artifactTitle}</div>
        <div style={{ fontSize: 64, margin: '34px 0 50px', opacity: rise(t, 0) }}>{p.artifactHeading}</div>
        {p.artifactLines.map((l, i) => {
          const o = rise(t, p.lineAt[i] ?? 0.2 + i * 0.25);
          return (
            <div key={i} style={{ display: 'flex', gap: 30, marginBottom: 46, fontSize: 60, lineHeight: 1.2, opacity: o,
              transform: `translateY(${(1 - o) * 24}px)` }}>
              <span style={{ color: ACC_TEXT, minWidth: 60 }}>{i + 1}.</span><span>{l.replace(/^\s*\d+\.\s*/, '')}</span>
            </div>
          );
        })}
      </div>
      <HaiBug />
    </AbsoluteFill>
  );
};
