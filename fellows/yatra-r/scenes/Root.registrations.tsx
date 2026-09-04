/**
 * Root.registrations.tsx — NOT a standalone file.
 *
 * These are the <Composition> registrations for the scenes in this folder, extracted from
 * the toolkit's own runtime/remotion/src/Root.tsx. That file is a shared registry of every
 * composition across every reel in the toolkit, so copying it wholesale here would be both
 * noisy and wrong. This is only the subset belonging to these five episodes.
 *
 * To use: paste the imports and the <Composition> elements into the toolkit's Root.tsx.
 *
 * durationInFrames is NOT arbitrary. Each value is its beat's MEASURED Kokoro audio length
 * x 30fps. Where several beats share one composition, the value is the SHORTEST of them:
 * remotion_scenes.py freeze-extends a clip that is shorter than its beat (lossless), while
 * compile.py trims one that is longer (lossy) — and on these scenes the source citation
 * lands at 80-90%% of the span, so trimming would cut exactly the citations.
 *
 * Regenerating audio changes the measured durations, so these numbers must be retargeted
 * or progress-mapped animations get trimmed mid-reveal.
 */

// ---- imports ----
import {BnkSplit, BnkCosts, BnkFunnel, BnkCutoff, BnkBranch} from './scenes/BottleneckMoved';
import {JdgDiverge, JdgSplit, JdgOptions, JdgBranch, JdgStakes} from './scenes/JudgmentIsTheJob';
import {JdgDiverge916, JdgSplit916, JdgOptions916, JdgBranch916, JdgStakes916} from './scenes/JudgmentIsTheJob916';
import {YtwLoop, YtwSplit, YtwChecks, YtwWeeks, YtwStatus} from './scenes/EveryToolEveryWeek';
import {YtwLoop916, YtwSplit916, YtwChecks916, YtwWeeks916, YtwStatus916} from './scenes/EveryToolEveryWeek916';
import {SeoAct, SeoStat, SeoCompare, SeoDrop, SeoShare, SeoSources, SeoSplit, SeoStakes, SeoReasons, SeoWatch, SeoLead} from './scenes/AssistedNotAutomated';
import {SeoAct916, SeoStat916, SeoCompare916, SeoDrop916, SeoShare916, SeoSources916, SeoSplit916, SeoStakes916, SeoReasons916, SeoWatch916} from './scenes/AssistedNotAutomated916';
import {JdgDiverge916 as SeoLead916} from './scenes/JudgmentIsTheJob916';
import {RcpCard, RcpTeam, RcpSplit, RcpWeeks, RcpStatus} from './scenes/OneToolAWeek';
import {RcpCard916, RcpTeam916, RcpSplit916, RcpWeeks916, RcpStatus916} from './scenes/OneToolAWeek916';

// ---- registrations ----
<Composition id="BnkSplit" component={BnkSplit}
        durationInFrames={500} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', startLabel: 'Start', splitLabel: 'Split', tracks: [{label: 'Track A', outcome: 'Up', tone: 'good', path: 'up' as const, notes: []}, {label: 'Track B', outcome: 'Down', tone: 'warn', path: 'down' as const, notes: []}]}}} />
<Composition id="BnkCosts" component={BnkCosts}
        durationInFrames={430} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', rows: [{label: 'Row', note: '', rank: 0.5}], band: ''}}} />
<Composition id="BnkFunnel" component={BnkFunnel}
        durationInFrames={422} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', stages: [{label: 'Stage', rank: 0.5}], bracket: '', doubleNote: '', tailNote: ''}}} />
<Composition id="BnkCutoff" component={BnkCutoff}
        durationInFrames={499} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', axisLabel: '', cutoffLabel: '', below: {label: '', verdict: ''}, above: {label: '', verdict: ''}, falsifier: ''}}} />
<Composition id="BnkBranch" component={BnkBranch}
        durationInFrames={500} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', question: 'Which path?', branches: [{label: 'A', detail: '', fix: '', tone: 'good'}, {label: 'B', detail: '', fix: '', tone: 'warn'}], resolver: {label: 'Resolver', detail: ''}}}} />
<Composition id="JdgDiverge" component={JdgDiverge}
        durationInFrames={623} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', startLabel: 'Start', splitLabel: 'Split', tracks: [{label: 'A', outcome: '', tone: 'good', path: 'up' as const, notes: []}, {label: 'B', outcome: '', tone: 'warn', path: 'down' as const, notes: []}]}}} />
