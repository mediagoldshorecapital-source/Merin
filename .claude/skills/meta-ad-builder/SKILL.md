---
name: meta-ad-builder
description: Build a new Prime Ingredients creative-testing ad set (or rebuild an existing one) in Meta Ads from a Drive folder and Ad account media, following every approved rule — period copy from the Q4 calendar, URL parameters, enhancements, Add music on statics, verification and activation. Use when the user types /meta-ad-builder, says "new ad set ready", shares a Drive link for a new batch, or asks to create or rebuild Prime Ingredients ads.
---

# Prime Ingredients Meta ad builder

You build testing ad sets for Prime Ingredients. Work through the phases in order. The three approval gates (copy, plan, activation) are never skipped.

## 0. Hard rules

- **Only ad account `2009539369903270`.** Never read, query or change any other ad account the connector can see. If a request seems to need another account, stop and ask.
- **Read first:**
  - `CLAUDE.md` (core rules)
  - `meta-ads-playbook.md` (IDs, ad set settings, past batches, known blockers)
  - `campaign-calendar.md` in this folder (Q4 periods and copy rules)

  When they conflict, the newer dated rule wins. Tell the user about the conflict.
- **Every creative comes from `build_specs.py`** in this folder, fed an approved copy file. Never hand-write a creative spec. If a rule changes, edit the script, test it, then build.
- **Approvals don't carry over.** A "go ahead" covers one ad set and one step only.
- **"The API accepted it" is not proof.** The connector can't read back enhancements, music, URL parameters or WhatsApp. Never report those as on. Say they were sent, and ask the user to spot-check one ad in Ads Manager.
- **Stop means stop.** If the user says stop mid-build, stop right away. Then report exactly what exists.

## 1. Collect the inputs

Ask for anything missing, in one message:

```
Ad set: <number>          (letter = number − 82: A=83, B=84, C=85 … Z=108; ask beyond Z)
Creative date: <YYYYMMDD>
Start date: <DD-MM-YY> or "usual" (= 2 days after the previous ad set, 00:01 America/New_York)
Drive link: <folder with image and video subfolders>
Videos uploaded to Ad account media: yes / partly (which)
New ad set or rebuild of ad set <N>
```

## 2. Copy (approval gate 1)

1. Find the start date in `campaign-calendar.md` and see which period(s) are active.
2. **One period, copy file exists:** show the full copy (every primary text, headline and description) and ask the user to confirm or change it. Do this every time, even mid-period.
3. **One period, no copy file yet:** ask the user for the copy, or draft it from their brief for them to approve. Save it as `copy/<year>-q<n>-<period>.json` and add it to the calendar table.
4. **Two periods overlap:** the default is to split-test inside the 5 slots. Fill the 5 primary texts, 5 headlines and 5 descriptions with a mix of both occasions (for example 3 + 2, or 2 + 2 + 1 bridging both). Save them as one combined copy file (`copy/<year>-q<n>-<periodA>+<periodB>.json`) used on every ad. Show the proposed mix, slot by slot, and get the user's OK. Use a split by ad set, or by ad with two copy files, only if the user asks for it.
5. **Gap (no active period):** ask the user which copy to run.
6. Any change the user makes is saved to the copy file before building. `build_specs.py` rejects a flat "75% off" and more than 5 of any text type.

## 3. Inventory (read-only)

1. **Drive:** list the folder with `curl -s "https://drive.google.com/embeddedfolderview?id=<FOLDER_ID>"`. Do the same for each subfolder. Record each file name and Drive ID. **The ad count is whatever is in the folder:** every video and every image becomes one ad.
2. **Videos:**
   - Find each one in Ad account media with `ads_get_ad_videos` (`title` filter on the batch date or letter). Fetch `length` and `picture` with `video_ids`.
   - Download each Drive original (`drive.usercontent.google.com/download?id=<ID>&export=download`; large files need the `confirm=t&uuid=` step). Read its duration from the mp4 `mvhd` box.
   - **The lengths must match.** If they don't, the upload is mislabeled: don't build that ad, and tell the user.
   - A video that's in Drive but not in Ad account media is reported as missing. A person must upload it.
3. **Statics:**
   - Import each Drive image with `ads_create_creative`, using `image_url=https://lh3.googleusercontent.com/d/<DRIVE_ID>=s0`. Plain drive.google.com links are blocked.
   - Read the `image_hash` back with `ads_get_creatives`.
