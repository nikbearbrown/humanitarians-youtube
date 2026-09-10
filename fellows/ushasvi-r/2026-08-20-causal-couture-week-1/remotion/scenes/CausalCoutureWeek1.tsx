import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {SAFE} from '../tokens/layout';

const kinds = [
  'intro', 'sources', 'integration', 'preprocessing', 'dataset', 'features-a',
  'features-b', 'scorecard', 'recommendation', 'backend', 'pipeline',
  'boundary', 'outcome', 'outro',
] as const;

export const causalCoutureWeek1Schema = z.object({
  kind: z.enum(kinds),
  next: z.string().optional(),
});
export type CausalCoutureWeek1Props = z.infer<typeof causalCoutureWeek1Schema>;

const serif = CLAUDE_FONT.serif;
const sans = CLAUDE_FONT.ui;
const mono = CLAUDE_FONT.mono;

const DATA_SOURCES = ['Sales', 'Inventory', 'Social Engagement', 'Web Activity'];
const SCORECARD = ['Demand Pressure', 'Stock Risk', 'Engagement Momentum', 'Conversion Strength'];
const PIPELINE = ['Source Data', 'Validation', 'Preprocessing', 'Unified Dataset', 'Analytical Scorecard', 'Recommendation', 'Interactive Frontend'];

const titles: Record<typeof kinds[number], string> = {
  intro: 'From Four Sources to One Prototype',
  sources: 'Four Sources. Four Business Views.',
  integration: 'One Ingestion Workflow',
  preprocessing: 'Prepare the Sources',
  dataset: 'One Common Analytical Grain',
  'features-a': 'Demand and Inventory Signals',
  'features-b': 'Engagement and Conversion Signals',
  scorecard: 'The Heuristic Business Scorecard',
  recommendation: 'Signals Into Decision Support',
  backend: 'Analysis Connected to an Interface',
  pipeline: 'The Week 1 End-to-End Workflow',
  boundary: 'The Methodological Boundary',
  outcome: 'A Working Phase 3 Prototype',
  outro: 'Causal Couture',
};

