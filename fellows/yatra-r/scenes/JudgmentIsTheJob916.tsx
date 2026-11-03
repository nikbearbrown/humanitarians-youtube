/**
 * JudgmentIsTheJob916.tsx — PORTRAIT (9:16) scenes for
 * `claude-liam-the-judgment-is-the-job`.
 *
 * THE COMPOSITION LOGIC (explainer SKILL.md, the Shorts law): "16:9 lays out SIDE BY
 * SIDE; 9:16 stacks TOP AND BOTTOM. Portrait relayouts re-band the same content
 * vertically — they never merely scale the landscape composition down."
 *
 * So these are not scaled clones of the landscape scenes. Each one re-bands:
 *   · JdgSplit916   — the two ledger columns become two STACKED sections.
 *   · JdgOptions916 — the 4×3 concept wall becomes 3×4.
 *   · JdgBranch916  — the two branches stack vertically instead of splaying L/R.
 *   · JdgDiverge916 — the diverging tracks become two stacked outcome bands.
 *   · JdgStakes916  — already vertical; re-spaced for the taller safe box.
 *
 * SHORTS UI KEEP-OUT: layout.ts warns that the YouTube Shorts chrome covers roughly the
 * bottom ~25% and right ~11% of the frame at runtime. So every scene here keeps its
 * essential content above y≈1440 and left of x≈960 — tighter than SAFE916 alone
 * (x 54–1026, y 96–1824) would require. The corner bug moves to the LOWER-LEFT for the
 * same reason: lower-right is where the Shorts UI lives.
 *
 * shorts.py finds these by name: it rewires `<pattern>` → `<pattern>916` when Root.tsx
 * registers one, and re-renders the beat portrait rather than centre-cropping it
 * (generated graphics are never cropped — a crop chops text mid-word).
 *
 * Same house rules as the landscape set: no numeric datum is renderable anywhere, one
 * terracotta event per beat, and it always marks JUDGMENT.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import type {SplitData, OptionsData, StakesData} from './JudgmentIsTheJob';
import type {BranchData, FatesData} from '../deckPatterns';

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';

/** Shorts-chrome-aware working box: inside SAFE916 but clear of the UI overlay. */
const BOX = {
  x: SAFE916.x,
  y: SAFE916.y,
  w: 906,          // 960 keep-out limit − SAFE916.x
  bottom: 1440,    // above the bottom-25% Shorts chrome
} as const;

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/** LOGO LAW, portrait: lower-LEFT, because the Shorts UI owns the lower-right. */
const LogoBug916: React.FC = () => (
  <div
    style={{
      position: 'absolute', left: BOX.x, top: BOX.bottom + 40,
      fontFamily: CLAUDE_FONT.serif, fontSize: 30, color: CLAUDE.INK,
      opacity: 0.3, letterSpacing: '.04em',
    }}
  >
    @Yatra
  </div>
);

const Stage916: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    {children}
    <LogoBug916 />
  </AbsoluteFill>
);

const Head916: React.FC<{meta: string; title: string}> = ({meta, title}) => (
  <>
    <div
      style={{
        position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w,
        fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em',
        color: MUTE, fontWeight: 600,
      }}
    >
      {meta.toUpperCase()}
    </div>
    <div
      style={{
        position: 'absolute', left: BOX.x, top: BOX.y + 76, width: BOX.w,
        fontFamily: CLAUDE_FONT.serif, fontSize: 88, color: CLAUDE.INK, lineHeight: 1.04,
      }}
    >
      {title}
    </div>
  </>
);

