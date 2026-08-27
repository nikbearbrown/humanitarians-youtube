import React from 'react';
import {AbsoluteFill} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {SparkLine, STAGE, clamp, remap, ease, useP} from '../illustrations/kit';

/**
 * GemmaConvergenceThread — the reframe beat for gemma4-unified.
 *
 * Two things get called "architectures converging" and they are not the same
 * claim. This exhibit separates them and puts Gemma 4 on the correct side:
 *
 *   LEFT   encoder convergence — perception folds into the decoder. Gemma 4 12B
 *          is an instance (FACTCHECK #27).
 *   RIGHT  understanding/generation convergence — one stack both makes and
 *          judges. Gemma 4 is NOT an instance: it emits text only, no image
 *          head (FACTCHECK #23, #26).
 *
 * The model names on the right are pointers only — the reel makes no
 * performance claim about any of them (FACTCHECK #28).
 */

export const gemmaConvergenceThreadSchema = z.object({
  sparkLine: z.string().default('Two different convergences.'),
});
export type GemmaConvergenceThreadProps = z.infer<typeof gemmaConvergenceThreadSchema>;

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const MONO = CLAUDE_FONT.mono;

// Columns are shortened so the footer clears the title-safe bottom (y=1026 +7px
// margin in runtime/qc/final_frame_check.py) — the earlier 560px column pushed
// the last footer line to a 1024 baseline, i.e. descenders on the edge.
const COL_Y = 244;
const COL_H = 540;
const L_X = 112;
const R_X = 988;
const COL_W = 820;

const UNIFIED_MODELS = ['Chameleon', 'Emu3', 'Show-o', 'Transfusion', 'Janus', 'BAGEL'];

