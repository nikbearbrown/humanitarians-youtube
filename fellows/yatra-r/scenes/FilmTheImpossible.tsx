/**
 * FilmTheImpossible.tsx — reel-local scenes for `yatra-film-the-impossible`
 * ("Film the Impossible." — AI-generated video trends becoming their own genre on TikTok:
 * creators filming themselves into scenes that never happened).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The human asked for a new video, not a variation. No earlier family (Pq*, Geo*, Wk*,
 * Wwa*, …) is reused. Shapes come from this reel's argument: a three-frame film strip
 * BLUF, a composite diagram (you + a scene that never existed → AI video tool → you, in
 * it), three flat sketches of the supplied trend examples (lion ride, car from thin air,
 * wolf bodyguards), a two-column trend board, and a documenting ↔ directing axis.
 *
 * ── ONE COMPONENT, BOTH ASPECTS ──────────────────────────────────────────────
 * Each scene reads the composition size and lays out for 16:9 (side by side) or 9:16
 * (stacked or sequential — never scaled). Portrait keeps content above y≈1440 and left of
 * x≈960 and moves the bug lower-left. Root.tsx registers `FtX` (1920×1080) and `FtX916`
 * (1080×1920).
 *
 * ── THE SOURCING CONSTRAINT, ENFORCED BY THE TYPES ───────────────────────────
 * One source, three supplied points, NO figures. So:
 *   · No numeric prop exists anywhere in the Ft* family (no views, counts, shares).
 *   · FtScenes draws the trend examples as flat SKETCHES and REQUIRES a `sketchNote`
 *     ("Sketches of the trends, not footage") plus a `source`.
 *   · FtTracker's traditional column takes only `leftSlots` (placeholder cards with no
 *     text prop) — no non-AI trend is ever named, because none was supplied.
 *   · No creator, tool, or platform-logo prop exists.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE, SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';
const INK = CLAUDE.INK;
const ACC = CLAUDE.SPARK;
const CARD = CLAUDE.CARD;
const BORDER = CLAUDE.BORDER;

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));
const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

type Box = {pt: boolean; x: number; y: number; w: number; r: number; b: number};
const useBox = (): Box => {
  const {width, height} = useVideoConfig();
  if (height > width) return {pt: true, x: SAFE916.x, y: SAFE916.y, w: 906, r: SAFE916.x + 906, b: 1440};
  return {pt: false, x: SAFE.x, y: SAFE.y, w: SAFE.w, r: SAFE.r, b: SAFE.b};
};

const Stage: React.FC<{B: Box; children: React.ReactNode}> = ({B, children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    {children}
    {B.pt ? (
      <div style={{position: 'absolute', left: B.x, top: B.b + 40, fontFamily: CLAUDE_FONT.serif, fontSize: 30, color: INK, opacity: 0.3, letterSpacing: '.04em'}}>@Yatra</div>
    ) : (
      <div style={{position: 'absolute', right: 1920 - SAFE.r, bottom: 1080 - SAFE.b, fontFamily: CLAUDE_FONT.serif, fontSize: 26, color: INK, opacity: 0.3, letterSpacing: '.04em'}}>@Yatra</div>
    )}
  </AbsoluteFill>
);

const Eyebrow: React.FC<{B: Box; text: string; opacity?: number}> = ({B, text, opacity = 1}) => (
  <div style={{position: 'absolute', left: B.x, top: B.y + 6, width: B.w, fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 26 : 22, letterSpacing: '.18em', color: MUTE, fontWeight: 600, opacity}}>
    {text.toUpperCase()}
  </div>
);

const Head: React.FC<{B: Box; meta: string; title: string; p: number}> = ({B, meta, title, p}) => (
  <>
    <Eyebrow B={B} text={meta} opacity={win(p, 0.0, 0.08)} />
    <div style={{position: 'absolute', left: B.x, top: B.y + (B.pt ? 64 : 62), width: B.w, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 74 : 80, color: INK, lineHeight: 1.06, opacity: win(p, 0.02, 0.1)}}>
      {title}
    </div>
  </>
);

const Source: React.FC<{B: Box; source: string; opacity: number; top?: number}> = ({B, source, opacity, top}) => (
  <div style={{position: 'absolute', left: B.x, top: top ?? (B.pt ? 1270 : SAFE.b - 128), width: B.w - (B.pt ? 0 : 220), fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 27 : 25, lineHeight: 1.3, color: MUTE, opacity}}>
    Source: {source}
  </div>
);

const Note: React.FC<{B: Box; text: string; opacity: number; top?: number}> = ({B, text, opacity, top}) => (
  <div style={{position: 'absolute', left: B.x, top: top ?? (B.pt ? 1352 : SAFE.b - 62), width: B.w - (B.pt ? 0 : 220), fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: 42, color: INK, opacity, lineHeight: 1.2}}>
    {text}
  </div>
);

const Chip: React.FC<{text: string; hot?: boolean; size?: number}> = ({text, hot, size = 22}) => (
  <span style={{fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600, letterSpacing: '.16em', textTransform: 'uppercase', color: hot ? ACC : MUTE, border: `${hot ? 2 : 1}px solid ${hot ? ACC : RULE}`, padding: '8px 16px', display: 'inline-block', whiteSpace: 'nowrap', backgroundColor: hot ? '#FFFFFF' : 'transparent'}}>
    {text}
  </span>
);

const Line: React.FC<{w: number; h?: number; o?: number}> = ({w, h = 14, o = 0.2}) => (
  <div style={{width: Math.max(0, w), height: h, borderRadius: h / 2, backgroundColor: INK, opacity: o}} />
);

/* ── SVG sketch primitives (viewBox units; flat shapes only) ─────────────────── */

