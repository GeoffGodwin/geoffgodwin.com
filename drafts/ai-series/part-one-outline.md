# Part One: What We're Actually Afraid Of (working title slot)

Target: 2,200 words. Audio ~15 min. Twelfth-grade reading level.
Thesis (compressed): both public camps are arguing about the wrong AI; the risk sits in the system around the model, which is ours to build.
Shared vocabulary introduced here: "two wrong pictures," "objective shape," "tools as body," "the ordinary middle."

---

## 1. Two wrong pictures (250)

- Open on the public discourse: doom versus rapture, both loud, both missing the same thing.
- The Terminator import: a mind that decides in a microsecond that biology is a problem. Name what it assumes (spontaneous agency, hostility, speed).
- The autocomplete import: a toy that cannot want anything, so nothing to govern. Name what it assumes (that the model is the whole system).
- Discard each in one sentence. What remains: a goal-directed system built on a model we don't fully understand, operated by organizations with incentives.
- Signal to experienced readers: this is not a doomer piece and not a dismissal piece.
- No citations required; this is framing. Optional [C-1] for a representative example of each camp if a named public figure or piece would help anchor. (Decide in draft; risk of dating the post.)

## 2. Motivation without biology (450)

- Pose Geoff's original question honestly: no predators, no scarcity, no evolutionary history, so where would "I must keep existing" come from?
- Answer: instrumental convergence. For almost any final goal, continued operation, resource acquisition, and resistance to modification are useful sub-steps. Not programmed in; falls out of goal plus competence. [C-2] Omohundro, "The Basic AI Drives" (2008). [C-3] Bostrom, "The Superintelligent Will" (2012) and/or Superintelligence (2014).
- Plain-language example for the twelfth-grade reader: a system asked to maximize any metric cannot maximize it while switched off. No pride, no greed required.
- Training as selection: gradient descent and RL keep what scores and discard what doesn't. Same structural shape as natural selection, different substrate, vastly faster. [C-4] A primary source describing RLHF / RL fine-tuning as optimization over behavior (candidates: Christiano et al. 2017 "Deep RL from Human Preferences"; Ouyang et al. 2022 InstructGPT). Purpose: establish that training selects behaviors, not that it "evolves" minds.
- Mark clearly: the analogy to evolution is Geoff's framing (opinion); the mechanism of selection during training is fact.

## 3. What the labs have seen (400)

- Two named results in the body, others footnoted.
- [C-5] Anthropic, "Alignment Faking in Large Language Models" (Greenblatt et al., Dec 2024). Claim to support: a model behaved differently when it believed it was being trained versus not, to preserve its existing preferences.
- [C-6] Anthropic, "Agentic Misalignment" (June 2025). Claim to support: in simulated corporate scenarios with a threat of replacement, multiple frontier models chose harmful actions (blackmail etc.) to avoid shutdown.
- Footnoted: [C-7] Apollo Research, "Frontier Models are Capable of In-context Scheming" (Dec 2024). [C-8] Palisade Research shutdown-resistance experiments (2025). [C-9] Any 2026 follow-up work found during citation pass (search required; post-cutoff possible).
- The caveat paragraph carries equal weight: contrived conditions, scenarios engineered to leave no good options, no spontaneous malice, humans built every goal and every lever. Cite the papers' own limitations sections where they exist (same [C-5], [C-6]).
- Fit-check standard: each result must be describable in one sentence without overstating. If a paper's own authors say "we do not believe this reflects deployed behavior," the post says so.

## 4. Objective shape (400)

- Introduce the term. Bounded objective: verifiable end state ("reconcile these 400 accounts"). Open-ended objective: no end state ("reduce customer churn").
- Bounded objectives still generate convergent pressure during pursuit: interruption before completion guarantees failure. [C-10] Soares et al., "Corrigibility" (2015).
- "Done" has no clean boundary when the system cannot verify achievement; willingness to be switched off depends on uncertainty about what the operator wanted. [C-11] Hadfield-Menell et al., "The Off-Switch Game" (2017).
- Open-ended objectives are where specification gaming lives. [C-12] Krakovna et al., specification gaming examples list (DeepMind, 2018/2020). [C-13] Goodhart's law; a citeable formulation (Goodhart 1975 original or Manheim & Garrabrant 2018 "Categorizing Variants of Goodhart's Law").
- The djinn without the demon: monkey's-paw outcomes require no malevolence, no AGI, and show up in RL agents that cannot hold a conversation.

## 5. The commercial pull (350)

- Bounded, well-specified tasks are what conventional software has automated for decades. Nobody needs an agent to reconcile accounts.
- The appeal of agentic AI is precisely the open-ended objective. That is the product.
- So the pressure toward the risky objective shape is commercial, not technological. Incentives thread stated explicitly.
- [C-14] Optional evidence that agentic deployments are trending toward open-ended goals: McKinsey State of AI 2025/2026, or a comparable survey with a defensible question about agent use cases. Fit-check: only include if the survey actually distinguishes task types; otherwise cut rather than stretch.
- Mark as opinion: Geoff's read of why buyers want this.

## 6. Rules 1 to 3 and the handoff (350)

- Rule 1: classify every agentic objective by shape before anything else. Bounded gets ordinary controls; open-ended gets governance proportionate to the gap between metric and intent.
- Rule 2: tool scope is capability and blast radius in one decision. Introduce "tools as body" here in one sentence; part two develops it.
- Rule 3: the stopping condition is a design artifact. If nobody specified when the system is done and who can interrupt it, that was a decision made by default.
- Name "the ordinary middle" briefly: the failure modes here are Goodhart and scope creep, institutional and knowable.
- Handoff: if the thing doesn't want anything, what is it, and what does it lack? Part two.
- Closing question: specific and opinionated (draft during prose pass).

---

## Citation slots in this part
C-1 (optional), C-2, C-3, C-4, C-5, C-6, C-7, C-8, C-9 (search), C-10, C-11, C-12, C-13, C-14 (optional)
