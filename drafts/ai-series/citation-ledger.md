# Citation Ledger (both parts)

**Phase 1 status: complete as far as this environment allowed, and not complete
to the standard the procedure specifies.** Document fetching was blocked by the
network egress proxy for every publisher and preprint host. Bibliography,
identifiers and venue are established and cross-checked. Claim confirmation was
possible only at the level of abstracts, or of full text mirrored on GitHub for
the batch 5 slots. No slot has been checked against a publisher's source of
record. See `citations/README.md` and `citations/verification-notes.md`.

Status key: FIT (evidence supports the claim as stated) / MISFIT (does not, or
only with a stretch) / FOUND (located, claim unconfirmed) / CUT.

Evidence key: **G** GitHub-mirrored full text / **A** published abstract /
**S** search metadata only. Nothing carries publisher-verified full text.

| Slot | Part | Status | Ev | Notes |
|---|---|---|---|---|
| C-1 | 1 | CUT | S | Dating risk, and the dismissive bucket has no occupant who can be labelled that way fairly. Describe the disagreement without names. |
| C-2 | 1 | FOUND | S | Omohundro 2008, FAIA vol. 171, IOS Press, pp. 483-492. No DOI exists; the ACM 10.5555 string is not one. His derivation runs through self-improvement, so "goal plus competence" may compress it. |
| C-3 | 1 | FOUND | S | Bostrom 2012, DOI 10.1007/s11023-012-9281-3. Prefer the paper to the book: short, free, peer-reviewed, and it does not drag the takeoff framework along. |
| C-4 | 1 | FOUND | S | Prefer Ouyang et al. 2022 to Christiano et al. 2017: it is the LLM paper, the scored unit is an output, and it is recognisable as ChatGPT's method. Evolution-analogy fit-check not discharged. |
| C-5 | 1 | FOUND | S | Greenblatt et al., arXiv:2412.14093. Body citation. Two things the post must carry: the model's belief about training is planted in its prompt rather than inferred, and the replication finds the effect in a minority of models. See C-34. |
| C-6 | 1 | FOUND | S | Anthropic, June 2025. Body citation. The authors reportedly concede they red-teamed iteratively until harmful behaviour became likely; the post must not present as discovery what the authors describe as engineered. Disclaimers unquoted. |
| C-7 | 1 | FOUND | S | Apollo Research, arXiv:2412.04984. Footnote. Outline wording already matches the authors' capability-versus-propensity framing; do not shorten it to "models scheme." |
| C-8 | 1 | FOUND | S | **Retitled.** Schlatter, Weinstein-Raun and Ladish, "Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs," arXiv:2509.14260, TMLR 2026. The retitle supports the instrumental-convergence reading; consider promoting from footnote. Conflicting figures unresolved, see notes. |
| C-9 | 1 | FOUND | S | Not empty. Alignment Faking Revisited, the evaluation-awareness qualification, and Anthropic's summer 2026 extension. See C-34 and C-35. |
| C-10 | 1 | FOUND | S | Soares et al. 2015. Author order contested. Do not swap in Orseau and Armstrong 2016: their headline result is positive and the rhetorical shape is wrong for the claim. |
| C-11 | 1 | FOUND | S | Hadfield-Menell et al., IJCAI-17 pp. 220-227, DOI 10.24963/ijcai.2017/32. Cleanest bibliography in the set. A formal result with modelling assumptions; do not present as an empirical finding about deployed systems. |
| C-12 | 1 | FOUND | S | DeepMind post 2020-04-21 plus Krakovna's master list. Chosen examples: CoastRunners boat (Clark and Amodei, OpenAI, 2016) with solid provenance, and the Lego block flip (Popov et al., arXiv:1704.03073) whose detail is unconfirmed. Drop the second if the paper does not describe it. |
| C-13 | 1 | FOUND | S | **Attribution trap.** "When a measure becomes a target" is Strathern 1997, European Review 5(3): 305-321, glossing Goodhart. Which 1975 Goodhart paper carries the original is unresolved; the 1984 Macmillan reprint sidesteps it. Credit both, explicitly. |
| C-14 | 1 | CUT | S | No candidate survey has a bounded-versus-open-ended axis. Worse, the available evidence suggests what reaches production is narrow while open-ended deployments stall, which cuts against the section as worded. Keep the claim as opinion about appetite, not deployment. |
| C-15 | 2 | FOUND | S | Russell and Norvig 4th ed., ISBN 978-0134610993, section 1.1.1, where the six subfields are named. Prefer to the AI Index: a definition rather than a measurement, and it does not date. |
| C-16 | 2 | FOUND | S | Weizenbaum 1966, CACM 9(1) 36-45, DOI 10.1145/365153.365168. Use alone. No clean modern fit found; 2022-2026 candidates measure anthropomorphism, trust and anxiety rather than attribution of understanding. |
| C-17 | 2 | FOUND | G | GPT-2 section 2. Distribution-estimation jargon, so quote one sentence and gloss it. Flag that next-token prediction describes pretraining, not the RLHF'd product. |
| C-18 | 2 | **MISFIT as worded** | G | See the report below. Claim (a) holds for one model. Claim (b) is materially weaker in the paper than the outline assumes. |
| C-19 | 2 | FOUND | G | Li et al., ICLR 2023. Original probes were nonlinear; the causal weight sits in the intervention experiments, not the probes. Nanda et al., BlackboxNLP 2023 pp. 16-30, corrects the representation to linear in the right basis. Cite both or the post states a claim the field revised. |
| C-20 | 2 | FOUND | G | Bender et al., DOI 10.1145/3442188.3445922, pp. 610-623. Definition on p. 617. Scope note: the parrot argument is one section of six; the paper is mostly about environmental cost, training-data documentation and opportunity cost. |
| C-21 | 2 | FIT | A | Cowan 2001, DOI 10.1017/S0140525X01003922. Abstract carries "three to five chunks" with the boundary conditions. Needs the rider: only when rehearsal and chunking are prevented. |
| C-22 | 2 | FIT | A | Loftus and Palmer 1974, chosen over Bartlett and Schacter. The abstract's own last sentence uses "reconstruction." Solid post-replication-crisis. |
| C-23 | 2 | FIT | A | Diekelmann and Born 2010, DOI 10.1038/nrn2762. Prefer or add Klinzing, Niethard and Born 2019, DOI 10.1038/s41593-019-0467-3. Quantitative claims have weakened since; the qualitative asymmetry the post needs survives. |
| C-24 | 2 | **Split FIT / MISFIT** | G | GPT-3's "no weight updates are allowed" is direct and supports the frozen-weights half. "Does not persist across sessions" is an inference the authors do not make and is false of products with bolt-on memory. Reword. |
| C-25 | 2 | **MISFIT as worded** | A | Raichle et al. 2001, DOI 10.1073/pnas.98.2.676. "The DMN is highly active at rest" is the press version. The paper defines a baseline and identifies the DMN by task-induced decreases. The brains-don't-idle point lives in Raichle and Mintun 2006, DOI 10.1146/annurev.neuro.29.051605.112819. |
| C-26 | 2 | **MISFIT as worded** | A | Clark 2013, DOI 10.1017/S0140525X12000477. The abstract supports continuous prediction against input, not "without task input." That claim needs Berkes et al. 2011, DOI 10.1126/science.1195870. A BBS target article with serious critics; do not present as settled. |
| C-27 | 2 | CUT | A | Friston 2010. Adds formalism and an unfalsifiability controversy, buys nothing for this audience. |
| C-28 | 2 | FIT (architecture only) | G | Vaswani et al. "Dispensing with recurrence and convolutions entirely" supports feedforward-per-token. The paper says nothing about persistent state between passes, and real inference uses a KV cache, which is state derived from context. Reword to "nothing carries from one forward pass to the next except the token sequence itself." |
| C-29 | 2 | CUT | S | Dehaene and Changeux 2011 correctly identified but imports consciousness science and invites the question the post does not want. The architectural rebuttal is cheaper: transformers are massively parallel internally and autoregressive only at the output. |
| C-30 | 2 | FOUND | A | Damasio and Carvalho 2013, DOI 10.1038/nrn3403, for the narrow biological point. Man and Damasio 2019, DOI 10.1038/s42256-019-0103-7, does more work but is a design proposal for machines with homeostatic motivation; see verification notes. Attribute, do not assert: contested by LeDoux and Barrett. |
| C-31 | 2 | FOUND | S | Harnad 1990, DOI 10.1016/0167-2789(90)90087-6, for the problem. Harnad 2025, "Language writ large," Frontiers in AI, DOI 10.3389/frai.2024.1490698, for the application to LLMs. Cite both; the second pre-empts the written-before-the-technology objection. Written as a dialogue with ChatGPT-4. |
| C-32 | 2 | CUT | S | No neutral source documents the "it understands" marketing move specifically; FTC actions cover claiming AI you don't have and unsubstantiated performance. Assert the pattern in your own voice. Do not use the SEC source: it names two financial-services firms. |
| C-33 | 2 | FOUND | S | Parasuraman and Manzey 2010, DOI 10.1177/0018720810376055. A review of two decades, which is exactly the institutional-and-decades-old shape the argument needs; cite the year and the word "review." Usage warning: "complacency" reads as blame inside a bank, inverting the finding. |

