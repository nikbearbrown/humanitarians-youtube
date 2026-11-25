/**
 * AiCitedAuthority.tsx — reel-local scenes for `yatra-be-the-sentence`
 * ("Be the Sentence." — SEO evolving into Search Everywhere Optimization: being the
 * sentence ChatGPT, Claude and Google AI Overviews quote back).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The human asked for a new video, not a variation. No earlier family (Seo*, Ctr*,
 * Adp*, …) is reused. Shapes come from this reel's argument: a results page beside an
 * AI answer with one quoted line, a reach ring, a small-club growth pair, a blind-spot
 * bracket, pillars standing on an SEO foundation slab, an evidence boost chart, a
 * 30-day freshness strip, and a split bar of who writes a brand's AI reputation.
 *
 * ── ONE COMPONENT, BOTH ASPECTS ──────────────────────────────────────────────
 * Each scene reads the composition size and lays out for 16:9 (side by side) or 9:16
 * (stacked, re-banded — never scaled). Portrait keeps content above y≈1440 and left of
 * x≈960 (platform UI keep-out) and moves the bug lower-left. Root.tsx registers each
 * scene twice: `GeoX` at 1920×1080 and `GeoX916` at 1080×1920.
 *
 * ── THE SOURCING CONSTRAINT, ENFORCED BY THE TYPES ───────────────────────────
 * Seven supplied findings, no others. So:
 *   · Every figure-bearing scene REQUIRES a `source` string (muted ink, never accent).
 *   · `value` is a verbatim STRING ("~94%", "+41%", "3.2×"); `bar`/`ratio` is a separate
 *     number that only drives drawing. Nothing parses a displayed string.
 *   · GeoGap's bracket has a `gapLabel` and NO numeric prop — 43 − 14 is arithmetic,
 *     not a finding, so it is never printed.
 *   · GeoSplit's third-party `kinds` are label strings only — no per-kind share exists.
 *   · GeoBluf's results rows and answer lines are placeholders, never invented text.
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

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));
const typed = (text: string, g: number) => text.slice(0, Math.round(text.length * g));

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/** Layout box: landscape = SAFE; portrait = column left of the keep-out, above y 1440. */
type Box = {pt: boolean; x: number; y: number; w: number; r: number; b: number};
const useBox = (): Box => {
  const {width, height} = useVideoConfig();
  if (height > width) {
    return {pt: true, x: SAFE916.x, y: SAFE916.y, w: 906, r: SAFE916.x + 906, b: 1440};
  }
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

/** Provenance: always muted ink, never the accent. */
const Source: React.FC<{B: Box; source: string; opacity: number; top?: number}> = ({B, source, opacity, top}) => (
  <div style={{position: 'absolute', left: B.x, top: top ?? (B.pt ? 1270 : SAFE.b - 128), width: B.w, fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 27 : 25, lineHeight: 1.3, color: MUTE, opacity}}>
    Source: {source}
  </div>
);

const Note: React.FC<{B: Box; text: string; opacity: number; muted?: boolean; top?: number}> = ({B, text, opacity, muted, top}) => (
  <div style={{position: 'absolute', left: B.x, top: top ?? (B.pt ? 1352 : SAFE.b - 62), width: B.w, fontFamily: muted ? CLAUDE_FONT.ui : CLAUDE_FONT.serif, fontSize: muted ? (B.pt ? 28 : 27) : (B.pt ? 42 : 42), color: muted ? MUTE : INK, opacity, lineHeight: 1.2}}>
    {text}
  </div>
);

const Chip: React.FC<{text: string; hot?: boolean; size?: number}> = ({text, hot, size = 22}) => (
  <span style={{fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600, letterSpacing: '.16em', textTransform: 'uppercase', color: hot ? ACC : MUTE, border: `${hot ? 2 : 1}px solid ${hot ? ACC : RULE}`, padding: '8px 16px', display: 'inline-block', whiteSpace: 'nowrap', backgroundColor: hot ? '#FFFFFF' : 'transparent'}}>
    {text}
  </span>
);

const Line: React.FC<{w: number; h?: number; o?: number; color?: string}> = ({w, h = 14, o = 0.2, color = INK}) => (
  <div style={{width: Math.max(0, w), height: h, borderRadius: h / 2, backgroundColor: color, opacity: o}} />
);

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — GeoBluf: THEN a results page of ten ranked rows; NOW an AI answer card in
   which ONE line is quoted (the accent) with a citation chip. Rows dim (≥55%) but stay
   readable — ranking still matters.
   ═══════════════════════════════════════════════════════════════════════════ */
export type GeoBlufData = {
  slideMeta: string;
  thenLabel: string; thenLine: string;
  nowLabel: string; nowLine: string;
  term: string; closer: string;
};

export const GeoBluf: React.FC<{data: GeoBlufData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const now = win(p, 0.38, 0.46);
  const quote = win(p, 0.52, 0.62);

  const L = B.pt
    ? {tx: B.x, ty: B.y + 64, tw: B.w, rowsTop: B.y + 210, rowH: 40, nx: B.x, ny: B.y + 640, nw: B.w, cardTop: B.y + 790, cardH: 330, lineSize: 54, termTop: B.y + 1150}
    : {tx: B.x, ty: B.y + 70, tw: 760, rowsTop: B.y + 250, rowH: 62, nx: B.x + 900, ny: B.y + 70, nw: B.w - 900, cardTop: B.y + 250, cardH: 440, lineSize: 58, termTop: B.y + 730};

  const rows = Array.from({length: 10});
  const cardLines = 5;
  return (
    <Stage B={B}>
      {/* THEN */}
      <div style={{position: 'absolute', left: L.tx, top: L.ty, width: L.tw, opacity: win(p, 0.02, 0.1)}}>
        <Chip text={data.thenLabel} size={B.pt ? 24 : 22} />
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: L.lineSize, color: INK, lineHeight: 1.08, marginTop: 18}}>{data.thenLine}</div>
      </div>
      <div style={{position: 'absolute', left: L.tx, top: L.rowsTop, width: L.tw, opacity: 1 - 0.42 * now}}>
        {rows.map((_, i) => {
          const g = win(p, 0.05 + i * 0.02, 0.12 + i * 0.02);
          return (
            <div key={i} style={{height: L.rowH, display: 'flex', alignItems: 'center', gap: 22, opacity: g}}>
              <div style={{width: 46, fontFamily: CLAUDE_FONT.mono, fontSize: B.pt ? 26 : 28, color: MUTE, textAlign: 'right'}}>{i + 1}</div>
              <div style={{display: 'flex', flexDirection: 'column', gap: 9}}>
                <Line w={(L.tw - 90) * (0.62 + 0.3 * ((i * 37) % 10) / 10)} h={B.pt ? 11 : 14} o={0.42} />
                {!B.pt && <Line w={(L.tw - 90) * 0.85} h={9} o={0.16} />}
              </div>
            </div>
          );
        })}
      </div>

      {/* NOW */}
      <div style={{position: 'absolute', left: L.nx, top: L.ny, width: L.nw, opacity: now}}>
        <Chip text={data.nowLabel} hot={false} size={B.pt ? 24 : 22} />
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: L.lineSize, color: INK, lineHeight: 1.08, marginTop: 18}}>{data.nowLine}</div>
      </div>
      <div style={{position: 'absolute', left: L.nx, top: L.cardTop, width: L.nw, height: L.cardH, backgroundColor: CLAUDE.CARD, border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 22, boxSizing: 'border-box', padding: B.pt ? '34px 40px' : '44px 52px', opacity: now, boxShadow: '0 10px 30px rgba(61,57,41,0.06)'}}>
        <div style={{display: 'flex', alignItems: 'center', gap: 14, marginBottom: B.pt ? 26 : 36}}>
          <div style={{width: 26, height: 26, borderRadius: 13, border: `2px solid ${MUTE}`}} />
          <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 24 : 24, letterSpacing: '.14em', color: MUTE, fontWeight: 600}}>AI ANSWER</div>
        </div>
        <div style={{display: 'flex', flexDirection: 'column', gap: B.pt ? 22 : 30}}>
          {Array.from({length: cardLines}).map((_, i) => {
            const w = (L.nw - (B.pt ? 80 : 104)) * (i === cardLines - 1 ? 0.55 : 0.94);
            const g = win(p, 0.42 + i * 0.02, 0.5 + i * 0.02);
            if (i === 2) {
              return (
                <div key={i} style={{display: 'flex', alignItems: 'center', gap: 16}}>
                  <div style={{position: 'relative', width: w - 70, height: B.pt ? 16 : 20}}>
                    <div style={{position: 'absolute', inset: 0, borderRadius: 10, backgroundColor: INK, opacity: 0.2 * g}} />
                    <div style={{position: 'absolute', left: 0, top: 0, bottom: 0, width: `${quote * 100}%`, borderRadius: 10, backgroundColor: ACC}} />
                  </div>
                  <div style={{width: 48, height: 48, borderRadius: 24, border: `2px solid ${ACC}`, color: ACC, fontFamily: CLAUDE_FONT.ui, fontWeight: 700, fontSize: 24, display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: win(p, 0.58, 0.64), transform: `scale(${0.6 + 0.4 * win(p, 0.58, 0.66)})`}}>1</div>
                </div>
              );
            }
            return <div key={i} style={{opacity: g}}><Line w={w} h={B.pt ? 13 : 16} o={0.2} /></div>;
          })}
        </div>
      </div>
      <div style={{position: 'absolute', left: L.nx, top: L.termTop, width: L.nw, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 46 : 50, color: INK, opacity: win(p, 0.64, 0.72)}}>
        {typed(data.term, win(p, 0.64, 0.78))}
      </div>
      <Note B={B} text={data.closer} opacity={win(p, 0.84, 0.94)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — GeoReach: one ring gauge sweeping to the verbatim figure.
   ═══════════════════════════════════════════════════════════════════════════ */
export type GeoReachData = {slideMeta: string; value: string; bar: number; label: string; note: string; source: string};

export const GeoReach: React.FC<{data: GeoReachData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const sweep = win(p, 0.12, 0.42);
  const R = B.pt ? 300 : 300;
  const SW = B.pt ? 60 : 58;
  const cx = B.pt ? B.x + B.w / 2 : B.x + 360;
  const cy = B.pt ? B.y + 520 : B.y + 470;
  const C = 2 * Math.PI * R;
  const frac = (data.bar / 100) * sweep;
  return (
    <Stage B={B}>
      <Eyebrow B={B} text={data.slideMeta} opacity={win(p, 0, 0.08)} />
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0}}>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke={RULE} strokeWidth={SW} opacity={win(p, 0.04, 0.12)} />
        <circle cx={cx} cy={cy} r={R} fill="none" stroke={ACC} strokeWidth={SW} strokeLinecap="butt"
          strokeDasharray={`${C * frac} ${C}`} transform={`rotate(-90 ${cx} ${cy})`} />
      </svg>
      <div style={{position: 'absolute', left: cx - R, top: cy - 80, width: 2 * R, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 150, lineHeight: 1, color: INK, opacity: win(p, 0.3, 0.42)}}>
        {data.value}
      </div>
      <div style={{position: 'absolute', left: B.pt ? B.x : B.x + 800, top: B.pt ? B.y + 880 : B.y + 300, width: B.pt ? B.w : B.w - 800, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 58 : 66, lineHeight: 1.12, color: INK, opacity: win(p, 0.44, 0.56)}}>
        {data.label}
      </div>
      <div style={{position: 'absolute', left: B.pt ? B.x : B.x + 800, top: B.pt ? B.y + 1080 : B.y + 600, width: B.pt ? B.w : B.w - 800, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 44 : 46, lineHeight: 1.2, color: INK, opacity: win(p, 0.7, 0.8)}}>
        {data.note}
      </div>
      <Source B={B} source={data.source} opacity={win(p, 0.6, 0.72)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B03 — GeoCited: two columns on a baseline (mid-2025 → May 2026) with a growth arrow.
   Axis is unlabelled; the column heights only draw the verbatim values.
   ═══════════════════════════════════════════════════════════════════════════ */
export type GeoPoint = {when: string; value: string; bar: number; hot: boolean};
export type GeoCitedData = {slideMeta: string; title: string; points: GeoPoint[]; note: string; source: string};

export const GeoCited: React.FC<{data: GeoCitedData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const base = B.pt ? 1120 : 800;
  const H = B.pt ? 600 : 440;
  const colW = B.pt ? 230 : 280;
  const max = Math.max(...data.points.map((q) => q.bar)) * 1.15;
  const centers = B.pt ? [B.x + 210, B.x + 650] : [B.x + 520, B.x + 1180];
  const tops = data.points.map((q, i) => {
    const at = 0.08 + i * 0.34;
    return base - H * (q.bar / max) * win(p, at, at + 0.16);
  });
  const arrow = win(p, 0.6, 0.74);
  const [x1, x2] = [centers[0] + colW / 2 + 20, centers[1] - colW / 2 - 20];
  const [y1, y2] = [tops[0] - 140, tops[1] - 140];
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      <div style={{position: 'absolute', left: B.x, top: base, width: B.w, height: 3, backgroundColor: INK, opacity: 0.5 * win(p, 0.02, 0.1)}} />
      {data.points.map((q, i) => {
        const at = 0.08 + i * 0.34;
        const color = q.hot ? ACC : INK;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: centers[i] - colW / 2, top: tops[i], width: colW, height: base - tops[i], backgroundColor: color, opacity: 0.9}} />
            <div style={{position: 'absolute', left: centers[i] - 200, top: tops[i] - (B.pt ? 116 : 124), width: 400, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 100 : 108, lineHeight: 1, color, opacity: win(p, at + 0.1, at + 0.2)}}>{q.value}</div>
            <div style={{position: 'absolute', left: centers[i] - 220, top: base + 22, width: 440, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 34 : 34, fontWeight: 600, color: INK, opacity: win(p, at, at + 0.08)}}>{q.when}</div>
          </React.Fragment>
        );
      })}
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0, opacity: arrow}}>
        <defs>
          <marker id="geoArr" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto">
            <path d="M0,0 L12,6 L0,12 z" fill={INK} />
          </marker>
        </defs>
        <line x1={x1} y1={y1 + 60} x2={x1 + (x2 - x1) * arrow} y2={y1 + 60 + (y2 - y1) * arrow} stroke={INK} strokeWidth={4} strokeDasharray="14 10" markerEnd="url(#geoArr)" opacity={0.7} />
      </svg>
      <Source B={B} source={data.source} opacity={win(p, 0.8, 0.9)} top={B.pt ? 1210 : undefined} />
      <Note B={B} text={data.note} opacity={win(p, 0.84, 0.94)} top={B.pt ? 1290 : undefined} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B04 — GeoGap: two bars on a 0–100 track; a terracotta bracket spans the gap between
   their ends. The bracket carries a LABEL ONLY — no numeric prop exists for the gap.
   ═══════════════════════════════════════════════════════════════════════════ */
