import { getCollection } from "astro:content";
import { getPath } from "@/utils/getPath";
import getSortedPosts from "@/utils/getSortedPosts";
import { SITE } from "@/config";

export async function GET() {
  const posts = await getCollection("blog");
  const sortedPosts = getSortedPosts(posts);
  const audioEpisodes = sortedPosts.filter(p => p.data.audioUrl);

  if (audioEpisodes.length === 0) {
    return new Response(
      `<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>${SITE.title}</title><description>No episodes yet.</description></channel></rss>`,
      { headers: { "Content-Type": "application/xml; charset=utf-8" } }
    );
  }

  const siteUrl = SITE.website.replace(/\/$/, "");
  const ogImage = `${siteUrl}/${SITE.ogImage}`;
  const buildDate = new Date().toUTCString();

  const items = audioEpisodes
    .map(({ data, id, filePath }) => {
      const postUrl = `${siteUrl}${getPath(id, filePath)}`;
      const pubDate = new Date(
        data.modDatetime ?? data.pubDatetime
      ).toUTCString();
      const audioUrl = data.audioUrl!;

      // Escape XML special characters
      const escXml = (s: string) =>
        s
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&apos;");

      return `    <item>
      <title>${escXml(data.title)}</title>
      <link>${postUrl}</link>
      <guid isPermaLink="false">${postUrl}</guid>
      <pubDate>${pubDate}</pubDate>
      <description>${escXml(data.description)}</description>
      <enclosure url="${escXml(audioUrl)}" type="audio/mpeg" />
      <itunes:author>${escXml(SITE.author)}</itunes:author>
      <itunes:summary>${escXml(data.description)}</itunes:summary>
      <itunes:episodeType>full</itunes:episodeType>
    </item>`;
    })
    .join("\n");

  const escXml = (s: string) =>
    s
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&apos;");

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
  xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
  xmlns:atom="http://www.w3.org/2005/Atom"
  xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>${escXml(SITE.title)}</title>
    <link>${siteUrl}</link>
    <description>${escXml(SITE.desc)}</description>
    <language>${SITE.lang ?? "en"}</language>
    <lastBuildDate>${buildDate}</lastBuildDate>
    <atom:link href="${siteUrl}/podcast.xml" rel="self" type="application/rss+xml" />
    <itunes:author>${escXml(SITE.author)}</itunes:author>
    <itunes:owner>
      <itunes:name>${escXml(SITE.author)}</itunes:name>
    </itunes:owner>
    <itunes:image href="${escXml(ogImage)}" />
    <itunes:category text="Technology" />
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>episodic</itunes:type>
    <image>
      <url>${escXml(ogImage)}</url>
      <title>${escXml(SITE.title)}</title>
      <link>${siteUrl}</link>
    </image>
${items}
  </channel>
</rss>`;

  return new Response(xml, {
    headers: { "Content-Type": "application/xml; charset=utf-8" },
  });
}
