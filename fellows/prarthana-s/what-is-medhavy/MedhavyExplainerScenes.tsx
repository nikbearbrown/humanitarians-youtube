import React from 'react';
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {z} from 'zod';
import {MEDHAVY_SERIES as T, SERIES, typography} from './medhavySeriesTheme';

export const medhavyExplainerSchema = z.object({
  sparkLine: z.string().default(''),
  visualBrief: z.string().optional(),
  onScreenText: z.array(z.string()).default([]),
  badge: z.string().optional(),
});
export type MedhavyExplainerProps = z.infer<typeof medhavyExplainerSchema>;

const clamp = (v: number) => Math.max(0, Math.min(1, v));
const ease = (frame: number, a: number, b: number) =>
  interpolate(frame, [a, b], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

const stageOpacity = (frame: number, start: number, end: number, fadeFrames = 8) => {
  if (frame < start || frame > end) return 0;
  const fadeIn = ease(frame, start, start + fadeFrames);
  const fadeOut = 1 - ease(frame, end - fadeFrames, end);
  return clamp(Math.min(fadeIn, fadeOut));
};

const Pop: React.FC<{children: React.ReactNode; delay?: number; style?: React.CSSProperties}> = ({
  children,
  delay = 0,
  style,
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const s = spring({frame: frame - delay, fps, config: {damping: 16, stiffness: 120, mass: 0.9}});
  return (
    <div
      style={{
        opacity: clamp(s),
        transform: `translateY(${(1 - clamp(s)) * 22}px) scale(${0.96 + 0.04 * clamp(s)})`,
        ...style,
      }}
    >
      {children}
    </div>
  );
};

const PaperTexture: React.FC = () => (
  <>
    <AbsoluteFill
      style={{
        backgroundColor: T.bg,
        backgroundImage:
          `linear-gradient(${T.grid} 1px, transparent 1px), linear-gradient(90deg, ${T.grid} 1px, transparent 1px)`,
        backgroundSize: '42px 42px',
      }}
    />
    <AbsoluteFill
      style={{
        background:
          'radial-gradient(circle at 50% 10%, rgba(255,255,255,0.6), transparent 45%), linear-gradient(180deg, rgba(255,255,255,0.14), rgba(0,0,0,0.02))',
      }}
    />
  </>
);

const ChapterHeader: React.FC<{title: string; sub?: string}> = ({title, sub}) => {
  const frame = useCurrentFrame();
  return (
    <div
      style={{
        position: 'absolute',
        top: 34,
        left: 64,
        right: 64,
        display: 'flex',
        alignItems: 'flex-start',
        justifyContent: 'space-between',
        opacity: ease(frame, 0, 12),
      }}
    >
      <div>
        <div style={{fontFamily: typography.display, fontSize: 16, fontWeight: 800, letterSpacing: '0.14em', color: T.teal}}>
          {SERIES.chapterPrefix} // {SERIES.episode}
        </div>
        <div style={{fontFamily: typography.serif, fontSize: 28, fontWeight: 700, color: T.ink, marginTop: 5}}>
          {title}
        </div>
      </div>
      {sub ? (
        <div style={{fontFamily: typography.display, fontSize: 17, fontWeight: 650, color: T.muted, maxWidth: 560, textAlign: 'right'}}>
          {sub}
        </div>
      ) : null}
    </div>
  );
};

const FooterRule: React.FC = () => (
  <div style={{position: 'absolute', bottom: 31, left: 64, right: 64, height: 1, background: T.line}} />
);

const Shell: React.FC<{title: string; sparkLine: string; children: React.ReactNode; badge?: string}> = ({
  title,
  sparkLine,
  children,
  badge,
}) => (
  <AbsoluteFill style={{overflow: 'hidden', color: T.ink}}>
    <PaperTexture />
    <ChapterHeader title={title} sub={sparkLine} />
    <div style={{position: 'absolute', left: 64, right: 64, top: 115, bottom: 60}}>{children}</div>
    <FooterRule />
    {badge ? (
      <div
        style={{
          position: 'absolute',
          bottom: 50,
          right: 78,
          padding: '8px 14px',
          borderRadius: 999,
          border: `1px solid ${T.gold}`,
          background: T.paper,
          color: T.gold,
          fontFamily: typography.display,
          fontWeight: 800,
          fontSize: 13,
          letterSpacing: '0.05em',
          textTransform: 'uppercase',
        }}
      >
        Vision / Coming Soon
      </div>
    ) : null}
  </AbsoluteFill>
);

const Page: React.FC<{children: React.ReactNode; style?: React.CSSProperties}> = ({children, style}) => (
  <div
    style={{
      background: T.paper,
      border: `1px solid ${T.line}`,
      boxShadow: '0 18px 55px rgba(20,30,28,0.09)',
      borderRadius: 16,
      ...style,
    }}
  >
    {children}
  </div>
);

const H: React.FC<{children: React.ReactNode; color?: string; size?: number}> = ({children, color = T.ink, size = 36}) => (
  <div style={{fontFamily: typography.serif, fontWeight: 700, fontSize: size, lineHeight: 1.08, color}}>{children}</div>
);

const P: React.FC<{children: React.ReactNode; color?: string; size?: number}> = ({children, color = T.muted, size = 21}) => (
  <div style={{fontFamily: typography.display, fontWeight: 500, fontSize: size, lineHeight: 1.42, color}}>{children}</div>
);

const HighlightLine: React.FC<{width?: string; active?: boolean}> = ({width = '80%', active = false}) => (
  <div
    style={{
      height: 12,
      width,
      borderRadius: 3,
      marginBottom: 13,
      background: active ? T.goldSoft : 'rgba(30,43,42,0.12)',
      borderLeft: active ? `5px solid ${T.gold}` : undefined,
    }}
  />
);

const MarginNote: React.FC<{text: string; color?: string}> = ({text, color = T.teal}) => (
  <div
    style={{
      borderLeft: `4px solid ${color}`,
      paddingLeft: 14,
      fontFamily: typography.display,
      fontWeight: 700,
      fontSize: 18,
      color,
      lineHeight: 1.3,
    }}
  >
    {text}
  </div>
);

const Arrow: React.FC<{progress: number; color?: string; width?: number}> = ({progress, color = T.teal, width = 150}) => (
  <div style={{display: 'flex', alignItems: 'center', width, opacity: clamp(progress)}}>
    <div style={{height: 3, flex: 1, background: color, transform: `scaleX(${clamp(progress)})`, transformOrigin: 'left'}} />
    <div style={{width: 0, height: 0, borderTop: '8px solid transparent', borderBottom: '8px solid transparent', borderLeft: `14px solid ${color}`}} />
  </div>
);

const TutorBubble: React.FC<{text: string; accent?: string}> = ({text, accent = T.teal}) => (
  <div style={{background: T.paper, border: `2px solid ${accent}`, borderRadius: 20, padding: '22px 26px', width: 460}}>
    <div style={{fontFamily: typography.display, fontWeight: 800, color: accent, fontSize: 15, letterSpacing: '0.08em', textTransform: 'uppercase'}}>Tutor</div>
    <div style={{fontFamily: typography.display, color: T.ink, fontSize: 21, lineHeight: 1.38, marginTop: 10}}>{text}</div>
  </div>
);

const LabelChip: React.FC<{text: string; color?: string}> = ({text, color = T.teal}) => (
  <div style={{padding: '12px 18px', borderRadius: 999, border: `2px solid ${color}`, background: T.paper, fontFamily: typography.display, fontWeight: 750, fontSize: 18, color}}>
    {text}
  </div>
);

const Book: React.FC<{title?: string; accent?: string}> = ({title = 'Interactive textbook', accent = T.teal}) => (
  <div style={{display: 'flex', alignItems: 'center', gap: 18}}>
    <div style={{width: 100, height: 132, borderRadius: '7px 16px 16px 7px', background: T.paper, border: `3px solid ${T.ink}`, borderLeft: `13px solid ${accent}`, padding: 15}}>
      <div style={{height: 8, background: T.line, marginTop: 18}} />
      <div style={{height: 8, width: '70%', background: T.line, marginTop: 12}} />
      <div style={{height: 8, width: '85%', background: T.line, marginTop: 12}} />
    </div>
    <H size={30}>{title}</H>
  </div>
);

/* B00 — 5 visual moments: book -> chatbot -> tension -> question -> convergence */
export const MedhavyHook: React.FC<MedhavyExplainerProps> = ({sparkLine}) => {
  const f = useCurrentFrame();
  const s1 = stageOpacity(f, 0, 90);
  const s2 = stageOpacity(f, 70, 175);
  const s3 = stageOpacity(f, 155, 255);
  const s4 = stageOpacity(f, 235, 335);
  const s5 = ease(f, 315, 390);

  return (
    <Shell title="What if the book could teach?" sparkLine={sparkLine}>
      <div style={{height: '100%', position: 'relative'}}>
        <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: s1}}>
          <Pop>
            <Page style={{width: 720, padding: 48}}>
              <Book title="A normal digital textbook" accent={T.muted} />
              <div style={{marginTop: 40}}>
                <HighlightLine width="92%" /><HighlightLine width="83%" /><HighlightLine width="76%" /><HighlightLine width="88%" />
              </div>
              <div style={{marginTop: 24}}><MarginNote text="Searchable. Readable. Still static." color={T.muted} /></div>
            </Page>
          </Pop>
        </div>

        <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'space-around', opacity: s2}}>
          <Page style={{width: 620, padding: 42}}>
            <Book title="Textbook" accent={T.muted} />
            <div style={{marginTop: 25}}><P>Course content lives here.</P></div>
          </Page>
          <Page style={{width: 620, padding: 42}}>
            <H size={28} color={T.blue}>Generic AI chatbot</H>
            <div style={{marginTop: 26, display: 'grid', gap: 13}}>
              {['Ask me anything', 'Another unrelated answer', 'More outside context'].map((x) => (
                <div key={x} style={{padding: 14, borderRadius: 12, background: '#EDF2F5', fontFamily: typography.display, color: T.muted, fontSize: 18}}>{x}</div>
              ))}
            </div>
          </Page>
        </div>

        <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: s3}}>
          <div style={{textAlign: 'center'}}>
            <div style={{fontFamily: typography.serif, fontWeight: 800, fontSize: 112, color: T.gold}}>?</div>
            <H size={50}>What if they worked together?</H>
          </div>
        </div>

        <div style={{position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', opacity: s4}}>
          <Page style={{width: 1120, padding: 45}}>
            <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 34}}>
              <Book title="Course content" />
              <Arrow progress={ease(f, 245, 285)} />
              <TutorBubble text="Ask questions without leaving the textbook." />
            </div>
          </Page>
        </div>

        <div style={{position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', opacity: s5}}>
          <div style={{fontFamily: typography.display, fontWeight: 900, fontSize: 82, letterSpacing: '-0.03em', color: T.teal}}>MEDHAVY</div>
          <div style={{marginTop: 20}}><H size={36}>A textbook that teaches back.</H></div>
        </div>
      </div>
    </Shell>
  );
};

