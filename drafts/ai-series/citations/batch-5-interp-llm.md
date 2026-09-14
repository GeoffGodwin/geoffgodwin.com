# Batch 5 — Interpretability / LLM mechanics citations

**Verified:** 2026-09-14

## READ THIS FIRST — access constraint affecting every slot in this batch

This session's network egress policy blocked **every scholarly host I tried**:
`transformer-circuits.pub`, `www.anthropic.com`, `arxiv.org`, `export.arxiv.org`,
`ar5iv.labs.arxiv.org`, `dl.acm.org`, `openreview.net`, `aclanthology.org`,
`proceedings.neurips.cc`, `www.semanticscholar.org`, `huggingface.co`,
`cdn.openai.com`, `www.neelnanda.io`, `www.lesswrong.com`, `faculty.washington.edu`,
`web.archive.org`, `en.wikipedia.org`. The proxy README states these are
organization-policy denials and must be reported, not routed around.

The only reachable hosts were `github.com` / `raw.githubusercontent.com`. All
quotations below were therefore taken from **full-text copies of the papers hosted
on GitHub**, and cross-checked against independent copies wherever more than one
existed. That is good evidence but it is **not the same as reading the publisher's
own file**. Per the hard rules, no slot in this batch is marked FIT on the strength
of a mirror alone unless the wording is corroborated across multiple independent
copies; the highest-priority slot (C-18) is marked **FOUND**.

**Action for the author:** every quote below should be re-checked against the
publisher's page before publication. I have given the exact section for each one so
this is a two-minute job per quote.

---