/* ── B01 — two STACKED outcome bands (was: diverging tracks) ─────────────── */
export const JdgDiverge916: React.FC<{data: FatesData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  const BAND = 380;
  return (
    <Stage916>
      <Head916 meta={data.slideMeta} title={data.startLabel} />
      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP - 62, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.SPARK,
          letterSpacing: '.08em', opacity: win(p, 0.1, 0.22),
        }}
      >
        {data.splitLabel.toUpperCase()} ↓
      </div>
      {data.tracks.map((t, i) => {
        const accent = t.tone === 'warn';
        const g = win(p, 0.26 + i * 0.3, 0.5 + i * 0.3);
        const y = TOP + i * (BAND + 40);
        return (
          <div key={i} style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, opacity: g}}>
            <div style={{width: 12, height: 64 * g, backgroundColor: accent ? CLAUDE.SPARK : CLAUDE.INK}} />
            <div style={{marginTop: 18, fontFamily: CLAUDE_FONT.ui, fontSize: 60, color: accent ? CLAUDE.SPARK : CLAUDE.INK}}>
              {t.label}
            </div>
            <div style={{marginTop: 10, fontFamily: CLAUDE_FONT.serif, fontSize: 52, color: accent ? CLAUDE.SPARK : MUTE}}>
              {t.outcome}
            </div>
            <div style={{marginTop: 22, display: 'flex', flexWrap: 'wrap', gap: '14px 26px'}}>
              {t.notes.map((n, j) => (
                <span key={j} style={{fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE}}>· {n}</span>
              ))}
            </div>
          </div>
        );
      })}
    </Stage916>
  );
};

/* ── B02 — the ledger, STACKED (was: side-by-side columns) ───────────────── */
export const JdgSplit916: React.FC<{data: SplitData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  const section = (
    side: {heading: string; items: string[]},
    y: number,
    accent: boolean,
    from: number,
  ) => (
    <>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: y, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, letterSpacing: '.1em', fontWeight: 600,
          color: accent ? CLAUDE.SPARK : MUTE, opacity: win(p, from - 0.06, from),
        }}
      >
        {side.heading.toUpperCase()}
      </div>
      {side.items.map((it, i) => {
        const g = win(p, from + i * 0.05, from + 0.05 + i * 0.05);
        return (
          <div key={i} style={{position: 'absolute', left: BOX.x, top: y + 58 + i * 78, width: BOX.w, opacity: g}}>
            <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 44, color: accent ? CLAUDE.SPARK : CLAUDE.INK}}>
              {it}
            </div>
            <div style={{marginTop: 14, width: BOX.w, height: 1, backgroundColor: RULE}} />
          </div>
        );
      })}
    </>
  );
  return (
    <Stage916>
      <Head916 meta={data.slideMeta} title={data.title} />
      {section(data.left, TOP, false, 0.2)}
      {section(data.right, TOP + 420, true, 0.56)}
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 84, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 42, color: CLAUDE.INK, lineHeight: 1.25,
          opacity: win(p, 0.86, 0.95),
        }}
      >
        {data.note}
      </div>
    </Stage916>
  );
};

/* ── B04 — the concept wall, 3 across × 4 down (was: 4 × 3) ──────────────── */
export const JdgOptions916: React.FC<{data: OptionsData}> = ({data}) => {
  const p = useP();
  const COLS = 3;
  const GAP = 20;
  const CARD_W = (BOX.w - GAP * (COLS - 1)) / COLS;
  const TOP = BOX.y + 300;
  const rows = Math.ceil(data.options.length / COLS);
  const CARD_H = Math.min(200, (BOX.bottom - 110 - TOP - GAP * (rows - 1)) / rows);
  const chose = win(p, 0.78, 0.9);
  return (
    <Stage916>
      <Head916 meta={data.slideMeta} title={data.title} />
      {data.options.map((label, i) => {
        const c = i % COLS, r = Math.floor(i / COLS);
        const g = win(p, 0.08 + i * 0.032, 0.16 + i * 0.032);
        const ring = i === data.chosenIndex ? chose : 0;
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: BOX.x + c * (CARD_W + GAP),
              top: TOP + r * (CARD_H + GAP),
              width: CARD_W, height: CARD_H,
              backgroundColor: '#FFFFFF',
              border: `${1 + 4 * ring}px solid ${ring > 0 ? CLAUDE.SPARK : '#E5E2D9'}`,
              borderRadius: 10, opacity: g,
              transform: `scale(${0.94 + 0.06 * g})`,
              display: 'flex', alignItems: 'flex-end',
              boxSizing: 'border-box', padding: 16,
            }}
          >
            <div
              style={{
                fontFamily: CLAUDE_FONT.ui, fontSize: 26, lineHeight: 1.2,
                color: ring > 0 ? CLAUDE.SPARK : CLAUDE.INK, overflow: 'hidden',
              }}
            >
              {label}
            </div>
          </div>
        );
      })}
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 74, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 44, color: CLAUDE.INK,
          opacity: win(p, 0.9, 0.97),
        }}
      >
        {data.caption}
      </div>
    </Stage916>
  );
};

