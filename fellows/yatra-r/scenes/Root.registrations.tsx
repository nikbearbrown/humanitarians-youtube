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


// ============================================================================
// Added 2026-09-03 — Nobody Wrote This. + This Week, Gordy.
//
// Two refusals below are enforced by the TYPES rather than by memory, and are the
// reason these are separate components instead of reuses:
//   * WkReview's `slots` carry a label and NOTHING else — no title, summary or
//     content prop exists, because the two articles are in review and unpublished.
//   * WkPipeline has no per-stage `state` field, so the framework beat cannot leak
//     the status board that the following beat reveals.
//   * LnkAllOrNothing has no remainder-bar prop: the human-written share was never
//     published, and a bar length is a number.
//   * LnkLadder takes an explicit `bar` number separate from the verbatim `value`
//     string, because three values are ranges and the house num() helper misreads
//     "4-13%" as 413.
// ============================================================================

import {LnkBluf, LnkFrame, LnkStat, LnkLadder, LnkDisproportion, LnkAllOrNothing, LnkContradiction, LnkFalsify, LnkPressure} from './scenes/NobodyWroteThis';
import {WkBluf, WkPipeline, WkTool, WkStatus, WkShip, WkReview, WkNotClaiming} from './scenes/WeekGordy';
import {WkBluf916, WkPipeline916, WkTool916, WkStatus916, WkShip916, WkReview916, WkNotClaiming916} from './scenes/WeekGordy916';
import {LnkBluf916, LnkFrame916, LnkStat916, LnkLadder916, LnkDisproportion916, LnkAllOrNothing916, LnkContradiction916, LnkFalsify916, LnkPressure916} from './scenes/NobodyWroteThis916';

<Composition id="WkBluf" component={WkBluf}
        durationInFrames={326} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', lines: [{label: '', chip: ''}], closer: ''}}} />
<Composition id="WkPipeline" component={WkPipeline}
        durationInFrames={379} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', stages: [{label: '', sub: ''}], hotIndex: 0, note: ''}}} />
<Composition id="WkTool" component={WkTool}
        durationInFrames={444} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', name: '', quote: '', chips: [], audience: '', url: '', source: '', note: ''}}} />
<Composition id="WkStatus" component={WkStatus}
        durationInFrames={348} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', stages: [{label: '', detail: '', state: 'closed'}], tally: '', note: ''}}} />
<Composition id="WkShip" component={WkShip}
        durationInFrames={409} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', made: {label: '', sub: ''}, destination: {label: '', sub: ''}, chip: '', note: ''}}} />
<Composition id="WkReview" component={WkReview}
        durationInFrames={370} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', slots: [{label: ''}], withhold: '', stages: [{label: '', state: 'done'}], note: ''}}} />
<Composition id="WkNotClaiming" component={WkNotClaiming}
        durationInFrames={377} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', claiming: {heading: '', items: []}, notClaiming: {heading: '', items: []}, note: ''}}} />
<Composition id="WkBluf916" component={WkBluf916}
        durationInFrames={326} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', lines: [{label: '', chip: ''}], closer: ''}}} />
<Composition id="WkPipeline916" component={WkPipeline916}
        durationInFrames={379} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', stages: [{label: '', sub: ''}], hotIndex: 0, note: ''}}} />
<Composition id="WkTool916" component={WkTool916}
        durationInFrames={444} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', name: '', quote: '', chips: [], audience: '', url: '', source: '', note: ''}}} />
<Composition id="WkStatus916" component={WkStatus916}
        durationInFrames={348} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', stages: [{label: '', detail: '', state: 'closed'}], tally: '', note: ''}}} />
<Composition id="WkShip916" component={WkShip916}
        durationInFrames={409} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', made: {label: '', sub: ''}, destination: {label: '', sub: ''}, chip: '', note: ''}}} />
<Composition id="WkReview916" component={WkReview916}
        durationInFrames={370} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', slots: [{label: ''}], withhold: '', stages: [{label: '', state: 'done'}], note: ''}}} />
