/**
 * Post-build check: assert dist/ is a complete, servable site.
 *
 * A build can exit 0 and still produce something broken — a page that
 * references a missing asset, or a newsletter whose email file never got
 * copied. This checks the output rather than the exit code.
 */
import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';

const OUT = path.join(process.cwd(), 'dist');
const errors = [];

async function present(rel, label) {
  try {
    const info = await stat(path.join(OUT, rel));
    if (!info.isFile()) {
      errors.push(`${label}: ${rel} is not a file`);
    } else if (info.size === 0) {
      errors.push(`${label}: ${rel} is empty`);
    }
  } catch {
    errors.push(`${label}: ${rel} is missing`);
  }
}

const REQUIRED = [
  'index.html',
  'preview.html',
  '404.html',
  'assets/forge.css',
  'assets/theme.js',
  'assets/index.js',
  'assets/preview.js',
  'data/newsletters.json',
  '_redirects',
  '_headers',
];

for (const rel of REQUIRED) await present(rel, 'site');

let data;
try {
  data = JSON.parse(await readFile(path.join(OUT, 'data', 'newsletters.json'), 'utf8'));
} catch (err) {
  console.error(`verify: could not read newsletters.json — ${err.message}`);
  process.exit(1);
}

const newsletters = data.newsletters ?? [];
for (const n of newsletters) {
  if (!n.id) errors.push('newsletter: entry with no id');
  if (!n.title) errors.push(`${n.id}: no title`);
  await present(n.file, n.id);
}

// Every local asset the pages reference must actually exist in dist/.
for (const page of ['index.html', 'preview.html']) {
  let html;
  try {
    html = await readFile(path.join(OUT, page), 'utf8');
  } catch {
    continue; // already reported as missing above
  }
  const refs = [...html.matchAll(/(?:src|href)\s*=\s*"([^"]+)"/g)]
    .map((m) => m[1].split(/[?#]/)[0])
    .filter((r) => r && !/^(https?:|data:|mailto:)/.test(r))
    .filter((r) => !r.endsWith('/'))      // directory links resolve to index.html
    .filter((r) => !r.endsWith('.html')); // page-to-page links
  for (const ref of new Set(refs)) await present(ref, page);
}

if (errors.length) {
  console.error('verify: FAILED\n' + errors.map((e) => `  - ${e}`).join('\n'));
  process.exit(1);
}

console.log(`verify: OK — ${newsletters.length} newsletter(s), ${REQUIRED.length} required file(s) present`);
