/**
 * AssistedNotAutomated.tsx — scenes for `yatra-assisted-not-automated`, a long-form
 * (deep-explainer act structure) episode on how agencies restructured around AI SEO.
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The previous three reels in this series were built under a "no invented statistics"
 * rule, and their scenes were deliberately written so that no numeric datum was
 * *renderable* — the constraint was enforced structurally rather than by memory.
 *
 * This episode inverts that. The human supplied seven verified figures and asked that
 * they be cited on screen. So these components do the opposite job, and enforce the
 * opposite discipline:
 *
 *   EVERY SCENE THAT SHOWS A FIGURE REQUIRES A `source` STRING.
 *
 * `source` is non-optional on SeoStat, SeoCompare, SeoDrop and SeoShare. A stat scene
 * cannot be authored without its citation, because the failure mode this episode is
 * most exposed to is a number drifting away from its provenance. Values are typed as
 * STRINGS ("74.2%", "65%") and rendered verbatim — never parsed, never recomputed,
 * never re-derived — so a figure on screen is always exactly what the human supplied.
 *
 * ── ACCENT SEMANTICS ─────────────────────────────────────────────────────────
 * Terracotta marks the figure that carries the argument. Citations always render in
 * muted ink: a source is provenance, not emphasis, and colouring it would make the
 * accent meaningless.
 */
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {PlainStage, Head, RULE, MUTE, win} from './claudeStage';
import {JdgSplit, JdgStakes} from './JudgmentIsTheJob';
import {DivergentFates, type FatesData} from '../deckPatterns';
import {SafeStage} from './claudeStage';

/** Reused generic shapes under this episode's names. */
export const SeoSplit = JdgSplit;      // two-column ledger
export const SeoStakes = JdgStakes;    // N items with a one-line why
export const SeoReasons = JdgStakes;
export const SeoWatch = JdgStakes;

export const SeoLead: React.FC<{data: FatesData}> = ({data}) => (
  <SafeStage>
    <DivergentFates data={data} />
  </SafeStage>
);

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/**
 * The citation line. Deliberately the same treatment everywhere so a viewer learns to
 * look in one place, and deliberately NOT in the accent colour.
 */
const SourceLine: React.FC<{source: string; top: number; opacity: number}> = ({source, top, opacity}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top, width: SAFE.w, opacity,
      fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, letterSpacing: '.04em',
    }}
  >
    Source: {source}
  </div>
);

/* ═══ Act card ═══════════════════════════════════════════════════════════ */
export type ActData = {act: string; title: string};

export const SeoAct: React.FC<{data: ActData}> = ({data}) => {
  const p = useP();
  return (
    <PlainStage>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 300, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 32, letterSpacing: '.24em', color: MUTE,
          opacity: win(p, 0.05, 0.25), fontWeight: 600,
        }}
      >
        {data.act.toUpperCase()}
      </div>
      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.y + 372, width: SAFE.w * win(p, 0.15, 0.4), height: 4, backgroundColor: CLAUDE.SPARK}} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 420, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 132, color: CLAUDE.INK, lineHeight: 1.02,
          opacity: win(p, 0.3, 0.55),
        }}
      >
        {data.title}
      </div>
    </PlainStage>
  );
};

/* ═══ One hero figure ════════════════════════════════════════════════════ */
export type StatData = {
  slideMeta: string; title: string;
  value: string;          // rendered VERBATIM — never parsed or recomputed
  label: string;
  source: string;         // REQUIRED
  note: string;
};