/* B01 — page transforms into tutor-enabled textbook */
export const MedhavyBookTutor: React.FC<MedhavyExplainerProps> = ({sparkLine}) => {
  const f = useCurrentFrame();
  return (
    <Shell title="The tutor lives inside" sparkLine={sparkLine}>
      <div style={{height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
        <Page style={{width: 1380, height: 650, padding: 42, display: 'grid', gridTemplateColumns: '1.25fr 0.75fr', gap: 34}}>
          <div style={{borderRight: `1px solid ${T.line}`, paddingRight: 32}}>
            <div style={{opacity: ease(f, 0, 20)}}><Book title="Interactive textbook" /></div>
            <div style={{marginTop: 34}}>
              <HighlightLine width="91%" />
              <HighlightLine width="84%" active={f > 80} />
              <HighlightLine width="77%" />
              <HighlightLine width="88%" />
              <HighlightLine width="68%" />
            </div>
            <div style={{marginTop: 28, opacity: ease(f, 75, 100)}}>
              <MarginNote text="The learning content remains at the center." />
            </div>
          </div>
          <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'center', opacity: ease(f, 55, 95), transform: `translateX(${(1-ease(f,55,95))*60}px)`}}>
            <TutorBubble text="I can explain this passage, give a hint, or ask you a guiding question." />
            <div style={{marginTop: 26}}><LabelChip text="Built-in AI tutor" /></div>
          </div>
        </Page>
      </div>
    </Shell>
  );
};

