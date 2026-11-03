/**
 * OneToolAWeek.tsx — scenes for `yatra-one-tool-a-week-brandy`, a weekly recap of the
 * Humanitarians AI tool series.
 *
 * HONESTY CONSTRAINT (from the human, and it shapes both components):
 * tool descriptions and article summaries must stay exactly at the level supplied —
 * Brandy is "a brand-audit tool", Ogilvy is "an AI copywriting coach" — with no invented
 * audit findings, coaching outcomes or statistics. So:
 *
 *   · RcpCard takes `lines: string[]` and renders them verbatim. There is no "summary"
 *     or "findings" field, because a field like that is an invitation to fill it.
 *   · RcpTeam requires a `status` string and renders it in the accent colour, so a
 *     proposed initiative cannot be shown as if it were underway. The reel's fashion-team
 *     beat is PROPOSED, and the component makes that the most visible thing on the card.
 *
 * Article titles arrive PARTIAL from the human ("I Ran Our Own Brand Audit Tool On…") and
 * are rendered verbatim, ellipsis included — never completed by guesswork.
 *
 * Terracotta marks the actionable or the unfinished: the tool link, the title rule, the
 * "proposed, not started" status.
 */
import React from 'react';
import {useCurrentFrame, useVideoConfig} from 'remotion';
import {SAFE} from '../tokens/layout';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {PlainStage, Head, RULE, MUTE, win} from './claudeStage';
import {JdgSplit} from './JudgmentIsTheJob';
import {YtwWeeks, YtwStatus} from './EveryToolEveryWeek';

/** Reused generic shapes under this reel's names (own registrations, own durations). */
export const RcpSplit = JdgSplit;
export const RcpWeeks = YtwWeeks;
export const RcpStatus = YtwStatus;

const useP = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return Math.min(1, Math.max(0, frame / Math.max(1, durationInFrames - 1)));
};

/* ═══ A tool or an article, as a card ════════════════════════════════════ */
export type CardData = {
  kicker: string;
  title: string;
  /** rendered verbatim — deliberately not a "summary" field */
  lines: string[];
  /** empty string = no link row */
  link: string;
  note: string;
};

