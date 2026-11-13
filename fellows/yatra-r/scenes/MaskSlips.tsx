/**
 * MaskSlips.tsx — reel-local scenes for `yatra-the-mask-slips`
 * ("The Mask Slips." — AI influencer accounts that earn fast and collapse faster).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * The human asked for a video that is not a variation of any previous one. Nothing
 * from the `Itm*`, `Wk*`, `Lnk*`, `Rcp*`, `Seo*`, `Ytw*` or `Jdg*` families is reused
 * or re-exported here. The shapes are driven by this reel's own argument: a curve whose
 * fall begins at a *named moment* rather than a trend, a wire that turns out to have
 * been dashed all along, and a bar that halves itself on the spoken word.
 *
 * ── THE SOURCING CONSTRAINT, ENFORCED BY THE TYPES ───────────────────────────
 * Every figure in this reel comes from ONE report (Garbage Day, October 2026), and the
 * human's instruction was to cite on screen and invent nothing further. So:
 *
 *   Every scene that renders a figure REQUIRES a `source` string.
 *
 * `MskSpike`, `MskMoney` and `MskDrop` cannot be used without one — a number cannot
 * reach the screen uncited, because the type will not allow it. `SourceLine` always
 * renders in MUTE and never in the accent: a citation is provenance, not emphasis.
 *
 * ── THREE REFUSALS WORTH NAMING ──────────────────────────────────────────────
 *
 * 1. **Values are strings, rendered verbatim.** `value: string` everywhere, never a
 *    number formatted at render time. "$13,700" stays "$13,700"; "2.2 million" is never
 *    converted to 2_200_000; "roughly 50%" keeps its hedge; and `MskDrop`'s second case
 *    carries the value "the same drop", which is not a number at all and must not be
 *    coerced into one. Any bar length comes from a SEPARATE numeric prop, so no code
 *    path ever parses a displayed string.
 *
 * 2. **`MskMoney` requires a `stamp`.** The $13,700 is *reported*, not audited, and the
 *    hedge renders hard against the figure rather than in a footnote — a reader who sees
 *    the number sees the qualifier in the same glance.
 *
 * 3. **Neither account is named, and cannot be.** The human described them
 *    ("one of the earliest popular AI influencer accounts", "another AI persona") and
 *    named neither. `MskDrop`'s cases carry a `label` that holds that description, and
 *    there is no `name`, `handle` or `account` prop anywhere in this file.
 *
 * `MskArc` is numeral-free by construction for the same reason: its axes carry no
 * ticks and no scale, it has no numeric prop at all, and it REQUIRES an `axisNote`
 * saying so on screen — the curve argues shape, and shape is all it is allowed to argue.
 *
 * ── ACCENT SEMANTICS ─────────────────────────────────────────────────────────
 * Terracotta is the ONE accent per beat and it always marks THE COLLAPSE SIDE: the
 * identification marker, the dashed wire, the halved remainder, the turn. The gold-rush
 * half of the story is deliberately rendered in plain ink — the accent belongs to what
 * the reel is warning about, so the money never glows.
 */
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {PlainStage, Head, RULE, MUTE, win} from './claudeStage';

/** progress through the beat, 0..1 */
const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

const NoteLine: React.FC<{note: string; opacity: number; accent?: boolean}> = ({note, opacity, accent}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: SAFE.b - 62, width: SAFE.w,
      fontFamily: CLAUDE_FONT.serif, fontSize: 40,
      color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity, lineHeight: 1.2,
    }}
  >
    {note}
  </div>
);

/** Provenance. Always MUTE, never the accent — a citation is not emphasis. */
const SourceLine: React.FC<{source: string; opacity: number; top?: number}> = ({source, opacity, top}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: top ?? SAFE.b - 128, width: SAFE.w,
      fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, opacity, letterSpacing: '.01em',
    }}
  >
    Source: {source}
  </div>
);

const Eyebrow: React.FC<{text: string; opacity?: number}> = ({text, opacity = 1}) => (
  <div
    style={{
      position: 'absolute', left: SAFE.x, top: SAFE.y + 6, width: SAFE.w,
      fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.18em',
      color: MUTE, fontWeight: 600, opacity,
    }}
  >
    {text.toUpperCase()}
  </div>
);

