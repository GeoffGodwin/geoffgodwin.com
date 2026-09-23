# Batch 7 — Grounding, definitional scope, and optional slots

Verified: 2026-09-14
Slots: C-31 (required, priority), C-15 (required), C-16, C-33, C-29, C-32 (optional)

> **ENVIRONMENT LIMITATION — READ FIRST.** Same condition as batches 1–4. All
> direct page retrieval was blocked. `WebFetch` returned `EGRESS_BLOCKED` for
> every domain attempted in this session: eprints.soton.ac.uk,
> www.southampton.ac.uk, arxiv.org, www.sciencedirect.com, dl.acm.org,
> api.crossref.org, philpapers.org, aclanthology.org, www.ftc.gov, doi.org,
> www.semanticscholar.org, www.cs.ox.ac.uk, pmc.ncbi.nlm.nih.gov. `curl` through
> the proxy returned `CONNECT tunnel failed, response 403`. Reading the proxy's
> own documentation was denied by the permission classifier. No mirror,
> reader-proxy or archive workaround was attempted, per the standing rule.
>
> Only keyword search was available. Search returns links plus a **secondary
> summariser's** rendering of page content. Where a passage below is presented
> as verbatim, it is because the *same wording was returned independently across
> two or more separate searches* — which is good evidence it is genuine, but it
> is **not** the same as having read the source.
>
> Consequence, per the standing rules: **no slot in this batch is graded FIT.**
> Bibliographic identification (authors, venues, volumes, pages, DOIs, ISBNs) is
> solid and cross-checked. Quoted passages are marked with a confidence level
> and must be confirmed against the primary source before publication.
>
> The two slots recommended CUT (C-29, C-32) are graded CUT on editorial
> grounds, not on access grounds — that recommendation stands regardless of the
> proxy.

---

### C-31
- **Status:** FOUND — required, priority slot. Source positively identified, claim strongly corroborated, full text not opened from this environment, therefore not graded FIT. This is the slot most worth spending a manual verification pass on.

- **Citation:**
  - **Primary (1990):** Harnad, S. (1990). The symbol grounding problem. *Physica D: Nonlinear Phenomena*, 42(1–3), 335–346.
  - **Companion (2025) — recommended as a co-citation, see Notes:** Harnad, S. (2025). Language writ large: LLMs, ChatGPT, meaning, and understanding. *Frontiers in Artificial Intelligence*, 7, 1490698.

- **URL/DOI:**
  - 1990: `https://doi.org/10.1016/0167-2789(90)90087-6` (Elsevier PII `0167278990900876`). Author's open-access preprint of the same paper: arXiv `cs/9906002` (`https://arxiv.org/abs/cs/9906002`); institutional copy at `https://eprints.soton.ac.uk/250382/1/symgro.pdf`.
  - 2025: `https://doi.org/10.3389/frai.2024.1490698` — open access (CC-BY). Publisher page: `https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1490698/full`. PMC copy: `PMC11861094`. Preprint: arXiv `2402.02243`, titled *"Language Writ Large: LLMs, ChatGPT, Grounding, Meaning and Understanding"* (note the preprint title differs from the published title — cite the published one).
  - Accepted 20 Dec 2024; published 12 Feb 2025. The DOI year-stamp (`frai.2024`) reflects the Frontiers volume, not the publication date. Cite it as 2025 and give the volume as 7; if a house style objects to the mismatch, "Front. Artif. Intell. 7:1490698 (2025)" is unambiguous.

- **Claim needed:** Meaning requires symbols to be tied to sensorimotor contact with a world; symbols defined only in terms of other symbols never acquire intrinsic meaning.