/** Standing person: feet at (x, fy), height h. */
const Person: React.FC<{x: number; fy: number; h: number; color?: string; o?: number}> = ({x, fy, h, color = INK, o = 1}) => {
  const r = h * 0.1;
  const top = fy - h;
  const bw = h * 0.26;
  return (
    <g opacity={o} fill={color}>
      <circle cx={x} cy={top + r} r={r} />
      <rect x={x - bw / 2} y={top + 2.3 * r} width={bw} height={h * 0.38} rx={bw * 0.35} />
      <rect x={x - bw / 2 + 1} y={top + 2.3 * r + h * 0.33} width={bw * 0.42} height={h * 0.42} rx={bw * 0.18} />
      <rect x={x + bw * 0.08 - 1} y={top + 2.3 * r + h * 0.33} width={bw * 0.42} height={h * 0.42} rx={bw * 0.18} />
    </g>
  );
};

/** Side-view wolf facing right; (x, fy) = rear foot on ground; s = scale. */
const Wolf: React.FC<{x: number; fy: number; s: number; color: string; o?: number}> = ({x, fy, s, color, o = 1}) => (
  <g transform={`translate(${x} ${fy}) scale(${s})`} fill={color} opacity={o}>
    <rect x={2} y={-34} width={7} height={34} rx={3} />
    <rect x={14} y={-34} width={7} height={34} rx={3} />
    <rect x={52} y={-34} width={7} height={34} rx={3} />
    <rect x={64} y={-34} width={7} height={34} rx={3} />
    <ellipse cx={38} cy={-44} rx={42} ry={17} />
    <path d="M70,-54 L92,-62 L104,-52 L96,-44 L76,-38 Z" />
    <path d="M84,-60 L88,-76 L94,-60 Z" />
    <path d="M92,-58 L98,-72 L101,-56 Z" />
    <path d="M0,-48 Q-18,-44 -24,-26 Q-12,-34 2,-38 Z" />
  </g>
);

/** Lion facing right; (x, fy) rear foot; s scale. */
const Lion: React.FC<{color: string; o?: number}> = ({color, o = 1}) => (
  <g fill={color} opacity={o}>
    <rect x={98} y={410} width={20} height={64} rx={8} />
    <rect x={128} y={410} width={20} height={64} rx={8} />
    <rect x={218} y={410} width={20} height={64} rx={8} />
    <rect x={248} y={410} width={20} height={64} rx={8} />
    <ellipse cx={182} cy={396} rx={104} ry={44} />
    <circle cx={286} cy={352} r={48} stroke={color} strokeWidth={18} strokeDasharray="7 5" fill={color} />
    <ellipse cx={306} cy={362} rx={30} ry={24} fill={color} />
    <path d="M80,388 Q46,372 44,330" stroke={color} strokeWidth={8} fill="none" strokeLinecap="round" />
    <circle cx={44} cy={326} r={9} />
  </g>
);

/** Sports car side view, unit box ~ (0..300, 0..100). */
const CAR_PATH = 'M10,80 L22,52 L80,40 L130,14 L210,14 L252,40 L290,48 L298,80 Z';

