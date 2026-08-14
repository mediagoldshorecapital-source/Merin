# -*- coding: utf-8 -*-
import sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from icp_data import ICPS, QUOTES, EMOTIONS, FLAG_LABELS, FINDINGS, HARVEST

E = lambda s: html.escape(str(s))
counts = {e: sum(1 for q in QUOTES if q["emotion"] == e) for e in EMOTIONS}
ready = [q for q in QUOTES if len(q["flags"]) >= 3]

CSS = """
:root{--ground:#EDF1F3;--surface:#FCFCFB;--surface-2:#F4F7F8;--ink:#111A1F;--ink-2:#4E5F68;--ink-3:#74858E;
--rule:#D2DBDF;--rule-soft:#E3EAED;--accent:#00819C;--accent-soft:#D7EDF2;--neg:#C03A1E;--neg-soft:#F7E0DA;
--warn:#8A5A0B;--warn-soft:#F6EBD6;--good:#1B6547;--good-soft:#DCEDE4;
--shadow:0 1px 2px rgba(17,26,31,.06),0 8px 24px -16px rgba(17,26,31,.28);}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ground:#0D1418;--surface:#151E23;--surface-2:#1B262C;
--ink:#E2E9EC;--ink-2:#9DAEB7;--ink-3:#7A8B94;--rule:#28343A;--rule-soft:#202B31;--accent:#2FA6AE;--accent-soft:#10333A;
--neg:#D9604A;--neg-soft:#3A211C;--warn:#D2A24A;--warn-soft:#332916;--good:#58BF8D;--good-soft:#12301F;
--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -16px rgba(0,0,0,.8);}}
:root[data-theme="dark"]{--ground:#0D1418;--surface:#151E23;--surface-2:#1B262C;--ink:#E2E9EC;--ink-2:#9DAEB7;
--ink-3:#7A8B94;--rule:#28343A;--rule-soft:#202B31;--accent:#2FA6AE;--accent-soft:#10333A;--neg:#D9604A;
--neg-soft:#3A211C;--warn:#D2A24A;--warn-soft:#332916;--good:#58BF8D;--good-soft:#12301F;
--shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -16px rgba(0,0,0,.8);}
*{box-sizing:border-box}
body{background:var(--ground);color:var(--ink);font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
font-size:16px;line-height:1.6;margin:0;padding:0 20px 96px;-webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;display:flex;flex-direction:column;gap:56px}
h1,h2,h3,h4{font-family:"Iowan Old Style","Palatino Linotype","Book Antiqua",Palatino,Georgia,serif;font-weight:600;text-wrap:balance;margin:0;letter-spacing:-.01em}
h1{font-size:clamp(2rem,4.6vw,3.1rem);line-height:1.08}
h2{font-size:clamp(1.5rem,2.8vw,2rem);line-height:1.15}
h3{font-size:1.14rem;line-height:1.3}
h4{font-size:.98rem;line-height:1.35}
p{margin:0}
.eyebrow{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-3)}
header.masthead{padding:64px 0 0;display:flex;flex-direction:column;gap:22px}
.masthead .lede{font-size:1.2rem;line-height:1.55;color:var(--ink-2);max-width:62ch}
.meta-row{display:flex;flex-wrap:wrap;gap:8px 28px;padding-top:20px;border-top:1px solid var(--rule);
font-family:ui-monospace,Menlo,monospace;font-size:.76rem;color:var(--ink-3)}
.meta-row b{color:var(--ink-2);font-weight:600}
section{display:flex;flex-direction:column;gap:22px}
.sec-head{display:flex;flex-direction:column;gap:10px}
.sec-head p{color:var(--ink-2);max-width:70ch}
.callout{background:var(--surface-2);border:1px solid var(--rule);border-radius:3px;padding:18px 22px;font-size:.93rem;color:var(--ink-2);max-width:78ch}
.callout b{color:var(--ink)}
.callout.warn{background:var(--warn-soft);border-color:var(--warn)}
.callout.bad{background:var(--neg-soft);border-color:var(--neg)}
.callout.good{background:var(--good-soft);border-color:var(--good)}
.key{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:1px;background:var(--rule);border:1px solid var(--rule);border-radius:3px;overflow:hidden}
.key>div{background:var(--surface);padding:14px 16px;display:flex;flex-direction:column;gap:4px}
.key .k{font-family:ui-monospace,Menlo,monospace;font-size:.78rem;font-weight:700;color:var(--accent)}
.key .v{font-size:.84rem;color:var(--ink-2)}
.finding{background:var(--surface);border:1px solid var(--rule);border-left:3px solid var(--rule);border-radius:3px;padding:24px 26px;display:flex;flex-direction:column;gap:14px;box-shadow:var(--shadow)}
.finding.critical{border-left-color:var(--neg)}
.finding.high{border-left-color:var(--warn)}
.finding.medium{border-left-color:var(--accent)}
.chip{display:inline-block;font-family:ui-monospace,Menlo,monospace;font-size:.62rem;letter-spacing:.09em;text-transform:uppercase;padding:2px 7px;border-radius:2px;white-space:nowrap}
.chip.critical{background:var(--neg-soft);color:var(--neg)}
.chip.high{background:var(--warn-soft);color:var(--warn)}
.chip.medium{background:var(--accent-soft);color:var(--accent)}
.chip.plain{background:var(--surface-2);color:var(--ink-3);border:1px solid var(--rule-soft)}
.chip.good{background:var(--good-soft);color:var(--good)}
.finding p{font-size:.94rem;color:var(--ink-2);max-width:76ch}
.vox{display:flex;flex-direction:column;gap:8px;margin:0;padding:0}
.vox blockquote{margin:0;padding:11px 15px;background:var(--surface-2);border-left:2px solid var(--neg);border-radius:2px;
font-size:.9rem;color:var(--ink);font-style:italic}
.act{font-size:.9rem;color:var(--ink-2);border-top:1px dotted var(--rule);padding-top:11px}
.act b{color:var(--ink)}
.icp{background:var(--surface);border:1px solid var(--rule);border-top:3px solid var(--rule);border-radius:3px;padding:26px 28px;display:flex;flex-direction:column;gap:18px;box-shadow:var(--shadow)}
.icp.accent{border-top-color:var(--accent)} .icp.good{border-top-color:var(--good)}
.icp.warn{border-top-color:var(--warn)} .icp.neg{border-top-color:var(--neg)}
.icp-top{display:flex;flex-direction:column;gap:8px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:1px;background:var(--rule);border:1px solid var(--rule);border-radius:3px;overflow:hidden}
.stats>div{background:var(--surface-2);padding:11px 13px;display:flex;flex-direction:column;gap:3px}
.stats .sl{font-size:.7rem;color:var(--ink-3)}
.stats .sv{font-family:ui-monospace,Menlo,monospace;font-size:1rem;font-weight:600;color:var(--ink);font-variant-numeric:tabular-nums}
.parts{display:flex;flex-direction:column;gap:1px;background:var(--rule-soft);border:1px solid var(--rule-soft);border-radius:3px;overflow:hidden}
.part{background:var(--surface);padding:14px 18px;display:grid;grid-template-columns:210px 1fr;gap:18px}
.part .pn{font-family:ui-monospace,Menlo,monospace;font-size:.74rem;color:var(--accent);font-weight:600;padding-top:2px}
.part p{font-size:.9rem;color:var(--ink-2)}
@media (max-width:700px){.part{grid-template-columns:1fr;gap:6px}}
.t-scroll{overflow-x:auto;border:1px solid var(--rule);border-radius:3px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:.85rem;min-width:640px}
caption{caption-side:top;text-align:left;padding:16px 20px 12px;font-size:.82rem;color:var(--ink-3);border-bottom:1px solid var(--rule-soft)}
th,td{padding:10px 15px;text-align:left;border-bottom:1px solid var(--rule-soft);vertical-align:top}
thead th{font-size:.7rem;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--ink-3);background:var(--surface-2);white-space:nowrap}
tbody td{color:var(--ink-2)}
tbody tr:last-child td{border-bottom:none}
td.num{font-variant-numeric:tabular-nums;text-align:right;font-family:ui-monospace,Menlo,monospace}
tr.empty td{background:var(--neg-soft)}
tr.empty td:first-child{color:var(--neg);font-weight:600}
.qgrid{display:flex;flex-direction:column;gap:10px}
.qcard{background:var(--surface);border:1px solid var(--rule);border-radius:3px;padding:16px 20px;display:flex;flex-direction:column;gap:9px}
.qcard blockquote{margin:0;font-size:1rem;color:var(--ink);font-style:italic;line-height:1.45}
.qmeta{display:flex;flex-wrap:wrap;gap:6px}
footer{border-top:1px solid var(--rule);padding-top:22px;font-size:.82rem;color:var(--ink-3);max-width:78ch}
a{color:var(--accent)}
a:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

find_html = "".join(f"""<article class="finding {f['sev']}">
<div><span class="chip {f['sev']}">{E(f['sev'])}</span></div>
<h3>{E(f['title'])}</h3>
<p>{E(f['body'])}</p>
<div class="vox">{''.join(f'<blockquote>&ldquo;{E(x)}&rdquo;</blockquote>' for x in f['quotes'])}</div>
<p class="act"><b>Do this:</b> {E(f['action'])}</p>
</article>""" for f in FINDINGS)

icp_html = ""
for icp in ICPS:
    stats = "".join(f'<div><span class="sl">{E(l)}</span><span class="sv">{E(v)}</span></div>' for l, v in icp["headline_stats"])
    parts = "".join(f'<div class="part"><span class="pn">{E(k)}</span><p>{E(v)}</p></div>' for k, v in icp["parts"].items())
    icp_html += f"""<article class="icp {icp['colour']}">
