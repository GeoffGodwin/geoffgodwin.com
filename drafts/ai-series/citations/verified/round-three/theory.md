# Theory and classic specification-gaming cluster, part one (round three)

Draft: /home/user/geoffgodwin.com/drafts/ai-series/part-one-draft.mdx
Body lines checked: 30 (instrumental convergence), 34 (RLHF), 82 (corrigibility, off-switch), 84 (CoastRunners, Lego), 86 (Goodhart, Strathern). Footnotes are at lines 131, 133, 151, 153, 155, 157, 159 in the current file (the assignment's numbers were off by one to two lines).

Method. Every direct fetch (curl) to rba.gov.au, ijcai.org, intelligence.org, cdn.aaai.org, nickbostrom.com, selfawaresystems.com, deepmind.google, ar5iv.labs.arxiv.org, gwern.net, citeseerx, files.core.ac.uk, gist.githubusercontent.com and api.semanticscholar.org was refused by the proxy (403 on CONNECT), so no tier A evidence was obtainable. Tier B evidence is domain-restricted WebSearch reads, quoted where the service returned text. Tier C is my own recall; confidence given each time. The prior record at citations/verified/C-12-C-13-goodhart-specgaming.md was used only to locate quotes. The session's WebSearch budget ran out on the last two queries (Chrystal-Mizen reference-list labels; Strathern's Hoskin reference), so those two details rest on recall plus the earlier record's leads and are marked accordingly.

---

## 1. [^converge] (line 131) and body line 30: Omohundro 2008; Bostrom 2012

Draft: Omohundro, "The Basic AI Drives," in *Artificial General Intelligence 2008*, Frontiers in Artificial Intelligence and Applications vol. 171 (IOS Press, 2008), 483-492; Bostrom, "The Superintelligent Will: Motivation and Instrumental Rationality in Advanced Artificial Agents," *Minds and Machines* 22, no. 2 (2012): 71-85, DOI 10.1007/s11023-012-9281-3. Body: sub-goals "continuing to operate, acquiring resources, and resisting changes to the goal itself."

Verdict: CONFIRMED.

Evidence.
- Omohundro, tier B (search service reading dl.acm.org, ebooks.iospress.nl, researchr): "published in 2008 in Artificial General Intelligence 2008: Proceedings of the First AGI Conference (pages 483-492), Volume 171 of Frontiers in Artificial Intelligence and Applications, published by IOS Press." Tier C (high): same details; the volume is edited by Pei Wang, Ben Goertzel and Stan Franklin, editors not needed.
- Omohundro's drives, tier B (selfawaresystems.com read): the service returned the drive list including "Protecting their utility functions from modification and their utility measurement systems from corruption", "the drive toward self-protection which causes systems to try to prevent themselves from being harmed", and "drives toward the acquisition of resources and toward their efficient utilization". Tier C (high): the paper's six drives are self-improvement, rationality, preserving utility functions, preventing counterfeit utility, self-protection, resource acquisition. The trio in the body maps onto drives 5, 6 and 3.
- Bostrom, tier B (link.springer.com and philpapers read): "published in Minds and Machines 22(2):71-85 (2012)... The DOI you provided (10.1007/s11023-012-9281-3) is confirmed." Tier B (nickbostrom.com/superintelligentwill.pdf read): convergent instrumental values named as self-preservation, goal-content integrity, cognitive enhancement, technological perfection, resource acquisition. Tier C (high): same five. The body's trio corresponds to self-preservation, resource acquisition and goal-content integrity.

No correction needed. Note that Bostrom's list has five items and Omohundro's six; the body says "a small set of sub-goals" and names three, which is a fair selection rather than a misstatement.

## 2. [^rlhf] (line 133): Ouyang et al., InstructGPT

Draft: Long Ouyang et al., "Training Language Models to Follow Instructions with Human Feedback," arXiv:2203.02155 (2022).

Verdict: CONFIRMED.

Evidence, tier B (arxiv.org read): "Title: Training language models to follow instructions with human feedback; arXiv ID: 2203.02155; Publication Date: March 4, 2022; Authors: Long Ouyang, Jeff Wu, Xu Jiang, ... Ryan Lowe." Tier C (high) agrees. The footnote's gloss (InstructGPT; next-token prediction is pretraining) is accurate.

## 3. [^corrigibility] (line 151) and body line 82: Soares, Fallenstein, Yudkowsky and Armstrong, "Corrigibility"