export const SeoStat: React.FC<{data: StatData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 300;
  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 300, lineHeight: 1,
          color: CLAUDE.SPARK, opacity: win(p, 0.12, 0.4),
          transform: `translateY(${(1 - win(p, 0.12, 0.4)) * 24}px)`,
        }}
      >
        {data.value}
      </div>
      <div style={{position: 'absolute', left: SAFE.x, top: TOP + 330, width: SAFE.w * 0.5 * win(p, 0.6, 0.78), height: 5, backgroundColor: CLAUDE.SPARK}} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 368, width: SAFE.w * 0.82,
          fontFamily: CLAUDE_FONT.ui, fontSize: 48, color: CLAUDE.INK, lineHeight: 1.25,
          opacity: win(p, 0.45, 0.65),
        }}
      >
        {data.label}
      </div>
      <SourceLine source={data.source} top={SAFE.b - 118} opacity={win(p, 0.8, 0.92)} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 62, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK,
          opacity: win(p, 0.86, 0.96),
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};

/* ═══ Two figures compared ═══════════════════════════════════════════════ */
export type CompareData = {
  slideMeta: string; title: string;
  items: {label: string; value: string; hot?: boolean}[];
  source: string;         // REQUIRED
  note: string;
};

export const SeoCompare: React.FC<{data: CompareData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 300;
  const ROW = 210;
  const TRACK = SAFE.w - 420;
  // Bar length is proportional to the leading digits ONLY so the two bars read as
  // comparable; the printed value is always the verbatim string, never this number.
  const num = (v: string) => parseFloat(v.replace(/[^0-9.]/g, '')) || 0;
  const max = Math.max(...data.items.map((i) => num(i.value)), 1);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.items.map((it, i) => {
        const g = win(p, 0.18 + i * 0.22, 0.44 + i * 0.22);
        const w = TRACK * (num(it.value) / max) * g;
        const c = it.hot ? CLAUDE.SPARK : CLAUDE.INK;
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: SAFE.x, top: y, width: SAFE.w, fontFamily: CLAUDE_FONT.ui, fontSize: 38, color: CLAUDE.INK, opacity: 0.35 + 0.65 * g}}>
              {it.label}
            </div>
            <div style={{position: 'absolute', left: SAFE.x, top: y + 58, width: TRACK, height: 1, backgroundColor: RULE}} />
            <div style={{position: 'absolute', left: SAFE.x, top: y + 58, width: w, height: 84, backgroundColor: c}} />
            <div
              style={{
                position: 'absolute', left: SAFE.x + w + 28, top: y + 60,
                fontFamily: CLAUDE_FONT.serif, fontSize: 84, color: c, opacity: g, lineHeight: 1,
              }}
            >
              {it.value}
            </div>
          </React.Fragment>
        );
      })}
      <SourceLine source={data.source} top={SAFE.b - 118} opacity={win(p, 0.76, 0.9)} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 62, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK,
          opacity: win(p, 0.86, 0.96),
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};

/* ═══ A collapse: before → after ═════════════════════════════════════════ */
export type DropData = {
  slideMeta: string; title: string;
  fromLabel: string; fromValue: string;
  toLabel: string; toValue: string;
  source: string;         // REQUIRED
  note: string;
};

export const SeoDrop: React.FC<{data: DropData}> = ({data}) => {
  const p = useP();
  const num = (v: string) => parseFloat(v.replace(/[^0-9.]/g, '')) || 0;
  const TOP = SAFE.y + 300;
  const H = 460;
  const COL = 300;
  const fromH = H;
  const toH = H * (num(data.toValue) / Math.max(num(data.fromValue), 1));
  const drop = win(p, 0.45, 0.72);

  const col = (x: number, label: string, value: string, h: number, accent: boolean, g: number) => (
    <>
      <div style={{position: 'absolute', left: x, top: TOP + H - h, width: COL, height: h, backgroundColor: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: g}} />
      <div style={{position: 'absolute', left: x, top: TOP + H - h - 108, width: COL + 200, fontFamily: CLAUDE_FONT.serif, fontSize: 96, color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity: g, lineHeight: 1}}>
        {value}
      </div>
      <div style={{position: 'absolute', left: x, top: TOP + H + 22, width: COL + 160, fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: MUTE, opacity: g}}>
        {label}
      </div>
    </>
  );

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {col(SAFE.x, data.fromLabel, data.fromValue, fromH, false, win(p, 0.12, 0.34))}
      {col(SAFE.x + 620, data.toLabel, data.toValue, toH * drop, true, drop)}
      {/* the fall, drawn as a rule from the old height to the new one */}
      <div
        style={{
          position: 'absolute', left: SAFE.x + COL + 40, top: TOP + 10,
          width: 540 * drop, height: 3, backgroundColor: CLAUDE.SPARK, opacity: drop * 0.7,
          transform: `rotate(${18 * drop}deg)`, transformOrigin: 'left center',
        }}
      />
      <SourceLine source={data.source} top={SAFE.b - 118} opacity={win(p, 0.78, 0.9)} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 62, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK,
          opacity: win(p, 0.86, 0.96),
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};

