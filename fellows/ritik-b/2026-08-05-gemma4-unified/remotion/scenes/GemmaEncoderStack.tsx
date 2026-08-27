import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {SparkLine, STAGE, clamp, remap, ease, useP} from '../illustrations/kit';

/**
 * GemmaEncoderStack — the exhibit for the gemma4-unified reel.
 *
 * Three input lanes (image / audio / text) feed a decoder slab. Each lane
 * carries the perception module that used to sit in front of the decoder, and
 * the focus states walk through what Gemma 4 12B deleted:
 *
 *   focus="specialists"  the pre-2026 regime, and Gemma 4's April four —
 *                        150M/550M ViT + 305M USM Conformer, frozen, bolted on
 *   focus="vision"       the 550M vision encoder collapses to a 35M matmul
 *   focus="audio"        the 305M audio encoder is removed outright
 *
 * COLOR GRAMMAR (see beat_sheet metadata.color_semantics): terracotta marks the
 * component under the knife in THIS beat. Everything surviving stays warm ink.
 * Numbers are from FACTCHECK.md #8/#9/#12/#14 (arXiv:2607.02770).
 */

export const gemmaEncoderStackSchema = z.object({
  sparkLine: z.string().default('Three specialists, bolted on.'),
  focus: z.enum(['specialists', 'vision', 'audio']).default('specialists'),
  /** Citation shown at the moment these figures are asserted. Every number on
   *  this exhibit (150M/550M ViT, 305M Conformer, 35M matmul, 48×48×3, 262k) comes
   *  from one place, so one visible source covers the beat. A reel that preaches
   *  "no source, no verdict" has to carry its own receipt on screen. */
  sourceNote: z.string().default('arXiv:2607.02770 · Gemma 4 Technical Report'),
});
export type GemmaEncoderStackProps = z.infer<typeof gemmaEncoderStackSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CLAUDE_FONT.mono;

// Lane geometry. Deliberately wide — the canvas-fill law wants the exhibit to
// own the frame, not float in the middle of it.
const LANE_Y = [332, 566, 800];
const IN_X = 132;
const IN_W = 300;
const BOX_X = 476;
const BOX_W = 556;
const DEC_X = 1214;
const DEC_W = 574;
const DEC_Y = 258;
const DEC_H = 616;

type Lane = {
  key: 'vision' | 'audio' | 'text';
  input: string;
  inputSub: string;
  name: string;
  size: string;
  note: string;
};

const LANES: Lane[] = [
  {
    key: 'vision',
    input: 'IMAGE',
    inputSub: '48×48×3 patches',
    name: 'Vision Transformer',
    size: '550M',
    note: 'frozen encoder',
  },
  {
    key: 'audio',
    input: 'AUDIO',
    inputSub: '16 kHz · 40 ms frames',
    name: 'USM Conformer',
    size: '305M',
    note: 'frozen encoder',
  },
  {
    key: 'text',
    input: 'TEXT',
    inputSub: '262k vocabulary',
    name: 'SentencePiece',
    size: '', // no parameter count to quote — and a bare dash reads as a minus sign
    note: 'tokenizer — no encoder needed',
  },
];

/** Arrow from the module column into the decoder slab. */
const Feed: React.FC<{y: number; o: number; dashed?: boolean; color: string}> = ({
  y,
  o,
  dashed,
  color,
}) => {
  const x0 = BOX_X + BOX_W + 16;
  const x1 = DEC_X - 14;
  return (
    <g opacity={o}>
      <line
        x1={x0}
        y1={y}
        x2={x1 - 16}
        y2={y}
        stroke={color}
        strokeWidth={4}
        strokeDasharray={dashed ? '12 10' : undefined}
      />
      <polygon points={`${x1},${y} ${x1 - 18},${y - 10} ${x1 - 18},${y + 10}`} fill={color} />
    </g>
  );
};