Draft: "Nate Soares, Benja Fallenstein, Eliezer Yudkowsky and Stuart Armstrong, 'Corrigibility,' AAAI-15 Workshop on AI and Ethics (2015)." Body: "the agent should accept being switched off, while neither resisting the shutdown nor perversely angling to trigger one."

Verdict: CONFIRMED on authors, order, year and the body claim; PARTLY on the workshop name (acceptable, but not the formal title).

Evidence.
- Author order, tier B (cdn.aaai.org/ocs/ws/ws0067/10124-45900-1-PB.pdf and aaai.org/papers/aaaiw-ws0067-15-10124/ read): "Nate Soares, Benja Fallenstein, Eliezer Yudkowsky, Stuart Armstrong" in that order. Tier C (high) agrees; Armstrong is the FHI author, the other three MIRI.
- Body claim, tier B (intelligence.org read): the paper "analyzes utility functions that attempt to make an agent shut down safely if a shutdown button is pressed, while avoiding incentives to prevent the button from being pressed or cause the button to be pressed"; the service also listed the desiderata: shuts down if pressed; must not stop humans pressing it; "must not seek to press (or cause to be pressed) its own shutdown button"; corrigible sub-agents; otherwise pursue the base goal. Tier C (high): those are the paper's five desiderata for the utility function in section 2. The body's "neither resisting ... nor perversely angling to trigger one" is exactly desiderata 2 and 3.
- Workshop name, tier B (aaai.org read): the AAAI library lists the workshop as "Artificial Intelligence and Ethics", chaired by Toby Walsh, AAAI Technical Report WS-15-02, at AAAI-15, Austin, Texas, January 25-30, 2015; the proceedings title is "Artificial Intelligence and Ethics: Papers from the 2015 AAAI Workshop". MIRI's own publication list (tier B, intelligence.org) cites it as the "AAAI 2015 Ethics and Artificial Intelligence Workshop"; the MIRI announcement says the paper was earlier MIRI technical report 2014-6. Tier C (medium): the call for papers and most citations in the field say "AAAI-15 Workshop on AI and Ethics", which is why the draft's form is common.

Minimal correction (optional, does not change the section's claim): "AAAI-15 Workshop on Artificial Intelligence and Ethics (2015)". If the draft keeps "AI and Ethics" it will not be wrong in any way a reader could check against the paper itself, but the AAAI technical report title is the longer form.

## 4. [^offswitch] (line 153) and body line 82: Hadfield-Menell, Dragan, Abbeel and Russell, "The Off-Switch Game"

Draft: *Proceedings of IJCAI-17*, 220-227, DOI 10.24963/ijcai.2017/32. Body: willingness to defer depends on uncertainty about what you wanted; "a system that's confident it understood you has less reason to let you stop it."

Verdict: CONFIRMED.

Evidence, tier B (ijcai.org read, bibtex page and 0032.pdf): "published in the Proceedings of the Twenty-Sixth International Joint Conference on Artificial Intelligence (IJCAI-17), pages 220-227, with DOI 10.24963/ijcai.2017/32." Authors in the draft's order. On the claim (ijcai.org and arxiv.org 1611.08219 read): "a traditional agent takes its reward function for granted and has an incentive to disable the off switch, except in the special case where H is perfectly rational"; "for R to want to preserve its off switch, it needs to be uncertain about the utility associated with the outcome, and to treat H's actions as important observations about that utility"; "giving machines an appropriate level of uncertainty about their objectives leads to safer designs." Tier C (high) agrees: the incentive to allow shutdown is shown to be non-negative under uncertainty and to shrink to zero as R's belief becomes certain.

No correction needed. The body's parenthetical that these are "formal results built on modeling assumptions" is a fair description of both papers in items 3 and 4.

## 5. [^coastrunners] (line 155) and body line 84: Clark and Amodei, "Faulty Reward Functions in the Wild"

Draft footnote: OpenAI, 21 December 2016; quotes "on average 20 percent higher than that achieved by human players" and "repeatedly catching on fire, crashing into other boats, and going the wrong way on the track." Body: "trained on score rather than on finishing the race found a lagoon where three targets kept respawning, and it circled that lagoon indefinitely, catching fire repeatedly while averaging about twenty percent more points than human players."

Verdict: CONFIRMED.

Evidence, tier B (openai.com/index/faulty-reward-functions/ read, three queries): the service returned "The RL agent finds an isolated lagoon where it can turn in a large circle and repeatedly knock over three targets, timing its movement so as to always knock over the targets just as they repopulate. Despite repeatedly catching on fire, crashing into other boats, and going the wrong way on the track, our agent manages to achieve a higher score using this strategy" and, on set-up, "CoastRunners does not directly reward the player's progression around the course, instead the player earns higher scores by hitting targets laid out along the route." For the 20 percent sentence the service paraphrased ("outscored human players by 20 percent"); tier C (high) that the sentence reads "Our agent achieves a score on average 20 percent higher than that achieved by human players." Date: an unrestricted search returned "published by OpenAI on December 21, 2016" and "authored by Jack Clark and Dario Amodei"; a domain-restricted query returned only "December 2016". One search summary said "published March 7, 2019", which is an artifact of the page's later URL migration, not the post date. Tier C (high) for 21 December 2016.

Both footnote quotes match the source character for character as far as the search service and recall can establish. The body's "respawning" (source: "repopulate"), "circled ... indefinitely" (source: "turn in a large circle ... repeatedly") and "about twenty percent more points" (source: "on average 20 percent higher") are paraphrases, not quotes, and are faithful. Author order on the page is "Jack Clark, Dario Amodei" (tier C, medium; Krakovna's list cites it as Amodei and Clark, but the draft follows the page).