const Chip: React.FC<{
  text: string; left: number; top: number; hot?: boolean; opacity: number; size?: number;
}> = ({text, left, top, hot, opacity, size = 22}) => (
  <div
    style={{
      position: 'absolute', left, top, opacity,
      fontFamily: CLAUDE_FONT.ui, fontSize: size, fontWeight: 600,
      letterSpacing: '.16em', textTransform: 'uppercase' as const,
      color: hot ? CLAUDE.SPARK : MUTE,
      border: `1px solid ${hot ? CLAUDE.SPARK : RULE}`,
      padding: '9px 16px', display: 'inline-block', whiteSpace: 'nowrap' as const,
    }}
  >
    {text}
  </div>
);

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — MskBluf: the whole arc as two phases, pivoting at the middle.

   EXECUTIVE-SUMMARY LAW: the gist before any specific. The two phases sit side by
   side with a divider that DRAWS on the spoken "then", so the beat enacts the pivot
   rather than presenting two static columns. The second phase takes the accent,
   because the collapse is what the reel is about.
   ═══════════════════════════════════════════════════════════════════════════ */
export type BlufData = {
  slideMeta: string;
  firstHead: string;
  firstLines: string[];
  secondHead: string;
  secondLines: string[];
  closer: string;
};

export const MskBluf: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const COL_W = 780;
  const L_X = SAFE.x;
  const R_X = SAFE.x + 948;
  const HEAD_Y = SAFE.y + 170;
  const LINE_Y = SAFE.y + 290;
  const divide = win(p, 0.36, 0.56);

  const phase = (x: number, head: string, lines: string[], at: number, hot: boolean) => (
    <>
      <Chip text={head} left={x} top={HEAD_Y} hot={hot} opacity={win(p, at, at + 0.1)} size={26} />
      {lines.map((ln, i) => {
        const g = win(p, at + 0.08 + i * 0.1, at + 0.26 + i * 0.1);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: x, top: LINE_Y + i * 180, width: COL_W,
              fontFamily: CLAUDE_FONT.serif, fontSize: 68, lineHeight: 1.18,
              color: hot ? CLAUDE.SPARK : CLAUDE.INK,
              opacity: g, transform: `translateY(${(1 - g) * 18}px)`,
            }}
          >
            {ln}
          </div>
        );
      })}
    </>
  );

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.16)} />
      {phase(L_X, data.firstHead, data.firstLines, 0.08, false)}
      {/* the divider draws down the middle ON the pivot */}
      <div
        style={{
          position: 'absolute', left: SAFE.x + 888, top: HEAD_Y,
          width: 2, height: 520 * divide, backgroundColor: RULE,
        }}
      />
      {phase(R_X, data.secondHead, data.secondLines, 0.52, true)}
      <NoteLine note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — MskSpike: how little time this took.

   REQUIRES a `source`. All three figures are strings printed verbatim — "2.2 million"
   is never converted, and nothing here computes a rate, a per-day figure or any other
   number the report did not publish. The only drawn element is a baseline with a single
   accent tick, and the tick's position is a fixed design constant, not data.
   ═══════════════════════════════════════════════════════════════════════════ */
export type SpikeData = {
  slideMeta: string;
  title: string;
  lead: {value: string; label: string};
  figures: {value: string; label: string}[];
  /** REQUIRED — a figure cannot reach the screen uncited */
  source: string;
  note: string;
};

export const MskSpike: React.FC<{data: SpikeData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 250;
  const lead = win(p, 0.06, 0.26);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* the lead figure owns the left third and lands first */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP, width: 620,
          fontFamily: CLAUDE_FONT.serif, fontSize: 170, lineHeight: 1,
          color: CLAUDE.INK, opacity: lead, transform: `translateY(${(1 - lead) * 20}px)`,
        }}
      >
        {data.lead.value}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 190, width: 600,
          fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: MUTE, lineHeight: 1.3,
          opacity: win(p, 0.18, 0.34),
        }}
      >
        {data.lead.label}
      </div>

      {/* the two scale figures stack on the right */}
      {data.figures.map((f, i) => {
        const g = win(p, 0.34 + i * 0.22, 0.54 + i * 0.22);
        const y = TOP + i * 200;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: SAFE.x + 760, top: y, width: 960,
                fontFamily: CLAUDE_FONT.serif, fontSize: 104, lineHeight: 1,
                color: CLAUDE.INK, opacity: g, transform: `translateY(${(1 - g) * 16}px)`,
              }}
            >
              {f.value}
            </div>
            <div
              style={{
                position: 'absolute', left: SAFE.x + 760, top: y + 116, width: 960,
                fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE,
                opacity: win(p, 0.4 + i * 0.22, 0.6 + i * 0.22),
              }}
            >
              {f.label}
            </div>
          </React.Fragment>
        );
      })}

      {/* the baseline, with ONE accent tick marking how early the spike landed */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 190,
          width: SAFE.w * win(p, 0.76, 0.9), height: 2, backgroundColor: RULE,
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x + 70, top: SAFE.b - 214,
          width: 6, height: 50 * win(p, 0.86, 0.96), backgroundColor: CLAUDE.SPARK,
        }}
      />

      <SourceLine source={data.source} opacity={win(p, 0.78, 0.9)} />
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B03 — MskMoney: one figure, one qualifier, one hedge.

   REQUIRES both a `source` AND a `stamp`. The figure is reported rather than audited,
   and the stamp renders hard against the number so the two are read together. The
   accent underlines the NOTE, not the figure: this beat is the gold-rush half of the
   story, and the reel does not let the money glow.
   ═══════════════════════════════════════════════════════════════════════════ */
