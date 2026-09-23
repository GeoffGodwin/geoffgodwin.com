# Batch 3 — Safety Theory (instrumental convergence, corrigibility, reward optimization)

**Verifier:** Claude (agent run) · **Date:** 2026-09-14

> ## ⚠️ BLOCKER — READ FIRST
>
> **No primary source in this batch was read.** Outbound network egress in this
> session is restricted by organization policy to GitHub only. Every scholarly
> host needed for this batch returned a proxy `403 CONNECT tunnel failed` or an
> `EGRESS_BLOCKED` error:
>
> `arxiv.org`, `link.springer.com`, `doi.org`, `dl.acm.org`, `www.ijcai.org`,
> `nickbostrom.com`, `selfawaresystems.com`, `ebooks.iospress.nl`,
> `intelligence.org`, `www.semanticscholar.org`, `pmc.ncbi.nlm.nih.gov`,
> `gwern.net`, `jstor.org`, `openreview.net`, `proceedings.neurips.cc`,
> `people.eecs.berkeley.edu`, `cdn.openai.com`, `en.wikipedia.org`.
>
> Per the batch method's hard rule — *"if you cannot access full text say so and
> mark FOUND, not FIT"* — **every slot below is marked FOUND.** None is cleared
> for publication.
>
> **No verbatim quotes are supplied.** Bibliographic details below come from
> search-engine result text (secondary, cross-corroborated where possible) and
> are marked with a confidence level. Anything labelled `REPORTED WORDING` is a
> widely-circulated phrasing that I could **not** check against the source; it
> must not be set in quotation marks in the post until someone opens the PDF.
>
> **To clear this batch:** re-run with `arxiv.org`, `link.springer.com`,
> `doi.org`, `www.ijcai.org` and `intelligence.org` added to the egress
> allowlist. Four of the six slots (C-3, C-4, C-10, C-11) are fully
> resolvable from open-access PDFs once arXiv and IJCAI are reachable.

---

### C-2
- **Status:** FOUND
- **Citation:** Omohundro, Stephen M. (2008). "The Basic AI Drives." In Pei Wang, Ben Goertzel & Stan Franklin (eds.), *Artificial General Intelligence 2008: Proceedings of the First AGI Conference*. Frontiers in Artificial Intelligence and Applications, Vol. 171. Amsterdam: IOS Press, pp. 483–492.
- **URL/DOI:** Publisher volume: https://ebooks.iospress.nl/volume/artificial-general-intelligence-2008-proceedings-of-the-first-agi-conference · ACM DL record: https://dl.acm.org/doi/10.5555/1566174.1566226 · Author's copy (canonical, per Omohundro's own site): https://selfawaresystems.com/2007/11/30/paper-on-the-basic-ai-drives/
  - ⚠️ **No DOI confirmed.** IOS Press FAIA volumes from 2008 frequently have no per-chapter DOI. The ACM DL `10.5555/…` string is an ACM-internal identifier, **not** a registered DOI — do not print it as one.
- **Claim needed:** Self-preservation and resource acquisition arise as instrumental subgoals of nearly any final goal; the drive falls out of *goal plus competence*, not out of programming.
- **Supporting passage:** **NOT OBTAINED — full text inaccessible (see blocker).**
- **Author-stated limitations / assumptions the post must repeat:** **NOT OBTAINED.** These must be captured before publication. Specifically, verify on the PDF:
  - The paper's argument is framed around agents that are (or self-modify toward being) **rational expected-utility maximizers**. That is a strong modelling premise and the post should say so.
  - Omohundro's standard hedge is that the drives are **tendencies that appear unless explicitly counteracted**, not inevitabilities. Confirm the exact hedging language — it is what keeps the post from overclaiming.
  - The paper is a **conceptual/theoretical argument**, not an empirical study of any system.