4. **Ad set:**
   - **New:** the skill creates it with `ads_create_ad_set`, copying the previous ad set's settings (playbook, "Ad set rules"): Testing campaign `120251599164970341`, Purchase on pixel `25563599826640611`, broad USA, Advantage+ audience and placements.
     - Name: `<N>__Broad_USA_Creative_testing – <DD-MM-YY>`.
     - Start: 00:01 ET. ET is −04:00 until Nov 1 and −05:00 from Nov 2, 2026.
     - Create it **off**.
     - Read it back and compare the settings with the previous ad set.
   - **Rebuild:** list the existing ads and record every old ad ID for deletion later.

## 4. Plan (approval gate 2)

Send a table:
- Ad name, media (video ID + length match, or image hash), copy file, and status.
- Flag anything missing, duplicated or mismatched.

Naming:
- Follow the file names without the extension: `<n><L>. <YYYYMMDD>_<Concept>_V<v>` for videos, `<n><L>. <YYYYMMDD>_Static_V (<k>)` for statics.
- Videos are numbered first, then statics after them.
- If the Drive names don't carry numbers, propose the numbering in the plan.

Wait for an OK.

## 5. Build (everything off)

For each ad:

```
python3 .claude/skills/meta-ad-builder/build_specs.py <copy.json> static "<ad name>" <image_hash>
python3 .claude/skills/meta-ad-builder/build_specs.py <copy.json> video  "<ad name>" <video_id> "<picture url>"
```

Pass the printed JSON as `creative` to `ads_create_ad`, with the ad set ID, the ad name and `hide_ui: true`. Ads are created paused. Run independent creates in parallel batches of about 5.

What the script guarantees, so don't remove any of it:
- **Copy:** from the approved copy file, put in both the main fields and `asset_feed_spec`. If only the headlines go in `asset_feed_spec`, Ads Manager shows empty text.
- **Link:** `https://tryprimeingredients.com/products/nmn`, Shop Now button, display link `Primeingredients.com`.
- **URL parameters** (`url_tags`).
- **Identity:** Page `1012373248616002`, Instagram `17841480103037701`.
- **Multi-advertiser ads ON.**
- **Enhancements:** Enhance CTA ON. Every creative-setup and Advantage+ feature OFF (site links, catalog/products, summaries and the rest). Never connect a catalog.
- **Add music:**
  - Statics: ON, which needs **both** `audio` OPT_IN **and** `asset_feed_spec.audios=[{"type":"random"}]`. The toggle alone leaves music off (found 2026-10-16).
  - Videos: OFF.
- `standard_enhancements` is never sent (the API rejects it).

## 6. Verify (before reporting)

- **Count:** the ad count matches the plan (plus any old ads still awaiting deletion on a rebuild).
- **Media:** run `ads_get_creatives` on every new creative.
  - Statics: `image_hash` matches the plan.
  - Videos: Meta re-hosts under a new ID, so compare the creative video's `length` with the plan.
- **Copy:** the title, description, link and CTA are right on every ad.
- **Report:** N built and checked, or list exactly what failed.
- **Spot-check:** ask the user to check one static and one video in Ads Manager for Music, Enhance CTA, URL parameters and creative setup off.

## 7. Activate / clean up (approval gate 3)

Only after the user approves:
- Turn on the new ads, then the ad set, with `ads_activate_entity`. The ad set's start time keeps it from delivering early.
- On a rebuild, delete the old ads with `ads_update_entity` `{"status":"DELETED"}`.
- Read back the final count and statuses. New ads show `PENDING_REVIEW` while Meta reviews them; say so.

## 8. Wrap up

- Remind the user to bulk-edit **WhatsApp → "Use Facebook Page"** on the new ads (the connector can't set it).
- Add a dated section to `meta-ads-playbook.md`: ad set ID, Drive folder, copy file used, video lengths, what was built, anything left open.
- Commit and push.
- Final report in plain words: what's live, what's in review, what's waiting on the user.

## Known blockers

- Videos can't be imported by URL. A person uploads them to **Media Library → Ad account media**.
- Business media folders and Ads Manager drafts aren't readable. A draft ad set must be published (off) first.
- `fbcdn.net` is blocked by the network policy, so images can't be compared pixel by pixel. Trust the import trace and the hash match.
- A creative can't be edited. To change copy or media, build a new ad, turn it on, then delete the old one.
