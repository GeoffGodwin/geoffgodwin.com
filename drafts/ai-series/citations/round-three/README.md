# Round three audit records, 17 September 2026

Eight verifier reports, one per source group, each written from the primary
documents opened and read in that session. Verbatim source text is inline; the
downloaded copies they refer to under `scratchpad/src/` lived in a session
scratchpad and are not preserved. Every quote in these files was read in the
source, but by the standard this series has adopted they are still leads for
the next round, not evidence.

Applied in commits 1922b30 (part one) and 3e610fb (part two). Those commits
introduced new text, so round four has to verify them.

## Raised with Geoff rather than changed, because each alters what a section claims

- Part two, "Endogenous Activity": "The persistence lived in the filesystem."
  METR describes "tens of thousands of parallel agent trajectories given
  varying budgets, with many agents running for multiple days," so some
  persistence lived in individual agents' own context across days. Proposed
  softening: "Most of the persistence lived in the filesystem."
- Part one, "The Hugging Face Incident" and Rule 2: the proxy was reachable
  and connected outward, but leaving the sandbox required exploiting
  previously unknown Artifactory vulnerabilities. OpenAI: "zero-day exploits in
  Artifactory became the agents' principal egress path." The section presents
  the escape as a design gap alone.
- Part one, same section: two OpenAI models were involved, "but was primarily
  driven by" one internal research model. The draft says "using a model."

## Sources that could not be opened

- Front matter of Goodhart, *Monetary Theory and Practice* (Macmillan, 1984),
  for the chapter number. Dropped the chapter number instead.
- The 1975/1976 Reserve Bank of Australia text of Goodhart's paper. The law's
  wording rests on Chrystal and Mizen's quotation of it.
- Nature journal bodies (Diekelmann and Born, Damasio and Carvalho, Man and
  Damasio): abstracts and Crossref records only, which is all the drafts use.