- **Notes / risks:**
  - **Confidence on bibliography: HIGH.** Volume, editors, series number (171), publisher, conference (AGI 2008, Univ. of Memphis, 1–3 March 2008) and page range 483–492 were corroborated across multiple independent indexes.
  - **Confidence on the specific claim: MEDIUM-HIGH but UNVERIFIED.** Secondary sources consistently describe the paper as arguing for drives including self-preservation/self-protection and resource acquisition, and as deriving them from goal-seeking rather than from explicit programming. That is exactly the claim the post needs — but "consistently described as" is not verification, and this is precisely the kind of paper that gets summarised more confidently than it argues.
  - **Specific fit-check still owed.** The post needs Omohundro to argue the drives fall out of *goal + competence*. Note that his actual chain of reasoning runs through **self-improvement and rationality** (systems become utility maximizers, and utility maximizers then exhibit the drives). If the derivation depends on a self-improvement step, "goal plus competence" is a slight compression and the post should either match the paper's chain or soften to "goal plus capability and the pressure to pursue it coherently."
  - **Alternative if C-2 cannot be verified:** Bostrom 2012 (C-3) argues the same instrumental-convergence point and is open-access and easier to verify. Omohundro is the priority-of-origin citation; Bostrom is the citable-and-checkable one. Citing both, with Omohundro credited for priority, is the low-risk move.

---