<Composition id="WkNotClaiming916" component={WkNotClaiming916}
        durationInFrames={377} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', claiming: {heading: '', items: []}, notClaiming: {heading: '', items: []}, note: ''}}} />
<Composition id="LnkBluf" component={LnkBluf}
        durationInFrames={314} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', lead: '', hot: '', struck: '', replacement: '', closer: ''}}} />
<Composition id="LnkFrame" component={LnkFrame}
        durationInFrames={366} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', bins: [{label: '', sub: ''}], hotIndex: 0, source: '', note: ''}}} />
<Composition id="LnkStat" component={LnkStat}
        durationInFrames={387} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', value: '0%', label: '', rank: '', source: '', note: ''}}} />
<Composition id="LnkLadder" component={LnkLadder}
        durationInFrames={435} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', value: '0%', bar: 0}], baseline: {bar: 0, label: ''}, source: '', note: ''}}} />
<Composition id="LnkDisproportion" component={LnkDisproportion}
        durationInFrames={323} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', top: {label: '', value: '', bar: 0}, bottom: {label: '', value: '', bar: 0}, source: '', note: ''}}} />
<Composition id="LnkAllOrNothing" component={LnkAllOrNothing}
        durationInFrames={332} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', assisted: {label: '', value: '', bar: 0}, generated: {label: '', value: '', bar: 0}, remainderLabel: '', source: '', note: ''}}} />
<Composition id="LnkContradiction" component={LnkContradiction}
        durationInFrames={372} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', label: '', sub: ''}, right: {heading: '', label: '', sub: ''}, collision: '', source: '', note: ''}}} />
<Composition id="LnkFalsify" component={LnkFalsify}
        durationInFrames={327} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="LnkPressure" component={LnkPressure}
        durationInFrames={370} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', left: {tag: '', label: '', sub: '', cite: ''}, right: {tag: '', label: '', sub: '', cite: ''}, marker: '', axisLabel: '', note: ''}}} />
<Composition id="LnkBluf916" component={LnkBluf916}
        durationInFrames={314} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', lead: '', hot: '', struck: '', replacement: '', closer: ''}}} />
<Composition id="LnkFrame916" component={LnkFrame916}
        durationInFrames={366} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', bins: [{label: '', sub: ''}], hotIndex: 0, source: '', note: ''}}} />
<Composition id="LnkStat916" component={LnkStat916}
        durationInFrames={387} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', value: '0%', label: '', rank: '', source: '', note: ''}}} />
<Composition id="LnkLadder916" component={LnkLadder916}
        durationInFrames={435} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', value: '0%', bar: 0}], baseline: {bar: 0, label: ''}, source: '', note: ''}}} />
<Composition id="LnkDisproportion916" component={LnkDisproportion916}
        durationInFrames={323} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', top: {label: '', value: '', bar: 0}, bottom: {label: '', value: '', bar: 0}, source: '', note: ''}}} />
<Composition id="LnkAllOrNothing916" component={LnkAllOrNothing916}
        durationInFrames={332} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', assisted: {label: '', value: '', bar: 0}, generated: {label: '', value: '', bar: 0}, remainderLabel: '', source: '', note: ''}}} />
<Composition id="LnkContradiction916" component={LnkContradiction916}
        durationInFrames={372} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', left: {heading: '', label: '', sub: ''}, right: {heading: '', label: '', sub: ''}, collision: '', source: '', note: ''}}} />
<Composition id="LnkFalsify916" component={LnkFalsify916}
        durationInFrames={327} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', items: [{label: '', why: ''}], closer: ''}}} />
<Composition id="LnkPressure916" component={LnkPressure916}
        durationInFrames={370} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', left: {tag: '', label: '', sub: '', cite: ''}, right: {tag: '', label: '', sub: '', cite: ''}, marker: '', axisLabel: '', note: ''}}} />


