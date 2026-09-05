/**
 * WeekGordy.tsx — reel-local scenes for `yatra-this-week-gordy`
 * ("This Week, Gordy." — the weekly Humanitarians AI tool recap).
 *
 * ── WHY THESE ARE NEW COMPONENTS ─────────────────────────────────────────────
 * This is the next episode of the same weekly series as
 * `yatra-one-tool-a-week-brandy` (the `Rcp*` family). Nothing from that family
 * is reused, and neither is the `Lnk*` family: the human asked for an episode
 * that is not a variation of a previous video, and re-skinning last week's
 * components is exactly what that would have been. The shapes here are driven
 * by what makes THIS week different — the week ends mid-pipeline, with work
 * still sitting in review — so the five-stage method and its one unclosed stage
 * are the reel's subject rather than a footnote.
 *
 * ── THE CONSTRAINT THAT SHAPES `WkReview` ────────────────────────────────────
 * The two articles are written but NOT approved and NOT published. The human's
 * instruction was explicit: do not say they are published, and do not invent
 * anything about their content.
 *
 *   `WkReview`'s `slots` are typed `{label: string}[]`.
 *
 * There is no `title`, `summary`, `excerpt`, `blurb` or `content` prop on it,
 * and no code path by which an article's contents could reach the screen. The
 * slots render as dashed, empty cards under a "withheld" band. Refusing the
 * prop is the only way to refuse the claim — a component that *can* render a
 * title will eventually be given one.
 *
 * Two related refusals, same reasoning:
 *   · `WkShip` names the deliverable and its destination but draws NO artwork.
 *     Inventing graphics and presenting them as the week's output would be a
 *     fabricated artifact. Its chip reads `MADE`, never `LIVE` or `POSTED` —
 *     the human said the graphics were *created for* the page, and that is all
 *     that is claimed.
 *   · `WkTool` renders the tool page's description as a VERBATIM quote and
 *     carries a `note` stating that one line is all the page publishes. The
 *     page says "two-mode" but never names the modes, so no mode names exist
 *     anywhere in this file.
 *
 * ── ACCENT SEMANTICS ─────────────────────────────────────────────────────────
 * Terracotta is the ONE accent per beat and it always marks THE UNCLOSED STAGE:
 * the "not yet" chip, the open Publish box, the in-review node, the
 * "what I'm not claiming" column. The accent carries the reel's thesis — an
 * honest week, not a finished one — instead of decorating the frame. Sources
 * and provenance stay muted ink.
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
      fontFamily: CLAUDE_FONT.serif, fontSize: 42,
      color: accent ? CLAUDE.SPARK : CLAUDE.INK, opacity,
    }}
  >
    {note}
  </div>
);

/** A small bordered status chip. `hot` is the reel's one accent per beat. */
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
   B01 — WkBluf: the week in one breath, as three stated facts with states.

   EXECUTIVE-SUMMARY LAW: the whole idea before any detail. The third line is
   the point of the episode, so it is the one that lands in the accent — the
   summary states up front that the week is unfinished rather than saving it.
   ═══════════════════════════════════════════════════════════════════════════ */
export type BlufData = {
  slideMeta: string;
  lines: {label: string; chip: string}[];
  closer: string;
};