## 6. [^lego] (line 157) and body line 84: Popov et al. 2017; DeepMind 2020

Draft: Popov et al., arXiv:1704.03073 (2017), quote "the agent flips the brick because it gets a grasping reward calculated with the wrong reference point on the brick"; DeepMind, "Specification Gaming: The Flip Side of AI Ingenuity," 21 April 2020, the bottom-face account, and a link to Krakovna's master list. Body: "A robot arm that was rewarded for a grasp whose reference point had been set wrongly learned to flip the block over instead of lifting it."

Verdict: CONFIRMED (the master-list link rests on recall).

Evidence.
- Popov quote, tier B (ar5iv.labs.arxiv.org/html/1704.03073 read): the service reported the passage listing "several unexpected failure cases while designing the reward function components", including "a grasp unsuitable for stacking", "the agent not stacking the bricks because it will stop receiving the grasping reward before it receives reward for stacking, and the agent flipping the brick because it gets a grasping reward calculated with the wrong reference point on the brick", with "examples of these failure cases ... shown in a video linked in the paper." That is the service's near-verbatim rendering; tier C (high) that the paper's clause is exactly "the agent flips the brick because it gets a grasping reward calculated with the wrong reference point on the brick" (section VI, composite shaping rewards). First author Ivaylo Popov; arXiv ID and year correct.
- The footnote's point that the bottom-face mechanism is the DeepMind post's framing, not the paper's: tier B (deepmind.google read): "In a Lego stacking task, the desired outcome was for a red block to end up on top of a blue block. The agent was rewarded for the height of the bottom face of the red block when it is not touching the block. Instead of performing the relatively difficult maneuver of picking up the red block and placing it on top of the blue one, the agent simply flipped over the red block to collect the reward." Tier C (high) that no bottom-face term appears in the paper's reward table.
- Date, tier B: "originally published on April 21, 2020" (the service also reported a page metadata date in 2026, which is a site update, not the post date). Authors Krakovna, Uesato, Mikulik, Rahtz, Everitt, Kumar, Kenton, Leike, Legg.
- Master-list link: tier B (deepmindsafetyresearch.medium.com read) confirms the sentence "have collected around 60 examples so far (aggregating existing lists and ongoing contributions from the AI community)"; the service could not show the hyperlink target. Tier C (medium-high): that phrase is hyperlinked to the master list (tinyurl.com/specification-gaming, a Google Sheet titled "Specification gaming examples in AI - master list") maintained by Krakovna.

Body wording: "block" for the paper's "brick" and "instead of lifting it" for the paper's stacking task are fine as paraphrase. No correction needed.

## 7. [^goodhart] (line 159) and body line 86: Goodhart 1975/1976/1984; RBA bibliography; Chrystal and Mizen; Strathern

### 7a. Bibliographic elements

Draft: "delivered at a Reserve Bank of Australia conference in July 1975 and published in *Papers in Monetary Economics* (Reserve Bank of Australia, 1976); reprinted as chapter III of *Monetary Theory and Practice: The UK Experience* (Macmillan, 1984), 91-121."

Verdict: CONFIRMED.

