/**
 * InterestMedia916.tsx — PORTRAIT (9:16) scenes for `yatra-interest-media`.
 *
 * Re-banded vertically per the Shorts law's composition logic, NOT scaled clones.
 * Five of the landscape layouts are horizontal by nature and are genuinely rebuilt:
 *
 *   · ItmSource916   — the rename STACKS (old word above, new word below) instead of
 *                      sitting side by side; two 96px words will not fit across 972px.
 *   · ItmFeed916     — the two columns become two STACKED GROUPS, and the signal rail
 *                      moves between them so the wire still points at the group it
 *                      explains (now downward instead of upward).
 *   · ItmQuestion916 — the machine runs TOP → BOTTOM: posts enter from above, the
 *                      keyed slot sits mid-frame, the feed leaves below.
 *   · ItmModels916   — each track becomes a VERTICAL chain and the two tracks sit
 *                      side by side, so the gate/no-gate comparison is still read in
 *                      one glance. The gate becomes a horizontal barrier across the
 *                      left chain.
 *   · ItmLimits916   — the two ledgers stack into two labelled groups; a two-column
 *                      ledger is unreadable at portrait width.
 *
 * The two refusals hold here because they live in the shared types imported from
 * InterestMedia.tsx: there is still no `quote` prop (so the source cannot be made to
 * say anything), and still no numeric prop anywhere (so no figure can reach either
 * cut). MARKS and TICKS are imported rather than redeclared so the two cuts of one
 * reel cannot silently disagree about density.
 *
 * KEEP-OUT: content stays above y≈1440 and left of x≈960 — the Shorts/Reels chrome
 * region — with the brand bug lower-left.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {MARKS, NODES, TICKS, rnd} from './InterestMedia';
import type {
  BlufData, SourceData, FeedData, VolumeData, QuestionData, ModelsData, JobData, LimitsData,
} from './InterestMedia';

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';
/** working box: full safe width, but critical content is kept left of x≈960 */
const BOX = {x: SAFE916.x, y: SAFE916.y, w: 972, keep: 960, bottom: 1440} as const;

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));

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

const Eyebrow: React.FC<{text: string; opacity?: number}> = ({text, opacity = 1}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600, opacity}}>
    {text.toUpperCase()}
  </div>
);

const Head: React.FC<{meta: string; title: string}> = ({meta, title}) => (
  <>
    <Eyebrow text={meta} />
    <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 76, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 74, color: CLAUDE.INK, lineHeight: 1.06}}>
      {title}
    </div>
  </>
);

const Note: React.FC<{note: string; opacity: number; accent?: boolean}> = ({note, opacity, accent}) => (
  <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 96, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: accent ? CLAUDE.SPARK : CLAUDE.INK, lineHeight: 1.25, opacity}}>
    {note}
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

