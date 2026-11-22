# PROMPTS — How Do Websites Know I'm Not a Robot?

**No open generation slots.** Three Remotion compositions (`ClaudeComposerAsk` twice, `BrutalistHesitantWriter`), two
more bookends (`ClaudeVerdictArtifact`, `LogoOutro`), and eight Manim scenes per orientation. No image model and no paid
API. Narration is generated locally with Kokoro voice `af_bella`.

## B01: the on-screen typed ask

> Explain how websites know I'm not a robot.

Result lines that land under it (all taken from ideas already in `SCRIPT.md`, none new):

> Websites check how you behave
> A score, not a puzzle
> Traffic lights aren't the whole test

## B03: the hesitant writer

Typed first, in terracotta, then deleted:

> Prove you can see traffic lights.

Replaced by:

> Prove you behave like a person.

The on-screen lines are the ones in `SCRIPT.md` (on screen only, not narrated). They are set on short lines
(landscape: "Prove you can see / traffic lights." and "Prove you behave / like a person.") so the whole correction can
finish typing early in the beat. The whole sentence is the trigger phrase, so the correction replaces the sentence, not
one word. There is no lead silence on B03, matching the earlier films. B03's audio is now 9.34 s, long enough for the type, pause, delete and retype.

## BHTF: Your Turn (typed on screen, and read aloud in the narration)

> Explain why a website showed me a 'Verify you are human' page, what it might have checked in the background, and how
> you would tell a person from a bot without traffic lights.

The spoken version first adds: "This week, count how many times a website asks if you're human, and notice when it lets
you through without asking." That sentence is in the narration only, not on screen, as in `SCRIPT.md`. The narration
reads the prompt as written in `SCRIPT.md`, with "Verify you are human" in quotation marks. On screen the prompt is
typed with single quotes around that phrase so it can sit inside the composer's own double-quoted line without
breaking.

What a good answer should show, so you can judge what Claude gives back. Only what your sources support should count as
a good answer:

- It says a site can decide using signals gathered before any puzzle appears: for example cookies, browsing history and
  mouse movements, which are the ones named in your sources.
- It mentions that some systems give a score instead of asking a question, and that the puzzle is shown when the system
  is unsure.
- It says how you could tell a person from a bot without traffic lights: by behaviour over time, not by one picture.

If Claude's answer is certain about what one particular site checked, it is guessing: no source here says what any
specific page looked at. A good answer says "might have", as the prompt does.

## Pronunciation (voice only; the on-screen text and the narration text are untouched)

Set in `metadata.pronounce`:

| Word | IPA | Notes |
|---|---|---|
| Keya | `kˈeɪjɛə` | "Kay-yeah" |

Only Keya is set. Everything else is on Kokoro's defaults. Preview of what Kokoro will say for the words you asked to
listen-check, from the phonemizer:

| Written | Kokoro's phonemes | Reads as |
|---|---|---|
| CAPTCHA | `kˈæpttʃɚ` | "kap-cher". A "t" may be heard before the "ch" ("kapt-cher"). Check by ear. |
| reCAPTCHA v3 | `ɹˌiː kˈæpttʃə vˈiː θɹˈiː` | "ree-kap-cher vee three". Check "v3" reads as "vee three". |
| Cloudflare | `klˈaʊdflɛɹ` | "cloud-flair". Looks normal. |
| UC Irvine | `jˌuːsˈiː ˈɜːvaɪn` | "you-see ER-vine". Looks normal. |
| ETH Zurich | `ˌiːtˌiːˈeɪtʃ zjˈʊɹɪk` | "E-T-H zyoor-ik". Check: the usual sound is closer to "ZOO-rik". |
| Keya | `kˈeɪjɛə` (set) | "Kay-yeah". Without the setting Kokoro would say `kˈiːə` ("kee-uh"). |

Not touched: anything beyond Keya. These are the five words you asked to listen to. Tell me which sound wrong and I
will add a pronunciation entry and regenerate only the beats that contain them: CAPTCHA (B02, B04, B06, B07, B08),
reCAPTCHA v3 (B06), Cloudflare (B07), UC Irvine (B08), ETH Zurich (B09).
