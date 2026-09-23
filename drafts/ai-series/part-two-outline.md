# Part Two: What Comprehension Would Require (working title slot)

Target: 2,200 words. Audio ~15 min. Twelfth-grade reading level.
Thesis (full, delivered in section 6): both extremes assume the model is the whole story; the failure modes are institutional and knowable; that is the grounds for measured confidence.
Shared vocabulary reused from part one: "two wrong pictures," "objective shape," "tools as body," "the ordinary middle." Introduced here: "the fluency error," "definition by absence."

---

## 1. The fluency error (250)

- One-sentence callback to part one (readable without it).
- AI is a field; LLMs are a product within it. The public has collapsed the first into the second. [C-15] A neutral definitional source for the breadth of AI as a discipline (candidates: Russell & Norvig, AI: A Modern Approach; or a Stanford AI Index framing). Purpose: establish scope, not argue.
- The "sounds like a duck" test: people conclude comprehension from fluent conversation. Name it as the fluency error: a test of output quality mistaken for a test of mind.
- Optional [C-16]: evidence that people attribute understanding to fluent systems (candidates: ELIZA effect, Weizenbaum 1966/1976; or recent survey work on anthropomorphism of chatbots). Fit-check: prefer a primary study over commentary.

## 2. Giving the other side its due (350)

- "Word guessing machine" is accurate about the training objective. State the objective plainly: predict the next token. [C-17] A primary source for the pretraining objective (candidates: Radford et al. 2019 GPT-2 paper; Brown et al. 2020 GPT-3).
- It is misleading about the trained system. Interpretability results:
  - [C-18] Anthropic, "On the Biology of a Large Language Model" / circuit tracing (March 2025). Claims to support: planning rhyme words ahead of time; language-independent concept representations.
  - [C-19] Li et al., "Emergent World Representations" (Othello-GPT, ICLR 2023). Claim to support: a next-token model built an internal board-state representation it was never trained to have.
- The stochastic parrot position stated fairly as a real academic position. [C-20] Bender et al., "On the Dangers of Stochastic Parrots" (2021).
- The pivot: none of these results, on either side, touch the four properties that follow. Fluency and internal representation are orthogonal to them.

## 3. Four properties (700)

Each property: what biological cognizers have, the common misconception, the real asymmetry, why LLM-plus-memory-plus-loop still lacks it.