/* ── B01 — three claims; already vertical, so this one re-spaces rather than rebuilds ── */
export const ItmBluf916: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 220;
  const STEP = 330;

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.16)} />
      {data.claims.map((c, i) => {
        const g = win(p, 0.08 + i * 0.28, 0.34 + i * 0.28);
        const hot = i === data.hotIndex;
        const y = TOP + i * STEP;
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: BOX.x, top: y, width: 8, height: 230 * g, backgroundColor: hot ? CLAUDE.SPARK : RULE}} />
            <div
              style={{
                position: 'absolute', left: BOX.x + 48, top: y, width: BOX.w - 60,
                fontFamily: CLAUDE_FONT.serif, fontSize: 74, lineHeight: 1.15,
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

/* ── B02 — attribution card, then the rename STACKED (old above, new below) ── */
export const ItmSource916: React.FC<{data: SourceData}> = ({data}) => {
  const p = useP();
  const card = win(p, 0.06, 0.24);
  const band = win(p, 0.18, 0.36);
  const strike = win(p, 0.44, 0.60);
  const arrive = win(p, 0.56, 0.72);
  const qOld = win(p, 0.72, 0.84);
  const qNew = win(p, 0.86, 0.96);

  const OLD_Y = BOX.y + 620;
  const NEW_Y = BOX.y + 900;

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={card} />

      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.y + 80, width: BOX.w,
          backgroundColor: '#FFFFFF', border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 14,
          padding: '34px 36px', boxSizing: 'border-box', opacity: card,
          transform: `translateY(${(1 - card) * 16}px)`,
        }}
      >
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 62, color: CLAUDE.INK, lineHeight: 1.1}}>
          {data.who}
        </div>
        <div style={{marginTop: 18, fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: MUTE, lineHeight: 1.32, opacity: band}}>
          {data.claimParaphrase}
        </div>
      </div>
      <Chip text={data.stamp} left={BOX.x} top={BOX.y + 480} opacity={band} />

      {/* old — struck */}
      <div style={{position: 'absolute', left: BOX.x, top: OLD_Y, opacity: card}}>
        <div style={{position: 'relative', display: 'inline-block'}}>
          <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 92, color: CLAUDE.INK}}>{data.oldWord}</span>
          <div style={{position: 'absolute', left: 0, top: 63, width: `${100 * strike}%`, height: 6, backgroundColor: CLAUDE.INK}} />
        </div>
        <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 92, color: MUTE, marginLeft: 20}}>{data.tail}</span>
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: OLD_Y + 132, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 40, color: MUTE, opacity: qOld}}>
        {data.oldAsks}
      </div>

      {/* new — THE accent */}
      <div style={{position: 'absolute', left: BOX.x, top: NEW_Y, opacity: arrive, transform: `translateY(${(1 - arrive) * 22}px)`}}>
        <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 92, color: CLAUDE.SPARK}}>{data.newWord}</span>
        <span style={{fontFamily: CLAUDE_FONT.serif, fontSize: 92, color: MUTE, marginLeft: 20}}>{data.tail}</span>
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: NEW_Y + 132, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 40, color: CLAUDE.INK, opacity: qNew}}>
        {data.newAsks}
      </div>

      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B03 — the two columns become two STACKED groups; the wire now points DOWN ── */
export const ItmFeed916: React.FC<{data: FeedData}> = ({data}) => {
  const p = useP();
  const CARD_H = 104;
  const GAP = 16;
  const TOP_Y = BOX.y + 130;
  const RAIL_Y = BOX.y + 640;
  const BOT_Y = BOX.y + 830;

  const dim = 1 - 0.58 * win(p, 0.32, 0.48);

  const group = (
    y: number, head: string, items: string[], foot: string,
    startAt: number, opacityScale: number, marked: boolean,
  ) => (
    <>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: y - 56, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.14em',
          color: MUTE, fontWeight: 600, opacity: opacityScale * win(p, startAt, startAt + 0.1),
        }}
      >
        {head.toUpperCase()}
      </div>
      {items.map((it, i) => {
        const g = win(p, startAt + 0.04 + i * 0.06, startAt + 0.18 + i * 0.06);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: BOX.x, top: y + i * (CARD_H + GAP), width: BOX.w,
              height: CARD_H, boxSizing: 'border-box',
              backgroundColor: '#FFFFFF', border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 12,
              padding: '26px 28px',
              fontFamily: CLAUDE_FONT.serif, fontSize: 42, color: CLAUDE.INK,
              opacity: opacityScale * g, transform: `translateY(${(1 - g) * 14}px)`,
              overflow: 'hidden', whiteSpace: 'nowrap', textOverflow: 'ellipsis',
            }}
          >
            {it}
          </div>
        );
      })}
      <div
        style={{
          position: 'absolute', left: BOX.x, top: y + items.length * (CARD_H + GAP) + 8,
          width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 30,
          color: marked ? CLAUDE.INK : MUTE,
          opacity: opacityScale * win(p, startAt + 0.24, startAt + 0.36),
        }}
      >
        {foot}
      </div>
    </>
  );

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />
      {group(TOP_Y, data.leftHead, data.leftItems, data.leftFoot, 0.08, dim, false)}

      {/* the signal rail sits BETWEEN the groups in portrait */}
      <div style={{position: 'absolute', left: BOX.x, top: RAIL_Y - 22, width: BOX.w * win(p, 0.68, 0.78), height: 1, backgroundColor: RULE}} />
      {data.signals.map((s, i) => (
        <Chip key={i} text={s} left={BOX.x + i * 300} top={RAIL_Y} opacity={win(p, 0.70 + i * 0.06, 0.80 + i * 0.06)} size={25} />
      ))}

      {group(BOT_Y, data.rightHead, data.rightItems, data.rightFoot, 0.48, 1, true)}

      {/* the ONE accent: the wire runs DOWN from the rail into the group it explains */}
      <div
        style={{
          position: 'absolute', left: BOX.x + 300, top: RAIL_Y + 62,
          width: 5, height: 108 * win(p, 0.86, 0.96), backgroundColor: CLAUDE.SPARK,
        }}
      />
      <div
        style={{
          position: 'absolute', left: BOX.x + 300, top: RAIL_Y + 170,
          width: 5 + 70 * win(p, 0.88, 0.97), height: 5,
          backgroundColor: CLAUDE.SPARK, opacity: win(p, 0.88, 0.97),
        }}
      />

      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B04 — the flood fills the tall field; same density constant as landscape ── */
