/**
 * AssistedNotAutomated916.tsx — PORTRAIT (9:16) scenes for `yatra-assisted-not-automated`.
 *
 * Re-banded vertically per the Shorts law's composition logic, not scaled down:
 *   · SeoCompare916 — two bars become two stacked blocks, each with its figure beneath.
 *   · SeoDrop916    — before/after columns become before/after ROWS, so the collapse
 *                     reads as a shortening bar rather than a squeezed pair.
 *   · SeoShare916   — the two proportion tracks stack with more vertical air.
 *   · SeoStat916    — the hero figure gets the top third; label and citation beneath.
 *   · SeoSources916 — claim and citation stack per row instead of sitting side by side
 *                     (a two-column table is unreadable at portrait width).
 *   · SeoAct916     — act card, centred in the upper band.
 *
 * NOTE ON TARGET: this reel's vertical is FULL LENGTH for TikTok, deliberately over the
 * 3:00 cap that applies to YouTube Shorts and Instagram Reels. The Shorts-chrome keep-out
 * is still respected (content above y≈1440, left of x≈960, bug lower-left) because TikTok
 * overlays its own UI in the same regions.
 *
 * The citation discipline is identical to the landscape set: every stat scene REQUIRES a
 * `source`, values are rendered verbatim as strings, and citations render in muted ink
 * rather than the terracotta accent.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {JdgSplit916, JdgStakes916} from './JudgmentIsTheJob916';
import type {ActData, StatData, CompareData, DropData, ShareData, SourcesData} from './AssistedNotAutomated';

/** Reused generic portrait shapes under this episode's names. */
export const SeoSplit916 = JdgSplit916;
export const SeoStakes916 = JdgStakes916;
export const SeoReasons916 = JdgStakes916;
export const SeoWatch916 = JdgStakes916;

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';
const BOX = {x: SAFE916.x, y: SAFE916.y, w: 906, bottom: 1440} as const;

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));
const num = (v: string) => parseFloat(v.replace(/[^0-9.]/g, '')) || 0;

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

const LogoBug916: React.FC = () => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom + 40, fontFamily: CLAUDE_FONT.serif, fontSize: 30, color: CLAUDE.INK, opacity: 0.3, letterSpacing: '.04em'}}>
    @Yatra
  </div>
);

const Stage: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    {children}
    <LogoBug916 />
  </AbsoluteFill>
);

const Head: React.FC<{meta: string; title: string}> = ({meta, title}) => (
  <>
    <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600}}>
      {meta.toUpperCase()}
    </div>
    <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 76, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 78, color: CLAUDE.INK, lineHeight: 1.06}}>
      {title}
    </div>
  </>
);

const Source: React.FC<{source: string; top: number; opacity: number}> = ({source, top, opacity}) => (
  <div style={{position: 'absolute', left: BOX.x, top, width: BOX.w, opacity, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE}}>
    Source: {source}
  </div>
);

const Note: React.FC<{note: string; opacity: number}> = ({note, opacity}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 88, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: CLAUDE.INK, lineHeight: 1.25, opacity}}>
    {note}
  </div>
);

/* ── Act card ────────────────────────────────────────────────────────────── */
export const SeoAct916: React.FC<{data: ActData}> = ({data}) => {
  const p = useP();
  return (
    <Stage>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 420, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 34, letterSpacing: '.24em', color: MUTE, fontWeight: 600, opacity: win(p, 0.05, 0.25)}}>
        {data.act.toUpperCase()}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 496, width: BOX.w * win(p, 0.15, 0.4), height: 5, backgroundColor: CLAUDE.SPARK}} />
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 548, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 118, color: CLAUDE.INK, lineHeight: 1.02, opacity: win(p, 0.3, 0.55)}}>
        {data.title}
      </div>
    </Stage>
  );
};

/* ── One hero figure ─────────────────────────────────────────────────────── */
export const SeoStat916: React.FC<{data: StatData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 250, lineHeight: 1, color: CLAUDE.SPARK, opacity: win(p, 0.12, 0.4)}}>
        {data.value}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 285, width: BOX.w * 0.6 * win(p, 0.6, 0.78), height: 5, backgroundColor: CLAUDE.SPARK}} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 325, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 42, color: CLAUDE.INK, lineHeight: 1.28, opacity: win(p, 0.45, 0.65)}}>
        {data.label}
      </div>
      <Source source={data.source} top={BOX.bottom - 150} opacity={win(p, 0.8, 0.92)} />
      <Note note={data.note} opacity={win(p, 0.86, 0.96)} />
    </Stage>
  );
};