export const WkBluf: React.FC<{data: BlufData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 170;
  const STEP = 200;

  return (
    <PlainStage>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 6,
          fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.18em',
          color: MUTE, fontWeight: 600, opacity: win(p, 0.02, 0.16),
        }}
      >
        {data.slideMeta.toUpperCase()}
      </div>

      {data.lines.map((ln, i) => {
        const g = win(p, 0.08 + i * 0.26, 0.3 + i * 0.26);
        const hot = i === data.lines.length - 1;   // the unfinished one
        const y = TOP + i * STEP;
        return (
          <React.Fragment key={i}>
            <Chip text={ln.chip} left={SAFE.x} top={y + 16} hot={hot} opacity={g} />
            <div
              style={{
                position: 'absolute', left: SAFE.x + 230, top: y, width: SAFE.w - 230,
                fontFamily: CLAUDE_FONT.serif, fontSize: 66, lineHeight: 1.16,
                color: hot ? CLAUDE.SPARK : CLAUDE.INK, opacity: g,
                transform: `translateY(${(1 - g) * 16}px)`,
              }}
            >
              {ln.label}
            </div>
            <div
              style={{
                position: 'absolute', left: SAFE.x, top: y + STEP - 42,
                width: SAFE.w * g, height: 1, backgroundColor: RULE,
              }}
            />
          </React.Fragment>
        );
      })}

      <NoteLine note={data.closer} opacity={win(p, 0.86, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B02 — WkPipeline: the method, five stages, ALL UNLIT.

   This is the FRAMEWORK beat and it runs before the worked example, so no
   stage carries a state here: showing what closed would spend B05's reveal.
   There is deliberately no `state` field on a stage in this type.
   ═══════════════════════════════════════════════════════════════════════════ */
export type PipelineData = {
  slideMeta: string;
  title: string;
  stages: {label: string; sub: string}[];
  hotIndex: number;      // the stage the narration points at last
  note: string;
};

export const WkPipeline: React.FC<{data: PipelineData}> = ({data}) => {
  const p = useP();
  const n = data.stages.length;
  const GAP = 68;
  const BOX_W = (SAFE.w - GAP * (n - 1)) / n;
  const BOX_H = 400;
  const TOP = SAFE.y + 290;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.stages.map((s, i) => {
        const g = win(p, 0.1 + i * 0.14, 0.26 + i * 0.14);
        const hot = i === data.hotIndex ? win(p, 0.82, 0.94) : 0;
        const x = SAFE.x + i * (BOX_W + GAP);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: x, top: TOP, width: BOX_W, height: BOX_H * g, border: `2px solid ${RULE}`, boxSizing: 'border-box'}} />
            {/* the accent: the last stage the narration names reddens at the end */}
            <div style={{position: 'absolute', left: x, top: TOP, width: BOX_W, height: BOX_H, border: `3px solid ${CLAUDE.SPARK}`, boxSizing: 'border-box', opacity: hot}} />
            <div style={{position: 'absolute', left: x, top: TOP + 34, width: BOX_W, fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.16em', color: MUTE, textAlign: 'center' as const, opacity: g}}>
              {String(i + 1).padStart(2, '0')}
            </div>
            <div style={{position: 'absolute', left: x + 14, top: TOP + 140, width: BOX_W - 28, fontFamily: CLAUDE_FONT.serif, fontSize: 56, color: CLAUDE.INK, textAlign: 'center' as const, opacity: g, lineHeight: 1.1}}>
              {s.label}
            </div>
            <div style={{position: 'absolute', left: x + 14, top: TOP + 232, width: BOX_W - 28, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, textAlign: 'center' as const, opacity: g, lineHeight: 1.3}}>
              {s.sub}
            </div>
            {/* connector into the next stage */}
            {i < n - 1 && (
              <div
                style={{
                  position: 'absolute', left: x + BOX_W, top: TOP + BOX_H / 2 - 1,
                  width: GAP * win(p, 0.16 + i * 0.14, 0.3 + i * 0.14), height: 2,
                  backgroundColor: RULE,
                }}
              />
            )}
          </React.Fragment>
        );
      })}
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B03 — WkTool: the tool, described in its own words.

   `quote` renders inside quotation marks because it IS the page's sentence,
   not a paraphrase. `source` is required. `note` is the honest disclosure that
   the quote is the entire public description — the reel does not pad a thin
   source, it reports the thinness.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ToolData = {
  slideMeta: string;
  name: string;
  quote: string;      // VERBATIM from the tool page
  chips: string[];
  audience: string;
  url: string;
  source: string;     // REQUIRED
  note: string;
};

export const WkTool: React.FC<{data: ToolData}> = ({data}) => {
  const p = useP();

  return (
    <PlainStage>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 6,
          fontFamily: CLAUDE_FONT.ui, fontSize: 22, letterSpacing: '.18em',
          color: MUTE, fontWeight: 600, opacity: win(p, 0.02, 0.14),
        }}
      >
        {data.slideMeta.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 52, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 132, color: CLAUDE.INK,
          lineHeight: 1, opacity: win(p, 0.06, 0.24),
        }}
      >
        {data.name}
      </div>

      {/* the page's own sentence, in quotes because it is verbatim */}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 230, width: SAFE.w * 0.94,
          fontFamily: CLAUDE_FONT.serif, fontSize: 58, fontStyle: 'italic' as const,
          color: CLAUDE.INK, lineHeight: 1.28, opacity: win(p, 0.24, 0.46),
        }}
      >
        “{data.quote}”
      </div>

      {data.chips.map((c, i) => {
        const g = win(p, 0.5 + i * 0.045, 0.62 + i * 0.045);
        const per = SAFE.w / data.chips.length;
        return <Chip key={i} text={c} left={SAFE.x + i * per} top={SAFE.y + 452} opacity={g} size={21} />;
      })}

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 560, width: SAFE.w * 0.9,
          fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK,
          lineHeight: 1.3, opacity: win(p, 0.66, 0.8),
        }}
      >
        {data.audience}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.y + 650,
          fontFamily: CLAUDE_FONT.mono, fontSize: 32, color: MUTE,
          opacity: win(p, 0.76, 0.88),
        }}
      >
        {data.url}
      </div>

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 118, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, letterSpacing: '.04em',
          opacity: win(p, 0.82, 0.92),
        }}
      >
        Source: {data.source}
      </div>
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.99)} accent />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — WkStatus: the same five stages, now with this week's real state.

   Laid out as ROWS rather than B02's columns, on purpose: the open stage
   carries a long detail line ("with Nina for review — Substack once approved")
   that does not fit a fifth of the safe width, and re-using the identical
   scheme three beats later would be the wallpaper smell ILLUSTRATE LAW warns
   about. Same stages, same order, different shape — a callback, not a repeat.
   ═══════════════════════════════════════════════════════════════════════════ */