<div class="icp-top">
  <span class="eyebrow">{E(icp['size'])} · evidence: {E(icp['evidence'])}</span>
  <h3>{E(icp['name'])}</h3>
  <p style="color:var(--ink-2);font-size:1.02rem">{E(icp['tagline'])}</p>
</div>
<div class="stats">{stats}</div>
<div class="parts">{parts}</div>
</article>"""

emo_rows = "".join(
    f'<tr class="{"empty" if counts[e] < 5 else ""}"><td>{E(e)}</td><td class="num">{counts[e]}</td>'
    f'<td>{"NO DATA — nothing in the corpus. Harvest required." if counts[e]==0 else ("Thin — harvest required." if counts[e]<5 else "Well covered.")}</td></tr>'
    for e in EMOTIONS)

ready_html = "".join(f"""<div class="qcard">
<blockquote>&ldquo;{E(q['text'])}&rdquo;</blockquote>
<div class="qmeta"><span class="chip plain">{E(q['emotion'])}</span><span class="chip plain">{E(q['kind'])}</span>
<span class="chip plain">{E(q['icp'])}</span><span class="chip good">{len(q['flags'])} flags</span>
<span class="chip plain">{E(q['dt'])}</span></div>
<p style="font-size:.86rem;color:var(--ink-3)"><b>Job:</b> {E(q['jtbd'])} &nbsp;·&nbsp; <b>Trigger:</b> {E(q['trigger'])}</p>
</div>""" for q in sorted(ready, key=lambda x: -len(x["flags"])))

harvest_rows = "".join(f"<tr><td class='num'>{h['rank']}</td><td><b>{E(h['source'])}</b></td><td>{E(h['est'])}</td>"
                       f"<td>{E(h['why'])}</td><td>{E(h['effort'])}</td></tr>" for h in HARVEST)

HTML = f"""<title>Prime Ingredients — Four-ICP Dossier</title>
<style>{CSS}</style>
<div class="wrap">

