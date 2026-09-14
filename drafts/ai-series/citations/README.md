# Citation pass status

**Phase 1 is incomplete and nothing in this directory is citable copy.**

The verification procedure in `../citation-ledger.md` has four steps: locate the
primary source, confirm the specific claim appears in it, record the authors'
stated limitations, and record a stable URL or DOI. In the session that produced
these files, steps 1 and 4 succeeded and steps 2 and 3 could not be performed.

Outbound document fetching was blocked by the network egress proxy for every
domain attempted, including arxiv.org, anthropic.com, nature.com, dl.acm.org and
a wikipedia.org control. Web search worked, because it routes through a search
service rather than direct egress; opening a document did not. The proxy
documentation directs that a policy denial be reported rather than routed
around, so no mirror or reader-proxy workaround was attempted.

What these files therefore contain:

- Reliable bibliographic records: full author lists, titles, venues, dates,
  arXiv IDs and DOIs, established from search metadata.
- Research leads, explicitly labelled as unverified paraphrase, drawn from
  search result summaries.
- No verbatim quotes, and no slot graded FIT.

Everything here is the input to a verification pass, not the output of one.
Before any of it reaches a draft, each slot needs the primary source opened and
read, particularly the slots whose value to the series lies in repeating the
authors' own caveats accurately.

To finish the pass, either add the publisher domains to the environment's egress
allowlist and re-run, run the pass from an unrestricted machine, or supply the
PDFs for the load-bearing sources directly.