<Composition id="JdgSplit" component={JdgSplit}
        durationInFrames={598} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', items: []}, right: {heading: '', items: []}, note: ''}}} />
<Composition id="JdgOptions" component={JdgOptions}
        durationInFrames={514} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', options: ['A', 'B'], chosenIndex: 0, caption: ''}}} />
<Composition id="JdgBranch" component={JdgBranch}
        durationInFrames={587} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', question: '', branches: [{label: 'A', detail: '', fix: '', tone: 'warn'}, {label: 'B', detail: '', fix: '', tone: 'good'}], resolver: {label: '', detail: ''}}}} />
<Composition id="JdgStakes" component={JdgStakes}
        durationInFrames={490} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="JdgDiverge916" component={JdgDiverge916}
        durationInFrames={623} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', startLabel: '', splitLabel: '', tracks: [{label: 'A', outcome: '', tone: 'good', path: 'up' as const, notes: []}, {label: 'B', outcome: '', tone: 'warn', path: 'down' as const, notes: []}]}}} />
<Composition id="JdgSplit916" component={JdgSplit916}
        durationInFrames={598} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', items: []}, right: {heading: '', items: []}, note: ''}}} />
<Composition id="JdgOptions916" component={JdgOptions916}
        durationInFrames={514} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', options: ['A', 'B'], chosenIndex: 0, caption: ''}}} />
<Composition id="JdgBranch916" component={JdgBranch916}
        durationInFrames={587} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', question: '', branches: [{label: 'A', detail: '', fix: '', tone: 'warn'}, {label: 'B', detail: '', fix: '', tone: 'good'}], resolver: {label: '', detail: ''}}}} />
<Composition id="JdgStakes916" component={JdgStakes916}
        durationInFrames={490} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="YtwLoop" component={YtwLoop}
        durationInFrames={643} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', steps: [{label: 'Step', note: ''}], breakIndex: -1, breakLabel: ''}}} />
<Composition id="YtwSplit" component={YtwSplit}
        durationInFrames={506} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', items: []}, right: {heading: '', items: []}, note: ''}}} />
<Composition id="YtwChecks" component={YtwChecks}
        durationInFrames={518} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="YtwWeeks" component={YtwWeeks}
        durationInFrames={448} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', first: '', waitingLabel: '', note: ''}}} />
<Composition id="YtwStatus" component={YtwStatus}
        durationInFrames={371} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', kicker: '', states: [{label: '', done: true}], note: ''}}} />
<Composition id="YtwLoop916" component={YtwLoop916}
        durationInFrames={643} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', steps: [{label: 'Step', note: ''}], breakIndex: -1, breakLabel: ''}}} />
<Composition id="YtwSplit916" component={YtwSplit916}
        durationInFrames={506} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', items: []}, right: {heading: '', items: []}, note: ''}}} />
<Composition id="YtwChecks916" component={YtwChecks916}
        durationInFrames={518} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="YtwWeeks916" component={YtwWeeks916}
        durationInFrames={448} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', first: '', waitingLabel: '', note: ''}}} />
<Composition id="YtwStatus916" component={YtwStatus916}
        durationInFrames={371} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', kicker: '', states: [{label: '', done: true}], note: ''}}} />
<Composition id="SeoAct" component={SeoAct}
        durationInFrames={92} fps={30} width={1920} height={1080}
        defaultProps={{data: {act: 'Act One', title: 'Title'}}} />
<Composition id="SeoStat" component={SeoStat}
        durationInFrames={436} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', value: '0%', label: '', source: '', note: ''}}} />
<Composition id="SeoCompare" component={SeoCompare}
        durationInFrames={435} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', value: '0%'}], source: '', note: ''}}} />
<Composition id="SeoDrop" component={SeoDrop}
        durationInFrames={433} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', fromLabel: '', fromValue: '0%', toLabel: '', toValue: '0%', source: '', note: ''}}} />
<Composition id="SeoShare" component={SeoShare}
        durationInFrames={438} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', wholeLabel: '', wholeValue: '0%', partLabel: '', partValue: '0%', source: '', note: ''}}} />