export type GeoGapRow = {label: string; value: string; bar: number};
export type GeoGapData = {slideMeta: string; title: string; rows: GeoGapRow[]; gapLabel: string; source: string};

export const GeoGap: React.FC<{data: GeoGapData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const valW = B.pt ? 210 : 260;
  const TX = B.x + valW;
  const TW = B.w - valW;
  const top0 = B.pt ? B.y + 300 : B.y + 250;
  const step = B.pt ? 330 : 250;
  const barH = B.pt ? 96 : 88;
  const labelH = B.pt ? 128 : 66;
  const xs = data.rows.map((r) => TX + TW * (r.bar / 100));
  const br = win(p, 0.66, 0.78);
  const brY = top0 + step + labelH + barH + 50;
  const lo = Math.min(...xs), hi = Math.max(...xs);
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {data.rows.map((r, i) => {
        const at = 0.08 + i * 0.38;
        const y = top0 + i * step;
        const fill = win(p, at + 0.04, at + 0.2);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: TX, top: y, width: TW, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 46 : 46, lineHeight: 1.1, color: INK, opacity: win(p, at, at + 0.08)}}>{r.label}</div>
            <div style={{position: 'absolute', left: B.x, top: y + labelH - 6, width: valW - 24, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 96 : 104, lineHeight: 1, color: INK, opacity: win(p, at + 0.1, at + 0.2)}}>{r.value}</div>
            <div style={{position: 'absolute', left: TX, top: y + labelH, width: TW, height: barH, border: `1px solid ${RULE}`, boxSizing: 'border-box', opacity: win(p, at, at + 0.06)}} />
            <div style={{position: 'absolute', left: TX, top: y + labelH, width: TW * (r.bar / 100) * fill, height: barH, backgroundColor: INK, opacity: 0.85}} />
          </React.Fragment>
        );
      })}
      {/* the bracket — label only */}
      <svg width={1920} height={1920} style={{position: 'absolute', left: 0, top: 0, opacity: br}}>
        <line x1={hi} y1={top0 + step + labelH} x2={hi} y2={brY} stroke={ACC} strokeWidth={4} strokeDasharray="10 8" />
        <line x1={lo} y1={top0 + step + labelH + barH} x2={lo} y2={brY} stroke={ACC} strokeWidth={4} strokeDasharray="10 8" />
        <line x1={lo} y1={brY} x2={lo + (hi - lo) * br} y2={brY} stroke={ACC} strokeWidth={6} />
      </svg>
      <div style={{position: 'absolute', left: lo, top: brY + 16, width: Math.max(hi - lo, 360), fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 50 : 52, color: ACC, opacity: win(p, 0.72, 0.82)}}>{data.gapLabel}</div>
      <Source B={B} source={data.source} opacity={win(p, 0.84, 0.94)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — GeoFoundation: two pillar tracks (0–100%) standing on a slab. Fills rise from
   the slab to each verbatim value; then the slab lights (the accent) — the foundation.
   ═══════════════════════════════════════════════════════════════════════════ */
export type GeoPillar = {label: string; value: string; bar: number};
export type GeoFoundationData = {slideMeta: string; title: string; pillars: GeoPillar[]; foundation: string; closer: string; source: string};

export const GeoFoundation: React.FC<{data: GeoFoundationData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const slabTop = B.pt ? 1100 : 760;
  const slabH = B.pt ? 96 : 92;
  const H = B.pt ? 520 : 400;
  const pw = B.pt ? 190 : 200;
  const centers = B.pt ? [B.x + 226, B.x + 680] : [B.x + 520, B.x + 1200];
  const lit = win(p, 0.66, 0.74);
  const slabX = B.pt ? B.x : B.x + 150;
  const slabW = B.pt ? B.w : B.w - 300;
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {data.pillars.map((q, i) => {
        const at = 0.16 + i * 0.22;
        const fill = win(p, at, at + 0.16);
        const tTop = slabTop - H;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: centers[i] - pw / 2, top: tTop, width: pw, height: H, border: `1px solid ${RULE}`, boxSizing: 'border-box', opacity: win(p, 0.1, 0.18)}} />
            <div style={{position: 'absolute', left: centers[i] - pw / 2, top: slabTop - H * (q.bar / 100) * fill, width: pw, height: H * (q.bar / 100) * fill, backgroundColor: INK, opacity: 0.85}} />
            {B.pt ? (
              <>
                <div style={{position: 'absolute', left: centers[i] - 220, top: tTop - 196, width: 440, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 30, fontWeight: 600, lineHeight: 1.2, color: INK, opacity: win(p, at, at + 0.08)}}>{q.label}</div>
                <div style={{position: 'absolute', left: centers[i] - 220, top: tTop - 110, width: 440, textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 92, lineHeight: 1, color: INK, opacity: win(p, at + 0.08, at + 0.18)}}>{q.value}</div>
              </>
            ) : (
              <div style={{position: 'absolute', left: centers[i] + pw / 2 + 32, top: tTop + 30, width: 380, opacity: win(p, at + 0.06, at + 0.16)}}>
                <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 110, lineHeight: 1, color: INK}}>{q.value}</div>
                <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 32, fontWeight: 600, lineHeight: 1.25, color: INK, marginTop: 14}}>{q.label}</div>
              </div>
            )}
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: slabX, top: slabTop, width: slabW, height: slabH, boxSizing: 'border-box', border: `2px solid ${lit > 0 ? ACC : INK}`, backgroundColor: `rgba(217,119,87,${lit})`, display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: win(p, 0.04, 0.12)}}>
        <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 32 : 36, fontWeight: 700, letterSpacing: '.12em', textTransform: 'uppercase', color: lit > 0.5 ? '#FFFFFF' : INK}}>{data.foundation}</div>
      </div>
      <Source B={B} source={data.source} opacity={win(p, 0.78, 0.88)} top={B.pt ? 1236 : undefined} />
      <Note B={B} text={data.closer} opacity={win(p, 0.86, 0.95)} top={B.pt ? 1310 : undefined} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — GeoBoost: three horizontal bars in narration order (scale 0–50).
   ═══════════════════════════════════════════════════════════════════════════ */