### 3a. Continuous learning
- Correction first: brains are lossy and windowed too. Working memory holds roughly four chunks. [C-21] Cowan (2001), "The magical number 4." (Miller 1956 as the older seven figure, optional.) Memory is reconstructive, not recorded. [C-22] Bartlett (1932) Remembering; or Schacter, "The Seven Sins of Memory" (1999/2001); or Loftus misinformation-effect work (Loftus & Palmer 1974). Pick one, prefer the most accessible.
- The real asymmetry: consolidation. Brains compress experience into long-term structure, notably during sleep. [C-23] A primary or review source on memory consolidation during sleep (candidates: Diekelmann & Born 2010, "The memory function of sleep," Nature Reviews Neuroscience).
- Deployed model weights are frozen; nothing learned in a conversation changes the model. [C-24] A source establishing that inference does not update weights / in-context learning does not persist (candidates: the GPT-3 paper's own description of in-context learning; or a survey on continual learning in LLMs that states the gap). Fit-check: must state plainly that weights are fixed at inference.
- Why memory graphs don't close the gap: retrieval is not learning; the model reading its notes is not the model changing.

### 3b. Endogenous activity
- Correction first: brains do not idle. The default mode network is highly active at rest. [C-25] Raichle et al. (2001), "A default mode of brain function," PNAS.
- Predictive processing: cortex continuously generates expectations even without a task. [C-26] Clark (2013), "Whatever next? Predictive brains, situated agents," BBS. Optional [C-27] Friston (2010), free energy principle, Nature Reviews Neuroscience. Fit-check: cite Clark for the accessible claim, Friston only if needed.
- Note the point of agreement: the brain is also a prediction machine. The difference is not prediction; it is architecture and learning.
- The real asymmetry: between calls, a model does nothing at all. A transformer is feedforward per token, carrying no internal state between tokens except the text itself. [C-28] Vaswani et al. (2017), "Attention Is All You Need," for the architecture. Brains are recurrent with persistent dynamics.
- Why sub-agents don't close the gap: each is another stateless call. A bureaucracy, not a mind.
- Avoid: any claim that the brain is "parallel" and the model "serial" (invites global workspace objections). Optional [C-29] Dehaene, global workspace, only if the objection needs pre-empting.

### 3c. Intrinsic stakes
- Biological goals are homeostatic: the organism has them because of what it is. [C-30] Damasio (candidates: The Strange Order of Things, 2018; or Damasio & Carvalho 2013, "The nature of feelings," Nature Reviews Neuroscience).
- A model's goals arrive in a prompt and leave with it. Nothing is at stake for the system.
- Consequence for the reader: the system never gets tired, bored, or resentful, and never notices anything nobody asked about. (Pays off as Rule 5.)
- Mark as opinion: whether intrinsic stakes are necessary for comprehension is Geoff's position; that models lack them is fact.

### 3d. Grounding
- Symbol grounding: meaning tied to sensorimotor contact with a world. [C-31] Harnad (1990), "The Symbol Grounding Problem," Physica D.
- Tools as body: for a deployed system, its integrations are its senses and limbs. Its world is exactly what its tools can perceive and touch.
- The distributed-system paragraph: a system running in many places at once has a different shape of world than a body does; its peripherals shape what it can notice and how it acts. Mark as opinion.
- Why this pays off practically: change the tools, change the world. (Pays off as Rule 6.)

## 4. What this doesn't settle (250)

- Definition by absence, not a theory of mind.
- Whether internal representations count as understanding is genuinely open. The public error is treating it as settled in the yes direction; the dismisser's error is treating it as settled in the no direction.
- Interpretability results are real and do not move any of the four properties.
- No citations required; this is Geoff's epistemic position stated plainly.

## 5. The commercial pull (300)

- Mirror of part one section 5 by mechanism: part one was what operators are tempted to deploy; this is what buyers are tempted to believe.
- Vendors sell understanding because it is what buyers want to hear; the market rewards the fluency error.
- Optional [C-32]: an example of vendor marketing language claiming understanding or reasoning. Fit-check: only if it can be cited neutrally without naming a competitor or partner of Geoff's employer. Likely safer to describe the pattern without a citation. Decide in draft.

## 6. Rules 4 to 6, the chaff, and the close (350)

- Rule 4: interrogate the plumbing, not the model. Memory, retrieval, tools, and who maintains them are where "understanding your customers" actually lives.
- Rule 5: monitoring is the substitute for the conscience the system lacks. It will not flag its own drift.
- Rule 6: when the system's tools change, its world changes. Re-evaluate scope, risk, and objective shape together.
- The chaff, named explicitly: AGI timeline debates, benchmark leaderboards, "reasoning" as a product word, headline job-loss forecasts. None change a single rule above.
- The ordinary middle in full: the failure modes are Goodhart, automation bias, accountability gaps; institutional, decades-old, imperfectly but knowably governed. Optional [C-33] automation bias (candidates: Parasuraman & Manzey 2010, "Complacency and bias in human use of automation," Human Factors).
- Both extremes assume the model is the whole story. Measured confidence, with a bill attached.
- Closing question: specific and opinionated (draft during prose pass).

---

## Citation slots in this part
C-15, C-16 (optional), C-17, C-18, C-19, C-20, C-21, C-22, C-23, C-24, C-25, C-26, C-27 (optional), C-28, C-29 (optional), C-30, C-31, C-32 (optional, likely cut), C-33 (optional)