export const RcpCard: React.FC<{data: CardData}> = ({data}) => {
  const p = useP();
  const X = SAFE.x;
  const W = SAFE.w * 0.78;
  const TOP = SAFE.y + 250;
  const open = win(p, 0.08, 0.26);

  return (
    <PlainStage>
      <div
        style={{
          position: 'absolute', left: X, top: SAFE.y + 6, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 24, letterSpacing: '.18em',
          color: MUTE, fontWeight: 600, opacity: open,
        }}
      >
        {data.kicker.toUpperCase()}
      </div>

      <div
        style={{
          position: 'absolute', left: X, top: TOP, width: W,
          backgroundColor: '#FFFFFF', border: '1px solid #E5E2D9', borderRadius: 14,
          padding: 48, boxSizing: 'border-box', opacity: open,
          transform: `translateY(${(1 - open) * 18}px)`,
        }}
      >
        <div style={{fontFamily: CLAUDE_FONT.serif, fontSize: 82, color: CLAUDE.INK, lineHeight: 1.08}}>
          {data.title}
        </div>
        {/* the accent underlines the title rather than colouring it */}
        <div style={{marginTop: 26, width: `${100 * win(p, 0.6, 0.8)}%`, height: 5, backgroundColor: CLAUDE.SPARK}} />
        {data.lines.map((l, i) => (
          <div
            key={i}
            style={{
              marginTop: i === 0 ? 30 : 16,
              fontFamily: CLAUDE_FONT.ui, fontSize: 38, color: CLAUDE.INK, lineHeight: 1.3,
              opacity: win(p, 0.38 + i * 0.12, 0.56 + i * 0.12),
            }}
          >
            {l}
          </div>
        ))}
        {data.link ? (
          <div
            style={{
              marginTop: 34, fontFamily: CLAUDE_FONT.ui, fontSize: 34, color: CLAUDE.SPARK,
              opacity: win(p, 0.68, 0.84), wordBreak: 'break-all',
            }}
          >
            {data.link}
          </div>
        ) : null}
      </div>

      <div
        style={{
          position: 'absolute', left: X, top: SAFE.b - 62, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 40, color: CLAUDE.INK,
          opacity: win(p, 0.86, 0.96),
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};

/* ═══ A team, and whether it has actually started ════════════════════════ */
export type TeamData = {
  slideMeta: string;
  title: string;
  /** REQUIRED and rendered in the accent — a proposal cannot be shown as underway */
  status: string;
  people: string[];
  withLabel: string;
  withPerson: string;
  remit: string[];
  note: string;
};

export const RcpTeam: React.FC<{data: TeamData}> = ({data}) => {
  const p = useP();
  const TOP = SAFE.y + 300;
  const chip = (label: string, x: number, y: number, g: number, accent: boolean) => (
    <div
      style={{
        position: 'absolute', left: x, top: y,
        padding: '22px 40px', borderRadius: 999,
        border: `2px solid ${accent ? CLAUDE.SPARK : '#D8D4C8'}`,
        backgroundColor: '#FFFFFF',
        fontFamily: CLAUDE_FONT.ui, fontSize: 42,
        color: accent ? CLAUDE.SPARK : CLAUDE.INK,
        opacity: g, transform: `translateY(${(1 - g) * 14}px)`,
        whiteSpace: 'nowrap',
      }}
    >
      {label}
    </div>
  );

  let x = SAFE.x;
  const chips = data.people.map((name, i) => {
    const g = win(p, 0.3 + i * 0.1, 0.44 + i * 0.1);
    const el = chip(name, x, TOP, g, false);
    x += name.length * 26 + 96;
    return <React.Fragment key={i}>{el}</React.Fragment>;
  });
  const withG = win(p, 0.3 + data.people.length * 0.1, 0.46 + data.people.length * 0.1);

  return (
    <PlainStage>
      <Head meta={data.slideMeta} title={data.title} />
      {chips}
      <div
        style={{
          position: 'absolute', left: x + 10, top: TOP + 26,
          fontFamily: CLAUDE_FONT.ui, fontSize: 32, color: MUTE, opacity: withG,
        }}
      >
        {data.withLabel}
      </div>
      {chip(data.withPerson, x + 10 + data.withLabel.length * 17 + 30, TOP, withG, false)}

      {data.remit.map((r, i) => (
        <div
          key={i}
          style={{
            position: 'absolute', left: SAFE.x, top: TOP + 160 + i * 78, width: SAFE.w,
            fontFamily: CLAUDE_FONT.ui, fontSize: 40, color: CLAUDE.INK,
            opacity: win(p, 0.62 + i * 0.08, 0.76 + i * 0.08),
          }}
        >
          · {r}
        </div>
      ))}

      {/* the status is the loudest thing on the card, by design */}
      <div style={{position: 'absolute', left: SAFE.x, top: SAFE.b - 150, width: SAFE.w * 0.6 * win(p, 0.84, 0.94), height: 5, backgroundColor: CLAUDE.SPARK}} />
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 128, width: SAFE.w,
          fontFamily: CLAUDE_FONT.ui, fontSize: 44, color: CLAUDE.SPARK,
          opacity: win(p, 0.85, 0.95),
        }}
      >
        {data.status}
      </div>
      <div
        style={{
          position: 'absolute', left: SAFE.x, top: SAFE.b - 58, width: SAFE.w,
          fontFamily: CLAUDE_FONT.serif, fontSize: 38, color: CLAUDE.INK,
          opacity: win(p, 0.9, 0.98),
        }}
      >
        {data.note}
      </div>
    </PlainStage>
  );
};