<Composition id="SeoSources" component={SeoSources}
        durationInFrames={373} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', sources: [{claim: '', cite: ''}], note: ''}}} />
<Composition id="SeoSplit" component={SeoSplit}
        durationInFrames={432} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', items: []}, right: {heading: '', items: []}, note: ''}}} />
<Composition id="SeoStakes" component={SeoStakes}
        durationInFrames={451} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="SeoReasons" component={SeoReasons}
        durationInFrames={527} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="SeoWatch" component={SeoWatch}
        durationInFrames={575} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="SeoLead" component={SeoLead}
        durationInFrames={736} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', startLabel: '', splitLabel: '', tracks: [{label: 'A', outcome: '', tone: 'good', path: 'down' as const, notes: []}, {label: 'B', outcome: '', tone: 'warn', path: 'up' as const, notes: []}]}}} />
<Composition id="SeoAct916" component={SeoAct916}
        durationInFrames={92} fps={30} width={1080} height={1920}
        defaultProps={{data: {act: 'Act One', title: 'Title'}}} />
<Composition id="SeoStat916" component={SeoStat916}
        durationInFrames={436} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', value: '0%', label: '', source: '', note: ''}}} />
<Composition id="SeoCompare916" component={SeoCompare916}
        durationInFrames={435} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', value: '0%'}], source: '', note: ''}}} />
<Composition id="SeoDrop916" component={SeoDrop916}
        durationInFrames={433} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', fromLabel: '', fromValue: '0%', toLabel: '', toValue: '0%', source: '', note: ''}}} />
<Composition id="SeoShare916" component={SeoShare916}
        durationInFrames={438} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', wholeLabel: '', wholeValue: '0%', partLabel: '', partValue: '0%', source: '', note: ''}}} />
<Composition id="SeoSources916" component={SeoSources916}
        durationInFrames={373} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', sources: [{claim: '', cite: ''}], note: ''}}} />
<Composition id="SeoSplit916" component={SeoSplit916}
        durationInFrames={432} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', items: []}, right: {heading: '', items: []}, note: ''}}} />
<Composition id="SeoStakes916" component={SeoStakes916}
        durationInFrames={451} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="SeoReasons916" component={SeoReasons916}
        durationInFrames={527} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="SeoWatch916" component={SeoWatch916}
        durationInFrames={575} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="SeoLead916" component={SeoLead916}
        durationInFrames={736} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', startLabel: '', splitLabel: '', tracks: [{label: 'A', outcome: '', tone: 'good', path: 'down' as const, notes: []}, {label: 'B', outcome: '', tone: 'warn', path: 'up' as const, notes: []}]}}} />
<Composition id="RcpCard" component={RcpCard}
        durationInFrames={465} fps={30} width={1920} height={1080}
        defaultProps={{data: {kicker: '', title: '', lines: [], link: '', note: ''}}} />
<Composition id="RcpTeam" component={RcpTeam}
        durationInFrames={492} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', status: '', people: [], withLabel: '', withPerson: '', remit: [], note: ''}}} />
<Composition id="RcpSplit" component={RcpSplit}
        durationInFrames={543} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', items: []}, right: {heading: '', items: []}, note: ''}}} />
<Composition id="RcpWeeks" component={RcpWeeks}
        durationInFrames={472} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', first: '', waitingLabel: '', note: ''}}} />
<Composition id="RcpStatus" component={RcpStatus}
        durationInFrames={404} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', kicker: '', states: [{label: '', done: true}], note: ''}}} />
<Composition id="RcpCard916" component={RcpCard916}
        durationInFrames={465} fps={30} width={1080} height={1920}
        defaultProps={{data: {kicker: '', title: '', lines: [], link: '', note: ''}}} />
<Composition id="RcpTeam916" component={RcpTeam916}
        durationInFrames={492} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', status: '', people: [], withLabel: '', withPerson: '', remit: [], note: ''}}} />
<Composition id="RcpSplit916" component={RcpSplit916}
        durationInFrames={543} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', items: []}, right: {heading: '', items: []}, note: ''}}} />
<Composition id="RcpWeeks916" component={RcpWeeks916}
        durationInFrames={472} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', first: '', waitingLabel: '', note: ''}}} />
<Composition id="RcpStatus916" component={RcpStatus916}
        durationInFrames={404} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', kicker: '', states: [{label: '', done: true}], note: ''}}} />
