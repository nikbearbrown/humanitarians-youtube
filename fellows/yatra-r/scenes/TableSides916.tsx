/**
 * TableSides916.tsx — PORTRAIT (9:16) scenes for `yatra-both-sides-of-the-table`.
 *
 * Re-banded vertically per the Shorts law's composition logic, NOT scaled clones.
 * Five of the landscape layouts are horizontal by nature and are genuinely rebuilt:
 *
 *   · TblTable916  — the two sides become TOP and BOTTOM. The table stays a horizontal
 *                    bar across the middle, the company and its AI sit above it, the
 *                    candidate and their AI below, and the machine-to-machine traffic
 *                    runs VERTICALLY through the table. Four seats across 972px would
 *                    be 230px each, which cannot hold "its screening AI".
 *   · TblWalk916   — the row of applicant marks wraps to two rows (25 marks at 66px
 *                    is 1650px wide); the leaving share still departs DOWNWARD out of
 *                    the row, so the motion still reads as withdrawing rather than
 *                    being filtered.
 *   · TblTrust916  — the two figures STACK, each keeping its own separate citation.
 *   · TblInject916 — the page sits above its figure instead of beside it.
 *   · TblSide916   — the "other side of the table" ghost moves BELOW the active side.
 *
 * Every refusal holds, because the types are imported from TableSides.tsx rather than
 * redeclared: `source` is still required on every figure-bearing scene (and still
 * PER-FIGURE on TblTrust916, which carries two studies), `value` is still a verbatim
 * string with a separate numeric `bar`, `TblInject916` still requires its `stamp`,
 * `TblInterview916` still requires its `deltaNote`, and no remainder is ever captioned.
 *
 * KEEP-OUT: content stays above y≈1440 and left of x≈960 — the Shorts/Reels chrome
 * region — with the brand bug lower-left.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import type {
  BlufData, SideData, TableData, InterviewData, WalkData, TrustData, TrustFigure,
  InjectData, LimitsData,
} from './TableSides';

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';
const BOX = {x: SAFE916.x, y: SAFE916.y, w: 972, keep: 960, bottom: 1440} as const;

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

const Stage: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{backgroundColor: STAGE}}>
    {children}
    <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom + 40, fontFamily: CLAUDE_FONT.serif, fontSize: 30, color: CLAUDE.INK, opacity: 0.3, letterSpacing: '.04em'}}>
      @Yatra
    </div>
  </AbsoluteFill>
);

const Eyebrow: React.FC<{text: string; opacity?: number}> = ({text, opacity = 1}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600, opacity}}>
    {text.toUpperCase()}
  </div>
);

const Head: React.FC<{meta: string; title: string}> = ({meta, title}) => (
  <>
    <Eyebrow text={meta} />
    <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 76, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 72, color: CLAUDE.INK, lineHeight: 1.06}}>
      {title}
    </div>
  </>
);

const Note: React.FC<{note: string; opacity: number; accent?: boolean}> = ({note, opacity, accent}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 96, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: accent ? CLAUDE.SPARK : CLAUDE.INK, lineHeight: 1.25, opacity}}>
    {note}
  </div>
);

const SourceLine: React.FC<{source: string; opacity: number; top?: number; left?: number; width?: number}> =
({source, opacity, top, left, width}) => (
  <div style={{position: 'absolute', left: left ?? BOX.x, top: top ?? BOX.bottom - 166, width: width ?? BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, opacity, lineHeight: 1.3}}>
    Source: {source}
  </div>
);

const Chip: React.FC<{
  text: string; left: number; top: number; hot?: boolean; opacity: number; size?: number;
}> = ({text, left, top, hot, opacity, size = 24}) => (
  <div
    style={{
      position: 'absolute', left, top, opacity,
      fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600,
      letterSpacing: '.14em', textTransform: 'uppercase' as const,
      color: hot ? CLAUDE.SPARK : MUTE,
      border: `1px solid ${hot ? CLAUDE.SPARK : RULE}`,
      padding: '9px 15px', display: 'inline-block', whiteSpace: 'nowrap' as const,
    }}
  >
    {text}
  </div>
);

/* ── B01 — claims stack; the rule alternates sides to keep the "two sides" read ── */
export const TblBluf916: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 220;
  const STEP = 330;

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.16)} />
      {data.claims.map((c, i) => {
        const g = win(p, 0.08 + i * 0.26, 0.34 + i * 0.26);
        const hot = i === data.hotIndex;
        const y = TOP + i * STEP;
        const right = c.align === 'right';
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: right ? BOX.x + BOX.w - 8 : BOX.x, top: y,
                width: 8, height: 230 * g, backgroundColor: hot ? CLAUDE.SPARK : RULE,
              }}
            />
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y, width: BOX.w,
                textAlign: right ? 'right' : 'left',
                paddingRight: right ? 34 : 0, paddingLeft: right ? 0 : 34,
                boxSizing: 'border-box',
                fontFamily: CLAUDE_FONT.serif, fontSize: 72, lineHeight: 1.16,
                color: hot ? CLAUDE.SPARK : CLAUDE.INK, opacity: g,
                transform: `translateY(${(1 - g) * 18}px)`,
              }}
            >
              {c.label}
            </div>
          </React.Fragment>
        );
      })}
      <Note note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </Stage>
  );
};