## New slots opened by the pass

| Slot | Part | Claim the source must support | Source | Status | Notes |
|---|---|---|---|---|---|
| C-34 | 1 | Alignment faking appears in a minority of models, not as a general property | Hughes et al., "Alignment Faking Revisited"; peer-reviewed companion "Why Do Some Language Models Fake Alignment While Others Don't?", arXiv:2506.18032, NeurIPS 2025 | FOUND | Reported figures conflict: batch 2 said 3 of 16, search indicates 5 of 25. Either way a minority result. Required to keep C-5 honest. |
| C-35 | 1 | This class of misalignment research overinterprets model behaviour | Gupta et al., "Position: Anthropomorphic Misalignment Research Needs Stronger Evidence," arXiv:2606.07612, ICML 2026 oral | FOUND | Engage in section 3, do not footnote. The strongest available support for the caveat paragraph carrying equal weight. |
| C-36 | 1 | Evaluation awareness qualifies results across the literature | OpenAI and Apollo anti-scheming work; METR; UK AISI | FOUND | Unresolved identifiers. The 2024-25 results came from models less able to tell they were being tested. Relevant to the caveat paragraph. |

## What must be done before drafting can meet the stated standard

Open these and read them. Nothing else on this list matters as much.

1. C-18, both papers, including the Biology paper's section 14 limitations, which the batch could not reach.
2. C-6, for the two disclaimer sentences the caveat paragraph depends on.
3. C-8, to resolve the conflict between the reported precedence-clause fix and the reported 97% figure.
4. C-5 and C-34 together, to fix the body sentence's scope.
5. C-13, to settle which 1975 paper.
6. C-12, to confirm or drop the Lego flip.