// ============================================================================
// Added 2026-09-07 — Interest Media.
//
// Two refusals below are enforced by the TYPES rather than by memory, and are the
// reason these are new components instead of reuses:
//   * ItmSource has a `claimParaphrase` field and NO `quote` field. The "interest
//     media" framing is credited to Gary Vaynerchuk and the instruction was to
//     paraphrase him, never to quote him — so there is no prop to quote him with.
//   * NOTHING in this family carries a numeric prop. No value, pct, count, bar or
//     stat exists on any type here, so this reel cannot print a statistic. That
//     matters most on ItmVolume, whose subject IS volume: its marks are unlabelled
//     and uncounted, and it argues density rather than a figure.
//
// MARKS and TICKS are exported from InterestMedia.tsx and IMPORTED by the portrait
// module rather than redeclared, so the two cuts of one reel cannot drift apart on
// how dense "too much" looks.
// ============================================================================

import {ItmBluf, ItmSource, ItmFeed, ItmVolume, ItmQuestion, ItmModels, ItmJob, ItmLimits} from './scenes/InterestMedia';
import {ItmBluf916, ItmSource916, ItmFeed916, ItmVolume916, ItmQuestion916, ItmModels916, ItmJob916, ItmLimits916} from './scenes/InterestMedia916';

<Composition id="ItmBluf" component={ItmBluf}
        durationInFrames={314} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', claims: [{label: ''}], hotIndex: 0, closer: ''}}} />
<Composition id="ItmSource" component={ItmSource}
        durationInFrames={493} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', who: '', claimParaphrase: '', stamp: '', oldWord: '', newWord: '', tail: '', oldAsks: '', newAsks: '', note: ''}}} />
<Composition id="ItmFeed" component={ItmFeed}
        durationInFrames={426} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', leftHead: '', leftItems: [], leftFoot: '', rightHead: '', rightItems: [], rightFoot: '', signals: [], note: ''}}} />
<Composition id="ItmVolume" component={ItmVolume}
        durationInFrames={309} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', networkLabel: '', networkSub: '', verdictBand: '', note: ''}}} />
<Composition id="ItmQuestion" component={ItmQuestion}
        durationInFrames={210} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', inputLabel: '', outputLabel: '', oldKey: '', newKey: '', note: ''}}} />
<Composition id="ItmModels" component={ItmModels}
        durationInFrames={408} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', oldTitle: '', oldSteps: ['', '', ''], oldGateLabel: '', oldFoot: '', newTitle: '', newSteps: ['', '', ''], newFoot: '', note: ''}}} />
<Composition id="ItmJob" component={ItmJob}
        durationInFrames={282} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', oldHead: '', oldQuestion: '', newHead: '', newQuestion: '', tickLabel: '', note: ''}}} />
<Composition id="ItmLimits" component={ItmLimits}
        durationInFrames={372} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', claims: {heading: '', items: []}, refusals: {heading: '', items: []}, provenance: '', falsifier: ''}}} />
<Composition id="ItmBluf916" component={ItmBluf916}
        durationInFrames={314} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', claims: [{label: ''}], hotIndex: 0, closer: ''}}} />
<Composition id="ItmSource916" component={ItmSource916}
        durationInFrames={493} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', who: '', claimParaphrase: '', stamp: '', oldWord: '', newWord: '', tail: '', oldAsks: '', newAsks: '', note: ''}}} />
<Composition id="ItmFeed916" component={ItmFeed916}
        durationInFrames={426} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', leftHead: '', leftItems: [], leftFoot: '', rightHead: '', rightItems: [], rightFoot: '', signals: [], note: ''}}} />
<Composition id="ItmVolume916" component={ItmVolume916}
        durationInFrames={309} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', networkLabel: '', networkSub: '', verdictBand: '', note: ''}}} />
<Composition id="ItmQuestion916" component={ItmQuestion916}
        durationInFrames={210} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', inputLabel: '', outputLabel: '', oldKey: '', newKey: '', note: ''}}} />
<Composition id="ItmModels916" component={ItmModels916}
        durationInFrames={408} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', oldTitle: '', oldSteps: ['', '', ''], oldGateLabel: '', oldFoot: '', newTitle: '', newSteps: ['', '', ''], newFoot: '', note: ''}}} />