export const ItmVolume916: React.FC<{data: VolumeData}> = ({data}) => {
  const p = useP();
  const flood = win(p, 0.22, 0.80);
  const give = win(p, 0.68, 0.84);
  const bandG = win(p, 0.84, 0.95);

  const FIELD_TOP = BOX.y + 300;
  const FIELD_H = 900;
  const RING_CX = BOX.x + 486;
  const RING_CY = FIELD_TOP + 300;
  const RING_R = 150;

  return (
    <Stage>
      <Head meta={data.slideMeta} title={data.title} />

      {Array.from({length: MARKS}).map((_, i) => {
        const ax = rnd(i * 3 + 1);
        const ay = rnd(i * 3 + 2);
        const aw = rnd(i * 3 + 3);
        const arrive = Math.min(1, Math.max(0, (flood - ax * 0.85) / 0.15));
        if (arrive <= 0) return null;
        const x = BOX.x + ax * (BOX.w - 110);
        const y = FIELD_TOP + ay * (FIELD_H - 30);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: x, top: y - (1 - arrive) * 90,
              width: 48 + aw * 58, height: 11,
              backgroundColor: CLAUDE.INK, opacity: 0.34 * arrive, borderRadius: 3,
            }}
          />
        );
      })}

      <div
        style={{
          position: 'absolute', left: RING_CX - RING_R - 26, top: RING_CY - RING_R - 26,
          width: (RING_R + 26) * 2, height: (RING_R + 26) * 2, borderRadius: '50%',
          backgroundColor: STAGE, border: `1px solid ${RULE}`, opacity: 1 - 0.45 * give,
        }}
      />
      {Array.from({length: NODES}).map((_, i) => {
        const a = (i / NODES) * Math.PI * 2 - Math.PI / 2;
        const g = win(p, 0.04 + i * 0.02, 0.16 + i * 0.02);
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: RING_CX + Math.cos(a) * RING_R - 14,
              top: RING_CY + Math.sin(a) * RING_R - 14,
              width: 28, height: 28, borderRadius: '50%',
              backgroundColor: CLAUDE.INK, opacity: (1 - 0.55 * give) * g,
            }}
          />
        );
      })}
      <div
        style={{
          position: 'absolute', left: RING_CX - 230, top: RING_CY - 36, width: 460,
          textAlign: 'center', fontFamily: CLAUDE_FONT.serif, fontSize: 42,
          color: CLAUDE.INK, opacity: (1 - 0.5 * give) * win(p, 0.08, 0.2),
        }}
      >
        {data.networkLabel}
      </div>
      <div
        style={{
          position: 'absolute', left: RING_CX - 230, top: RING_CY + 16, width: 460,
          textAlign: 'center', fontFamily: CLAUDE_FONT.ui, fontSize: 27,
          color: MUTE, opacity: (1 - 0.5 * give) * win(p, 0.1, 0.22),
        }}
      >
        {data.networkSub}
      </div>

      <div
        style={{
          position: 'absolute', left: BOX.x, top: FIELD_TOP + FIELD_H - 118,
          width: BOX.w * bandG, height: 108, backgroundColor: CLAUDE.SPARK, opacity: 0.97,
          display: 'flex', alignItems: 'center', overflow: 'hidden',
        }}
      >
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 44, color: '#FFFFFF', paddingLeft: 28, lineHeight: 1.15, opacity: win(p, 0.88, 0.96)}}>
          {data.verdictBand}
        </div>
      </div>

      <Note note={data.note} opacity={win(p, 0.92, 1.0)} />
    </Stage>
  );
};

