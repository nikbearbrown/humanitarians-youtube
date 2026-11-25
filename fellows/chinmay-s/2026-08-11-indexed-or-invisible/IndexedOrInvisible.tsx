import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * IndexedOrInvisible — the scene set for the "Indexed or Invisible" deep-explainer
 * (Jobsekr delivery chain: database → exposure → discovery → programmatic → validation).
 *
 * Claude fidelity skin throughout: cream page, warm ink, ONE terracotta accent.
 * Every scene is duration-agnostic — animations settle early and hold, so compile.py
 * can conform each beat to its measured narration length without clipping motion.
 */

const S = CLAUDE_FONT.serif;
const U = CLAUDE_FONT.ui;
const M = CLAUDE_FONT.mono;

// ── shared primitives ───────────────────────────────────────────────────────

export const useRise = (delay = 0, damping = 26) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return spring({ frame: frame - delay, fps, config: { damping, stiffness: 130, mass: 0.8 } });
};

export const Spark: React.FC<{ size?: number }> = ({ size = 16 }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" style={{ flexShrink: 0 }}>
    {Array.from({ length: 8 }, (_, i) => (
      <line key={i} x1={12} y1={12}
        x2={12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}
        y2={12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}
        stroke={CLAUDE.SPARK} strokeWidth={3.2} strokeLinecap="round" />
    ))}
  </svg>
);

export const Eyebrow: React.FC<{ text: string; delay?: number }> = ({ text, delay = 0 }) => {
  const t = useRise(delay);
  return (
    <div style={{
      fontFamily: U, fontSize: 20, fontWeight: 600, letterSpacing: 3.2,
      textTransform: 'uppercase', color: CLAUDE.INK_SOFT,
      opacity: t, transform: `translateY(${(1 - t) * 10}px)`,
    }}>{text}</div>
  );
};

export const SparkLine: React.FC<{ text: string; delay?: number }> = ({ text, delay = 20 }) => {
  const t = useRise(delay);
  if (!text) return null;
  return (
    <div style={{
      position: 'absolute', left: 96, bottom: 64, right: 96,
      display: 'flex', alignItems: 'center', gap: 12,
      opacity: t, transform: `translateY(${(1 - t) * 8}px)`,
    }}>
      <Spark size={18} />
      <span style={{ fontFamily: S, fontStyle: 'italic', fontSize: 27, color: CLAUDE.INK }}>{text}</span>
    </div>
  );
};

export const Page: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <AbsoluteFill style={{ background: CLAUDE.PAGE }}>{children}</AbsoluteFill>
);

