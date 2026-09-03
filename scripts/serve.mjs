/** Zero-dependency static server for local previewing of dist/. */
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';

const OUT = path.join(process.cwd(), 'dist');
const PORT = Number(process.env.PORT) || 4173;

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.webp': 'image/webp',
  '.ico': 'image/x-icon',
};

createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host}`);
  let rel = decodeURIComponent(url.pathname);
  if (rel.endsWith('/')) rel += 'index.html';

  // Keep requests inside dist/.
  const file = path.join(OUT, path.normalize(rel).replace(/^(\.\.[/\\])+/, ''));
  if (!file.startsWith(OUT)) {
    res.writeHead(403).end('Forbidden');
    return;
  }

  try {
    const info = await stat(file);
    const target = info.isDirectory() ? path.join(file, 'index.html') : file;
    const body = await readFile(target);
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(target)] ?? 'application/octet-stream' });
    res.end(body);
  } catch {
    try {
      const body = await readFile(path.join(OUT, '404.html'));
      res.writeHead(404, { 'Content-Type': TYPES['.html'] });
      res.end(body);
    } catch {
      res.writeHead(404).end('Not found');
    }
  }
}).listen(PORT, () => {
  console.log(`Forge dev server -> http://localhost:${PORT}`);
});
