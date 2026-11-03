import React, {useEffect, useState} from 'react';
import {AbsoluteFill, Img, staticFile, delayRender, continueRender, useCurrentFrame, useVideoConfig, interpolate} from 'remotion';
import {z} from 'zod';
import {HUMANITARIANS as C} from '../tokens/humanitarians';

export const deepaRagSchema=z.object({beat:z.string(),frames:z.number(),audit:z.boolean().optional()});
const CREAM=C.CREAM, INK=C.INK, TEAL=C.TEAL, NAVY=C.SLATE, ORANGE=C.CRIMSON, PAPER='#FFFCF5', GOLD=C.GOLD;

/** Animated, source-first RAG diagrams with independently responsive native layouts. */
export const DeepaRagExplainer:React.FC<z.infer<typeof deepaRagSchema>>=({beat,frames,audit=false})=>{
 const f=useCurrentFrame();const {width:w,height:h}=useVideoConfig();const p=h>w;const unit=p?w/1080:w/1920;
 const [gate]=useState(()=>delayRender('HAI typography and RAG layout'));
 useEffect(()=>{Promise.all([['EB Garamond','EBGaramond-Regular.ttf'],['Montserrat','Montserrat-Medium.ttf']].map(async([name,file])=>{const face=new FontFace(name,`url(${staticFile('fonts/'+file)})`);await face.load();(document.fonts as any).add(face);})).then(()=>requestAnimationFrame(()=>requestAnimationFrame(()=>{
  if(audit){const root=document.querySelector('[data-rag-root]')!;const rr=root.getBoundingClientRect();const sx=w/rr.width,sy=h/rr.height;const rows=Array.from(root.querySelectorAll('[data-qc]')).map((el)=>{const r=el.getBoundingClientRect(),s=getComputedStyle(el);return {text:el.textContent,x:(r.x-rr.x)*sx,y:(r.y-rr.y)*sy,w:r.width*sx,h:r.height*sy,font:parseFloat(s.fontSize),color:s.color,scrollOverflow:(el as HTMLElement).scrollWidth>(el as HTMLElement).clientWidth+2};});console.log('RAG_QC '+JSON.stringify({beat,portrait:p,width:w,height:h,rows}));}
  continueRender(gate);
 })));},[gate]);
 const serif='EB Garamond, Georgia, serif', sans='Montserrat, Arial, sans-serif';
 const appear=(step:number)=>interpolate(f,[Math.floor(frames*step),Math.floor(frames*step)+12],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 const text=(s:string,size:number,color=INK,extra:React.CSSProperties={})=><div data-qc style={{fontFamily:serif,fontSize:size*unit,lineHeight:1.13,color,overflowWrap:'break-word',...extra}}>{s}</div>;
 const label=(s:string,color=NAVY,extra:React.CSSProperties={})=><div data-qc style={{fontFamily:sans,fontWeight:500,fontSize:(p?27:23)*unit,lineHeight:1.18,color,letterSpacing:'.035em',...extra}}>{s}</div>;
 const panel=(children:React.ReactNode,step=0,extra:React.CSSProperties={})=><div style={{boxSizing:'border-box',padding:(p?28:30)*unit,border:`${2.5*unit}px solid ${NAVY}`,borderRadius:15*unit,background:PAPER,opacity:appear(step),transform:`translateY(${(1-appear(step))*12*unit}px)`,...extra}}>{children}</div>;
 const pill=(s:string,color=TEAL,extra:React.CSSProperties={})=><div style={{padding:`${10*unit}px ${18*unit}px`,border:`${2*unit}px solid ${color}`,borderRadius:999*unit,color,fontFamily:sans,fontSize:(p?25:21)*unit,fontWeight:500,textAlign:'center',...extra}}>{s}</div>;
 const arrow=(vertical=false,color=TEAL)=><div aria-hidden style={{height:vertical?42*unit:4*unit,width:vertical?4*unit:48*unit,background:color,borderRadius:8*unit,position:'relative'}}><div style={vertical?{position:'absolute',left:-5*unit,bottom:-1*unit,width:12*unit,height:12*unit,borderRight:`${3*unit}px solid ${color}`,borderBottom:`${3*unit}px solid ${color}`,transform:'rotate(45deg)'}:{position:'absolute',right:-1*unit,top:-5*unit,width:12*unit,height:12*unit,borderRight:`${3*unit}px solid ${color}`,borderTop:`${3*unit}px solid ${color}`,transform:'rotate(45deg)'}}/></div>;
 const documentCard=(title:string,sub:string,selected=false,step=0)=><div style={{opacity:appear(step),boxSizing:'border-box',padding:(p?20:18)*unit,border:`${2*unit}px solid ${selected?TEAL:NAVY}`,borderRadius:12*unit,background:selected?'#E6F0EA':PAPER,minHeight:(p?120:102)*unit}}><div style={{width:34*unit,height:5*unit,background:selected?TEAL:NAVY,marginBottom:11*unit,borderRadius:4*unit}}/>{label(title,selected?TEAL:NAVY)}{text(sub,p?27:22,INK,{marginTop:7*unit})}</div>;
 const model=(small=false,step=0)=><div style={{opacity:appear(step),boxSizing:'border-box',padding:(p?23:21)*unit,border:`${3*unit}px solid ${TEAL}`,borderRadius:18*unit,background:'#E4EFEB',textAlign:'center'}}><div style={{display:'flex',justifyContent:'center',gap:6*unit,marginBottom:12*unit}}>{[0,1,2,3].map(i=><span key={i} style={{width:9*unit,height:9*unit,borderRadius:'50%',background:[NAVY,TEAL,ORANGE,GOLD][i]}}/>)}</div>{label('LANGUAGE MODEL',TEAL)}{!small&&text('Generate',p?36:30,INK,{marginTop:5*unit})}</div>;
 const title=(s:string)=><div style={{position:'absolute',left:w*.08,right:w*.08,top:h*(p?.155:.16)}}>{text(s,p?68:77,INK,{fontWeight:600})}</div>;
 const content:React.ReactNode=(()=>{
  switch(beat){
   case 'B00': return <>
    <div style={{position:'absolute',left:w*.08,right:w*.08,top:h*(p?.19:.17)}}>{text('How RAG Gives AI',p?80:100,INK,{fontWeight:600})}{text('Access to External Knowledge',p?72:92,TEAL,{fontWeight:600})}</div>
    <div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.48:.54),display:'flex',flexDirection:p?'column':'row',alignItems:'center',justifyContent:'space-between',gap:18*unit}}>{panel(<>{label('USER QUESTION')}{text('What is our remote-work policy?',p?37:34,INK,{marginTop:7*unit})}</>,.12,{width:p?'100%':'31%'})}{arrow(p)}{panel(<>{label('RETRIEVE')}{text('Find the right source',p?37:34,INK,{marginTop:7*unit})}</>,.3,{width:p?'100%':'28%'})}{arrow(p)}{panel(<>{label('GENERATE')}{text('Grounded response',p?37:34,INK,{marginTop:7*unit})}</>,.48,{width:p?'100%':'31%'})}</div>
    <div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.85:.81)}}>{label('Deepa Shenoy  ·  AI narration: Liam for Deepa',NAVY)}</div>
   </>;
   case 'B01': return <>{title('Why bring in outside knowledge?')}
    <div style={{position:'absolute',left:w*.08,right:w*.08,top:h*(p?.31:.38),display:'flex',flexDirection:p?'column':'row',alignItems:'center',justifyContent:'space-between',gap:24*unit}}>
     {panel(<>{label('ALREADY LEARNED')}{text('Patterns in training data',p?39:37,INK,{marginTop:12*unit})}</>,.05,{width:p?'100%':'34%'})}{arrow(p)}{model(false,.2)}{arrow(p)}{panel(<>{label('MAY BE MISSING',ORANGE)}{text('Specific · current · private',p?37:35,INK,{marginTop:12*unit})}</>,.36,{width:p?'100%':'34%',borderColor:ORANGE})}
    </div><div style={{position:'absolute',left:w*.12,right:w*.12,top:h*(p?.79:.75),textAlign:'center'}}>{label('A MODEL USES LEARNED PARAMETERS + THE CONTEXT IT RECEIVES',NAVY)}</div>
   </>;
   case 'B02': return <>{title('A question about company policy')}
    <div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.31:.37),display:'flex',flexDirection:p?'column':'row',alignItems:'stretch',gap:24*unit}}>
     {panel(<>{label('EMPLOYEE ASKS')}{text('“What is our company’s remote-work policy?”',p?49:46,INK,{marginTop:14*unit})}</>,.05,{flex:1})}
     {!p&&arrow(false,NAVY)}
     {panel(<><div style={{fontSize:48*unit,marginBottom:8*unit}}>▤</div>{label('APPROVED KNOWLEDGE BASE',TEAL)}{text('Company policy documents',p?34:31,INK,{marginTop:10*unit})}</>,.24,{flex:1,borderColor:TEAL})}
    </div>{p&&<div style={{position:'absolute',left:'48%',top:h*.58}}>{arrow(true,NAVY)}</div>}
    <div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.76:.70),textAlign:'center'}}>{pill('FICTIONAL EXAMPLE',ORANGE,{display:'inline-block'})}</div>
   </>;
   case 'B03': return <>{title('First: retrieve relevant information')}
    <div style={{position:'absolute',left:w*.08,right:w*.08,top:h*(p?.29:.34),display:'flex',flexDirection:p?'column':'row',alignItems:'center',gap:19*unit}}>
     <div style={{display:'grid',gridTemplateColumns:p?'1fr':'repeat(3,1fr)',gap:12*unit,width:p?'100%':'51%'}}>{documentCard('Benefits guide','General benefits',false,.02)}{documentCard('Remote work','Fictional policy section',false,.12)}{documentCard('Travel rules','Expenses',false,.2)}</div>
     {arrow(p)}
     <div style={{width:p?'100%':'39%'}}>{panel(<>{label('RETRIEVED PASSAGE',TEAL)}{text('Eligible employees may work remotely up to two days each week.',p?40:36,INK,{marginTop:14*unit,background:'#F3EBDD',padding:12*unit,borderLeft:`${6*unit}px solid ${GOLD}`})}</>,.38,{borderColor:TEAL})}</div>
    </div><div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.84:.78),textAlign:'center'}}>{label('FICTIONAL POLICY EXAMPLE  ·  SEARCH BEFORE GENERATION',NAVY)}</div>
   </>;
   case 'B04': return <>{title('Then: add the passage as context')}
    <div style={{position:'absolute',left:w*.09,right:w*.09,top:h*(p?.29:.34),display:'flex',flexDirection:p?'column':'row',alignItems:'center',gap:19*unit}}>
     {panel(<>{label('QUESTION',NAVY)}{text('Remote-work policy?',p?39:35,INK,{marginTop:8*unit})}</>,.04,{flex:1})}{!p&&arrow(false)}
     {panel(<>{label('RETRIEVED CONTEXT',TEAL)}{text('Up to two days each week',p?36:33,INK,{marginTop:8*unit})}</>,.18,{flex:1,borderColor:TEAL})}{arrow(p)}
     <div style={{width:p?'100%':'31%'}}>{model(false,.34)}</div>
    </div><div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.78:.73),textAlign:'center'}}>{pill('QUESTION  +  SOURCE TEXT  →  MODEL INPUT',TEAL,{display:'inline-block'})}</div>
   </>;
   case 'B05': return <>{title('Finally: generate from the retrieved source')}
    <div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.30:.36),display:'flex',flexDirection:p?'column':'row',alignItems:'center',justifyContent:'center',gap:24*unit}}>{model(false,.04)}{arrow(p)}
     {panel(<>{label('FICTIONAL RESPONSE',TEAL)}{text('The policy allows eligible employees to work remotely up to two days each week.',p?43:40,INK,{marginTop:14*unit})}<div style={{marginTop:16*unit,paddingTop:12*unit,borderTop:`${2*unit}px solid ${TEAL}`}}>{label('Assuming that is what the policy says.',NAVY)}</div></>,.2,{width:p?'100%':'59%',borderColor:TEAL})}
    </div><div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.81:.78),textAlign:'center'}}>{label('THE SOURCE PASSAGE ARRIVES BEFORE THE ANSWER',NAVY)}</div>
   </>;
   case 'B06': return <>{title('Retrieval-Augmented Generation')}
    <div style={{position:'absolute',left:w*.09,right:w*.09,top:h*(p?.27:.34),display:'flex',flexDirection:p?'column':'row',alignItems:'center',justifyContent:'space-between',gap:18*unit}}>{[['01','RETRIEVE','Find relevant information'],['02','AUGMENT','Add it to context'],['03','GENERATE','Compose a response']].map((a,i)=><React.Fragment key={a[0]}>{panel(<>{label(a[0],TEAL)}{text(a[1],p?42:37,NAVY,{fontFamily:sans,fontWeight:500,marginTop:8*unit})}{text(a[2],p?35:30,INK,{marginTop:7*unit})}</>,.02+i*.16,{flex:1,width:p?'100%':'31%',borderColor:i===1?TEAL:NAVY})}{i<2&&arrow(p)}</React.Fragment>)}</div>
    <div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.81:.76),display:'flex',flexDirection:p?'column':'row',justifyContent:'center',alignItems:'center',gap:12*unit}}>{pill('DOCUMENTS  ·  DATABASES  ·  OTHER APPROVED SOURCES',TEAL)}{pill('NO PER-QUESTION RETRAINING',NAVY)}</div>
   </>;
   case 'B07': return <>{title('Grounding helps. It is not a guarantee.')}
    <div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.32:.39),display:'flex',flexDirection:p?'column':'row',alignItems:'stretch',gap:22*unit}}>
     {panel(<>{label('RETRIEVED EVIDENCE',TEAL)}{text('Relevant context can support an answer.',p?38:35,INK,{marginTop:12*unit})}</>,.05,{flex:1,borderColor:TEAL})}
     {panel(<>{label('STILL CAN GO WRONG',ORANGE)}{text('Missed results · weak or outdated sources',p?35:33,INK,{marginTop:12*unit})}{text('RAG does not eliminate hallucinations.',p?35:32,ORANGE,{marginTop:10*unit})}</>,.24,{flex:1,borderColor:ORANGE})}
    </div><div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.75:.72),textAlign:'center'}}>{label('RETRIEVAL QUALITY + SOURCE QUALITY MATTER',NAVY)}</div>
   </>;
   default: return <>
    <div style={{position:'absolute',left:w*.09,right:w*.09,top:h*(p?.22:.2)}}>{text('How RAG Gives AI',p?81:98,INK,{fontWeight:600})}{text('Access to External Knowledge',p?67:88,TEAL,{fontWeight:600})}</div>
    <div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.59:.62),display:'flex',flexDirection:p?'column':'row',alignItems:p?'flex-start':'center',justifyContent:'space-between',gap:22*unit}}>{text('Deepa Shenoy',p?44:39,INK)}{label('AI narration: Liam for Deepa',NAVY)}
    </div>
    <div style={{position:'absolute',left:w*.1,right:w*.1,top:h*(p?.77:.82),display:'flex',flexDirection:p?'column':'row',alignItems:p?'flex-start':'center',justifyContent:'space-between',gap:18*unit}}>{text('@HumanitariansAI',p?36:28,INK,{fontFamily:sans})}<Img src={staticFile('hai-wordmark-outlined.svg')} style={{width:(p?270:260)*unit,height:(p?45:38)*unit,objectFit:'contain',objectPosition:'left'}}/></div>
   </>;
  }
 })();
 const headerTop=h*(p?.065:.065), footerTop=h*(p?.91:.91);
 return <AbsoluteFill data-rag-root style={{background:CREAM,color:INK,fontFamily:serif,overflow:'hidden'}}>
  <div style={{position:'absolute',left:w*.08,right:w*.08,top:headerTop,display:'flex',justifyContent:'space-between',alignItems:'center'}}>{text('Deepa Shenoy',p?31:27,NAVY)}{label('WEEK 3  ·  STEM / AI',TEAL)}</div>
  {content}
  {beat!=='B08'&&<div style={{position:'absolute',left:w*.08,right:w*.08,top:footerTop,display:'flex',flexDirection:p?'column':'row',alignItems:p?'flex-start':'center',justifyContent:'space-between',gap:8*unit}}>{text('@HumanitariansAI',p?28:23,INK,{fontFamily:sans})}<Img src={staticFile('hai-wordmark-outlined.svg')} style={{width:(p?220:230)*unit,height:35*unit,objectFit:'contain',objectPosition:'left'}}/></div>}
 </AbsoluteFill>;
};