export type MoneyData = {
  slideMeta: string;
  /** rendered VERBATIM — never parsed, never reformatted */
  value: string;
  qualifier: string;
  /** REQUIRED — the hedge travels with the figure */
  stamp: string;
  /** REQUIRED */
  source: string;
  note: string;
};

export const MskMoney: React.FC<{data: MoneyData}> = ({data}) => {
  const p = useP();
  const set = win(p, 0.08, 0.3);
  const TOP = SAFE.y + 230;

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.16)} />

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 280, lineHeight: 1,
          color: CLAUDE.INK, opacity: set, transform: `translateY(${(1 - set) * 24}px)`,
        }}
      >
        {data.value}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + 310, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 64, color: CLAUDE.INK,
          opacity: win(p, 0.3, 0.48),
        }}
      >
        {data.qualifier}
      </div>
      {/* the hedge sits against the figure, not in a footnote */}
      <Chip text={data.stamp} left={SAFE.x} top={TOP + 404} opacity={win(p, 0.48, 0.64)} size={26} />

      {/* QC: lifted clear of the accent rule below. At the default SAFE.b-128 the
         terracotta rule sat directly under this line and read as underlining the
         CITATION — sources stay muted ink and never take the accent. */}
      <SourceLine source={data.source} opacity={win(p, 0.7, 0.84)} top={SAFE.b - 196} />
      {/* the accent underlines the caveat, never the money and never the source */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 78,
          width: SAFE.w * 0.44 * win(p, 0.84, 0.95), height: 5, backgroundColor: CLAUDE.SPARK,
        }}
      />
      <NoteLine note={data.note} opacity={win(p, 0.86, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — MskArc: the shape of the whole thing.

   The ask→result pair's RESULT. Deliberately NUMERAL-FREE: there is no numeric prop on
   this type, the axes carry no ticks or scale, and an `axisNote` is REQUIRED and
   rendered on screen saying the curve carries no figures. The one accent is the
   identification marker, placed at the crest — the fall is shown as a consequence of a
   moment, which is the beat's actual claim.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ArcData = {
  slideMeta: string;
  title: string;
  riseLabel: string;
  markerLabel: string;
  fallLabel: string;
  /** REQUIRED — the curve must say on screen that it carries no figures */
  axisNote: string;
  note: string;
};

export const MskArc: React.FC<{data: ArcData}> = ({data}) => {
  const p = useP();
  const rise = win(p, 0.06, 0.38);
  const mark = win(p, 0.52, 0.66);
  const fall = win(p, 0.66, 0.9);

  /* plot box, in canvas coordinates */
  const X0 = SAFE.x + 60;
  const Y0 = SAFE.b - 250;      // baseline
  const PEAK_X = SAFE.x + 760;
  const PEAK_Y = SAFE.y + 250;
  const END_X = SAFE.r - 120;
  const END_Y = Y0 - 110;

  const risePath = `M ${X0} ${Y0} C ${X0 + 230} ${Y0} ${PEAK_X - 150} ${PEAK_Y + 40} ${PEAK_X} ${PEAK_Y}`;
  const fallPath = `M ${PEAK_X} ${PEAK_Y} C ${PEAK_X + 190} ${PEAK_Y + 60} ${END_X - 240} ${END_Y - 40} ${END_X} ${END_Y}`;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      <svg
        width={1920} height={1080}
        style={{position: 'absolute', left: 0, top: 0}}
        viewBox="0 0 1920 1080"
      >
        {/* an axis with NO ticks and NO scale — there is nothing here to read a value off */}
        <line x1={X0} y1={Y0} x2={END_X} y2={Y0} stroke={RULE} strokeWidth={2} />
        <path
          d={risePath} fill="none" stroke={CLAUDE.INK} strokeWidth={7}
          strokeLinecap="round"
          pathLength={1} strokeDasharray={1} strokeDashoffset={1 - rise}
        />
        <path
          d={fallPath} fill="none" stroke={CLAUDE.INK} strokeWidth={7}
          strokeLinecap="round" opacity={0.55}
          pathLength={1} strokeDasharray={1} strokeDashoffset={1 - fall}
        />
        {/* the ONE accent: the cause, dropped at the crest */}
        <line
          x1={PEAK_X} y1={PEAK_Y - 60} x2={PEAK_X} y2={PEAK_Y + 150 * mark}
          stroke={CLAUDE.SPARK} strokeWidth={5} opacity={mark}
        />
        <circle cx={PEAK_X} cy={PEAK_Y} r={16 * mark} fill={CLAUDE.SPARK} />
      </svg>

      <div
        style={{
          /* QC: moved BELOW the baseline — at Y0-86 the rising curve passed
             straight through this label (collision). */
          position: 'absolute', left: X0 + 20, top: Y0 + 22, width: 520,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE,
          opacity: win(p, 0.2, 0.36),
        }}
      >
        {data.riseLabel}
      </div>
      <div
        style={{
          position: 'absolute', left: PEAK_X + 34, top: PEAK_Y - 96, width: 620,
          fontFamily: CLAUDE_FONT.ui, fontSize: 40, fontWeight: 600, color: CLAUDE.SPARK,
          opacity: mark, lineHeight: 1.2,
        }}
      >
        {data.markerLabel}
      </div>
      <div
        style={{
          position: 'absolute', left: END_X - 540, top: END_Y + 42, width: 540,
          textAlign: 'right', fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE,
          opacity: win(p, 0.82, 0.94),
        }}
      >
        {data.fallLabel}
      </div>

      {/* the disclosure is not optional — see the type */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 128, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE,
          opacity: win(p, 0.86, 0.96),
        }}
      >
        {data.axisNote}
      </div>
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — MskReveal: what actually breaks.

   The mechanism performs the sentence. The wire does NOT snap — it turns dashed along
   its whole length, retroactively, because the beat's claim is that the relationship was
   never there rather than that it was damaged. A snap would illustrate the wrong idea.
   ═══════════════════════════════════════════════════════════════════════════ */
export type RevealData = {
  slideMeta: string;
  title: string;
  leftLabel: string;
  rightBefore: string;
  rightAfter: string;
  wireLabel: string;
  verdict: string;
  note: string;
};

export const MskReveal: React.FC<{data: RevealData}> = ({data}) => {
  const p = useP();
  const draw = win(p, 0.06, 0.26);
  const strike = win(p, 0.5, 0.64);
  const after = win(p, 0.58, 0.72);
  const dash = win(p, 0.68, 0.84);

  const MID_Y = SAFE.y + 440;
  const L_X = SAFE.x + 40;
  const R_X = SAFE.r - 560;
  const NODE_W = 520;

  const node = (x: number, label: string, g: number, struck: boolean, hot: boolean) => (
    <div
      style={{
        position: 'absolute', left: x, top: MID_Y - 80, width: NODE_W, minHeight: 160,
        boxSizing: 'border-box', border: `2px solid ${hot ? CLAUDE.SPARK : CLAUDE.INK}`,
        borderRadius: 14, backgroundColor: '#FFFFFF',
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        padding: '18px 24px', textAlign: 'center',
        fontFamily: CLAUDE_FONT.serif, fontSize: 56, lineHeight: 1.15,
        color: hot ? CLAUDE.SPARK : CLAUDE.INK, opacity: g,
      }}
    >
      {/* the strike is drawn on an inline wrapper so it spans the TEXT, not the card */}
      <span style={{position: 'relative', display: 'inline-block'}}>
        {label}
        {struck ? (
          <span
            style={{
              position: 'absolute', left: 0, top: '52%',
              width: `${100 * strike}%`, height: 5, backgroundColor: CLAUDE.INK,
            }}
          />
        ) : null}
      </span>
    </div>
  );

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* the wire — solid, then dashed along its whole length */}
      <div
        style={{
          position: 'absolute', left: L_X + NODE_W, top: MID_Y - 3,
          width: (R_X - L_X - NODE_W) * draw, height: 6,
          backgroundColor: dash > 0.02 ? 'transparent' : CLAUDE.INK,
          backgroundImage: dash > 0.02
            ? `repeating-linear-gradient(90deg, ${CLAUDE.SPARK} 0 22px, transparent 22px 44px)`
            : 'none',
          opacity: 1,
        }}
      />
      <div
        style={{
          position: 'absolute', left: L_X + NODE_W, top: MID_Y - 62,
          width: R_X - L_X - NODE_W, textAlign: 'center',
          fontFamily: CLAUDE_FONT.ui, fontSize: 30,
          color: dash > 0.5 ? CLAUDE.SPARK : MUTE, opacity: win(p, 0.26, 0.4),
        }}
      >
        {data.wireLabel}
      </div>

      {node(L_X, data.leftLabel, draw, false, false)}

      {/* the far node: what the audience believed, struck, then replaced */}
      {after < 0.5 ? node(R_X, data.rightBefore, draw, strike > 0.02, false)
                   : node(R_X, data.rightAfter, after, false, true)}

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 160, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 60, color: CLAUDE.SPARK,
          opacity: win(p, 0.84, 0.94),
        }}
      >
        {data.verdict}
      </div>
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — MskDrop: the bars halve themselves.

   REQUIRES a `source`. Each case's `value` is a STRING printed verbatim — one is
   "roughly 50%" (the hedge survives) and the other is "the same drop" (not a number at
   all). The bar's motion is a fixed halving, driven by progress rather than by any
   numeric prop, so nothing here computes or implies a figure the report did not give.
   `label` holds the human's DESCRIPTION of each account; there is no `name` prop,
   because neither account was named to us.
   ═══════════════════════════════════════════════════════════════════════════ */