const Card: React.FC<{children: React.ReactNode; accent?: boolean; muted?: boolean; monoText?: boolean; small?: boolean}> = ({children, accent, muted, monoText, small}) => (
  <div style={{
    minHeight: small ? 108 : 126,
    borderRadius: 22,
    border: `2px solid ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
    background: accent ? '#FFF5F0' : muted ? CLAUDE.FOOTER : CLAUDE.CARD,
    boxShadow: '0 10px 32px rgba(61,57,41,0.08)',
    padding: small ? '18px 16px' : '26px 30px',
    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
    textAlign: 'center', color: CLAUDE.INK,
    fontFamily: monoText ? mono : sans, fontSize: small ? 21 : 28, fontWeight: 650, lineHeight: 1.2,
    whiteSpace: 'pre-line',
  }}>{children}</div>
);

const Arrow: React.FC<{vertical?: boolean}> = ({vertical}) => (
  <div style={{fontFamily: sans, fontSize: 44, color: CLAUDE.SPARK, lineHeight: 1}}>{vertical ? '↓' : '→'}</div>
);

const FourSources: React.FC<{compact?: boolean}> = ({compact}) => (
  <div style={{display: 'grid', gridTemplateColumns: compact ? 'repeat(4, 1fr)' : 'repeat(2, 1fr)', gap: 22, width: '100%'}}>
    {DATA_SOURCES.map((source, i) => <Card key={source} accent={i === 0}>{source}</Card>)}
  </div>
);

const Flow: React.FC<{items: string[]; compact?: boolean}> = ({items, compact}) => (
  <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', gap: compact ? 10 : 18, width: '100%'}}>
    {items.map((item, i) => <React.Fragment key={item}>
      <div style={{flex: 1, minWidth: 0}}><Card accent={i === items.length - 1} small={compact}>{item}</Card></div>
      {i < items.length - 1 && <Arrow/>}
    </React.Fragment>)}
  </div>
);

const SceneBody: React.FC<CausalCoutureWeek1Props> = ({kind, next}) => {
  switch (kind) {
    case 'intro': return <div style={{display: 'grid', gridTemplateColumns: '1.05fr 0.12fr 0.75fr', gap: 22, alignItems: 'center'}}><FourSources/><Arrow/><Card accent>Working Phase 3<br/>Prototype</Card></div>;
    case 'sources': return <FourSources/>;
    case 'integration': return <div style={{display: 'grid', gridTemplateColumns: '1.1fr 0.12fr 0.7fr', gap: 24, alignItems: 'center'}}><FourSources/><Arrow/><Card accent>Prototype Inputs</Card></div>;
    case 'preprocessing': return <Flow items={['Incoming Sources', 'Validation', 'Standardization', 'Preprocessing', 'Analysis-Ready Records']} compact/>;
    case 'dataset': return <div style={{display: 'grid', gridTemplateColumns: '0.75fr 0.12fr 1fr', gap: 28, alignItems: 'center'}}><div style={{display: 'grid', gap: 12}}>{DATA_SOURCES.map(x => <Card key={x} muted>{x}</Card>)}</div><Arrow/><div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 2, border: `2px solid ${CLAUDE.SPARK}`, background: CLAUDE.BORDER, borderRadius: 20, overflow: 'hidden'}}>{['date', 'SKU', 'business signals', 'unified dataset'].map((x, i) => <div key={x} style={{background: i < 2 ? '#FFF5F0' : CLAUDE.CARD, padding: 42, fontFamily: i < 2 ? mono : sans, fontSize: 30, fontWeight: 700, textAlign: 'center'}}>{x}</div>)}</div></div>;
    case 'features-a': return <Flow items={['Unified Dataset', 'Sales + Demand Activity', 'Inventory Availability', 'Low-Stock Conditions']} compact/>;
    case 'features-b': return <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 20}}>{['Social Engagement', 'Web Conversion Behavior', 'Sales + Social Spikes', 'Sell-Through Behavior', 'View-to-Cart Conversion'].map((x, i) => <Card key={x} accent={i === 4}>{x}</Card>)}<Card muted>Analytical Signals<br/><span style={{color: CLAUDE.SPARK}}>Not causal effects · Not forecasts</span></Card></div>;
    case 'scorecard': return <div style={{display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 24}}>{SCORECARD.map((x, i) => <Card key={x} accent={i === 0}>{x}</Card>)}</div>;
    case 'recommendation': return <div style={{display: 'grid', gridTemplateColumns: '1fr 0.12fr 0.9fr', gap: 24, alignItems: 'center'}}><div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 14}}>{SCORECARD.map(x => <Card key={x} muted>{x}</Card>)}</div><Arrow/><div style={{display: 'grid', gap: 20}}><Card accent>Overall Score</Card><Card>Rule-Based Recommendation</Card><div style={{fontFamily: serif, fontSize: 30, textAlign: 'center'}}>Business decision support</div></div></div>;
    case 'backend': return <Flow items={['Pandas · Polars\nCSV / Parquet\nDuckDB-related architecture', 'Python + FastAPI\nAPI layer', 'Interactive Frontend']} />;
    case 'pipeline': return <Flow items={PIPELINE} compact/>;
    case 'boundary': return <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 26}}><Card accent>Heuristic Decision Support<br/><span style={{fontFamily: mono, fontSize: 22}}>COMPLETED IN PHASE 3</span></Card><Card muted>Causal Estimates<br/><span style={{color: CLAUDE.SPARK}}>NOT YET</span></Card><Card muted>Demand Forecasts<br/><span style={{color: CLAUDE.SPARK}}>NOT YET</span></Card></div>;
    case 'outcome': return <div style={{display: 'grid', gap: 28}}><Flow items={['Four Sources', 'Unified Dataset', 'Scorecard', 'Recommendation', 'API', 'Interactive Frontend']} compact/><Card accent>Working Phase 3 End-to-End Analytical Prototype</Card><div style={{fontFamily: serif, fontSize: 34, fontStyle: 'italic', textAlign: 'center'}}>{next}</div></div>;
    case 'outro': return <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 24}}><div style={{fontFamily: serif, fontSize: 92, fontWeight: 700}}>Causal Couture<span style={{color: CLAUDE.SPARK}}>.</span></div><div style={{fontFamily: sans, fontSize: 34}}>Week 1 of 4</div><div style={{width: 120, height: 4, background: CLAUDE.SPARK}}/><div style={{fontFamily: serif, fontSize: 48}}>Ushasvi Rachel</div><div style={{fontFamily: sans, fontSize: 28, color: CLAUDE.INK_SOFT}}>Humanitarians.ai</div></div>;
  }
};

export const CausalCoutureWeek1: React.FC<CausalCoutureWeek1Props> = (props) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const entered = spring({frame, fps, config: {damping: 24, stiffness: 105, mass: 0.9}});
  const progress = interpolate(frame, [0, 110], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const isBookend = props.kind === 'intro' || props.kind === 'outro';
  return <AbsoluteFill style={{background: CLAUDE.PAGE, color: CLAUDE.INK}}>
    <div style={{position: 'absolute', left: SAFE.x, top: SAFE.y, right: SAFE.x, display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontFamily: sans, fontSize: 17, letterSpacing: 3, fontWeight: 750, color: CLAUDE.INK_SOFT, textTransform: 'uppercase'}}>
      <span>Causal Couture · Progress Series</span><span>Week 1 of 4</span>
    </div>
    <div style={{position: 'absolute', left: SAFE.x, right: SAFE.x, top: 118, height: 3, background: CLAUDE.BORDER}}><div style={{height: '100%', width: `${progress * 100}%`, background: CLAUDE.SPARK}}/></div>
    {!isBookend && <div style={{position: 'absolute', left: SAFE.x, right: SAFE.x, top: 156, fontFamily: serif, fontSize: 58, fontWeight: 700, lineHeight: 1.05}}>{titles[props.kind]}</div>}
    <div style={{position: 'absolute', left: SAFE.x, right: SAFE.x, top: isBookend ? 170 : 275, bottom: 135, display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: entered, transform: `translateY(${(1 - entered) * 24}px)`}}>
      <div style={{width: '100%'}}><SceneBody {...props}/></div>
    </div>
    <div style={{position: 'absolute', left: SAFE.x, right: SAFE.x, bottom: 62, display: 'flex', justifyContent: 'space-between', fontFamily: sans, fontSize: 20, color: CLAUDE.INK_SOFT}}><span>Ushasvi Rachel</span><span>Humanitarians.ai</span></div>
  </AbsoluteFill>;
};
