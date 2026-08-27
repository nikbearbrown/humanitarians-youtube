import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {SparkLine, STAGE, clamp, remap, ease, useP} from '../illustrations/kit';

/**
 * GemmaScoreboard — the evidence exhibit for gemma4-unified.
 *
 *   focus="split"     the two benchmark families disagree: the encoder-free 12B
 *                     loses on MMMU-Pro and wins on FLEURS ASR
 *   focus="confound"  the same bars, annotated with parameter counts — every
 *                     comparison moves size AND architecture, and the technical
 *                     report never runs the matched-size ablation
 *
 * Numbers: FACTCHECK.md #17 (TR Table 6) and #18 (TR Tables 7–8). The confound
 * reading is FACTCHECK #21, logged there as ARGUMENT, not as a finding.
 */

export const gemmaScoreboardSchema = z.object({
  sparkLine: z.string().default('Worse at seeing. Better at hearing.'),
  focus: z.enum(['split', 'confound']).default('split'),
});
export type GemmaScoreboardProps = z.infer<typeof gemmaScoreboardSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CLAUDE_FONT.mono;

type Row = {label: string; params: string; value: number; free?: boolean};

const VISION: Row[] = [
  {label: '12B unified', params: '12B params', value: 69.1, free: true},
  {label: '26B-A4B', params: '26B params', value: 73.8},
  {label: '31B dense', params: '31B params', value: 76.9},
];
const AUDIO: Row[] = [
  {label: '12B unified', params: '12B params', value: 0.067, free: true},
  {label: 'E4B', params: '4.5B params', value: 0.075},
  {label: 'E2B', params: '2.3B params', value: 0.090},
];

const PANEL_Y = 236;
const PANEL_H = 636;
// Rows pulled up and tightened so the third row's parameter label (drawn 50px
// below its baseline in the confound state) clears the verdict strip. At
// [430,574,718] the "31B params" / "2.3B params" chips were sliced in half by it.
const ROW_Y = [428, 560, 692];
const BAR_H = 74;
const PARAM_DY = 50;
const VERDICT_DY = 96; // strip top, measured up from the panel bottom

const Panel: React.FC<{
  x: number;
  w: number;
  title: string;
  metric: string;
  better: string;
  rows: Row[];
  max: number;
  fmt: (v: number) => string;
  verdict: string;
  o: number;
  grow: number;
  confound: number;
}> = ({x, w, title, metric, better, rows, max, fmt, verdict, o, grow, confound}) => {
  const barX = x + 250;
  // 210px reserved on the right for the value label — at 190 the three-decimal
  // WER figures ("0.067") ran within 24px of the panel edge and read as clipped.
  const barMax = w - 250 - 210;
  return (
    <g opacity={o}>
      <rect
        x={x}
        y={PANEL_Y}
        width={w}
        height={PANEL_H}
        rx={22}
        fill={CLAUDE.CARD}
        stroke={CLAUDE.BORDER}
        strokeWidth={3}
      />
      <text x={x + 40} y={PANEL_Y + 74} fontFamily={SERIF} fontSize={50} fontWeight={700} fill={CLAUDE.INK}>
        {title}
      </text>
      <text x={x + 40} y={PANEL_Y + 122} fontFamily={SANS} fontSize={28} fill={CLAUDE.INK_SOFT}>
        {metric} · {better}
      </text>

      {rows.map((r, i) => {
        const y = ROW_Y[i];
        const wBar = Math.max(6, (r.value / max) * barMax * grow);
        const fill = r.free ? CLAUDE.SPARK : CLAUDE.INK;
        return (
          <g key={r.label}>
            <text
              x={x + 40}
              y={y + 12}
              fontFamily={SANS}
              fontSize={34}
              fontWeight={r.free ? 700 : 400}
              fill={CLAUDE.INK}
            >
              {r.label}
            </text>
            {/* parameter count only appears in the confound state — it is the
                second variable the benchmark tables quietly move */}
            <text
              x={x + 40}
              y={y + PARAM_DY}
              fontFamily={MONO}
              fontSize={26}
              fill={CLAUDE.SPARK}
              opacity={confound}
            >
              {r.params}
            </text>
            <rect x={barX} y={y - BAR_H / 2} width={barMax} height={BAR_H} rx={10} fill={CLAUDE.PILL} />
            <rect x={barX} y={y - BAR_H / 2} width={wBar} height={BAR_H} rx={10} fill={fill} />
            <text
              x={barX + barMax + 26}
              y={y + 16}
              fontFamily={SERIF}
              fontSize={46}
              fontWeight={700}
              fill={CLAUDE.INK}
            >
              {fmt(r.value)}
            </text>
          </g>
        );
      })}

      {/* the encoder-free verdict for this metric family */}
      <g opacity={clamp(remap(grow, 0.7, 1, 0, 1), 0, 1)}>
        <rect
          x={x + 40}
          y={PANEL_Y + PANEL_H - VERDICT_DY}
          width={w - 80}
          height={72}
          rx={14}
          fill={CLAUDE.FOOTER}
        />
        <text
          x={x + w / 2}
          y={PANEL_Y + PANEL_H - VERDICT_DY + 48}
          textAnchor="middle"
          fontFamily={SANS}
          fontSize={32}
          fontWeight={700}
          fill={CLAUDE.INK}
        >
          {verdict}
        </text>
      </g>
    </g>
  );
};