export type DropData = {
  slideMeta: string;
  title: string;
  cases: {label: string; value: string; detail: string}[];
  beforeLabel: string;
  afterLabel: string;
  /** REQUIRED */
  source: string;
  note: string;
};

export const MskDrop: React.FC<{data: DropData}> = ({data}) => {
  const p = useP();
  const TRACK_W = 980;
  const X = SAFE.x;
  const TOP = SAFE.y + 230;
  const ROW = 230;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {data.cases.map((c, i) => {
        const at = 0.1 + i * 0.3;
        const grow = win(p, at, at + 0.12);
        const halve = win(p, at + 0.16, at + 0.3);
        const y = TOP + i * ROW;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: X, top: y, width: TRACK_W + 640,
                fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.INK,
                opacity: grow, lineHeight: 1.25,
              }}
            >
              {c.label}
            </div>
            {/* the ghost of the original height stays visible behind the halved bar */}
            <div
              style={{
                position: 'absolute', left: X, top: y + 54,
                width: TRACK_W * grow, height: 64,
                border: `2px dashed ${RULE}`, boxSizing: 'border-box',
              }}
            />
            <div
              style={{
                position: 'absolute', left: X, top: y + 54,
                width: TRACK_W * grow * (1 - 0.5 * halve), height: 64,
                backgroundColor: halve > 0.5 ? CLAUDE.SPARK : CLAUDE.INK,
                opacity: halve > 0.5 ? 0.9 : 0.82,
              }}
            />
            <div
              style={{
                position: 'absolute', left: X + TRACK_W + 40, top: y + 50,
                width: 600, fontFamily: CLAUDE_FONT.serif, fontSize: 62,
                color: CLAUDE.SPARK, opacity: win(p, at + 0.22, at + 0.34), lineHeight: 1.1,
              }}
            >
              {c.value}
            </div>
            <div
              style={{
                position: 'absolute', left: X + TRACK_W + 40, top: y + 124,
                width: 620, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE,
                opacity: win(p, at + 0.26, at + 0.38), lineHeight: 1.25,
              }}
            >
              {c.detail}
            </div>
          </React.Fragment>
        );
      })}

      <div
        style={{
          position: 'absolute', left: X, top: TOP + data.cases.length * ROW - 10,
          width: TRACK_W, display: 'flex', justifyContent: 'space-between',
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE,
          opacity: win(p, 0.72, 0.84),
        }}
      >
        <span>{data.beforeLabel}</span>
        <span>{data.afterLabel}</span>
      </div>

      <SourceLine source={data.source} opacity={win(p, 0.84, 0.94)} />
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B08 — MskTurn: ruling out the comfortable explanations.

   Each candidate explanation sets and is struck through in narration order, so the
   beat argues by elimination on screen rather than asserting a conclusion. The survivor
   lands alone and large in the accent. Numeral-free by construction.
   ═══════════════════════════════════════════════════════════════════════════ */
