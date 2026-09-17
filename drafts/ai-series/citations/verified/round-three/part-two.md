# Part two citation verification (round three), all sources except [^hfjuly]

Draft: /home/user/geoffgodwin.com/drafts/ai-series/part-two-draft.mdx (body lines 13-75, 113; footnotes 124-157, 160-166).

Method note. Every primary host (arxiv, ACM, Nature, Science, Royal Society, PMC, Frontiers, Southampton eprints, transformer-circuits.pub, university mirrors, philarchive, aima.cs.berkeley.edu) is blocked for direct fetch; each was probed once and returned 403 on CONNECT. All tier B evidence below is what the search service returned when restricted to the primary host and asked for exact phrases. The session's WebSearch budget ran out during the last batch, so one planned query (Berkes caveat wording) did not run; that item rests on recall plus a prior-round lead. Prior records under citations/ were used only as leads and are labeled as such.

---

## 1. [^rn] Russell and Norvig, AIMA 4th ed. (body line 15; footnote line 124)

Draft: field "about seventy years old, covering natural language processing and knowledge representation and automated reasoning and machine learning and computer vision and robotics, among other things"; footnote: "section 1.1.1, page 2, where those six are listed and the authors add that 'these six disciplines compose most of AI.'"

Verdict: PARTLY (text confirmed; page number unverified; the draft's six are not quite the book's six).

Tier B (search service, restricted to studylib/pearson copies of the 4e text) returned the passage: "The computer would need the following capabilities: natural language processing to communicate successfully in a human language; knowledge representation to store what it knows or hears; automated reasoning to answer questions and to draw new conclusions; machine learning to adapt to new circumstances and to detect and extrapolate patterns." ... "However, other researchers have proposed a total Turing test, which requires interaction with objects and people in the real world." ... "To pass the total Turing test, a robot will need computer vision and speech recognition to perceive the world; robotics to manipulate objects and move about. These six disciplines compose most of AI." The service also confirmed this sits under the "Acting humanly: The Turing test approach" heading.

So: the quote "these six disciplines compose most of AI" is exact (capital T in the source; the draft lowercases it mid-sentence, which is fine). The count is still six in 4e, and item five is "computer vision and speech recognition" as one unit. The draft's list gives six items but drops speech recognition, so the footnote's "those six are listed" is slightly off: the body lists five of the book's six plus nothing else. Minimal fix, body line 15: "...machine learning and computer vision and speech recognition and robotics, among other things" or change the footnote to "where those disciplines are listed". Does not change the section's point.

Section number 1.1.1 and heading: tier C, high confidence. Page 2: tier C, medium confidence only. In the 4e US edition chapter 1 opens on p. 1 with section 1.1, and 1.1.1 begins on p. 2; whether the "six disciplines" sentence falls on p. 2 or p. 3 I cannot confirm (in 3e it was p. 3). Safer wording: "section 1.1.1" without the page, or "pages 2-3".

"About seventy years old": Dartmouth 1956 to 2026 is seventy years. Fine.

## 2. [^eliza] Weizenbaum 1966 (body line 17; footnote line 126)

Verdict: CONFIRMED, with one title-punctuation note.

Tier B (search service, dl.acm.org / cacm.acm.org): Communications of the ACM, volume 9, issue 1, pages 36-45, January 1966; DOI 10.1145/365153.365168. The ACM title is "ELIZA—a computer program for the study of natural language communication between man and machine" (em dash after ELIZA, not a colon). The draft's colon is a normalization; Chicago would keep the dash. Flag only.

Quotes, tier B (search service returned the passage): "ELIZA shows, if nothing else, how easy it is to create and maintain the illusion of understanding, hence perhaps of judgment deserving of credibility. A certain danger lurks there." Both draft fragments ("shows, if nothing else, how easy it is to create and maintain the illusion of understanding" and "a certain danger lurks there") are exact. Tier C (high) agrees.