export type GeoBoostRow = {label: string; value: string; bar: number; hot: boolean};
export type GeoBoostData = {slideMeta: string; title: string; rows: GeoBoostRow[]; caption: string; source: string};

export const GeoBoost: React.FC<{data: GeoBoostData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const ats = [0.22, 0.48, 0.62];
  const SCALE = 50;
  const labelW = B.pt ? 0 : 500;
  const valW = B.pt ? 230 : 260;
  const TX = B.x + labelW;
  const TW = B.w - labelW - valW;
  const top0 = B.pt ? B.y + 300 : B.y + 270;
  const step = B.pt ? 290 : 190;
  const barH = B.pt ? 100 : 104;
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {data.rows.map((r, i) => {
        const at = ats[i] ?? 0.2 + i * 0.2;
        const y = top0 + i * step;
        const by = B.pt ? y + 76 : y;
        const fill = win(p, at, at + 0.12);
        const color = r.hot ? ACC : INK;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: B.x, top: B.pt ? y : by + barH / 2 - 30, width: B.pt ? B.w : labelW - 30, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 50 : 50, lineHeight: 1.1, color: INK, opacity: win(p, at - 0.04, at + 0.04)}}>{r.label}</div>
            <div style={{position: 'absolute', left: TX, top: by, width: TW * (r.bar / SCALE) * fill, height: barH, backgroundColor: color, opacity: 0.9}} />
            <div style={{position: 'absolute', left: TX + TW * (r.bar / SCALE) * fill + 24, top: by + barH / 2 - 52, width: valW, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 96 : 104, lineHeight: 1, color, opacity: win(p, at + 0.06, at + 0.12)}}>{r.value}</div>
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: TX, top: top0 - 20, width: 3, height: (data.rows.length - 1) * step + barH + 40 + (B.pt ? 76 : 0), backgroundColor: INK, opacity: 0.4 * win(p, 0.1, 0.2)}} />
      <Source B={B} source={data.source} opacity={win(p, 0.8, 0.9)} top={B.pt ? 1236 : undefined} />
      <Note B={B} text={data.caption} muted opacity={win(p, 0.84, 0.94)} top={B.pt ? 1340 : undefined} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B08 — GeoFresh: a 30-day window of day ticks, then a stale bar at baseline length and
   a fresh bar at `ratio` × baseline (the accent). The ratio prints verbatim from `value`.
   ═══════════════════════════════════════════════════════════════════════════ */