/* ── B02 / B03 — the ghost side moves BELOW the active one ───────────────── */
export const TblSide916: React.FC<{data: SideData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 160;
  const set = win(p, 0.26, 0.46);
  const fill = win(p, 0.42, 0.68);

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      <div style={{position: 'absolute', left: BOX.x, top: TOP, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.14em', color: MUTE, fontWeight: 600, opacity: win(p, 0.06, 0.2)}}>
        {data.head.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP + 60, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 190, lineHeight: 1,
          color: CLAUDE.INK, opacity: set, transform: `translateY(${(1 - set) * 20}px)`,
        }}
      >
        {data.value}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 280, width: BOX.w, height: 54, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: BOX.x + 1, top: TOP + 281, width: (BOX.w - 2) * (data.bar / 100) * fill, height: 52, backgroundColor: CLAUDE.INK, opacity: 0.85}} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 356, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK, lineHeight: 1.3, opacity: win(p, 0.56, 0.72)}}>
        {data.label}
      </div>
      <Chip text={data.qualifier} left={BOX.x} top={TOP + 470} opacity={win(p, 0.68, 0.82)} size={24} />

      {/* the other side: present, below, not this beat's subject */}
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 580, width: BOX.w, height: 220, border: `1px dashed ${RULE}`, borderRadius: 14, opacity: 0.5}} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 672, width: BOX.w, textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, opacity: 0.55}}>
        the other side of the table
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.8, 0.92)} />
      <Note note={data.note} opacity={win(p, 0.88, 0.98)} />
    </Stage>
  );
};

/* ── B05 — the two sides become TOP and BOTTOM; traffic runs vertically ──── */
export const TblTable916: React.FC<{data: TableData}> = ({data}) => {
  const p = useP();
  const MID_Y = BOX.y + 700;
  const draw = win(p, 0.06, 0.2);
  const topIn = win(p, 0.18, 0.36);
  const botIn = win(p, 0.34, 0.52);
  const traffic = win(p, 0.56, 0.78);
  const pushBack = win(p, 0.74, 0.9);
  const humanDim = 1 - 0.42 * pushBack;

  const seat = (y: number, label: string, g: number, machine: boolean, dim: number) => (
    <div
      style={{
        position: 'absolute', left: BOX.x + 106, top: y, width: BOX.w - 212, minHeight: 112,
        boxSizing: 'border-box',
        border: `2px solid ${machine ? CLAUDE.INK : RULE}`,
        backgroundColor: '#FFFFFF', borderRadius: 12,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        padding: '14px 18px', textAlign: 'center',
        fontFamily: CLAUDE_FONT.ui, fontSize: 34, lineHeight: 1.22,
        color: CLAUDE.INK, opacity: g * dim,
      }}
    >
      {label}
    </div>
  );

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* QC: the whole stack was re-spaced. Previously the outer (human) seats were
          pushed 90px outward from y+230 and y+960, which drove the top seat into the
          TITLE and the bottom seat into the VERDICT line at full push. The rows below
          are spaced so that, even at pushBack = 1, the top seat clears the title and
          the bottom seat clears the verdict. */}
      {seat(BOX.y + 240 - 40 * pushBack, data.leftOuter, draw, false, humanDim)}
      {seat(BOX.y + 430, data.leftInner, topIn, true, 1)}

      {/* the table — the two machine seats sit either side of it */}
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.y + 620,
          width: BOX.w * draw, height: 80,
          backgroundColor: '#FFFFFF', border: `2px solid ${CLAUDE.INK}`, borderRadius: 10,
        }}
      />

      {seat(BOX.y + 810, data.rightInner, botIn, true, 1)}
      {seat(BOX.y + 980 + 30 * pushBack, data.rightOuter, draw, false, humanDim)}

      {/* the only live exchange: machine ↔ machine, straight through the table */}
      <div
        style={{
          position: 'absolute', left: BOX.x + BOX.w / 2 - 3, top: BOX.y + 542,
          width: 6, height: (810 - 542) * traffic,
          backgroundColor: CLAUDE.SPARK, opacity: 0.9,
        }}
      />
      <div
        style={{
          position: 'absolute', left: BOX.x + BOX.w / 2 + 28, top: BOX.y + 640,
          width: 380, fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: CLAUDE.SPARK,
          opacity: win(p, 0.66, 0.8), lineHeight: 1.25,
        }}
      >
        {data.trafficLabel}
      </div>

      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 190, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 52, color: CLAUDE.SPARK, lineHeight: 1.2,
          opacity: win(p, 0.86, 0.96),
        }}
      >
        {data.verdict}
      </div>
      <Note note={data.note} opacity={win(p, 0.92, 1.0)} />
    </Stage>
  );
};