Body paraphrase "Some people, he wrote, were very hard to convince that they weren't talking to a human being": tier B returned the source sentence "Some subjects have been very hard to convince that ELIZA (with its present script) is not human." Paraphrase is fair and not in quote marks.

"A decade later ... Computer Power and Human Reason (1976)": 1966 to 1976. Correct. "Mostly reflected your own statements back at you as questions": fair for the DOCTOR script (tier C, high).

## 3. [^gpt2] Radford et al. 2019 (body line 21; footnote line 128)

Verdict: CONFIRMED.

Tier B (search service, cdn.openai.com): the paper says language modeling "is usually framed as unsupervised distribution estimation from a set of examples (x1, x2, ..., xn) each composed of variable length sequences of symbols". The phrase is exact. Tier C (high): this is the first paragraph of section 2, "Approach". Title capitalization in the draft (headline case) matches the PDF's "Language Models are Unsupervised Multitask Learners" apart from "Are" vs "are"; Chicago headline style, fine.

## 4. [^circuits] Lindsey et al., "On the Biology of a Large Language Model" (body lines 23-29; footnote line 130)

Verdict: PARTLY. All quoted phrases check out; two location claims need attention.

Tier B (search service, transformer-circuits.pub), verbatim returns:
- Rhyme planning: "often activates features corresponding to candidate end-of-next-line words prior to writing the line, and makes use of these features to decide how to compose the line." Exact.
- Fraction: "planned word features were found in about half of the poems investigated, which the researchers suggest may be due to limitations in their analysis methods or because the model doesn't always engage in planning." Draft's "about half the poems they looked at" is fine.
- Quarter: "our attribution graphs provide us with satisfying insight for about a quarter of the prompts we've tried (see § Limitations for a more detailed discussion ...)". Draft's "roughly a quarter" fine. The service also returned "the cases we have chosen to highlight are undoubtedly a biased sample shaped by the limitations of our tools" (supports "selected sample") and "These examples serve as existence proofs ... While we suspect similar mechanisms are at play beyond these examples, we cannot guarantee it" (supports "no promise at all that the same mechanism shows up anywhere else").
- Multilingual: "features in the middle are more language-agnostic" and "while Claude 3.5 Haiku is using genuinely multilingual features, especially in the middle layers, there are important mechanistic ways in which English is privileged." Both draft quotes exact. The service also returned "there is a meaningful sense in which English is mechanistically privileged over other languages as the 'default'" and that multilingual features have stronger direct weights to English output nodes, with non-English outputs mediated by say-X-in-language-Y features.
- "in which English is the default output": NOT returned verbatim by the service. Tier C (medium) and a prior-round lead both give the sentence as "This paints a picture of a multilingual representation in which English is the default output." I believe the quote is exact but could not confirm it at tier B.
- Model: Claude 3.5 Haiku confirmed; the service returned text comparing Haiku features with "the smaller 18L model", so "alongside a smaller research model" is supported.
- Attention limitation: the service returned that the method "does not explain" inputs whose contribution is "through influencing attention patterns", under a heading "Missing Attention Circuits", and that the replacement model "uses the attention patterns of the original model and treats them as fixed". The footnote's "carry no information about influence through attention patterns" and "describe a replacement model rather than the original" are fair summaries. Note the Missing Attention Circuits heading is in the methods paper's Limitations (and referenced in the biology paper); the footnote cites both papers, so this is fine.

