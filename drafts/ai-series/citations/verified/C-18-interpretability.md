# C-18 — Interpretability citations: verification against primary sources

**Verified:** 2026-09-14
**Method:** Full HTML of both papers retrieved directly from `transformer-circuits.pub` and converted to plain text locally, because `WebFetch` truncated the Biology paper at ~§10 ("Life of a Jailbreak") and therefore could not reach §14. All quotes below were read in the full source text. Nothing here rests on a web-search summary or a mirror.

Primary sources read:

1. https://transformer-circuits.pub/2025/attribution-graphs/biology.html (full document, 707 text blocks)
2. https://transformer-circuits.pub/2025/attribution-graphs/methods.html (full document, 884 text blocks)

---

## Citations (correct full form)

**Biology paper** — as given in the paper's own "Citation Information" section:

> Lindsey, et al., "On the Biology of a Large Language Model", Transformer Circuits, 2025.

BibTeX key `lindsey2025biology`; journal field given as **Transformer Circuits Thread**; year 2025. Author list as printed: Jack Lindsey†, Wes Gurnee\*, Emmanuel Ameisen\*, Brian Chen\*, Adam Pearce\*, Nicholas L. Turner\*, Craig Citro\*, David Abrahams, Shan Carter, Basil Hosmer, Jonathan Marcus, Michael Sklar, Adly Templeton, Trenton Bricken, Callum McDougall◊, Hoagy Cunningham, Thomas Henighan, Adam Jermyn, Andy Jones, Andrew Persic, Zhenyi Qi, T. Ben Thompson, Sam Zimmerman, Kelley Rivoire, Thomas Conerly, Chris Olah, Joshua Batson\*‡. Affiliation: Anthropic. **Published: March 27, 2025** (stated in the page's "Published" field).

**Methods / companion paper** — as given in its own "Citation Information" section:

> Ameisen, et al., "Circuit Tracing: Revealing Computational Graphs in Language Models", Transformer Circuits, 2025.

BibTeX key `ameisen2025circuit`; journal field **Transformer Circuits Thread**; year 2025. First-author order differs from the Biology paper: Emmanuel Ameisen\*, Jack Lindsey\*, Adam Pearce\*, Wes Gurnee\*, Nicholas L. Turner\*, Brian Chen\*, Craig Citro\*, then the same remaining author list. **Published: March 27, 2025.**

**arXiv / journal version: none found.** Both are self-published in the Transformer Circuits Thread. Searches for an arXiv or journal mirror of either title returned only the transformer-circuits.pub pages plus third-party papers citing them. Cite the transformer-circuits.pub URL; do not cite an arXiv number.

---

## A. "The model studied is Claude 3.5 Haiku only." — **CORRECTED**

Claude 3.5 Haiku is the *primary* and headline subject of the Biology paper, but it is not the only model in play, and the Methods paper's own primary subject is a different, smaller model.

Biology paper subtitle (§ title block):

> We investigate the internal mechanisms used by Claude 3.5 Haiku — Anthropic's lightweight production model — in a variety of contexts, using our circuit tracing methodology.

But the Acknowledgments section names two research targets:

> The Pretraining and Finetuning teams trained Claude 3.5 Haiku and the 18-layer research model, which were the targets of our research.
> — § Acknowledgments

And the Methods paper's abstract makes the division explicit:

> We develop a suite of visualization and validation tools we use to investigate these "attribution graphs" supporting simple behaviors of an 18-layer language model, and lay the groundwork for a companion paper applying these methods to a frontier model, Claude 3.5 Haiku.
> — § Abstract, Circuit Tracing (methods paper)

Two further qualifications inside the Biology paper:

- The multilingual scaling result is a **comparison against a smaller model**: "compared to the smaller model, Claude 3.5 Haiku exhibits a higher degree of generalization" (§ Multilingual Circuits → "How General are Multilingual Features?").
- §12 "Uncovering Hidden Goals in a Misaligned Model" studies a deliberately fine-tuned variant, not stock Claude 3.5 Haiku.

**Honest wording for the blog:** "Anthropic's March 2025 circuit-tracing work studies Claude 3.5 Haiku (the companion methods paper works mainly on an 18-layer research model)."

---

## B. Rhyme planning wording — **CONFIRMED (verbatim, with an important adjoining caveat)**

The claimed wording is exact:

> Specifically, the model often activates features corresponding to candidate end-of-next-line words prior to writing the line, and makes use of these features to decide how to compose the line.
> — § Planning in Poems

The very next sentence in the same paragraph is the caveat and should travel with the quote:

> We found planned word features in about half of the poems we investigated, which may be due to our CLT not capturing features for the planned words, or it may be the case that the model does not always engage in planning.
> — § Planning in Poems

The framing that sets up the finding:

> Language models are trained to predict the next word, one word at a time. Given this, one might think the model would rely on pure improvisation. However, we find compelling evidence for a planning mechanism.
> — § Planning in Poems

And the Discussion's summary of the same result, which is the strongest causal statement in the paper:

> Knowing that it needs to produce a line of poetry that rhymes with "grab it", it activates "rabbit" and "habit" features on the new-line token before the line even begins. By inhibiting the model's preferred plan (ending the line with "rabbit"), we can cause it to rewrite the line so that it naturally ends with "habit."
> — § Discussion → "Plan Formation"

---

## C. Language independence / multilingual circuits — **CONFIRMED (all three phrasings exact)**

**(i) "more language-agnostic":**

> These results show that features at the beginning and end of models are highly language-specific (consistent with the {de, re}-tokenization hypothesis), while features in the middle are more language-agnostic.
> — § Multilingual Circuits → "How General are Multilingual Features?"

**(ii) "there are important mechanistic ways in which English is privileged":**

> It seems to us that Claude 3.5 Haiku is using genuinely multilingual features, especially in the middle layers. However, there are important mechanistic ways in which English is privileged.
> — § Multilingual Circuits → "Do Models Think in English?"

**(iii) "in which English is the default output":**

> This paints a picture of a multilingual representation in which English is the default output.
> — § Multilingual Circuits → "Do Models Think in English?"

Supporting detail in the same subsection (the mechanism behind the privilege):

> For example, multilingual features have more significant direct weights to corresponding English output nodes, with non-English outputs being more strongly mediated by say-X-in-language-Y features.
> — § Multilingual Circuits → "Do Models Think in English?"

A second, earlier statement of the same point:

> However, our English graph suggests that there is a meaningful sense in which English is mechanistically privileged over other languages as the "default".
> — § Multilingual Circuits (overview, before "Editing the Operation")

**Important footnote caveat**, attached to the "language-independent representation" claim in the same overview paragraph — this materially limits how strongly (b) can be stated:

> We make this claim on the basis that (1) the feature visualizations show that they activate in many languages, (2) 20 out of 27 of the features in multilingual nodes are active across all three prompts. However, we note that the set of features that are influential to the model's response varies quite a bit by prompt (only 10/27 appear in the pruned attribution graphs for all three prompts).
> — § Multilingual Circuits, footnote

---

## D. Generalisation limits — **CORRECTED (quotes are right; the section attribution is wrong)**

All three phrases are verbatim-correct, **but none of them are in §14 Limitations.** They are in §1 Introduction, under the subsection heading **"A note on our approach and its limitations."** Cite them as Introduction, not Limitations.

**(i) "about a quarter of the prompts we've tried":**

> Though it's difficult to quantify precisely, we've found that our attribution graphs provide us with satisfying insight for about a quarter of the prompts we've tried (see § Limitations for a more detailed discussion of when our methods are likely to succeed or fail).
> — § Introduction → "A note on our approach and its limitations"

The sentence immediately following is worth quoting alongside it:

> The examples we highlight are success cases where we have managed to learn something interesting; moreover, even in our successful case studies, the discoveries we highlight here only capture a small fraction of the mechanisms of the model.
> — § Introduction → "A note on our approach and its limitations"

**(ii) "a biased sample":**

> Moreover, the cases we have chosen to highlight are undoubtedly a biased sample shaped by the limitations of our tools.
> — § Introduction → "A note on our approach and its limitations"

**(iii) "existence proofs" and the non-guarantee of generalisation:**

> These examples serve as existence proofs — concrete evidence that specific mechanisms operate in certain contexts. While we suspect similar mechanisms are at play beyond these examples, we cannot guarantee it (see § Open Questions for suggested follow-up investigations).
> — § Introduction → "A note on our approach and its limitations"

Also relevant, and this one *is* in §14:

> Our results are only claims about specific examples. We don't make claims about mechanisms more broadly. For example, when we discuss planning in poems, we show a few specific examples in which planning appears to occur. It seems likely that the phenomenon is more widespread, but it's not our intent to make that claim.
> — § Limitations (§14)

---

## E. §14 "Limitations" — **VERIFIED IN FULL (previously unverified)**

Read in full from the complete source document. §14 sits between §13 "Commonly Observed Circuit Components and Structure" and §15 "Discussion". Section credit in Author Contributions: "Limitations – Jack Lindsey".

### Structure

§14 has two parts:

1. **An unheaded preamble** of three bullet-style claims about the *scope of this paper's case studies*.
2. **"When Do Our Methods Not Work?"** — a list of six failure conditions, followed by a list of seven named methodological issues, each cross-linked to a fuller treatment in the companion methods paper.

### Part 1 — scope of the paper's claims

Framing sentence:

> This paper focuses on cases where we have successfully applied our methods to gain insights about the mechanisms of Claude 3.5 Haiku. Before addressing the general limitations of these methods, we discuss their limitations as applied to the case studies in this paper.

The three scope limits, verbatim:

> Our results are only claims about specific examples. We don't make claims about mechanisms more broadly. For example, when we discuss planning in poems, we show a few specific examples in which planning appears to occur. It seems likely that the phenomenon is more widespread, but it's not our intent to make that claim.

> We only demonstrate the existence of mechanisms in particular examples. There are likely additional mechanisms which we don't see.

> The examples presented are cases where attribution graph analysis revealed interesting mechanisms. There are many other cases where our methods fell short, and we were unable to come to a satisfactory description of the mechanisms behind a given behavior.

### Part 2a — "When Do Our Methods Not Work?"

Introduced by: "In practice, our methods fail to provide insight in the following cases:" Six cases, each with a bolded lead:

1. **Reasoning that can't be boiled down to a single "crux" token.** — "Our methods produce an attribution graph for a single output token at a time. Often, models produce responses using reasoning chains that span sentences or paragraphs, and in many cases it is not clear which token(s) are most important."
2. **Long Prompts.** — "This is in part due to engineering limitations (we have not scaled our method to apply to prompts longer than about a hundred tokens), and in part a fundamental issue."
3. **Long Internal Reasoning Chains.** — "Our tracing methods lose information at each step, and these errors compound."
4. **"Unusual Prompts" with Obscure Entities or Obfuscated Language.** — "Our CLTs can only reveal computation for which they have learned the relevant features, and are less likely to have learned features for obscure concepts. In these cases, the graph will be dominated by error nodes, and thus uninformative."
5. **"Why does the model not do X?" rather than "Why does the model do X?"** — "This is because by default, our methods do not highlight inactive features and the reasons for their inactivity."
6. **The completion is a copy of a word earlier in the sequence.** — "Our graphs just show an edge directly from (an input feature for) that word and the model output."

### Part 2b — the seven named methodological issues

1. **Missing Attention Circuits** — "We don't explain how attention patterns are computed by the model, and often miss the interesting part of the computation as a result. This prevents us from understanding a variety of behaviors that hinge on the model 'fetching' a piece of information from earlier in the context." Worked example: for a multiple-choice question answered B, "we can see that the model attends back to the tokens corresponding to the 'B' option, but not why it does so – in other words, we can't explain how the model decided that the correct answer was B!"
2. **Reconstruction Errors & Dark Matter** — see quote below.
3. **The Role of Inactive Features & Inhibitory Circuits** — "Often the fact that certain features are not active is just as interesting as the fact that others are." Finding such mechanisms "is generally inconvenient using our method, as it requires identifying a suitable pair of prompts."
4. **Graph Complexity** — pruned, pre-labelled graphs are shown in the paper; unlabelled real graphs are "a slow manual process that can take over an hour for one of our researchers. For longer or more complex prompts, understanding can be out of reach entirely." And: "to some degree, the complexity is inherent to the model, and something that we must reckon with if we are to understand it."
5. **Features at the Wrong Level of Abstraction** — feature splitting; features often represent conjunctions more specific than the concept of interest. The manual "supernode" grouping workaround "is labor-intensive, subjective, and likely loses information."
6. **Difficulty of Understanding Global Circuits** — "we have found the resulting global circuits more challenging to make sense of than prompt-specific attribution graphs."
7. **Mechanistic Faithfulness** — transcoders "may learn fundamentally different mechanisms that, due to correlations in the data distribution, happen to produce the same outputs on the training data." Manifests as "attribution graphs that are occasionally inconsistent with the results of perturbation experiments." The paper's own example: activating an "unknown names" feature failed to produce a refusal, contrary to graph prediction. "(We note that this sort of failed perturbation experiment is uncommon across our case studies.)"

### The four most quotable sentences from §14

> Our results are only claims about specific examples. We don't make claims about mechanisms more broadly.
> — § Limitations, preamble

> We only demonstrate the existence of mechanisms in particular examples. There are likely additional mechanisms which we don't see.
> — § Limitations, preamble

> We only explain a fraction of the model's computation. The remaining "dark matter" manifests as error nodes in our attribution graphs, which (unlike features) have no interpretable function, and whose inputs we cannot easily trace.
> — § Limitations → "Reconstruction Errors & Dark Matter"

> This paper has focused on prompts that are simple enough to avoid these issues. However, even the graphs we have highlighted contain significant contributions from error nodes.
> — § Limitations → "Reconstruction Errors & Dark Matter"

A fifth, for anyone tempted to read the work as an audit capability (this one is in §15 Discussion, not §14, but it is the sharpest self-limiting sentence in the paper):

> there is a very significant likelihood our present method would miss the important safety-relevant computation.
> — § Discussion → "A Path to Safety Auditing Applications"

---

## F. Methods paper: replacement model, and attention — **CONFIRMED**

**(i) Attribution graphs describe the replacement model, not the original model:**

> This is because attribution graphs describe interactions in the local replacement model, which may differ from the underlying model.
> — Circuit Tracing, § Evaluations (validation discussion)

> The local replacement model serves as the basis of our attribution graphs, where we study the feature-feature interactions of the local replacement model on the prompt for which it was made. These graphs are the primary object of study of this paper.
> — Circuit Tracing, § Method Overview (local replacement model)

The consequence, stated in the Biology paper:

> Because they are based on our replacement model, we cannot use attribution graphs to draw conclusions with certainty about the underlying model (i.e. Claude 3.5 Haiku). Thus, the attribution graphs provide hypotheses about mechanisms operating in the underlying model.
> — Biology, § Method Overview

Quantified fidelity, from the methods paper:

> We find that while perturbation results are reasonably similar between the two models when measured one layer after the intervention (~0.8 cosine similarity, ~0.4 normalized mean squared error), perturbation discrepancies compound significantly over layers.
> — Circuit Tracing, § Evaluations

**(ii) No information about influence mediated by attention patterns:**

> Note that these graphs do not contain information about the influence of nodes on other nodes via their influence on attention patterns, but do contain information about node-to-node influence through the outputs of frozen attention. In other words, we account for the information which flows from one token position to another, but not why the model moved that information. That is, our model ignores the "QK-circuits" but captures the "OV-circuits".
> — Circuit Tracing, § Method Overview (attribution graph construction)

> Attribution graphs are constructed by using the underlying model's attention patterns, so edges in the graph do not account for effects mediated via QK circuits. Similarly, in our perturbation experiments, we keep attention patterns fixed at the values observed during an unperturbed forward pass.
> — Circuit Tracing, § Evaluations

And from the methods paper's own Limitations:

> One significant limitation of our approach is that we compute our attribution graphs with respect to fixed attention patterns. This makes attribution a well-defined and principled operation, but also means that our graphs do not attempt to explain how the model's attention patterns were formed [...] However, we have also found many cases where this limitation renders our attribution graphs essentially useless.
> — Circuit Tracing, § Limitations → "Missing Attention Circuits"

---

## Fit assessment

### Claim (a) — "the model plans rhyme words ahead of time"

**Can be stated fairly strongly, but must be scoped to the demonstrated cases.**

This is the best-supported claim of the two. It is not merely correlational: the authors read off planned-word features on the newline token *before* the line is written, and then show causally that suppressing the preferred plan ("rabbit") makes the model rewrite the line to land on "habit" instead. That is an intervention result in the original model, not just a graph reading — and the paper explicitly notes that interventions on actual model outputs are their strongest form of validation.

Three honest limits:

- Planned-word features were found in **about half** of the poems investigated, not all.
- §14's first bullet applies directly to this result by name: "when we discuss planning in poems, we show a few specific examples in which planning appears to occur. It seems likely that the phenomenon is more widespread, but it's not our intent to make that claim."
- The mechanism is demonstrated for rhyming-poem line endings, a narrow and unusually clean case. It is not evidence of general-purpose forward planning across tasks.

**Honest formulation:** "In Anthropic's circuit-tracing study of Claude 3.5 Haiku, the researchers found that when writing rhyming poetry the model activates features for candidate end-of-line words *before* writing the line — and when they suppressed the model's preferred rhyme, it rewrote the line to reach a different one. They found this in about half the poems they examined, and are careful to present it as evidence about specific examples rather than a general claim about how the model writes."

### Claim (b) — "concepts are represented language-independently"

**Materially weaker in the paper than a flat "language-independent concept representations." Do not state it flat.**

What the paper actually supports:

- Features in the **middle layers** are "more language-agnostic" — a comparative, not an absolute. Features at the input and output ends are "highly language-specific."
- There *are* genuinely shared multilingual features, and the shared core carries the semantic operation (antonym-of-small → large) across English, French and Chinese.
- The degree of sharing **increases with scale** (higher in Haiku than in the smaller model), which is a real and interesting finding.

What the paper says against the flat version:

- "there are important mechanistic ways in which English is privileged."
- "This paints a picture of a multilingual representation in which **English is the default output**."
- Multilingual features wire more strongly to English output nodes; non-English outputs need extra say-X-in-language-Y machinery.
- The underlying evidence is three short parallel prompts, and even there only **10 of 27** multilingual features appear in the pruned attribution graphs for all three.
- §14's blanket scope limit applies: these are existence proofs on specific examples, and the case studies are "a biased sample."

A flat "concepts are represented language-independently" implies a symmetric, language-neutral conceptual interlingua. The paper explicitly rejects that reading in favour of an asymmetric picture with English at the centre. Note also that the paper's own "universal mental language" phrase (Discussion) is hedged — "in a sense" — and sits in the summary prose, not in the results.

**Honest formulation:** "Anthropic found that Claude 3.5 Haiku uses partly shared, language-agnostic machinery in its middle layers — asked for the opposite of 'small' in English, French or Chinese, it runs the same core features before converting to a language-specific output. The sharing increases with model scale. But they stop well short of a neutral interlingua: they report 'important mechanistic ways in which English is privileged,' and describe the picture as one 'in which English is the default output.'"

If the blog needs a single line: **"partially shared, English-centred"** is the defensible characterisation; **"language-independent"** is not.