/* ═══ A whole and the small part inside it ═══════════════════════════════ */
export type ShareData = {
  slideMeta: string; title: string;
  wholeLabel: string; wholeValue: string;
  partLabel: string; partValue: string;
  source: string;         // REQUIRED
  note: string;
};

export const SeoShare: React.FC<{data: ShareData}> = ({data}) => {
  const p = useP();
  const num = (v: string) => parseFloat(v.replace(/[^0-9.]/g, '')) || 0;
  const TOP = SAFE.y + 320;
  const BAND = 150;
  const TRACK = SAFE.w;
  const wholeW = TRACK * (num(data.wholeValue) / 100) * win(p, 0.14, 0.42);
  const partW = TRACK * (num(data.partValue) / 100) * win(p, 0.5, 0.72);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {/* full-width reference track = all new pages */}
      <div style={{position: 'absolute', left: SAFE.x, top: TOP, width: TRACK, height: BAND, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: SAFE.x, top: TOP, width: wholeW, height: BAND, backgroundColor: CLAUDE.INK, opacity: 0.85}} />
      <div style={{position: 'absolute', left: SAFE.x, top: TOP + BAND + 18, width: TRACK, fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK, opacity: win(p, 0.2, 0.42)}}>
        {data.wholeLabel} — <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 46}}>{data.wholeValue}</span>
      </div>

      <div style={{position: 'absolute', left: SAFE.x, top: TOP + BAND + 150, width: TRACK, height: BAND, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: SAFE.x, top: TOP + BAND + 150, width: partW, height: BAND, backgroundColor: CLAUDE.SPARK}} />
      <div style={{position: 'absolute', left: SAFE.x, top: TOP + BAND * 2 + 168, width: TRACK, fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.SPARK, opacity: win(p, 0.56, 0.76)}}>
        {data.partLabel} — <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 46}}>{data.partValue}</span>
      </div>

      <SourceLine source={data.source} top={SAFE.b - 118} opacity={win(p, 0.78, 0.9)} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 62, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK,
          opacity: win(p, 0.86, 0.96),
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};

/* ═══ The sources card ═══════════════════════════════════════════════════ */
export type SourcesData = {
  slideMeta: string; title: string;
  sources: {claim: string; cite: string}[];
  note: string;
};

export const SeoSources: React.FC<{data: SourcesData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 250;
  const n = data.sources.length;
  const ROW = Math.min(96, (SAFE.b - 150 - TOP) / n);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.sources.map((s, i) => {
        const g = win(p, 0.08 + i * 0.075, 0.2 + i * 0.075);
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: SAFE.x, top: y, width: SAFE.w * 0.66, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.INK, opacity: g, lineHeight: 1.2}}>
              {s.claim}
            </div>
            <div style={{position: 'absolute', left: SAFE.x + SAFE.w * 0.68, top: y, width: SAFE.w * 0.32, fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, opacity: g}}>
              {s.cite}
            </div>
            <div style={{position: 'absolute', left: SAFE.x, top: y + ROW - 22, width: SAFE.w, height: 1, backgroundColor: RULE, opacity: g}} />
          </React.Fragment>
        );
      })}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 66, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: CLAUDE.INK,
          opacity: win(p, 0.84, 0.95),
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};
