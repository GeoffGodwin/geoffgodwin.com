# Geoff's voice rules

Two sources. The rules Geoff stated directly are in the first section. The rules
in the second section were derived from his edit pass over the machine draft of
part one, commit `20c33d1` (machine) to `71851ec` (Geoff), and from the corpus
in `src/data/blog/`. Anything derived rather than stated is marked with what the
evidence was, so a later pass can tell a confirmed rule from an inference.

## Stated directly

1. No em dashes anywhere. Use commas, colons, semicolons. Note that
   remark-smartypants converts a double hyphen in prose into an em dash, so a
   double hyphen is banned too.
2. No "it isn't X, it's Y" antithesis.
3. Contractions where they fall naturally.
4. Conversational but not casual. Practitioner to practitioner.
5. Comfortable with "I believe" and "my understanding is."
6. Longer, varied sentences. Never choppy fragments, and never stacked short
   declaratives building to a reveal.
7. Metaphors sparingly, and only to clarify a dense point that has already been
   stated plainly.
8. No emojis.
9. No anecdote-weakening of the "most teams I talk to" kind.
10. No content-calendar language, nothing like "this week's post."
11. Never "matters" as a standalone predicate.
12. Section headers read as chapter titles, not engagement hooks.
13. Closing questions are specific and opinionated.

## Derived from the edit pass

### 14. American spelling, without exception

Evidence: the corpus is unanimous. Across eleven posts, "behavior" 13 and
"behaviour" 0, "organization" 24 and "organisation" 0, "recognize" 5 and
"recognise" 0, "optimize" 3 and "optimise" 0, "analyze" 2 and "analyse" 0.
Geoff also changed "recognise" to "recognize" by hand in his pass. So:
behavior, modeling, judgment, honoring, rationalized, maximize, optimize.
Quoted source material keeps its original spelling.

### 15. Orient before claiming

Open a paragraph or a section by placing the reader, then make the move. This
reads as throat-clearing to a compression-minded editor and should not be cut.

- "Two pictures of artificial intelligence are in wide circulation right now"
  became "While the world is filled with varying opinions on the recent boom of
  AI, I feel like two distinct pictures of artificial intelligence are in wide
  circulation right now."
- "The question I kept returning to" became "Something I often think about when
  it comes to these fear-inducing premises."
- "Two results from the past two years are worth naming" became "I want to call
  out two results from the past two years."

### 16. Narrate the process, not only the conclusion

- "The answer that changed my mind came from a literature predating" became
  "So I started hunting on my own time to find an answer to this and the thing
  that changed my mind came from literature that predates."

The reader is told where the thinking came from, not handed the result.

### 17. Stance verbs are feeling verbs

Rule 5 above understates this. "I believe" is the floor, not the register.
Geoff reaches for softer, warmer, more tentative markers.

- "I believe both are wrong in the same way" became "I also have this nagging
  feeling that both are incorrect."
- "worth naming" became "that I feel are valuable."
- "the caveats are more instructive than the headlines" became "I find the
  caveats to be the real findings."
- "for a long time I treated it as one" became "for a long time that's
  basically how I saw it."

### 18. Decompress. Repeat the noun rather than making the reader resolve a pronoun

The single most consistent change in the pass, and the one whose absence made
section 3 unreadable to him. Compression that saves five words at the cost of
one unresolved referent is a bad trade in this voice, every time.

- "the lineages that didn't" became "all the 'competitors' that didn't have
  that same drive."
- "it was told." became "it was told that it was being trained."
- "the incentives of the organization that chose both" became "the incentives
  of the organization that chose those objectives and tools."
- "a model nobody fully understands" became "a model that people understand the
  concept behind and creation of but not the inner workings of."

Practical test: if a sentence contains "it," "this," "that" or "both" standing
in for something more than one clause away, name the thing instead.

### 19. Cut literary flourish, keep conversational idiom

The distinction is whether the phrase belongs to written English or to spoken
English. Written-literary goes; spoken-idiomatic stays and is welcome.

- Cut: "Three assumptions ride along unexamined," which became "This also
  typically requires three base assumptions."
- Cut: "and the more consequential of the two," deleted entirely rather than
  rephrased. Comparative ranking for rhetorical effect is flourish.
- Kept and strengthened: "I'd hold it loosely" became "it's not a hill I'm
  willing to die on." "smuggles in" survived as "also tries to smuggle in."
  "does real work later" became "does some heavy lifting later."

### 20. Name the technical term where it is explained

Geoff inserted "The term is instrumental convergence, and" into a paragraph
that had described the concept and labelled it only afterwards. Attach the
label at the point of explanation rather than assuming it from context or
deferring it.

### 21. Address the reader as "we," not by role

- "which parts of it a person with a budget can act on" became "which parts we
  can meaningfully act on."

Avoid casting the reader as an economic function. This also serves the
proprietary-restraint constraint, since role-nouns drift toward describing a
specific workplace.

### 22. Hedge universals in time

- "an AI that doesn't exist" became "an AI that doesn't exist today."
- "this is a quirk of one family" became "this must be a quirk of one family."

Claims about the state of the technology carry a temporal marker.

### 23. Break a very long sentence with a demonstrative subject

Where a sentence runs past roughly forty words and has a natural pivot, Geoff
splits it and restarts with "That's" or similar rather than adding another
subordinate clause.

- "a model nobody fully understands, wrapped in scaffolding that grants it
  memory" became "...but not the inner workings of. That's wrapped in
  scaffolding that grants it memory."

### 24. Connect paragraphs with spoken discourse markers

Paragraphs open with a connector that carries the argument forward rather than
starting cold: "The thing is though," "So then based on that," "Now I do want
to be careful," "So I started hunting."

## Open question, not yet a rule

Geoff's pass consistently added words rather than removing them, which is in
direct tension with a fixed word target. Sections 15, 16, 18 and 24 all cost
words. The working assumption from here is that clarity and voice win and the
word count is reported honestly rather than met by compression, but this has
not been confirmed with him.