### C-3
- **Status:** FOUND
- **Citation:** Bostrom, Nick (2012). "The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents." *Minds and Machines* 22(2): 71–85.
- **URL/DOI:** **DOI: 10.1007/s11023-012-9281-3** → https://doi.org/10.1007/s11023-012-9281-3 · Author's PDF: https://nickbostrom.com/superintelligentwill.pdf
  - Book alternative: Bostrom, Nick (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford: Oxford University Press. (Instrumental convergence is Ch. 7, "The superintelligent will"; orthogonality is in the same chapter.) ⚠️ Chapter number and page range **unverified** — confirm before printing a page cite.
- **Claim needed:** The instrumental convergence thesis, and the orthogonality of goals and intelligence.
- **Supporting passage:** **NOT OBTAINED — full text inaccessible (see blocker).**
  - `REPORTED WORDING — DO NOT QUOTE UNTIL CHECKED.` Search results paraphrase the two theses as: the orthogonality thesis holds "(with some caveats)" that intelligence and final goals are orthogonal axes along which possible artificial intellects can freely vary; and the instrumental convergence thesis holds that agents with a wide range of final goals will pursue similar intermediary goals because they have instrumental reasons to do so, provided they possess a sufficient level of intelligence. **This is abstract-level paraphrase, not Bostrom's formal indented statement of either thesis.** The post asked for the formal statement verbatim; it is not obtained. Both theses are set out as displayed, formally-worded propositions in the paper — fetch the PDF and copy them exactly.
- **Author-stated limitations / assumptions the post must repeat:**
  - Bostrom **explicitly qualifies orthogonality** ("with some caveats" appears even in the abstract). The post must not present orthogonality as unqualified. Retrieve and reproduce the caveats.
  - The instrumental convergence thesis is conditioned on a **sufficient level of intelligence** — it is not a claim about current systems.
  - Convergence is stated as agents having **instrumental reason** to pursue certain subgoals — a claim about rational pressure, not a prediction that any particular built system will behave that way. Bostrom's own framing is that the theses "point to some potential dangers," which is deliberately weaker than "show that."
  - Both theses are **philosophical arguments**, not empirical results.
- **Notes / risks:**
  - **Confidence on bibliography: HIGH.** Journal, volume 22, issue 2, pages 71–85, year 2012 and the DOI were corroborated across Springer, PhilPapers, FHI's own publication listing and ACM's record.
  - **RECOMMENDATION for a general business audience: cite the 2012 paper, not the book.** Reasons: (1) it is short, single-topic and free to read at the author's URL, so a sceptical reader can check it in ten minutes rather than buying a book; (2) it is peer-reviewed with a stable DOI, which is the stronger provenance signal in a business context; (3) the book's treatment is embedded in a long speculative argument about takeoff scenarios, and citing it invites the reader to attribute that whole framework to your post. The paper lets you cite the narrow thesis you actually need. Use *Superintelligence* only as an optional "for the longer treatment, see" pointer.
  - **Risk:** Bostrom is a polarising citation for some business readers and has attracted separate controversy unrelated to this work. That is an editorial judgement, not a citation defect, but it is worth a conscious decision. If you want a non-Bostrom framing of the same idea, Omohundro (C-2) carries priority and Russell's *Human Compatible* (2019) is the mainstream-respectable restatement.

---

### C-4
- **Status:** FOUND
- **Citation (recommended candidate):** Ouyang, Long; Wu, Jeffrey; Jiang, Xu; Almeida, Diogo; Wainwright, Carroll L.; Mishkin, Pamela; Zhang, Chong; Agarwal, Sandhini; Slama, Katarina; Ray, Alex; et al. (2022). "Training Language Models to Follow Instructions with Human Feedback." *Advances in Neural Information Processing Systems* 35 (NeurIPS 2022).
  - ⚠️ **Author list is long (20 authors) and only partially corroborated here. Use `et al.` after the first three, or verify the full list on the PDF. Do not print a full author list from this file.**
- **Citation (alternative candidate):** Christiano, Paul F.; Leike, Jan; Brown, Tom B.; Martic, Miljan; Legg, Shane; Amodei, Dario (2017). "Deep Reinforcement Learning from Human Preferences." *Advances in Neural Information Processing Systems* 30 (NIPS 2017), pp. 4299–4307. ⚠️ Page range unverified.
- **URL/DOI:** Ouyang et al.: https://arxiv.org/abs/2203.02155 · Christiano et al.: https://arxiv.org/abs/1706.03741
  - Neither NeurIPS proceedings paper carries a publisher DOI; the arXiv `/abs/` links are the correct stable URLs.
- **Claim needed:** RL fine-tuning selects behaviors that score well under a reward signal.
- **Supporting passage:** **NOT OBTAINED — full text inaccessible (see blocker).**
- **Author-stated limitations / assumptions the post must repeat:** Partially obtained, all UNVERIFIED:
  - Ouyang et al. state that InstructGPT "still makes simple mistakes" and that the models are **not fully aligned or fully safe**. The paper has an explicit, unusually candid limitations section covering labeler demographics and the fact that the models are aligned to a *specific* small group of labelers' and researchers' preferences — **not to humanity, not to the user, and not to truth.** The post must not let "trained on human feedback" slide into "trained to be good."
  - Christiano et al.'s result is about **communicating goals** via preference comparisons in Atari and simulated robotics; it is a sample-efficiency result, not a claim about language models or about deployed systems.
- **Notes / risks — RECOMMENDATION AND FIT-CHECK:**
  - **RECOMMEND Ouyang et al. 2022 (InstructGPT)** over Christiano et al. 2017, for three reasons. (1) **Relevance:** the post is about language models, and InstructGPT is the paper that actually describes RLHF applied to an LLM — Christiano et al. is Atari agents and simulated robots, and a business reader who clicks through will find it doesn't look like the thing being discussed. (2) **Plainness:** InstructGPT describes the procedure in the abstract in plainly behavioural terms — collect human rankings *of model outputs*, then fine-tune against a reward model of those rankings. The unit being scored is an **output**, which is exactly the "selects behaviors" framing the post needs. (3) **Recognisability:** it is the paper behind ChatGPT's training method, which a business audience can place.
  - Christiano et al. remains the right citation if the post needs the **origin** of preference-based RL rather than its application to LLMs. If both are cited, credit Christiano et al. with the method and Ouyang et al. with the LLM application.
  - **⚠️ CRITICAL FIT-CHECK — NOT DISCHARGED, and it is the one that matters most in this batch.** The instruction was to flag wording in the paper that would make an "evolution" analogy look like a claim about the paper rather than the author's own framing. I could not read either paper, so **I cannot certify that the post's evolution analogy is safely separated from the cited source.** What I can say from structure alone:
    - Neither paper claims to select *minds*, *values*, or *goals*. Both describe optimizing a policy against a learned reward model. The post's claim must stay at that level: **training selects outputs that score well under a reward model built from human comparisons.**
    - The words to watch in the post are "evolution," "selection pressure," "survives," "breeding," and "what the model wants." All of these are the author's framing and **none of them will be found in either paper.** Any sentence combining one of those words with a citation to Ouyang or Christiano will read as attributing the analogy to the paper. Fix by placing the citation on the mechanical claim and starting a new, uncited sentence for the analogy — e.g. cite the paper for "fine-tuning optimizes the model's outputs against a reward model trained on human rankings," then say "It is worth thinking of this as a kind of selection pressure" without a footnote.
    - There is a second, subtler trap: RLHF papers do describe optimizing a **policy**, and "policy" is easy to over-read as "disposition" or "character." It is a mapping from inputs to output distributions. The post should not let "policy" do work that "behavior" can't.
    - **This fit-check must be redone against the PDF before publication.** It is the single highest-risk item in the batch.

---

### C-10
- **Status:** FOUND
- **Citation:** Soares, Nate; Fallenstein, Benja; Yudkowsky, Eliezer; & Armstrong, Stuart (2015). "Corrigibility." In *Artificial Intelligence and Ethics: Papers from the 2015 AAAI Workshop* (Workshops at the Twenty-Ninth AAAI Conference on Artificial Intelligence), Austin, TX, 25–26 January 2015. AAAI Technical Report WS-15-02.
  - ⚠️ **Author order is contested across indexes.** FHI's own listing gives **Soares, Fallenstein, Armstrong, Yudkowsky**; the slot brief gives Soares, Fallenstein, Yudkowsky, Armstrong. Verify the order on the paper's title page before printing. ⚠️ Technical report number `WS-15-02` and page numbers **unverified**.
- **URL/DOI:** https://intelligence.org/files/Corrigibility.pdf · AAAI workshop listing: https://aaai.org/proceeding/ws-15-02/ (unverified) — no DOI; AAAI workshop papers of this vintage generally have none.
- **Claim needed:** Systems pursuing a goal have reason to resist interruption before completion; corrigibility is therefore a design problem rather than a default property.
- **Supporting passage:** **NOT OBTAINED — full text inaccessible (see blocker).**
  - `REPORTED WORDING — DO NOT QUOTE UNTIL CHECKED.` Secondary sources render the paper's definition roughly as: a system is "corrigible" if it cooperates with what its creators regard as a corrective intervention, despite default incentives for rational agents to resist attempts to shut them down or modify their preferences. **This tracks the needed claim closely but is not verified verbatim.**
- **Author-stated limitations / assumptions the post must repeat:**
  - **The paper's own framing is that it does NOT solve the problem.** It presents corrigibility as an **open problem**, introduces "some simple models" (including a version of Armstrong's utility indifference), and — per every secondary account — reports that the proposals analysed **fail** or are unsatisfactory. This is the most important thing for the post to carry: the paper is a statement of an unsolved design problem, not a demonstration of a fix. **Verify the exact self-assessment language on the PDF; it is the passage the post most needs.**
  - The "default incentive to resist" holds for **rational agents with stable goals** — a modelling assumption, not an observation about any built system.
  - The desiderata are specific and worth naming: an agent that shuts down safely when the button is pressed, has **no incentive to prevent** the button being pressed, **no incentive to cause** it to be pressed, and **propagates** the shutdown behaviour to subsystems and successors it creates. That fourth condition is the one popular summaries drop.
