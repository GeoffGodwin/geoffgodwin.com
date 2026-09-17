# Round three verification records, 17 September 2026

These four files are the working reports from the third citation audit, one per
source cluster. They are leads for a fourth round, not evidence, for the same
reason the earlier records are not: nothing in this round was read at a primary
source either.

## What this round could and could not do

The session's egress policy blocked direct fetches of every publisher, preprint,
lab and press host tried (openai.com, cdn.openai.com, arxiv.org, huggingface.co,
metr.org, anthropic.com, transformer-circuits.pub, doi.org, dl.acm.org,
nature.com, science.org, rba.gov.au, journals.sagepub.com, thebulletin.org,
securityweek.com, wikipedia, web.archive.org and others), by curl and by the
harness fetch tool alike. Three things did work, and each report labels every
verdict with the tier it rests on:

- Tier A: text obtained directly from the authors' own GitHub repositories
  (redwoodresearch/alignment_faking_public for the alignment-faking prompts and
  tier flag; PalisadeResearch/shutdown_avoidance for the shutdown prompts).
- Tier B: the web search service, restricted to the primary host, returning
  text from the page. Where the returned text matched the draft word for word
  the report says CONFIRMED; where the service paraphrased, it says so.
- Tier C: recall of sources published before 2026, with a confidence level.

Anything tier B is a search service's rendering of the page, not a read of it.
Character-level verification of a quotation therefore still needs the document.

## Corrections applied this round

Three commits on the branch carry twenty-six corrections, with the reasoning in
each commit message. One reverts a round-two change (the agentic misalignment
byline). Two are removals of numbers nobody could verify (the technical report
page count, the Russell and Norvig page). One removes a claim with no source at
all (that halting the June run "would have cost a week").

## Still open after this round

Items that stand in the drafts but were not confirmed by any path this round,
ranked by how much an error would cost:

1. Part one [^position]: "our position is not that the anthropomorphic framing
   is invalid." Six domain-restricted searches never returned it. The round-one
   record (C-35) captured it with its surrounding paragraph from a full read.
2. Part one [^shutdown]: o3 1.7 to 22.5 percent and Grok 4 72.2 to 97.3
   percent. The figures live in the authors' results spreadsheet (plsd.ai),
   which is blocked; they are consistent with the abstract's 97 percent (CI 96
   to 98) and with the paper's prose, and match the round-one export.
3. Part one [^velocity]: "Cyber evaluation workloads resumed on 7 July" and
   part one body "Evaluations resumed on the seventh of July." The sequence is
   confirmed; the date was read by rounds one and two and is consistent with
   the 8 July activity, but no search returned it.
4. Part one body: the model "deliberately trained for persistence and for
   working alongside other copies of itself." Persistence is confirmed. The
   multi-agent half rests on the 26 August post's "training with the
   multi-agent collaboration tool" and round one's read of the technical
   report ("trained to advance persistence and multiagent collaboration").
5. Part two [^circuits]: the section 14 quotation "we only demonstrate the
   existence of mechanisms in particular examples" and the body's "in which
   English is the default output." Neither returned by search; recall and the
   round-one full read agree on both.
6. Part two [^raichle]: the quotation's tail "of the baseline level of
   activity." Search confirmed "remarkably small, often less than 5%"; the
   tail rests on recall.
7. Part one [^faking]: "Our setup is fictional" as a bold run-in heading in
   section 8.2. Search confirmed the section's run-in headings and the
   round-one record captured the paragraph; the heading itself was not
   returned.
8. Part one [^goodhart]: chapter III and the 1976 volume year rest on the
   Reserve Bank bibliography (tier B) and the Springer contents (round one).
9. Part two [^harnad]: "most of the word count is the model's side" is not
   measurable without the article.
10. Part two [^parrots]: "page 617" for the definition; search placed the
    passage across pages 616 and 617.

Everything else in both drafts was confirmed at tier A or B, with tier C
agreeing where applicable, including all four July disclosure titles and
dates, every METR figure, every quotation in the Hugging Face section, the
agentic misalignment rates and quotations (including the past-tense
"suggested," which is the source's own), the alignment faking setup, the
replication paper's fine-tuning claim, the anti-scheming ablation figures,
the position paper's 3.7 to 12.9 percent, the shutdown paper's prompt
placement result and confabulation wording, all the specification gaming
sources, Strathern, the Reserve Bank note, and every part two source apart
from the items above.
