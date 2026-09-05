import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {SAFE} from '../tokens/layout';

const kinds = [
  'continuation', 'review', 'architecture', 'scorecard', 'recommendation',
  'boundary', 'correlation', 'recommendation-limit', 'transition',
  'planned-capabilities', 'planned-architecture', 'frontend-review',
  'requirements', 'outcome',
] as const;

export const causalCoutureWeek2Schema = z.object({kind: z.enum(kinds)});
export type CausalCoutureWeek2Props = z.infer<typeof causalCoutureWeek2Schema>;

const serif = CLAUDE_FONT.serif;
const sans = CLAUDE_FONT.ui;
const mono = CLAUDE_FONT.mono;
const accentWash = '#FFF5F0';

const titles: Record<typeof kinds[number], string> = {
  continuation: 'Review Before Expansion',
  review: 'The Prototype Under Review',
  architecture: 'Reviewing the End-to-End Architecture',
  scorecard: 'Reviewing the Existing Scorecard',
  recommendation: 'From Signals to Recommendations',
  boundary: 'The Methodological Boundary',
  correlation: 'Association Is Not Causation',
  'recommendation-limit': 'A Static View of Current Conditions',
  transition: 'The Next Analytical Direction',
  'planned-capabilities': 'Capabilities Identified for Future Work',
  'planned-architecture': 'Planned Decision and Architecture Improvements',
  'frontend-review': 'A Clearer Information Hierarchy',
  requirements: 'Requirements for the Next Phase',
  outcome: 'Phase 3 Reviewed. Next Direction Established.',
};