/* B02 — login -> hub -> books -> tools collapse into one environment */
export const MedhavyHub: React.FC<MedhavyExplainerProps> = ({sparkLine, onScreenText}) => {
  const f = useCurrentFrame();
  const books = onScreenText.length ? onScreenText : ['Physics','Cancer Biology','Quantum Mechanics','Electron Microscopy'];
  return (
    <Shell title="One learning environment" sparkLine={sparkLine}>
      <div style={{height: '100%', position: 'relative'}}>
        <div style={{position: 'absolute', inset: 0, display: 'flex', justifyContent: 'center', alignItems: 'center', opacity: stageOpacity(f,0,120)}}>
          <Page style={{padding: '34px 58px', textAlign: 'center'}}>
            <div style={{fontFamily: typography.display, fontWeight: 800, fontSize: 20, color: T.muted}}>SIGN IN ONCE</div>
            <div style={{marginTop: 12}}><H size={44}>Enter Medhavy</H></div>
          </Page>
        </div>
        <div style={{position: 'absolute', inset: 0, opacity: stageOpacity(f,95,360)}}>
          <div style={{display:'flex', justifyContent:'center', marginTop: 35}}>
            <Page style={{padding:'20px 34px'}}><H size={32}>Medhavy Hub</H></Page>
          </div>
          <div style={{display:'grid', gridTemplateColumns:'repeat(4,1fr)', gap:24, marginTop:70}}>
            {books.slice(0,4).map((b,i)=>(
              <Pop key={b} delay={110+i*18}>
                <Page style={{padding:28, minHeight:230}}>
                  <div style={{height:10, background:[T.blue,T.teal,T.gold,T.lavender][i], borderRadius:99, width:'42%', marginBottom:28}} />
                  <H size={26}>{b}</H>
                  <div style={{marginTop:24}}><P size={17}>Textbook + tutor + learning tools</P></div>
                </Page>
              </Pop>
            ))}
          </div>
        </div>
        <div style={{position:'absolute', inset:0, display:'flex', alignItems:'center', justifyContent:'center', opacity:ease(f,350,430)}}>
          <Page style={{padding:'38px 58px'}}>
            <div style={{display:'flex', gap:18, alignItems:'center'}}>
              {['Textbook','Tutor','Learning tools'].map((x,i)=><LabelChip key={x} text={x} color={[T.blue,T.teal,T.gold][i]} />)}
              <div style={{fontFamily:typography.serif, fontSize:46, margin:'0 10px'}}>→</div>
              <H size={36} color={T.teal}>One environment</H>
            </div>
          </Page>
        </div>
      </div>
    </Shell>
  );
};

