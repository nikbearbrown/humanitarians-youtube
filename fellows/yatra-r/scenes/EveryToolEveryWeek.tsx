/**
 * EveryToolEveryWeek.tsx — reel-local scenes for `yatra-every-tool-every-week`
 * ("Every Tool, Every Week."), a first-person progress report on the Humanitarians AI
 * tools.
 *
 * GENRE NOTE. This reel is not a concept explainer — it reports what one person actually
 * did in one week. So the binding constraint here is not "no invented statistics" but the
 * stricter "no invented FACTS": nothing on screen may assert a tool count, a date, a
 * metric, a description of what the Ogilvy tool does, or that the article is published.
 * The components below are built so those things are not expressible:
 *   · YtwWeeks shows ONE named week and an open-ended run of unnamed ones — it cannot
 *     render a schedule length or a tool count.
 *   · YtwStatus renders a fixed two-state row (done / not done) — it cannot claim a
 *     publish date or a soft launch.
 *   · YtwLoop takes labelled steps only — no throughput, no timing.
 *
 * Terracotta is the ONE accent per beat and always marks THE OPEN OR BROKEN THING: the
 * step that was down, the unposted draft. The accent tracks honesty rather than emphasis.
 *
 * Two shapes are reused rather than rebuilt — `JdgSplit` (two-column ledger) and
 * `JdgStakes` (N named items with a one-line why). They are generic, already QC'd, and
 * re-exported here under this reel's names so the beat sheet reads in its own vocabulary.
 * (They live in JudgmentIsTheJob.tsx only because that is the reel that first needed
 * them; promoting both into a shared illustrations module is the obvious follow-up.)
 */
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {PlainStage, Head, RULE, MUTE, win} from './claudeStage';
import {JdgSplit, JdgStakes} from './JudgmentIsTheJob';

/** Reused generic shapes, renamed for this reel's beat sheet. */
export const YtwSplit = JdgSplit;
export const YtwChecks = JdgStakes;

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/* ═══════════════════════════════════════════════════════════════════════════
   B01 — YtwLoop: the per-tool loop, with the step that was broken.
   ═══════════════════════════════════════════════════════════════════════════ */
export type LoopData = {
  slideMeta: string;
  title: string;
  steps: {label: string; note: string}[];
  /** index of the step to mark broken, or -1 for none */
  breakIndex: number;
  breakLabel: string;
};

export const YtwLoop: React.FC<{data: LoopData}> = ({data}) => {
  const p = useP();
  const n = data.steps.length;
  const TOP = SAFE.y + 300;
  const GAP = 26;
  const CARD_W = (SAFE.w - GAP * (n - 1)) / n;
  const CARD_H = 300;
  const brk = win(p, 0.82, 0.94);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {data.steps.map((s, i) => {
        const g = win(p, 0.08 + i * 0.13, 0.22 + i * 0.13);
        const x = SAFE.x + i * (CARD_W + GAP);
        const isBroken = i === data.breakIndex;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: x, top: TOP, width: CARD_W, height: CARD_H,
                backgroundColor: '#FFFFFF',
                border: `${1 + 3 * (isBroken ? brk : 0)}px solid ${isBroken && brk > 0 ? CLAUDE.SPARK : '#E5E2D9'}`,
                borderRadius: 10, opacity: g,
                transform: `translateY(${(1 - g) * 16}px)`,
                boxSizing: 'border-box', padding: 26,
              }}
            >
              <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 22, color: MUTE, letterSpacing: '.14em'}}>
                STEP {i + 1}
              </div>
              <div
                style={{
                  marginTop: 16, fontFamily: CLAUDE_FONT.ui, fontSize: 38, lineHeight: 1.15,
                  color: isBroken && brk > 0 ? CLAUDE.SPARK : CLAUDE.INK,
                }}
              >
                {s.label}
              </div>
              <div style={{marginTop: 18, fontFamily: CLAUDE_FONT.ui, fontSize: 24, color: MUTE, lineHeight: 1.3}}>
                {s.note}
              </div>
            </div>
            {/* connector into the next step */}
            {i < n - 1 && (
              <div
                style={{
                  position: 'absolute', left: x + CARD_W + 4, top: TOP + CARD_H / 2 - 1,
                  width: (GAP - 8) * win(p, 0.14 + i * 0.13, 0.26 + i * 0.13),
                  height: 2, backgroundColor: RULE,
                }}
              />
            )}
          </React.Fragment>
        );
      })}

      {/* the return arrow — this repeats, per tool */}
      <div style={{opacity: win(p, 0.6, 0.72)}}>
        <div style={{position: 'absolute', left: SAFE.x, top: TOP + CARD_H + 70, width: SAFE.w, height: 2, backgroundColor: RULE}} />
        <div
          style={{
            position: 'absolute', left: SAFE.x, top: TOP + CARD_H + 84,
            fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, letterSpacing: '.06em',
          }}
        >
          ↺ then the next tool
        </div>
      </div>

      {/* the break mark — the ONE accent */}
      {data.breakIndex >= 0 && (
        <div style={{opacity: brk}}>
          {/* Sits on the card's BOTTOM edge, not through its middle. At CARD_H/2 the bar
              crossed the note line and read as a strikethrough — "this text is cancelled"
              rather than "this step was broken". Caught by looking at the frame; the
              numeric checks were all clean. */}
          <div
            style={{
              position: 'absolute',
              left: SAFE.x + data.breakIndex * (CARD_W + GAP),
              top: TOP + CARD_H - 6,
              width: CARD_W, height: 6, backgroundColor: CLAUDE.SPARK,
            }}
          />
          <div
            style={{
              position: 'absolute',
              left: SAFE.x + data.breakIndex * (CARD_W + GAP),
              top: TOP - 54, width: CARD_W * 2,
              fontFamily: CLAUDE_FONT.ui, fontSize: 28, color: CLAUDE.SPARK, letterSpacing: '.05em',
            }}
          >
            {data.breakLabel}
          </div>
        </div>
      )}
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B05 — YtwWeeks: one named week, then an open-ended run of unnamed ones.
   Deliberately cannot express a schedule length or a tool count.
   ═══════════════════════════════════════════════════════════════════════════ */