/* ── B05 — the two branches STACKED (was: splayed left/right) ────────────── */
export const JdgBranch916: React.FC<{data: BranchData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  return (
    <Stage916>
      <Head916 meta={data.slideMeta} title={data.question} />
      {data.branches.map((b, i) => {
        const accent = b.tone !== 'good';
        const g = win(p, 0.22 + i * 0.28, 0.44 + i * 0.28);
        const y = TOP + i * 330;
        return (
          <div key={i} style={{position: 'absolute', left: BOX.x, top: y, width: BOX.w, opacity: g}}>
            <div style={{display: 'flex', gap: 20}}>
              <div style={{width: 10, backgroundColor: accent ? CLAUDE.SPARK : CLAUDE.INK, alignSelf: 'stretch'}} />
              <div style={{flex: 1}}>
                <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 52, color: accent ? CLAUDE.SPARK : CLAUDE.INK, lineHeight: 1.15}}>
                  {b.label}
                </div>
                <div style={{marginTop: 14, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, lineHeight: 1.3}}>
                  {b.detail}
                </div>
                <div style={{marginTop: 14, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, lineHeight: 1.3}}>
                  → {b.fix}
                </div>
              </div>
            </div>
          </div>
        );
      })}
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 150, width: BOX.w, opacity: win(p, 0.84, 0.94)}}>
        <div style={{width: BOX.w, height: 2, backgroundColor: CLAUDE.SPARK}} />
        <div style={{marginTop: 18, fontFamily: CLAUDE_FONT.serif, fontSize: 44, color: CLAUDE.INK, lineHeight: 1.2}}>
          {data.resolver.label}
        </div>
      </div>
    </Stage916>
  );
};

/* ── B06 — four stakes, re-spaced for the taller box ─────────────────────── */
export const JdgStakes916: React.FC<{data: StakesData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  const n = data.items.length;
  const ROW = Math.min(230, (BOX.bottom - 120 - TOP) / n);
  return (
    <Stage916>
      <Head916 meta={data.slideMeta} title={data.title} />
      {data.items.map((it, i) => {
        const g = win(p, 0.1 + i * 0.15, 0.24 + i * 0.15);
        const whyG = win(p, 0.2 + i * 0.15, 0.34 + i * 0.15);
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y + 10, width: 12, height: 56 * g, backgroundColor: CLAUDE.SPARK}} />
            <div
              style={{
                position: 'absolute', left: BOX.x + 40, top: y, width: BOX.w - 40,
                fontFamily: CLAUDE_FONT.ui, fontSize: 50, color: CLAUDE.INK,
                lineHeight: 1.15, opacity: g,
              }}
            >
              {it.label}
            </div>
            <div
              style={{
                position: 'absolute', left: BOX.x + 40, top: y + 122, width: BOX.w - 60,
                fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE,
                lineHeight: 1.28, opacity: whyG,
              }}
            >
              {it.why}
            </div>
          </React.Fragment>
        );
      })}
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 84, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK, lineHeight: 1.25,
          opacity: win(p, 0.88, 0.96),
        }}
      >
        {data.closer}
      </div>
    </Stage916>
  );
};