/* B03 — prompt sprawl -> knowledge sprawl -> warning */
export const GenericChatbotRisk: React.FC<MedhavyExplainerProps> = ({sparkLine}) => {
  const f = useCurrentFrame();
  return (
    <Shell title="The problem with generic AI" sparkLine={sparkLine}>
      <div style={{height:'100%', position:'relative'}}>
        <div style={{position:'absolute', inset:0, opacity:stageOpacity(f,0,150), display:'flex', alignItems:'center', justifyContent:'center'}}>
          <Page style={{width:980, padding:42}}>
            <H size={34} color={T.blue}>Ask almost anything</H>
            <div style={{display:'grid', gridTemplateColumns:'repeat(3,1fr)', gap:18, marginTop:35}}>
              {['Physics question','Recipe question','Travel question'].map((x,i)=><LabelChip key={x} text={x} color={[T.blue,T.gold,T.lavender][i]} />)}
            </div>
          </Page>
        </div>
        <div style={{position:'absolute', inset:0, opacity:stageOpacity(f,125,315), display:'flex', alignItems:'center', justifyContent:'space-around'}}>
          <div>
            <H size={36}>Huge knowledge space</H>
            <div style={{marginTop:30, width:620, height:360, position:'relative'}}>
              {Array.from({length:18}).map((_,i)=>(
                <div key={i} style={{position:'absolute', left:`${(i*37)%90}%`, top:`${(i*53)%80}%`, width:12+(i%4)*5, height:12+(i%4)*5, borderRadius:999, background:[T.blue,T.gold,T.lavender,T.crimson][i%4], opacity:0.75}} />
              ))}
            </div>
          </div>
          <div style={{fontFamily:typography.serif,fontSize:150,color:T.crimson,fontWeight:900}}>!</div>
        </div>
        <div style={{position:'absolute', inset:0, opacity:ease(f,300,390), display:'flex', alignItems:'center', justifyContent:'center'}}>
          <Page style={{padding:'40px 64px', border:`2px solid ${T.crimson}`}}>
            <H size={44} color={T.crimson}>The answer may not match the course.</H>
          </Page>
        </div>
      </div>
    </Shell>
  );
};

