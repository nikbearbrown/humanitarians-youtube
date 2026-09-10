import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {CLAUDE, CLAUDE_FONT} from '../tokens/claude';
import {SAFE} from '../tokens/layout';

const kinds = [
  'continuation', 'next-layer', 'engine', 'variables', 'scenario-inputs',
  'scenario-outputs', 'comparison', 'example', 'boundary', 'heuristics',
  'validation', 'product-architecture', 'scenario-lab', 'ux-plan',
  'backend', 'reuse', 'outcome',
] as const;

export const causalCoutureWeek3Schema = z.object({kind: z.enum(kinds)});
export type CausalCoutureWeek3Props = z.infer<typeof causalCoutureWeek3Schema>;

const serif = CLAUDE_FONT.serif;
const sans = CLAUDE_FONT.ui;
const mono = CLAUDE_FONT.mono;
const wash = '#FFF5F0';
const oliveWash = '#F4F3EB';

const titles: Record<typeof kinds[number], string> = {
  continuation: 'From Review to Design',
  'next-layer': 'Designing the Next Analytical Layer',
  engine: 'The Scenario Intelligence Engine',
  variables: 'Four Initial Scenario Variables',
  'scenario-inputs': 'A Consistent Scenario Structure',
  'scenario-outputs': 'From Differences to Interpretation',
  comparison: 'Baseline Beside Scenario',
  example: 'Demand Up. Inventory Down.',
  boundary: 'The Methodological Boundary',
  heuristics: 'Existing Heuristics. New Comparison.',
  validation: 'Validation Before Analysis',
  'product-architecture': 'A Clearer Product Architecture',
  'scenario-lab': 'The Planned Scenario Lab',
  'ux-plan': 'From Prototype to Product Experience',
  backend: 'A Modular Backend Blueprint',
  reuse: 'Reuse the Logic. Do Not Duplicate It.',
  outcome: 'Designed and Prepared for Implementation',
};

const Card: React.FC<{
  children: React.ReactNode; accent?: boolean; muted?: boolean; dashed?: boolean;
  small?: boolean; status?: string; align?: 'center'|'left';
}> = ({children, accent, muted, dashed, small, status, align = 'center'}) => <div style={{
  minHeight: small ? 88 : 118,
  padding: small ? '15px 18px' : '22px 26px',
  borderRadius: 20,
  border: `${dashed ? '2px dashed' : '2px solid'} ${accent ? CLAUDE.SPARK : CLAUDE.BORDER}`,
  background: accent ? wash : muted ? oliveWash : CLAUDE.CARD,
  boxShadow: '0 10px 30px rgba(61,57,41,0.075)',
  display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: align === 'left' ? 'flex-start' : 'center', gap: 8,
  fontFamily: sans, color: CLAUDE.INK, fontSize: small ? 20 : 26, fontWeight: 650,
  lineHeight: 1.16, textAlign: align, whiteSpace: 'pre-line',
}}>
  {status && <div style={{fontFamily: mono, fontSize: 14, color: CLAUDE.SPARK, letterSpacing: 1.5, textTransform: 'uppercase'}}>{status}</div>}
  {children}
</div>;

const Arrow: React.FC<{vertical?: boolean; muted?: boolean}> = ({vertical, muted}) => <div style={{
  fontFamily: sans, fontSize: 38, color: muted ? CLAUDE.BORDER : CLAUDE.SPARK,
  lineHeight: 1, textAlign: 'center', transform: vertical ? 'rotate(90deg)' : undefined,
}}>→</div>;

const Key: React.FC<{children: React.ReactNode}> = ({children}) => <div style={{
  display: 'inline-flex', alignItems: 'center', gap: 10, padding: '8px 14px',
  border: `1px solid ${CLAUDE.SPARK}`, borderRadius: 999, background: wash,
  color: CLAUDE.SPARK, fontFamily: mono, fontSize: 15, letterSpacing: 1.25,
  textTransform: 'uppercase',
}}><span style={{width: 8, height: 8, borderRadius: 20, background: CLAUDE.SPARK}}/>{children}</div>;