export const GemmaScoreboard: React.FC<GemmaScoreboardProps> = ({sparkLine, focus}) => {
  const p = useP();
  const head = ease(remap(p, 0.02, 0.14, 0, 1));
  const left = ease(remap(p, 0.08, 0.3, 0, 1));
  const right = ease(remap(p, 0.2, 0.44, 0, 1));
  const grow = ease(remap(p, 0.16, 0.6, 0, 1));
  const conf = focus === 'confound' ? ease(remap(p, 0.3, 0.62, 0, 1)) : 0;
  const banner = focus === 'confound' ? ease(remap(p, 0.6, 0.86, 0, 1)) : 0;

  return (
    <AbsoluteFill style={{background: STAGE, overflow: 'hidden'}}>
      <svg width={1920} height={1080} style={{position: 'absolute', inset: 0}}>
        <g opacity={head}>
          <text x={112} y={178} fontFamily={SANS} fontSize={28} fontWeight={700} fill={CLAUDE.SPARK} letterSpacing={3}>
            {focus === 'split' ? 'GEMMA 4 TECHNICAL REPORT · TABLES 6–8' : 'THE COMPARISON MOVES TWO VARIABLES'}
          </text>
          <text x={112} y={212} fontFamily={SERIF} fontSize={30} fill={CLAUDE.INK_SOFT}>
            {focus === 'split'
              ? 'encoder-free 12B in terracotta'
              : 'architecture and parameter count change together — every row'}
          </text>
        </g>

        <Panel
          x={112}
          w={820}
          title="Seeing"
          metric="MMMU-Pro"
          better="higher is better"
          rows={VISION}
          max={80}
          fmt={(v) => v.toFixed(1)}
          verdict="encoder-free LOSES by 7.8"
          o={left}
          grow={grow}
          confound={conf}
        />
        <Panel
          x={988}
          w={820}
          title="Hearing"
          metric="FLEURS ASR · word error rate"
          better="lower is better"
          rows={AUDIO}
          max={0.1}
          fmt={(v) => v.toFixed(3)}
          verdict="encoder-free WINS by 0.008"
          o={right}
          grow={grow}
          confound={conf}
        />

        {/* The split state's own bottom line. Not padding: it states the
            contradiction the beat exists to set up, and it keeps the lower fifth
            of the frame from sitting empty (canvas-fill law). Deliberately
            quieter than the confound banner so B06 still escalates. */}
        {focus === 'split' && (
          <g opacity={clamp(remap(grow, 0.8, 1, 0, 1), 0, 1)}>
            <line x1={112} y1={912} x2={1808} y2={912} stroke={CLAUDE.BORDER} strokeWidth={3} />
            <text x={960} y={972} textAnchor="middle" fontFamily={SERIF} fontSize={46} fontWeight={700} fill={CLAUDE.INK}>
              Same report, same model — opposite answers
            </text>
          </g>
        )}

        {/* the missing experiment */}
        {focus === 'confound' && (
          <g opacity={banner}>
            <rect x={112} y={912} width={1696} height={104} rx={16} fill={CLAUDE.SPARK} />
            <text
              x={960}
              y={956}
              textAnchor="middle"
              fontFamily={SERIF}
              fontSize={44}
              fontWeight={700}
              fill="#FFFFFF"
            >
              No experiment holds size fixed and toggles the encoder
            </text>
            <text x={960} y={996} textAnchor="middle" fontFamily={SANS} fontSize={27} fill="#FFFFFF">
              the 12B is benchmarked against Gemma 3 — not against its own siblings
            </text>
          </g>
        )}
      </svg>

      <SparkLine text={sparkLine} pos="top" />
    </AbsoluteFill>
  );
};