/* ── B06 — stacked; same delta-only discipline ───────────────────────────── */
export const TblInterview916: React.FC<{data: InterviewData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 220;
  const set = win(p, 0.06, 0.26);
  const fill = win(p, 0.3, 0.52);

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 230, lineHeight: 1,
          color: CLAUDE.INK, opacity: set, transform: `translateY(${(1 - set) * 22}px)`,
        }}
      >
        {data.value}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 258, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 38, color: CLAUDE.INK, lineHeight: 1.28, opacity: win(p, 0.24, 0.42)}}>
        {data.label}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 400, width: BOX.w, height: 48, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
      <div style={{position: 'absolute', left: BOX.x + 1, top: TOP + 401, width: (BOX.w - 2) * (data.bar / 100) * fill, height: 46, backgroundColor: CLAUDE.INK, opacity: 0.85}} />

      <Chip text={data.delta} left={BOX.x} top={TOP + 490} hot opacity={win(p, 0.6, 0.76)} size={30} />
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 580, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, lineHeight: 1.32, opacity: win(p, 0.72, 0.86)}}>
        {data.deltaNote}
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.82, 0.92)} />
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B07 — the marks wrap to two rows; the leaving share still departs down ─ */
const WALK_MARKS = 25;
const PER_ROW = 13;