export type TurnData = {
  slideMeta: string;
  ruledOut: string[];
  survivor: string;
  closer: string;
  note: string;
};

export const MskTurn: React.FC<{data: TurnData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 150;
  const STEP = 130;

  return (
    <PlainStage>
      <Eyebrow text={data.slideMeta} opacity={win(p, 0.02, 0.14)} />

      {data.ruledOut.map((r, i) => {
        const at = 0.08 + i * 0.2;
        const set = win(p, at, at + 0.08);
        const rule = win(p, at + 0.1, at + 0.2);
        return (
          <div key={i} style={{position: 'absolute', left: SAFE.x, top: TOP + i * STEP}}>
            <div style={{position: 'relative', display: 'inline-block'}}>
              <span
                style={{
                  fontFamily: CLAUDE_FONT.serif, fontSize: 64,
                  color: CLAUDE.INK, opacity: set * (1 - 0.5 * rule),
                }}
              >
                {r}
              </span>
              <span
                style={{
                  position: 'absolute', left: 0, top: 44,
                  width: `${100 * rule}%`, height: 4, backgroundColor: CLAUDE.INK, opacity: 0.6,
                }}
              />
            </div>
          </div>
        );
      })}

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + data.ruledOut.length * STEP + 50,
          width: SAFE.w, fontFamily: CLAUDE_FONT.serif, fontSize: 150, lineHeight: 1.05,
          color: CLAUDE.SPARK, opacity: win(p, 0.68, 0.82),
          transform: `translateY(${(1 - win(p, 0.68, 0.82)) * 22}px)`,
        }}
      >
        {data.survivor}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 136, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 38, color: CLAUDE.INK,
          opacity: win(p, 0.84, 0.94), lineHeight: 1.25,
        }}
      >
        {data.closer}
      </div>
      <NoteLine note={data.note} opacity={win(p, 0.92, 1.0)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B09 — MskLimits: being exact about the claim.

   The FALSIFIABILITY beat. `provenance` and `falsifier` are both REQUIRED, so the beat
   cannot be authored without naming the source behind every figure and giving the viewer
   a way to check the claim. The accent sits on the REFUSALS column — in this reel the
   honest part is what is being declined.
   ═══════════════════════════════════════════════════════════════════════════ */
export type LimitsData = {
  slideMeta: string;
  title: string;
  claims: {heading: string; items: string[]};
  refusals: {heading: string; items: string[]};
  /** REQUIRED */
  provenance: string;
  /** REQUIRED */
  falsifier: string;
};

export const MskLimits: React.FC<{data: LimitsData}> = ({data}) => {
  const p = useP();
  const COL_W = 806;
  const L_X = SAFE.x;
  const R_X = SAFE.x + 922;
  const HEAD_Y = SAFE.y + 236;
  const ITEM_Y = SAFE.y + 310;
  const STEP = 140;

  const ledger = (x: number, heading: string, items: string[], startAt: number, hot: boolean) => (
    <>
      <div
        style={{
          position: 'absolute', left: x, top: HEAD_Y, width: COL_W,
          fontFamily: CLAUDE_FONT.ui, fontSize: 27, letterSpacing: '.16em', fontWeight: 600,
          color: hot ? CLAUDE.SPARK : MUTE, opacity: win(p, startAt, startAt + 0.08),
        }}
      >
        {heading.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: x, top: HEAD_Y + 44,
          width: COL_W * win(p, startAt, startAt + 0.12), height: 2,
          backgroundColor: hot ? CLAUDE.SPARK : RULE,
        }}
      />
      {items.map((it, i) => {
        const g = win(p, startAt + 0.05 + i * 0.07, startAt + 0.2 + i * 0.07);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: x, top: ITEM_Y + i * STEP, width: COL_W,
              fontFamily: CLAUDE_FONT.ui, fontSize: 35, lineHeight: 1.32,
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
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {ledger(L_X, data.claims.heading, data.claims.items, 0.08, false)}
      {ledger(R_X, data.refusals.heading, data.refusals.items, 0.44, true)}

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 170,
          width: SAFE.w * win(p, 0.78, 0.88), height: 1, backgroundColor: RULE,
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 150, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 27, color: MUTE, lineHeight: 1.3,
          opacity: win(p, 0.8, 0.9),
        }}
      >
        {data.provenance}
      </div>
      <NoteLine note={data.falsifier} opacity={win(p, 0.9, 0.99)} />
    </PlainStage>
  );
};