- **Notes / risks:**
  - **Confidence on bibliography: MEDIUM.** Venue, year and workshop are corroborated; author order, technical report number and pagination are not.
  - **On preferring Orseau & Armstrong, "Safely Interruptible Agents" (UAI 2016)** — full cite: Orseau, Laurent & Armstrong, Stuart (2016). "Safely Interruptible Agents." *Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence (UAI 2016)*, pp. 557–566. https://intelligence.org/files/Interruptibility.pdf (⚠️ pages unverified). **RECOMMENDATION: cite Soares et al. as the primary, and do NOT swap in Orseau & Armstrong.** Reason: they make *different* claims, and Orseau & Armstrong is the weaker fit for this slot. Their result is that certain RL agents (Q-learning) are already safely interruptible or (Sarsa) can easily be made so — a **positive** result about specific off-policy learners under a formal definition of interruptibility. The post's claim is that corrigibility is *not* a default property and is a design problem. Citing a paper whose headline is "these agents are already safely interruptible" to support "this doesn't come for free" invites an easy rebuttal. Orseau & Armstrong is the right citation only if the post separately wants to say that *some* narrow formal progress exists — in which case cite it as a qualifier, in the author's own voice, not as support for the design-problem claim.
  - Secondary risk: Soares et al. is a **workshop paper** by an advocacy-adjacent institute, which a hostile business reader may discount. Mitigate by pairing it with Hadfield-Menell et al. (C-11), which is a mainstream IJCAI paper making a compatible point. Do not replace it — Soares et al. is where the framing originates.

---