/* ── B05 — the machine runs TOP → BOTTOM; the key still swaps out of the slot ── */
export const ItmQuestion916: React.FC<{data: QuestionData}> = ({data}) => {
  const p = useP();
  const draw = win(p, 0.06, 0.22);
  const seat = win(p, 0.22, 0.36);
  const lift = win(p, 0.50, 0.64);
  const drop = win(p, 0.64, 0.78);
  const rerun = win(p, 0.80, 0.96);

  const BOX_X = BOX.x;
  const BOX_W = 900;
  const BOX_Y = BOX.y + 620;
  const BOX_H = 300;
  const IN_Y = BOX.y + 200;
  const OUT_Y = BOX.y + 1080;

  const stack = (y: number, label: string, g: number, hot: boolean) => (
    <>
      {Array.from({length: 4}).map((_, i) => (
        <div
          key={i}
          style={{
            position: 'absolute', left: BOX.x + i * 232, top: y,
            width: 200, height: 44, borderRadius: 5,
            backgroundColor: hot ? CLAUDE.SPARK : CLAUDE.INK,
            opacity: (hot ? 0.5 : 0.26) * win(p, g + i * 0.02, g + 0.14 + i * 0.02),
          }}
        />
      ))}
      <div
        style={{
          position: 'absolute', left: BOX.x, top: y + 62, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE,
          opacity: win(p, g, g + 0.12),
        }}
      >
        {label}
      </div>
    </>
  );

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={draw} />
      {stack(IN_Y, data.inputLabel, 0.08, false)}
      {stack(OUT_Y, data.outputLabel, 0.82, true)}

      <div style={{position: 'absolute', left: BOX_X, top: BOX_Y, width: BOX_W, height: BOX_H, border: `2px solid ${CLAUDE.INK}`, borderRadius: 16, backgroundColor: '#FFFFFF', opacity: draw}} />
      <div style={{position: 'absolute', left: BOX_X + 48, top: BOX_Y + 100, width: BOX_W - 96, height: 100, border: `2px dashed ${RULE}`, borderRadius: 10, opacity: draw}} />

      {/* wires run vertically and re-run after the swap */}
      <div
        style={{
          position: 'absolute', left: BOX_X + BOX_W / 2 - 3, top: IN_Y + 110,
          width: 5, height: (BOX_Y - IN_Y - 110) * Math.max(seat, rerun),
          backgroundColor: rerun > 0.02 ? CLAUDE.SPARK : CLAUDE.INK,
          opacity: rerun > 0.02 ? 0.85 : 0.5,
        }}
      />
      <div
        style={{
          position: 'absolute', left: BOX_X + BOX_W / 2 - 3, top: BOX_Y + BOX_H,
          width: 5, height: (OUT_Y - BOX_Y - BOX_H) * rerun,
          backgroundColor: CLAUDE.SPARK, opacity: 0.85,
        }}
      />

      {/* OLD KEY — lifts out of the slot and greys */}
      <div
        style={{
          position: 'absolute', left: BOX_X + 68, top: BOX_Y + 114 - 230 * lift,
          width: BOX_W - 136, height: 72, borderRadius: 8,
          border: `2px solid ${CLAUDE.INK}`, backgroundColor: '#FFFFFF',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontFamily: CLAUDE_FONT.ui, fontSize: 36, color: CLAUDE.INK,
          opacity: seat * (1 - 0.72 * lift),
        }}
      >
        {data.oldKey}
      </div>

      {/* NEW KEY — the ONE accent */}
      <div
        style={{
          position: 'absolute', left: BOX_X + 68, top: BOX_Y + 114 - 160 * (1 - drop),
          width: BOX_W - 136, height: 72, borderRadius: 8,
          border: `2px solid ${CLAUDE.SPARK}`, backgroundColor: CLAUDE.SPARK,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontFamily: CLAUDE_FONT.ui, fontSize: 36, fontWeight: 600,
          color: '#FFFFFF', opacity: drop,
        }}
      >
        {data.newKey}
      </div>

      <Note note={data.note} opacity={win(p, 0.9, 0.99)} />
    </Stage>
  );
};

