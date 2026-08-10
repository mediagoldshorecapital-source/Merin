# -*- coding: utf-8 -*-
import sys, html, os
from collections import Counter, OrderedDict
sys.path.insert(0, '/tmp/claude-0/-home-user-Merin/66489eb8-aec6-586f-abae-afced68687e0/scratchpad')
from matrix_data import ROWS

E = lambda s: html.escape(str(s))
TIER_CLASS = {"Proven": "proven", "Adjacent": "adjacent", "Untested": "untested"}

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
h3{font-size:1.1rem;line-height:1.3}
p{margin:0}
.eyebrow{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-3)}
header.masthead{padding:64px 0 0;display:flex;flex-direction:column;gap:22px}
.masthead .lede{font-size:1.2rem;line-height:1.55;color:var(--ink-2);max-width:62ch}
.meta-row{display:flex;flex-wrap:wrap;gap:8px 28px;padding-top:20px;border-top:1px solid var(--rule);
font-family:ui-monospace,Menlo,monospace;font-size:.76rem;color:var(--ink-3)}
.meta-row b{color:var(--ink-2);font-weight:600}
section{display:flex;flex-direction:column;gap:22px}
.sec-head{display:flex;flex-direction:column;gap:10px}
.sec-head p{color:var(--ink-2);max-width:68ch}
.callout{background:var(--surface-2);border:1px solid var(--rule);border-radius:3px;padding:18px 22px;font-size:.93rem;color:var(--ink-2);max-width:78ch}
.callout b{color:var(--ink)}
.callout.warn{background:var(--warn-soft);border-color:var(--warn)}
.rules{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:1px;background:var(--rule);border:1px solid var(--rule);border-radius:3px;overflow:hidden;counter-reset:rl}
.rules li{counter-increment:rl;background:var(--surface);padding:16px 22px 16px 56px;position:relative;font-size:.93rem;color:var(--ink-2)}
.rules li::before{content:counter(rl);position:absolute;left:22px;top:16px;font-family:ui-monospace,Menlo,monospace;font-size:.8rem;color:var(--accent);font-weight:600}
.rules b{color:var(--ink)}
.t-scroll{overflow-x:auto;border:1px solid var(--rule);border-radius:3px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:.84rem;min-width:760px}
caption{caption-side:top;text-align:left;padding:16px 20px 12px;font-size:.82rem;color:var(--ink-3);border-bottom:1px solid var(--rule-soft)}
th,td{padding:9px 14px;text-align:left;border-bottom:1px solid var(--rule-soft);vertical-align:top}
thead th{font-size:.7rem;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--ink-3);background:var(--surface-2);white-space:nowrap}
tbody td{color:var(--ink-2)}
tbody tr:last-child td{border-bottom:none}
td.num{font-variant-numeric:tabular-nums;color:var(--ink-3);font-family:ui-monospace,Menlo,monospace;font-size:.78rem}
.chip{display:inline-block;font-family:ui-monospace,Menlo,monospace;font-size:.62rem;letter-spacing:.09em;text-transform:uppercase;padding:2px 7px;border-radius:2px;white-space:nowrap}
.chip.proven{background:var(--good-soft);color:var(--good)}
.chip.adjacent{background:var(--warn-soft);color:var(--warn)}
.chip.untested{background:var(--neg-soft);color:var(--neg)}
.chip.robert{background:var(--accent-soft);color:var(--accent)}
.chip.plain{background:var(--surface-2);color:var(--ink-3);border:1px solid var(--rule-soft)}
.cards{display:flex;flex-direction:column;gap:16px}
.pcard{background:var(--surface);border:1px solid var(--rule);border-left:3px solid var(--rule);border-radius:3px;padding:24px 26px;display:flex;flex-direction:column;gap:16px;box-shadow:var(--shadow)}
.pcard.proven{border-left-color:var(--good)}
.pcard.adjacent{border-left-color:var(--warn)}
.pcard.untested{border-left-color:var(--neg)}
.pc-top{display:flex;flex-direction:column;gap:9px}
.pc-num{font-family:ui-monospace,Menlo,monospace;font-size:.72rem;color:var(--ink-3)}
.pc-chips{display:flex;flex-wrap:wrap;gap:6px}
.pc-pain{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}
.pc-pain>div{background:var(--surface-2);border-radius:2px;padding:12px 14px}
.lbl{font-family:ui-monospace,Menlo,monospace;font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);display:block;margin-bottom:5px}
.pc-pain p{font-size:.87rem;color:var(--ink-2)}
.hookbox{border-left:2px solid var(--accent);background:var(--accent-soft);padding:14px 16px;border-radius:2px;display:flex;flex-direction:column;gap:8px}
.hookbox .hk{font-size:1.02rem;font-weight:600;color:var(--ink)}
.hookbox .hd{font-family:"Iowan Old Style",Palatino,Georgia,serif;font-size:1.05rem;color:var(--ink)}
.hookbox .sh{font-size:.9rem;color:var(--ink-2)}
.pc-body{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
.pc-body>div{display:flex;flex-direction:column;gap:5px}
.pc-body p{font-size:.88rem;color:var(--ink-2)}
.pc-idea{background:var(--surface-2);border-radius:2px;padding:13px 15px}
.pc-idea p{font-size:.89rem;color:var(--ink-2)}
footer{border-top:1px solid var(--rule);padding-top:22px;font-size:.82rem;color:var(--ink-3);max-width:78ch}
a{color:var(--accent)}
a:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

tiers = Counter(r["tier"] for r in ROWS)
personas = Counter(r["persona"] for r in ROWS)

# index table
idx = []
for r in ROWS:
    idx.append(f"""<tr>
<td class="num">{r['n']}</td>
<td>{E(r['pain'])}</td>
<td>{E(r['cat'])}</td>
<td><span class="chip {TIER_CLASS[r['tier']]}">{E(r['tier'])}</span></td>
<td>{E(r['funnel'])}</td>
<td>{E(r['fmt'])}</td>
<td>{E(r['hook'])}</td>
</tr>""")

# grouped cards
groups = OrderedDict()
for r in ROWS:
    key = "Robert — the male buyer" if r["persona"] == "Robert" else r["cat"]
    groups.setdefault(key, []).append(r)

card_sections = []
for gname, rows in groups.items():
    cards = []
    for r in rows:
        rob = '<span class="chip robert">Robert</span>' if r["persona"] == "Robert" else ""
        cards.append(f"""<article class="pcard {TIER_CLASS[r['tier']]}">
<div class="pc-top">
  <span class="pc-num">Pain point {r['n']:02d}</span>
  <h3>{E(r['pain'])}</h3>
  <div class="pc-chips">{rob}<span class="chip {TIER_CLASS[r['tier']]}">{E(r['tier'])}</span>
  <span class="chip plain">{E(r['funnel'])}</span><span class="chip plain">{E(r['fmt'])}</span></div>
</div>
<div class="pc-pain">
  <div><span class="lbl">Surface pain — what she says</span><p>{E(r['surface'])}</p></div>
  <div><span class="lbl">Deep pain — what she means</span><p>{E(r['deep'])}</p></div>
  <div><span class="lbl">Evidence anchor</span><p>{E(r['evidence'])}</p></div>
</div>
<div class="hookbox">
  <span class="lbl">Qualifying hook</span>
  <span class="hk">{E(r['hook'])}</span>
  <span class="hd">{E(r['heading'])}</span>
  <span class="sh">{E(r['subheading'])}</span>
</div>
<div class="pc-idea"><span class="lbl">Angle — {E(r['angle'])}</span><p>{E(r['idea'])}</p></div>
<div class="pc-body">
  <div><span class="lbl">Creative description — poster</span><p>{E(r['poster'])}</p></div>
  <div><span class="lbl">Video description — reel</span><p>{E(r['reel'])}</p></div>
</div>
</article>""")
    card_sections.append(f"""<section>
<div class="sec-head"><span class="eyebrow">{E(gname)} · {len(rows)} pain points</span></div>
<div class="cards">{''.join(cards)}</div>
</section>""")

HTML = f"""<title>NMN — Pain Point &amp; Creative Brief Matrix</title>
<style>{CSS}</style>
<div class="wrap">

<header class="masthead">
  <span class="eyebrow">Creative production brief · Prime Ingredients · NMN Complex</span>
  <h1>Thirty pain points, thirty ads, one rule: qualify her, don’t just catch her.</h1>
  <p class="lede">Every pain point below comes from the NMN customer intelligence research. Every hook, heading and treatment is written in the structure that actually converts in your Meta account — measured across 1,220 ads and $381K of spend. A designer should be able to build the poster, and an editor cut the reel, from a single entry without asking a follow-up question.</p>
  <div class="meta-row">
    <span><b>Pain points</b> {len(ROWS)}</span>
    <span><b>Linda</b> {personas['Linda']} · <b>Robert</b> {personas['Robert']}</span>
    <span><b>Proven</b> {tiers['Proven']} · <b>Adjacent</b> {tiers['Adjacent']} · <b>Untested</b> {tiers['Untested']}</span>
    <span><b>Built</b> 10 Aug 2026</span>
  </div>
</header>

<div class="callout warn">
  <b>The one rule that governs all thirty.</b> In this account, hook rate, hold rate and click-through rate all correlate <em>negatively</em> with return — in all seven months measured. Losing ads buy 36% more clicks and convert them 39% worse. So every hook here is written to <b>disqualify</b>: to give a non-buyer a reason to scroll past. That is why several of them look narrower, plainer and less “scroll-stopping” than a normal brief. That is deliberate, and it is the difference between $31.90 and $58.09 cost per acquisition.
</div>

<section>
  <div class="sec-head"><span class="eyebrow">Non-negotiables</span><h2>Rules every asset must follow</h2>
  <p>Derived from the six-month creative teardown, not from preference.</p></div>
  <ol class="rules">
    <li><b>Hooks qualify, they do not attract.</b> If a line would appeal to someone who has never felt this pain, rewrite it.</li>
    <li><b>Committed verbs only</b> — <em>plummeting, collapsing, rebuild</em>. Never <em>naturally declines, helps support, may assist</em>. This is the 0.92-vs-1.41 ROAS difference and the single most important rule here.</li>
    <li><b>Never put “75% OFF” in a headline.</b> It lost on conversions-per-click in five months out of five. Lead with the per-bottle anchor: $29.98 → $16.66.</li>
    <li><b>Talent must read 58–68.</b> She compares herself to her peer group; a 45-year-old model breaks the mirror.</li>
    <li><b>Reels: 20 seconds, hook inside 3, captions burned in.</b> She watches in a recliner with the TV on and the sound off.</li>
    <li><b>Plain beats polished.</b> In this account the winners look homemade and the losers look like adverts.</li>
    <li><b>Judge on conversions per click</b>, not hook rate or CTR. ≥4.0% scale · 3.0–4.0% hold · &lt;2.8% kill, after ~40 clicks (≈$60). Read it from Meta — the Triple Whale checkout event fires on only ~63% of purchases.</li>
  </ol>
</section>

<section>
  <div class="sec-head"><span class="eyebrow">Index</span><h2>All thirty at a glance</h2>
  <p>Evidence tier tells you how much budget a concept has earned. <b>Proven</b> has winning ads behind it, <b>adjacent</b> is a variant of a winner, <b>untested</b> is new — do not launch twelve untested concepts at once.</p></div>
  <div class="t-scroll"><table>
    <caption>Pain point index · sorted by category</caption>
    <thead><tr><th>#</th><th>Pain point</th><th>Category</th><th>Tier</th><th>Funnel</th><th>Format</th><th>Qualifying hook</th></tr></thead>
    <tbody>{''.join(idx)}</tbody>
  </table></div>
</section>

{''.join(card_sections)}

<section>
  <div class="sec-head"><span class="eyebrow">Operations</span><h2>Naming, flags and where to start</h2></div>
  <div class="callout">
    <b>Naming convention.</b> <code>NMN_[PainPoint#]_[Angle]_[Format]_[Variant]_[YYYYMM]</code> — for example <code>NMN_16_QualityContrast_DemoCOA_A_202608</code>. Three separate rows currently exist for what looks like one ad (<code>- Video - Ad -2</code>, <code>- Video - Ad - 2</code>, <code>Video - Ad - 2</code>), which quietly fragments every angle-level report. Adopt this scheme so new assets are analysable on arrival.
  </div>
  <div class="callout warn">
    <b>Flags before anything ships.</b> Pain point 14 (weight) must not carry a weight-loss claim and needs legal review. Pain point 23 claims self-serve cancellation — verify that is true before running it, particularly as 97% of orders are now subscriptions. Pain point 15 is blocked until Multi Collagen COGS is populated, since its margin is currently unknown.
  </div>
  <div class="callout">
    <b>If you brief only three this month, brief these.</b> <b>16</b> — the quality-contrast angle is your best-performing structure by CPM and has never once run on NMN, which is 94% of revenue. <b>9</b> — “slept eight hours, woke up like it was four” is the most self-identifying line in the entire research and should be your highest-volume angle. <b>26</b> — Robert is reported at 1.81 ROAS, the only segment above your ~1.70 breakeven, and has no creative written to him at all.
  </div>
</section>

<footer>
Pain points drawn from the NMN Deep Customer Intelligence Report (Prime Ingredients, 20 May 2026). Copy structures, evidence tiers and the qualification rule are drawn from a six-month teardown of 1,220 Meta ads and $381,106 of spend, read from the Triple Whale warehouse on 10 August 2026. Ad performance figures behind the tiers are Meta channel-reported and are valid for ranking creative against creative rather than as absolute profit measures, since Triple Whale pixel attribution does not exist before June 2026. Robert’s 1.81 ROAS is carried from the research document and is not independently verifiable in the warehouse — confirm in Ads Manager before scaling against it. All copy here is a production brief, not legally reviewed final copy; supplement claims are the advertiser’s responsibility.
</footer>

</div>"""

out = "/home/user/Merin/analysis/nmn-pain-point-matrix/report.html"
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w").write(HTML)
print("wrote", out, len(HTML), "chars")