### C-18
- **Status:** FOUND (not FIT — Anthropic's own site was unreachable from this session)
- **Citation:**
  - Lindsey, J., Gurnee, W., Ameisen, E., Chen, B., Pearce, A., Turner, N. L., Citro, C.,
    Abrahams, D., Carter, S., Hosmer, B., Marcus, J., Sklar, M., Templeton, A., Bricken, T.,
    McDougall, C., Cunningham, H., Henighan, T., Jermyn, A., Jones, A., Persic, A., Qi, Z.,
    Thompson, T. B., Zimmerman, S., Rivoire, K., Conerly, T., Olah, C., & Batson, J. (2025).
    "On the Biology of a Large Language Model." *Transformer Circuits Thread*, 27 March 2025.
  - Companion methods paper: Ameisen, E., Lindsey, J., Pearce, A., Gurnee, W., Turner, N. L.,
    Chen, B., Citro, C., Abrahams, D., Carter, S., Hosmer, B., Marcus, J., Sklar, M.,
    Templeton, A., Bricken, T., McDougall, C., Cunningham, H., Henighan, T., Jermyn, A.,
    Jones, A., Persic, A., Qi, Z., Thompson, T. B., Zimmerman, S., Rivoire, K., Conerly, T.,
    Olah, C., & Batson, J. (2025). "Circuit Tracing: Revealing Computational Graphs in
    Language Models." *Transformer Circuits Thread*, 27 March 2025.
- **URL/DOI:**
  - https://transformer-circuits.pub/2025/attribution-graphs/biology.html
  - https://transformer-circuits.pub/2025/attribution-graphs/methods.html
  - (No DOI; Transformer Circuits Thread is self-published, not peer-reviewed. Say so in the post.)
- **Claim needed:** (a) the model plans rhyme words ahead of time rather than choosing
  them only at the end of a line; (b) there are language-independent concept
  representations — a shared conceptual space across languages.

- **(i) Which model was studied:** **Claude 3.5 Haiku** — described in the paper as
  "Claude 3.5 Haiku — Anthropic's lightweight production model." One model, one size.
  Nothing in either paper licenses a claim about "LLMs" in general, or about
  frontier-scale Claude models.

- **Supporting passage — claim (a), rhyme planning** (§4 "Planning in Poems"):
  > "Specifically, the model often activates features corresponding to candidate
  > end-of-next-line words prior to writing the line, and makes use of these features
  > to decide how to compose the line."

  and:
  > "We observe that the model holds multiple possible planned words 'in mind' at the
  > same time."

  The paper also reports "evidence of both forward planning and backwards planning"
  in the same section. *Caution: the copy of that particular sentence I could reach
  is mangled (an unbalanced parenthesis), so do not quote it verbatim without
  re-checking it on Anthropic's page.* The two quotes above came through clean.

- **Supporting passage — claim (b), cross-language representations** (§5 "Multilingual
  Circuits" and §5.5 "Do Models Think in English?"):
  > "Modern neural networks have highly abstract representations which often unify the
  > same concept across multiple languages."

  > "The high-level story of each is the same: the model recognizes, using a
  > language-independent representation, that it's being asked about antonyms of 'small'."

  > "It seems to us that Claude 3.5 Haiku is using genuinely multilingual features,
  > especially in the middle layers. However, there are important mechanistic ways in
  > which English is privileged."

  > "Features at the beginning and end of models are highly language-specific
  > (consistent with the {de, re}-tokenization hypothesis), while features in the middle
  > are more language-agnostic."

- **(ii) What the attribution-graph method can and cannot establish:**
  - It can produce a *local, linearized* description of how one token prediction was
    computed **in a replacement model** (cross-layer transcoder features standing in
    for MLP neurons), and it can be stress-tested by intervening on features and
    checking the output changes as predicted.
  - It **cannot** establish that the real model uses the same mechanism. From the
    methods paper's Limitations section, verbatim:
    > "However, this does not guarantee that the local replacement model and underlying
    > model use the same mechanisms."
  - It **cannot** explain attention. Verbatim from the same section:
    > "Note that these graphs do not contain information about the influence of nodes on
    > other nodes via their influence on attention patterns."
    The method accounts for information flowing from one token position to another but
    not *why* the model moved that information (QK circuits are outside the graph).
  - Unexplained MLP output shows up as "error nodes" in the graphs; sparse coding is
    described as "an imperfect way of identifying features"; pruned graphs still carry
    "hundreds of nodes and tens of thousands of edges."

- **Author-stated limitations the post must repeat** (all from §1.1 "A note on our
  approach and its limitations", quoted verbatim):
  - Hit rate: "we've found that our attribution graphs provide us with satisfying insight
    for **about a quarter of the prompts we've tried**."
  - Selection bias: "The examples we highlight are success cases where we have managed to
    learn something interesting" and "the cases we have chosen to highlight are undoubtedly
    a biased sample shaped by the limitations of our tools."
  - Partiality: "even in our successful case studies, the discoveries we highlight here only
    capture a small fraction of the interpretable 'replacement model,' which incompletely and
    imperfectly captures the original."
  - Presentation is simplified: "we will often present highly distilled and subjectively
    determined simplifications of the picture uncovered by our methods, losing even more
    information in the process."
  - Epistemic status of the findings: "These examples serve as **existence proofs** — concrete
    evidence that specific mechanisms operate in certain contexts. While we suspect similar
    mechanisms are at play beyond these examples, **we cannot guarantee it**."
  - Their own framing of the field: "a preparadigmatic field still in search of the right
    abstractions."

- **Overstatement risk (this is the important part):**
  1. **Claim (b) is materially weaker in the paper than the outline assumes.** The outline
     says "there are language-independent concept representations, a shared conceptual space
     across languages." The paper says middle-layer features are "more language-agnostic,"
     that the model uses "a language-independent representation" *for the specific antonym
     task studied*, and then immediately hedges: "there are important mechanistic ways in
     which English is privileged," concluding that this "paints a picture of a multilingual
     representation in which **English is the default output**." It is a
     partially-shared, English-biased middle layer, not a clean language-neutral concept
     space. Press coverage flattened this into "Claude thinks in a universal language of
     thought"; the paper explicitly does not say that. **Recommend rewriting the outline
     claim to: "middle-layer features are substantially shared across languages, though
     English is mechanistically privileged."**
  2. **Claim (a) is broadly supported but narrower than it sounds.** The paper shows
     candidate rhyme words active *before* the line is written, and that intervening on
     those features changes the line — but the finding is on one model, one poem-completion
     setup, presented as an existence proof, from a method that yields satisfying graphs on
     roughly a quarter of prompts. "The model plans" is fair; "models plan" is not.
  3. Coverage routinely presented attribution graphs as a readout of what the model is
     *actually* doing. They are a readout of a *replacement* model, with the faithfulness
     caveat quoted above, and with attention effects invisible.
  4. Neither paper is peer-reviewed; both are Anthropic self-publications about Anthropic's
     own model. Worth one sentence in the post.

- **Notes / risks:** I could not open transformer-circuits.pub. Quotes above were read from
  a GitHub mirror of the Biology paper (`duoduoyeah/Tracing-the-thoughts-of-a-large-language-model`,
  file `On the Biology of a Large Language Model.md`), which is **truncated after §8** — so
  the paper's own **§14 Limitations** section is unverified by me; the method-limitation
  quotes come instead from a mirror of the companion methods paper
  (`callummcdougall/ARENA_3.0`, `.../papers/attribution_graphs_2025.txt` — Callum McDougall
  is one of the authors). Re-verify all C-18 quotes against Anthropic's own pages, and read
  §14 of the Biology paper directly before publishing.

---

### C-19
- **Status:** FOUND (abstract verified verbatim from the authors' own repo; the paper body,
  including the probing-caveat discussion, could not be opened)
- **Citation:** Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M.
  (2023). "Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic
  Task." *The Eleventh International Conference on Learning Representations (ICLR 2023)*.
  arXiv:2210.13382.
- **URL/DOI:** https://arxiv.org/abs/2210.13382 · https://openreview.net/forum?id=DeG07_TcZvT
- **Claim needed:** a model trained purely on next-token prediction built an internal
  representation of board state it was never trained to have.
- **Supporting passage** (Abstract, verbatim, from the authors' own repository
  `likenneth/othello_world`):
  > "We investigate this question by applying a variant of the GPT model to the task of
  > predicting legal moves in a simple board game, Othello. Although the network has no a
  > priori knowledge of the game or its rules, we uncover evidence of an emergent nonlinear
  > internal representation of the board state."

  and:
  > "Interventional experiments indicate this representation can be used to control the
  > output of the network and create 'latent saliency maps' that can help explain
  > predictions in human terms."

- **Author-stated limitations the post must repeat:**
  - **(a) Synthetic task, small model.** The paper's own subtitle is "…Trained on a
    Synthetic Task." The model is an 8-layer GPT variant (8 attention heads, 512-dim
    hidden state) over a 60-token move vocabulary — not a language model in any
    ordinary sense. Two training sets: ~139k championship games, and 20M synthetic
    games sampled uniformly from the Othello game tree. *(Architecture and dataset
    figures are from third-party notes on the paper, not from the paper itself —
    verify before printing numbers.)*
  - **(b) Probing methodology.** The representation was recovered by **nonlinear**
    (MLP) probes; **linear probes performed poorly** (reported at >20% error) in the
    original paper, which is why the paper says "nonlinear." The authors did not rest
    on probes alone — they added *interventional* experiments (edit the activation to a
    counterfactual board, see the move predictions change accordingly), which is the
    part that makes the result more than correlational. **The post should not cite the
    probe result without the intervention result**; a probe on its own shows only that
    the information is decodable, not that the model uses it.
  - **(c) The follow-up both strengthens and qualifies.** Nanda, N., Lee, A., &
    Wattenberg, M. (2023), "Emergent Linear Representations in World Models of
    Self-Supervised Sequence Models," *BlackboxNLP 2023* (pp. 16–30). Abstract, verbatim
    (from the official ACL Anthology XML in `acl-org/acl-anthology`):
    > "Prior work suggests that Othello-playing neural network learned nonlinear models
    > of the board state (Li et al., 2023a). In this work, we provide evidence of a
    > closely related linear representation of the board. In particular, we show that
    > probing for 'my colour' vs. 'opponent's colour' may be a simple yet powerful way
    > to interpret the model's internal state. This precise understanding of the
    > internal representations allows us to control the model's behaviour with simple
    > vector arithmetic."

    **Net effect: it strengthens the world-model claim and qualifies the description of
    it.** The representation is there and is *more* legible than Li et al. thought —
    linear, once you use the right basis (mine/theirs rather than black/white). The
    lesson is that the original paper's "nonlinear" was an artifact of the probe's
    coordinate system, not a property of the model. If the post says "nonlinear
    representation," it is repeating a claim the follow-up corrected.
- **Overstatement risk:** the popular reading is "LLMs build world models, proven." What
  was shown is that *one small transformer on a fully synthetic, rule-governed, perfectly
  observable game* built a causally-used representation of the game's state. It is a strong
  existence proof against "surface statistics only" — which is exactly how the authors
  frame it — and nothing more. Generalising it to natural-language models is an argument
  the post must make on its own, not a result it can cite.
- **Notes / risks:** arXiv and OpenReview were both blocked; the abstract above is from the
  first author's own GitHub repo and matches the ACL/OpenReview metadata. I could not read
  §7 / the paper's own limitations discussion, so any caveat the authors state there is not
  captured here.

---

### C-17
- **Status:** FOUND (wording corroborated across several independent copies; the OpenAI PDF
  itself was unreachable)
- **Citation:** Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. (2019).
  "Language Models are Unsupervised Multitask Learners." OpenAI technical report.
- **URL/DOI:** https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
  (no DOI; not peer-reviewed)
- **Claim needed:** the pretraining objective is next-token prediction.
- **Supporting passage** (§2 "Approach", opening paragraph, verbatim):
  > "At the core of our approach is language modeling. Language modeling is usually framed
  > as unsupervised distribution estimation from a set of examples… Since language has a
  > natural sequential ordering, it is common to factorize the joint probabilities over
  > symbols as the product of conditional probabilities."

  followed by equation (1): p(x) = ∏ p(sₙ | s₁, …, sₙ₋₁).
- **Author-stated limitations the post must repeat:** none needed for this narrow claim.
- **Overstatement risk:** low. One thing to avoid: "trained to predict the next word"
  describes *pretraining only*. Deployed assistant models have been through instruction
  tuning and RLHF on top, so "an LLM is just a next-word predictor" is true of the base
  model and misleading about the product.
- **Notes / risks:** **Recommendation — use GPT-2 for the claim but do not quote §2 to a lay
  reader.** The passage above is the plainest *primary* statement of the objective, but it is
  written in distribution-estimation language and will read as jargon. Options: (a) quote it
  and gloss it in your own words; (b) quote Brown et al. 2020's plainer framing of GPT-3 as
  "an autoregressive language model" (see C-24 for the verified wording) and cite Radford
  et al. 2019 as the objective's source. I'd do (a) — one sentence of quote, one of gloss.
  Wording above was corroborated across three independent GitHub copies of the paper text.

---

### C-20
- **Status:** FOUND (quotes corroborated across four independent copies with page numbers;
  the ACM DL page was unreachable)
- **Citation:** Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021).
  "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜" In *Proceedings
  of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21)*,
  pp. 610–623. ACM.