/* ── B07 — each track becomes a VERTICAL chain; the two sit side by side ── */
export const ItmModels916: React.FC<{data: ModelsData}> = ({data}) => {
  const p = useP();
  const COL_W = 430;
  const L_X = BOX.x;
  const R_X = BOX.x + 470;
  const CHAIN_TOP = BOX.y + 300;
  const STEP = 300;

  const t1 = win(p, 0.06, 0.20);
  const t2 = win(p, 0.48, 0.62);
  const run1 = win(p, 0.22, 0.40);
  const run2 = win(p, 0.66, 0.86);
  const matchHot = win(p, 0.84, 0.95);

  const node = (x: number, y: number, label: string, g: number, hot: boolean) => (
    <div
      style={{
        position: 'absolute', left: x, top: y, width: COL_W, minHeight: 150,
        boxSizing: 'border-box',
        border: `2px solid ${hot ? CLAUDE.SPARK : CLAUDE.INK}`,
        backgroundColor: hot ? CLAUDE.SPARK : '#FFFFFF', borderRadius: 10,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        padding: '14px 18px',
        fontFamily: CLAUDE_FONT.ui, fontSize: 30, lineHeight: 1.24, textAlign: 'center',
        color: hot ? '#FFFFFF' : CLAUDE.INK, opacity: g,
      }}
    >
      {label}
    </div>
  );

  const chain = (
    x: number, title: string, steps: string[], footText: string,
    base: number, gated: boolean, hotMid: boolean, accentFoot: boolean,
  ) => (
    <>
      <div
        style={{
          position: 'absolute', left: x, top: BOX.y + 210, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 25, letterSpacing: '.12em',
          color: MUTE, fontWeight: 600, lineHeight: 1.2,
          opacity: win(p, base, base + 0.14),
        }}
      >
        {title.toUpperCase()}
      </div>
      {/* the spine */}
      <div
        style={{
          position: 'absolute', left: x + COL_W / 2 - 2, top: CHAIN_TOP,
          width: 4, height: (STEP * 2 + 150) * win(p, base, base + 0.14),
          backgroundColor: RULE,
        }}
      />
      {node(x, CHAIN_TOP, steps[0], win(p, base, base + 0.14), false)}
      {node(x, CHAIN_TOP + STEP, steps[1], win(p, base + 0.06, base + 0.20), hotMid)}
      {node(x, CHAIN_TOP + STEP * 2, steps[2], win(p, base + 0.10, base + 0.24), false)}
      <div
        style={{
          position: 'absolute', left: x, top: CHAIN_TOP + STEP * 2 + 176, width: COL_W,
          fontFamily: CLAUDE_FONT.serif, fontSize: 32, lineHeight: 1.25,
          color: accentFoot ? CLAUDE.SPARK : MUTE,
          opacity: win(p, accentFoot ? 0.88 : 0.36, accentFoot ? 0.97 : 0.48),
        }}
      >
        {footText}
      </div>
      {gated ? (
        <>
          {/* the gate: a barrier laid ACROSS the chain */}
          {Array.from({length: 5}).map((_, i) => (
            <div
              key={i}
              style={{
                position: 'absolute', left: x + 30, top: CHAIN_TOP + 190 + i * 16,
                width: COL_W - 60, height: 5, backgroundColor: CLAUDE.INK,
                opacity: 0.75 * win(p, 0.20, 0.34),
              }}
            />
          ))}
          <div
            style={{
              position: 'absolute', left: x + 30, top: CHAIN_TOP + 268,
              fontFamily: CLAUDE_FONT.ui, fontSize: 23, letterSpacing: '.16em',
              color: CLAUDE.INK, fontWeight: 600, opacity: win(p, 0.24, 0.38),
            }}
          >
            {data.oldGateLabel.toUpperCase()}
          </div>
        </>
      ) : null}
    </>
  );

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={t1} />
      {chain(L_X, data.oldTitle, data.oldSteps, data.oldFoot, 0.06, true, false, false)}
      {chain(R_X, data.newTitle, data.newSteps, data.newFoot, 0.48, false, matchHot > 0.5, true)}

      {/* the post stops at the barrier on the left chain */}
      <div
        style={{
          position: 'absolute', left: L_X + COL_W / 2 - 13,
          top: CHAIN_TOP + 156 + 20 * run1,
          width: 26, height: 26, borderRadius: '50%',
          backgroundColor: CLAUDE.INK, opacity: win(p, 0.20, 0.30),
        }}
      />
      {/* and crosses straight through on the right */}
      <div
        style={{
          position: 'absolute', left: R_X + COL_W / 2 - 13,
          top: CHAIN_TOP + 156 + (STEP * 2 - 156) * run2,
          width: 26, height: 26, borderRadius: '50%',
          backgroundColor: CLAUDE.SPARK, opacity: win(p, 0.64, 0.74),
        }}
      />

      <Note note={data.note} opacity={win(p, 0.93, 1.0)} />
    </Stage>
  );
};

