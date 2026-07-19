import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './empty_timing.json';
import { ClaudeComposerAsk } from '../runtime/scenes/ClaudeComposerAsk';
import { claudeComposerAskSchema } from '../runtime/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../onda/registry/components/claude-callout/schema';
import { CLAUDE, CLAUDE_FONT } from '../runtime/tokens/claude';

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const COMMAND = 'why am I out of usage until Friday?';

// Callouts in ACCUMULATION order (one per beat B01..B05), each pointing at
// the window element it indicts. Geometry: proven 1280x720 slots.
const ITEMS = [
  { title: 'the real cost', body: 'run dry Tuesday.\nwork returns at reset.\nthe wait is the price.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'one chip, all the blame', body: 'Fable 5 + High\non everything —\nemail drafts included.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
  { title: 'judgment on chores', body: 'the architecture model\ndoesn’t need to\nrename your files.', x: 0.22, y: 0.42, targetX: 0.34, targetY: 0.52, bend: 0.2, delay: 0 },
  { title: 'opus takes the bulk', body: 'skill runs, batches,\nlong refactors —\nClaude Code’s lane.', x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'author high, run low', body: 'your best model writes\nthe skill once.\nquality freezes in.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
];

type Beat = { id: string; narration: string; kind: string; calloutIndex?: number; sparkLine?: string };
export const BEATS: Beat[] = [
  { id: 'B00', narration: 'I know people who stop working for days because they ran out of Claude. Not because the work stopped — because the model did. That’s not a limit problem. That’s a routing problem.', kind: 'ask' },
  { id: 'B01', narration: 'The real cost isn’t tokens. Run dry on Tuesday and the work just waits for the reset. The wait is the price — and it’s self-inflicted.', kind: 'claim', calloutIndex: 0, sparkLine: 'The wait is the price.' },
  { id: 'B02', narration: 'Where did it go? One chip: the flagship, effort on High, for everything. Hard problems, email drafts, renaming files — all billed at genius rates.', kind: 'claim', calloutIndex: 1, sparkLine: 'High on everything.' },
  { id: 'B03', narration: 'Flagship-by-default feels safe. But you’re spending judgment on chores. The model that can hold your whole architecture in its head does not need to rename your files.', kind: 'claim', calloutIndex: 2, sparkLine: 'Judgment spent on chores.' },
  { id: 'B04', narration: 'Route by task. The bulk work — running skills, batch renders, long refactors — hand it to Opus in Claude Code. That lane is built for the long haul.', kind: 'claim', calloutIndex: 3, sparkLine: 'Opus takes the bulk.' },
  { id: 'B05', narration: 'Save Fable for the words that get reused: the skill, the plan, the tricky call. Author with your best model once — the quality freezes into the file, and every cheap run inherits it.', kind: 'claim', calloutIndex: 4, sparkLine: 'Author high, run low.' },
  { id: 'B06', narration: 'Then Thursday’s hard problem arrives — and Fable is still there. Same budget. Different week.', kind: 'breathe', sparkLine: 'There when it counts.' },
  { id: 'B07', narration: 'The routing, on one page. Fable writes what gets reused. Opus runs it. Medium effort for the everyday, High only when it earns it. Usage is a budget — spend it where only your best will do.', kind: 'verdict' },
  { id: 'B08', narration: 'If this saves your Thursday, subscribe. Nik Bear Brown.', kind: 'outro' },
];
const TIMED = BEATS.map((b, i) => ({ ...b, frames: TIMING[i].frames, audio: TIMING[i].audio }));
export const TOTAL_FRAMES = TIMED.reduce((a, b) => a + b.frames, 0);

const Caption: React.FC<{ text: string; beatId: string }> = ({ text, beatId }) => (
  <div style={{
    position: 'absolute', left: '8%', right: '8%', bottom: '3.5%',
    textAlign: 'center', fontFamily: SANS, fontSize: 22, lineHeight: 1.4,
    color: CLAUDE.INK_SOFT, background: 'rgba(250,249,245,0.92)',
    border: `1px solid ${CLAUDE.BORDER}`, borderRadius: 10, padding: '10px 18px',
  }}>
    <span style={{ color: CLAUDE.SPARK, fontWeight: 700, marginRight: 10 }}>{beatId}</span>
    {text}
  </div>
);

// Inner beat: centered window, spark line (SPARK-LINE LAW), callouts accumulate.
const UsageBeat: React.FC<{ upTo: number; sparkLine: string }> = ({ upTo, sparkLine }) => {
  const settled = upTo > 0 ? ITEMS.slice(0, upTo).map((it) => ({ ...it })) : [];
  const active = upTo >= 0 && upTo < ITEMS.length ? [{ ...ITEMS[upTo] }] : [];
  const allSettled = upTo < 0 ? ITEMS.map((it) => ({ ...it })) : [];
  return (
    <AbsoluteFill style={{ background: '#F2F0E9' }}>
      <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
        <ClaudeWindow {...claudeWindowSchema.parse({
          view: 'composer', width: 640, height: 460, fontSize: 13,
          greeting: sparkLine, command: COMMAND, delay: 0, typeSpeed: 1,
        })} />
      </AbsoluteFill>
      {settled.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: settled, delay: -600, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
      {active.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: active, delay: 8, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
      {allSettled.length > 0 && (
        <ClaudeCallout {...claudeCalloutSchema.parse({ items: allSettled, delay: -600, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
      )}
    </AbsoluteFill>
  );
};

const VerdictBeat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9', alignItems: 'center', justifyContent: 'center' }}>
    <ClaudeWindow {...claudeWindowSchema.parse({
      view: 'artifact', width: 900, height: 560, fontSize: 17,
      artifactTitle: 'The Routing — one page',
      artifactHeading: 'Who does what',
      artifactLines: [
        'Fable 5 — skills, plans, the tricky calls. Words that get reused.',
        'Opus + Claude Code — runs, batches, refactors. The long haul.',
        'Effort Medium — the everyday default.',
        'Effort High — only when the problem earns it.',
      ],
    })} />
  </AbsoluteFill>
);

const OutroCard: React.FC = () => {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 12], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  return (
    <AbsoluteFill style={{ background: CLAUDE.PAGE, alignItems: 'center', justifyContent: 'center', opacity: o }}>
      <div style={{ fontFamily: SERIF, fontWeight: 700, fontSize: 76, color: '#111', letterSpacing: '-0.02em', textAlign: 'center', lineHeight: 1.05 }}>
        Claude, on empty<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@NikBearBrown</div>
      <div style={{ fontFamily: SANS, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · spend it where it counts</div>
    </AbsoluteFill>
  );
};

export const ClaudeOnEmpty: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ask') content = (
      <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
        greeting: 'Sawubona, Bear',
        topic: 'COWORK · USAGE',
        segment: 'Claude, On Empty',
        command: COMMAND,
        runningText: 'checking the spend…',
      })} />
    );
    else if (b.kind === 'claim') content = <UsageBeat upTo={b.calloutIndex!} sparkLine={b.sparkLine!} />;
    else if (b.kind === 'breathe') content = <UsageBeat upTo={-1} sparkLine={b.sparkLine!} />;
    else if (b.kind === 'verdict') content = <VerdictBeat />;
    else content = <OutroCard />;
    return (
      <Sequence key={b.id} from={from} durationInFrames={b.frames}>
        {content}
        <Audio src={staticFile(b.audio)} />
        <Caption text={b.narration} beatId={b.id} />
      </Sequence>
    );
  });
  return <AbsoluteFill style={{ background: CLAUDE.PAGE }}>{seqs}</AbsoluteFill>;
};