/* B04 — chapter highlight -> question in margin -> grounded tutor -> source trace */
export const GroundedTutor: React.FC<MedhavyExplainerProps> = ({sparkLine}) => {
  const f = useCurrentFrame();
  return (
    <Shell title="Grounded in the book" sparkLine={sparkLine}>
      <div style={{height:'100%', display:'flex', alignItems:'center', justifyContent:'center'}}>
        <Page style={{width:1450, height:690, padding:40, display:'grid', gridTemplateColumns:'1.15fr 0.85fr', gap:38}}>
          <div style={{paddingRight:32, borderRight:`1px solid ${T.line}`}}>
            <H size={30}>Chapter 4 — The concept</H>
            <div style={{marginTop:32}}>
              <HighlightLine width="92%" />
              <HighlightLine width="84%" />
              <HighlightLine width="76%" active={f>60} />
              <HighlightLine width="88%" active={f>115} />
              <HighlightLine width="68%" />
            </div>
            <div style={{marginTop:28, opacity:ease(f,85,115)}}>
              <MarginNote text="Student: I don't understand this part." color={T.gold} />
            </div>
            <div style={{marginTop:32, opacity:ease(f,245,285)}}>
              <MarginNote text="Answer traced back to the chapter." color={T.teal} />
            </div>
          </div>
          <div style={{display:'flex', flexDirection:'column', justifyContent:'center'}}>
            <div style={{opacity:ease(f,130,165)}}><TutorBubble text="Let's stay with this chapter. Here's another way to think about the highlighted passage..." /></div>
            <div style={{marginTop:30, opacity:ease(f,205,240)}}>
              <LabelChip text="Grounded answer" color={T.teal} />
            </div>
            <div style={{marginTop:20, opacity:ease(f,270,310)}}>
              <P size={18} color={T.teal}>SOURCE → Chapter 4, highlighted passage</P>
            </div>
          </div>
        </Page>
      </div>
    </Shell>
  );
};

