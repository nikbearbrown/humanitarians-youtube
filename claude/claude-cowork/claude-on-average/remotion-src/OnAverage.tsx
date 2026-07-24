import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './on_average_timing.json';
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
const COMMAND = 'why did I get a different answer this time?';

const ITEMS = [
  { title: 'not a database', body: 'same question,\nthree answers,\nall plausible.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'a draw, not a lookup', body: 'next token,\nmost likely\ngiven all context.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
  { title: 'temp-zero steers', body: "frozen ≠ specified.\na persona shifts\nwhat is most likely.", x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'variance is the feature', body: 'creativity lives\nin the tails.\nuse it.', x: 0.22, y: 0.66, targetX: 0.3, targetY: 0.66, bend: 0.15, delay: 0 },
  { title: 'one draw ≠ the answer', body: 'certify with a gate.\nnever trust\na single sample.', x: 0.22, y: 0.2, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
];

type Beat = { id: string; narration: string; kind: string; calloutIndex?: number; sparkLine?: string };
export const BEATS: Beat[] = [
  { id: 'B00', narration: "Every time I ask Claude the same question, I can get a different answer. Sometimes slightly different. Sometimes dramatically different. Same prompt, different draw. That's not a bug. This episode: what that actually means — and why everything else in this series is a consequence of it.", kind: 'ask' },
  { id: 'B01', narration: 'Three runs. Same prompt. Three answers — all plausible, none identical. A database returns one row. Claude returns a draw from a distribution. These are not the same operation.', kind: 'code' },
  { id: 'B02', narration: "The alternative — treating Claude like a lookup — breaks immediately. You ask a question. You get an answer. You run it again. Different answer. You can't cache the right one. There is no right one. There's only the distribution.", kind: 'claim', calloutIndex: 0, sparkLine: 'Not a database.' },
  { id: 'B03', narration: 'What it actually does: next-token prediction. At every step it estimates the most likely continuation of everything before it — the prompt, the system message, everything it has already generated. It\'s not retrieving a stored answer. It\'s generating, token by token, conditioned on all of that.', kind: 'claim', calloutIndex: 1, sparkLine: 'A draw, not a lookup.' },
  { id: 'B04', narration: "Temperature zero makes the most probable token always win. But probable is conditioned on everything in the context. Add a different persona and you shift what's most probable, even at temperature zero. Steering the distribution is not the same as specifying an output. Frozen is not pinned.", kind: 'claim', calloutIndex: 2, sparkLine: 'Temp-zero steers.' },
  { id: 'B05', narration: "This is also why it's useful. The variance is the creativity. You want different takes on the same brief. You want the unexpected riff. The tails of the distribution are where the interesting answers live. You're not sampling noise. You're sampling possibility.", kind: 'claim', calloutIndex: 3, sparkLine: 'Variance is the feature.' },
  { id: 'B06', narration: "And this is what it costs you. One draw is not the answer. One draw is a sample. If exactness matters — if two runs must agree — you don't prompt. You script. You run the gate. Never certify a single draw as truth.", kind: 'claim', calloutIndex: 4, sparkLine: 'One draw is not the answer.' },
  { id: 'B07', narration: "The distribution rules. Same prompt, different draw — that's the definition. Temperature zero steers toward likely; it doesn't specify an exact answer. Variance is the creativity — certify it with a gate, not with faith. Scripts pin the exact. Skills bias the draw. Gates catch the bad draws. The whole system is consequence of one fact: Claude is a distribution.", kind: 'verdict' },
  { id: 'B08', narration: 'If this reframes how you think about prompting, subscribe. Nik Bear Brown.', kind: 'outro' },
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
        title: 'same prompt, three draws',
        code: '$ claude -p "write one line about focus"\n▸ Focus is the art of saying no.\n\n$ claude -p "write one line about focus"\n▸ Attention narrows. That\'s how you get anywhere.\n\n$ claude -p "write one line about focus"\n▸ What you choose not to do is the strategy.',
        fontSize: 17,
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
      artifactTitle: 'The distribution rules — one page',
      artifactHeading: 'What Claude actually is',
      artifactLines: [
        "You're not querying a database. You're sampling a distribution.",
        "Same prompt, different draw — that's not a bug, that's the definition.",
        'Temperature zero steers toward most likely; it does not specify an output.',
        'Variance is the creativity. Certify draws with gates, not with faith.',
        'Scripts pin the exact. Skills bias the draw. Gates catch the bad draws.',
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
        Claude, on average<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@HumanitariansAI</div>
      <div style={{ fontFamily: SANS, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · sample deliberately</div>
    </AbsoluteFill>
  );
};

export const ClaudeOnAverage: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ask') content = (
      <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
        greeting: 'Annyeong, Bear',
        topic: 'COWORK · LLMs',
        segment: 'Claude, On Average',
        command: COMMAND,
        runningText: 'sampling the distribution…',
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
