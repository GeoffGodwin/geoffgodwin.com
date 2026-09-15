# Markdown pipeline findings (settled by a real build, 14 September 2026)

Tested by adding a temporary probe post, running `npx astro build` inside WSL,
and reading the generated HTML in `dist/`. The probe was removed afterwards.

## Footnotes render correctly

GFM footnote syntax works in `.mdx` under this Astro configuration, with no
plugin change required. Astro enables `remark-gfm` by default and
`mdx({ extendMarkdownConfig: true })` passes it through to MDX files.

Input:

    This is a sentence with a footnote marker.[^probe1]

    [^probe1]: The first footnote body, with a [link](https://example.com).

Output:

    ...footnote marker.<sup><a href="#user-content-fn-probe1"
      id="user-content-fnref-probe1" data-footnote-ref
      aria-describedby="footnote-label">1</a></sup>

    <section data-footnotes class="footnotes">
      <h2 class="sr-only" id="footnote-label">Footnotes</h2>
      <ol>
        <li id="user-content-fn-probe1">
          <p>The first footnote body, with a <a href="...">link</a>.
             <a href="#user-content-fnref-probe1" data-footnote-backref
                class="data-footnote-backref">&#8617;</a></p>
        </li>
      </ol>
    </section>

Numbering, ordering, backlinks and links inside footnote bodies all work.
Footnote definitions can sit anywhere in the file; the section is appended at
the end of the article body, before the post footer divider.

**One cosmetic issue for Geoff to decide on.** The "Footnotes" heading carries
`class="sr-only"`, which is `remark-rehype`'s default. Screen readers announce
it; sighted readers see an unlabelled ordered list appear under the closing
sign-off. No existing post has footnotes, so no CSS in `src/styles/` addresses
this. Two cheap fixes, either of which is a one-line change:

1. In `astro.config.ts`, under `markdown`, add
   `remarkRehype: { footnoteLabelProperties: {} }` to drop the `sr-only` class
   so the heading is visible.
2. Leave the markup alone and style `.footnotes` in the global stylesheet with
   a top border and spacing, treating the list itself as the visual separator.

Option 1 is the smaller change and gives the reader a labelled section. I have
not made either change; it affects every future post, so it is Geoff's call.

## Smartypants rewrites hyphens, which interacts with the no-em-dash rule

Astro enables `remark-smartypants` by default. In the probe, `--` in prose was
rendered as a literal em dash in the HTML output. The voice rules forbid em
dashes, so the drafts must never contain a double hyphen in running prose. The
`---` sequence survived as-is in the probe, but there is no reason to rely on
that. Use commas, colons and semicolons, and keep `---` only as a section rule
on its own line, which is how the existing posts use it.
