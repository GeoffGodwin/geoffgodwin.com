# part-two-b: verification report (part two, lines 43-113 and footnotes cowan..automation)

Sources opened (all saved under scratchpad/src/):
- Crossref JSON for all 11 DOIs (crossref-*.json)
- cowan2001-cambridge.pdf (Cambridge Core bronze PDF of BBS 24(1), 99 pp incl. commentaries) -> cowan2001.txt
- loftus1974-uci-wb.pdf (Wayback copy of webfiles.uci.edu/eloftus/LoftusPalmer74.pdf, publisher scan) -> loftus1974.txt
- diekelmann2010-nature.html, klinzing2019-nature.html, damasio2013-nature.html, man2019-nature.html (nature.com abstract pages; bodies paywalled)
- arxiv-2005.14165.pdf/.txt (GPT-3), arxiv-1706.03762.pdf/.txt (Transformer)
- raichle2015-pmc.xml/.txt (Europe PMC full text, PMC4387513)
- berkes2011-wb.txt (Wayback copy of PMC3065813, NIH author manuscript; PMC itself is behind reCAPTCHA and Europe PMC returned 500)
- harnad1990-arxiv.txt (arXiv cs/9906002 e-print source = harnad90.sgproblem.html, the author's HTML; soton.ac.uk copies are bot-blocked)
- harnad2025-frontiers.txt (frontiersin.org full text)
- parasuraman2010-tuberlin.pdf/.txt (TU Berlin DepositOnce copy, publisher layout, 30 pp)

## 1. [^cowan] (line 137) and line 43
| Draft | Source | Verdict |
|---|---|---|
| Line 43: "Working memory holds something like three to five items at a time, once you stop people from rehearsing them or grouping them together, rather than the famous seven." | Abstract: "Miller (1956) summarized evidence that people can remember about seven chunks in short-term memory (STM) tasks. However, that number was meant more as a rough estimate and a rhetorical device than as a real capacity limit. Others have since suggested that there is a more precise capacity limit, but that it is only three to five chunks. ... Under these conditions, rehearsal and long-term memory cannot be used to combine stimulus items into chunks of an unknown size ... A single, central capacity limit averaging about four chunks is implicated" | CONFIRMED |
| Footnote metadata: BBS 24, no. 1 (2001): 87-114 | Crossref: vol 24, issue 1, pages 87-114, issued 2001-02. Running head in PDF: "BEHAVIORAL AND BRAIN SCIENCES (2001) 24:1" (first page banner says "(2000) 24, 87–185", a known BBS quirk; 2001 is correct) | CONFIRMED |
| "Cowan's claim is a range, three to five chunks, and it holds only where rehearsal and chunking are prevented." | Sec. 1 end: "...capacity limits of three to five chunks as the population average (with a maximum range of two to six chunks in individuals)". Sec. 4.3.1: "the number seven estimates a commonly obtained, compound capacity limit, rather than a pure capacity limit in which chunking has been eliminated." | CONFIRMED |
| "The four in the title is a midpoint and partly a rhetorical device, much as Miller's seven was." | Cowan applies "rhetorical device" only to Miller: "Although Miller (1956) offered his magical number only as a rhetorical device..." He presents four as an empirical average: "A single, central capacity limit averaging about four chunks". Nothing in the target article calls his own 4 a rhetorical device. | OVERSTATED (minor). Fix: "The four in the title is the midpoint of that range, an average rather than a hard number, much as Miller's seven was a rough estimate." (Does not change the section's claim.) |

## 2. [^loftus] (line 139) and line 43
| Draft | Source | Verdict |
|---|---|---|
| Journal of Verbal Learning and Verbal Behavior 13, no. 5 (1974): 585-589 | Crossref: vol 13, issue 5, 585-589, Oct 1974. PDF header: "JOURNAL OF VERBAL LEARNING AND VERBAL BEHAVIOR 13, 585-589 (1974)" | CONFIRMED |
| "Asking how fast the cars were going when they 'smashed into' each other rather than 'hit' each other changed both the speed estimates and whether people remembered broken glass that was never there." | Abstract: "The question, “About how fast were the cars going when they smashed into each other?” elicited higher estimates of speed than questions which used the verbs collided, bumped, contacted, or hit in place of smashed. On a retest one week later, those subjects who received the verb smashed were more likely to say “yes” to the question, “Did you see any broken glass?”, even though broken glass was not present in the film." | CONFIRMED |
| Line 43: "Loftus and Palmer showed by changing one verb in a question which resulted in a change to what people remembered experiencing" | Abstract: "the questions asked subsequent to an event can cause a reconstruction in one’s memory of that event." | CONFIRMED |

## 3. [^sleep] (line 141) and line 45
| Draft | Source | Verdict |
|---|---|---|
| Diekelmann and Born, "The Memory Function of Sleep," NRN 11 (2010): 114-126 | Crossref: title "The memory function of sleep", NRN vol 11 issue 2, 114-126, 2010 | CONFIRMED |
| "Klinzing, Niethard and Born's 2019 review" | Crossref 10.1038/s41593-019-0467-3: Jens G. Klinzing, Niels Niethard, Jan Born, "Mechanisms of systems memory consolidation during sleep", Nature Neuroscience 22(10): 1598-1610, 2019 | CONFIRMED |
| Line 45: "Brains compress experience into long-term structure, a lot of that work happening during sleep, so the version of you that wakes up tomorrow has been quietly reorganized by today." | Diekelmann & Born abstract: "Sleep has been identified as a state that optimizes the consolidation of newly acquired information in memory ... Consolidation during sleep promotes both quantitative and qualitative changes of memory representations." Klinzing abstract: "qualitative transformations of memories during systems consolidation resulting in abstracted, gist-like representations." | CONFIRMED (abstract level; bodies paywalled) |
| "Several of the quantitative claims in this literature have weakened since" | Author's own judgement; not a claim about either paper's text. | UNVERIFIABLE (not a source claim) |

## 4. [^frozen] (line 143) and line 45
| Draft | Source | Verdict |
|---|---|---|
| "no weight updates are allowed" (GPT-3 paper) | Sec. 2, bullet: "Few-Shot (FS) is the term we will use in this work to refer to the setting where the model is given a few demonstrations of the task at inference time as conditioning [RWC+19], but no weight updates are allowed." | CONFIRMED (verbatim) |
| Footnote: "The paper is describing in-context learning when it says no weight updates are allowed" | The sentence defines the few-shot setting, introduced as one of the settings for "learning within the context" ("Our use of in-context learning is also similar to [RWC+19], but in this work we systematically explore different settings for learning within the context.") | CONFIRMED |
| arXiv:2005.14165 (2020), Tom B. Brown et al. | arXiv listing matches | CONFIRMED |

## 5. [^raichle] (line 145) and line 51
| Draft | Source | Verdict |
|---|---|---|
| "often less than 5% of the baseline level of activity" | Sec. 2(a): "Relative to this very high rate of ongoing energy consumption in the resting state, the additional energy consumption associated with changes in brain activity is remarkably small, often less than 5% of the baseline level of activity [5]." | CONFIRMED (verbatim) |
| Line 51 sentence: "The extra consumption that comes from changing what you're doing runs ..." | Source says "changes in brain activity", not "changing what you're doing". Close gloss; acceptable. | CONFIRMED |
| "citing his own earlier review with Mark Mintun, 'Brain Work and Brain Imaging,' Annual Review of Neuroscience 29 (2006): 449-476" | Ref 5: "Raichle ME, Mintun MA. 2006. Brain work and brain imaging. Annu. Rev. Neurosci. 29, 449–476." | CONFIRMED |
| Metadata: Phil Trans R Soc B 370 (2015): 20140172 | Crossref: vol 370, issue 1668, page 20140172, 2015-05-19 | CONFIRMED |
| Denominator note (against brain's own resting baseline; brain's ~20% share) | Same paragraph: "the brain represents about 2% of the total body weight yet it accounts for 20% of all the energy consumed [3,4]" | CONFIRMED |

## 6. [^berkes] (line 147) and line 51
| Draft | Source (NIH author manuscript via Wayback/PMC) | Verdict |
|---|---|---|
| Authors/metadata | Crossref: Pietro Berkes, Gergő Orbán, Máté Lengyel, József Fiser; Science 331(6013): 83-87, 7 Jan 2011 | CONFIRMED |
| "awake, freely viewing ferrets, visual cortex, natural-scene movies rather than gratings or noise, across four developmental stages from eye opening to roughly five months" | "We therefore measured the population activity within the visual cortex of awake, freely viewing ferrets in response to natural-scene movies (aEA) and in darkness (SA) at four different developmental stages: after eye opening at postnatal day (P) 29-30, after the maturation of orientation tuning and long-range horizontal connections at P44-45 (18), and in two groups of mature animals at P83-90 and P129-151 (n = 16 animals in total, Table S1)." Controls: "drifting sinusoid gratings at different orientations and frequencies, and dynamic binary block noise". P129-151 = 4.3-5 months. | CONFIRMED |
| "The authors note they can't separate experience-driven adaptation from a developmental program." | "While these findings do not address the degree to which statistical adaptation in the cortex is driven by visual experience or by developmental programs, they set useful constraints..." | CONFIRMED |
| Line 51: "comparing what the cortex did while the animal watched natural scenes against what it did with nothing in particular to look at" | Spontaneous activity was recorded "in darkness (SA)". "Nothing in particular to look at" understates the condition. | OVERSTATED (minor). Fix: "...against what it did in the dark." |
| Line 51: "recorded from the visual cortex of young ferrets as they grew up" | Cross-sectional design: four age groups, "n = 16 animals in total"; Fig. 4B legend: "Each dot represents one activity distribution in a different animal". Not the same animals followed over time. | OVERSTATED (minor). Fix: "recorded from the visual cortex of ferrets at four ages between eye opening and maturity". Or keep "young ferrets" and drop "as they grew up". Does not change the claim. |
| Line 51: "Over the months from eye opening to maturity, the resting pattern gradually came to match the watching pattern." | "The divergence between aEA and SA decreased with age (Fig. 2B-C, Spearman’s, ρ = −0.70, p < 0.004) and the two distributions were not significantly different in mature animals" | CONFIRMED |

## 7. [^attention] (line 149) and line 53
| Draft | Source | Verdict |
|---|---|---|
| "with recurrence and convolutions entirely" | Abstract: "We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely." | CONFIRMED (verbatim fragment; draft's "having dispensed" + quote is a fair splice) |
| "NeurIPS 2017" | Paper footer: "31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA." | CONFIRMED (conference was styled NIPS in 2017; "NeurIPS 2017" is the now-standard retroactive name; optionally "NIPS 2017") |
| "says nothing at all about persistent state between passes" | No such discussion found in the paper. | CONFIRMED |

## 8. [^damasio] (line 153) and line 59
| Draft | Source | Verdict |
|---|---|---|
| "a crucial component of the mechanisms of life regulation, from simple to complex" | Abstract (nature.com and PubMed): "Feelings are mental experiences of body states. ... Feelings constitute a crucial component of the mechanisms of life regulation, from simple to complex." | CONFIRMED (verbatim) |
| Metadata: Antonio Damasio and Gil B. Carvalho, NRN 14 (2013): 143-152 | Crossref: Antonio Damasio, Gil B. Carvalho; vol 14 issue 2, 143-152, 2013 | CONFIRMED |
| "Man and Damasio's 2019 proposal for machines built with homeostatic vulnerability" | Crossref/nature.com: Kingson Man and Antonio Damasio, "Homeostasis and soft robotics in the design of feeling machines", Nature Machine Intelligence 1(10): 446-452, 9 Oct 2019. Abstract: "we propose a new class of machines inspired by the principles of homeostasis. The resulting machines would (1) exhibit equivalents to feeling..." The word "vulnerability" is not in the abstract (body paywalled). | CONFIRMED for title/year; "vulnerability" wording UNVERIFIABLE from the abstract (a paraphrase, not a quote, so acceptable) |

## 9. [^harnad] (line 155) and lines 69-71 (HIGH RISK)
| Draft | Source | Verdict |
|---|---|---|
| "The problem is analogous to trying to learn Chinese from a Chinese/Chinese dictionary alone." | Abstract (arXiv cs/9906002 author HTML): "The problem is analogous to trying to learn Chinese from a Chinese/Chinese dictionary alone." | CONFIRMED (verbatim, in the abstract) |
| Line 69: "Picture trying to learn Chinese as a first language, with a Chinese-to-Chinese dictionary as your only source." Does Harnad say first language? | Sec. 2.2 "The Chinese/Chinese Dictionary-Go-Round": "My own example of the symbol grounding problem has two versions, one difficult, and one, I think, impossible. The difficult version is: Suppose you had to learn Chinese as a second language and the only source of information you had was a Chinese/Chinese dictionary. ... The second variant of the Dictionary-Go-Round, however, goes far beyond the conceivable resources of cryptology: Suppose you had to learn Chinese as a first language and the only source of information you had was a Chinese/Chinese dictionary! [8] This is more like the actual task faced by a purely symbolic model of the mind" | CONFIRMED. "First language" is Harnad's own second (the "impossible") variant, and he says it is the one that matches the symbolic model. "his own way of putting it" matches "My own example". |
| Physica D 42 (1990): 335-346 | Crossref: Physica D: Nonlinear Phenomena 42(1-3): 335-346, June 1990; author's header: "Physica D 42: 335-346" | CONFIRMED |
| "Language Writ Large: LLMs, ChatGPT, Meaning, and Understanding," Frontiers in Artificial Intelligence 7 (2025): 1490698 | Frontiers citation line: "Harnad S (2025) Language writ large: LLMs, ChatGPT, meaning, and understanding. Front. Artif. Intell. 7:1490698. doi: 10.3389/frai.2024.1490698 ... Published 12 February 2025". Page header says "Volume 7 - 2024" but the journal's own citation uses (2025). | CONFIRMED (title case vs sentence case is a style choice) |
| "your own explanation is not 'indirectly' grounded: it is not grounded at all!" | SH turn: "You, GPT, can provide this indirect verbal grounding to the human learner too—the way a human teacher, or a dictionary or an encyclopedia or a textbook (written by grounded humans) can. But this is with the fundamental difference that for you, GPT—the “teacher,” the verbal explainer—your own explanation is not “indirectly” grounded: it is not grounded at all!" Spoken by Harnad (SH:). Source has curly double quotes around indirectly; draft nests single quotes, standard. | CONFIRMED (verbatim apart from quote-mark nesting) |
| Line 71 framing: "he has no patience for the usual defense, which is that these systems are grounded indirectly through all the grounded human writing they trained on. His answer to that: [quote]" | The quoted sentence is Harnad's "niggle" in reply to GPT-4's own statement that it contributes "indirect grounding for users, despite having no grounding myself"; GPT-4 was not mounting that defense. But Harnad does address exactly that idea elsewhere in the same turn and later: "You lack grounding, just as a dictionary does. A dictionary’s words are all parasitic on the grounding of the lexicographers who wrote it—and your words are parasitic on the grounding of the authors of your LLM database." and "an LLM super-dictionary, like an ordinary dictionary, would continue to be an ungrounded database, hence you, GPT are only capable of providing indirect grounding to grounded human heads, while yourself remaining completely ungrounded, either directly or indirectly." | CONFIRMED in substance; slightly loose in that the quote is not literally "his answer" to someone raising that defense. Optional tightening: "His verdict on that:" instead of "His answer to that:". |
| "It is not true that it understands. But it is also not true that we understand how it can do what it can do." | Abstract: "This has even driven some of us to conclude that ChatGPT actually understands. It is not true that it understands. But it is also not true that we understand how it can do what it can do." (Harnad's own abstract, not an SH: dialogue turn) | CONFIRMED (verbatim) |
| "written as a dialogue with ChatGPT-4, and most of the word count is the model's side" | Abstract: "The exposition will be in the form of a dialogue with ChatGPT-4." Speaker labels are "SH:" and "GPT-4:" (59 turns each); word count of turns: GPT-4 ~16,800, SH ~11,600. | CONFIRMED |
| Line 71: "Harnad came back to this for language models in 2025" | Published 12 Feb 2025 (received 3 Sep 2024) | CONFIRMED |

## 10. [^automation] (line 157) and line 113
| Draft | Source (TU Berlin DepositOnce copy) | Verdict |
|---|---|---|
| Metadata: Human Factors 52, no. 3 (2010): 381-410 | PDF header: "HUMAN FACTORS Vol. 52, No. 3, June 2010, pp. 381–410. DOI: 10.1177/0018720810376055"; Crossref agrees; author "Dietrich H. Manzey" | CONFIRMED |
| "A review covering three decades of prior work" | Intro: "In the three decades since the early anecdotal reports and accident analyses mentioning complacency, a number of investigators have followed Wiener’s (1981) call for such empirical research." The "three decades" refers to complacency research since ~1980. Automation bias per se dates from Mosier and Skitka (1996): "Mosier and Skitka (1996) defined automation bias as resulting from people’s using the outcome of the decision aid “as a heuristic replacement for vigilant information seeking and processing” (p. 205)." Aviation evidence cited from Mosier, Palmer & Degani (1992) onward. | CONFIRMED for the footnote ("three decades of prior work" is the paper's own span, for the field as a whole) |
| Line 113: "Researchers reviewing three decades of work on how people use automation found the middle one of those, deference to a machine that is usually right, thoroughly documented long before this generation of technology existed." | The empirical automation-bias literature the paper reviews runs 1992-2008 (see above); "three decades" is the paper's span for complacency plus bias together. "Long before this generation of technology" (2010 review; 1990s-2000s studies) holds. Abstract: "Automation bias occurs in both naive and expert participants, cannot be prevented by training or instructions..." | CONFIRMED (slight looseness: the three decades is the review's overall span, not the automation-bias evidence specifically; no wording change strictly required. If tightening: "Researchers reviewing three decades of work on how people use automation found the middle one of those ... well documented by the late 1990s") |

## Other observations in territory
- Line 45 / [^frozen]: nothing further.
- Line 53 [^attention]: the paper's own venue string is "NIPS 2017"; harmless.
- [^harnad]: the Frontiers page header "Volume 7 - 2024" could tempt a "corrector" to change 2025 to 2024; do not, the journal's citation is (2025) and the DOI carries 2024 only because it was assigned in 2024.
- The arXiv "PDF" link for cs/9906002 returns an HTML error; the paper is only available there as HTML source (https://arxiv.org/html/cs/9906002 or the e-print). The footnote links the DOI, which is fine.
