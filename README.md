# Forge

A static newsletter studio for **Prime Ingredients**. Every email under
`newsletters/` is rendered here exactly as it will land in the inbox, alongside a
preflight check of the source — message size, links, images, unsubscribe — so
nothing ships broken.

Built as a plain static site with **no runtime dependencies**: the build is a
single Node script, and the output in `dist/` is HTML, CSS and JS.

## Local development

```bash
npm run build     # scan newsletters/ -> dist/
npm run dev       # build, then serve dist/ at http://localhost:4173
```

There is nothing to `npm install` — `package.json` has no dependencies.

## Deploying to Netlify

`netlify.toml` already carries the full configuration, so Netlify needs no
manual build settings:

| Setting | Value |
| --- | --- |
| Build command | `npm run build` |
| Publish directory | `dist` |
| Node version | 20 |

**From the Netlify UI:** *Add new site → Import an existing project*, pick this
repository and the branch you want to deploy. Netlify reads `netlify.toml` and
fills the build settings in automatically — accept them and deploy.

**From the CLI:**

```bash
npx netlify-cli deploy --build          # draft deploy, gives a preview URL
npx netlify-cli deploy --build --prod   # promote to production
```

Deploys are fully static: no environment variables, no secrets, no serverless
functions. If that changes later, add functions under `netlify/functions/` and
Netlify will pick them up without further configuration.

## Adding a newsletter

Create a folder under `newsletters/` containing an `email.html`. The next build
picks it up automatically — the folder name becomes the URL id.

```
newsletters/
  my-campaign/
    email.html     # required — the email source
    meta.json      # optional — campaign metadata (see below)
    README.md      # optional — fallback metadata source
```

`meta.json` is the reliable way to supply metadata:

```json
{
  "title": "Campaign name",
  "summary": "One-line description.",
  "brand": "Prime Ingredients",
  "status": "draft",
  "date": "2026-09-02",
  "subject": "Subject line as it appears in the inbox",
  "previewText": "Preheader text shown after the subject.",
  "links": [{ "label": "Klaviyo — campaign", "url": "https://…" }],
  "checklist": ["Things to confirm before sending."]
}
```

Without a `meta.json` the build falls back to parsing `README.md` for the title,
subject, preview text, Canva/Klaviyo links and the "Before sending" checklist,
so existing newsletters work unchanged.

## What preflight checks

| Check | Why it matters |
| --- | --- |
| Message size | Gmail clips anything over 102 KB, hiding the footer and unsubscribe link |
| Unsubscribe link | Required by CAN-SPAM and GDPR before a campaign can send |
| Images without `alt` | Most clients block images by default; missing alt text renders blank |
| Unique outbound links | Every destination is listed so it can be checked before sending |

Subject line and preview text are also measured against the points where inbox
clients typically truncate them (60 and 140 characters).

## Layout

```
site/            static source — copied verbatim into dist/
  index.html     newsletter gallery
  preview.html   single-newsletter preview + preflight
  assets/        stylesheet and page scripts
scripts/
  build.mjs      scans newsletters/, writes dist/
  serve.mjs      dependency-free local static server
netlify.toml     build settings, redirects, headers
```