const Flow: React.FC<{items: string[]; planned?: boolean; accentAt?: number}> = ({items, planned, accentAt = items.length - 1}) => <div style={{display: 'flex', alignItems: 'center', gap: 9, width: '100%'}}>
  {items.map((item, i) => <React.Fragment key={item}>
    <div style={{flex: 1, minWidth: 0}}><Card small accent={i === accentAt} dashed={planned} status={planned ? 'Planned' : undefined}>{item}</Card></div>
    {i < items.length - 1 && <Arrow/>}
  </React.Fragment>)}
</div>;

const SceneBody: React.FC<CausalCoutureWeek3Props> = ({kind}) => {
  switch (kind) {
    case 'continuation': return <div style={{display: 'grid', gap: 25}}>
      <Flow items={['Prototype Reviewed', 'Limitations Documented', 'Scenario-Based Layer Required']} accentAt={2}/>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 0.1fr 1fr', gap: 20, alignItems: 'center'}}>
        <Card muted>Week 2 Outcome</Card><Arrow/><Card accent dashed status="Design phase">Design Before Implementation</Card>
      </div>
    </div>;
    case 'next-layer': return <div style={{display: 'grid', gridTemplateColumns: '0.9fr 0.12fr 1.2fr', gap: 24, alignItems: 'center'}}>
      <Card>Current Business Signals</Card><Arrow/><div style={{display: 'grid', gap: 16}}><Card accent dashed status="Planned analytical layer">Structured What-If Analysis</Card><Card dashed status="Decision context">Fashion Inventory & Demand Decisions</Card></div>
    </div>;
    case 'engine': return <div style={{display: 'grid', gap: 22}}>
      <div style={{textAlign: 'center'}}><Key>Proposed what-if framework</Key></div>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 0.1fr 1.25fr 0.1fr 1fr', gap: 16, alignItems: 'center'}}>
        <Card>Existing Analytical Framework</Card><Arrow/><Card accent dashed status="Designed">Scenario Intelligence Engine</Card><Arrow/><Card>Scenario Signals & Recommendations</Card>
      </div>
      <div style={{width: '36%', margin: '0 auto'}}><Card small dashed status="User input">Selected Business Assumptions</Card></div>
    </div>;
    case 'variables': return <div style={{display: 'grid', gap: 22}}>
      <div style={{textAlign: 'center'}}><Key>Initial adjustable assumptions</Key></div>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 18}}>
        {['Demand change', 'Inventory change', 'Engagement change', 'Conversion change'].map((x, i) => <Card key={x} accent={i === 0} dashed status="Scenario variable"><span style={{fontFamily: serif, fontSize: 30}}>{x}</span><span style={{color: CLAUDE.SPARK, fontSize: 30}}>{i % 2 ? '↕' : '↕'}</span></Card>)}
      </div>
      <div style={{fontFamily: serif, fontSize: 25, color: CLAUDE.INK_SOFT, textAlign: 'center'}}>Symbolic controls · no values, ranges, or thresholds claimed</div>
    </div>;
    case 'scenario-inputs': return <div style={{display: 'grid', gap: 28}}>
      <Flow items={['Current Baseline', 'User Hypothetical Assumptions', 'Recalculated Scenario Signals']} planned accentAt={2}/>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 0.1fr 1fr', gap: 18, alignItems: 'center'}}><Card muted>Observed Current State</Card><Arrow/><Card accent dashed status="Controlled what-if">Hypothetical State</Card></div>
    </div>;
    case 'scenario-outputs': return <div style={{display: 'grid', gap: 18}}>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 16}}>{['Baseline–Scenario Differences', 'Direction of Change', 'Resulting Recommendation'].map((x, i) => <Card key={x} accent={i === 0} dashed status="Planned output">{x}</Card>)}</div>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, width: '72%', margin: '0 auto'}}><Card dashed status="Interpretation">Explanation</Card><Card dashed status="Interpretation">Confidence / Context</Card></div>
      <div style={{fontFamily: mono, fontSize: 16, textAlign: 'center', color: CLAUDE.INK_SOFT}}>NO INVENTED SCORES · NO FABRICATED RECOMMENDATION COPY</div>
    </div>;
    case 'comparison': return <div style={{display: 'grid', gap: 16}}>
      <div style={{textAlign: 'center'}}><Key>Planned comparison view</Key></div>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 0.32fr 1fr', gap: 18}}>
        <div style={{display: 'grid', gap: 12}}><Card accent status="Current baseline">Business State</Card>{['Demand Signal', 'Stock Risk', 'Recommendation'].map(x => <Card small key={x}>{x}</Card>)}</div>
        <div style={{display: 'grid', alignContent: 'center', gap: 18, textAlign: 'center', fontFamily: mono, color: CLAUDE.SPARK}}><div>DIFFERENCE</div><div style={{fontSize: 48}}>⇄</div><div>DIRECTION</div></div>
        <div style={{display: 'grid', gap: 12}}><Card dashed status="Hypothetical scenario">Simulated State</Card>{['Demand Signal', 'Stock Risk', 'Recommendation'].map(x => <Card small dashed key={x}>{x}</Card>)}</div>
      </div>
    </div>;
    case 'example': return <div style={{display: 'grid', gap: 22}}>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 20}}><Card accent dashed status="Hypothetical assumption">Demand ↑</Card><Card dashed status="Hypothetical assumption">Available Inventory ↓</Card></div>
      <Arrow vertical/>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 0.12fr 1fr', gap: 20, alignItems: 'center'}}><Card accent dashed status="Possible response">Stock-Risk Signal<br/>More Urgent?</Card><Arrow/><Card accent dashed status="Possible response">Recommendation Signal<br/>More Urgent?</Card></div>
      <div style={{fontFamily: mono, fontSize: 16, textAlign: 'center', color: CLAUDE.INK_SOFT}}>CONDITIONAL RESPONSE · NOT A HISTORICAL RESULT</div>
    </div>;
    case 'boundary': return <div style={{display: 'grid', gridTemplateColumns: '1.2fr 0.08fr 1fr', gap: 22, alignItems: 'stretch'}}>
      <Card accent status="Designed scope"><span style={{fontFamily: serif, fontSize: 34}}>Controlled What-If Simulation</span><span>How signals respond under hypothetical assumptions</span></Card>
      <div style={{display: 'flex', justifyContent: 'center'}}><div style={{width: 3, height: '100%', background: CLAUDE.SPARK}}/></div>
      <div style={{display: 'grid', gap: 18}}><Card muted>Forecasting<br/><span style={{color: CLAUDE.SPARK}}>NOT CLAIMED</span></Card><Card muted>Causal Inference<br/><span style={{color: CLAUDE.SPARK}}>NOT CLAIMED</span></Card></div>
    </div>;
    case 'heuristics': return <div style={{display: 'grid', gap: 26}}>
      <div style={{width: '48%', margin: '0 auto'}}><Card accent status="Existing framework">Heuristic Analytical Calculations</Card></div>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 0.12fr 1fr', gap: 20, alignItems: 'center'}}><Card>Baseline Decision-Support Signals</Card><div style={{fontSize: 42, color: CLAUDE.SPARK, textAlign: 'center'}}>↙ ↘</div><Card dashed status="Proposed">Scenario Decision-Support Signals</Card></div>
      <div style={{display: 'flex', gap: 16, justifyContent: 'center'}}><Key>Not prediction</Key><Key>Not causal effects</Key></div>
    </div>;
    case 'validation': return <div style={{display: 'grid', gridTemplateColumns: '1fr 0.15fr 1fr 0.15fr 1fr', gap: 16, alignItems: 'center'}}>
      <div style={{display: 'grid', gap: 14}}><Card dashed>Scenario Assumptions</Card><Card muted>Malformed or Unrealistic Assumptions</Card></div><Arrow/><Card accent dashed status="Planned boundary">Input Validation</Card><Arrow/><Card>Analytical Workflow</Card>
    </div>;
    case 'product-architecture': return <div style={{display: 'grid', gap: 22}}>
      <div style={{textAlign: 'center'}}><Key>Planned information architecture</Key></div>
      <Flow items={['Overview', 'Data', 'Intelligence', 'Scenario Lab', 'Insights']} planned accentAt={3}/>
      <div style={{height: 2, background: CLAUDE.BORDER}}/>
      <div style={{fontFamily: mono, color: CLAUDE.INK_SOFT, textAlign: 'center', letterSpacing: 1}}>INTENDED USER JOURNEY</div>
      <Flow items={['Upload', 'Validate', 'Integrate', 'Analyze', 'Simulate', 'Decide']} accentAt={4}/>
    </div>;
    case 'scenario-lab': return <div style={{display: 'grid', gap: 14}}>
      <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}><Key>Conceptual interface · planned</Key><div style={{fontFamily: mono, fontSize: 15, color: CLAUDE.INK_SOFT}}>OVERVIEW · DATA · INTELLIGENCE · <span style={{color: CLAUDE.SPARK}}>SCENARIO LAB</span> · INSIGHTS</div></div>
      <div style={{border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 22, padding: 18, background: CLAUDE.CARD, display: 'grid', gridTemplateColumns: '0.7fr 1.35fr 0.8fr', gap: 15}}>
        <div style={{display: 'grid', gap: 10}}><Card small accent status="Assumptions">Demand</Card><Card small status="Assumptions">Inventory</Card><Card small status="Assumptions">Engagement</Card><Card small status="Assumptions">Conversion</Card></div>
        <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10}}><Card small accent status="Baseline">Current State</Card><Card small dashed status="Scenario">Simulated State</Card><Card small>Difference</Card><Card small>Direction</Card></div>
        <div style={{display: 'grid', gap: 10}}><Card small dashed status="Planned output">Recommendation</Card><Card small dashed>Explanation</Card><Card small dashed>Context</Card></div>
      </div>
    </div>;
    case 'ux-plan': return <div style={{display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 18}}>
      <Card accent align="left" status="Clearer structure">Functional separation<br/>Sticky navigation<br/>Responsive layouts<br/>Improved hierarchy</Card>
      <Card align="left" status="Clearer decisions">KPI presentation<br/>Recommendation cards<br/>Source indicators<br/>Progressive disclosure</Card>
      <Card align="left" status="Clearer experience">Loading feedback<br/>Success / error feedback<br/>Fashion-oriented identity</Card>
    </div>;
    case 'backend': return <div style={{display: 'grid', gap: 22}}>
      <div style={{textAlign: 'center'}}><Key>Planned modules · not yet implemented</Key></div>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 14}}>{['Core Scorecard Calculations', 'Scenario Simulation', 'Trend Analysis', 'Alert Generation', 'Dashboard Aggregation'].map((x, i) => <Card key={x} small accent={i === 0} dashed status="Planned component">{x}</Card>)}</div>
      <div style={{fontFamily: serif, fontSize: 28, textAlign: 'center', color: CLAUDE.INK_SOFT}}>Separate responsibilities before scenario implementation</div>
    </div>;
    case 'reuse': return <div style={{display: 'grid', gap: 24}}>
      <div style={{width: '46%', margin: '0 auto'}}><Card accent status="Shared logic">Core Scorecard Calculations</Card></div>
      <div style={{fontSize: 45, color: CLAUDE.SPARK, textAlign: 'center'}}>↙　↘</div>
      <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24}}><Card>Baseline Dashboard Workflow</Card><Card dashed status="Future workflow">Scenario Analysis</Card></div>
      <div style={{textAlign: 'center'}}><Key>Reuse across workflows · no duplicated calculation logic</Key></div>
    </div>;
    case 'outcome': return <div style={{display: 'grid', gap: 22}}>
      <div style={{display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 13}}>{['Framework Designed', 'Inputs & Outputs Defined', 'Boundaries Established', 'Scenario Lab Planned', 'Architecture Outlined'].map((x, i) => <Card key={x} small accent={i === 0}>{x}</Card>)}</div>
      <div style={{fontFamily: serif, fontSize: 50, fontWeight: 700, textAlign: 'center'}}>Prepared for Implementation<span style={{color: CLAUDE.SPARK}}>.</span></div>
      <div style={{display: 'flex', justifyContent: 'center', gap: 28, fontFamily: sans, fontSize: 27}}><span>Ushasvi Rachel</span><span style={{color: CLAUDE.SPARK}}>·</span><span>Humanitarians.ai</span></div>
    </div>;
  }
};

export const CausalCoutureWeek3: React.FC<CausalCoutureWeek3Props> = (props) => {
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