export type WeeksData = {
  slideMeta: string;
  title: string;
  first: string;
  waitingLabel: string;
  note: string;
};

export const YtwWeeks: React.FC<{data: WeeksData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 320;
  const H = 240;
  const SLOTS = 5;                       // visual rhythm only — not a schedule length
  const GAP = 24;
  // The strip must read as "this keeps going" WITHOUT leaving the title-safe box. An
  // earlier version overshot SAFE by 260px to run off-frame; Gate V correctly failed it
  // (x_max 3705 against a right edge of 3648). Continuation is now carried by the last
  // slot's fade and the trailing ellipsis, which costs nothing and stays legal.
  const W = (SAFE.w - GAP * (SLOTS - 1)) / SLOTS;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {Array.from({length: SLOTS}).map((_, i) => {
        const g = win(p, 0.1 + i * 0.09, 0.24 + i * 0.09);
        const named = i === 0;
        const fill = named ? win(p, 0.42, 0.56) : 0;
        const x = SAFE.x + i * (W + GAP);
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: x, top: TOP, width: W, height: H,
              border: `${1 + 3 * fill}px solid ${fill > 0 ? CLAUDE.SPARK : '#E0DCD1'}`,
              backgroundColor: '#FFFFFF', borderRadius: 10,
              opacity: g * (i === SLOTS - 1 ? 0.3 : i === SLOTS - 2 ? 0.6 : 1),   // fades out — it keeps going
              boxSizing: 'border-box', padding: 24,
            }}
          >
            <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 22, color: MUTE, letterSpacing: '.14em'}}>
              WEEK
            </div>
            <div
              style={{
                marginTop: 28, fontFamily: named ? CLAUDE_FONT.serif : CLAUDE_FONT.ui,
                fontSize: named ? 54 : 32,
                color: named && fill > 0 ? CLAUDE.SPARK : MUTE,
                lineHeight: 1.1,
              }}
            >
              {named ? data.first : data.waitingLabel}
            </div>
          </div>
        );
      })}
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: TOP + H + 70, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 44, color: CLAUDE.INK, lineHeight: 1.25,
          opacity: win(p, 0.88, 0.96),
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};

/* ═══════════════════════════════════════════════════════════════════════════
   B06 — YtwStatus: a document and its honest state. Two rows, done / not done.
   ═══════════════════════════════════════════════════════════════════════════ */
export type StatusData = {
  slideMeta: string;
  title: string;
  kicker: string;
  states: {label: string; done: boolean}[];
  note: string;
};

export const YtwStatus: React.FC<{data: StatusData}> = ({data}) => {
  const p = useP();
  const CARD_X = SAFE.x;
  const CARD_W = SAFE.w * 0.62;
  const TOP = SAFE.y + 300;

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.kicker} />
      <div
        style={{
          position: 'absolute', left: CARD_X, top: TOP, width: CARD_W,
          backgroundColor: '#FFFFFF', border: '1px solid #E5E2D9', borderRadius: 12,
          padding: 40, boxSizing: 'border-box',
          opacity: win(p, 0.08, 0.22),
        }}
      >
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 86, color: CLAUDE.INK, lineHeight: 1.05}}>
          {data.title}
        </div>
        <div style={{marginTop: 40, height: 1, backgroundColor: RULE}} />
        {data.states.map((s, i) => {
          const g = win(p, 0.4 + i * 0.26, 0.58 + i * 0.26);
          const accent = !s.done;
          return (
            <div key={i} style={{marginTop: 32, display: 'flex', alignItems: 'center', gap: 22, opacity: g}}>
              <div
                style={{
                  width: 26, height: 26, borderRadius: 4,
                  border: `3px solid ${accent ? CLAUDE.SPARK : CLAUDE.INK}`,
                  backgroundColor: s.done ? CLAUDE.INK : 'transparent',
                }}
              />
              <div
                style={{
                  fontFamily: CLAUDE_FONT.ui, fontSize: 44,
                  color: accent ? CLAUDE.SPARK : CLAUDE.INK,
                }}
              >
                {s.label}
              </div>
            </div>
          );
        })}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 70, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 44, color: CLAUDE.INK,
          opacity: win(p, 0.88, 0.96),
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};