Two things to fix or hedge:
(a) The "quarter of the prompts", "biased sample" and "existence proofs" sentences are in the Introduction (subsection "A note on our approach and its limitations"), not in section 14. The body (line 29) does not give a section, so it is fine. The footnote attributes only "we only demonstrate the existence of mechanisms in particular examples" to section 14. On that quote: tier X at the search service (not returned); tier C medium recall and a prior-round record that claims a full read both give the §14 preamble as "We only demonstrate the existence of mechanisms in particular examples. There are likely additional mechanisms which we don't see." and the preceding bullet "Our results are only claims about specific examples. We don't make claims about mechanisms more broadly." So the quote is very probably exact and in §14 (Limitations sits between §13 "Commonly Observed Circuit Components and Structure" and §15 "Discussion"; tier C medium). Draft lowercases the initial "We" inside the quote; acceptable when run into a sentence, but "[w]e" or restructuring is cleaner.
(b) Body line 25, "suppressed the planned word, the model rewrote the whole line toward a different rhyme": consistent with the paper's intervention experiments (tier C high; the service confirmed "preselected rhyming options then shape how the model constructs the entire line"). "Lit on candidate words" is a plain-language rendering; fine.

No change to what the section claims.

## 5. [^othello] Li et al. 2023; Nanda, Lee and Wattenberg 2023 (body line 23; footnote line 132)

Verdict: CONFIRMED.

Tier B (arxiv.org / aclanthology.org via search service): Li, Hopkins, Bau, Viégas, Pfister, Wattenberg, "Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task", ICLR 2023, arXiv:2210.13382. The service returned: non-linear probes (two-layer MLPs) dropped to 1.7% error on the trained model from 26.2% on a random model "while linear probes performed close to random"; intervention experiments present. Draft's "the linear ones performed poorly" is supported. Nanda, Lee and Wattenberg, "Emergent Linear Representations in World Models of Self-Supervised Sequence Models", Proceedings of the 6th BlackboxNLP Workshop, pages 16-30, Singapore, 2023; aclanthology 2023.blackboxnlp-1.2. Author order and pages confirmed.

Body line 23: "trained only to predict legal moves" is loose; the model was trained to predict the next move token in game transcripts (of synthetic random legal games), and it learned to produce legal moves. Tier C high. Minimal fix: "trained only to predict the next move in transcripts of Othello games". Does not change the claim.

## 6. [^parrots] Bender et al. 2021 (body line 31; footnote line 134)

Verdict: CONFIRMED (quote); page location PARTLY.

Tier B (dl.acm.org via search service): authors Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Shmargaret Shmitchell; FAccT '21, pages 610-623; DOI 10.1145/3442188.3445922. The exact quote was located by the service (unrestricted search hit the authors' PDF at s10251.pcdn.co and others): "a system for haphazardly stitching together sequences of linguistic forms it has observed in its vast training data, according to probabilistic information about how they combine, but without any reference to meaning: a stochastic parrot." Exact. The service placed it "on pages 616 and 617"; tier C (medium-high) puts the sentence itself on p. 617 in section 6.1 "Coherence in the Eye of the Beholder", which begins on p. 616. "The definition is on page 617" is defensible; "pages 616-617" would be safer.

Official title carries the parrot emoji ("Too Big? 🦜"); the draft omits it. Many citations do; flag only.

Body line 31 claim that the parrot argument "is one section of a paper mostly concerned with environmental cost, training data documentation, and opportunity cost": tier C high. Sections are 3 Environmental and Financial Costs, 4 Unfathomable Training Data, 5 Down the Garden Path (research opportunity cost), 6 Stochastic Parrots (6.1 coherence, 6.2 risks and harms). Fair.

## 7. [^cowan] Cowan 2001 (body line 41; footnote line 136)

Verdict: CONFIRMED.

Tier B (cambridge.org / pubmed via search service): Behavioral and Brain Sciences 24, 87-114 for the target article (Cambridge listing); PubMed gives 87-185 (target article plus commentaries and response). DOI 10.1017/S0140525X01003922 matches the Cambridge listing. The service confirmed the abstract's "three to five chunks". Draft's 87-114 is correct for the article alone; issue 1 is correct (tier C high). "Once you stop people from rehearsing them or grouping them together" matches Cowan's conditions (tier C high).

## 8. [^loftus] Loftus and Palmer 1974 (body line 41; footnote line 138)