export type GeoFreshData = {slideMeta: string; title: string; stale: string; fresh: string; value: string; ratio: number; days: number; note: string; source: string};

export const GeoFresh: React.FC<{data: GeoFreshData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const n = data.days;
  const gap = B.pt ? 6 : 10;
  const stripW = B.pt ? B.w : 1300;
  const sq = (stripW - gap * (n - 1)) / n;
  const stripTop = B.pt ? B.y + 290 : B.y + 250;
  const labelW = B.pt ? 0 : 520;
  const valW = B.pt ? 230 : 280;
  const TX = B.x + labelW;
  const maxW = B.w - labelW - valW;
  const unit = maxW / data.ratio;
  const rows = [
    {label: data.stale, len: unit, at: 0.26, hot: false},
    {label: data.fresh, len: maxW, at: 0.4, hot: true},
  ];
  const top0 = B.pt ? B.y + 470 : B.y + 470;
  const step = B.pt ? 300 : 190;
  const barH = B.pt ? 100 : 104;
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      <div style={{position: 'absolute', left: B.x, top: stripTop, display: 'flex', gap}}>
        {Array.from({length: n}).map((_, i) => {
          const g = win(p, 0.06 + i * 0.005, 0.1 + i * 0.005);
          return <div key={i} style={{width: sq, height: sq, borderRadius: 4, border: `1px solid ${RULE}`, backgroundColor: INK, opacity: 0.12 + 0.38 * g, boxSizing: 'border-box'}} />;
        })}
      </div>
      <div style={{position: 'absolute', left: B.pt ? B.x : B.x + stripW + 30, top: B.pt ? stripTop + sq + 16 : stripTop + sq / 2 - 20, fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 30 : 32, fontWeight: 600, color: MUTE, opacity: win(p, 0.14, 0.22)}}>
        last {data.days} days
      </div>
      {rows.map((r, i) => {
        const y = top0 + i * step;
        const by = B.pt ? y + 76 : y;
        const fill = win(p, r.at, r.at + 0.14);
        const color = r.hot ? ACC : INK;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: B.x, top: B.pt ? y : by + barH / 2 - 30, width: B.pt ? B.w : labelW - 30, fontFamily: CLAUDE_FONT.serif, fontSize: 48, lineHeight: 1.1, color: INK, opacity: win(p, r.at - 0.06, r.at + 0.02)}}>{r.label}</div>
            <div style={{position: 'absolute', left: TX, top: by, width: r.len * fill, height: barH, backgroundColor: color, opacity: 0.9}} />
            {r.hot && (
              <div style={{position: 'absolute', left: TX + r.len * fill + 24, top: by + barH / 2 - 56, width: valW, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 100 : 112, lineHeight: 1, color: INK, opacity: win(p, r.at + 0.1, r.at + 0.16)}}>{data.value}</div>
            )}
          </React.Fragment>
        );
      })}
      <Source B={B} source={data.source} opacity={win(p, 0.78, 0.88)} top={B.pt ? 1236 : undefined} />
      <Note B={B} text={data.note} opacity={win(p, 0.84, 0.94)} top={B.pt ? 1310 : undefined} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B09 — GeoSplit: one bar split own-site (ink) vs third-party (accent); three kind chips
   drop from the third-party segment. Chips are labels only — no per-kind share exists.
   ═══════════════════════════════════════════════════════════════════════════ */