/* B05 — three mini-teaching modes shown sequentially */
export const LearningPaths: React.FC<MedhavyExplainerProps> = ({sparkLine}) => {
  const f = useCurrentFrame();
  const stages = [
    {start:0,end:150,title:'See it',color:T.blue,body:'A visual diagram makes the idea click.',icon:'◫'},
    {start:125,end:285,title:'Work through it',color:T.teal,body:'Break the concept into clear steps.',icon:'1 → 2 → 3'},
    {start:260,end:420,title:'Be guided',color:T.gold,body:'The tutor asks the right question.',icon:'?'},
  ];
  return (
    <Shell title="Different learners. Different paths." sparkLine={sparkLine}>
      <div style={{height:'100%', position:'relative'}}>
        {stages.map((s)=>(
          <div key={s.title} style={{position:'absolute', inset:0, opacity:stageOpacity(f,s.start,s.end), display:'flex', alignItems:'center', justifyContent:'center'}}>
            <Page style={{width:1200, padding:54}}>
              <div style={{display:'grid', gridTemplateColumns:'0.7fr 1.3fr', gap:60, alignItems:'center'}}>
                <div style={{fontFamily:typography.serif,fontWeight:900,fontSize:s.icon.length>2?66:140,color:s.color,textAlign:'center'}}>{s.icon}</div>
                <div>
                  <H size={50} color={s.color}>{s.title}</H>
                  <div style={{marginTop:22}}><P size={27}>{s.body}</P></div>
                </div>
              </div>
            </Page>
          </div>
        ))}
      </div>
    </Shell>
  );
};

/* B06 — interactions accumulate -> profile -> tutor adapts */
export const LearnerMemory: React.FC<MedhavyExplainerProps> = ({sparkLine}) => {
  const f = useCurrentFrame();
  const interactions = ['Asked for a visual','Needed a smaller step','Answered a guiding question','Revisited the concept'];
  return (
    <Shell title="Learning over time" sparkLine={sparkLine}>
      <div style={{height:'100%', display:'grid', gridTemplateColumns:'1fr 1fr', gap:60, alignItems:'center'}}>
        <div>
          <H size={36}>Interactions accumulate</H>
          <div style={{marginTop:30, display:'grid', gap:16}}>
            {interactions.map((x,i)=>(
              <div key={x} style={{opacity:ease(f,20+i*35,45+i*35), transform:`translateX(${(1-ease(f,20+i*35,45+i*35))*-30}px)`}}>
                <Page style={{padding:'18px 24px'}}><P size={19}>{x}</P></Page>
              </div>
            ))}
          </div>
        </div>
        <div>
          <Page style={{padding:42}}>
            <H size={32} color={T.teal}>Learner profile</H>
            <div style={{marginTop:30}}>
              {[
                ['Visual support',0.83,T.blue],
                ['Step-by-step',0.67,T.teal],
                ['Question-based',0.76,T.gold],
              ].map(([label,val,color]:any,i)=>(
                <div key={label} style={{marginBottom:28,opacity:ease(f,175+i*25,205+i*25)}}>
                  <P size={18}>{label}</P>
                  <div style={{height:13,background:T.line,borderRadius:99,marginTop:8}}>
                    <div style={{height:'100%',width:`${Number(val)*100}%`,background:color,borderRadius:99}} />
                  </div>
                </div>
              ))}
            </div>
          </Page>
          <div style={{marginTop:26, opacity:ease(f,300,345)}}>
            <TutorBubble text="Next time, I can explain it in a way that better fits this learner." />
          </div>
        </div>
      </div>
    </Shell>
  );
};