- **Supporting passage(s):**

  **(a) Harnad's own statement of the problem** — from the abstract. Returned identically across three independent searches; high confidence, still confirm wording:

  > "How can the semantic interpretation of a formal symbol system be made intrinsic to the system, rather than just parasitic on the meanings in our heads?"
  > *(Abstract, p. 335)*

  And, immediately following:

  > "How can the meanings of the meaningless symbol tokens, manipulated solely on the basis of their (arbitrary) shapes, be grounded in anything but other meaningless symbols?"
  > *(Abstract, p. 335)*

  **(b) Harnad's own illustration of the problem** — §2.2, "The Chinese/Chinese Dictionary-Go-Round." Harnad's image is of trying to learn Chinese from a Chinese/Chinese dictionary alone: the trip through the dictionary is a merry-go-round, "passing endlessly from one meaningless symbol or symbol-string to another, never coming to a halt on what anything meant." Confidence: medium-high on the wording, high on the substance and the section location. **Confirm before quoting.** For a business audience this is the more usable of the two — it is a picture, not a thesis — and it is Harnad's own, not a paraphrase.

  **(c) What he argues is required to solve it** — abstract, and developed in §3 ("Grounding symbol systems in categorizer capacity"). Returned verbatim across two independent searches:

  > "Symbolic representations must be grounded bottom-up in nonsymbolic representations of two kinds: (1) iconic representations, which are analogs of the proximal sensory projections of distal objects and events, and (2) categorical representations, which are learned and innate feature detectors that pick out the invariant features of object and event categories from their sensory projections."
  > *(Abstract, p. 335)*

  Precisely what Harnad says is required, stated plainly:
  1. A **hybrid** nonsymbolic/symbolic system, not a purely symbolic one. Critically, "such a hybrid model would not have an autonomous symbolic 'module'" — the symbolic layer is not bolted on top; it emerges as an intrinsically *dedicated* symbol system out of the bottom-up grounding.
  2. **Iconic** representations (analog sensory projections) and **categorical** representations (invariance-extracting feature detectors) as the nonsymbolic base.
  3. **Connectionism as the mechanism**, not as a rival theory: Harnad casts neural nets as the natural candidate for learning the invariant features underlying categorical representations, "thereby connecting names to the proximal projections of the distal objects they stand for."
  4. **Robotic (sensorimotor) capacity**, not just linguistic capacity: the system must be able to discriminate, categorise, identify and act upon the things its symbols refer to. Harnad ties this to passing the **Total Turing Test** — linguistic *and* robotic indistinguishability — rather than the Turing Test alone.

  **(d) The 2025 companion, on LLMs specifically** — from the published abstract. Harnad's stated position on ChatGPT:

  > "It is not true that it understands. But it is also not true that we understand how it can do what it can do."
  > *(Abstract)*

  And, on what is missing, phrased in exactly the terms the post needs:

  > "...what it is that ChatGPT lacks, which is direct sensorimotor grounding to connect its words to their referents and its propositions to their meanings."
  > *(Abstract)*

  Confidence on (d): high on substance, medium-high on exact wording. Both sentences were returned independently across two searches. The 2025 paper is open access, so verification is cheap once egress is available.

