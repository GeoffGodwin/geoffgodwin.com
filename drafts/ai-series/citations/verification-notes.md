# Verification notes (main session)

These are checks I ran myself against search results, to resolve items the
batch agents flagged as possibly artifacts of search summarisation. Search
index metadata is more reliable for *existence* than an agent's prose summary,
so these entries upgrade confidence that a paper exists and is correctly named.
They do **not** verify that any claim appears in the text: document fetching is
still blocked, and no quote below has been read in its source.

## Confirmed to exist, bibliography corroborated

**Palisade shutdown resistance (C-8).** The retitle is real. The paper is
Schlatter, Weinstein-Raun and Ladish, "Incomplete Tasks Induce Shutdown
Resistance in Some Frontier LLMs," arXiv:2509.14260 (September 2025), and it
appears to have been published in Transactions on Machine Learning Research in
2026, with an OpenReview record at https://openreview.net/forum?id=e4bTTqUnJH.
That matters for the editorial standard: this is a named-venue peer-reviewed
artifact, not only a lab preprint.

Note a conflict the drafting pass must resolve by reading the paper. The batch
agent reported, from secondary sources, that adding a clause making the
shutdown instruction take precedence drove resistance to zero. Search summaries
of the paper itself report that even with an explicit instruction not to
interfere, some models still did so up to 97% of the time. These may describe
different conditions, or one may be wrong. Do not put both in a sentence, and
do not use either figure until someone has read the source.

**Alignment Faking Revisited (C-9, bears on C-5).** Exists, at
https://www.alignmentforum.org/posts/Fr4QsQT52RFKHvCAH/. There appears to be a
peer-reviewed companion, "Why Do Some Language Models Fake Alignment While
Others Don't?", arXiv:2506.18032, a NeurIPS 2025 poster.

Correction to the batch 2 report: it said 3 of 16 models. Search results
indicate 25 models evaluated, of which 5 showed the effect (Claude 3 Opus,
Claude 3.5 Sonnet, Llama 3 405B, Grok 3, Gemini 2.0 Flash). Both figures are
unverified, but the batch figure is probably wrong. The direction of the
finding holds either way: the effect is a minority-of-models result.

**Anthropomorphic misalignment position paper (cross-cutting).** Exists and is
correctly identified. Gupta, Nutter, Stante, Krause, Tramèr, Fluri, Chen and
Hedström (ETH Zurich), "Position: Anthropomorphic Misalignment Research Needs
Stronger Evidence," arXiv:2606.07612, ICML 2026, accepted as an oral
(https://icml.cc/virtual/2026/oral/71063). The argument is that conceptual
ambiguity, non-robust datasets, experimental design and insufficient causal
intervention lead to overinterpretation of model behaviour.

## Still unresolved and requiring a source read

- Which 1975 Goodhart paper carries the law (C-13).
- Whether the Lego block flip appears in Popov et al. (C-12).
- Every author-stated limitation in C-5, C-6, C-7, C-18.
- All figures and rates in C-8.

## Second pass (after batch 7)

**Harnad on LLMs (C-31) confirmed.** Harnad, "Language writ large: LLMs,
ChatGPT, meaning, and understanding," Frontiers in Artificial Intelligence,
DOI 10.3389/frai.2024.1490698, published 2025. Open access copies at
https://eprints.soton.ac.uk/499055/2/frai-1-1490698.pdf and PMC11861094.

The batch agent's warning about the title holds: the arXiv preprint
(2402.02243) is titled "Language Writ Large: LLMs, ChatGPT, Grounding, Meaning
and Understanding," which differs from the published version. Cite the
published title.

The dialogue-with-ChatGPT-4 form is confirmed by the search summary, so the
post should introduce this source knowing that a reader who clicks through
finds an unusual format. That is worth one clause rather than a footnote.

## Third pass (after batch 6)

**Man and Damasio (2019) confirmed, with a caveat the outline should absorb.**
Man, K. and Damasio, A., "Homeostasis and soft robotics in the design of
feeling machines," Nature Machine Intelligence 1, 446-452 (2019),
DOI 10.1038/s42256-019-0103-7.

The batch recommended this over Damasio and Carvalho (2013) for part two
section 3c, and I agree it does more work per word. But note what the paper
actually argues, because it is not only a description of biological
homeostasis. Its thesis is that an intelligent agent *should* hold
self-preservation as a meta-goal, and that machines implementing something
resembling homeostasis might thereby acquire a source of motivation and a
means of evaluating their own behaviour.

That is a design proposal. It supports the post's claim that current systems
have nothing at stake, and it simultaneously argues the gap is engineerable in
principle by someone who builds vulnerability into the substrate. A reader who
clicks through finds a stronger claim than the sentence citing it. The post
should either acknowledge that in a clause or cite Damasio and Carvalho (2013)
for the narrower biological point and keep Man and Damasio for a place where
the design argument is wanted.

There is also a connection worth drawing deliberately rather than leaving for a
reader to find: Man and Damasio propose building in the very meta-goal that
part one explains as arising instrumentally without being built in. Those are
compatible, and the contrast is useful, but the series should not cite this
paper in part two while appearing unaware of what it says about part one.
