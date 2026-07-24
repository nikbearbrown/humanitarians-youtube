import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './scripted_timing.json';
import { ClaudeComposerAsk } from '../runtime/scenes/ClaudeComposerAsk';
import { claudeComposerAskSchema } from '../runtime/scenes/ClaudeComposerAsk';
import { ClaudeWindow } from '../onda/registry/components/claude-window/ClaudeWindow';
import { claudeWindowSchema } from '../onda/registry/components/claude-window/schema';
import { ClaudeCallout } from '../onda/registry/components/claude-callout/ClaudeCallout';
import { claudeCalloutSchema } from '../onda/registry/components/claude-callout/schema';
import { CodeBlock } from '../onda/registry/components/code-block/CodeBlock';
import { codeBlockSchema } from '../onda/registry/components/code-block/schema';
import { CLAUDE, CLAUDE_FONT } from '../runtime/tokens/claude';

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const COMMAND = 'why does claude keep rewriting the same ffmpeg loop?';

const ITEMS = [
  { title: 'the rewrite tax', body: 'same logic, re-derived.\nre-debugged, re-billed.\nevery single run.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'exact means script', body: 'two runs must agree?\nscript.\ntwo runs may differ? prompt.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
  { title: 'one belt', body: 'generate_audio.py,\ncompile.py —\none script, all brands.', x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'forks breed bugs', body: 'copied, not parameterized.\nthe bug now lives twice.\none fix misses the other.', x: 0.22, y: 0.66, targetX: 0.3, targetY: 0.66, bend: 0.15, delay: 0 },
  { title: 'reuse before you write', body: 'call it.\nparameterize it.\nonly then: write new.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
];

type Beat = { id: string; narration: string; kind: string; calloutIndex?: number; sparkLine?: string };
export const BEATS: Beat[] = [
  { id: 'B00', narration: 'Every reel I make runs the same ffmpeg loop. Same audio generation. Same timing conform. I never rewrite that logic — it lives in a script and gets called. This episode: why that decision is not laziness. It\'s the rule.', kind: 'ask' },
  { id: 'B01', narration: 'One call. Same result every time, regardless of reel, brand, or model. It measures the mp3s, calculates the frames, writes the timing file. Same answer this run as last run. That consistency is the feature.', kind: 'code' },
  { id: 'B02', narration: 'The alternative is asking Claude to re-derive it every run. Same ffmpeg flags, re-debugged. Same formula — ceiling of duration plus 0.4, times 30 — re-calculated, re-billed. Every run. That\'s the rewrite tax. You pay it in tokens and you pay it in drift.', kind: 'claim', calloutIndex: 0, sparkLine: 'The rewrite tax.' },
  { id: 'B03', narration: 'Here\'s the axis. Some work must come out exact — two runs must agree. Some work may vary — the second run can be different, even better. Scripts own the exact. Prompts own the variable. That\'s not preference. It\'s a decision rule.', kind: 'claim', calloutIndex: 1, sparkLine: 'Exact means script.' },
  { id: 'B04', narration: 'In this pipeline, one belt of scripts handles every reel and every brand. generate_audio.py, compile.py, remotion_scenes.py — not one per channel, one for all of them. The skill says what. The script does exactly. And there is only one script to debug.', kind: 'claim', calloutIndex: 2, sparkLine: 'One belt.' },
  { id: 'B05', narration: 'The honest self-own: generate_audio.py exists twice in this repo. The fork happened when a new brand needed tweaks and someone copied instead of parameterized. Two scripts means the bug lives in both. One fix lands in one. The other runs wrong for weeks.', kind: 'claim', calloutIndex: 3, sparkLine: 'Forks breed bugs.' },
  { id: 'B06', narration: 'The law: reuse before you write. If a script exists that does the thing — call it. If it almost does the thing — parameterize it. Write new code only when neither works. Writing is the last resort, not the first move.', kind: 'claim', calloutIndex: 4, sparkLine: 'Reuse before you write.' },
  { id: 'B07', narration: 'Script or prompt — one page. Two runs must agree: script. Two runs may differ: prompt. Pay the rewrite tax once to write it, never again to call it. One belt, shared across all brands. Reuse before you write. Parameterize before you copy. Write only when neither works.', kind: 'verdict' },
  { id: 'B08', narration: 'If this saves you a debugging session, subscribe. Nik Bear Brown.', kind: 'outro' },
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

const CodeBeat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9' }}>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <ClaudeWindow {...claudeWindowSchema.parse({ view: 'blank', width: 860, height: 540, fontSize: 15 })} />
    </AbsoluteFill>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <CodeBlock {...codeBlockSchema.parse({
        title: 'the belt — one call',
        code: '$ python3 runtime/scripts/generate_audio.py \\\n    youtube/claude-scripted/\n# measures mp3s, calculates frames\n# writes timing json, updates beat_sheet\n# same script · every reel · every brand',
        fontSize: 18,
        width: 740,
        lineDelay: 8,
      })} />
    </AbsoluteFill>
  </AbsoluteFill>
);

const UsageBeat: React.FC<{ upTo: number; sparkLine: string }> = ({ upTo, sparkLine }) => {
  const settled = upTo > 0 ? ITEMS.slice(0, upTo).map((it) => ({ ...it })) : [];
  const active = [{ ...ITEMS[upTo] }];
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
      <ClaudeCallout {...claudeCalloutSchema.parse({ items: active, delay: 8, increment: 0, titleSize: 26, bodySize: 17, maxWidth: 260 })} />
    </AbsoluteFill>
  );
};

const VerdictBeat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9', alignItems: 'center', justifyContent: 'center' }}>
    <ClaudeWindow {...claudeWindowSchema.parse({
      view: 'artifact', width: 900, height: 560, fontSize: 17,
      artifactTitle: 'Script or prompt? — one page',
      artifactHeading: 'The decision rule',
      artifactLines: [
        'Two runs must agree → script. Two runs may differ → prompt.',
        'The rewrite tax: re-deriving exact logic costs tokens and drift every run.',
        'One belt: one script per operation, shared across all brands and reels.',
        'Forks breed bugs: copy instead of parameterize and you own two broken scripts.',
        'Reuse before you write. Parameterize before you copy. Write only when neither works.',
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
        Claude, scripted<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@HumanitariansAI</div>
      <div style={{ fontFamily: SANS, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · reuse before you write</div>
    </AbsoluteFill>
  );
};

export const ClaudeScripted: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ask') content = (
      <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
        greeting: 'Habari, Bear',
        topic: 'COWORK · SCRIPTS',
        segment: 'Claude, Scripted',
        command: COMMAND,
        runningText: 'checking the belt…',
      })} />
    );
    else if (b.kind === 'code') content = <CodeBeat />;
    else if (b.kind === 'claim') content = <UsageBeat upTo={b.calloutIndex!} sparkLine={b.sparkLine!} />;
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