/* B07 — camera-like conceptual handoff from student to instructor */
export const InstructorIntro: React.FC<MedhavyExplainerProps> = ({sparkLine}) => {
  const f = useCurrentFrame();
  const shift = ease(f,55,125);
  return (
    <Shell title="The other side of the classroom" sparkLine={sparkLine}>
      <div style={{height:'100%', position:'relative'}}>
        <div style={{position:'absolute',top:'50%',left:`${38-shift*23}%`,transform:'translate(-50%,-50%)',opacity:1-shift*0.7}}>
          <Page style={{padding:40,width:500}}><H size={36}>Student</H><div style={{marginTop:22}}><Book title="Learning experience" /></div></Page>
        </div>
        <div style={{position:'absolute',top:'50%',left:`${76-shift*20}%`,transform:'translate(-50%,-50%)',opacity:ease(f,40,90)}}>
          <Page style={{padding:45,width:620,border:`2px solid ${T.teal}`}}>
            <H size={42} color={T.teal}>Instructor workspace</H>
            <div style={{marginTop:26,display:'flex',gap:14,flexWrap:'wrap'}}>
              {['Textbooks','Notes','Assessments','Course material'].map((x)=><LabelChip key={x} text={x} />)}
            </div>
          </Page>
        </div>
      </div>
    </Shell>
  );
};

/* B08 — materials -> processing -> outputs -> instructor control */
export const CoInstructorPipeline: React.FC<MedhavyExplainerProps> = ({sparkLine, badge}) => {
  const f = useCurrentFrame();
  return (
    <Shell title="From course knowledge to teaching tools" sparkLine={sparkLine} badge={badge}>
      <div style={{height:'100%',position:'relative'}}>
        <div style={{position:'absolute',inset:0,opacity:stageOpacity(f,0,180),display:'flex',alignItems:'center',justifyContent:'center',gap:28}}>
          {['Textbook','Lecture notes','Course materials'].map((x,i)=><Pop key={x} delay={i*18}><Page style={{padding:'32px 38px'}}><H size={28}>{x}</H></Page></Pop>)}
        </div>
        <div style={{position:'absolute',inset:0,opacity:stageOpacity(f,150,360),display:'flex',alignItems:'center',justifyContent:'center',gap:40}}>
          <div style={{display:'grid',gap:16}}>
            {['Textbook','Lecture notes','Course materials'].map((x)=><LabelChip key={x} text={x} />)}
          </div>
          <Arrow progress={ease(f,170,220)} />
          <Page style={{padding:46,border:`2px solid ${T.teal}`}}><H size={38} color={T.teal}>AI co-instructor</H><div style={{marginTop:18}}><P size={18}>Uses the instructor's own material</P></div></Page>
        </div>
        <div style={{position:'absolute',inset:0,opacity:stageOpacity(f,330,610),display:'flex',alignItems:'center',justifyContent:'center',gap:28}}>
          {['Summary','Quiz','Exam','Lecture notes'].map((x,i)=><Pop key={x} delay={350+i*22}><Page style={{padding:'34px 42px',border:`2px solid ${[T.blue,T.teal,T.gold,T.lavender][i]}`}}><H size={28}>{x}</H></Page></Pop>)}
        </div>
        <div style={{position:'absolute',inset:0,opacity:ease(f,590,690),display:'flex',alignItems:'center',justifyContent:'center'}}>
          <Page style={{padding:'42px 60px'}}><H size={42}>Instructor remains at the center.</H></Page>
        </div>
      </div>
    </Shell>
  );
};

/* B09 — task accumulation -> stretched timeline -> clock */
export const CourseCreationProblem: React.FC<MedhavyExplainerProps> = ({sparkLine}) => {
  const f = useCurrentFrame();
  const tasks=['Organize material','Create modules','Write assessments','Prepare resources'];
  return (
    <Shell title="Building from scratch takes time" sparkLine={sparkLine}>
      <div style={{height:'100%',display:'grid',gridTemplateColumns:'1.15fr 0.85fr',gap:70,alignItems:'center'}}>
        <div>
          {tasks.map((x,i)=>(
            <div key={x} style={{opacity:ease(f,15+i*35,42+i*35),marginBottom:20}}>
              <Page style={{padding:'20px 28px',display:'flex',alignItems:'center',gap:18}}>
                <div style={{width:26,height:26,border:`2px solid ${T.muted}`,borderRadius:6}} />
                <P size={21}>{x}</P>
              </Page>
            </div>
          ))}
          <div style={{marginTop:28,height:5,background:T.line,position:'relative'}}>
            <div style={{height:'100%',width:`${ease(f,170,300)*100}%`,background:T.crimson}} />
          </div>
        </div>
        <div style={{textAlign:'center'}}>
          <div style={{fontFamily:typography.serif,fontSize:130,color:T.crimson,fontWeight:900,transform:`rotate(${ease(f,120,330)*300}deg)`}}>◴</div>
          <H size={36} color={T.crimson}>Hours before class starts</H>
        </div>
      </div>
    </Shell>
  );
};