const Card: React.FC<{
  children: React.ReactNode; accent?: boolean; muted?: boolean; small?: boolean;
  dashed?: boolean; status?: string;
}> = ({children, accent, muted, small, dashed, status}) => (
  <div style={{
    minHeight: small ? 104 : 132,
    borderRadius: 22,
    border: `${dashed ? '2px dashed' : '2px solid'} ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
    background: accent ? accentWash : muted ? CLAUDE.FOOTER : CLAUDE.CARD,
    boxShadow: '0 10px 32px rgba(61,57,41,0.08)',
    padding: small ? '18px 16px' : '26px 30px',
    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 10,
    textAlign: 'center', color: CLAUDE.INK, fontFamily: sans,
    fontSize: small ? 21 : 28, fontWeight: 650, lineHeight: 1.18, whiteSpace: 'pre-line',
  }}>
    {status && <div style={{fontFamily: mono, fontSize: 15, letterSpacing: 1.5, color: CLAUDE.SPARK, textTransform: 'uppercase'}}>{status}</div>}
    {children}
  </div>
);

const Arrow: React.FC<{muted?: boolean}> = ({muted}) => (
  <div style={{fontFamily: sans, fontSize: 42, color: muted ? CLAUDE.BORDER : CLAUDE.SPARK, lineHeight: 1}}>→</div>
);

const Flow: React.FC<{items: string[]; finalAccent?: boolean; planned?: boolean}> = ({items, finalAccent = true, planned}) => (
  <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 10, width: '100%'}}>
    {items.map((item, i) => <React.Fragment key={item}>
      <div style={{flex: 1, minWidth: 0}}>
        <Card small accent={finalAccent && i === items.length - 1} dashed={planned} status={planned ? 'Planned' : undefined}>{item}</Card>
      </div>
      {i < items.length - 1 && <Arrow/>}
    </React.Fragment>)}
  </div>
);

const SCORECARD = ['Demand Pressure', 'Stock Risk', 'Engagement Momentum', 'Conversion Strength'];
const ARCHITECTURE = ['Data Ingestion', 'Preprocessing', 'Feature Engineering', 'Unified Dataset', 'Business-Signal Scoring', 'API', 'Frontend'];

const StatusKey: React.FC<{text: string}> = ({text}) => <div style={{
  display: 'inline-flex', alignItems: 'center', gap: 10, padding: '9px 14px', borderRadius: 999,
  background: accentWash, border: `1px solid ${CLAUDE.SPARK}`, fontFamily: mono,
  fontSize: 16, letterSpacing: 1.2, color: CLAUDE.SPARK, textTransform: 'uppercase',
}}><span style={{width: 8, height: 8, borderRadius: 99, background: CLAUDE.SPARK}}/>{text}</div>;

const SceneBody: React.FC<CausalCoutureWeek2Props> = ({kind}) => {
  switch (kind) {
    case 'continuation': return <div style={{display: 'grid', gap: 28}}>
      <Flow items={['Four Sources', 'Unified Dataset', 'Scorecard', 'Recommendation', 'API', 'Interactive Frontend']}/>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 0.12fr 0.8fr', alignItems: 'center', gap: 22}}>
        <Card accent>Functioning Phase 3 Analytical Prototype</Card><Arrow/><Card>Structured Review</Card>
      </div>
      <div style={{textAlign: 'center'}}><StatusKey text="Phase 3 Review & Analytical Limitations"/></div>
    </div>;
    case 'review': return <div style={{display: 'grid', gridTemplateColumns: '1fr 0.12fr 1fr', gap: 28, alignItems: 'center'}}>
      <Card accent>Completed Phase 3 Prototype</Card><Arrow/><div style={{display: 'grid', gap: 22}}><Card>Reusable</Card><Card>Needs Restructuring</Card><div style={{fontFamily: serif, fontSize: 26, textAlign: 'center', color: CLAUDE.INK_SOFT}}>Review categories · no component assignments claimed</div></div>
    </div>;
    case 'architecture': return <div style={{display: 'grid', gap: 30}}><Flow items={ARCHITECTURE}/><div style={{textAlign: 'center'}}><StatusKey text="One connected analytical workflow under review"/></div></div>;
    case 'scorecard': return <div style={{display: 'grid', gridTemplateColumns: '1.2fr 0.12fr 0.65fr', gap: 26, alignItems: 'center'}}>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 18}}>{SCORECARD.map(x => <Card key={x}>{x}</Card>)}</div><Arrow/><Card accent>Overall Signal</Card>
    </div>;
    case 'recommendation': return <Flow items={['Four Scorecard Signals', 'Overall Signal', 'Business Recommendation', 'Decision Support']}/>;
    case 'boundary': return <div style={{display: 'grid', gridTemplateColumns: '1fr 0.16fr 1fr', gap: 24, alignItems: 'stretch'}}>
      <div style={{display: 'grid', gap: 20}}><Card accent>Descriptive Signals</Card><Card accent>Heuristic Decision Support</Card></div>
      <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center'}}><div style={{height: '100%', width: 3, background: CLAUDE.SPARK}}/></div>
      <div style={{display: 'grid', gap: 20}}><Card muted>Causal Effects<br/><span style={{color: CLAUDE.SPARK}}>NOT ESTABLISHED</span></Card><Card muted>Forecasts<br/><span style={{color: CLAUDE.SPARK}}>NOT PROVIDED</span></Card></div>
    </div>;
    case 'correlation': return <div style={{display: 'grid', gap: 26}}>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24}}>
        <Card><span style={{color: CLAUDE.SPARK}}>↗</span> Engagement</Card><Card><span style={{color: CLAUDE.SPARK}}>↗</span> Sales</Card>
      </div>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 0.12fr 1fr', gap: 20, alignItems: 'center'}}><Card accent>Signals May Move Together</Card><Arrow/><Card muted>Does Not Establish<br/><span style={{color: CLAUDE.SPARK}}>Engagement Caused Sales</span></Card></div>
      <div style={{fontFamily: serif, fontSize: 42, fontWeight: 700, textAlign: 'center'}}>Association ≠ Causal Effect</div>
    </div>;
    case 'recommendation-limit': return <div style={{display: 'grid', gap: 26}}>
      <Flow items={['Current Conditions', 'Signal Summary', 'Recommendation']}/>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 22}}>{['Hypothetical Condition', 'Alternative Condition', 'Changed Condition'].map(x => <Card key={x} muted dashed status="Limited evaluation">{x}</Card>)}</div>
    </div>;
    case 'transition': return <div style={{display: 'grid', gridTemplateColumns: '0.85fr 0.14fr 1.15fr', gap: 26, alignItems: 'center'}}>
      <Card>Static Business-Signal Scorecard</Card><Arrow/><Card accent dashed status="Next analytical direction">Scenario & Decision-Intelligence Layer</Card>
    </div>;
    case 'planned-capabilities': return <div style={{display: 'grid', gap: 24}}>
      <div style={{textAlign: 'center'}}><StatusKey text="Identified for subsequent development"/></div>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 22}}>{['What-If Scenario Analysis', 'Baseline-versus-Scenario Comparison', 'Recent-Period Trend Analysis', 'Business-Condition Alerts'].map(x => <Card key={x} dashed status="Planned">{x}</Card>)}</div>
    </div>;
    case 'planned-architecture': return <div style={{display: 'grid', gap: 28}}>
      <div style={{textAlign: 'center'}}><StatusKey text="Planned improvements · not Week 2 implementation"/></div>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 0.12fr 1fr', gap: 24, alignItems: 'center'}}><div style={{display: 'grid', gap: 18}}><Card dashed status="Planned layer">Analytical Calculations</Card><Card dashed status="Planned layer">API Logic</Card></div><Arrow/><Card accent dashed status="Planned">More Structured Recommendations</Card></div>
    </div>;
    case 'frontend-review': return <div style={{display: 'grid', gap: 24}}>
      <div style={{textAlign: 'center'}}><StatusKey text="Conceptual information hierarchy"/></div>
      <div style={{border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 24, background: CLAUDE.CARD, padding: 24, display: 'grid', gridTemplateColumns: '0.55fr 1.45fr', gap: 20}}>
        <div style={{display: 'grid', gap: 14}}>{['Data Management', 'Intelligence Outputs', 'Scenarios', 'Technical Information'].map((x, i) => <Card key={x} small accent={i === 1}>{x}</Card>)}</div>
        <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16}}><Card muted>Clearly Separated Areas</Card><Card muted>Stronger Information Hierarchy</Card><Card accent>Improved Analytical Presentation</Card><Card muted>Not a Historical Screenshot</Card></div>
      </div>
    </div>;
    case 'requirements': return <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 24}}>
      <Card accent dashed status="Requirement">Scenario Analysis</Card><Card dashed status="Requirement">Clearer Decision Support</Card><Card dashed status="Requirement">Architecture & Presentation</Card>
    </div>;
    case 'outcome': return <div style={{display: 'grid', gap: 34}}>
      <Flow items={['Prototype Reviewed', 'Limitations Documented', 'Next-Phase Requirements Established']}/>
      <div style={{fontFamily: serif, fontSize: 56, fontWeight: 700, textAlign: 'center'}}>Causal Couture<span style={{color: CLAUDE.SPARK}}>.</span></div>
      <div style={{display: 'flex', justifyContent: 'center', gap: 30, alignItems: 'center', fontFamily: sans, fontSize: 28}}><span>Ushasvi Rachel</span><span style={{color: CLAUDE.SPARK}}>·</span><span>Humanitarians.ai</span></div>
    </div>;
  }
};

export const CausalCoutureWeek2: React.FC<CausalCoutureWeek2Props> = (props) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const entered = spring({frame, fps, config: {damping: 24, stiffness: 105, mass: 0.9}});
  const progress = interpolate(frame, [0, 110], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return <AbsoluteFill style={{background: CLAUDE.PAGE, color: CLAUDE.INK}}>
    <div style={{position: 'absolute', left: SAFE.x, top: SAFE.y, fontFamily: sans, fontSize: 17, letterSpacing: 3, fontWeight: 750, color: CLAUDE.INK_SOFT, textTransform: 'uppercase'}}>Causal Couture</div>
    <div style={{position: 'absolute', left: SAFE.x, right: SAFE.x, top: 118, height: 3, background: CLAUDE.BORDER}}><div style={{height: '100%', width: `${progress * 100}%`, background: CLAUDE.SPARK}}/></div>
    <div style={{position: 'absolute', left: SAFE.x, right: SAFE.x, top: 156, fontFamily: serif, fontSize: 58, fontWeight: 700, lineHeight: 1.05}}>{titles[props.kind]}</div>
    <div style={{position: 'absolute', left: SAFE.x, right: SAFE.x, top: 275, bottom: 135, display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: entered, transform: `translateY(${(1 - entered) * 24}px)`}}><div style={{width: '100%'}}><SceneBody {...props}/></div></div>
    <div style={{position: 'absolute', left: SAFE.x, right: SAFE.x, bottom: 62, display: 'flex', justifyContent: 'space-between', fontFamily: sans, fontSize: 20, color: CLAUDE.INK_SOFT}}><span>Ushasvi Rachel</span><span>Humanitarians.ai</span></div>
  </AbsoluteFill>;
};
