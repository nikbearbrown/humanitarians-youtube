# PEDAGOGY — software-design-document

## Concept

SDD as pre-build decision document. How does an SDD prevent scope drift?

## Question

How does an SDD prevent scope drift?

## Answer

The Principle Collision Test forces real conflicts to surface at the principle level before code is written. The non-component list makes scope explicit — naming what is out of scope prevents it from silently entering the build. A principle that survives every realistic scenario is a tagline; the Collision Test distinguishes real principles from taglines.

## Key Concept: Five sections of the SDD

1. Problem Statement — one user, one done-condition, one sentence
2. Architecture Principles — must survive the Collision Test
3. User Needs — stopwatch-and-laptop measurable
4. Component List — includes explicit non-components
5. Open Questions — unresolved decisions

## The Principle Collision Test

For each architecture principle, ask: is there a realistic scenario where this principle conflicts with another principle? If no conflict exists under any realistic scenario, the principle is not constraining anything — it is a tagline.

## Source

Chapter 07: Software Design Document — claude-code-for-students