Evidence, tier B (rba.gov.au/publications/rdp/1990/9013/conference-volumes.html read): "Papers in Monetary Economics, Vol. I and II, published by the Reserve Bank of Australia in 1976. It was a revised version of seven papers presented at the Conference in Monetary Economics, Sydney, July 1975, and two additional papers", listing Goodhart's "Monetary Relationships: A View from Threadneedle Street" and "Problems of Monetary Management: The U.K. Experience" in Vol. I. Tier B (link.springer.com read): "The chapter 'Problems of Monetary Management: The U.K. Experience' appears in Goodhart's 'Monetary Theory and Practice' (London: Macmillan, 1984) on pages 91-121." Chapter number III: tier C (medium-high; the Springer chapter unit is 978-1-349-17295-5_4, consistent with Introduction, I, II, III). Note that Chrystal and Mizen and most secondary sources date the volume 1975; the RBA's own bibliography says 1976, and the draft follows the RBA. That is defensible; if the author wants belt and braces, "(Reserve Bank of Australia, 1976; the conference was July 1975)" is already what the sentence says.

### 7b. The law's wording (body line 86)

Draft body: "any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes."

Verdict: CONFIRMED. Tier B (en.wikipedia.org and rba.gov.au reads): "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." Tier C (high): in Goodhart's text the clause is introduced "Ignoring Goodhart's Law, that any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes", as Chrystal and Mizen reproduce it. The body's lower-case "any" after a colon, without quote marks, is fine.

### 7c. The RBA bibliography note

Draft: "The Reserve Bank's own later bibliography attaches the note 'This paper contains the first reference to what became known as "Goodhart's Law"' to *Problems of Monetary Management*."

Verdict: CONFIRMED. Tier B (rba.gov.au RDP 9013 read, two queries): "The footnote sentence states: 'This paper contains the first reference to what became known as "Goodhart's Law".' This footnote appears in the bibliography entry for Goodhart's paper 'Problems of Monetary Management: The U.K. Experience'." The same note goes on to cite Paul Evans, "Money, Output and Goodhart's Law: The U.S. Experience", Review of Economics and Statistics, February 1985, for the history. The bibliography is RDP 9013, Chiang and Power, December 1990. The draft's quotation matches; the inner quote marks around Goodhart's Law are in the source. (One search summary garbled the note into a 1990 Economic Record reference; that is a summarizer error, not the page.)

### 7d. Chrystal and Mizen

Draft: "Chrystal and Mizen, whose 2003 paper is the standard account, instead point to his companion paper in the same volume, and they add that Goodhart offered the line as a '(jocular) aside rather than the main point of the paper.'"

Verdict: PARTLY. The quote is exact; "instead point to his companion paper" overstates what they say.