/** One sketch frame (viewBox 360×640). `g` = generation progress, `hot` = accent on. */
const Sketch: React.FC<{kind: string; g: number; hot: boolean; p: number}> = ({kind, g, hot, p}) => {
  const gen = hot ? ACC : INK;
  const genO = hot ? 0.92 : 0.7;
  return (
    <svg viewBox="0 0 360 640" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" style={{display: 'block'}}>
      <rect x={0} y={0} width={360} height={640} fill={CARD} />
      <line x1={0} y1={476} x2={360} y2={476} stroke={INK} strokeOpacity={0.35} strokeWidth={2} />
      {kind === 'lion' && (
        <>
          <Lion color={gen} o={genO * g} />
          {/* rider seated on the back */}
          <g fill={INK} opacity={win(g, 0.5, 1)}>
            <circle cx={176} cy={262} r={17} />
            <rect x={160} y={282} width={32} height={70} rx={12} />
            <path d="M162,336 L150,404 L164,406 L180,342 Z" />
          </g>
        </>
      )}
      {kind === 'car' && (
        <>
          {Array.from({length: 6}).map((_, i) => (
            <line key={i} x1={20 + i * 70} y1={490} x2={-30 + i * 70} y2={640} stroke={INK} strokeOpacity={0.28} strokeWidth={4} />
          ))}
          <Person x={62} fy={476} h={150} />
          <g transform="translate(118 392) scale(0.8)">
            <path d={CAR_PATH} fill={gen} opacity={genO * win(g, 0.55, 1)} />
            <circle cx={78} cy={82} r={22} fill={INK} opacity={win(g, 0.6, 1)} />
            <circle cx={232} cy={82} r={22} fill={INK} opacity={win(g, 0.6, 1)} />
          </g>
          {/* particles converging into the car */}
          {Array.from({length: 34}).map((_, i) => {
            const sx = (i * 97) % 360, sy = 60 + ((i * 53) % 300);
            const ex = 130 + ((i * 37) % 220), ey = 410 + ((i * 29) % 50);
            const t = win(g, 0, 0.7);
            return <circle key={i} cx={lerp(sx, ex, t)} cy={lerp(sy, ey, t)} r={4} fill={gen} opacity={(1 - win(g, 0.6, 1)) * 0.8 * Math.min(1, g * 4)} />;
          })}
        </>
      )}
      {kind === 'wolves' && (
        <>
          {[20, 70, 120, 236, 290, 334].map((x, i) => (
            <rect key={i} x={x} y={0} width={14 + (i % 3) * 8} height={476} fill={INK} opacity={0.14 + (i % 2) * 0.06} />
          ))}
          {[300, 410].map((y, i) => (
            <rect key={i} x={-120 + ((p * 160 + i * 80) % 160)} y={y} width={560} height={46} rx={23} fill={STAGE} opacity={0.75} />
          ))}
          <Wolf x={214} fy={430} s={0.85} color={gen} o={genO * win(g, 0.1, 0.5)} />
          <Person x={180} fy={500} h={176} />
          <Wolf x={30} fy={524} s={1.15} color={gen} o={genO * win(g, 0.3, 0.7)} />
          <Wolf x={222} fy={536} s={1.15} color={gen} o={genO * win(g, 0.5, 0.9)} />
        </>
      )}
    </svg>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — FtBluf: a film strip of three frames that develop in narration order; the
   `hot` frame is the accent.
   ═══════════════════════════════════════════════════════════════════════════ */
export type FtBlufData = {slideMeta: string; frames: string[]; hot: number; closer: string};

export const FtBluf: React.FC<{data: FtBlufData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const ats = [0.12, 0.4, 0.66];
  const strip = B.pt ? {x: B.x, y: B.y + 70, w: B.w, h: 1130} : {x: B.x, y: B.y + 100, w: B.w, h: 700};
  const band = 56;
  const n = data.frames.length;
  const gap = 28;
  const inner = B.pt
    ? {x: strip.x + band, y: strip.y + 24, w: strip.w - 2 * band, h: strip.h - 48}
    : {x: strip.x + 24, y: strip.y + band, w: strip.w - 48, h: strip.h - 2 * band};
  const fw = B.pt ? inner.w : (inner.w - gap * (n - 1)) / n;
  const fh = B.pt ? (inner.h - gap * (n - 1)) / n : inner.h;
  const holes = B.pt ? Math.floor(strip.h / 62) : Math.floor(strip.w / 62);
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.06)} />
      <div style={{position: 'absolute', left: strip.x, top: strip.y, width: strip.w, height: strip.h, backgroundColor: INK, borderRadius: 10, opacity: 0.92 * win(p, 0.02, 0.1)}}>
        {Array.from({length: holes}).map((_, i) => {
          const s: React.CSSProperties = B.pt
            ? {left: 16, top: 20 + i * 62, width: 24, height: 34}
            : {left: 20 + i * 62, top: 14, width: 34, height: 26};
          const s2: React.CSSProperties = B.pt ? {...s, left: strip.w - 40} : {...s, top: strip.h - 40};
          return (
            <React.Fragment key={i}>
              <div style={{position: 'absolute', ...s, borderRadius: 5, backgroundColor: STAGE}} />
              <div style={{position: 'absolute', ...s2, borderRadius: 5, backgroundColor: STAGE}} />
            </React.Fragment>
          );
        })}
      </div>
      {data.frames.map((t, i) => {
        const at = ats[i] ?? 0.2 + i * 0.2;
        const g = win(p, at, at + 0.1);
        const hot = i === data.hot;
        const x = B.pt ? inner.x : inner.x + i * (fw + gap);
        const y = B.pt ? inner.y + i * (fh + gap) : inner.y;
        return (
          <div key={i} style={{position: 'absolute', left: x, top: y, width: fw, height: fh, boxSizing: 'border-box', backgroundColor: lerpColor(g), border: hot && g > 0.5 ? `4px solid ${ACC}` : 'none', borderRadius: 6, padding: B.pt ? '26px 40px' : '30px 36px', display: 'flex', flexDirection: 'column', justifyContent: 'center', opacity: win(p, 0.04, 0.12)}}>
            <div style={{fontFamily: CLAUDE_FONT.mono, fontSize: B.pt ? 26 : 24, color: MUTE, opacity: g, position: 'absolute', top: B.pt ? 20 : 24, left: B.pt ? 30 : 30}}>{String(i + 1).padStart(2, '0')}</div>
            <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 62 : 68, lineHeight: 1.12, color: hot ? ACC : INK, opacity: g, transform: `translateY(${16 * (1 - g)}px)`}}>{t}</div>
          </div>
        );
      })}
      <Note B={B} text={data.closer} opacity={win(p, 0.86, 0.94)} />
    </Stage>
  );
};

