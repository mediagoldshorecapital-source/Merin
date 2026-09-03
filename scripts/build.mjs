/**
 * Forge build — scans newsletters/ and emits a fully static site into dist/.
 *
 * No dependencies: the whole thing is plain Node + string work, so Netlify
 * only has to run `npm run build` with nothing to install.
 */
import { readFile, writeFile, mkdir, rm, readdir, cp } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const SITE = path.join(root, 'site');
const NEWSLETTERS = path.join(root, 'newsletters');
const OUT = path.join(root, 'dist');

// Gmail clips messages larger than this and hides the tail behind
// a "[Message clipped]" link, which usually eats the unsubscribe footer.
const GMAIL_CLIP_BYTES = 102 * 1024;

/** Pull whatever we can out of a newsletter README when there's no meta.json. */
function fromReadme(md) {
  const meta = {};
  const pick = (re) => {
    const m = md.match(re);
    return m ? m[1].trim() : undefined;
  };
  meta.title = pick(/^#\s+(.+)$/m);
  meta.subject = pick(/^\s*[-*]\s*Subject:\s*`(.+?)`/m);
  meta.previewText = pick(/^\s*[-*]\s*Preview text:\s*`(.+?)`/m);
  if (/\bDRAFT\b/.test(md)) meta.status = 'draft';

  const links = [];
  const canvaEdit = pick(/^\s*[-*]\s*Edit:\s*(https:\/\/www\.canva\.com\/\S+)/m);
  const canvaView = pick(/^\s*[-*]\s*View:\s*(https:\/\/www\.canva\.com\/\S+)/m);
  if (canvaEdit) links.push({ label: 'Canva — edit', url: canvaEdit });
  if (canvaView) links.push({ label: 'Canva — view', url: canvaView });
  for (const m of md.matchAll(/(https:\/\/www\.klaviyo\.com\/\S+?)(?=[\s)]|$)/g)) {
    const url = m[1];
    const label = url.includes('/campaign/') ? 'Klaviyo — campaign' : 'Klaviyo — template';
    if (!links.some((l) => l.url === url)) links.push({ label, url });
  }
  if (links.length) meta.links = links;

  // "## Before sending — checklist" -> the bolded lead of each numbered item.
  const section = md.split(/^##\s+/m).find((s) => /^Before sending/i.test(s));
  if (section) {
    const items = [...section.matchAll(/^\s*\d+\.\s+\*\*(.+?)\*\*/gm)].map((m) => m[1].trim());
    if (items.length) meta.checklist = items;
  }
  return meta;
}

/** Static preflight checks on the rendered email HTML. */
function analyze(html) {
  const bytes = Buffer.byteLength(html, 'utf8');

  const counts = new Map();
  for (const m of html.matchAll(/href\s*=\s*"([^"]*)"/gi)) {
    const url = m[1].trim();
    if (!url || url.startsWith('#')) continue;
    if (url.startsWith('{%') || url.startsWith('{{')) continue; // Klaviyo tags
    counts.set(url, (counts.get(url) ?? 0) + 1);
  }
  const links = [...counts]
    .map(([url, count]) => ({ url, count }))
    .sort((a, b) => b.count - a.count || a.url.localeCompare(b.url));

  const imgs = [...html.matchAll(/<img\b[^>]*>/gi)].map((m) => m[0]);
  const missingAlt = imgs.filter((tag) => !/\balt\s*=/i.test(tag)).length;

  return {
    bytes,
    kb: Math.round((bytes / 1024) * 10) / 10,
    clipped: bytes > GMAIL_CLIP_BYTES,
    links,
    linkCount: links.length,
    images: imgs.length,
    imagesMissingAlt: missingAlt,
    hasUnsubscribe: /unsubscribe/i.test(html),
    title: (html.match(/<title>([\s\S]*?)<\/title>/i)?.[1] ?? '').trim(),
  };
}

async function collect() {
  if (!existsSync(NEWSLETTERS)) return [];
  const dirs = (await readdir(NEWSLETTERS, { withFileTypes: true }))
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .sort();

  const out = [];
  for (const id of dirs) {
    const dir = path.join(NEWSLETTERS, id);
    const emailPath = path.join(dir, 'email.html');
    if (!existsSync(emailPath)) {
      console.warn(`  skip ${id} — no email.html`);
      continue;
    }

    const html = await readFile(emailPath, 'utf8');

    let meta = {};
    const metaPath = path.join(dir, 'meta.json');
    const readmePath = path.join(dir, 'README.md');
    if (existsSync(metaPath)) {
      meta = JSON.parse(await readFile(metaPath, 'utf8'));
    } else if (existsSync(readmePath)) {
      meta = fromReadme(await readFile(readmePath, 'utf8'));
    }

    const stats = analyze(html);
    out.push({
      id,
      title: meta.title || stats.title || id,
      summary: meta.summary ?? '',
      brand: meta.brand ?? 'Prime Ingredients',
      status: meta.status ?? 'draft',
      date: meta.date ?? '',
      subject: meta.subject ?? '',
      previewText: meta.previewText ?? '',
      links: meta.links ?? [],
      checklist: meta.checklist ?? [],
      file: `emails/${id}.html`,
      source: `newsletters/${id}/email.html`,
      stats,
    });

    await writeFile(path.join(OUT, 'emails', `${id}.html`), html);
    console.log(`  + ${id} (${stats.kb} KB, ${stats.linkCount} links)`);
  }
  return out;
}

async function main() {
  await rm(OUT, { recursive: true, force: true });
  await mkdir(path.join(OUT, 'emails'), { recursive: true });
  await mkdir(path.join(OUT, 'data'), { recursive: true });

  await cp(SITE, OUT, { recursive: true });

  console.log('Forge: building newsletters');
  const newsletters = await collect();

  await writeFile(
    path.join(OUT, 'data', 'newsletters.json'),
    JSON.stringify({ builtAt: new Date().toISOString(), newsletters }, null, 2),
  );

  console.log(`Forge: ${newsletters.length} newsletter(s) -> dist/`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