export type StatusData = {
  slideMeta: string;
  title: string;
  stages: {label: string; detail: string; state: string}[];   // state: 'closed' | 'open'
  tally: string;
  note: string;
};

export const WkStatus: React.FC<{data: StatusData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 250;
  const STEP = 112;
  const MARK = 30;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.stages.map((s, i) => {
        const g = win(p, 0.06 + i * 0.13, 0.22 + i * 0.13);
        const open = s.state !== 'closed';
        const y = TOP + i * STEP;
        return (
          <React.Fragment key={i}>
            {/* filled square = closed; hollow terracotta square = open */}
            <div
              style={{
                position: 'absolute', left: SAFE.x, top: y + 14,
                width: MARK, height: MARK,
                backgroundColor: open ? 'transparent' : CLAUDE.INK,
                border: open ? `3px solid ${CLAUDE.SPARK}` : 'none',
                boxSizing: 'border-box', opacity: g,
              }}
            />
            <div
              style={{
                position: 'absolute', left: SAFE.x + 66, top: y, width: 300,
                fontFamily: CLAUDE_FONT.serif, fontSize: 48,
                color: open ? CLAUDE.SPARK : CLAUDE.INK, opacity: g, lineHeight: 1.1,
              }}
            >
              {s.label}
            </div>
            <div
              style={{
                position: 'absolute', left: SAFE.x + 400, top: y + 10, width: SAFE.w - 400 - 210,
                fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: open ? CLAUDE.INK : MUTE,
                opacity: g, lineHeight: 1.28,
              }}
            >
              {s.detail}
            </div>
            <Chip
              text={open ? 'open' : 'closed'}
              left={SAFE.r - 170} top={y + 10} hot={open} opacity={g} size={20}
            />
            <div style={{position: 'absolute', left: SAFE.x, top: y + STEP - 26, width: SAFE.w * g, height: 1, backgroundColor: RULE}} />
          </React.Fragment>
        );
      })}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 122,
          fontFamily: CLAUDE_FONT.ui, fontSize: 30, letterSpacing: '.1em',
          textTransform: 'uppercase' as const, color: MUTE, opacity: win(p, 0.8, 0.9),
        }}
      >
        {data.tally}
      </div>
      <NoteLine note={data.note} opacity={win(p, 0.88, 0.97)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — WkShip: what was made, and where it went.

   Draws NO artwork. The deliverable is named and routed; a mock-up of the
   graphics would be an invented artifact presented as the week's output. The
   chip says MADE, not LIVE — see the header note.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ShipData = {
  slideMeta: string;
  title: string;
  made: {label: string; sub: string};
  destination: {label: string; sub: string};
  chip: string;
  note: string;
};

export const WkShip: React.FC<{data: ShipData}> = ({data}) => {
  const p = useP();
  const BOX_W = 700;
  const BOX_H = 380;
  const TOP = SAFE.y + 280;
  const MIDY = TOP + BOX_H / 2;
  const leftIn = win(p, 0.08, 0.3);
  const rightIn = win(p, 0.56, 0.76);
  const wireIn = win(p, 0.4, 0.6);
  const chipIn = win(p, 0.74, 0.88);

  const node = (x: number, d: {label: string; sub: string}, g: number) => (
    <>
      <div style={{position: 'absolute', left: x, top: TOP, width: BOX_W, height: BOX_H, border: `2px solid ${RULE}`, boxSizing: 'border-box', opacity: g}} />
      <div style={{position: 'absolute', left: x + 34, top: TOP + 96, maxWidth: BOX_W - 68, fontFamily: CLAUDE_FONT.serif, fontSize: 62, color: CLAUDE.INK, opacity: g, lineHeight: 1.1}}>
        {d.label}
      </div>
      <div style={{position: 'absolute', left: x + 34, top: TOP + 240, maxWidth: BOX_W - 68, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, opacity: g, lineHeight: 1.3}}>
        {d.sub}
      </div>
    </>
  );

  const wireX = SAFE.x + BOX_W;
  const wireW = (SAFE.r - BOX_W) - wireX;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {node(SAFE.x, data.made, leftIn)}
      {node(SAFE.r - BOX_W, data.destination, rightIn)}

      {/* the route */}
      <div style={{position: 'absolute', left: wireX, top: MIDY - 1, width: wireW * wireIn, height: 2, backgroundColor: MUTE, opacity: 0.7}} />
      <Chip
        text={data.chip}
        left={wireX + wireW / 2 - 62} top={MIDY - 62}
        hot opacity={chipIn} size={22}
      />

      <NoteLine note={data.note} opacity={win(p, 0.88, 0.98)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B07 — WkReview: two articles that exist, and are not shown.

   THE MISSING PROPS ARE THE POINT. `slots` carries a label and nothing else —
   no title, summary, excerpt or content field exists on this type, so the
   articles cannot be described even by accident. They render as dashed empty
   cards under a withheld band, and the Substack node stays hollow because
   nothing has been published.
   ═══════════════════════════════════════════════════════════════════════════ */
export type ReviewData = {
  slideMeta: string;
  title: string;
  slots: {label: string}[];      // label ONLY — see the note above
  withhold: string;
  stages: {label: string; state: string}[];   // 'done' | 'current' | 'pending'
  note: string;
};

export const WkReview: React.FC<{data: ReviewData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 240;
  const SLOT_H = 200;
  const GAP = 60;
  const SLOT_W = (SAFE.w - GAP) / 2;
  const BAND_Y = TOP + SLOT_H + 26;
  const TRACK_Y = BAND_Y + 150;
  const n = data.stages.length;
  const NODE_GAP = 84;
  const NODE_W = (SAFE.w - NODE_GAP * (n - 1)) / n;
  const NODE_H = 140;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />

      {/* the articles: dashed, empty, unnamed */}
      {data.slots.map((s, i) => {
        const g = win(p, 0.06 + i * 0.1, 0.24 + i * 0.1);
        const x = SAFE.x + i * (SLOT_W + GAP);
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: x, top: TOP, width: SLOT_W, height: SLOT_H, border: `2px dashed ${RULE}`, boxSizing: 'border-box', opacity: g}} />
            <div
              style={{
                position: 'absolute', left: x, top: TOP + SLOT_H / 2 - 26, width: SLOT_W,
                fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: MUTE,
                textAlign: 'center' as const, opacity: g,
              }}
            >
              {s.label}
            </div>
          </React.Fragment>
        );
      })}

      <div
        style={{
          position: 'absolute', left: SAFE.x, top: BAND_Y, width: SAFE.w, height: 64,
          border: `1px solid ${RULE}`, boxSizing: 'border-box',
          opacity: win(p, 0.3, 0.46),
        }}
      />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: BAND_Y + 18, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 27, letterSpacing: '.08em',
          color: MUTE, textAlign: 'center' as const, opacity: win(p, 0.34, 0.5),
        }}
      >
        {data.withhold}
      </div>

      {/* written → in review → substack */}
      {data.stages.map((s, i) => {
        const g = win(p, 0.5 + i * 0.13, 0.66 + i * 0.13);
        const x = SAFE.x + i * (NODE_W + NODE_GAP);
        const current = s.state === 'current';
        const done = s.state === 'done';
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: x, top: TRACK_Y, width: NODE_W, height: NODE_H,
                backgroundColor: done ? CLAUDE.INK : 'transparent',
                border: current ? `3px solid ${CLAUDE.SPARK}` : done ? 'none' : `2px dashed ${RULE}`,
                boxSizing: 'border-box', opacity: g,
              }}
            />
            <div
              style={{
                position: 'absolute', left: x + 12, top: TRACK_Y + NODE_H / 2 - 24, width: NODE_W - 24,
                fontFamily: CLAUDE_FONT.ui, fontSize: 32,
                color: done ? CLAUDE.PAGE : current ? CLAUDE.SPARK : MUTE,
                textAlign: 'center' as const, opacity: g, lineHeight: 1.2,
              }}
            >
              {s.label}
            </div>
            {i < n - 1 && (
              <div style={{position: 'absolute', left: x + NODE_W, top: TRACK_Y + NODE_H / 2 - 1, width: NODE_GAP * g, height: 2, backgroundColor: RULE}} />
            )}
          </React.Fragment>
        );
      })}

      <NoteLine note={data.note} opacity={win(p, 0.9, 0.98)} />
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B08 — WkNotClaiming: the two columns, side by side.

   The falsifiability beat for a first-person recap. Putting the refusals ON
   SCREEN next to the claims is what stops the frame implying more than the
   week earned; saying it only in the voice would leave the visuals overclaiming.
   ═══════════════════════════════════════════════════════════════════════════ */
