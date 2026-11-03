# What Is Medhavy?

**Fellow:** Prarthana Ganesh Shetty  
**Project:** Medhavy  

## About Medhavy

Medhavy is an AI-powered learning platform built around interactive textbooks. It brings textbook content, an AI tutor, and learning tools into one learning environment so students can stay connected to the material they are actually studying.

Instead of using a general chatbot separately from the course content, Medhavy is designed so the tutor works with the textbook itself. Students can ask questions while reading, get guided explanations, and interact with learning features such as simulations. Over time, the platform is also designed to adapt more closely to how a student learns.

Medhavy also supports instructors. Course material such as textbooks and lecture notes can be used to help create summaries, quizzes, assessments, and other learning resources, while keeping the instructor at the center of the course.

## How We Structured the Video

The video was created as a high-level introduction for a non-technical audience, so the structure was intentionally simple.

We first introduce the main idea behind Medhavy, then explain why a textbook-grounded tutor is different from a generic AI chatbot. From there, the video moves into personalization, instructor support, and course creation. The final part shows the actual student experience using real Medhavy screen recordings.

This structure helped the video move from the idea, to the problem Medhavy is solving, to how the platform works in practice.

## How the Video Was Built

The video was created using the Brutalist workflow with a `beat_sheet.json`, Kokoro narration, and custom Remotion scenes.

Each section of the narration was treated as its own beat. The beat sheet controlled the narration, timing, and visual direction, while Remotion was used to create the animated scenes.

The first visual version felt too static because some sections stayed on one layout for too long. To make the video more dynamic, the scenes were redesigned so the visuals change along with the narration. Elements appear in stages, move across the frame, connect to each other, expand, collapse, and transition as new ideas are introduced.

For example, instead of showing one fixed screen for an entire explanation, a scene may begin with one object, introduce additional elements as the narration progresses, and then visually connect those elements at the end of the section.

The later product-focused sections use actual Medhavy screen recordings so viewers can see the platform directly instead of only seeing illustrated explanations.

## Main Files

- `beat_sheet.json` - narration, timing, and scene instructions
- `MedhavyExplainerScenes.tsx` - custom Remotion animations
- `medhavySeriesTheme.ts` - shared visual styling
- `Root.tsx` - Remotion composition registrations
- `transcript.md` - narration transcript
