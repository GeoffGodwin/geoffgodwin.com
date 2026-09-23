#!/usr/bin/env python3
"""Check every link in the built HTML for both drafts.

Reads hrefs out of the generated pages rather than out of the markdown, because
the rendered page is what a reader actually clicks, and because markdown link
parsing has edge cases (a DOI containing parentheses, for one) that a regex over
the source will get wrong.

Run build-check.sh first, or pass --keep to it, so dist/ has the pages.
A 403 is flagged CHECK rather than FAIL: several publishers refuse automated
clients while serving the page fine in a browser.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.home() / "workspace/geoffgodwin/geoffgodwin.com"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
SKIP = ("linkedin.com/in/geoffgodwin", "github.com/geoffgodwin")


def hrefs_from(path):
    html = path.read_text(encoding="utf-8", errors="replace")
    # Only the article body, so we skip the site's own nav and footer links.
    start = html.find("<article")
    end = html.find("</article>")
    body = html[start:end] if start != -1 and end != -1 else html
    return re.findall(r'href="(https?://[^"]+)"', body)


def status_of(url):
    out = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L",
         "--max-time", "30", "-A", UA, url],
        capture_output=True, text=True,
    )
    return out.stdout.strip() or "000"


def main():
    pages = sorted((ROOT / "dist/posts").glob("zz-part-*/index.html"))
    if not pages:
        print("No built pages found. Run build-check.sh with --keep first.")
        return 1

    seen = {}
    for page in pages:
        for url in hrefs_from(page):
            seen.setdefault(url, set()).add(page.parent.name)

    bad = 0
    for url in sorted(seen):
        if any(s in url for s in SKIP):
            continue
        code = status_of(url)
        if code in ("200", "301", "302"):
            label = "OK   "
        elif code in ("403", "405", "429"):
            label = "CHECK"
        else:
            label = "FAIL "
            bad += 1
        print(f"{label} {code}  {url}   [{', '.join(sorted(seen[url]))}]")

    print(f"\n{len(seen)} unique links, {bad} failing.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