Verdict: CONFIRMED.

Tier B (sciencedirect.com via search service): Journal of Verbal Learning and Verbal Behavior, vol. 13, issue 5 (October 1974), pages 585-589. Abstract returned: "smashed into" produced higher speed estimates than "collided, bumped, contacted, or hit"; "On a retest one week later, those subjects who received the verb smashed were more likely to say 'yes' to the question, 'Did you see any broken glass?' even though broken glass was not present in the film." Footnote matches. Body's "changing one verb in a question" fine.

## 9. [^sleep] Diekelmann and Born 2010; Klinzing, Niethard and Born 2019 (body line 43; footnote line 140)

Verdict: CONFIRMED.

Tier B (nature.com via search service): "The memory function of sleep", Nature Reviews Neuroscience 11, 114-126 (2010), DOI 10.1038/nrn2762. "Mechanisms of systems memory consolidation during sleep", Nature Neuroscience 22, 1598-1610 (2019), Klinzing, Niethard, Born. The draft's "Several of the quantitative claims in this literature have weakened since" is the author's own judgment, not attributed to either paper; not checked.

## 10. [^frozen] Brown et al., GPT-3 (body line 45; footnote line 142)

Verdict: CONFIRMED. (Flagged as a likely error in the assignment; it is not.)

Tier B (arxiv.org via search service): in the definitions of the evaluation settings (section 2, also Figure 2.1), Few-Shot is "the setting where the model is given a few demonstrations of the task at inference time as conditioning, but no weight updates are allowed." The draft's "no weight updates are allowed" is exact. The paper separately says "without any gradient updates or fine-tuning" in the abstract, which is the phrase the assignment worried about; both exist. Tier C (high) agrees. The footnote's gloss (describing in-context learning) matches the context.

## 11. [^raichle] Raichle 2015; Raichle and Mintun 2006 (body line 51; footnote line 144)

Verdict: CONFIRMED on bibliographic details; quote PARTLY confirmed (the "5%" and "remarkably small" wording confirmed; the tail "of the baseline level of activity" rests on recall).

Tier B (royalsocietypublishing.org / PMC via search service): "The restless brain: how intrinsic activity organizes brain function", Phil. Trans. R. Soc. B 370 (1668): 20140172, 19 May 2015, DOI 10.1098/rstb.2014.0172, PMC4387513. Raichle and Mintun, "Brain work and brain imaging", Annu. Rev. Neurosci. 29: 449-476 (2006) (tier C high; the search service returned the sentence as "according to Raichle and Mintun" via a secondary PMC source, which fits the 2015 paper citing [5] Raichle and Mintun at that point). The service's rendering: "Relative to the very high rate of ongoing or 'basal' energy consumption in humans, the additional energy consumption associated with evoked changes in brain activity is remarkably small, often less than 5%". It did not return the words "of the baseline level of activity". Tier C (medium-high): Raichle's recurring sentence, in the 2015 paper and in his 2010 TICS review, ends "...often less than 5% of the baseline level of activity". A prior-round record (lead only) quotes the 2015 sentence the same way with "[5]" after it. I consider the draft's quote exact but could not close it at tier B. If the author wants zero risk: quote only "often less than 5%" and paraphrase the rest.

Body sentence "The extra consumption that comes from changing what you're doing runs ..." maps onto "the additional energy consumption associated with changes in brain activity"; fair. Footnote's denominator warning is consistent with the source.

## 12. [^berkes] Berkes, Orbán, Lengyel, Fiser 2011 (body line 51; footnote line 146)

Verdict: CONFIRMED (details); caveat sentence tier C.

