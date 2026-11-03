import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Img, staticFile, delayRender, continueRender, useCurrentFrame, useVideoConfig, interpolate} from 'remotion';
import {z} from 'zod';
import {HUMANITARIANS as C} from '../tokens/humanitarians';

export const deepaHallucinationsSchema = z.object({beat: z.string(), frames: z.number()});
type Props = z.infer<typeof deepaHallucinationsSchema>;
const SERIF = 'EB Garamond, Georgia, serif';
const SANS = 'Montserrat, Arial, sans-serif';

/** HAI-native visual results and title card for Deepa's hallucination explainer. */
export const DeepaHallucinations: React.FC<Props> = ({beat}) => {
  const frame = useCurrentFrame();
  const {width: w, height: h, fps} = useVideoConfig();
  const portrait = h > w;
  const [fontGate] = useState(() => delayRender('Load Humanitarians AI fonts'));
  useEffect(() => {
    Promise.all([
      ['EB Garamond', 'EBGaramond-Regular.ttf'],
      ['Montserrat', 'Montserrat-Medium.ttf'],
    ].map(async ([name, file]) => {
      const face = new FontFace(name, `url(${staticFile(`fonts/${file}`)})`);
      await face.load();
      (document.fonts as any).add(face);
    })).then(() => continueRender(fontGate));
  }, [fontGate]);

  const appear = (offset = 0) => interpolate(frame - offset, [0, Math.max(8, fps * 0.45)], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const side = w * 0.085;
  const bodySize = h * (portrait ? 0.030 : 0.034);
  const titleSize = h * (portrait ? 0.049 : 0.057);
  const footerY = h * 0.925;
  const titleStyle: React.CSSProperties = {position: 'absolute', left: side, right: side, top: h * (portrait ? 0.075 : 0.085), fontFamily: SERIF, fontSize: titleSize, lineHeight: 1.08, color: C.INK, fontWeight: 600};
  const labelStyle: React.CSSProperties = {fontFamily: SANS, fontSize: h * (portrait ? 0.023 : 0.022), lineHeight: 1.4, color: C.INK};
  const footer = <div style={{position: 'absolute', left: side, right: side, top: footerY, display: 'flex', justifyContent: 'space-between', alignItems: 'center', color: C.INK, fontFamily: SERIF, fontSize: h * (portrait ? 0.026 : 0.029)}}><span>@HumanitariansAI</span><Img src={staticFile('hai-wordmark-outlined.svg')} style={{width: w * (portrait ? 0.29 : 0.22), height: 'auto', maxHeight: h * 0.055, objectFit: 'contain'}} /></div>;
  const source = (text: string) => <div style={{position: 'absolute', left: side, right: side, top: h * 0.855, ...labelStyle, fontSize: h * (portrait ? 0.018 : 0.019), color: '#57504A'}}>{text}</div>;
  const card: React.CSSProperties = {background: '#FFFCF5', border: `2px solid ${C.INK}`, borderRadius: 12, boxShadow: '0 10px 30px rgba(47,42,38,.08)'};

  if (beat === 'B03') {
    const nodes = [
      {head: 'LEARNED PATTERNS', text: 'Words and contexts from training'},
      {head: 'NEXT TOKEN', text: 'Continue one piece at a time'},
      {head: 'FLUENT ANSWER', text: 'Can be plausible and still false'},
    ];
    return <AbsoluteFill style={{background: C.CREAM, color: C.INK, fontFamily: SERIF}}>
      <div style={titleStyle}>How a hallucination can happen</div>
      <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.20 : 0.245), padding: `${h * 0.022}px ${w * 0.035}px`, ...card, opacity: appear(0)}}>
        <div style={{...labelStyle, color: C.SLATE, fontWeight: 700}}>A hallucination</div>
        <div style={{fontFamily: SERIF, fontSize: h * (portrait ? 0.036 : 0.041), lineHeight: 1.2, marginTop: h * 0.012}}>A fluent answer with false or unsupported information.</div>
      </div>
      <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.40 : 0.48), display: 'flex', flexDirection: portrait ? 'column' : 'row', alignItems: 'stretch', gap: portrait ? h * 0.012 : w * 0.022}}>
        {nodes.map((n, i) => <div key={n.head} style={{...card, flex: 1, padding: `${h * (portrait ? 0.012 : 0.021)}px ${w * 0.023}px`, opacity: appear(9 + i * 10), borderTop: `7px solid ${i === 2 ? C.CRIMSON : C.TEAL}`}}>
          <div style={{...labelStyle, fontSize: h * (portrait ? 0.020 : 0.022), fontWeight: 700, color: i === 2 ? C.CRIMSON : C.TEAL}}>{n.head}</div>
          <div style={{fontFamily: SERIF, fontSize: h * (portrait ? 0.024 : 0.034), lineHeight: 1.2, marginTop: h * (portrait ? 0.004 : 0.012)}}>{n.text}</div>
        </div>)}
      </div>
      <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.74 : 0.72), textAlign: 'center', fontFamily: SERIF, fontSize: h * (portrait ? 0.028 : 0.035), color: C.INK}}>No automatic trusted-source check in ordinary generation.</div>
      {source('Sources: NIST AI 600-1 §2.2 · Brown et al., 2020')}{footer}
    </AbsoluteFill>;
  }

  if (beat === 'B05') {
    return <AbsoluteFill style={{background: C.CREAM, color: C.INK, fontFamily: SERIF}}>
      <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.075 : 0.08), fontFamily: SANS, fontWeight: 700, fontSize: h * (portrait ? 0.025 : 0.026), letterSpacing: 2, color: C.CRIMSON}}>FICTIONAL EXAMPLE</div>
      <div style={{...titleStyle, top: h * (portrait ? 0.125 : 0.14)}}>A confident answer is not evidence</div>
      <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.28 : 0.34), display: 'flex', flexDirection: portrait ? 'column' : 'row', gap: portrait ? h * 0.027 : w * 0.035, alignItems: 'stretch'}}>
        <div style={{...card, flex: 1, padding: `${h * (portrait ? 0.018 : 0.032)}px ${w * 0.035}px`, opacity: appear(0)}}>
          <div style={{...labelStyle, color: C.SLATE, fontWeight: 700}}>QUESTION</div>
          <div style={{fontSize: h * (portrait ? 0.039 : 0.046), lineHeight: 1.2, marginTop: h * 0.018}}>“What is the capital of Bellora?”</div>
          <div style={{...labelStyle, marginTop: h * 0.022}}>Bellora — fictional place</div>
        </div>
        <div style={{...card, flex: 1, padding: `${h * (portrait ? 0.018 : 0.032)}px ${w * 0.035}px`, opacity: appear(12), borderColor: C.CRIMSON}}>
          <div style={{...labelStyle, color: C.CRIMSON, fontWeight: 700}}>CONFIDENT-SOUNDING ANSWER</div>
          <div style={{fontSize: h * (portrait ? 0.055 : 0.066), lineHeight: 1.1, marginTop: h * 0.018, color: C.CRIMSON}}>“Lumen.”</div>
          <div style={{...labelStyle, marginTop: h * 0.022}}>Lumen — fictional answer</div>
        </div>
      </div>
      <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.77 : 0.68), ...card, padding: `${h * (portrait ? 0.007 : 0.02)}px ${w * 0.03}px`, textAlign: 'center', opacity: appear(24), background: '#F7E6DD', borderColor: C.CRIMSON, fontFamily: SANS, fontSize: h * (portrait ? 0.020 : 0.028), fontWeight: 700}}>{portrait ? 'IF BELIEVED → it could affect a decision' : 'IF BELIEVED → a false detail could influence a decision'}</div>
      {source('Illustrative scenario invented for this video · Risk framing: NIST AI 600-1 §2.2')}{footer}
    </AbsoluteFill>;
  }

  if (beat === 'B07') {
    const actions = [
      ['VERIFY', 'Verify claims'],
      ['SOURCE', 'Use reliable sources'],
      ['CONTEXT', 'Add useful context'],
      ['RETRIEVE', 'Retrieve evidence'],
    ];
    return <AbsoluteFill style={{background: C.CREAM, color: C.INK, fontFamily: SERIF}}>
      <div style={titleStyle}>Reduce risk. Keep checking.</div>
      <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.24 : 0.28), display: 'grid', gridTemplateColumns: '1fr 1fr', gridTemplateRows: 'auto auto', gap: h * (portrait ? 0.023 : 0.028)}}>
        {actions.map(([head, text], i) => <div key={head} style={{...card, padding: `${h * (portrait ? 0.027 : 0.021)}px ${w * 0.03}px`, opacity: appear(i * 8), borderLeft: `8px solid ${i === 3 ? C.SLATE : C.TEAL}`}}>
          <div style={{...labelStyle, fontWeight: 700, color: i === 3 ? C.SLATE : C.TEAL}}>{head}</div>
          <div style={{fontSize: h * (portrait ? 0.025 : 0.038), lineHeight: 1.2, marginTop: h * 0.01}}>{text}</div>
        </div>)}
      </div>
      <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.70 : 0.70), textAlign: 'center', fontFamily: SERIF, fontSize: h * (portrait ? 0.029 : 0.036), color: C.CRIMSON}}>These steps can reduce risk; they cannot guarantee truth.</div>
      {source('Retrieval approach: Lewis et al., 2020 · Limitations: NIST AI 600-1 §2.2')}{footer}
    </AbsoluteFill>;
  }

  // B09 — HAI title-restating end card.
  return <AbsoluteFill style={{background: C.CREAM, color: C.INK, fontFamily: SERIF}}>
    <div style={{position: 'absolute', left: side, right: side, top: h * 0.16, textAlign: 'center', fontFamily: SANS, fontWeight: 700, letterSpacing: 3, fontSize: h * (portrait ? 0.028 : 0.027), color: C.SLATE, opacity: appear(0)}}>HUMANITARIANS AI</div>
    <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.30 : 0.28), textAlign: 'center', fontFamily: SERIF, fontSize: h * (portrait ? 0.068 : 0.078), lineHeight: 1.05, fontWeight: 600, opacity: appear(6)}}>How AI<br/>Hallucinations<br/>Happen</div>
    <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.61 : 0.64), textAlign: 'center', fontFamily: SERIF, fontSize: h * (portrait ? 0.044 : 0.045), opacity: appear(12)}}>Deepa Shenoy</div>
    <div style={{position: 'absolute', left: side, right: side, top: h * (portrait ? 0.69 : 0.72), textAlign: 'center', fontFamily: SANS, fontSize: h * (portrait ? 0.024 : 0.025), opacity: appear(15)}}>AI narration: Liam for Deepa</div>
    <div style={{position: 'absolute', left: side, right: side, top: h * 0.82, display: 'flex', justifyContent: 'center'}}><Img src={staticFile('hai-wordmark-outlined.svg')} style={{width: w * (portrait ? 0.44 : 0.28), height: 'auto', maxHeight: h * 0.07, objectFit: 'contain', opacity: appear(18)}} /></div>
    <div style={{position: 'absolute', left: side, right: side, top: h * 0.92, textAlign: 'center', fontFamily: SERIF, fontSize: h * (portrait ? 0.027 : 0.029)}}>@HumanitariansAI</div>
  </AbsoluteFill>;
};