### C-11
- **Status:** FOUND
- **Citation:** Hadfield-Menell, Dylan; Dragan, Anca; Abbeel, Pieter; & Russell, Stuart (2017). "The Off-Switch Game." In *Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI-17)*, pp. 220–227.
- **URL/DOI:** **DOI: 10.24963/ijcai.2017/32** → https://doi.org/10.24963/ijcai.2017/32 · Proceedings PDF: https://www.ijcai.org/proceedings/2017/0032.pdf · Preprint: https://arxiv.org/abs/1611.08219
- **Claim needed:** A system's willingness to accept shutdown depends on its uncertainty about the operator's true objective.
- **Supporting passage:** **NOT OBTAINED — full text inaccessible (see blocker).**
  - `REPORTED WORDING — DO NOT QUOTE UNTIL CHECKED.` Secondary sources describe the stated goal of the work as studying **the incentives an agent has to allow itself to be switched off**, and the result as: an agent that takes its reward function for granted has an incentive to disable the off switch, whereas an agent **uncertain about human preferences** can be incentivized to defer to the human. **The claim the post needs appears to be the paper's actual central result** — but this is unverified.
- **Author-stated limitations / assumptions the post must repeat:** This slot's warning is correct and is the main risk here. The result is a **formal/game-theoretic** one and depends on modelling assumptions that the post must not drop:
  - It is a **two-player game-theoretic model** (a "cooperative inverse reinforcement learning"-style setup), analysed mathematically. **It is not an empirical finding about any deployed system, and the post must say so explicitly.** Do not write "AI systems accept shutdown when uncertain" — write "in a formal model of the interaction, an agent that is uncertain about the human's objective has an incentive to defer."
  - The result depends on the agent's uncertainty being over the **human's objective**, and on the human's behaviour being informative about that objective — i.e. the agent must treat the human's shutdown attempt as **evidence**.
  - **Human rationality is a load-bearing and explicitly varied assumption.** Secondary accounts indicate the paper analyses what happens as the human departs from perfect rationality, and that the deference incentive **degrades** with irrational humans — with the disable-the-switch incentive holding except in the perfectly-rational-human case. **Get this exactly right from the paper.** It is the qualification most often lost in popular retellings, and stating the result without it overstates it in a way a technical reader will catch.
  - More uncertainty is not simply better: the paper's framing is about a trade-off between deference and usefulness. Confirm on the PDF.
- **Notes / risks:**
  - **Confidence on bibliography: HIGH.** Authors, venue, year, page range 220–227 and the IJCAI DOI were corroborated across the IJCAI proceedings index, the ACM DL record and the arXiv listing. This is the cleanest citation in the batch.
  - **Risk:** this is the slot where an over-strong paraphrase is most tempting, because the result sounds like good news. Note that subsequent work has pushed back — e.g. Sven Neth, "Off-Switching Not Guaranteed" (philsci-archive.pitt.edu/24740/) argues the result does not hold as generally as often assumed. The post does not need to engage with that, but should not present the off-switch result as settled.

---

### C-13
- **Status:** FOUND — **with a substantive attribution finding, see notes**
- **Citation (Goodhart, the law itself):** Goodhart, Charles A. E. (1975). "Problems of Monetary Management: The U.K. Experience." In *Papers in Monetary Economics*, Vol. I. Sydney: Reserve Bank of Australia.
  - Reprinted as: Goodhart, C. A. E. (1984). *Monetary Theory and Practice: The UK Experience*. London: Macmillan. ⚠️ Chapter/page of the reprint **unverified**.
- **Citation (the popular phrasing — a DIFFERENT author):** Strathern, Marilyn (1997). "'Improving Ratings': Audit in the British University System." *European Review* 5(3): 305–321.
- **Citation (the AI-relevant formal treatment):** Manheim, David & Garrabrant, Scott (2018). "Categorizing Variants of Goodhart's Law." arXiv:1803.04585.
- **URL/DOI:** Goodhart 1975: no DOI; original is a Reserve Bank of Australia conference volume — cite the volume, or cite the 1984 Macmillan reprint, which is far easier for a reader to obtain. · Strathern 1997: *European Review* 5(3), 305–321, DOI likely `10.1002/(SICI)1234-981X(199707)5:3<305::AID-EURO184>3.0.CO;2-4` — ⚠️ **this DOI form is NOT verified; do not print it without checking.** · Manheim & Garrabrant: https://arxiv.org/abs/1803.04585
- **Claim needed:** A citeable formulation of Goodhart's law — optimizing a proxy degrades the proxy's value as a measure.
- **Supporting passage:** **NOT OBTAINED — full text inaccessible (see blocker).**
- **Author-stated limitations / assumptions the post must repeat:**
  - Goodhart's original claim is about **statistical regularities under policy control in monetary economics.** Its extension to machine learning is an **analogy made by later authors**, not something Goodhart argued. If the post applies it to AI training, that move belongs to the post (or to Manheim & Garrabrant), not to Goodhart.
  - Manheim & Garrabrant's own contribution is that "Goodhart's law" is **not one failure mode but several** (they identify four distinct mechanisms — regressional, extremal, causal, adversarial). ⚠️ The four names are from memory and secondary summary and are **unverified**. Their point is that the single-sentence popular version is too coarse to reason with. A post that invokes "Goodhart's law" as one thing is using the folk version.