<header class="masthead">
  <span class="eyebrow">Customer intelligence · Prime Ingredients · NMN</span>
  <h1>Your customers are talking. Most of what they&rsquo;re saying isn&rsquo;t about aging.</h1>
  <p class="lede">Four buyer profiles, all twelve parts, every claim marked by how well it is evidenced &mdash; plus {len(QUOTES)} verbatim quotes pulled from your own ad comments. The quote bank was the point of this exercise, and it turned up something bigger: the loudest, most repeated things your customers say in public are about delivery, subscriptions and a bottle that doesn&rsquo;t match the one in your ads.</p>
  <div class="meta-row">
    <span><b>ICPs</b> 4</span>
    <span><b>Verbatim quotes</b> {len(QUOTES)}</span>
    <span><b>Copy-ready</b> {len(ready)}</span>
    <span><b>Corpus</b> 468 comments · 304 people · Feb&ndash;Aug 2026</span>
  </div>
</header>

<div class="callout bad">
  <b>Read this before the personas.</b> You asked for a bank of the customer&rsquo;s own words so copy becomes transcription rather than invention. The ICP research contains <b>zero verbatim quotes</b> &mdash; every line in it is the researcher&rsquo;s inference. So I went looking for real language: <code>reviews_table</code> returns 0 rows, <code>post_purchase_survey_table</code> 0, brand mentions 0. The one live source is <b>468 Meta ad comments</b>, and every quote in this document comes from there, unedited, traceable to a comment ID. Nothing below is paraphrased or invented.
</div>

<section>
  <div class="sec-head"><span class="eyebrow">01 &mdash; What they actually say</span>
  <h2>Seven things customers are reporting in public, right now</h2>
  <p>These sit above the personas because they are worth more. Three are severe enough that no amount of better creative compensates for them. They are customer allegations, not verified facts &mdash; but they are being made publicly, under live ads, where the next buyer reads them.</p></div>
  {find_html}
</section>