<Composition id="ItmJob916" component={ItmJob916}
        durationInFrames={282} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', oldHead: '', oldQuestion: '', newHead: '', newQuestion: '', tickLabel: '', note: ''}}} />
<Composition id="ItmLimits916" component={ItmLimits916}
        durationInFrames={372} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', claims: {heading: '', items: []}, refusals: {heading: '', items: []}, provenance: '', falsifier: ''}}} />


// ============================================================================
// Added 2026-10-21 — Both Sides of the Table. + The Mask Slips.
//
// Citation discipline in both families, enforced by the types:
//   * TblSide / TblInterview / TblWalk / TblInject each REQUIRE a `source`.
//   * TblTrust requires a SEPARATE source on each of its two figures — the 26%
//     (Greenhouse) and the 66% (Pew) are different studies of different
//     populations, so there is no shared source field that could merge them.
//   * MskSpike / MskMoney / MskDrop each REQUIRE a `source`; every value is a
//     verbatim string, so "roughly 50%" keeps its hedge and $13,700 is never
//     reformatted.
// ============================================================================

import {MskBluf, MskSpike, MskMoney, MskArc, MskReveal, MskDrop, MskTurn, MskLimits} from './scenes/MaskSlips';
import {MskBluf916, MskSpike916, MskMoney916, MskArc916, MskReveal916, MskDrop916, MskTurn916, MskLimits916} from './scenes/MaskSlips916';
import {TblBluf, TblSide, TblTable, TblInterview, TblWalk, TblTrust, TblInject, TblLimits} from './scenes/TableSides';
import {TblBluf916, TblSide916, TblTable916, TblInterview916, TblWalk916, TblTrust916, TblInject916, TblLimits916} from './scenes/TableSides916';

<Composition id="MskBluf" component={MskBluf}
        durationInFrames={400} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', firstHead: '', firstLines: [], secondHead: '', secondLines: [], closer: ''}}} />
<Composition id="MskSpike" component={MskSpike}
        durationInFrames={381} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', lead: {value: '', label: ''}, figures: [], source: '', note: ''}}} />
<Composition id="MskMoney" component={MskMoney}
        durationInFrames={378} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', value: '', qualifier: '', stamp: '', source: '', note: ''}}} />
<Composition id="MskArc" component={MskArc}
        durationInFrames={350} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', riseLabel: '', markerLabel: '', fallLabel: '', axisNote: '', note: ''}}} />
<Composition id="MskReveal" component={MskReveal}
        durationInFrames={382} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', leftLabel: '', rightBefore: '', rightAfter: '', wireLabel: '', verdict: '', note: ''}}} />
<Composition id="MskDrop" component={MskDrop}
        durationInFrames={438} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', cases: [{label: '', value: '', detail: ''}], beforeLabel: '', afterLabel: '', source: '', note: ''}}} />
<Composition id="MskTurn" component={MskTurn}
        durationInFrames={417} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', ruledOut: [], survivor: '', closer: '', note: ''}}} />
<Composition id="MskLimits" component={MskLimits}
        durationInFrames={496} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', claims: {heading: '', items: []}, refusals: {heading: '', items: []}, provenance: '', falsifier: ''}}} />
<Composition id="MskBluf916" component={MskBluf916}
        durationInFrames={400} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', firstHead: '', firstLines: [], secondHead: '', secondLines: [], closer: ''}}} />
<Composition id="MskSpike916" component={MskSpike916}
        durationInFrames={381} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', lead: {value: '', label: ''}, figures: [], source: '', note: ''}}} />
<Composition id="MskMoney916" component={MskMoney916}
        durationInFrames={378} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', value: '', qualifier: '', stamp: '', source: '', note: ''}}} />
<Composition id="MskArc916" component={MskArc916}
        durationInFrames={350} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', riseLabel: '', markerLabel: '', fallLabel: '', axisNote: '', note: ''}}} />
