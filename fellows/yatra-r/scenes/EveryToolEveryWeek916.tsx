/**
 * EveryToolEveryWeek916.tsx — PORTRAIT (9:16) scenes for `yatra-every-tool-every-week`.
 *
 * THE COMPOSITION LOGIC (Shorts law): "16:9 lays out SIDE BY SIDE; 9:16 stacks TOP AND
 * BOTTOM. Portrait relayouts re-band the same content vertically — they never merely scale
 * the landscape composition down." Applied here:
 *   · YtwLoop916   — the four steps run left-to-right in landscape; here they STACK, and
 *                    the "then the next tool" return reads as a loop back to the top.
 *   · YtwWeeks916  — the week strip becomes a vertical list of week rows.
 *   · YtwStatus916 — the document card goes full-width with the states beneath it.
 *
 * SHORTS UI KEEP-OUT: content stays left of x≈960 and above y≈1440, and the corner bug
 * sits lower-LEFT, because the Shorts chrome owns the bottom ~25% and right ~11%.
 *
 * Two shapes are reused from the previous reel's portrait set (JdgSplit916, JdgStakes916)
 * — they are generic and already QC'd in portrait.
 *
 * Same honesty constraint as the landscape set: no tool count, no date, no metric is
 * expressible. YtwWeeks916 names ONE week and fades the rest.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {JdgSplit916, JdgStakes916} from './JudgmentIsTheJob916';
import type {LoopData, WeeksData, StatusData} from './EveryToolEveryWeek';

/** Reused generic portrait shapes, renamed for this reel's short sheet. */
export const YtwSplit916 = JdgSplit916;
export const YtwChecks916 = JdgStakes916;

const STAGE = '#F2F0E9';
const RULE = '#D8D4C8';
const MUTE = '#7A7265';

const BOX = {x: SAFE916.x, y: SAFE916.y, w: 906, bottom: 1440} as const;

const ease = (t: number) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
const win = (p: number, a: number, b: number) => ease((p - a) / (b - a));

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

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

/* ── B01 — the four steps STACK (was: a left-to-right row) ───────────────── */
export const YtwLoop916: React.FC<{data: LoopData}> = ({data}) => {
  const p = useP();
  const n = data.steps.length;
  const TOP = BOX.y + 290;
  const ROW = Math.min(220, (BOX.bottom - 130 - TOP) / n);
  const brk = win(p, 0.82, 0.94);

  return (
    <Stage916>
      <Head916 meta={data.slideMeta} title={data.title} />
      {data.steps.map((s, i) => {
        const g = win(p, 0.08 + i * 0.13, 0.22 + i * 0.13);
        const y = TOP + i * ROW;
        const isBroken = i === data.breakIndex;
        const hot = isBroken && brk > 0;
        return (
          <React.Fragment key={i}>
            <div
              style={{
                position: 'absolute', left: BOX.x, top: y, width: BOX.w,
                height: ROW - 18, backgroundColor: '#FFFFFF',
                border: `${1 + 3 * (isBroken ? brk : 0)}px solid ${hot ? CLAUDE.SPARK : '#E5E2D9'}`,
                borderRadius: 10, opacity: g, boxSizing: 'border-box', padding: 22,
                transform: `translateY(${(1 - g) * 14}px)`,
              }}
            >
              <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 22, color: MUTE, letterSpacing: '.14em'}}>
                STEP {i + 1}
              </div>
              <div style={{marginTop: 10, fontFamily: CLAUDE_FONT.ui, fontSize: 46, lineHeight: 1.1, color: hot ? CLAUDE.SPARK : CLAUDE.INK}}>
                {s.label}
              </div>
              <div style={{marginTop: 8, fontFamily: CLAUDE_FONT.ui, fontSize: 26, color: MUTE, lineHeight: 1.25}}>
                {s.note}
              </div>
            </div>
            {/* the break underlines the card — never crosses its text */}
            {hot && (
              <div style={{position: 'absolute', left: BOX.x, top: y + ROW - 24, width: BOX.w, height: 6, backgroundColor: CLAUDE.SPARK, opacity: brk}} />
            )}
          </React.Fragment>
        );
      })}
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 76, width: BOX.w, opacity: win(p, 0.6, 0.72)}}>
        <div style={{width: BOX.w, height: 1, backgroundColor: RULE}} />
        <div style={{marginTop: 14, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE}}>
          ↺ then the next tool
        </div>
      </div>
      {data.breakIndex >= 0 && (
        <div
          style={{
            position: 'absolute', left: BOX.x, top: TOP - 52, width: BOX.w,
            fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.SPARK, opacity: brk,
          }}
        >
          {data.breakLabel}
        </div>
      )}
    </Stage916>
  );
};