/* ── B08 — the two job cards STACK; the tick row sits beneath the new one ── */
export const ItmJob916: React.FC<{data: JobData}> = ({data}) => {
  const p = useP();
  const OLD_Y = BOX.y + 190;
  const NEW_Y = BOX.y + 560;
  const CARD_H = 280;

  const oldIn = win(p, 0.08, 0.24);
  const retire = win(p, 0.34, 0.50);
  const newIn = win(p, 0.52, 0.70);

  return (
    <Stage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      <div style={{position: 'absolute', left: BOX.x, top: OLD_Y - 54, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600, opacity: oldIn}}>
        {data.oldHead.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: OLD_Y + 14 * retire, width: BOX.w,
          minHeight: CARD_H, boxSizing: 'border-box',
          backgroundColor: '#FFFFFF', border: `1px solid ${RULE}`, borderRadius: 14,
          padding: 38, opacity: oldIn * (1 - 0.42 * retire),
          fontFamily: CLAUDE_FONT.serif, fontSize: 60, color: CLAUDE.INK, lineHeight: 1.18,
        }}
      >
        {data.oldQuestion}
      </div>

      <div style={{position: 'absolute', left: BOX.x, top: NEW_Y - 54, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: CLAUDE.SPARK, fontWeight: 600, opacity: newIn}}>
        {data.newHead.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: NEW_Y - 18 * (1 - newIn), width: BOX.w,
          minHeight: CARD_H + 90, boxSizing: 'border-box',
          backgroundColor: '#FFFFFF', border: `2px solid ${CLAUDE.SPARK}`, borderRadius: 14,
          padding: 38, opacity: newIn,
          fontFamily: CLAUDE_FONT.serif, fontSize: 60, color: CLAUDE.SPARK, lineHeight: 1.18,
        }}
      >
        {data.newQuestion}
      </div>

      {/* marks, never a tally — same TICKS as the landscape cut */}
      {Array.from({length: TICKS}).map((_, i) => {
        const g = win(p, 0.74 + i * 0.018, 0.80 + i * 0.018);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: BOX.x + i * 100, top: NEW_Y + CARD_H + 150,
              width: 62, height: 62, borderRadius: 8,
              border: `2px solid ${CLAUDE.SPARK}`, backgroundColor: CLAUDE.SPARK,
              opacity: 0.85 * g, transform: `scale(${0.6 + 0.4 * g})`,
            }}
          />
        );
      })}
      <div
        style={{
          position: 'absolute', left: BOX.x, top: NEW_Y + CARD_H + 232, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: MUTE, opacity: win(p, 0.86, 0.95),
        }}
      >
        {data.tickLabel}
      </div>

      <Note note={data.note} opacity={win(p, 0.92, 1.0)} />
    </Stage>
  );
};

/* ── B09 — the two ledgers STACK into two labelled groups ── */
export const ItmLimits916: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const G1_Y = BOX.y + 270;
  const G2_Y = BOX.y + 730;
  const STEP = 118;

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
      <div
        style={{
          position: 'absolute', left: BOX.x, top: y + 42,
          width: BOX.w * win(p, startAt, startAt + 0.12), height: 2,
          backgroundColor: hot ? CLAUDE.SPARK : RULE,
        }}
      />
      {items.map((it, i) => {
        const g = win(p, startAt + 0.05 + i * 0.07, startAt + 0.2 + i * 0.07);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: BOX.x, top: y + 74 + i * STEP, width: BOX.w,
              fontFamily: CLAUDE_FONT.ui, fontSize: 34, lineHeight: 1.3,
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
      {ledger(G2_Y, data.refusals.heading, data.refusals.items, 0.42, true)}

      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 210, width: BOX.w * win(p, 0.78, 0.88), height: 1, backgroundColor: RULE}} />
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 190, width: BOX.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: MUTE, lineHeight: 1.32,
          opacity: win(p, 0.80, 0.90),
        }}
      >
        {data.provenance}
      </div>

      <Note note={data.falsifier} opacity={win(p, 0.90, 0.99)} />
    </Stage>
  );
};