/** Unexposed frame (dark) → developed (card white). */
function lerpColor(g: number): string {
  const a = [0x55, 0x51, 0x42], b = [0xff, 0xff, 0xff];
  const c = a.map((v, i) => Math.round(lerp(v, b[i], g)));
  return `rgb(${c[0]},${c[1]},${c[2]})`;
}

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — FtAnatomy: "You" + "a scene that never existed" feed an AI video tool node; the
   output phone frame shows the silhouette inside the scene with the accent chip.
   ═══════════════════════════════════════════════════════════════════════════ */
export type FtAnatomyData = {slideMeta: string; youLabel: string; sceneLabel: string; toolLabel: string; outLabel: string; chip: string; closer: string};

export const FtAnatomy: React.FC<{data: FtAnatomyData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const c1 = win(p, 0.06, 0.14);
  const c2 = win(p, 0.3, 0.38);
  const node = win(p, 0.48, 0.56);
  const wires = win(p, 0.5, 0.62);
  const out = win(p, 0.68, 0.76);
  const L = B.pt
    ? {c1: {x: B.x, y: B.y + 70, w: 430, h: 330}, c2: {x: B.x + 476, y: B.y + 70, w: 430, h: 330}, node: {x: B.x + 453, y: B.y + 560, r: 92},
       ph: {x: B.x + 40, y: B.y + 700, w: 290, h: 516}, lab: {x: B.x + 380, y: B.y + 860, w: 520}}
    : {c1: {x: B.x, y: B.y + 70, w: 470, h: 330}, c2: {x: B.x, y: B.y + 440, w: 470, h: 330}, node: {x: B.x + 780, y: B.y + 420, r: 112},
       ph: {x: B.x + 1090, y: B.y + 90, w: 370, h: 658}, lab: {x: B.x + 1500, y: B.y + 330, w: 228}};
  const cardBox = (c: {x: number; y: number; w: number; h: number}, g: number, label: string, art: React.ReactNode) => (
    <div style={{position: 'absolute', left: c.x, top: c.y, width: c.w, height: c.h, backgroundColor: CARD, border: `1px solid ${BORDER}`, borderRadius: 18, boxSizing: 'border-box', padding: 26, opacity: g, transform: `translateY(${16 * (1 - g)}px)`, display: 'flex', flexDirection: 'column'}}>
      <div style={{flex: 1, minHeight: 0, position: 'relative', overflow: 'hidden'}}>{art}</div>
      <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 38 : 40, lineHeight: 1.1, color: INK, marginTop: 12}}>{label}</div>
    </div>
  );
  // wire endpoints
  const n = L.node;
  const w1 = B.pt ? {x1: L.c1.x + L.c1.w / 2, y1: L.c1.y + L.c1.h, x2: n.x - 40, y2: n.y - n.r + 10} : {x1: L.c1.x + L.c1.w, y1: L.c1.y + L.c1.h / 2, x2: n.x - n.r + 8, y2: n.y - 30};
  const w2 = B.pt ? {x1: L.c2.x + L.c2.w / 2, y1: L.c2.y + L.c2.h, x2: n.x + 40, y2: n.y - n.r + 10} : {x1: L.c2.x + L.c2.w, y1: L.c2.y + L.c2.h / 2, x2: n.x - n.r + 8, y2: n.y + 30};
  const w3 = B.pt ? {x1: n.x - 40, y1: n.y + n.r, x2: L.ph.x + L.ph.w / 2, y2: L.ph.y - 10} : {x1: n.x + n.r, y1: n.y, x2: L.ph.x - 14, y2: n.y};
  const seg = (w: {x1: number; y1: number; x2: number; y2: number}, t: number, key: string, mk?: boolean) => (
    <line key={key} x1={w.x1} y1={w.y1} x2={lerp(w.x1, w.x2, t)} y2={lerp(w.y1, w.y2, t)} stroke={INK} strokeWidth={4} strokeDasharray="14 10" opacity={0.7 * Math.min(1, t * 3)} markerEnd={mk ? 'url(#ftArr)' : undefined} />
  );
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.06)} />
      {cardBox(L.c1, c1, data.youLabel, (
        <svg viewBox="0 0 200 160" width="100%" height="100%" preserveAspectRatio="xMidYMid meet"><Person x={100} fy={156} h={150} /></svg>
      ))}
      {cardBox(L.c2, c2, data.sceneLabel, (
        <div style={{position: 'absolute', inset: 0, border: `3px dashed ${MUTE}`, borderRadius: 10, overflow: 'hidden'}}>
          <svg viewBox="0 0 300 160" width="100%" height="100%" preserveAspectRatio="none">
            <circle cx={226} cy={46} r={20} fill={INK} opacity={0.15} />
            <path d="M0,130 L70,70 L120,110 L180,52 L250,118 L300,90 L300,160 L0,160 Z" fill={INK} opacity={0.12} />
          </svg>
        </div>
      ))}
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        <defs>
          <marker id="ftArr" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto"><path d="M0,0 L12,6 L0,12 z" fill={INK} /></marker>
        </defs>
        {seg(w1, wires, 'w1')}
        {seg(w2, wires, 'w2')}
        {seg(w3, win(p, 0.62, 0.7), 'w3', true)}
        <circle cx={n.x} cy={n.y} r={n.r * (0.85 + 0.15 * node)} fill={CARD} stroke={INK} strokeWidth={3} opacity={node} />
      </svg>
      <div style={{position: 'absolute', left: n.x - n.r + 12, top: n.y - (B.pt ? 40 : 44), width: 2 * n.r - 24, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 34 : 38, lineHeight: 1.08, color: INK, opacity: node}}>{data.toolLabel}</div>
      {/* output phone */}
      <div style={{position: 'absolute', left: L.ph.x, top: L.ph.y, width: L.ph.w, height: L.ph.h, borderRadius: 36, border: `10px solid ${INK}`, boxSizing: 'border-box', overflow: 'hidden', opacity: out, transform: `scale(${0.94 + 0.06 * out})`}}>
        <svg viewBox="0 0 360 640" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">
          <rect width={360} height={640} fill={CARD} />
          <circle cx={268} cy={150} r={44} fill={ACC} opacity={0.85} />
          <path d="M0,470 L90,330 L160,420 L240,300 L360,440 L360,640 L0,640 Z" fill={INK} opacity={0.16} />
          <Person x={150} fy={560} h={250} />
        </svg>
      </div>
      <div style={{position: 'absolute', left: L.ph.x + 22, top: L.ph.y + 26, opacity: win(p, 0.74, 0.8)}}><Chip text={data.chip} hot size={B.pt ? 20 : 20} /></div>
      <div style={{position: 'absolute', left: L.lab.x, top: L.lab.y, width: L.lab.w, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 46 : 42, lineHeight: 1.12, color: INK, opacity: win(p, 0.76, 0.84)}}>{data.outLabel}</div>
      <Note B={B} text={data.closer} opacity={win(p, 0.88, 0.95)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B04 — FtScenes: the three supplied trend examples as flat sketches. Landscape: three
   frames side by side; portrait: one large frame at a time. The accent marks the
   GENERATED element of the scene currently being described. Requires `sketchNote`.
   ═══════════════════════════════════════════════════════════════════════════ */
export type FtScene = {kind: 'lion' | 'car' | 'wolves'; caption: string};
export type FtScenesData = {slideMeta: string; scenes: FtScene[]; chip: string; sketchNote: string; source: string};

export const FtScenes: React.FC<{data: FtScenesData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const ats = [0.02, 0.34, 0.62];
  const n = data.scenes.length;
  const active = ats.reduce((acc, a, i) => (p >= a ? i : acc), 0);
  if (B.pt) {
    const fw = 500, fh = 889;
    const fx = B.x + (B.w - fw) / 2, fy = B.y + 90;
    return (
      <Stage B={B}>
        <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.05)} />
        {data.scenes.map((sc, i) => {
          const at = ats[i] ?? i / n;
          const next = ats[i + 1] ?? 2;
          const vis = win(p, at, at + 0.04) * (1 - win(p, next - 0.02, next + 0.02));
          const g = win(p, at + 0.02, at + 0.2);
          return (
            <React.Fragment key={i}>
              <div style={{position: 'absolute', left: fx, top: fy, width: fw, height: fh, borderRadius: 40, border: `10px solid ${INK}`, boxSizing: 'border-box', overflow: 'hidden', opacity: vis}}>
                <Sketch kind={sc.kind} g={g} hot={i === active} p={p} />
              </div>
              <div style={{position: 'absolute', left: fx + 26, top: fy + 30, opacity: vis * win(p, at + 0.12, at + 0.18)}}><Chip text={data.chip} hot size={20} /></div>
              <div style={{position: 'absolute', left: B.x, top: fy + fh + 26, width: B.w, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 56, color: INK, opacity: vis}}>
                <span style={{fontFamily: CLAUDE_FONT.mono, fontSize: 34, color: MUTE, marginRight: 18}}>{i + 1}/{n}</span>{sc.caption}
              </div>
            </React.Fragment>
          );
        })}
        <div style={{position: 'absolute', left: B.x, top: 1196, width: B.w, fontFamily: CLAUDE_FONT.ui, fontSize: 27, color: MUTE, opacity: win(p, 0.86, 0.92)}}>{data.sketchNote}</div>
        <Source B={B} source={data.source} opacity={win(p, 0.86, 0.92)} />
      </Stage>
    );
  }
  const fw = 380, fh = 676, gapX = (B.w - n * fw) / (n - 1);
  const fy = B.y + 60;
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.05)} />
      {data.scenes.map((sc, i) => {
        const at = ats[i] ?? i / n;
        const g = win(p, at + 0.02, at + 0.2);
        const fx = B.x + i * (fw + gapX);
        const show = win(p, at, at + 0.05);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: fx, top: fy + 20 * (1 - show), width: fw, height: fh, borderRadius: 36, border: `10px solid ${INK}`, boxSizing: 'border-box', overflow: 'hidden', opacity: 0.25 + 0.75 * show}}>
              <Sketch kind={sc.kind} g={g} hot={i === active} p={p} />
            </div>
            <div style={{position: 'absolute', left: fx + 24, top: fy + 28, opacity: i === active ? win(p, at + 0.12, at + 0.18) : 0}}><Chip text={data.chip} hot size={18} /></div>
            <div style={{position: 'absolute', left: fx - 20, top: fy + fh + 18, width: fw + 40, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 44, color: INK, opacity: show}}>
              <span style={{fontFamily: CLAUDE_FONT.mono, fontSize: 28, color: MUTE, marginRight: 12}}>{i + 1}</span>{sc.caption}
            </div>
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: B.x, top: SAFE.b - 128, width: B.w, display: 'flex', gap: 28, fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity: win(p, 0.86, 0.92)}}>
        <span>{data.sketchNote}</span><span>·</span><span>Source: {data.source}</span>
      </div>
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — FtTracker: a trend board. Traditional column = `leftSlots` placeholder cards
   with NO text prop (no non-AI trend is named); AI column heading is the accent and
   its cards drop in.
   ═══════════════════════════════════════════════════════════════════════════ */