<Composition id="MskReveal916" component={MskReveal916}
        durationInFrames={382} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', leftLabel: '', rightBefore: '', rightAfter: '', wireLabel: '', verdict: '', note: ''}}} />
<Composition id="MskDrop916" component={MskDrop916}
        durationInFrames={438} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', cases: [{label: '', value: '', detail: ''}], beforeLabel: '', afterLabel: '', source: '', note: ''}}} />
<Composition id="MskTurn916" component={MskTurn916}
        durationInFrames={417} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', ruledOut: [], survivor: '', closer: '', note: ''}}} />
<Composition id="MskLimits916" component={MskLimits916}
        durationInFrames={496} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', claims: {heading: '', items: []}, refusals: {heading: '', items: []}, provenance: '', falsifier: ''}}} />
<Composition id="TblBluf" component={TblBluf}
        durationInFrames={354} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', claims: [{label: '', align: 'left'}], hotIndex: 0, closer: ''}}} />
<Composition id="TblSide" component={TblSide}
        durationInFrames={367} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', side: 'left', head: '', value: '', bar: 0, label: '', qualifier: '', source: '', note: ''}}} />
<Composition id="TblTable" component={TblTable}
        durationInFrames={340} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', leftOuter: '', leftInner: '', rightInner: '', rightOuter: '', trafficLabel: '', verdict: '', note: ''}}} />
<Composition id="TblInterview" component={TblInterview}
        durationInFrames={327} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', value: '', bar: 0, label: '', delta: '', deltaNote: '', source: '', note: ''}}} />
<Composition id="TblWalk" component={TblWalk}
        durationInFrames={327} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', value: '', bar: 0, label: '', verdict: '', source: '', note: ''}}} />
<Composition id="TblTrust" component={TblTrust}
        durationInFrames={395} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', left: {value: '', bar: 0, label: '', source: ''}, right: {value: '', bar: 0, label: '', source: ''}, note: ''}}} />
<Composition id="TblInject" component={TblInject}
        durationInFrames={418} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', value: '', bar: 0, label: '', stamp: '', visibleLines: [], hiddenLabel: '', source: '', note: ''}}} />
<Composition id="TblLimits" component={TblLimits}
        durationInFrames={400} fps={30} width={1920} height={1080}
        defaultProps={{data: {slideMeta: '', title: '', claims: {heading: '', items: []}, refusals: {heading: '', items: []}, provenance: '', falsifier: ''}}} />
<Composition id="TblBluf916" component={TblBluf916}
        durationInFrames={354} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', claims: [{label: '', align: 'left'}], hotIndex: 0, closer: ''}}} />
<Composition id="TblSide916" component={TblSide916}
        durationInFrames={367} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', side: 'left', head: '', value: '', bar: 0, label: '', qualifier: '', source: '', note: ''}}} />
<Composition id="TblTable916" component={TblTable916}
        durationInFrames={340} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', leftOuter: '', leftInner: '', rightInner: '', rightOuter: '', trafficLabel: '', verdict: '', note: ''}}} />
<Composition id="TblInterview916" component={TblInterview916}
        durationInFrames={327} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', value: '', bar: 0, label: '', delta: '', deltaNote: '', source: '', note: ''}}} />
<Composition id="TblWalk916" component={TblWalk916}
        durationInFrames={327} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', value: '', bar: 0, label: '', verdict: '', source: '', note: ''}}} />
<Composition id="TblTrust916" component={TblTrust916}
        durationInFrames={395} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', left: {value: '', bar: 0, label: '', source: ''}, right: {value: '', bar: 0, label: '', source: ''}, note: ''}}} />
<Composition id="TblInject916" component={TblInject916}
        durationInFrames={418} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', value: '', bar: 0, label: '', stamp: '', visibleLines: [], hiddenLabel: '', source: '', note: ''}}} />
<Composition id="TblLimits916" component={TblLimits916}
        durationInFrames={400} fps={30} width={1080} height={1920}
        defaultProps={{data: {slideMeta: '', title: '', claims: {heading: '', items: []}, refusals: {heading: '', items: []}, provenance: '', falsifier: ''}}} />
