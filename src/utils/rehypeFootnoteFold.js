/**
 * Wraps the GFM footnotes section in a closed <details> fold so long source
 * lists don't dominate the page. The screen-reader heading stays outside the
 * fold because footnote references point at it with aria-describedby.
 * A script in PostDetails.astro opens the fold when a footnote link is used.
 */
export function rehypeFootnoteFold() {
  return tree => {
    walk(tree);
  };
}

function walk(node) {
  if (!node || !Array.isArray(node.children)) return;
  for (const child of node.children) {
    if (
      child.type === "element" &&
      child.tagName === "section" &&
      child.properties &&
      child.properties.dataFootnotes !== undefined
    ) {
      fold(child);
    } else {
      walk(child);
    }
  }
}

function fold(section) {
  const heading = section.children.find(
    c => c.type === "element" && /^h[1-6]$/.test(c.tagName)
  );
  const rest = section.children.filter(c => c !== heading);
  const list = rest.find(c => c.type === "element" && c.tagName === "ol");
  const count = list
    ? list.children.filter(c => c.type === "element" && c.tagName === "li")
        .length
    : 0;

  const details = {
    type: "element",
    tagName: "details",
    properties: { className: ["footnotes-fold"] },
    children: [
      {
        type: "element",
        tagName: "summary",
        properties: {},
        children: [{ type: "text", value: `Sources and notes (${count})` }],
      },
      ...rest,
    ],
  };
  section.children = heading ? [heading, details] : [details];
}