export type NotClaimingData = {
  slideMeta: string;
  title: string;
  claiming: {heading: string; items: string[]};
  notClaiming: {heading: string; items: string[]};
  note: string;
};

export const WkNotClaiming: React.FC<{data: NotClaimingData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 250;
  const MID = SAFE.x + SAFE.w / 2;
  const COL_W = SAFE.w / 2 - 60;
  const STEP = 130;

  const column = (
    x: number,
    side: {heading: string; items: string[]},
    hot: boolean,
    from: number,
  ) => (
    <>
      <div
        style={{
          position: 'absolute', left: x, top: TOP,
          fontFamily: CLAUDE_FONT.ui, fontSize: 28, letterSpacing: '.14em', fontWeight: 600,
          textTransform: 'uppercase' as const, color: hot ? CLAUDE.SPARK : MUTE,
          opacity: win(p, from - 0.06, from), maxWidth: COL_W,
        }}
      >
        {side.heading}
      </div>
      {side.items.map((it, i) => {
        const g = win(p, from + i * 0.1, from + 0.12 + i * 0.1);
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: x, top: TOP + 84 + i * STEP, width: COL_W,
                fontFamily: CLAUDE_FONT.ui, fontSize: 38, lineHeight: 1.26,
                color: hot ? CLAUDE.SPARK : CLAUDE.INK, opacity: g,
                transform: `translateY(${(1 - g) * 12}px)`,
              }}
            >
              {it}
            </div>
            <div style={{position: 'absolute', left: x, top: TOP + 84 + i * STEP + STEP - 34, width: COL_W * g, height: 1, backgroundColor: RULE}} />
          </React.Fragment>
        );
      })}
    </>
  );

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {/* the divide, drawn before either side fills */}
      <div
        style={{
          position: 'absolute', left: MID, top: TOP - 20,
          width: 2, height: (SAFE.b - TOP - 100) * win(p, 0.04, 0.18),
          backgroundColor: RULE,
        }}
      />
      {column(SAFE.x, data.claiming, false, 0.14)}
      {column(MID + 58, data.notClaiming, true, 0.5)}
      <NoteLine note={data.note} opacity={win(p, 0.9, 0.98)} />
    </PlainStage>
  );
};