export type FtTrackerData = {slideMeta: string; title: string; leftHeading: string; leftNote: string; leftSlots: number; rightHeading: string; rightItems: string[]; stamp: string; source: string};

export const FtTracker: React.FC<{data: FtTrackerData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const colW = B.pt ? B.w : 790;
  const cardH = B.pt ? 88 : 112;
  const cg = B.pt ? 16 : 22;
  const lx = B.x, rx = B.pt ? B.x : B.x + 938;
  const ly = B.y + (B.pt ? 230 : 250);
  const listH = (k: number) => 92 + k * (cardH + cg);
  const ry = B.pt ? ly + listH(data.leftSlots) + 30 : ly;
  const stampY = B.pt ? ry + listH(data.rightItems.length) + 14 : ly + listH(Math.max(data.leftSlots, data.rightItems.length)) + 22;
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {/* traditional */}
      <div style={{position: 'absolute', left: lx, top: ly, width: colW, borderBottom: `1px solid ${RULE}`, paddingBottom: 10, display: 'flex', alignItems: 'baseline', gap: 18, opacity: win(p, 0.06, 0.12)}}>
        <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 44 : 48, color: INK}}>{data.leftHeading}</span>
        <span style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 24 : 25, color: MUTE}}>{data.leftNote}</span>
      </div>
      {Array.from({length: data.leftSlots}).map((_, i) => {
        const g = win(p, 0.14 + i * 0.04, 0.2 + i * 0.04);
        return (
          <div key={i} style={{position: 'absolute', left: lx, top: ly + 92 + i * (cardH + cg), width: colW, height: cardH, backgroundColor: CARD, border: `1px solid ${BORDER}`, borderRadius: 14, boxSizing: 'border-box', padding: B.pt ? '0 28px' : '0 32px', display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 12, opacity: g}}>
            <Line w={colW * (0.42 + 0.1 * (i % 2))} h={B.pt ? 14 : 16} o={0.32} />
            <Line w={colW * 0.62} h={B.pt ? 10 : 11} o={0.16} />
          </div>
        );
      })}
      {/* AI-generated */}
      <div style={{position: 'absolute', left: rx, top: ry, width: colW, borderBottom: `2px solid ${ACC}`, paddingBottom: 10, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 44 : 48, color: ACC, opacity: win(p, 0.4, 0.46)}}>{data.rightHeading}</div>
      {data.rightItems.map((it, i) => {
        const g = win(p, 0.48 + i * 0.05, 0.54 + i * 0.05);
        return (
          <div key={i} style={{position: 'absolute', left: rx, top: ry + 92 + i * (cardH + cg) - 30 * (1 - g), width: colW, height: cardH, backgroundColor: CARD, border: `1px solid ${BORDER}`, borderRadius: 14, boxSizing: 'border-box', padding: B.pt ? '0 28px' : '0 32px', display: 'flex', alignItems: 'center', gap: 22, opacity: g}}>
            <span style={{fontFamily: CLAUDE_FONT.mono, fontSize: B.pt ? 26 : 28, color: MUTE}}>{i + 1}</span>
            <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 42 : 46, color: INK}}>{it}</span>
          </div>
        );
      })}
      <div style={{position: 'absolute', left: B.pt ? B.x : rx, top: stampY, width: colW, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 42 : 44, color: INK, opacity: win(p, 0.8, 0.88)}}>{data.stamp}</div>
      <Source B={B} source={data.source} opacity={win(p, 0.84, 0.92)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — FtShift: an axis from "documenting reality" (REC dot) to "directing the
   impossible" (clapper). The marker slides to the accent end on the spoken word.
   ═══════════════════════════════════════════════════════════════════════════ */
export type FtShiftData = {slideMeta: string; title: string; leftEnd: string; leftSub: string; rightEnd: string; rightSub: string; chip: string; closer: string};

export const FtShift: React.FC<{data: FtShiftData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const ax = B.pt ? {x1: B.x + 40, x2: B.r - 40, y: B.y + 760} : {x1: B.x + 70, x2: B.r - 70, y: B.y + 560};
  const draw = win(p, 0.04, 0.14);
  const slide = win(p, 0.7, 0.84);
  const mx = lerp(ax.x1, ax.x2, slide);
  const arrived = slide > 0.98;
  const rightOn = win(p, 0.76, 0.84);
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      <div style={{position: 'absolute', left: B.pt ? B.x : B.x + (B.w - 600) / 2, top: B.pt ? B.y + 250 : B.y + 250, width: B.pt ? B.w : 600, textAlign: B.pt ? 'left' : 'center', opacity: win(p, 0.2, 0.28)}}><Chip text={data.chip} size={B.pt ? 26 : 26} /></div>
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        <line x1={ax.x1} y1={ax.y} x2={lerp(ax.x1, ax.x2, draw)} y2={ax.y} stroke={INK} strokeWidth={4} opacity={0.6} />
        <line x1={ax.x1} y1={ax.y - 22} x2={ax.x1} y2={ax.y + 22} stroke={INK} strokeWidth={4} opacity={0.6 * draw} />
        <line x1={ax.x2} y1={ax.y - 22} x2={ax.x2} y2={ax.y + 22} stroke={arrived ? ACC : INK} strokeWidth={4} opacity={0.6 * draw} />
        {Array.from({length: 9}).map((_, i) => (
          <line key={i} x1={lerp(ax.x1, ax.x2, (i + 1) / 10)} y1={ax.y - 8} x2={lerp(ax.x1, ax.x2, (i + 1) / 10)} y2={ax.y + 8} stroke={INK} strokeWidth={2} opacity={0.3 * draw} />
        ))}
        <circle cx={mx} cy={ax.y} r={B.pt ? 30 : 34} fill={arrived ? ACC : INK} opacity={win(p, 0.4, 0.46)} />
      </svg>
      {/* left end */}
      <div style={{position: 'absolute', left: B.pt ? B.x : ax.x1 - 10, top: B.pt ? ax.y - 250 : ax.y - 220, width: B.pt ? 600 : 640, opacity: win(p, 0.06, 0.14)}}>
        <div style={{display: 'flex', alignItems: 'center', gap: 14, marginBottom: 14}}>
          <div style={{width: 22, height: 22, borderRadius: 11, backgroundColor: INK, opacity: 0.7}} />
          <span style={{fontFamily: CLAUDE_FONT.ui, fontWeight: 700, letterSpacing: '.18em', fontSize: B.pt ? 24 : 24, color: MUTE}}>REC</span>
        </div>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 56 : 58, lineHeight: 1.05, color: INK}}>{data.leftEnd}</div>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 28 : 30, color: MUTE, marginTop: 8}}>{data.leftSub}</div>
      </div>
      {/* right end */}
      <div style={{position: 'absolute', left: B.pt ? B.r - 640 : ax.x2 - 640 + 10, top: B.pt ? ax.y + 70 : ax.y + 70, width: 640, textAlign: 'right', opacity: Math.max(0.35, rightOn)}}>
        <svg width={64} height={52} style={{display: 'inline-block', marginBottom: 10}}>
          <rect x={2} y={18} width={60} height={32} fill="none" stroke={rightOn > 0.5 ? ACC : INK} strokeWidth={3} />
          <path d="M2,6 L62,0 L62,14 L2,18 Z" fill={rightOn > 0.5 ? ACC : INK} opacity={0.85} />
        </svg>
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 56 : 58, lineHeight: 1.05, color: rightOn > 0.5 ? ACC : INK}}>{data.rightEnd}</div>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 28 : 30, color: MUTE, marginTop: 8}}>{data.rightSub}</div>
      </div>
      <Note B={B} text={data.closer} opacity={win(p, 0.88, 0.95)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — FtLimits: what we know vs what we don't; REQUIRES provenance and a viewer check.
   ═══════════════════════════════════════════════════════════════════════════ */
export type FtList = {heading: string; items: string[]};
export type FtLimitsData = {slideMeta: string; title: string; found: FtList; notFound: FtList; provenance: string; falsifier: string};

export const FtLimits: React.FC<{data: FtLimitsData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const colW = B.pt ? B.w : 860;
  const itemStep = B.pt ? 64 : 76;
  const cols = [
    {list: data.found, x: B.x, y: B.y + 260, at: 0.12, mark: 'yes' as const},
    {list: data.notFound, x: B.pt ? B.x : B.x + 960, y: B.pt ? B.y + 260 + 84 + data.found.items.length * itemStep + 50 : B.y + 260, at: 0.5, mark: 'no' as const},
  ];
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {cols.map((c, ci) => (
        <React.Fragment key={ci}>
          <div style={{position: 'absolute', left: c.x, top: c.y, width: ci === 0 || B.pt ? colW : B.w - 960, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 44 : 48, color: INK, opacity: win(p, 0.06, 0.12), borderBottom: `1px solid ${RULE}`, paddingBottom: 10}}>{c.list.heading}</div>
          {c.list.items.map((it, i) => {
            const at = c.at + i * 0.06;
            return (
              <div key={i} style={{position: 'absolute', left: c.x, top: c.y + (B.pt ? 84 : 100) + i * itemStep, width: ci === 0 || B.pt ? colW : B.w - 960, display: 'flex', alignItems: 'center', gap: 20, opacity: win(p, at, at + 0.06)}}>
                {c.mark === 'yes'
                  ? <div style={{width: 18, height: 18, borderRadius: 9, backgroundColor: INK, flexShrink: 0}} />
                  : <div style={{width: 18, height: 18, borderRadius: 9, border: `2px solid ${INK}`, boxSizing: 'border-box', flexShrink: 0}} />}
                <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 32 : 33, lineHeight: 1.2, color: INK}}>{it}</div>
              </div>
            );
          })}
        </React.Fragment>
      ))}
      <div style={{position: 'absolute', left: B.x, top: B.pt ? 1150 : SAFE.b - 240, width: B.w, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 42 : 48, lineHeight: 1.2, color: ACC, opacity: win(p, 0.8, 0.88)}}>{data.falsifier}</div>
      <div style={{position: 'absolute', left: B.x, top: B.pt ? 1290 : SAFE.b - 128, width: B.w - (B.pt ? 0 : 220), fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 26 : 25, lineHeight: 1.35, color: MUTE, opacity: win(p, 0.84, 0.92)}}>Source: {data.provenance}</div>
    </Stage>
  );
};