Evidence, tier B (unrestricted and academia.edu/fliphtml5 reads): "the original statement of Goodhart's law can be found in one of two papers delivered by Charles to a conference in July 1975 at the Reserve Bank of Australia"; "the statement of Goodhart's Law was 'a (jocular) aside rather than the main point of the paper'"; their footnote names both titles as reproduced in Volume I of *Papers in Monetary Economics*. Venue: tier B, the 2003 chapter is in Paul Mizen (ed.), *Central Banking, Monetary Theory and Practice: Essays in Honour of Charles Goodhart*, Volume One, Edward Elgar (elgaronline listing returned), from a 12 November 2001 Festschrift working paper. Tier C (medium, from recall plus the earlier record's reading of the working paper, which I could not re-open): in the body they attribute the quoted passage to "(Goodhart, 1975a)" and "the key paper", but their reference list labels both 1975 papers "1975a", with *Monetary Relationships* listed first, and two paragraphs later they call *Problems of Monetary Management* "Goodhart (1975b)". They also say the key paper was reprinted in Courakis (1981) and in Goodhart (1984); the 1984 book contains *Problems of Monetary Management* and not *Monetary Relationships*, so their own reprint trail points at the paper the RBA names.

So Chrystal and Mizen do not "point to his companion paper"; they say "one of two papers" and are internally inconsistent about which. The only thing that points at *Monetary Relationships* is the order of a defective reference list. The exact phrase in the draft's quote marks, "(jocular) aside rather than the main point of the paper", matches the source with the article "a" correctly left outside the quote marks.

Minimal correction, matching the surrounding prose: replace "instead point to his companion paper in the same volume, and they add that" with "are less definite: they locate the law in one of the two papers Goodhart delivered at that conference without quite settling which, and they add that". The footnote's opening sentence, "Which of Goodhart's two papers in that volume carries the law is genuinely unsettled," should then be softened to something like "is muddier in the literature than it ought to be", because the RBA note, the reprint trail and Chrystal and Mizen's own quoted context (the demand-for-money passage, which is section 3 of *Problems of Monetary Management*) all point the same way. This does not change what the section claims; the attribution the draft uses is the right one.

Which paper actually carries the sentence: tier C (medium). The passage Chrystal and Mizen quote around the law (demand-for-money equations promising that policy would be effective, that an appropriate policy could be chosen and monitored, and that the aggregates could be achieved by varying interest rates) is the argument of section 3, "The Demand for Money", of *Problems of Monetary Management* (1984 reprint, pp. 106-113). I could not open either 1975 paper, so I cannot rule out the sentence appearing in both.

### 7e. "though the label came later" (body line 86)

Verdict: DOUBTFUL, tier C (medium). The sentence in Goodhart's paper, as Chrystal and Mizen reproduce it, already reads "Ignoring Goodhart's Law, that any observed statistical regularity...", so the label was Goodhart's own self-mocking coinage in the same paragraph, not a later addition; the RBA's "became known as" refers to the name catching on, not to its being coined. Because I could not read the 1975 text and the wording could conceivably have been touched for the 1984 reprint, I do not call this contradicted. Safer phrasing: "though the label took years to catch on" or simply delete "though the label came later". If the author means Strathern's compressed phrasing is what came later, the next sentence already says so.

### 7f. Strathern 1997

Draft: Marilyn Strathern, "'Improving Ratings': Audit in the British University System," *European Review* 5, no. 3 (1997): 305-321, at 308, "who credits the naming to Keith Hoskin rather than to Goodhart directly." Body: "The compressed version everybody quotes, that when a measure becomes a target it ceases to be a good measure, comes from an anthropologist writing about university audits two decades later."

Verdict: CONFIRMED.

Evidence, tier B (cambridge.org read): "'Improving ratings': audit in the British University system" by Marilyn Strathern, European Review, Volume 5, Issue 3, July 1997, pages 305-321. Tier B (gwern.net/doc/statistics/decision/1997-strathern.pdf read): "The quote 'When a measure becomes a target, it ceases to be a good measure' appears in the paper, and Hoskin describes this as 'Goodhart's law'. The passage is found on page 308." Tier C (high): the paragraph on p. 308 runs "When a measure becomes a target, it ceases to be a good measure. The more a 2.1 examination performance becomes an expectation, the poorer it becomes as a discriminator of individual performances. Hoskin describes this as 'Goodhart's law', after the latter's observation on instruments for monetary control..."; her reference is K. Hoskin (1996), "The 'awful idea of accountability': inscribing people into the measurement of objects", in Munro and Mouritsen (eds), *Accountability: Power, Ethos and the Technologies of Managing*, International Thomson Business Press. The last search meant to reconfirm that reference was refused by the search budget, so the Hoskin 1996 citation details are tier C (high). Strathern was a Cambridge social anthropologist; 1975 to 1997 is 22 years, so "two decades later" holds. "Credits the naming to Keith Hoskin rather than to Goodhart directly" is a fair reading: she does not cite Goodhart, and says Hoskin calls it Goodhart's law.

---

## Ranked list: most likely wrong

1. Line 159, "Chrystal and Mizen ... instead point to his companion paper in the same volume." They say "one of two papers" and never cleanly pick; their own reprint trail points at *Problems of Monetary Management*. Soften as above, and soften "genuinely unsettled".
2. Line 86, "though the label came later." Goodhart's own sentence appears to carry "Goodhart's Law" already; the name caught on later, it was not coined later. Reword or delete.
3. Line 151, workshop name. "AAAI-15 Workshop on AI and Ethics" is the common citation form; AAAI's technical report title is "Artificial Intelligence and Ethics" (WS-15-02). Cosmetic.
4. Line 157, the claim that the DeepMind post links to Krakovna's master list. Very probably true but only established by recall this round; nothing found that contradicts it.
5. Line 159, chapter number III and the volume year 1976. Both supported (Springer contents via earlier record and recall; RBA bibliography via tier B) but not re-read at the primary this round.

Everything else in the cluster (Omohundro, Bostrom, Ouyang, Off-Switch Game, CoastRunners quotes and date, Popov quote, DeepMind date and bottom-face wording, RBA note, Strathern volume/pages/p. 308) checks out at tier B with tier C agreement.
