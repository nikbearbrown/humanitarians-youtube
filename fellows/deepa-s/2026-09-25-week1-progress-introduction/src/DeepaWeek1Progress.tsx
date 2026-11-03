import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Img, interpolate, useCurrentFrame, useVideoConfig, staticFile, delayRender, continueRender} from 'remotion';
import {z} from 'zod';
import {ClaudeComposerAsk, claudeComposerAskSchema} from './ClaudeComposerAsk';
import {HUMANITARIANS as C} from '../tokens/humanitarians';

/** DeepaWeek1Progress — native HAI introduction graphics in landscape and portrait. */
export const deepaWeek1ProgressSchema = z.object({beat: z.string(), frames: z.number()});
type Props = z.infer<typeof deepaWeek1ProgressSchema>;
const serif = '"EB Garamond", Georgia, serif';
const sans = 'Montserrat, Arial, sans-serif';

export const DeepaWeek1Progress: React.FC<Props> = ({beat}) => {
  const frame = useCurrentFrame();
  const {width: w, height: h} = useVideoConfig();
  const portrait = h > w;
  const [fontHandle] = useState(() => delayRender('Load HAI fonts'));
  useEffect(() => {
    Promise.all([
      ['EB Garamond', 'EBGaramond-Regular.ttf'],
      ['Montserrat', 'Montserrat-Medium.ttf'],
    ].map(async ([name, file]) => {
      const font = new FontFace(name, `url(${staticFile(`fonts/${file}`)})`);
      await font.load();
      (document.fonts as any).add(font);
    })).then(() => continueRender(fontHandle));
  }, [fontHandle]);

  const margin = portrait ? w * 0.075 : w * 0.11;
  const titleSize = portrait ? 90 : 76;
  const bodySize = portrait ? 62 : 48;
  const smallSize = portrait ? 90 : 48;
  const titleStyle: React.CSSProperties = {
    position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.21 : 0.15),
    fontFamily: serif, fontSize: titleSize, lineHeight: 1.08, color: C.INK,
  };
  const appear = (delay: number) => interpolate(frame, [delay, delay + 12], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const header = <div style={{position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.065 : 0.07), display: 'flex', flexDirection: portrait ? 'column' : 'row', justifyContent: portrait ? 'center' : 'space-between', alignItems: 'center', gap: portrait ? 8 : 0, textAlign: portrait ? 'center' : 'left', fontFamily: sans, fontSize: smallSize, lineHeight: 1.05, color: C.INK}}>
    <span>AI narration: Liam for Deepa</span>{!portrait && <span style={{fontWeight: 700}}>WEEK 1</span>}
  </div>;
  const footer = <div style={{position: 'absolute', left: margin, right: margin, bottom: h * (portrait ? 0.17 : 0.12), display: 'flex', flexDirection: portrait ? 'column' : 'row', justifyContent: portrait ? 'center' : 'space-between', alignItems: 'center', gap: portrait ? 10 : 0, textAlign: 'center', color: C.INK}}>
    <span style={{fontFamily: sans, fontSize: smallSize, fontWeight: 600}}>@HumanitariansAI</span>
    <Img src={staticFile('hai-wordmark-outlined.svg')} style={{width: portrait ? w * 0.32 : w * 0.23, height: 'auto', maxHeight: h * 0.055, objectFit: 'contain', opacity: 0.92}} />
  </div>;
  const title = (text: string) => <div style={titleStyle}>{text}</div>;
  const panel: React.CSSProperties = {background: C.SLATE, border: `2px solid ${C.SLATE}`, borderRadius: 18, boxShadow: '0 16px 36px rgba(47,42,38,0.12)', display: 'flex', justifyContent: 'center', alignItems: 'center', textAlign: 'center', padding: portrait ? 24 : 22};
  const tile = (text: string, index: number, surface: string = C.TEAL, height?: number) => <div key={text} style={{...panel, background: surface, borderTop: `8px solid ${C.CREAM}`, opacity: appear(7 + index * 8), transform: `translateY(${(1 - appear(7 + index * 8)) * 18}px)`, fontFamily: sans, fontWeight: 600, fontSize: bodySize, color: '#FFFFFF', minHeight: height ?? (portrait ? 170 : 180)}}>{text}</div>;
  const main: React.ReactNode = (() => {
    if (beat === 'B00') {
      return <>
        <div style={{position: 'absolute', inset: 0, transform: `translateY(${portrait ? -h * 0.035 : -h * 0.015}px) scale(${portrait ? 0.9 : 0.92})`}}>
          <ClaudeComposerAsk {...claudeComposerAskSchema.parse({
            command: 'Introduce Deepa and her first-week Humanitarians AI focus',
            topic: 'HUMANITARIANS AI', segment: 'Week 1 Progress / Introduction', greeting: 'Hi, Deepa',
            runningText: 'preparing a first progress update', output: ['Technical background', 'Learning Brutalist film-as-code'],
            folderLabel: '@HumanitariansAI', modelLabel: 'Illustrated interface', effortLabel: '',
            placeholder: '', animateTyping: true, largeText: true,
          })}/>
        </div>
      </>;
    }
    if (beat === 'B01') {
      const items = ['Information systems', 'Data engineering', 'Data analytics', 'Business intelligence'];
      return <>{title('My Background')}<div style={{position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.34 : 0.38), display: 'grid', gridTemplateColumns: portrait ? '1fr' : 'repeat(4, 1fr)', gap: portrait ? 20 : 24}}>{items.map((x, i) => tile(x, i))}</div></>;
    }
    if (beat === 'B02') {
      const tools = ['Python', 'SQL', 'Snowflake', 'Power BI', 'Tableau'];
      return <>{title('Tools I Have Worked With')}<div style={{position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.32 : 0.39), display: 'grid', gridTemplateColumns: portrait ? 'repeat(2, 1fr)' : 'repeat(5, 1fr)', gap: portrait ? 22 : 24}}>{tools.map((x, i) => tile(x, i, i % 2 ? C.SLATE : C.TEAL))}</div></>;
    }
    if (beat === 'B03') {
      const work = ['Data pipelines', 'Analytics solutions', 'Dashboards'];
      return <>{title('Data Work')}<div style={{position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.34 : 0.38), display: 'grid', gridTemplateColumns: portrait ? '1fr' : 'repeat(3, 1fr)', gap: portrait ? 25 : 32}}>{work.map((x, i) => tile(x, i, i === 1 ? C.SLATE : C.TEAL))}</div></>;
    }
    if (beat === 'B04') {
      return <>{title('Learning with Humanitarians AI')}<div style={{position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.38 : 0.42), display: 'flex', flexDirection: portrait ? 'column' : 'row', gap: portrait ? 32 : 40, alignItems: 'stretch'}}>
        <div style={{...panel, flex: 1, minHeight: portrait ? 270 : 310, background: C.SLATE, color: '#FFFFFF', fontFamily: serif, fontSize: portrait ? 76 : 72, lineHeight: 1.05}}>Humanitarians<br/>AI</div>
        <div style={{...panel, flex: 1, minHeight: portrait ? 270 : 310, background: C.TEAL, color: '#FFFFFF', borderLeft: `10px solid ${C.CRIMSON}`, fontFamily: sans, fontSize: bodySize, lineHeight: 1.3}}>Educational<br/>STEM + AI content</div>
      </div></>;
    }
    if (beat === 'B05') {
      const steps = ['Structured planning', 'Narration', 'Visual storytelling', 'Human review', 'Programmatic production'];
      return <>{title('Learning the Workflow')}<div style={{position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.28 : 0.40), display: 'grid', gridTemplateColumns: portrait ? '1fr' : 'repeat(5, 1fr)', gap: portrait ? 10 : 18}}>{steps.map((x, i) => tile(x, i, i === 3 ? C.CRIMSON : C.TEAL, portrait ? 150 : undefined))}</div></>;
    }
    if (beat === 'B06') {
      const steps = ['Technical background', 'Brutalist workflow', 'Clear STEM + AI explanations'];
      return <>{title('My Current Focus')}<div style={{position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.34 : 0.40), display: 'grid', gridTemplateColumns: portrait ? '1fr' : 'repeat(3, 1fr)', gap: portrait ? 26 : 30}}>{steps.map((x, i) => tile(x, i, i === 2 ? C.CRIMSON : C.TEAL))}</div></>;
    }
    if (beat === 'B07') {
      return <>{title('The Beginning')}<div style={{position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.36 : 0.4), fontFamily: serif, fontSize: portrait ? 88 : 68, lineHeight: 1.2, textAlign: 'center', opacity: appear(8)}}>This is the beginning of my work with Humanitarians AI, and I look forward to sharing what I learn and build along the way.</div><div style={{position: 'absolute', left: margin, right: margin, top: h * (portrait ? 0.72 : 0.74), fontFamily: sans, fontSize: portrait ? 72 : bodySize, textAlign: 'center', fontWeight: 700}}>Deepa Shenoy</div></>;
    }
    if (beat === 'B08') {
      return <div style={{position: 'absolute', inset: 0, background: portrait ? C.CREAM : C.SLATE, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
        <div style={{width: '82%', height: '78%', background: C.CREAM, border: portrait ? `4px solid ${C.SLATE}` : 'none', borderRadius: 24, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', textAlign: 'center', padding: portrait ? 36 : 30, boxSizing: 'border-box'}}>
          <div style={{fontFamily: sans, fontSize: smallSize, fontWeight: 700, color: C.TEAL, marginBottom: h * 0.035}}>HUMANITARIANS AI</div>
          <div style={{fontFamily: serif, fontSize: portrait ? 92 : 112, lineHeight: 1.08, color: C.INK, maxWidth: '100%'}}>Week 1 Progress<br/>/ Introduction</div>
          <div style={{fontFamily: serif, fontSize: portrait ? 78 : 84, marginTop: h * 0.035, color: C.INK}}>Deepa Shenoy</div>
          <div style={{fontFamily: sans, fontSize: smallSize, marginTop: 18, color: C.INK}}>AI narration: Liam for Deepa</div>
          {!portrait && <Img src={staticFile('hai-wordmark-outlined.svg')} style={{width: w * 0.38, height: 'auto', marginTop: h * 0.035}} />}
          <div style={{fontFamily: sans, fontSize: smallSize, fontWeight: 700, color: C.TEAL, marginTop: h * (portrait ? 0.055 : 0.025)}}>@HumanitariansAI</div>
        </div>
      </div>;
    }
    return <div style={{...titleStyle}}>Week 1 Progress / Introduction</div>;
  })();

  return <AbsoluteFill style={{backgroundColor: beat === 'B00' ? '#F2F0E9' : beat === 'B08' && !portrait ? C.SLATE : C.CREAM, color: C.INK, fontFamily: serif}}>
    {main}
    {beat !== 'B00' && beat !== 'B08' && <>{header}{footer}</>}
  </AbsoluteFill>;
};
