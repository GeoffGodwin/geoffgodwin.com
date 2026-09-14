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