- **Author-stated limitations:**
  - **1990 — the solution is explicitly a sketch, not a result.** The abstract itself says "a candidate solution is *sketched*." Harnad is proposing a research programme, not reporting that it has been carried out. Do not write "Harnad showed"; write "Harnad argued."
  - **1990 — the paper is about the scope and limits of *symbolic* models.** Its target is classical symbolic AI (and Searle's Chinese Room), not statistical learning systems, which did not exist at scale in 1990. Applying it to transformer models is an extension the 1990 paper does not itself make.
  - **1990 — "sensory" more than "sensorimotor."** The 1990 emphasis is on sensory projections and categorisation. The robotic/sensorimotor framing and the Total Turing Test are present but are developed much more fully in Harnad's later work. If the post's sentence is specifically "sensorimotor contact with a world," the 2025 paper supports that phrasing more directly than the 1990 paper does. **This is the main fit risk in the slot and the reason for the co-citation.**
  - **2025 — the position is argued, contested, and presented as conjecture.** Harnad explicitly offers "hunches about benign biases" — convergent constraints emerging at LLM scale — as an *explanation of why ChatGPT does better than it should*, not as a settled account. He says outright that we do not understand how it does what it does.
  - **2025 — the exposition is a dialogue with ChatGPT-4.** That is an unusual form for a peer-reviewed paper. It is genuinely peer-reviewed and in a real journal, but a skeptical reader who opens it will find Harnad in conversation with a chatbot. Worth knowing before you send a business audience to it.
  - **2025 — the field disagrees.** There is live published opposition, e.g. an EMNLP 2024 main-conference paper arguing that the symbol grounding problem does not apply to LLMs at all (`https://aclanthology.org/2024.emnlp-main.651/`), and work arguing LLMs *circumvent* rather than solve grounding. The post should not present grounding as settled consensus.

- **Recommendation:** **Use, with the 2025 paper cited alongside the 1990 paper.** Cite both, in that order, in the same note.

  This directly answers the objection you anticipated. Citing a 1990 paper at a 2026 system invites "you are quoting something written before the technology existed" — and the answer is that the author of the 1990 paper published a peer-reviewed paper in 2025 applying the same argument to ChatGPT by name, and reached the same conclusion. That is a much stronger position than a 1990 citation alone, and stronger than most people arguing this point in public have. It also pre-empts the objection without the post having to raise it.

  Suggested shape for the note: 1990 for the *problem*, 2025 for the *application*. Quote (b) or (c) from 1990 and quote (d) from 2025.

- **Notes / risks:**
  - **Verify before publication:** the exact abstract wording of both papers, the §2.2 dictionary-go-round sentence, and the page for the 1990 abstract (p. 335 is the paper's first page and is where the abstract sits, but confirm).
  - Do not cite the arXiv preprint title for the 2025 paper. The preprint is *"Language Writ Large: LLMs, ChatGPT, Grounding, Meaning and Understanding"*; the published article is *"Language writ large: LLMs, ChatGPT, meaning, and understanding."* Citing the preprint title against the journal DOI looks careless.
  - Harnad's affiliation on the 2025 paper is Department of Psychology, Université de Montréal (he is also Emeritus Professor at Southampton). Not needed in the citation, but it is the detail most often got wrong.
  - Harnad is a partisan in this debate, not a neutral referee. That is fine — the post is citing him for the statement of a problem he named — but do not present him as the field's consensus voice.
  - If the post wants a single citation rather than two, use the **2025** one. It contains the grounding argument, states it in terms of LLMs, is open access, and is recent. The 1990 paper is the more famous artefact but the weaker fit to a 2026 claim.

---

### C-15
- **Status:** FOUND — source positively identified with exact citable detail; the specific section was identified from the publisher's own table of contents rather than from the book text, so not graded FIT.

- **Citation:** Russell, S. J., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Hoboken, NJ: Pearson. ISBN-13 978-0-13-461099-3 (ISBN-10 0-13-461099-7).
  - **Cite to §1.1.1, "Acting humanly: The Turing test approach," Chapter 1 ("Introduction"), p. 2.**

- **URL/DOI:** Publisher page (stable): `https://www.pearson.com/en-us/subject-catalog/p/artificial-intelligence-a-modern-approach/P200000003500/9780134610993`
  - Authors' companion site, which carries the full table of contents: `https://aima.cs.berkeley.edu/` and `https://aima.cs.berkeley.edu/contents.html`
  - eTextbook edition ISBN-13 978-0-13-750513-5; Global Edition ISBN-13 978-1-292-40113-3. Use the US hardcover ISBN above unless the audience is non-US.

- **Claim needed:** AI is a broad discipline with many subfields, of which large language models are one product — establishing scope, not arguing a position.

- **Supporting passage:** §1.1.1 is where Russell & Norvig enumerate the capabilities a machine would need to pass the Turing test, and in doing so name the subfields of AI: **natural language processing, knowledge representation, automated reasoning, and machine learning**; then, for the *total* Turing test, **computer vision** and **robotics**. Six named subfields in roughly one page. This is exactly the "points somewhere specific rather than at a 1000-page book" you asked for.

  Confidence: high on the section number, title and page (drawn from the authors' own published table of contents, cross-checked against the 3rd-edition ToC where the same passage appears); the six-subfield list is the canonical AIMA passage carried across editions. **Confirm the list against the printed page before quoting verbatim.**

- **Author-stated limitations:**
  - §1.1.1 is framed around the *Turing test*, which Russell & Norvig are notably lukewarm about — they argue elsewhere in Ch. 1 that the test has not been a productive research target and that "acting rationally" is the better organising frame (§1.1.4). If you cite §1.1.1 for the subfield list, do not accidentally imply the authors endorse the Turing test as the goal of AI. Cite it for the taxonomy only.
  - The 4th edition's currency: it predates the current generation of large language models as products. It is the right source for *scope* — which is all this slot needs — and the wrong source for *state of the art*.
  - Edition/date pitfall: the 4th edition was published 28 April 2020 and carries a 2021 copyright on the US printing. Pick one and be consistent. **Confirm the copyright year on the title page before publication.** As of this check there is no 5th edition.

- **Recommendation:** **Use Russell & Norvig, not the AI Index.** For a business audience this is the clearly better choice, for three reasons:

  1. **It is a definition, not a measurement.** The slot's job is to establish that AI is a field and LLMs are one thing in it. A textbook does that by construction. The AI Index does it only incidentally, as a side effect of having chapters.
  2. **It does not date.** The AI Index is a snapshot; citing the 2026 edition means the citation is visibly stale in eighteen months. A business reader who notices that reads the whole post as stale.
  3. **It carries authority with a non-technical reader** in a way a think-tank report does not. "The standard graduate textbook" is a phrase that ends an argument. "A Stanford report" invites "whose report?"

  **Where the AI Index *is* better:** if the post ever needs adoption figures, investment figures, or a claim about what is actually being deployed in industry. For that, cite: *The 2026 AI Index Report*, Stanford Institute for Human-Centered AI (HAI), 2026 — `https://hai.stanford.edu/ai-index/2026-ai-index-report`. Nine chapters: Research and Development, Technical Performance, Responsible AI, Economy, Science, Medicine, Education, Policy and Governance, Public Opinion. It is free and citable. **Note: I did not verify the AI Index report's authorship line or its own preferred citation format from the primary document — confirm before citing.**

- **Notes / risks:**
  - If you want to hedge the "one product among many" framing even harder, the AI Index chapter list is itself a usable demonstration of breadth — nine domains, of which language models occupy part of one. But you do not need both sources, and two citations for a scope-setting sentence looks defensive.
  - Do not cite Wikipedia's AIMA article even though it is where the edition history is easiest to check.

---

### C-16
- **Status:** FOUND (Weizenbaum 1966) / **CUT** (the modern empirical study)

- **Citation:**
  - **Recommended:** Weizenbaum, J. (1966). ELIZA — a computer program for the study of natural language communication between man and machine. *Communications of the ACM*, 9(1), 36–45.
  - **Secondary, optional:** Weizenbaum, J. (1976). *Computer Power and Human Reason: From Judgment to Calculation.* San Francisco: W. H. Freeman. ISBN 0-7167-0463-3.

- **URL/DOI:** `https://doi.org/10.1145/365153.365168`
  - Publisher page: `https://cacm.acm.org/research/eliza-a-computer-program-for-the-study-of-natural-language-communication-between-man-and-machine-2/`
  - Widely mirrored for teaching, e.g. `https://www.csee.umbc.edu/courses/331/papers/eliza.html`

- **Claim needed:** People attribute understanding to fluent conversational systems, including when told the system does not understand.

- **Supporting passage:**

  > "Some subjects have been very hard to convince that ELIZA (with its present script) is not human."
  > *(p. 42)*

  Returned identically across two independent searches; the page is consistent across both. Confidence: high on the sentence, medium-high on the page. **Confirm p. 42 against the PDF.** Context: Weizenbaum is discussing what subjects believed about the machine as a result of conversing with it, and calls it "a striking form of Turing's test."

  The complementary passage, if a stronger one is wanted, is in the 1976 book's preface — Weizenbaum's account of being "startled" at how quickly and deeply people became emotionally involved with DOCTOR and "unequivocally" anthropomorphised it, and his remark that short exposures to a simple program "could induce powerful delusional thinking in quite normal people." **This wording is from secondary sources and is NOT verified against the book. Do not quote it without the book in hand.**

- **Author-stated limitations:**
  - The 1966 paper is an **observational report by the system's designer**, not a controlled study. Weizenbaum reports impressions of his own users. There is no sample, no measure and no control. It is evidence that the phenomenon exists and was noticed immediately; it is not evidence of prevalence or magnitude.
  - Weizenbaum's own framing in the paper is about the *illusion* of understanding as a deliberate demonstration — his point is that the effect is cheap to produce, which is the point the post wants, but it means the paper documents a demonstration rather than a finding.
  - The 1976 book is polemic, explicitly and by design. It is a fine source for Weizenbaum's own account of the ELIZA effect and a poor one to present as neutral evidence.

- **Recommendation:** **Use Weizenbaum 1966 alone.** It satisfies the "prefer a primary study over commentary" test — it *is* the primary document, by the person who built the system, and the single quoted sentence carries the whole claim. It is also rhetorically strong for a business audience: a 1966 program with a few hundred lines of pattern-matching produced the effect, which makes the point that fluency alone is sufficient to trigger attribution, independent of capability.

  **CUT the modern empirical companion.** I searched 2022–2026 work on anthropomorphism and LLM chatbots and did not find a clean fit. What exists is adjacent but off-claim:
  - Yao, X., & Xi, Y. (2025). From assistants to digital beings: exploring anthropomorphism, humanness perception, and AI anxiety in large-language-model chatbots. *Social Science Computer Review*. `https://doi.org/10.1177/08944393251354976` — survey of ~1,000 LLM chatbot users in China. Measures perceived *humanness* and AI *anxiety*, not attribution of understanding. Geographically narrow for a US/UK business audience.
  - A 2026 systematic review of anthropomorphism in *children's* interactions with LLM chatbots (ACM IDC 2026, `https://doi.org/10.1145/3773077.3806126`) — wrong population, and a review rather than a primary study.
  - A scoping review, "The impact of anthropomorphizing large language models-based chatbots" (Research Square preprint, not peer-reviewed).

  None of these measures "do users believe the system understands them." They measure anthropomorphism, trust, perceived competence and anxiety, which are neighbouring constructs. Citing one of them for the understanding claim would be stretching a source to fit — precisely what the standing rules forbid. Weizenbaum is the cleaner citation and the slot does not need two.

- **Notes / risks:**
  - A reader may object that a 1966 citation is quaint. The honest answer, which the post can make in half a sentence, is that that is the point: the effect is sixty years old and does not require the system to be good.
  - Weizenbaum's name carries baggage — he became a prominent AI critic. If the post is trying to sound non-polemical, cite the 1966 CACM paper and not the 1976 book; the paper is a technical report, the book is an argument.
  - If a modern empirical anchor really is wanted later, the honest search is for work on *overtrust* or *reliance* rather than *anthropomorphism* — and that literature is already covered by C-33, which makes C-16's modern half redundant.

---

### C-33
- **Status:** FOUND — source positively identified and the framing is supported; full text not opened, therefore not graded FIT.

- **Citation:** Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation: an attentional integration. *Human Factors: The Journal of the Human Factors and Ergonomics Society*, 52(3), 381–410.

- **URL/DOI:** `https://doi.org/10.1177/0018720810376055`
  - Publisher: `https://journals.sagepub.com/doi/10.1177/0018720810376055`
  - PubMed: PMID 21077562 (`https://pubmed.ncbi.nlm.nih.gov/21077562/`)
  - Author-institution open copy: `https://depositonce.tu-berlin.de/bitstream/11303/8923/1/Parasuraman_Manzey_2010.pdf`

- **Claim needed:** Automation bias and complacency are documented, long-studied failure modes in human use of automated systems — an institutional, decades-old, knowably governed problem.

- **Supporting passage:** From the structured abstract. Both lines returned verbatim in search; confidence medium-high, **confirm against the PDF:**

  > **Objective:** "Our aim was to review empirical studies of complacency and bias in human interaction with automated and decision support systems and provide an integrated theoretical model for their explanation."
  > *(Abstract, "Objective")*

  > **Background:** "Automation-related complacency and automation bias have typically been considered separately and independently."
  > *(Abstract, "Background")*

  And the conclusion, which is the sentence that actually carries the claim:

  > "...complacency and automation bias represent different manifestations of overlapping automation-induced phenomena, with attention playing a central role."
  > *(Abstract, "Conclusion")*

  Three findings from the paper that support the "knowably governed" half of the post's framing, and which are the substantively useful part:
  1. Automation complacency occurs under **multiple-task load** — when manual tasks compete with the automated task for the operator's attention. It is a workload phenomenon, not a character flaw.
  2. It is found in **both naive and expert participants**.
  3. It **cannot be overcome with simple practice.** Training alone does not fix it.

  Confidence: high on substance (these are the paper's headline findings and recur across every summary), medium on exact wording. **Do not publish (1)–(3) as quotes without the PDF.**

- **Author-stated limitations:**
  - It is a **review and theoretical integration**, not new empirical work. It synthesises other people's experiments. That is exactly what the post wants — it establishes that a body of work exists — but the citation should read "reviewing the empirical literature, Parasuraman and Manzey…" not "Parasuraman and Manzey found…"
  - The reviewed evidence base is overwhelmingly **laboratory studies, simulated flight decks, and process-control monitoring tasks**, circa 1990–2010. Generalisation to knowledge work with a conversational assistant is an analogy. Sound, but an analogy.
  - The systems reviewed are **deterministic, reliability-characterisable automation** — an autopilot has a knowable error rate. An LLM does not fail in the same shape. The mechanism (attention allocation under load) transfers; the risk model does not, cleanly.

- **Recommendation:** **Use with caveat** — and the caveat is small. This is a good fit for the slot as you described it. The post uses it in a list of "institutional, decades-old, knowably governed" failure modes, and a 2010 *Human Factors* review synthesising two decades of prior empirical work is close to the ideal shape of evidence for that sentence: not a hot take, not a finding, a *field*. Cite the year and the word "review" explicitly; they are doing the work.

  **On a newer source:** there is now strong 2025 work on automation bias with LLMs specifically. The best is:

  > Qazi, I. A., Khawaja, A. U., Akhtar, M. J., Sheikh, A. Z., & Alizai, M. H. (2025). Automation bias in large language model–assisted diagnostic reasoning among physicians trained in AI literacy — a randomized clinical trial. *NEJM AI*. `https://doi.org/10.1056/AIoa2501001`

  Single-blind RCT, 44 physicians who had completed a 20-hour AI literacy course; treatment arm received ChatGPT-4o suggestions with deliberately seeded errors in three of six cases. Finding: diagnostic reasoning degraded significantly versus the error-free arm, **and AI literacy training did not eliminate the bias.** Preprint: medRxiv `10.1101/2025.08.23.25334280`. **Author list and result figures are from search metadata and are NOT verified — confirm the author list in particular before citing, as I could not open the paper.**

  **I would not swap it in. I would add it only if the post has room.** Reasoning: the two sources do different jobs. Parasuraman & Manzey establishes that this is *old and studied* — which is the specific thing your sentence claims. The NEJM AI trial establishes that it is *current and unfixed by training* — which is a different and more alarming claim, and one that will pull the paragraph toward a healthcare example the post may not want. If you cite only one, cite Parasuraman & Manzey; it is the one that matches the framing. If you cite both, the pairing is genuinely strong: a 2010 review of two decades of work, plus a 2025 RCT showing the same failure mode survives contact with LLMs and with training designed to prevent it. That pairing is the single most defensible evidence chain in this batch.

- **Notes / risks:**
  - Parasuraman died in 2015; there is no risk of the author disowning the framing, but also no recent restatement from him. The 2025 RCT is the closest thing to a continuation.
  - The NEJM AI trial's population is physicians in Pakistan. Fine as evidence of the mechanism, but do not generalise its effect sizes to a bank.
  - Beware the word "complacency" in a bank. It reads as a performance judgement on staff. Parasuraman & Manzey's actual finding is the opposite — it is an attention-allocation effect under load that experts show as readily as novices. If the post uses the word, it should carry that correction, or the paragraph will land as blaming users.

---

### C-29
- **Status:** CUT (editorial recommendation; the source itself is real and correctly identified)

- **Citation:** Dehaene, S., & Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200–227.
  - Alternative, if a book-length treatment were ever wanted: Dehaene, S. (2014). *Consciousness and the Brain: Deciphering How the Brain Codes Our Thoughts.* New York: Viking. ISBN 978-0-670-02543-5.

- **URL/DOI:** `https://doi.org/10.1016/j.neuron.2011.03.018`
  - Publisher: `https://www.cell.com/neuron/fulltext/S0896-6273(11)00258-3`

- **Claim needed:** Pre-emptive only — to block the objection that brains are "parallel" and models "serial."

- **Supporting passage:** From the abstract; wording from search, **unverified:**

  > "Converging neuroimaging and neurophysiological data point to objective neural measures of conscious access: late amplification of relevant sensory activity, long-distance cortico-cortical synchronization at beta and gamma frequencies, and 'ignition' of a large-scale prefronto-parietal network."
  > *(Abstract)*

  The paper is the canonical review statement of the Global Neuronal Workspace (GNW) model. Substantively it *does* undercut the parallel/serial objection: GNW holds that massively parallel unconscious processing feeds a **capacity-limited, effectively serial global workspace**. On that account the brain is both, and the serial bottleneck is where conscious access happens. So the source technically does the job.

- **Author-stated limitations:**
  - It is a **review of one theory among several competitors** (Integrated Information Theory, higher-order theories, recurrent processing theory). Presenting GNW as "the" account of conscious processing would be a misrepresentation of the state of that field, which is genuinely unsettled.
  - It is about **conscious access to information** — reportability — not about comprehension, meaning, or machine cognition. The paper makes no claim about artificial systems.
  - The neural measures it reports are correlates of conscious access; the review is explicit that establishing a *causal* link between subjective experience and neuronal activity remains the open challenge.

- **Recommendation:** **CUT.**

  Two sentences, as requested. Including it buys a technically correct rebuttal to an objection almost nobody will actually raise, at the price of importing consciousness science into a post about machine comprehension — which hands every reader permission to ask whether the author thinks models are or are not conscious, a question the post has no interest in and cannot win. The cheaper and better defence, if the objection ever arrives, is architectural rather than neuroscientific: transformers are massively parallel internally and merely *autoregressive* at the output, so the "serial machine" premise is wrong on its own terms before any neuroscience is needed.

- **Notes / risks:**
  - Keep the citation on file. If a reviewer or commenter does raise the parallel/serial point, this is the right source to reach for — but reach for it in a reply, not in the post.
  - If it ever is used, use the 2011 *Neuron* review, not the 2014 trade book. The review is peer-reviewed, precisely scoped and citable to a DOI; the book is a popularisation and will read as the author reaching for a bestseller.

---

### C-32
- **Status:** CUT (with a usable fallback identified, if the slot is kept)

- **Citation (fallback, if the slot survives):**
  - **Preferred:** Atleson, M. (2023, February 27). *Keep your AI claims in check.* Federal Trade Commission, Division of Advertising Practices, Business Blog.
  - **Supporting:** Federal Trade Commission. (2024, September 25). *FTC announces crackdown on deceptive AI claims and schemes* ("Operation AI Comply"). Press release.
  - **Supporting, financial-sector:** U.S. Securities and Exchange Commission. (2024, March 18). *SEC charges two investment advisers with making false and misleading statements about their use of artificial intelligence* (Delphia (USA) Inc.; Global Predictions Inc.). Press Release 2024-36.

- **URL/DOI:**
  - `https://www.ftc.gov/business-guidance/blog/2023/02/keep-your-ai-claims-check`
  - `https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes`
  - `https://www.sec.gov/news/press-release/2024-36`

- **Claim needed:** Vendors market AI products with language claiming the product "understands" or "reasons."

- **Supporting passage:** The FTC 2023 blog is the closest neutral, aggregate documentation of the pattern. Its framing questions to marketers — all **unverified wording, from search:**
  - "Are you exaggerating what your AI product can do?" — and whether it can do something "beyond the current capability of any AI or automated technology."
  - Performance claims must rest on "actual scientific support," not "science fiction."
  - "Does the product actually use AI at all?"

  From the 2024 Operation AI Comply release, FTC Chair Lina M. Khan: *"there is no AI exemption from the laws on the books."* Widely reproduced; **unverified against the primary release.**

  From the SEC, Chair Gary Gensler on the first "AI washing" actions: the advisers *"marketed to their clients and prospective clients that they were using AI in certain ways when, in fact, they were not."* Two advisers, $225,000 and $175,000 civil penalties, settled without admitting or denying. **Unverified against the primary release.**

- **Author-stated limitations:**
  - **None of these documents the claim the slot actually needs.** The FTC and SEC actions are about claims that a product *uses* AI when it does not, and about *unsubstantiated performance* claims. They are not about the specific rhetorical move of saying a system "understands" or "reasons." That distinction is exactly the one the post turns on, and a careful reader will spot that the citation does not reach it.
  - The FTC blog is **staff guidance on a blog**, not a rule, a policy statement, or an enforcement action. It is neutral and quotable but it is not law, and its footer will say so.
  - The 2024 FTC actions target small-scale and outright fraudulent operations — fake-review generators, an "AI Lawyer," AI-storefront money-making schemes. Using them to characterise enterprise software marketing is a category error, and a hostile reader will say so.

- **Recommendation:** **CUT**, consistent with the fit-check.

  The pattern is real and the post can assert it as a pattern in its own voice without naming anyone — which is both safer for the author's position and more honest than attaching a regulator citation that does not actually say what the sentence says. A regulator source would have been ideal if one existed on point; the ones that exist are about *AI washing* (claiming to use AI when you don't) rather than *AI anthropomorphising* (claiming your AI understands). Those are different offences, and stapling one to the other is the stretch the standing rules prohibit.

  **If the slot is kept anyway**, cite the FTC 2023 blog and nothing else, and phrase the sentence to match what it supports — something in the shape of "regulators have warned advertisers against overstating what AI products can do" rather than "regulators have identified the 'it understands' claim as deceptive." The first is true and citable; the second is not.

- **Notes / risks:**
  - The SEC actions are the most tempting for a banking audience and the most dangerous. They name two specific firms. Citing them puts named financial-services firms into a post by a bank employee writing about AI claims in financial services. Even though neither is plausibly an employer, vendor or competitor, the optics are bad and the benefit is nil. **Do not use the SEC source.**
  - Operation AI Comply remained an active enforcement posture into 2025 under the succeeding administration, so the 2024 release has not been superseded. Not that this changes the recommendation.
  - All three URLs are US government pages and are subject to administration-change link rot. If any is used, archive it at the time of publication.

---

## Verification queue (what a second pass with working egress must do)

| Slot | Must confirm |
|---|---|
| C-31 | Harnad 1990 abstract wording (p. 335) and §2.2 dictionary-go-round sentence; Harnad 2025 abstract wording, both quoted sentences. Both are open access. **Highest priority in this batch.** |
| C-15 | The six-subfield list as printed in §1.1.1, p. 2; the title-page copyright year (2020 vs 2021). |
| C-16 | The p. 42 sentence in Weizenbaum 1966. If the 1976 book is used at all, its preface wording. |
| C-33 | Parasuraman & Manzey abstract Objective/Background/Conclusion wording; the three findings. Open copy available at depositonce.tu-berlin.de. If the NEJM AI trial is added: **its author list**, which I could not verify. |
| C-29 | Nothing — recommended CUT. |
| C-32 | Nothing — recommended CUT. If overridden, the FTC 2023 blog's framing questions. |