export type GeoSeg = {label: string; value: string; bar: number};
export type GeoSplitData = {slideMeta: string; title: string; own: GeoSeg; others: GeoSeg; kinds: string[]; source: string};

export const GeoSplit: React.FC<{data: GeoSplitData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const barTop = B.pt ? B.y + 520 : B.y + 420;
  const barH = B.pt ? 140 : 150;
  const total = data.own.bar + data.others.bar;
  const ownW = B.w * (data.own.bar / total);
  const othW = B.w - ownW;
  const fo = win(p, 0.1, 0.24);
  const ft = win(p, 0.36, 0.5);
  const segLabel = (seg: GeoSeg, x: number, w: number, color: string, op: number) => (
    <div style={{position: 'absolute', left: x, top: barTop - (B.pt ? 210 : 190), width: w - 20, opacity: op}}>
      <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 96 : 110, lineHeight: 1, color}}>{seg.value}</div>
      <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 28 : 32, fontWeight: 600, lineHeight: 1.2, color: INK, marginTop: 12}}>{seg.label}</div>
    </div>
  );
  const chipTop = barTop + barH + (B.pt ? 70 : 80);
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      <div style={{position: 'absolute', left: B.x, top: barTop, width: B.w, height: barH, border: `1px solid ${RULE}`, boxSizing: 'border-box', opacity: win(p, 0.04, 0.1)}} />
      <div style={{position: 'absolute', left: B.x, top: barTop, width: ownW * fo, height: barH, backgroundColor: INK, opacity: 0.85}} />
      <div style={{position: 'absolute', left: B.x + ownW + 4, top: barTop, width: Math.max(0, (othW - 4) * ft), height: barH, backgroundColor: ACC}} />
      {segLabel(data.own, B.x, ownW, INK, win(p, 0.16, 0.26))}
      {segLabel(data.others, B.x + ownW + 28, othW, ACC, win(p, 0.42, 0.52))}
      {data.kinds.map((k, i) => {
        const at = 0.56 + i * 0.06;
        const g = win(p, at, at + 0.08);
        const cx = B.pt ? B.x + ownW + 28 : B.x + ownW + 28 + i * (othW / data.kinds.length);
        const cy = B.pt ? chipTop + i * 100 : chipTop;
        return (
          <React.Fragment key={i}>
            {(!B.pt || i === 0) && <div style={{position: 'absolute', left: cx + 20, top: barTop + barH, width: 2, height: cy - (barTop + barH), backgroundColor: INK, opacity: 0.35 * g}} />}
            <div style={{position: 'absolute', left: cx, top: cy + 16 * (1 - g), opacity: g}}>
              <Chip text={k} size={B.pt ? 28 : 30} />
            </div>
          </React.Fragment>
        );
      })}
      <Source B={B} source={data.source} opacity={win(p, 0.8, 0.9)} />
    </Stage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B10 — GeoLimits: what the figures show vs what they don't; REQUIRES provenance and a
   falsifier string, so the falsifiability beat cannot be authored without them.
   ═══════════════════════════════════════════════════════════════════════════ */