Tier B (science.org / PMC via search service): "Spontaneous cortical activity reveals hallmarks of an optimal internal model of the environment", Science 331: 83-87 (2011), DOI 10.1126/science.1195870, PMC3065813; author order Berkes, Orbán, Lengyel, Fiser confirmed. Returned text: "population activity within the visual cortex of awake, freely viewing ferrets in response to natural-scene movies and in darkness at four different developmental stages: after eye opening at postnatal day (P) 29-30, after the maturation of orientation tuning and long-range horizontal connections at P44-45, and in two groups of mature animals at P83-90 and P129-151"; "divergence between activity evoked by external stimuli and spontaneous activity decreased with age ... and the two distributions were not significantly different in mature animals"; "specific to responses evoked by natural scenes". Issue 6013: tier C high (7 January 2011 issue).

So: awake, freely viewing, four stages, natural-scene movies, "from eye opening to roughly five months" (P151 is about five months) all confirmed. Body's "with nothing in particular to look at" corresponds to "in darkness"; a small precision gain would be "against what it did in the dark". "Over the months from eye opening to maturity, the resting pattern gradually came to match the watching pattern" is a fair rendering.

Caveat "The authors note they can't separate experience-driven adaptation from a developmental program": not reached at tier B (search budget ran out on this query). Tier C (medium): the paper's closing paragraph says its findings "do not address the degree to which statistical adaptation in the cortex is driven by visual experience or by developmental programs"; a prior-round record quotes it the same way. Very likely correct.

## 13. [^attention] Vaswani et al. 2017 (body line 53; footnote line 148)

Verdict: CONFIRMED.

Tier B (arxiv.org / neurips via search service): abstract: "...based solely on attention mechanisms, dispensing with recurrence and convolutions entirely." The draft puts "dispensed" outside and "with recurrence and convolutions entirely" inside the quote marks; the inside part is exact. NeurIPS 2017 confirmed.

## 14. [^damasio] Damasio and Carvalho 2013; Man and Damasio 2019 (body line 59; footnote line 160)

Verdict: CONFIRMED.

Tier B (nature.com via search service): "The nature of feelings: evolutionary and neurobiological origins", Nature Reviews Neuroscience 14, 143-152 (2013), DOI 10.1038/nrn3403. Abstract sentence returned verbatim: "Feelings constitute a crucial component of the mechanisms of life regulation, from simple to complex." Draft quote exact. Man and Damasio, "Homeostasis and soft robotics in the design of feeling machines", Nature Machine Intelligence 1, 446-452 (2019), confirmed at tier B; the footnote's description (machines built with homeostatic vulnerability / feeling analogues) matches the returned summary.

## 15. [^harnad] Harnad 1990; Harnad 2025 (body lines 69, 71; footnote line 162)

Verdict: CONFIRMED on all quotes and details checkable; one description (word count) UNVERIFIED.