- **Notes / risks — ⚠️ THE ATTRIBUTION FINDING (called out as requested):**
  - **The famous sentence is not Goodhart's.** "When a measure becomes a target, it ceases to be a good measure" was written by the anthropologist **Marilyn Strathern in 1997**, in *European Review*, in a paper about audit culture in British universities — not by Charles Goodhart, and not in 1975. Strathern was glossing Goodhart, and the gloss became more famous than the original. **Attributing that sentence to Goodhart is the single most common error in this citation, and the post must not make it.**
  - **What Goodhart actually wrote** is reported as: *"Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes."* `REPORTED WORDING — UNVERIFIED.` This is a narrower, more technical claim about econometric relationships breaking down when a central bank targets them. It is **not** a general claim about metrics and incentives.
  - **Which 1975 paper — this is the miscitation trap.** Goodhart published **two** papers in the same 1975 Reserve Bank of Australia volume (*Papers in Monetary Economics*, Vol. I), and sources disagree about which contains the law:
    - "Problems of Monetary Management: The U.K. Experience" — **this is the one that contains the first articulation**, per the better sources, and is what Wikipedia and most careful citations use.
    - "Monetary Relationships: A View from Threadneedle Street" — frequently cited instead, apparently in error.
    - ⚠️ **I could not open either paper or the standard scholarly treatment of the question (Chrystal & Mizen 2003, "Goodhart's Law: Its Origins, Meaning and Implications for Monetary Policy"), so I cannot settle this definitively.** My finding is that "Problems of Monetary Management" is the better-supported attribution, at **MEDIUM** confidence. If the post cites a specific 1975 paper title, this must be resolved first — and the honest fallback, if it cannot be, is to cite the **1984 Macmillan reprint** (*Monetary Theory and Practice: The UK Experience*), which sidesteps the question and is easier for a reader to obtain anyway.
  - **RECOMMENDATION for a business audience — cite it as a pair, and be explicit about who said what.** The cleanest and most defensible construction:
    > Charles Goodhart observed in 1975 that a statistical regularity tends to collapse once it is used as a target for control (Goodhart 1975/1984). The phrasing most people know — "when a measure becomes a target, it ceases to be a good measure" — is Marilyn Strathern's 1997 gloss, not Goodhart's own (Strathern 1997).
    This costs one extra clause and buys real credibility: the correction is itself interesting to a business reader, most of whom have seen the sentence misattributed. It also inoculates against the pedantic correction in the comments.
  - **On Manheim & Garrabrant as the primary instead: do not.** For a general business audience it is the wrong register — it is a formal taxonomy paper aimed at alignment researchers, and it is a **preprint with no peer-reviewed venue**, which is a weaker provenance signal in a business context than a named economist and a named anthropologist. Cite it only as an optional pointer if the post needs the claim that Goodhart failures come in distinct mechanical varieties, which is a genuinely useful point but probably below the post's altitude.
  - **Campbell's law** (Donald T. Campbell, 1979) is a near-identical and independently-developed claim from social science, and is sometimes the better citation for a policy-flavoured audience. Not pursued here.

---

## Summary table

| Slot | Source | Status | Blocking issue |
|---|---|---|---|
| C-2 | Omohundro 2008 | FOUND | No full text; no DOI; drive-derivation chain unverified |
| C-3 | Bostrom 2012 | FOUND | DOI confirmed; formal thesis statements not obtained |
| C-4 | Ouyang et al. 2022 (rec.) | FOUND | **Evolution-analogy fit-check not discharged** |
| C-10 | Soares et al. 2015 | FOUND | No full text; author order contested |
| C-11 | Hadfield-Menell et al. 2017 | FOUND | Bibliography clean; assumptions unverified |
| C-13 | Goodhart 1975 + Strathern 1997 | FOUND | Which 1975 paper unresolved; **attribution finding below** |

**Nothing in this batch is cleared for publication.** Re-run with scholarly egress enabled.