- **URL/DOI:** https://doi.org/10.1145/3442188.3445922
- **Claim needed:** state the stochastic-parrot position fairly, in the authors' own terms.
- **Supporting passage — the definition** (p. 617, verbatim):
  > "Contrary to how it may seem when we observe its output, an LM is a system for
  > haphazardly stitching together sequences of linguistic forms it has observed in its vast
  > training data, according to probabilistic information about how they combine, but
  > without any reference to meaning: a stochastic parrot."
- **Supporting passage — their claim about meaning and understanding** (≈p. 616, verbatim):
  > "Text generated by an LM is not grounded in communicative intent, any model of the
  > world, or any model of the reader's state of mind. It can't have been, because the
  > training data never included sharing thoughts with a listener, nor does the machine
  > have the ability to do that."
- **Supporting passage — the paper's own framing of its purpose** (§1, verbatim):
  > "We ask whether enough thought has been put into the potential risks associated with
  > developing them and strategies to mitigate these risks."
- **What the paper is actually mostly about (do not reduce it to one line):** the
  stochastic-parrot argument is **one section of a multi-part risk paper**, and arguably
  not its main subject. The paper covers, in order: (1) the trend toward ever-larger LMs;
  (2) **environmental and financial costs** of training (drawing on Strubell et al.), and
  who bears them; (3) **"unfathomable" training data** — web-scale corpora that
  overrepresent hegemonic viewpoints, plus the "documentation debt" of datasets too large
  to document after the fact, and the way naive toxicity filtering suppresses
  marginalised (e.g. LGBTQ) discourse; (4) **research opportunity cost** — scale crowding
  out other work; (5) the **illusion of meaning** — coherence supplied by the human reader,
  not the model (this is where the stochastic parrot appears), and downstream harms
  including automated disinformation and machine-translation errors; (6) a **path forward**
  — documentation, dataset curation, model cards and datasheets, pre-development impact
  analysis, value-sensitive design. A post that presents the paper as "the paper that said
  LLMs are just parrots" misrepresents roughly five-sixths of it.