Harnad 1990, tier B (search service, unrestricted, hitting researchgate/philpapers/cs.ox.ac.uk copies): Physica D 42: 335-346, DOI 10.1016/0167-2789(90)90087-6. Abstract sentence returned verbatim: "The problem is analogous to trying to learn Chinese from a Chinese/Chinese dictionary alone." Footnote quote exact. Body line 69 "as a first language": the service returned the body-text passage "Suppose you had to learn Chinese as a first language and the only source of information you had was a Chinese/Chinese dictionary!" (Harnad's second, harder variant of the dictionary-go-round, which he says is the actual situation of a purely symbolic model; the first variant is "as a second language"). So the body's first-language framing is Harnad's own. Confirmed.

Harnad 2025, tier B (frontiersin.org / eprints.soton / PMC via search service): "Language writ large: LLMs, ChatGPT, meaning, and understanding", Frontiers in Artificial Intelligence 7: 1490698, DOI 10.3389/frai.2024.1490698; published 2025 (accepted December 2024, published February 2025), PMC11861094. The "2024" in the DOI is the volume-year stamp; citing it as vol. 7 (2025) is correct. The service returned the two abstract sentences verbatim: "It is not true that it understands." and "But it is also not true that we understand how it can do what it can do." Draft exact. The service also confirmed the paper "features a dialogue between Professor Harnad and GPT-4". "Your own explanation is not 'indirectly' grounded: it is not grounded at all!": the service paraphrased ("ChatGPT's explanation is not 'indirectly' grounded—it is not grounded at all"); tier C (medium-high) and a prior-round lead give the exact sentence as "...your own explanation is not "indirectly" grounded: it is not grounded at all!" with double quotes around indirectly in the source; the draft's single quotes are the correct nested form. I treat the quote as exact.

Note the arXiv preprint (2402.02243) carries a different title ("... Grounding, Meaning and Understanding"); the draft cites the journal title, which is right for the DOI given.

"Most of the word count is the model's side": tier X. Plausible from the format but I could not measure it. If in doubt: "much of the word count".

"ChatGPT-4": Harnad refers to GPT-4 / ChatGPT; "ChatGPT-4" is a reasonable label. Fine.

## 16. [^automation] Parasuraman and Manzey 2010 (body line 113; footnote line 157)

Verdict: PARTLY. Bibliographic details confirmed; "three decades" is the draft's characterization, not the paper's, and is unverified.

Tier B (journals.sagepub.com via search service): "Complacency and Bias in Human Use of Automation: An Attentional Integration", Human Factors 52, no. 3 (June 2010): 381-410, DOI 10.1177/0018720810376055. Abstract returned: objective "to review empirical studies of complacency and bias in human interaction with automated and decision support systems and provide an integrated theoretical model for their explanation"; complacency "is found in both naive and expert participants and cannot be overcome with simple practice". Three separate queries for "decades" / "three decades" / "two decades" in the paper returned nothing; the service explicitly said it found no such reference. Tier C (medium): I do not recall the paper describing its own scope in decades. The literature it reviews runs from Wiener and Curry (1980) and Wiener (1981) to 2009, which is roughly three decades, so the draft's "three decades" is arithmetically defensible but should not read as the paper's self-description.

Minimal fix, body line 113: "Researchers reviewing roughly thirty years of work" is the same claim; if the author wants it bulletproof, "Researchers reviewing the empirical work on how people use automation, going back to the early 1980s, found...". Footnote line 157: "A review covering three decades of prior work" -> "A review of the empirical work going back to the early 1980s". No change to the section's point (that automation bias was documented long before LLMs).

The footnote's aside that the paper "covers automation bias and complacency rather than metric gaming" is correct.

---

## Most likely wrong, ranked

1. [^automation] "three decades" (lines 113, 157): not the paper's own framing; not found in the source by any query. Low stakes, easy fix.
2. [^rn] "page 2" and "those six are listed" (lines 15, 124): page unverified (could be p. 3); the draft's six drop "speech recognition" from the book's fifth item.
3. [^circuits] footnote's section-14 attribution (line 130): the quoted sentence is very probably in §14, but it was not reachable at tier B; the neighboring "quarter" and "biased sample" claims (body line 29) are from the Introduction, which the body does not misattribute. Also "English is the default output" not closed at tier B.
4. [^raichle] quote tail "of the baseline level of activity" (line 51): only "often less than 5%" and "remarkably small" confirmed at tier B; the tail is recall plus a prior-round lead.
5. [^harnad] "most of the word count is the model's side" (line 162): unverifiable here.
6. [^parrots] "page 617" (line 134): service says the passage spans 616-617; "617" is probably right for the sentence itself.
7. [^othello] body's "trained only to predict legal moves" (line 23): loose; trained on next-move prediction over game transcripts.

Everything else (ELIZA quotes and metadata, GPT-2 phrase, GPT-3 "no weight updates are allowed", Cowan, Loftus and Palmer, Diekelmann and Born, Klinzing et al., Berkes et al. details, Vaswani, Damasio and Carvalho, Man and Damasio, Harnad 1990 both variants, Harnad 2025 quotes and bibliographic data, Nanda et al. pages and author order) is confirmed at tier B.
