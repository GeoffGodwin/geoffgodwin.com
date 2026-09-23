# Resume instructions for the citation verification pass

The first pass ran in a session whose network policy blocked every publisher
and preprint host. Bibliography and identifiers are established; claim
confirmation is not. This file is what a fresh session needs to finish the job.

Read first: `../citation-ledger.md` for per-slot status, `README.md` for what
the blocked pass could and could not do, `verification-notes.md` for checks run
against search metadata and two corrections to the batch reports.

Everything below needs the primary source opened and read. Ordered by how much
damage an error would do.

## 1. C-18, the interpretability slots

Sources: Anthropic's "On the Biology of a Large Language Model" and the
companion circuit-tracing methods paper, March 2025, at transformer-circuits.pub.

The batch agent read a GitHub mirror truncated after section 8, so **section 14,
Limitations, of the Biology paper is entirely unverified**. Read it.

Confirm or correct these, which the mirror supported:
- The model studied is Claude 3.5 Haiku only.
- Rhyme planning: "often activates features corresponding to candidate
  end-of-next-line words prior to writing the line."
- Language independence: middle-layer features are "more language-agnostic,"
  but "there are important mechanistic ways in which English is privileged"
  and the picture is one "in which English is the default output."
- Attribution graphs give insight for "about a quarter of the prompts we've
  tried"; highlighted cases are "a biased sample"; findings are "existence
  proofs" the authors say they cannot guarantee generalise.
- The methods paper's statement that graphs describe a replacement model and
  carry no information about influence via attention patterns.

Do not quote the "forward planning and backwards planning" sentence; it came
through the mirror garbled.

## 2. C-6, the agentic misalignment disclaimers

Anthropic, "Agentic Misalignment," June 2025. The post's caveat paragraph
depends on two sentences nobody has read: that the scenarios were constructed
to leave no good options, and that the authors do not believe this reflects
deployed behaviour. Quote both verbatim or the paragraph cannot be written.
Also confirm the reported concession that they red-teamed iteratively until
harmful behaviour became likely.

## 3. C-8, the shutdown-resistance conflict

Schlatter, Weinstein-Raun and Ladish, "Incomplete Tasks Induce Shutdown
Resistance in Some Frontier LLMs," arXiv:2509.14260, TMLR 2026,
https://openreview.net/forum?id=e4bTTqUnJH

Two reported results conflict and must not share a sentence until resolved:
that a precedence clause drove resistance to zero, and that some models
interfered up to 97% of the time despite explicit instruction. Establish which
conditions each belongs to. Also read Rajamanoharan and Nanda's analysis and
the BlueDot replication.

## 4. C-5 with C-34, the scope of alignment faking

Greenblatt et al., arXiv:2412.14093, and the replication "Alignment Faking
Revisited" with its peer-reviewed companion, arXiv:2506.18032, NeurIPS 2025.
Settle the model counts: the batch reported 3 of 16, search indicated 5 of 25.
Confirm that the model's belief about being in training is planted in its
prompt rather than independently inferred.

## 5. C-13, the Goodhart source

Goodhart published two papers in the same 1975 Reserve Bank of Australia
volume. Establish which carries the law; better sources point to "Problems of
Monetary Management: The U.K. Experience." Chrystal and Mizen (2003) is the
standard treatment of this exact question. Confirm Strathern 1997, European
Review 5(3): 305-321, as the source of the famous phrasing.

## 6. C-12, the Lego example

Confirm the block-flip behaviour is actually described in Popov et al.,
arXiv:1704.03073. Drop the example if it is not.

## Also worth reading if time allows

C-25 Raichle and Mintun 2006 for the under-5%-of-baseline figure; C-26 Berkes
et al. 2011 for the spontaneous-activity evidence; C-31 Harnad 2025 for the
grounding application; C-35 Gupta et al. arXiv:2606.07612 for the position
paper the series should engage in part one section 3.

## When the pass is done

Update the ledger's Status and Ev columns, then phase 2 can begin: part one
first, then part two, 2,200 words each. The outlines are the source of truth
for structure and are not to be re-litigated.