- **Overstatement risk:** the usual distortion runs in *both* directions. Critics reduce it
  to a slogan and then attack the slogan; supporters cite it as if it had proved LLMs cannot
  mean anything. The paper's actual argument about meaning is an **in-principle argument
  about form vs. communicative intent and grounding** — the fuller version of which is
  Bender & Koller (2020), "Climbing towards NLU" (ACL) — not an empirical result about
  model internals. Stating it as a position, with its warrant, is the fair treatment.
  Note also: the published FAccT version lists four authors (Shmitchell is a pseudonym;
  Margaret Mitchell is widely reported as the fourth author, and some secondary copies list
  her by name — cite the four names as published).
- **Notes / risks:** DOI and page range are confirmed from multiple independent
  bibliographies. Page numbers on the two quotes come from a page-anchored Zotero export and
  a textbook citation (p. 617 for the definition); verify before printing page numbers.

---

### C-24
- **Status:** **Split.** FIT for "weights are not updated at inference." **MISFIT** for
  "in-context learning does not persist across sessions" — no source I reached states that.
- **Citation:** Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P.,
  Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. (2020). "Language Models are
  Few-Shot Learners." *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*.
  arXiv:2005.14165.
- **URL/DOI:** https://arxiv.org/abs/2005.14165
- **Claim needed:** deployed model weights are fixed at inference time, and in-context
  learning does not persist across sessions.
