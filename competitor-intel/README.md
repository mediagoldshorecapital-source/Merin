# Competitor Intel — Meta Ad Library

Structured teardown of our direct competitors' Meta ads, built from an Ad Library export.

**Start here:** [`static-creative-playbook.md`](static-creative-playbook.md) — the full report:
what their static creatives have in common, the frameworks underneath them, and the build plan
for our own batch.

## What's in the current dataset

| | |
|---|---|
| Source | `Competitor_meta_ads_library.docx` (Ad Library export, captured 18 Aug 2026) |
| Unique ads | 736 (375 static / 361 video) |
| Core advertisers | Timeline (Mitopure), Renue By Science, Omre, NOVOS, Elysium Health, Wonderfeel, Tru Niagen, ProHealth Longevity, Double Wood Supplements |
| Creative images extracted | 363 |
| Fields per ad | advertiser, first-seen date, days running, media type, primary text, headline, description, CTA, destination domain, page likes, creative image |

The export carries no spend or impression data, so **days running is the performance proxy**
throughout: nobody keeps paying to serve a static for 100+ days that isn't returning.

## Refreshing it

```bash
# parse a new export into rows + pull out every creative image
python scripts/parse_ad_library_export.py export.docx data/competitor_ads.csv \
       --media-dir data/creatives --json data/competitor_ads.json

# regenerate every statistic quoted in the playbook
python scripts/analyse_creative_patterns.py data/competitor_ads.csv > data/summary_stats.txt

# contact sheets of each brand's longest-running statics, for visual review
python scripts/build_contact_sheets.py data/competitor_ads.json data/creatives sheets/
```

Requires Python 3 and, for contact sheets only, Pillow (`pip install pillow`).

Creative images and contact sheets are intentionally not committed — they are competitor
artwork and they are large. Regenerate them from an export when needed.

## Layout

```
competitor-intel/
├── static-creative-playbook.md      the report
├── data/
│   ├── competitor_ads.csv           736 ads × 15 fields
│   └── summary_stats.txt            machine-generated statistics
└── scripts/
    ├── parse_ad_library_export.py   .docx  → CSV/JSON + images
    ├── analyse_creative_patterns.py CSV    → statistics
    └── build_contact_sheets.py      JSON   → labelled contact sheets
```