export const GemmaConvergenceThread: React.FC<GemmaConvergenceThreadProps> = ({sparkLine}) => {
  const p = useP();
  const head = ease(remap(p, 0.02, 0.13, 0, 1));
  const left = ease(remap(p, 0.08, 0.28, 0, 1));
  const right = ease(remap(p, 0.24, 0.46, 0, 1));
  const chips = (i: number) => ease(remap(p, 0.34 + i * 0.045, 0.5 + i * 0.045, 0, 1));
  const foot = ease(remap(p, 0.66, 0.9, 0, 1));

  return (
    <AbsoluteFill style={{background: STAGE, overflow: 'hidden'}}>
      <svg width={1920} height={1080} style={{position: 'absolute', inset: 0}}>
        <g opacity={head}>
          <text x={L_X} y={166} fontFamily={SANS} fontSize={28} fontWeight={700} fill={CLAUDE.SPARK} letterSpacing={3}>
            TWO CLAIMS THAT KEEP GETTING CONFLATED
          </text>
          <text x={L_X} y={218} fontFamily={SERIF} fontSize={52} fontWeight={700} fill={CLAUDE.INK}>
            “Architectures are converging” — which convergence?
          </text>
        </g>

        {/* ---------- LEFT: encoder convergence (this reel) ---------- */}
        <g opacity={left}>
          <rect
            x={L_X}
            y={COL_Y}
            width={COL_W}
            height={COL_H}
            rx={22}
            fill={CLAUDE.CARD}
            stroke={CLAUDE.SPARK}
            strokeWidth={5}
          />
          <rect x={L_X} y={COL_Y} width={COL_W} height={78} rx={22} fill={CLAUDE.SPARK} />
          <text x={L_X + 36} y={COL_Y + 54} fontFamily={SANS} fontSize={32} fontWeight={700} fill="#FFFFFF" letterSpacing={2}>
            ENCODER CONVERGENCE
          </text>
          <text x={L_X + 36} y={COL_Y + 156} fontFamily={SERIF} fontSize={44} fontWeight={700} fill={CLAUDE.INK}>
            Perception folds into the decoder
          </text>
          <text x={L_X + 36} y={COL_Y + 214} fontFamily={SANS} fontSize={31} fill={CLAUDE.INK_SOFT}>
            Modality-specific front-ends get deleted;
          </text>
          <text x={L_X + 36} y={COL_Y + 256} fontFamily={SANS} fontSize={31} fill={CLAUDE.INK_SOFT}>
            the general stack absorbs the job.
          </text>

          <rect x={L_X + 36} y={COL_Y + 300} width={COL_W - 72} height={96} rx={14} fill={CLAUDE.FOOTER} />
          <text x={L_X + 60} y={COL_Y + 340} fontFamily={MONO} fontSize={27} fill={CLAUDE.INK}>
            550M ViT → 35M matmul
          </text>
          <text x={L_X + 60} y={COL_Y + 378} fontFamily={MONO} fontSize={27} fill={CLAUDE.INK}>
            305M Conformer → nothing
          </text>

          <text x={L_X + 36} y={COL_Y + 470} fontFamily={SANS} fontSize={30} fontWeight={700} fill={CLAUDE.INK}>
            Gemma 4 12B: yes, this is the one.
          </text>
          <text x={L_X + 36} y={COL_Y + 516} fontFamily={SANS} fontSize={27} fill={CLAUDE.INK_SOFT}>
            …and still unproven at matched size.
          </text>
        </g>

        {/* ---------- RIGHT: generation/understanding convergence ---------- */}
        <g opacity={right}>
          <rect
            x={R_X}
            y={COL_Y}
            width={COL_W}
            height={COL_H}
            rx={22}
            fill={CLAUDE.CARD}
            stroke={CLAUDE.BORDER}
            strokeWidth={4}
          />
          <rect x={R_X} y={COL_Y} width={COL_W} height={78} rx={22} fill={CLAUDE.INK} />
          <text x={R_X + 36} y={COL_Y + 54} fontFamily={SANS} fontSize={32} fontWeight={700} fill="#FFFFFF" letterSpacing={2}>
            GENERATOR ↔ DISCRIMINATOR
          </text>
          <text x={R_X + 36} y={COL_Y + 156} fontFamily={SERIF} fontSize={44} fontWeight={700} fill={CLAUDE.INK}>
            One stack makes and judges
          </text>
          <text x={R_X + 36} y={COL_Y + 214} fontFamily={SANS} fontSize={31} fill={CLAUDE.INK_SOFT}>
            Where that work actually lives:
          </text>
          {/* These six are pointers, not endorsements — the reel makes no
              performance claim about any of them. One citation anchors the set. */}
          <text x={R_X + 36} y={COL_Y + 430} fontFamily={MONO} fontSize={24} fill={CLAUDE.GHOST}>
            pointers only · Show-o arXiv:2408.12528
          </text>

          {UNIFIED_MODELS.map((m, i) => {
            const cx = R_X + 40 + (i % 3) * 250;
            const cy = COL_Y + 250 + Math.floor(i / 3) * 88;
            return (
              <g key={m} opacity={chips(i)}>
                <rect x={cx} y={cy} width={228} height={68} rx={12} fill={CLAUDE.PILL} />
                <text
                  x={cx + 114}
                  y={cy + 45}
                  textAnchor="middle"
                  fontFamily={SANS}
                  fontSize={30}
                  fontWeight={700}
                  fill={CLAUDE.INK}
                >
                  {m}
                </text>
              </g>
            );
          })}

          <text x={R_X + 36} y={COL_Y + 470} fontFamily={SANS} fontSize={30} fontWeight={700} fill={CLAUDE.INK}>
            Gemma 4: not this one.
          </text>
          <text x={R_X + 36} y={COL_Y + 516} fontFamily={SANS} fontSize={27} fill={CLAUDE.INK_SOFT}>
            any modality in → text only out. No image head.
          </text>
        </g>

        {/* ---------- footer: the idea underneath, and its caveat ---------- */}
        <g opacity={foot}>
          <line x1={L_X} y1={830} x2={1808} y2={830} stroke={CLAUDE.BORDER} strokeWidth={3} />
          <text x={L_X} y={886} fontFamily={SERIF} fontSize={46} fontWeight={700} fill={CLAUDE.INK}>
            Underneath both: the Platonic Representation Hypothesis
          </text>
          {/* Both halves of this claim carry their citation on the same line as the
              claim — the hypothesis AND the rebuttal. Asserting "contested" without
              showing who contests it would fail this reel's own standard. */}
          <text x={1808} y={886} textAnchor="end" fontFamily={MONO} fontSize={26} fill={CLAUDE.INK_SOFT}>
            arXiv:2405.07987
          </text>
          <text x={L_X} y={938} fontFamily={SANS} fontSize={31} fill={CLAUDE.INK_SOFT}>
            different architectures drifting toward the same internal geometry —
          </text>
          <text x={L_X} y={990} fontFamily={SANS} fontSize={31} fill={CLAUDE.SPARK} fontWeight={700}>
            and contested: similarity metrics inflate with scale.
          </text>
          <text x={1808} y={990} textAnchor="end" fontFamily={MONO} fontSize={26} fill={CLAUDE.INK_SOFT}>
            arXiv:2604.18572
          </text>
        </g>
      </svg>

      <SparkLine text={sparkLine} pos="top" />
    </AbsoluteFill>
  );
};