/* B10 — inputs -> organized modules -> assessments -> faster structured course */
export const CourseImportPipeline: React.FC<MedhavyExplainerProps> = ({sparkLine, badge}) => {
  const f = useCurrentFrame();
  return (
    <Shell title="Start with what you already have" sparkLine={sparkLine} badge={badge}>
      <div style={{height:'100%',position:'relative'}}>
        <div style={{position:'absolute',inset:0,opacity:stageOpacity(f,0,180),display:'flex',alignItems:'center',justifyContent:'center',gap:50}}>
          <Page style={{padding:40}}><Book title="Textbook" /></Page>
          <div style={{fontFamily:typography.display,fontSize:70,fontWeight:900,color:T.ink}}>+</div>
          <Page style={{padding:40}}><H size={34}>GitHub repository</H><div style={{marginTop:18,fontFamily:'monospace',fontSize:17,color:T.muted}}>/chapters<br/>/figures<br/>/examples</div></Page>
        </div>
        <div style={{position:'absolute',inset:0,opacity:stageOpacity(f,150,390),display:'flex',alignItems:'center',justifyContent:'center'}}>
          <Page style={{padding:48,width:1150}}>
            <H size={38} color={T.teal}>Medhavy course builder</H>
            <div style={{marginTop:35,display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:16}}>
              {['Import','Organize','Generate','Structure'].map((x,i)=><div key={x} style={{padding:22,borderRadius:12,background:[T.tealSoft,T.paper,T.goldSoft,T.paper][i],border:`1px solid ${T.line}`,fontFamily:typography.display,fontWeight:800,textAlign:'center'}}>{x}</div>)}
            </div>
          </Page>
        </div>
        <div style={{position:'absolute',inset:0,opacity:ease(f,370,500),display:'flex',alignItems:'center',justifyContent:'center',gap:32}}>
          {['Module 1','Module 2','Assessments'].map((x,i)=><Page key={x} style={{padding:'38px 44px',border:`2px solid ${[T.blue,T.teal,T.gold][i]}`}}><H size={30}>{x}</H></Page>)}
        </div>
      </div>
    </Shell>
  );
};

/* B14 — return to book and lock the three principles in */
export const MedhavyClose: React.FC<MedhavyExplainerProps> = ({sparkLine, onScreenText}) => {
  const f = useCurrentFrame();
  const labels=onScreenText.length?onScreenText:['Personalized','Grounded','Built for learning'];
  return (
    <Shell title="The idea is simple" sparkLine={sparkLine}>
      <div style={{height:'100%',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center'}}>
        <div style={{opacity:ease(f,0,30)}}><Book title="An interactive textbook that teaches back" /></div>
        <div style={{marginTop:65,display:'flex',gap:20}}>
          {labels.slice(0,3).map((x,i)=><Pop key={x} delay={60+i*28}><LabelChip text={x} color={[T.blue,T.teal,T.gold][i]} /></Pop>)}
        </div>
        <div style={{marginTop:58,opacity:ease(f,170,240),textAlign:'center'}}>
          <H size={32} color={T.teal}>Learning and teaching, in one connected experience.</H>
        </div>
      </div>
    </Shell>
  );
};
