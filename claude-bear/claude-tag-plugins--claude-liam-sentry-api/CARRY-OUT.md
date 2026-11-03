# CARRY-OUT — claude-tag-plugins--claude-liam-sentry-api

**The wrong guess it defeats:** that the short, human-readable code shown at a
Sentry issue's URL (`PROJ-123`) is the identifier Claude sends on to the API —
so Claude could just read it off the screen.

**The carry-out line (written first, GATE C):**

> The ID shown in the browser isn't the ID Claude sends — and a two-hundred
> response isn't always the yes it looks like.

**Survives-being-repeated test:** someone who only half-heard the reel and
repeats just this sentence next week is still saying something true and
checkable: Sentry's visible shortId and its numeric ID are different things,
and a successful-looking HTTP status can still carry a rejection in its body.

**Compresses the distinction, not the topic:** the topic is "the sentry-api
skill." The distinction is "what's shown isn't what's sent, and looking okay
isn't the same as being okay" — which is what every beat before it built
toward (B00's correction on the shortId, B01–B02's specific map of IDs, events,
and the `detail` field, B03's both-directions split between what's marked
plainly and what's easy to miss).