/* ── Two figures, STACKED (was: two bars in a column) ────────────────────── */
export const SeoCompare916: React.FC<{data: CompareData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  const ROW = 300;
  const max = Math.max(...data.items.map((i) => num(i.value)), 1);
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.items.map((it, i) => {
        const g = win(p, 0.18 + i * 0.24, 0.46 + i * 0.24);
        const w = BOX.w * (num(it.value) / max) * g;
        const c = it.hot ? CLAUDE.SPARK : CLAUDE.INK;
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK, opacity: 0.35 + 0.65 * g, lineHeight: 1.2}}>
              {it.label}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + 84, width: BOX.w, height: 1, backgroundColor: RULE}} />
            <div style={{position: 'absolute', left: BOX.x, top: y + 84, width: w, height: 76, backgroundColor: c}} />
            <div style={{position: 'absolute', left: BOX.x, top: y + 172, fontFamily: CLAUDE_FONT.serif, fontSize: 76, color: c, opacity: g, lineHeight: 1}}>
              {it.value}
            </div>
          </React.Fragment>
        );
      })}
      <Source source={data.source} top={BOX.bottom - 150} opacity={win(p, 0.76, 0.9)} />
      <Note note={data.note} opacity={win(p, 0.86, 0.96)} />
    </Stage>
  );
};

/* ── The collapse, as two ROWS (was: two columns) ────────────────────────── */
export const SeoDrop916: React.FC<{data: DropData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 320;
  const H = 130;
  const drop = win(p, 0.45, 0.72);
  const fromW = BOX.w * win(p, 0.12, 0.34);
  const toW = BOX.w * (num(data.toValue) / Math.max(num(data.fromValue), 1)) * drop;
  const row = (y: number, label: string, value: string, w: number, accent: boolean, g: number) => (
    <>
      <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: MUTE, opacity: g}}>{label}</div>
      <div style={{position: 'absolute', left: BOX.x, top: y + 46, width: w, height: H, backgroundColor: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: g}} />
      <div style={{position: 'absolute', left: BOX.x, top: y + 46 + H + 14, fontFamily: CLAUDE_FONT.serif, fontSize: 88, color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: g, lineHeight: 1}}>{value}</div>
    </>
  );
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {row(TOP, data.fromLabel, data.fromValue, fromW, false, win(p, 0.12, 0.34))}
      {row(TOP + 330, data.toLabel, data.toValue, toW, true, drop)}
      <Source source={data.source} top={BOX.bottom - 150} opacity={win(p, 0.78, 0.9)} />
      <Note note={data.note} opacity={win(p, 0.86, 0.96)} />
    </Stage>
  );
};

/* ── Whole and part, stacked with more air ───────────────────────────────── */
export const SeoShare916: React.FC<{data: ShareData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 320;
  const BAND = 130;
  const wholeW = BOX.w * (num(data.wholeValue) / 100) * win(p, 0.14, 0.42);
  const partW = BOX.w * (num(data.partValue) / 100) * win(p, 0.5, 0.72);
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP, width: BOX.w, height: BAND, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP, width: wholeW, height: BAND, backgroundColor: CLAUDE.INK, opacity: 0.85}} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP + BAND + 16, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, opacity: win(p, 0.2, 0.42), lineHeight: 1.25}}>
        {data.wholeLabel}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + BAND + 62, fontFamily: CLAUDE_FONT.serif, fontSize: 76, color: CLAUDE.INK, opacity: win(p, 0.24, 0.46), lineHeight: 1}}>
        {data.wholeValue}
      </div>

      <div style={{position: 'absolute', left: BOX.x, top: TOP + 340, width: BOX.w, height: BAND, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 340, width: partW, height: BAND, backgroundColor: CLAUDE.SPARK}} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 340 + BAND + 16, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.SPARK, opacity: win(p, 0.56, 0.76), lineHeight: 1.25}}>
        {data.partLabel}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 340 + BAND + 62, fontFamily: CLAUDE_FONT.serif, fontSize: 76, color: CLAUDE.SPARK, opacity: win(p, 0.6, 0.8), lineHeight: 1}}>
        {data.partValue}
      </div>

      <Source source={data.source} top={BOX.bottom - 150} opacity={win(p, 0.78, 0.9)} />
      <Note note={data.note} opacity={win(p, 0.86, 0.96)} />
    </Stage>
  );
};

/* ── Sources: claim over citation per row (a 2-col table won't fit) ──────── */
export const SeoSources916: React.FC<{data: SourcesData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 250;
  const n = data.sources.length;
  const ROW = Math.min(150, (BOX.bottom - 120 - TOP) / n);
  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.sources.map((s, i) => {
        const g = win(p, 0.08 + i * 0.075, 0.2 + i * 0.075);
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 27, color: CLAUDE.INK, opacity: g, lineHeight: 1.2}}>
              {s.claim}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + 62, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity: g}}>
              {s.cite}
            </div>
            <div style={{position: 'absolute', left: BOX.x, top: y + ROW - 22, width: BOX.w, height: 1, backgroundColor: RULE, opacity: g}} />
          </React.Fragment>
        );
      })}
      <Note note={data.note} opacity={win(p, 0.84, 0.95)} />
    </Stage>
  );
};