- **Supporting passage** (Abstract, verbatim — corroborated across five independent copies):
  > "For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks
  > and few-shot demonstrations specified purely via text interaction with the model."

  §2.1, definition of the few-shot setting, verbatim:
  > "Few-Shot (FS) is the term we will use in this work to refer to the setting where the
  > model is given a few demonstrations of the task at inference time as conditioning
  > [RWC+19], but **no weight updates are allowed**."

  Related-work section, verbatim (this is the cleanest single sentence for the post):
  > "an inner loop of adaptation takes place through computation in the model's activations
  > across timesteps, **without updating the weights**, while an outer loop… updates the
  > weights."
- **Author-stated limitations the post must repeat:** the GPT-3 statements are descriptions
  of *the paper's own evaluation protocol*, not a general claim about how all deployed
  systems work. They establish that in-context learning happens in activations rather than
  weights. They say nothing about session boundaries, memory features, or retrieval.
- **Overstatement risk:** the second half of the claim is where the post can go wrong.
  "In-context learning does not persist across sessions" is an **inference** from (i) weights
  are not updated and (ii) the context window is the only carrier of state — it is not
  something GPT-3's authors asserted, and it is now **empirically false of many deployed
  products**, which bolt on persistent memory, retrieval, and periodic fine-tuning outside
  the model. Suggested safe formulation: *"Nothing learned in the conversation is written
  back into the model's weights; anything that carries over between sessions is a separate
  system storing text and replaying it into the context."* That is defensible and matches
  the source.