export type GeoList = {heading: string; items: string[]};
export type GeoLimitsData = {slideMeta: string; title: string; found: GeoList; notFound: GeoList; provenance: string; falsifier: string};

export const GeoLimits: React.FC<{data: GeoLimitsData}> = ({data}) => {
  const p = useP();
  const B = useBox();
  const colW = B.pt ? B.w : 800;
  const cols = [
    {list: data.found, x: B.x, y: B.pt ? B.y + 290 : B.y + 290, at: 0.14, mark: 'yes' as const},
    {list: data.notFound, x: B.pt ? B.x : B.x + 900, y: B.pt ? B.y + 290 + 80 + data.found.items.length * 64 + 40 : B.y + 290, at: 0.46, mark: 'no' as const},
  ];
  const itemStep = B.pt ? 64 : 78;
  return (
    <Stage B={B}>
      <Head B={B} meta={data.slideMeta} title={data.title} p={p} />
      {cols.map((c, ci) => (
        <React.Fragment key={ci}>
          <div style={{position: 'absolute', left: c.x, top: c.y, width: colW, fontFamily: CLAUDE_FONT.serif, fontSize: B.pt ? 44 : 46, color: INK, opacity: win(p, 0.06, 0.12), borderBottom: `1px solid ${RULE}`, paddingBottom: 10}}>{c.list.heading}</div>
          {c.list.items.map((it, i) => {
            const at = c.at + i * 0.06;
            return (
              <div key={i} style={{position: 'absolute', left: c.x, top: c.y + (B.pt ? 80 : 96) + i * itemStep, width: colW, display: 'flex', alignItems: 'center', gap: 20, opacity: win(p, at, at + 0.06)}}>
                {c.mark === 'yes'
                  ? <div style={{width: 18, height: 18, borderRadius: 9, backgroundColor: INK, flexShrink: 0}} />
                  : <div style={{width: 18, height: 18, borderRadius: 9, border: `2px solid ${INK}`, boxSizing: 'border-box', flexShrink: 0}} />}
                <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 32 : 34, lineHeight: 1.2, color: INK}}>{it}</div>
              </div>
            );
          })}
        </React.Fragment>
      ))}
      <div style={{position: 'absolute', left: B.x, top: B.pt ? 1150 : SAFE.b - 240, width: B.w, fontFamily: CLAUDE_FONT.serif, fontStyle: 'italic', fontSize: B.pt ? 42 : 46, lineHeight: 1.2, color: ACC, opacity: win(p, 0.8, 0.88)}}>{data.falsifier}</div>
      <div style={{position: 'absolute', left: B.x, top: B.pt ? 1300 : SAFE.b - 128, width: B.w - (B.pt ? 0 : 200), fontFamily: CLAUDE_FONT.ui, fontSize: B.pt ? 25 : 25, lineHeight: 1.35, color: MUTE, opacity: win(p, 0.84, 0.92)}}>Sources: {data.provenance}</div>
    </Stage>
  );
};
