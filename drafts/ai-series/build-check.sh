#!/usr/bin/env bash
# Builds both drafts as temporary unlisted posts and reports footnote integrity.
# Pass --keep to leave the built pages in dist/ (link-check.py reads them).
set -u
cd ~/workspace/geoffgodwin/geoffgodwin.com || exit 1

KEEP=0
[ "${1:-}" = "--keep" ] && KEEP=1

for f in part-one part-two; do
  sed -e 's/^draft: true/draft: false/' \
      -e 's/^pubDatetime: .*/pubDatetime: 2026-12-31T11:00:00Z/' \
      "drafts/ai-series/${f}-draft.mdx" > "src/data/blog/zz-${f}.mdx"
done

npx astro build 2>&1 | grep -Ei 'error|Complete!' | tail -2

for f in part-one part-two; do
  h="dist/posts/zz-${f}/index.html"
  if [ -f "$h" ]; then
    refs=$(grep -o 'data-footnote-ref' "$h" | wc -l)
    notes=$(grep -oE 'id="user-content-fn-[a-z0-9]+"' "$h" | wc -l)
    bad=$(grep -c '\[\^' "$h" || true)
    echo "${f}: refs=${refs} notes=${notes} unresolved=${bad}"
  else
    echo "${f}: PAGE NOT BUILT"
  fi
done

# The source .mdx copies always go; they must never be committed.
rm -f src/data/blog/zz-part-one.mdx src/data/blog/zz-part-two.mdx

if [ "$KEEP" -eq 0 ]; then
  rm -rf dist/posts/zz-part-one dist/posts/zz-part-two
else
  echo "(built pages kept in dist/posts/ for link checking)"
fi