export const TblWalk916: React.FC<{data: WalkData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 200;
  const leave = win(p, 0.34, 0.6);
  const leaving = Math.round((data.bar / 100) * WALK_MARKS);

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      {Array.from({length: WALK_MARKS}).map((_, i) => {
        const goes = i >= WALK_MARKS - leaving;
        const g = win(p, 0.06 + i * 0.006, 0.2 + i * 0.006);
        const off = goes ? leave : 0;
        const col = i % PER_ROW;
        const row = Math.floor(i / PER_ROW);
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: BOX.x + col * 74,
              top: TOP + row * 130 + off * 150,
              width: 46, height: 92, borderRadius: 8,
              backgroundColor: goes && leave > 0.1 ? CLAUDE.SPARK : CLAUDE.INK,
              opacity: (goes ? 1 - 0.45 * off : 0.82) * g,
            }}
          />
        );
      })}

      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP + 440, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 200, lineHeight: 1,
          color: CLAUDE.SPARK, opacity: win(p, 0.5, 0.68),
        }}
      >
        {data.value}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 660, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 36, color: CLAUDE.INK, lineHeight: 1.3, opacity: win(p, 0.6, 0.76)}}>
        {data.label}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: TOP + 800, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 52, color: CLAUDE.SPARK, opacity: win(p, 0.8, 0.92)}}>
        {data.verdict}
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B08 — the two figures STACK, each keeping its own citation ──────────── */
export const TblTrust916: React.FC<{data: TrustData}> = ({data}) => {
  const p = useP();
  const TOP_A = BOX.y + 230;
  const TOP_B = BOX.y + 760;

  const col = (y: number, f: TrustFigure, at: number) => {
    const set = win(p, at, at + 0.16);
    const fill = win(p, at + 0.1, at + 0.3);
    return (
      <>
        <div
          style={{
            position: 'absolute', left: BOX.x, top: y, width: BOX.w,
            fontFamily: CLAUDE_FONT.serif, fontSize: 170, lineHeight: 1,
            color: CLAUDE.SPARK, opacity: set, transform: `translateY(${(1 - set) * 18}px)`,
          }}
        >
          {f.value}
        </div>
        <div style={{position: 'absolute', left: BOX.x, top: y + 198, width: BOX.w, height: 46, border: `1px solid ${RULE}`, boxSizing: 'border-box'}} />
        <div style={{position: 'absolute', left: BOX.x + 1, top: y + 199, width: (BOX.w - 2) * (f.bar / 100) * fill, height: 44, backgroundColor: CLAUDE.SPARK, opacity: 0.85}} />
        <div style={{position: 'absolute', left: BOX.x, top: y + 268, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, lineHeight: 1.3, opacity: win(p, at + 0.18, at + 0.34)}}>
          {f.label}
        </div>
        <SourceLine source={f.source} opacity={win(p, at + 0.3, at + 0.44)} top={y + 390} />
      </>
    );
  };

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {col(TOP_A, data.left, 0.08)}
      {col(TOP_B, data.right, 0.44)}
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B09 — the page sits ABOVE its figure ────────────────────────────────── */
export const TblInject916: React.FC<{data: InjectData}> = ({data}) => {
  const p = useP();
  const PAGE_X = BOX.x;
  const PAGE_W = BOX.w;
  const PAGE_Y = BOX.y + 150;
  const PAGE_H = 620;
  const draw = win(p, 0.06, 0.24);
  const hidden = win(p, 0.36, 0.58);

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      <div style={{position: 'absolute', left: PAGE_X, top: PAGE_Y, width: PAGE_W, height: PAGE_H, backgroundColor: '#FFFFFF', border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 10, opacity: draw}} />
      {data.visibleLines.map((ln, i) => (
        <React.Fragment key={i}>
          <div
            style={{
              position: 'absolute', left: PAGE_X + 44, top: PAGE_Y + 50 + i * 128,
              fontFamily: CLAUDE_FONT.ui, fontSize: 30, fontWeight: 600, color: CLAUDE.INK,
              opacity: win(p, 0.1 + i * 0.04, 0.26 + i * 0.04),
            }}
          >
            {ln}
          </div>
          {[0, 1].map((k) => (
            <div
              key={k}
              style={{
                position: 'absolute', left: PAGE_X + 44, top: PAGE_Y + 96 + i * 128 + k * 26,
                width: (PAGE_W - 120) * (k === 1 ? 0.62 : 1), height: 10, borderRadius: 3,
                backgroundColor: CLAUDE.INK, opacity: 0.16 * win(p, 0.12 + i * 0.04, 0.3 + i * 0.04),
              }}
            />
          ))}
        </React.Fragment>
      ))}

      <div
        style={{
          position: 'absolute', left: PAGE_X + 44, top: PAGE_Y + 452, width: PAGE_W - 88,
          padding: '18px 20px', boxSizing: 'border-box',
          border: `2px dashed ${CLAUDE.SPARK}`, borderRadius: 8,
          fontFamily: CLAUDE_FONT.mono, fontSize: 24, lineHeight: 1.35,
          color: CLAUDE.SPARK, opacity: hidden,
        }}
      >
        {data.hiddenLabel}
      </div>

      <div
        style={{
          position: 'absolute', left: BOX.x, top: PAGE_Y + PAGE_H + 50, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 190, lineHeight: 1,
          color: CLAUDE.SPARK, opacity: win(p, 0.66, 0.82),
        }}
      >
        {data.value}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: PAGE_Y + PAGE_H + 250, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: CLAUDE.INK, lineHeight: 1.3,
          opacity: win(p, 0.74, 0.88),
        }}
      >
        {data.label}
      </div>
      <Chip text={data.stamp} left={BOX.x} top={PAGE_Y + PAGE_H + 370} opacity={win(p, 0.8, 0.92)} size={24} />

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B10 — the two ledgers STACK into two labelled groups ────────────────── */
export const TblLimits916: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const G1_Y = BOX.y + 240;
  const G2_Y = BOX.y + 700;
  const STEP = 120;

  const ledger = (y: number, heading: string, items: string[], startAt: number, hot: boolean) => (
    <>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: y, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 27, letterSpacing: '.16em', fontWeight: 600,
          color: hot ? CLAUDE.SPARK : MUTE, opacity: win(p, startAt, startAt + 0.08),
        }}
      >
        {heading.toUpperCase()}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: y + 42, width: BOX.w * win(p, startAt, startAt + 0.12), height: 2, backgroundColor: hot ? CLAUDE.SPARK : RULE}} />
      {items.map((it, i) => {
        const g = win(p, startAt + 0.05 + i * 0.07, startAt + 0.2 + i * 0.07);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: BOX.x, top: y + 74 + i * STEP, width: BOX.w,
              fontFamily: CLAUDE_FONT.ui, fontSize: 33, lineHeight: 1.3,
              color: hot ? CLAUDE.SPARK : CLAUDE.INK,
              opacity: g, transform: `translateY(${(1 - g) * 12}px)`,
            }}
          >
            · {it}
          </div>
        );
      })}
    </>
  );

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />
      {ledger(G1_Y, data.claims.heading, data.claims.items, 0.08, false)}
      {ledger(G2_Y, data.refusals.heading, data.refusals.items, 0.44, true)}

      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 250, width: BOX.w * win(p, 0.76, 0.86), height: 1, backgroundColor: RULE}} />
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 230, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 25, color: MUTE, lineHeight: 1.36,
          opacity: win(p, 0.78, 0.9),
        }}
      >
        {data.provenance}
      </div>
      <Note note={data.falsifier} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};
