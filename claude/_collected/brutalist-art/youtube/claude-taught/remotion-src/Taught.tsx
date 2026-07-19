import React from 'react';
import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate } from 'remotion';
import TIMING from './taught_timing.json';
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
const COMMAND = '/skill-creator teach claude my way of making videos';

// Callouts in ACCUMULATION order (B02..B06), pointing at composer window elements.
const ITEMS = [
  { title: 'the influence half', body: 'register, pickWhen, taste —\njudgment written once\nso runners never guess.', x: 0.22, y: 0.42, targetX: 0.49, targetY: 0.242, bend: 0.2, delay: 0 },
  { title: 'the specify half', body: 'file contracts, gates, laws.\nexact enough to run\nwithout asking anything.', x: 0.78, y: 0.66, targetX: 0.688, targetY: 0.632, bend: -0.15, delay: 0 },
  { title: 'authored once', body: 'Fable writes it once.\nOpus runs it forever.\nquality freezes in.', x: 0.78, y: 0.2, targetX: 0.548, targetY: 0.242, bend: -0.2, delay: 0 },
  { title: 'the vague skill', body: '"match my tone."\n"be thorough." —\nthe runner improvises.', x: 0.78, y: 0.42, targetX: 0.56, targetY: 0.52, bend: -0.2, delay: 0 },
  { title: 'author high, run low', body: 'the expensive part:\nthe authoring.\nthe cheap part: forever.', x: 0.22, y: 0.2, targetX: 0.34, targetY: 0.52, bend: 0.15, delay: 0 },
];

type Beat = { id: string; narration: string; kind: string; calloutIndex?: number; sparkLine?: string };
export const BEATS: Beat[] = [
  { id: 'B00', narration: 'You just found the file that runs this whole channel. One playbook that knows my register, my gates, my file layouts. Write it once, hand it to any model, and the taste is already in the room. What\'s actually in it?', kind: 'ask' },
  { id: 'B01', narration: 'A skill is one file, two halves. The top tells Claude when to load it. The bottom tells Claude what to do once it does. Almost every vague skill I\'ve seen is just the top half — wearing the word skill like a costume.', kind: 'code' },
  { id: 'B02', narration: 'The top half is the influence section. Register — how it sounds. PickWhen — what triggers it. Taste decisions the author locks in once so the runner never has to guess. The runner reads them and sounds like you, without asking.', kind: 'claim', calloutIndex: 0, sparkLine: 'Judgment, frozen.' },
  { id: 'B03', narration: 'The bottom half is the specify section. File contracts — where every output lands. Gates — what must be verified before money is spent. Laws — not suggestions, rules. This half the runner can execute start to finish, no interpretation required.', kind: 'claim', calloutIndex: 1, sparkLine: 'Laws, not vibes.' },
  { id: 'B04', narration: 'Fable authored this skill once. Every reel since has paid down that session — Opus following the laws, filling the gates, landing the files exactly where the contracts say. One authoring session. The quality freezes in at authoring time and every run inherits it.', kind: 'claim', calloutIndex: 2, sparkLine: 'Written once.' },
  { id: 'B05', narration: 'The failure mode looks like a skill but is only vibes. Match my tone. Be thorough. Keep it tight. The runner guesses, the output drifts, and you call it a hallucination. It\'s not. It\'s an empty playbook wearing the word skill.', kind: 'claim', calloutIndex: 3, sparkLine: "Runners don't improvise." },
  { id: 'B06', narration: 'Which is why the authoring model matters. Fable writes the skill — one session where every clause earns its place. Opus runs it, session after session, following the laws. The expensive part was always the authoring. The cheap part is the part that runs forever.', kind: 'claim', calloutIndex: 4, sparkLine: 'Author high, run low.' },
  { id: 'B07', narration: 'The anatomy, one page. The top half: pickWhen and register — the influence. The bottom half: laws and gates — the spec. Write it in Fable. Run it in Opus. The skill is judgment, written down once, so it never has to be improvised again.', kind: 'verdict' },
  { id: 'B08', narration: 'If this explains what a SKILL.md actually does, subscribe. Nik Bear Brown.', kind: 'outro' },
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

// B01 — dark glass Onda code-block on blank ClaudeWindow. Never re-skinned.
const CodeBeat: React.FC = () => (
  <AbsoluteFill style={{ background: '#F2F0E9' }}>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <ClaudeWindow {...claudeWindowSchema.parse({ view: 'blank', width: 860, height: 540, fontSize: 15 })} />
    </AbsoluteFill>
    <AbsoluteFill style={{ alignItems: 'center', justifyContent: 'center' }}>
      <CodeBlock {...codeBlockSchema.parse({
        title: 'SKILL.md — the anatomy',
        code: '---\nname: claude-explainer\npickWhen: user asks for a claude reel\nregister: Teardown\n---\n\n## Laws\n- GATE P before any audio spend\n- Cold open: always ClaudeComposerAsk\n- Spark line on every inner beat\n- Outro restates the episode title',
        fontSize: 18,
        width: 720,
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
      artifactTitle: 'Anatomy of a skill — one page',
      artifactHeading: 'What goes where',
      artifactLines: [
        'pickWhen + register — the influence half. When to load it and how to sound.',
        'Laws — the rules the runner never breaks, no matter what.',
        'Gates — what must pass before any money is spent.',
        'File contracts — where outputs land and what they\'re named.',
        'Author in Fable once. Run in Opus forever. The cheap part is the part that runs.',
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
        Claude, taught<span style={{ color: CLAUDE.SEND }}>.</span>
      </div>
      <div style={{ fontFamily: SERIF, fontSize: 40, color: CLAUDE.INK, marginTop: 30 }}>@NikBearBrown</div>
      <div style={{ fontFamily: SANS, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12 }}>subscribe · judgment, written down</div>
    </AbsoluteFill>
  );
};

export const ClaudeTaught: React.FC = () => {
  let at = 0;
  const seqs = TIMED.map((b) => {
    const from = at;
    at += b.frames;
    let content: React.ReactNode = null;
    if (b.kind === 'ask') content = (
      <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
        greeting: 'Wagwan, Bear',
        topic: 'COWORK · SKILLS',
        segment: 'Claude, Taught',
        command: COMMAND,
        runningText: 'reading the playbook…',
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