<section>
  <div class="sec-head"><span class="eyebrow">02 &mdash; Confidence key</span>
  <h2>How to read the four profiles</h2>
  <p>The four ICPs rest on very different evidence depths. Rather than smoothing that over, every claim is marked. A persona built mostly of [I] is a hypothesis wearing a name.</p></div>
  <div class="key">
    <div><span class="k">[M] Measured</span><span class="v">Triple Whale warehouse or the comment corpus. Trust these.</span></div>
    <div><span class="k">[R] Research</span><span class="v">The 20 May ICP report. Some is now out of date &mdash; timing especially.</span></div>
    <div><span class="k">[I] Inferred</span><span class="v">Reasoned, not observed. Treat as hypothesis.</span></div>
    <div><span class="k">[&mdash;] Not available</span><span class="v">No data exists. Named rather than guessed.</span></div>
  </div>
  <div class="callout warn">
    <b>The honest ranking.</b> <b>Margaret</b> is the best-evidenced of the four, because buying ASTA is an observable event &mdash; and she turns out to be your most valuable customer. <b>Robert</b> is well evidenced on spend, weaker on psychology. <b>Linda&ndash;Energy</b> is well evidenced demographically. <b>Linda&ndash;Clarity</b> is the weakest: it rests entirely on ManyChat self-selection, which is not in the warehouse, so it cannot be sized, costed or tied to revenue. It is a creative hypothesis, not a measured segment, and it is labelled that way throughout.
  </div>
</section>

<section>
  <div class="sec-head"><span class="eyebrow">03 &mdash; The four ICPs</span><h2>All twelve parts, per buyer</h2></div>
  {icp_html}
</section>

<section>
  <div class="sec-head"><span class="eyebrow">04 &mdash; The quote bank</span>
  <h2>What the corpus has, and what it is missing</h2>
  <p>{len(QUOTES)} verbatim quotes, each tagged on emotion, job-to-be-done, objection-or-benefit and trigger moment, plus six quality flags. A quote scoring three or more flags is marked copy-ready.</p></div>

  <div class="callout bad">
    <b>The corpus is 84% fear and anger.</b> That is the finding, not a limitation of the work. <b>Hope returns zero rows. Shame returns zero rows.</b> Relief, pride and grief are single digits. Your customers are currently generating objection language, not aspiration language &mdash; because the loudest experiences they are having are operational, not emotional. Those cells are left empty on purpose: an empty cell tells you where to go looking, an invented one tells you nothing.
  </div>

  <div class="t-scroll"><table>
    <caption>Emotion coverage across {len(QUOTES)} verbatim quotes</caption>
    <thead><tr><th>Emotion</th><th style="text-align:right">Quotes</th><th>Status</th></tr></thead>
    <tbody>{emo_rows}</tbody>
  </table></div>

  <div class="sec-head" style="padding-top:14px"><h3>The {len(ready)} copy-ready lines</h3>
  <p>Three or more quality flags &mdash; a specific time or place, a physical sensation, a comparison to a former self, an embarrassing admission, plain unbranded language, or under twelve words. These can go into an ad close to as written.</p></div>
  <div class="qgrid">{ready_html}</div>
  <div class="callout"><b>The full bank is in the spreadsheet</b>, filterable on every tag &mdash; all {len(QUOTES)} rows with comment IDs, dates, sentiment and the six flags as tick-columns.</div>
</section>

<section>
  <div class="sec-head"><span class="eyebrow">05 &mdash; Closing the gap</span>
  <h2>Where to get the words you don&rsquo;t have</h2>
  <p>Ranked by quotes per hour of effort. The first two are close to free and would roughly triple the bank.</p></div>
  <div class="t-scroll"><table>
    <caption>Harvest plan</caption>
    <thead><tr><th>#</th><th>Source</th><th>Volume</th><th>Why it matters</th><th>Effort</th></tr></thead>
    <tbody>{harvest_rows}</tbody>
  </table></div>
  <div class="callout good">
    <b>The quickest win in this whole document.</b> Your landing page cites <b>5,128 reviews</b>. The warehouse holds none of them, because the review platform was never connected. That is thousands of sentences of exactly the hope, relief and pride language this bank is missing, already written by your customers, sitting one integration away.
  </div>
</section>

<footer>
Personas synthesised from the NMN Deep Customer Intelligence Report (Prime Ingredients, 20 May 2026), cross-checked against the Triple Whale warehouse read on 10 August 2026. Segment sizing from <code>orders_table</code> for 1 Jan &ndash; 7 Aug 2026; Margaret is defined by observed ASTA purchase, Robert by first-name inference against a conservative male-name list, which makes 765 a floor rather than a count. Robert&rsquo;s 1.81 ROAS is carried from the research and is not verifiable in the warehouse &mdash; confirm in Ads Manager before moving budget against it. All {len(QUOTES)} quotes are verbatim from <code>social_media_comments_table</code> (468 comments, 304 unique users, 16 Feb &ndash; 13 Aug 2026), reproduced with the customer&rsquo;s own spelling and punctuation and traceable by comment ID. Commenters are not necessarily verified purchasers. The operational findings in section 01 are customer allegations reported in public; they require independent verification before being treated as fact.
</footer>

</div>"""

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report.html")
open(out, "w").write(HTML)
print("wrote", out, len(HTML), "chars")
print("findings:", len(FINDINGS), "| icps:", len(ICPS), "| quotes:", len(QUOTES), "| copy-ready:", len(ready))