export const GemmaEncoderStack: React.FC<GemmaEncoderStackProps> = ({sparkLine, focus, sourceNote}) => {
  const p = useP();

  // Staged reveal: header → lanes → decoder → the focus event.
  const head = ease(remap(p, 0.02, 0.14, 0, 1));
  const laneIn = (i: number) => ease(remap(p, 0.1 + i * 0.07, 0.3 + i * 0.07, 0, 1));
  const decIn = ease(remap(p, 0.2, 0.4, 0, 1));
  // The deletion lands late enough that the viewer has read the before-state.
  const cut = ease(remap(p, 0.46, 0.74, 0, 1));

  const eyebrow =
    focus === 'specialists'
      ? 'GEMMA 4 · APRIL 2026 · FOUR MODELS'
      : 'GEMMA 4 12B · JUNE 2026 · UNIFIED';
  const headline =
    focus === 'specialists'
      ? 'Perception is a separate machine'
      : focus === 'vision'
        ? 'The eyes become one matrix multiply'
        : 'The ears are removed entirely';

  return (
    <AbsoluteFill style={{background: STAGE, overflow: 'hidden'}}>
      <svg width={1920} height={1080} style={{position: 'absolute', inset: 0}}>
        {/* ---------- decoder slab ---------- */}
        <g opacity={decIn}>
          <rect
            x={DEC_X}
            y={DEC_Y}
            width={DEC_W}
            height={DEC_H}
            rx={22}
            fill={CLAUDE.CARD}
            stroke={CLAUDE.INK}
            strokeWidth={4}
          />
          <text
            x={DEC_X + DEC_W / 2}
            y={DEC_Y + 88}
            textAnchor="middle"
            fontFamily={SERIF}
            fontSize={54}
            fontWeight={700}
            fill={CLAUDE.INK}
          >
            Decoder
          </text>
          <text
            x={DEC_X + DEC_W / 2}
            y={DEC_Y + 140}
            textAnchor="middle"
            fontFamily={SANS}
            fontSize={30}
            fill={CLAUDE.INK_SOFT}
          >
            decoder-only Transformer
          </text>
          {/* the embedding space every lane lands in */}
          <rect
            x={DEC_X + 46}
            y={DEC_Y + 196}
            width={DEC_W - 92}
            height={128}
            rx={14}
            fill={CLAUDE.PILL}
          />
          <text
            x={DEC_X + DEC_W / 2}
            y={DEC_Y + 250}
            textAnchor="middle"
            fontFamily={SANS}
            fontSize={30}
            fontWeight={700}
            fill={CLAUDE.INK}
          >
            one embedding space
          </text>
          <text
            x={DEC_X + DEC_W / 2}
            y={DEC_Y + 292}
            textAnchor="middle"
            fontFamily={MONO}
            fontSize={26}
            fill={CLAUDE.INK_SOFT}
          >
            text · image · audio
          </text>
          <text
            x={DEC_X + DEC_W / 2}
            y={DEC_Y + 424}
            textAnchor="middle"
            fontFamily={SANS}
            fontSize={32}
            fill={CLAUDE.INK}
          >
            output: text only
          </text>
          <text
            x={DEC_X + DEC_W / 2}
            y={DEC_Y + 476}
            textAnchor="middle"
            fontFamily={SANS}
            fontSize={26}
            fill={CLAUDE.GHOST}
          >
            no image head · no audio head
          </text>
        </g>

        {/* ---------- lanes ---------- */}
        {LANES.map((lane, i) => {
          const y = LANE_Y[i];
          const o = laneIn(i);
          const targeted =
            (focus === 'vision' && lane.key === 'vision') ||
            (focus === 'audio' && lane.key === 'audio');
          // Already-deleted lanes stay deleted: by the audio beat the vision
          // encoder is gone too, so the exhibit accumulates rather than resets.
          const alreadyGone = focus === 'audio' && lane.key === 'vision';
          const accent = targeted ? CLAUDE.SPARK : CLAUDE.INK;

          // How far this lane's box has been struck through / hollowed out.
          // k = how far this lane's module has been cut. removed = how far the box
          // itself hollows out to a dashed ghost (audio only — vision keeps a box
          // because something, the 35M matmul, still lives there).
          const k = targeted ? cut : alreadyGone ? 1 : 0;
          const removed = targeted && focus === 'audio' ? cut : 0;

          return (
            <g key={lane.key} opacity={o}>
              {/* input chip */}
              <rect
                x={IN_X}
                y={y - 62}
                width={IN_W}
                height={124}
                rx={16}
                fill={CLAUDE.FOOTER}
                stroke={CLAUDE.BORDER}
                strokeWidth={3}
              />
              <text
                x={IN_X + IN_W / 2}
                y={y - 12}
                textAnchor="middle"
                fontFamily={SANS}
                fontSize={34}
                fontWeight={700}
                fill={CLAUDE.INK}
                letterSpacing={2}
              >
                {lane.input}
              </text>
              <text
                x={IN_X + IN_W / 2}
                y={y + 32}
                textAnchor="middle"
                fontFamily={MONO}
                fontSize={24}
                fill={CLAUDE.INK_SOFT}
              >
                {lane.inputSub}
              </text>

              {/* input → module */}
              <line
                x1={IN_X + IN_W + 14}
                y1={y}
                x2={BOX_X - 22}
                y2={y}
                stroke={CLAUDE.INK_SOFT}
                strokeWidth={4}
              />
              <polygon
                points={`${BOX_X - 6},${y} ${BOX_X - 24},${y - 10} ${BOX_X - 24},${y + 10}`}
                fill={CLAUDE.INK_SOFT}
              />

              {/* ---- the module box ---- */}
              {/* audio deletion: the box empties into a dashed ghost */}
              <rect
                x={BOX_X}
                y={y - 74}
                width={BOX_W}
                height={148}
                rx={18}
                fill={removed > 0.5 ? 'none' : CLAUDE.CARD}
                fillOpacity={clamp(1 - removed * 1.4, 0, 1)}
                stroke={accent}
                strokeWidth={4}
                strokeDasharray={removed > 0.5 ? '14 12' : undefined}
                opacity={clamp(1 - removed * 0.55, 0, 1)}
              />

              {/* module name + size, faded out as it is cut */}
              {/* Name/note live in the left ~320px and the size is right-aligned in
                  its own reserved zone. At 36/58px the long names ("Vision
                  Transformer") ran straight into the number. */}
              <g opacity={clamp(1 - k * 1.25, 0, 1)}>
                <text
                  x={BOX_X + 34}
                  y={y - 18}
                  fontFamily={SANS}
                  fontSize={34}
                  fontWeight={700}
                  fill={CLAUDE.INK}
                >
                  {lane.name}
                </text>
                <text x={BOX_X + 34} y={y + 28} fontFamily={SANS} fontSize={27} fill={CLAUDE.INK_SOFT}>
                  {lane.note}
                </text>
                <text
                  x={BOX_X + BOX_W - 30}
                  y={y + 16}
                  textAnchor="end"
                  fontFamily={SERIF}
                  fontSize={52}
                  fontWeight={700}
                  fill={CLAUDE.INK}
                >
                  {lane.size}
                </text>
              </g>

              {/* Strike-through only on the component being cut in THIS beat, and
                  only while it is being cut: it fades as the replacement label
                  arrives, so we never draw a line through the words "no encoder"
                  (which reads as the opposite of what it means). A lane that was
                  already cut in an earlier beat shows its replacement, not a line. */}
              {targeted && (
                <line
                  x1={BOX_X + 20}
                  y1={y}
                  x2={BOX_X + 20 + (BOX_W - 40) * k}
                  y2={y}
                  stroke={CLAUDE.SPARK}
                  strokeWidth={7}
                  strokeLinecap="round"
                  opacity={clamp(remap(k, 0.62, 0.95, 1, 0), 0, 1)}
                />
              )}

              {/* carried-forward context for a lane cut in an earlier beat */}
              {alreadyGone && (
                <text
                  x={BOX_X + 34}
                  y={y + 12}
                  fontFamily={SANS}
                  fontSize={28}
                  fill={CLAUDE.GHOST}
                >
                  was 550M
                </text>
              )}

              {/* vision replacement: the 35M matmul chip */}
              {lane.key === 'vision' && (focus === 'vision' || alreadyGone) && (
                <g opacity={focus === 'vision' ? clamp(remap(cut, 0.55, 1, 0, 1), 0, 1) : 1}>
                  <rect
                    x={BOX_X + BOX_W - 250}
                    y={y - 46}
                    width={228}
                    height={92}
                    rx={14}
                    fill={CLAUDE.SPARK}
                  />
                  <text
                    x={BOX_X + BOX_W - 136}
                    y={y - 8}
                    textAnchor="middle"
                    fontFamily={SERIF}
                    fontSize={44}
                    fontWeight={700}
                    fill="#FFFFFF"
                  >
                    35M
                  </text>
                  <text
                    x={BOX_X + BOX_W - 136}
                    y={y + 28}
                    textAnchor="middle"
                    fontFamily={SANS}
                    fontSize={24}
                    fill="#FFFFFF"
                  >
                    one matmul
                  </text>
                </g>
              )}

              {/* audio replacement: nothing at all */}
              {lane.key === 'audio' && focus === 'audio' && (
                <text
                  x={BOX_X + BOX_W / 2}
                  y={y + 14}
                  textAnchor="middle"
                  fontFamily={SERIF}
                  fontSize={46}
                  fontWeight={700}
                  fill={CLAUDE.SPARK}
                  opacity={clamp(remap(cut, 0.55, 1, 0, 1), 0, 1)}
                >
                  no encoder
                </text>
              )}

              <Feed
                y={y}
                o={decIn}
                dashed={lane.key === 'audio' && focus === 'audio' && cut > 0.5}
                color={targeted ? CLAUDE.SPARK : CLAUDE.INK_SOFT}
              />
            </g>
          );
        })}

        {/* ---------- header ---------- */}
        <g opacity={head}>
          <text
            x={IN_X}
            y={188}
            fontFamily={SANS}
            fontSize={28}
            fontWeight={700}
            fill={CLAUDE.SPARK}
            letterSpacing={3}
          >
            {eyebrow}
          </text>
          <text x={IN_X} y={248} fontFamily={SERIF} fontSize={56} fontWeight={700} fill={CLAUDE.INK}>
            {headline}
          </text>
          {/* Source, top-right on the header line — the bottom of this exhibit is
              already occupied by the 550M→35M / 305M→0 count. */}
          {sourceNote ? (
            <text
              x={1788}
              y={188}
              textAnchor="end"
              fontFamily={MONO}
              fontSize={26}
              fill={CLAUDE.INK_SOFT}
            >
              {sourceNote}
            </text>
          ) : null}
        </g>

        {/* ---------- footer: the count that carries the argument ---------- */}
        {focus !== 'specialists' && (
          <g opacity={clamp(remap(cut, 0.6, 1, 0, 1), 0, 1)}>
            <line x1={IN_X} y1={922} x2={1788} y2={922} stroke={CLAUDE.BORDER} strokeWidth={3} />
            <text x={IN_X} y={986} fontFamily={SERIF} fontSize={44} fontWeight={700} fill={CLAUDE.INK}>
              {focus === 'vision'
                ? '550M → 35M — 94% of the vision front-end, gone'
                : '305M → 0 — the audio encoder is not replaced'}
            </text>
          </g>
        )}
      </svg>

      <SparkLine text={sparkLine} pos="top" />
    </AbsoluteFill>
  );
};
