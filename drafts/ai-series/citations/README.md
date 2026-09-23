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

## Second attempt, 15 September 2026

The egress policy has not changed. Re-tested at the start of a fresh session,
by two independent paths:

- Direct HTTPS from the container (`curl` through the agent proxy at
  127.0.0.1:35835): `arxiv.org:443` and `transformer-circuits.pub:443` both
  returned `connect_rejected`, logged by the proxy as "gateway answered 403 to
  CONNECT (policy denial or upstream failure)."
- The harness fetch tool, which routes differently: `arxiv.org`,
  `transformer-circuits.pub`, `openreview.net` and an `en.wikipedia.org`
  control all returned `EGRESS_BLOCKED`.

Web search still works and still returns substantive summaries, because it
resolves through a search service rather than direct egress. That is the same
asymmetry the first pass hit, and it is the trap: the summaries read like
findings while meeting none of steps 2 and 3 of the verification procedure.
Nothing sourced that way has been promoted in the ledger.

One correction the search layer did surface, recorded here as a lead rather
than as verification. The batch 2 report held that a precedence clause drove
shutdown resistance to zero. Search summaries of arXiv:2509.14260 report the
opposite direction: placing the allow-shutdown instruction in the system or
developer prompt, where it would normally take precedence, made *most models
more* likely to resist than placing it in the user prompt, and the 97% figure
(95% CI: 96-98%) belongs to the condition with an explicit instruction not to
interfere. If that holds on a read of the paper, the batch report is wrong and
C-8 becomes a stronger slot than the ledger currently grades it. It still needs
the paper.

Unblocking requires a change to the environment's network policy, which is a
session-configuration matter rather than anything this session can reach. See
https://code.claude.com/docs/en/claude-code-on-the-web. The alternative is to
supply the PDFs for the load-bearing sources directly into the repository or
the session.