export const Card: React.FC<{
  style?: React.CSSProperties; children: React.ReactNode; accent?: boolean;
}> = ({ style, children, accent }) => (
  <div style={{
    background: CLAUDE.CARD,
    border: `1px solid ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
    borderRadius: 14,
    boxShadow: '0 2px 14px rgba(61,57,41,0.05)',
    ...style,
  }}>{children}</div>
);

// ── 1. IdxStatement — the connective-tissue card ────────────────────────────

export const idxStatementSchema = z.object({
  eyebrow: z.string().default(''),
  headline: z.string().default(''),
  kicker: z.string().default(''),
});
export type IdxStatementProps = z.infer<typeof idxStatementSchema>;

export const IdxStatement: React.FC<IdxStatementProps> = ({ eyebrow, headline, kicker }) => {
  const rule = useRise(10);
  const head = useRise(6, 30);
  const kick = useRise(18);
  return (
    <Page>
      <div style={{
        position: 'absolute', left: 130, right: 130, top: '50%',
        transform: 'translateY(-50%)',
      }}>
        <Eyebrow text={eyebrow} />
        <div style={{
          marginTop: 26, fontFamily: S, fontSize: 76, lineHeight: 1.16,
          color: CLAUDE.INK, letterSpacing: '-0.015em',
          opacity: head, transform: `translateY(${(1 - head) * 18}px)`,
        }}>{headline}</div>
        <div style={{
          marginTop: 34, width: 190 * rule, height: 3,
          background: CLAUDE.SPARK, borderRadius: 2,
        }} />
        {kicker ? (
          <div style={{
            marginTop: 30, fontFamily: U, fontSize: 30, lineHeight: 1.5,
            color: CLAUDE.INK_SOFT, maxWidth: 1180,
            opacity: kick, transform: `translateY(${(1 - kick) * 10}px)`,
          }}>{kicker}</div>
        ) : null}
      </div>
    </Page>
  );
};

// ── 2. IdxSplitPane — invisible rows | rich snippet ─────────────────────────

export const idxSplitPaneSchema = z.object({});

const ROWS = [
  ['#8814', 'Software Engineer', 'H-1B'],
  ['#8815', 'Data Analyst', 'CPT/OPT'],
  ['#8816', 'ML Engineer', 'H-1B'],
  ['#8817', 'Backend Developer', 'no-data'],
  ['#8818', 'Platform Engineer', 'H-1B'],
];

export const IdxSplitPane: React.FC = () => {
  const left = useRise(4);
  const right = useRise(30);
  const { width } = useVideoConfig();
  const mid = width / 2;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 78 }}>
        <Eyebrow text="the two ends of the pipeline" />
      </div>

      {/* LEFT — the database, correct but unseen */}
      <div style={{
        position: 'absolute', left: 96, top: 168, width: mid - 168,
        opacity: left, transform: `translateX(${(1 - left) * -22}px)`,
      }}>
        <div style={{ fontFamily: U, fontSize: 21, fontWeight: 600, letterSpacing: 2, color: CLAUDE.INK_SOFT, marginBottom: 16 }}>
          IN THE DATABASE — CORRECT
        </div>
        <Card style={{ padding: '22px 26px' }}>
          {ROWS.map(([id, title, tag], i) => (
            <div key={id} style={{
              display: 'flex', alignItems: 'center', gap: 18,
              padding: '13px 0',
              borderBottom: i < ROWS.length - 1 ? `1px solid ${CLAUDE.BORDER}` : 'none',
              fontFamily: M, fontSize: 22, color: CLAUDE.INK_SOFT,
            }}>
              <span style={{ color: CLAUDE.GHOST, width: 76 }}>{id}</span>
              <span style={{ flex: 1, color: CLAUDE.INK }}>{title}</span>
              <span style={{
                fontSize: 18, padding: '4px 12px', borderRadius: 20,
                background: CLAUDE.PILL, color: CLAUDE.INK_SOFT,
              }}>{tag}</span>
            </div>
          ))}
        </Card>
        <div style={{ marginTop: 20, fontFamily: U, fontSize: 25, color: CLAUDE.GHOST }}>
          …and invisible to every crawler
        </div>
      </div>

      {/* divider */}
      <div style={{
        position: 'absolute', left: mid - 1, top: 168, bottom: 190,
        width: 2, background: CLAUDE.BORDER,
      }} />

      {/* RIGHT — the rich snippet */}
      <div style={{
        position: 'absolute', left: mid + 72, top: 168, width: mid - 168,
        opacity: right, transform: `translateX(${(1 - right) * 22}px)`,
      }}>
        <div style={{ fontFamily: U, fontSize: 21, fontWeight: 600, letterSpacing: 2, color: CLAUDE.SPARK, marginBottom: 16 }}>
          IN THE SERP — VISIBLE
        </div>
        <Card accent style={{ padding: '26px 30px' }}>
          <div style={{ fontFamily: U, fontSize: 19, color: CLAUDE.INK_SOFT }}>jobsekr.com › jobs › 8814</div>
          <div style={{ fontFamily: U, fontSize: 34, color: '#1a0dab', marginTop: 10, lineHeight: 1.25 }}>
            Software Engineer — H-1B Sponsorship
          </div>
          <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 12, lineHeight: 1.45 }}>
            Full-time · Seattle, WA · Visa sponsorship available
          </div>
          <div style={{ display: 'flex', gap: 10, marginTop: 18, flexWrap: 'wrap' }}>
            {['JobPosting', 'datePosted', 'jobLocation', 'employmentType'].map((k) => (
              <span key={k} style={{
                fontFamily: M, fontSize: 17, padding: '5px 11px', borderRadius: 6,
                background: '#FBEEE8', color: CLAUDE.SEND,
              }}>{k}</span>
            ))}
          </div>
        </Card>
        <div style={{ marginTop: 20, fontFamily: U, fontSize: 25, color: CLAUDE.INK }}>
          the same row — parsed, ranked, displayed
        </div>
      </div>

      <SparkLine text="Same data. The only difference is whether it was exposed." delay={46} />
    </Page>
  );
};

// ── 3. IdxLayerStack — building upward ──────────────────────────────────────

export const idxLayerStackSchema = z.object({});

const LAYERS = [
  ['PROGRAMMATIC SEO', 'city × role routes that earn their own uniqueness'],
  ['ROUTE HANDLING', 'dynamic sitemaps, canonicals, noindex'],
  ['STRUCTURED DATA', 'JSON-LD JobPosting the crawler can parse'],
  ['THE DATABASE', 'idempotent migrations · batched classification'],
];

export const IdxLayerStack: React.FC = () => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the architectural journey — bottom up" />
      </div>
      <div style={{ position: 'absolute', left: 130, right: 130, top: 168 }}>
        {LAYERS.map(([name, sub], i) => {
          // bottom layer animates first
          const order = LAYERS.length - 1 - i;
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(6 + order * 13);
          const isBase = i === LAYERS.length - 1;
          return (
            <div key={name} style={{
              opacity: t, transform: `translateY(${(1 - t) * 26}px)`,
              marginBottom: 18,
            }}>
              <Card accent={isBase} style={{
                padding: '26px 34px', display: 'flex', alignItems: 'center', gap: 28,
                background: isBase ? '#FBEEE8' : CLAUDE.CARD,
              }}>
                <span style={{
                  fontFamily: M, fontSize: 22, color: isBase ? CLAUDE.SEND : CLAUDE.GHOST,
                  width: 44,
                }}>{`0${LAYERS.length - i}`}</span>
                <div style={{ flex: 1 }}>
                  <div style={{
                    fontFamily: U, fontSize: 32, fontWeight: 600, letterSpacing: 1.2,
                    color: CLAUDE.INK,
                  }}>{name}</div>
                  <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT, marginTop: 7 }}>{sub}</div>
                </div>
              </Card>
            </div>
          );
        })}
      </div>
      <SparkLine text="Start at the bottom. Every layer above is worthless without it." delay={62} />
    </Page>
  );
};

// ── 4. IdxBatchFlow — 23,000 rows, 1,000 at a time ──────────────────────────

export const idxBatchFlowSchema = z.object({});

export const IdxBatchFlow: React.FC = () => {
  const frame = useCurrentFrame();
  const pool = useRise(4);
  const box = useRise(22);
  const done = useRise(46);
  // batches consumed over time
  const consumed = Math.min(23, Math.floor(interpolate(frame, [40, 150], [0, 23], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  })));
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the batching solution" />
      </div>

      {/* the pool of 23 batches (1,000 each) */}
      <div style={{
        position: 'absolute', left: 130, top: 176, width: 700,
        opacity: pool,
      }}>
        <div style={{ fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT, marginBottom: 18 }}>
          23,000 rows <span style={{ fontFamily: M, color: CLAUDE.GHOST }}>WHERE visa_tag IS NULL</span>
        </div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 11, width: 640 }}>
          {Array.from({ length: 23 }, (_, i) => {
            const eaten = i < consumed;
            return (
              <div key={i} style={{
                width: 108, height: 46, borderRadius: 8,
                background: eaten ? '#FBEEE8' : CLAUDE.CARD,
                border: `1px solid ${eaten ? CLAUDE.SPARK : CLAUDE.BORDER}`,
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontFamily: M, fontSize: 17,
                color: eaten ? CLAUDE.SEND : CLAUDE.GHOST,
                transition: 'none',
              }}>1,000</div>
            );
          })}
        </div>
      </div>

      {/* the processor */}
      <div style={{
        position: 'absolute', right: 130, top: 246, width: 620,
        opacity: box, transform: `translateX(${(1 - box) * 20}px)`,
      }}>
        <Card accent style={{ padding: '30px 34px' }}>
          <div style={{ fontFamily: U, fontSize: 21, fontWeight: 600, letterSpacing: 2, color: CLAUDE.SPARK }}>
            ONE TRANSACTION PER BATCH
          </div>
          <div style={{ fontFamily: S, fontSize: 44, color: CLAUDE.INK, marginTop: 16, lineHeight: 1.25 }}>
            23 write locks,<br />not 23,000.
          </div>
          <div style={{ marginTop: 22, height: 1, background: CLAUDE.BORDER }} />
          <div style={{ display: 'flex', gap: 40, marginTop: 22 }}>
            <div>
              <div style={{ fontFamily: M, fontSize: 40, color: CLAUDE.INK }}>{consumed * 1000}</div>
              <div style={{ fontFamily: U, fontSize: 20, color: CLAUDE.INK_SOFT, marginTop: 4 }}>classified</div>
            </div>
            <div style={{ opacity: done }}>
              <div style={{ fontFamily: M, fontSize: 40, color: CLAUDE.SEND }}>&lt; 2 min</div>
              <div style={{ fontFamily: U, fontSize: 20, color: CLAUDE.INK_SOFT, marginTop: 4 }}>total runtime</div>
            </div>
          </div>
        </Card>
      </div>

      <SparkLine text="Compute is spent only on rows that were never classified." delay={66} />
    </Page>
  );
};

// ── 5. IdxJsonLdMap — wireframe fields → JSON-LD keys ───────────────────────

export const idxJsonLdMapSchema = z.object({});

const FIELDS: [string, string, boolean][] = [
  ['Job title', 'title', true],
  ['Posted date', 'datePosted', true],
  ['Company', 'hiringOrganization', true],
  ['Location', 'jobLocation', false],
  ['Remote role', 'jobLocationType', false],
];

export const IdxJsonLdMap: React.FC = () => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="mapping the page into JobPosting" />
      </div>
      <div style={{ position: 'absolute', left: 110, right: 110, top: 172, display: 'flex', gap: 56 }}>
        {/* wireframe */}
        <div style={{ flex: 1 }}>
          <div style={{ fontFamily: U, fontSize: 21, fontWeight: 600, letterSpacing: 2, color: CLAUDE.INK_SOFT, marginBottom: 16 }}>
            THE RENDERED PAGE
          </div>
          {FIELDS.map(([label, , req], i) => {
            // eslint-disable-next-line react-hooks/rules-of-hooks
            const t = useRise(6 + i * 9);
            return (
              <div key={label} style={{ opacity: t, transform: `translateX(${(1 - t) * -14}px)`, marginBottom: 13 }}>
                <Card style={{ padding: '18px 22px', display: 'flex', alignItems: 'center', gap: 14 }}>
                  <div style={{ width: 10, height: 10, borderRadius: 5, background: req ? CLAUDE.SPARK : CLAUDE.GHOST }} />
                  <span style={{ fontFamily: U, fontSize: 27, color: CLAUDE.INK }}>{label}</span>
                </Card>
              </div>
            );
          })}
        </div>

        {/* json-ld */}
        <div style={{ flex: 1.15 }}>
          <div style={{ fontFamily: U, fontSize: 21, fontWeight: 600, letterSpacing: 2, color: CLAUDE.SPARK, marginBottom: 16 }}>
            THE JSON-LD PAYLOAD
          </div>
          <Card style={{ padding: '24px 28px', fontFamily: M, fontSize: 23, lineHeight: 1.85, color: CLAUDE.INK_SOFT }}>
            <div style={{ color: CLAUDE.GHOST }}>{'{'}</div>
            <div style={{ paddingLeft: 22 }}>
              <span style={{ color: CLAUDE.SEND }}>"@type"</span>: "JobPosting",
            </div>
            {FIELDS.map(([, key, req], i) => {
              // eslint-disable-next-line react-hooks/rules-of-hooks
              const t = useRise(12 + i * 9);
              return (
                <div key={key} style={{ paddingLeft: 22, opacity: t }}>
                  <span style={{ color: req ? CLAUDE.SEND : CLAUDE.INK_SOFT }}>"{key}"</span>
                  <span>: …{req ? '' : ' '}</span>
                  {req ? <span style={{ fontSize: 18, color: CLAUDE.GHOST }}>  required</span> : null}
                </div>
              );
            })}
            <div style={{ color: CLAUDE.GHOST }}>{'}'}</div>
          </Card>
          <div style={{ marginTop: 18, fontFamily: U, fontSize: 24, color: CLAUDE.INK_SOFT }}>
            A missing required key is a rejected posting — not a warning.
          </div>
        </div>
      </div>
      <SparkLine text="Remote roles need an explicit telecommute type, or the JSON is invalid." delay={62} />
    </Page>
  );
};

// ── 6. IdxCanonical — duplicate risk → resolved ─────────────────────────────

export const idxCanonicalSchema = z.object({
  state: z.enum(['risk', 'fixed']).default('risk'),
});
export type IdxCanonicalProps = z.infer<typeof idxCanonicalSchema>;

export const IdxCanonical: React.FC<IdxCanonicalProps> = ({ state }) => {
  const a = useRise(5);
  const b = useRise(14);
  const verdict = useRise(28);
  const risk = state === 'risk';
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text={risk ? 'two URLs, one job' : 'one canonical target'} />
      </div>

      <div style={{ position: 'absolute', left: 130, right: 130, top: 196 }}>
        <div style={{ display: 'flex', gap: 38, alignItems: 'stretch' }}>
          {/* modal URL */}
          <div style={{ flex: 1, opacity: a, transform: `translateY(${(1 - a) * 16}px)` }}>
            <Card style={{
              padding: '28px 30px', height: '100%',
              borderStyle: risk ? 'solid' : 'dashed',
              opacity: risk ? 1 : 0.55,
            }}>
              <div style={{ fontFamily: U, fontSize: 20, letterSpacing: 2, color: CLAUDE.INK_SOFT }}>MODAL OVERLAY</div>
              <div style={{ fontFamily: M, fontSize: 24, color: CLAUDE.INK, marginTop: 14, wordBreak: 'break-all' }}>
                /jobs?id=8814&amp;modal=1
              </div>
              <div style={{
                marginTop: 20, fontFamily: U, fontSize: 22,
                color: risk ? CLAUDE.SEND : CLAUDE.GHOST,
              }}>
                {risk ? 'competing for the same content' : 'rel=canonical → standalone'}
              </div>
            </Card>
          </div>

          {/* standalone URL */}
          <div style={{ flex: 1, opacity: b, transform: `translateY(${(1 - b) * 16}px)` }}>
            <Card accent={!risk} style={{
              padding: '28px 30px', height: '100%',
              background: risk ? CLAUDE.CARD : '#FBEEE8',
            }}>
              <div style={{ fontFamily: U, fontSize: 20, letterSpacing: 2, color: risk ? CLAUDE.INK_SOFT : CLAUDE.SPARK }}>
                STANDALONE PAGE
              </div>
              <div style={{ fontFamily: M, fontSize: 24, color: CLAUDE.INK, marginTop: 14, wordBreak: 'break-all' }}>
                /jobs/8814/software-engineer
              </div>
              <div style={{
                marginTop: 20, fontFamily: U, fontSize: 22,
                color: risk ? CLAUDE.SEND : CLAUDE.SEND,
              }}>
                {risk ? 'competing for the same content' : 'the one indexable URL'}
              </div>
            </Card>
          </div>
        </div>

        {/* verdict strip */}
        <div style={{
          marginTop: 40, opacity: verdict, transform: `translateY(${(1 - verdict) * 12}px)`,
        }}>
          <Card style={{
            padding: '26px 32px',
            background: risk ? '#FBEEE8' : CLAUDE.CARD,
            border: `1px solid ${risk ? CLAUDE.SPARK : CLAUDE.BORDER}`,
          }}>
            <div style={{ fontFamily: S, fontSize: 42, color: CLAUDE.INK, lineHeight: 1.3 }}>
              {risk
                ? 'The crawler sees two pages competing — and splits the ranking.'
                : 'Expired roles ship an explicit noindex. Nothing dead stays indexable.'}
            </div>
          </Card>
        </div>
      </div>

      <SparkLine
        text={risk
          ? 'Duplicate content is not a warning. It is a ranking split.'
          : 'One job. One canonical URL. One place the ranking can land.'}
        delay={40} />
    </Page>
  );
};

// ── 7. IdxSitemapTree — index → children → shards ───────────────────────────

export const idxSitemapTreeSchema = z.object({});

export const IdxSitemapTree: React.FC = () => {
  const root = useRise(4);
  const kids = [useRise(16), useRise(23), useRise(30)];
  const shards = [useRise(44), useRise(50), useRise(56)];
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="under google's 50,000-URL ceiling" />
      </div>

      <div style={{ position: 'absolute', left: 130, right: 130, top: 180 }}>
        {/* root */}
        <div style={{ opacity: root, display: 'flex', justifyContent: 'center' }}>
          <Card accent style={{ padding: '20px 34px', background: '#FBEEE8' }}>
            <span style={{ fontFamily: M, fontSize: 28, color: CLAUDE.SEND }}>/sitemap.xml</span>
            <span style={{ fontFamily: U, fontSize: 20, color: CLAUDE.INK_SOFT, marginLeft: 16 }}>root index</span>
          </Card>
        </div>

        {/* connector */}
        <div style={{ height: 34, display: 'flex', justifyContent: 'center' }}>
          <div style={{ width: 2, background: CLAUDE.BORDER, opacity: root }} />
        </div>

        {/* children */}
        <div style={{ display: 'flex', gap: 26, justifyContent: 'center' }}>
          {[['/sitemaps/jobs', '23,000 live'], ['/sitemaps/companies', '3,100'], ['/sitemaps/static', '48']].map(([p, n], i) => (
            <div key={p} style={{ opacity: kids[i], transform: `translateY(${(1 - kids[i]) * 14}px)`, flex: 1, maxWidth: 400 }}>
              <Card style={{ padding: '20px 24px', textAlign: 'center' }}>
                <div style={{ fontFamily: M, fontSize: 24, color: CLAUDE.INK }}>{p}</div>
                <div style={{ fontFamily: U, fontSize: 21, color: CLAUDE.INK_SOFT, marginTop: 8 }}>{n} URLs</div>
              </Card>
            </div>
          ))}
        </div>

        {/* shard connector under jobs */}
        <div style={{ height: 30, display: 'flex', paddingLeft: '11%' }}>
          <div style={{ width: 2, background: CLAUDE.BORDER, opacity: shards[0] }} />
        </div>

        {/* shards */}
        <div style={{ display: 'flex', gap: 18, paddingLeft: '4%' }}>
          {['jobs-1.xml', 'jobs-2.xml', 'jobs-3.xml'].map((s, i) => (
            <div key={s} style={{ opacity: shards[i], transform: `translateY(${(1 - shards[i]) * 12}px)` }}>
              <Card style={{ padding: '15px 22px' }}>
                <span style={{ fontFamily: M, fontSize: 21, color: CLAUDE.INK_SOFT }}>{s}</span>
              </Card>
            </div>
          ))}
          <div style={{
            alignSelf: 'center', marginLeft: 20, opacity: shards[2],
            fontFamily: U, fontSize: 22, color: CLAUDE.SPARK,
          }}>
            auto-shards at the threshold
          </div>
        </div>
      </div>

      <SparkLine text="The tree is generated per request — never a file on disk." delay={64} />
    </Page>
  );
};

// ── 8. IdxCrawlBudget — spend it on live pages ──────────────────────────────

export const idxCrawlBudgetSchema = z.object({});

export const IdxCrawlBudget: React.FC = () => {
  const frame = useCurrentFrame();
  const bar = useRise(8);
  const split = interpolate(frame, [36, 84], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const wastePct = 34 * split;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the crawl budget is finite" />
      </div>

      <div style={{ position: 'absolute', left: 130, right: 130, top: 220 }}>
        <div style={{ fontFamily: S, fontSize: 52, color: CLAUDE.INK, lineHeight: 1.25, marginBottom: 40 }}>
          Googlebot spends a fixed amount of<br />time here — then it leaves.
        </div>

        {/* the budget bar */}
        <div style={{
          height: 86, borderRadius: 12, overflow: 'hidden', display: 'flex',
          border: `1px solid ${CLAUDE.BORDER}`, background: CLAUDE.CARD,
          opacity: bar,
        }}>
          <div style={{
            width: `${100 - wastePct}%`, background: '#FBEEE8',
            display: 'flex', alignItems: 'center', paddingLeft: 26,
            fontFamily: U, fontSize: 26, color: CLAUDE.SEND, fontWeight: 600,
          }}>
            live, indexable pages
          </div>
          <div style={{
            width: `${wastePct}%`, background: CLAUDE.PILL,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: U, fontSize: 24, color: CLAUDE.GHOST, whiteSpace: 'nowrap', overflow: 'hidden',
          }}>
            {wastePct > 18 ? 'expired links' : ''}
          </div>
        </div>

        <div style={{ display: 'flex', gap: 26, marginTop: 34 }}>
          <Card style={{ flex: 1, padding: '24px 28px' }}>
            <div style={{ fontFamily: M, fontSize: 22, color: CLAUDE.INK_SOFT, lineHeight: 1.7 }}>
              <span style={{ color: CLAUDE.SEND }}>WHERE</span> status = 'active'<br />
              <span style={{ color: CLAUDE.SEND }}>  AND</span> expires_at &gt; now()
            </div>
          </Card>
          <Card style={{ flex: 1.3, padding: '24px 28px' }}>
            <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.INK, lineHeight: 1.5 }}>
              The sitemap query and the indexing rules must agree — or you pay for the gap.
            </div>
          </Card>
        </div>
      </div>

      <SparkLine text="Every dead link is budget spent on a blank page." delay={70} />
    </Page>
  );
};

// ── 9. IdxMatrix — 30 cities × 15 roles ─────────────────────────────────────

export const idxMatrixSchema = z.object({});

export const IdxMatrix: React.FC = () => {
  const frame = useCurrentFrame();
  const grid = useRise(6);
  const url = useRise(52);
  const lit = interpolate(frame, [20, 110], [0, 450], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const COLS = 30, ROWS_N = 15;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 70 }}>
        <Eyebrow text="the generation matrix" />
      </div>

      <div style={{ position: 'absolute', left: 130, top: 156, opacity: grid }}>
        <div style={{ display: 'flex', gap: 26, alignItems: 'flex-end', marginBottom: 14 }}>
          <span style={{ fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT }}>30 US tech hubs</span>
          <span style={{ fontFamily: U, fontSize: 25, color: CLAUDE.GHOST }}>×</span>
          <span style={{ fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT }}>15 engineering roles</span>
        </div>
        <div style={{
          display: 'grid',
          gridTemplateColumns: `repeat(${COLS}, 1fr)`,
          gap: 5, width: 1180,
        }}>
          {Array.from({ length: COLS * ROWS_N }, (_, i) => {
            const on = i < lit;
            return (
              <div key={i} style={{
                aspectRatio: '1 / 1',
                borderRadius: 3,
                background: on ? CLAUDE.SPARK : CLAUDE.PILL,
                opacity: on ? 0.92 : 1,
              }} />
            );
          })}
        </div>
      </div>

      <div style={{
        position: 'absolute', left: 130, right: 130, top: 800,
        opacity: url, transform: `translateY(${(1 - url) * 12}px)`,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 30 }}>
          <div style={{ fontFamily: M, fontSize: 44, color: CLAUDE.INK }}>
            {Math.round(Math.min(lit, 450))}
          </div>
          <div style={{ fontFamily: U, fontSize: 26, color: CLAUDE.INK_SOFT }}>
            static routes, none written by hand
          </div>
          <div style={{ flex: 1 }} />
          <Card style={{ padding: '14px 22px' }}>
            <span style={{ fontFamily: M, fontSize: 24, color: CLAUDE.SEND }}>
              /h1b-jobs/seattle/software-engineer
            </span>
          </Card>
        </div>
      </div>

      <SparkLine text="One template. The server spins out every route." delay={72} />
    </Page>
  );
};

// ── 10. IdxFaqVariation — same template, distinct pages ─────────────────────

export const idxFaqVariationSchema = z.object({});

const VARIANTS = [
  ['Seattle', 'Software Engineer', '412 open roles'],
  ['Austin', 'Data Engineer', '187 open roles'],
  ['Boston', 'ML Engineer', '96 open roles'],
];

export const IdxFaqVariation: React.FC = () => {
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="one template — three distinct pages" />
      </div>

      <div style={{ position: 'absolute', left: 110, right: 110, top: 180, display: 'flex', gap: 26 }}>
        {VARIANTS.map(([city, role, count], i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(6 + i * 14);
          return (
            <div key={city} style={{ flex: 1, opacity: t, transform: `translateY(${(1 - t) * 20}px)` }}>
              <Card accent={i === 0} style={{ padding: '26px 26px', height: '100%' }}>
                <div style={{ fontFamily: M, fontSize: 19, color: CLAUDE.SEND, wordBreak: 'break-all' }}>
                  /{city.toLowerCase()}/{role.toLowerCase().replace(/ /g, '-')}
                </div>
                <div style={{ height: 1, background: CLAUDE.BORDER, margin: '18px 0' }} />
                <div style={{ fontFamily: U, fontSize: 30, color: CLAUDE.INK, fontWeight: 600, lineHeight: 1.3 }}>
                  {role} jobs in {city}
                </div>
                <div style={{ fontFamily: U, fontSize: 24, color: CLAUDE.SPARK, marginTop: 10 }}>{count}</div>
                <div style={{ marginTop: 22, fontFamily: U, fontSize: 20, letterSpacing: 1.6, color: CLAUDE.INK_SOFT }}>
                  FAQPage
                </div>
                <div style={{ fontFamily: U, fontSize: 21, color: CLAUDE.INK_SOFT, marginTop: 10, lineHeight: 1.5 }}>
                  “Do {role.toLowerCase()} roles in {city} sponsor H-1B?”
                </div>
              </Card>
            </div>
          );
        })}
      </div>

      <SparkLine text="Live counts and a per-route FAQ payload — no two pages match." delay={58} />
    </Page>
  );
};

// ── 11. IdxSearchConsole — the remediation loop ─────────────────────────────

export const idxSearchConsoleSchema = z.object({});

const FLAGS = [
  ['Missing field "salaryRange"', 'recommended'],
  ['Missing field "validThrough"', 'recommended'],
  ['Duplicate without canonical', 'warning'],
  ['Submitted URL marked noindex', 'warning'],
];

export const IdxSearchConsole: React.FC = () => {
  const frame = useCurrentFrame();
  const card = useRise(5);
  const cleared = interpolate(frame, [40, 130], [0, FLAGS.length], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  });
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="google search console — the only verdict that counts" />
      </div>

      <div style={{ position: 'absolute', left: 130, right: 130, top: 190, opacity: card }}>
        <Card style={{ padding: '30px 34px' }}>
          <div style={{ display: 'flex', alignItems: 'baseline', gap: 16, marginBottom: 22 }}>
            <span style={{ fontFamily: U, fontSize: 27, fontWeight: 600, color: CLAUDE.INK }}>Coverage</span>
            <span style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT }}>
              {Math.max(0, FLAGS.length - Math.floor(cleared))} open · {Math.floor(cleared)} resolved
            </span>
          </div>
          {FLAGS.map(([label, kind], i) => {
            const ok = i < cleared;
            return (
              <div key={label} style={{
                display: 'flex', alignItems: 'center', gap: 18, padding: '17px 0',
                borderBottom: i < FLAGS.length - 1 ? `1px solid ${CLAUDE.BORDER}` : 'none',
              }}>
                <div style={{
                  width: 26, height: 26, borderRadius: 13, flexShrink: 0,
                  background: ok ? '#FBEEE8' : CLAUDE.PILL,
                  border: `2px solid ${ok ? CLAUDE.SPARK : CLAUDE.GHOST}`,
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontFamily: U, fontSize: 16, color: CLAUDE.SEND, fontWeight: 700,
                }}>{ok ? '✓' : ''}</div>
                <span style={{
                  flex: 1, fontFamily: U, fontSize: 27,
                  color: ok ? CLAUDE.GHOST : CLAUDE.INK,
                  textDecoration: ok ? 'line-through' : 'none',
                }}>{label}</span>
                <span style={{
                  fontFamily: U, fontSize: 19, letterSpacing: 1.4, textTransform: 'uppercase',
                  color: ok ? CLAUDE.SPARK : CLAUDE.INK_SOFT,
                }}>{ok ? 'cleared' : kind}</span>
              </div>
            );
          })}
        </Card>
      </div>

      <SparkLine text="Adjust the fallbacks, resubmit, and read the platform's answer." delay={72} />
    </Page>
  );
};

// ── 12. IdxOutcomes — the measurable end state ──────────────────────────────

export const idxOutcomesSchema = z.object({
  score: z.number().default(100),
  scoreLabel: z.string().default('Lighthouse SEO'),
  count: z.number().default(23000),
  countLabel: z.string().default('previously excluded URLs, now in the live index'),
  closer: z.string().default('The database never changed. Only its exposure did.'),
  sparkLine: z.string().default('Same rows. Same classifier. A different outcome entirely.'),
});
export type IdxOutcomesProps = z.infer<typeof idxOutcomesSchema>;

export const IdxOutcomes: React.FC<IdxOutcomesProps> = ({
  score, scoreLabel, count, countLabel, closer, sparkLine,
}) => {
  const frame = useCurrentFrame();
  const a = useRise(6);
  const b = useRise(18);
  const seo = Math.round(interpolate(frame, [14, 74], [0, score], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
  const indexed = Math.round(interpolate(frame, [26, 104], [0, count], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }));
  const R = 92, C = 2 * Math.PI * R;
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 74 }}>
        <Eyebrow text="the measurable outcome" />
      </div>

      <div style={{
        position: 'absolute', left: 130, right: 130, top: 230,
        display: 'flex', gap: 60, alignItems: 'center',
      }}>
        {/* lighthouse dial */}
        <div style={{ opacity: a, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <svg width={230} height={230}>
            <circle cx={115} cy={115} r={R} fill="none" stroke={CLAUDE.PILL} strokeWidth={16} />
            <circle cx={115} cy={115} r={R} fill="none" stroke={CLAUDE.SPARK} strokeWidth={16}
              strokeLinecap="round" strokeDasharray={C}
              strokeDashoffset={C * (1 - seo / 100)}
              transform="rotate(-90 115 115)" />
            <text x={115} y={132} textAnchor="middle"
              style={{ fontFamily: M, fontSize: 62, fill: CLAUDE.INK }}>{seo}</text>
          </svg>
          <div style={{ fontFamily: U, fontSize: 25, color: CLAUDE.INK_SOFT, marginTop: 10 }}>{scoreLabel}</div>
        </div>

        {/* indexed counter */}
        <div style={{ flex: 1, opacity: b }}>
          <Card style={{ padding: '34px 38px' }}>
            <div style={{ fontFamily: M, fontSize: 92, color: CLAUDE.INK, lineHeight: 1 }}>
              {indexed.toLocaleString()}
            </div>
            <div style={{ fontFamily: U, fontSize: 28, color: CLAUDE.INK_SOFT, marginTop: 14 }}>
              {countLabel}
            </div>
            <div style={{ height: 1, background: CLAUDE.BORDER, margin: '24px 0' }} />
            <div style={{ fontFamily: S, fontSize: 34, color: CLAUDE.INK, lineHeight: 1.35 }}>
              {closer}
            </div>
          </Card>
        </div>
      </div>

      <SparkLine text={sparkLine} delay={78} />
    </Page>
  );
};

// ── 13. IdxPipelineFlow — scrape → detect → classify → tag ──────────────────

export const idxPipelineFlowSchema = z.object({});

const STEPS: [string, string, boolean][] = [
  ['SCRAPE', 'fresh listings arrive', false],
  ['US-BASED?', 'sponsorship law is US-specific', true],
  ['CLASSIFY', 'visa type by pattern set', false],
  ['TAG', 'the row becomes searchable', false],
];

export const IdxPipelineFlow: React.FC = () => {
  const closer = useRise(58);
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 82 }}>
        <Eyebrow text="one pipeline, four steps" />
      </div>

      <div style={{
        position: 'absolute', left: 96, right: 96, top: '46%',
        transform: 'translateY(-50%)',
        display: 'flex', alignItems: 'stretch', gap: 0,
      }}>
        {STEPS.map(([name, sub, gate], i) => {
          // eslint-disable-next-line react-hooks/rules-of-hooks
          const t = useRise(6 + i * 14);
          return (
            <React.Fragment key={name}>
              <div style={{
                flex: 1, opacity: t, transform: `translateY(${(1 - t) * 20}px)`,
              }}>
                <Card accent={gate} style={{
                  padding: '30px 24px', height: '100%',
                  background: gate ? '#FBEEE8' : CLAUDE.CARD,
                  textAlign: 'center',
                }}>
                  <div style={{
                    fontFamily: M, fontSize: 19, color: gate ? CLAUDE.SEND : CLAUDE.GHOST,
                    letterSpacing: 1.5,
                  }}>{`0${i + 1}`}</div>
                  <div style={{
                    fontFamily: U, fontSize: 33, fontWeight: 600, color: CLAUDE.INK,
                    marginTop: 12, letterSpacing: 0.6,
                  }}>{name}</div>
                  <div style={{
                    fontFamily: U, fontSize: 21, color: CLAUDE.INK_SOFT,
                    marginTop: 12, lineHeight: 1.45,
                  }}>{sub}</div>
                </Card>
              </div>
              {i < STEPS.length - 1 ? (
                <div style={{
                  width: 54, display: 'flex', alignItems: 'center', justifyContent: 'center',
                  opacity: t, fontFamily: U, fontSize: 30, color: CLAUDE.GHOST,
                }}>→</div>
              ) : null}
            </React.Fragment>
          );
        })}
      </div>

      <div style={{
        position: 'absolute', left: 96, right: 96, top: '76%',
        opacity: closer, transform: `translateY(${(1 - closer) * 12}px)`,
      }}>
        <div style={{ fontFamily: S, fontSize: 44, color: CLAUDE.INK, lineHeight: 1.3 }}>
          Twenty-three thousand invisible rows — now searchable by visa status.
        </div>
      </div>

      <SparkLine text="Filter the international noise early, or the classifier learns the wrong thing." delay={74} />
    </Page>
  );
};

// ── 14. IdxBlocked — shipped, then stopped ──────────────────────────────────

export const idxBlockedSchema = z.object({});

export const IdxBlocked: React.FC = () => {
  const frame = useCurrentFrame();
  const row = useRise(4);
  const wall = useRise(40, 22);
  const zero = useRise(58);
  const shipped = Math.min(11, Math.floor(interpolate(frame, [10, 62], [0, 11], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp',
  })));
  return (
    <Page>
      <div style={{ position: 'absolute', left: 96, top: 82 }}>
        <Eyebrow text="week twelve" />
      </div>

      {/* the 12-week strip */}
      <div style={{
        position: 'absolute', left: 96, right: 96, top: 210, opacity: row,
        display: 'flex', gap: 10, alignItems: 'flex-end',
      }}>
        {Array.from({ length: 11 }, (_, i) => (
          <div key={i} style={{ flex: 1 }}>
            <div style={{
              height: i < shipped ? 92 : 20,
              borderRadius: 8,
              background: i < shipped ? CLAUDE.SPARK : CLAUDE.PILL,
              opacity: i < shipped ? 0.9 : 1,
            }} />
            <div style={{
              fontFamily: M, fontSize: 17, color: CLAUDE.GHOST,
              textAlign: 'center', marginTop: 10,
            }}>{`w${i + 1}`}</div>
          </div>
        ))}
        {/* week 12 — the wall */}
        <div style={{ flex: 1.5, opacity: wall }}>
          <div style={{
            height: 92, borderRadius: 8,
            border: `2px dashed ${CLAUDE.GHOST}`,
            background: CLAUDE.PILL,
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            fontFamily: U, fontSize: 30, color: CLAUDE.GHOST,
          }}>—</div>
          <div style={{
            fontFamily: M, fontSize: 17, color: CLAUDE.INK,
            textAlign: 'center', marginTop: 10,
          }}>w12</div>
        </div>
      </div>

      {/* the reason */}
      <div style={{
        position: 'absolute', left: 96, right: 96, top: 400,
        opacity: wall, transform: `translateY(${(1 - wall) * 16}px)`,
      }}>
        <Card style={{ padding: '34px 38px', borderStyle: 'dashed' }}>
          <div style={{
            fontFamily: U, fontSize: 21, letterSpacing: 2.4, color: CLAUDE.INK_SOFT,
            textTransform: 'uppercase',
          }}>the blocker was not technical</div>
          <div style={{
            fontFamily: S, fontSize: 62, color: CLAUDE.INK, marginTop: 18, lineHeight: 1.2,
          }}>No repository access.</div>
          <div style={{
            display: 'flex', gap: 56, marginTop: 30, opacity: zero, alignItems: 'baseline',
          }}>
            <div>
              <div style={{ fontFamily: M, fontSize: 58, color: CLAUDE.SEND }}>0</div>
              <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT, marginTop: 6 }}>lines written</div>
            </div>
            <div>
              <div style={{ fontFamily: M, fontSize: 58, color: CLAUDE.INK }}>1</div>
              <div style={{ fontFamily: U, fontSize: 22, color: CLAUDE.INK_SOFT, marginTop: 6 }}>open ticket</div>
            </div>
          </div>
        </Card>
      </div>

      <SparkLine text="Eleven weeks of velocity, stopped by a permission." delay={78} />
    </Page>
  );
};
