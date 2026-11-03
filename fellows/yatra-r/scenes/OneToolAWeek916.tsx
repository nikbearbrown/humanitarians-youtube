/**
 * OneToolAWeek916.tsx — PORTRAIT (9:16) scenes for `yatra-one-tool-a-week-brandy`.
 *
 * Re-banded vertically, not scaled: the card goes full working-width with its lines
 * stacked, and the team's name chips wrap onto their own rows instead of running along a
 * single line (three chips plus a "working with" chip do not fit across 906px).
 *
 * The honesty constraints carry over unchanged: `lines` render verbatim (no summary
 * field to tempt invention), article titles keep their supplied ellipses, and `status` is
 * required and rendered in the accent so a proposed initiative cannot read as underway.
 *
 * Shorts/Reels chrome keep-out respected: content above y≈1440, left of x≈960, bug
 * lower-left. This reel's vertical is 2:25, so it fits Reels and LinkedIn natively.
 */
import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE916} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {JdgSplit916} from './JudgmentIsTheJob916';
import {YtwWeeks916, YtwStatus916} from './EveryToolEveryWeek916';
import type {CardData, TeamData} from './OneToolAWeek';

export const RcpSplit916 = JdgSplit916;
export const RcpWeeks916 = YtwWeeks916;
export const RcpStatus916 = YtwStatus916;

const STAGE = '#F2F0E9';
const MUTE = '#7A7265';
const BOX = {x: SAFE916.x, y: SAFE916.y, w: 906, bottom: 1440} as const;

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

export const RcpCard916: React.FC<{data: CardData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 230;
  const open = win(p, 0.08, 0.26);
  return (
    <Stage>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.18em', color: MUTE, fontWeight: 600, opacity: open}}>
        {data.kicker.toUpperCase()}
      </div>
      <div
        style={{
          position: 'absolute', left: BOX.x, top: TOP, width: BOX.w,
          backgroundColor: '#FFFFFF', border: '1px solid #E5E2D9', borderRadius: 14,
          padding: 40, boxSizing: 'border-box', opacity: open,
          transform: `translateY(${(1 - open) * 18}px)`,
        }}
      >
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 72, color: CLAUDE.INK, lineHeight: 1.1}}>
          {data.title}
        </div>
        <div style={{marginTop: 24, width: `${100 * win(p, 0.6, 0.8)}%`, height: 5, backgroundColor: CLAUDE.SPARK}} />
        {data.lines.map((l, i) => (
          <div key={i} style={{marginTop: i === 0 ? 28 : 14, fontFamily: CLAUDE_FONT.ui, fontSize: 36, color: CLAUDE.INK, lineHeight: 1.3, opacity: win(p, 0.38 + i * 0.12, 0.56 + i * 0.12)}}>
            {l}
          </div>
        ))}
        {data.link ? (
          <div style={{marginTop: 30, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: CLAUDE.SPARK, opacity: win(p, 0.68, 0.84), wordBreak: 'break-all'}}>
            {data.link}
          </div>
        ) : null}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 90, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: CLAUDE.INK, lineHeight: 1.25, opacity: win(p, 0.86, 0.96)}}>
        {data.note}
      </div>
    </Stage>
  );
};

export const RcpTeam916: React.FC<{data: TeamData}> = ({data}) => {
  const p = useP();
  const TOP = BOX.y + 260;
  const ROW = 108;
  return (
    <Stage>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 26, letterSpacing: '.16em', color: MUTE, fontWeight: 600}}>
        {data.slideMeta.toUpperCase()}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.y + 76, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 76, color: CLAUDE.INK, lineHeight: 1.06}}>
        {data.title}
      </div>
      {/* chips STACK in portrait — three names plus a 'working with' chip won't fit across */}
      {data.people.map((name, i) => {
        const g = win(p, 0.3 + i * 0.1, 0.44 + i * 0.1);
        return (
          <div key={i} style={{position: 'absolute', left: BOX.x, top: TOP + i * ROW, padding: '20px 38px', borderRadius: 999, border: '2px solid #D8D4C8', backgroundColor: '#FFFFFF', fontFamily: CLAUDE_FONT.ui, fontSize: 40, color: CLAUDE.INK, opacity: g, transform: `translateY(${(1 - g) * 12}px)`}}>
            {name}
          </div>
        );
      })}
      {(() => {
        const i = data.people.length;
        const g = win(p, 0.3 + i * 0.1, 0.46 + i * 0.1);
        return (
          <>
            <div style={{position: 'absolute', left: BOX.x, top: TOP + i * ROW + 8, fontFamily: CLAUDE_FONT.ui, fontSize: 30, color: MUTE, opacity: g}}>
              {data.withLabel}
            </div>
            <div style={{position: 'absolute', left: BOX.x + 220, top: TOP + i * ROW - 8, padding: '20px 38px', borderRadius: 999, border: '2px solid #D8D4C8', backgroundColor: '#FFFFFF', fontFamily: CLAUDE_FONT.ui, fontSize: 40, color: CLAUDE.INK, opacity: g}}>
              {data.withPerson}
            </div>
          </>
        );
      })()}
      {data.remit.map((r, i) => (
        <div key={i} style={{position: 'absolute', left: BOX.x, top: TOP + (data.people.length + 1) * ROW + 20 + i * 62, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.INK, opacity: win(p, 0.62 + i * 0.08, 0.76 + i * 0.08)}}>
          · {r}
        </div>
      ))}
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 170, width: BOX.w * 0.7 * win(p, 0.84, 0.94), height: 5, backgroundColor: CLAUDE.SPARK}} />
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 148, width: BOX.w, fontFamily: CLAUDE_FONT.ui, fontSize: 38, color: CLAUDE.SPARK, lineHeight: 1.2, opacity: win(p, 0.85, 0.95)}}>
        {data.status}
      </div>
      <div style={{position: 'absolute', left: BOX.x, top: BOX.bottom - 62, width: BOX.w, fontFamily: CLAUDE_FONT.serif, fontSize: 36, color: CLAUDE.INK, lineHeight: 1.25, opacity: win(p, 0.9, 0.98)}}>
        {data.note}
      </div>
    </Stage>
  );
};