/* ── B05 — week slots STACK as rows (was: a horizontal strip) ────────────── */
export const YtwWeeks916: React.FC<{data: WeeksData}> = ({data}) => {
  const p = useP();
  const SLOTS = 4;
  const TOP = BOX.y + 300;
  const ROW = Math.min(210, (BOX.bottom - 140 - TOP) / SLOTS);

  return (
    <Stage916>
      <Head916 meta={data.slideMeta} title={data.title} />
      {Array.from({length: SLOTS}).map((_, i) => {
        const g = win(p, 0.1 + i * 0.11, 0.26 + i * 0.11);
        const named = i === 0;
        const fill = named ? win(p, 0.42, 0.56) : 0;
        const fade = i === SLOTS - 1 ? 0.32 : i === SLOTS - 2 ? 0.62 : 1;
        return (
          <div
            key={i}
            style={{
              position: 'absolute', left: BOX.x, top: TOP + i * ROW, width: BOX.w,
              height: ROW - 20, backgroundColor: '#FFFFFF',
              border: `${1 + 3 * fill}px solid ${fill > 0 ? CLAUDE.SPARK : '#E0DCD1'}`,
              borderRadius: 10, opacity: g * fade,
              boxSizing: 'border-box', padding: 24,
              display: 'flex', alignItems: 'center', gap: 26,
            }}
          >
            <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 22, color: MUTE, letterSpacing: '.14em'}}>
              WEEK
            </div>
            <div
              style={{
                fontFamily: named ? CLAUDE_FONT.serif : CLAUDE_FONT.ui,
                fontSize: named ? 58 : 34,
                color: named && fill > 0 ? CLAUDE.SPARK : MUTE, lineHeight: 1.1,
              }}
            >
              {named ? data.first : data.waitingLabel}
            </div>
          </div>
        );
      })}
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 84, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK, lineHeight: 1.25,
          opacity: win(p, 0.88, 0.96),
        }}
      >
        {data.note}
      </div>
    </Stage916>
  );
};

/* ── B06 — the document card, full width, states beneath ─────────────────── */
export const YtwStatus916: React.FC<{data: StatusData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 300;
  return (
    <Stage916>
      <Head916 meta={data.slideMeta} title={data.kicker} />
      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP, width: BOX.w,
          backgroundColor: '#FFFFFF', border: '1px solid #E5E2D9', borderRadius: 12,
          padding: 36, boxSizing: 'border-box', opacity: win(p, 0.08, 0.22),
        }}
      >
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 92, color: CLAUDE.INK, lineHeight: 1.05}}>
          {data.title}
        </div>
        <div style={{marginTop: 34, height: 1, backgroundColor: RULE}} />
        {data.states.map((s, i) => {
          const g = win(p, 0.4 + i * 0.26, 0.58 + i * 0.26);
          const accent = !s.done;
          return (
            <div key={i} style={{marginTop: 30, display: 'flex', alignItems: 'center', gap: 20, opacity: g}}>
              <div
                style={{
                  width: 28, height: 28, borderRadius: 4,
                  border: `3px solid ${accent ? CLAUDE.SPARK : CLAUDE.INK}`,
                  backgroundColor: s.done ? CLAUDE.INK : 'transparent',
                }}
              />
              <div style={{fontFamily: CLAUDE_FONT.ui, fontSize: 46, color: accent ? CLAUDE.SPARK : CLAUDE.INK}}>
                {s.label}
              </div>
            </div>
          );
        })}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: BOX.bottom - 84, width: BOX.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK, lineHeight: 1.25,
          opacity: win(p, 0.88, 0.96),
        }}
      >
        {data.note}
      </div>
    </Stage916>
  );
};