- **Notes / risks:** I looked for a peer-reviewed continual-learning survey stating the gap
  plainly. The best candidate is **Shi, H., Xu, Z., Wang, H., Qin, W., Wang, W., Wang, Y.,
  Wang, Z., Ebrahimi, S., & Wang, H., "Continual Learning of Large Language Models: A
  Comprehensive Survey," *ACM Computing Surveys* (2025), DOI 10.1145/3735633** (arXiv
  2404.16789). Publication venue and DOI verified via the authors' companion GitHub repo;
  **I could not read the text**, so I cannot supply a quote and cannot confirm it states the
  claim in the form you need. Marked FOUND, not FIT — do not cite it for a specific sentence
  without opening it. Recommendation: lead with the GPT-3 quotes above, which are direct.

---

### C-28
- **Status:** FIT for the architectural half of the claim; the claim **as currently worded
  goes beyond the paper** and needs a second source (use C-24).
- **Citation:** Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N.,
  Kaiser, Ł., & Polosukhin, I. (2017). "Attention Is All You Need." *Advances in Neural
  Information Processing Systems 30 (NIPS 2017)*, pp. 5998–6008. arXiv:1706.03762.
- **URL/DOI:** https://arxiv.org/abs/1706.03762
- **Claim needed:** the transformer is feedforward per token and carries no persistent
  internal state between forward passes beyond the context itself.
- **Supporting passage** (Abstract, verbatim):
  > "We propose a new simple network architecture, the Transformer, based solely on attention
  > mechanisms, dispensing with recurrence and convolutions entirely."

  §1 Introduction, on what is being dispensed with, verbatim:
  > "they generate a sequence of hidden states ht, as a function of the previous hidden state
  > ht−1 and the input for position t. This inherently sequential nature precludes
  > parallelization within training examples."

  §3.1/§3.2 on how state is carried instead, verbatim:
  > "At each step the model is auto-regressive, consuming the previously generated symbols as
  > additional input when generating the next."

  §3.3 "Position-wise Feed-Forward Networks", verbatim:
  > "In addition to attention sub-layers, each of the layers in our encoder and decoder
  > contains a fully connected feed-forward network, which is applied to each position
  > separately and identically."
- **Author-stated limitations the post must repeat:** the paper is a 2017 machine-translation
  architecture paper (WMT14 En-De / En-Fr, plus English constituency parsing). It makes no
  claims about deployed language-model assistants, sessions, or memory.
- **Overstatement risk / FIT-CHECK result — read this:**
  1. **What the paper supports:** the architecture has **no recurrent hidden state**
     ("dispensing with recurrence… entirely"), and the feed-forward sub-layer is applied
     "to each position separately and identically." So "feedforward per token, no recurrence"
     is squarely supported, in the authors' own words.
  2. **What the paper does *not* say:** it never claims the model "carries no persistent
     internal state between forward passes." That is a statement about *inference-time
     deployment*, a topic the paper does not address. It is true of the architecture, but the
     paper isn't the place it is asserted.
  3. **A precision trap worth avoiding.** The paper's own §3 sentence says the decoder is
     auto-regressive, "consuming the previously generated symbols as additional input" —
     i.e. state is carried forward **as tokens re-fed into the next forward pass**, which is
     exactly your point. But note that real deployed inference uses a **KV cache**, which
     *is* state carried between forward passes within one generation. It is derived entirely
     from the context tokens and is discarded afterwards, so your claim survives — but if you
     write "no state whatsoever between forward passes," a technical reader will object.
     Safer wording: *"nothing carries from one forward pass to the next except the token
     sequence itself."*
  4. **Recommendation:** cite Vaswani et al. for "no recurrence / per-token feedforward," and
     pair it with the GPT-3 quotes in C-24 for "weights are not updated at inference." One
     source per half of the claim.
- **Notes / risks:** quotes taken from GitHub-hosted full-text copies of 1706.03762v7,
  cross-checked against several independent copies of the abstract and introduction. The
  abstract's BLEU figure differs between the arXiv v1 (41.0) and later versions (41.8) — not
  relevant to your claim, but don't quote BLEU numbers without checking which version.
