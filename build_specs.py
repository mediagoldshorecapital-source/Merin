"""Spec builder for Prime Ingredients ads (account 2009539369903270 only).

Encodes the CLAUDE.md core rules: approved copy, URL parameters, creative
setup/Advantage+ all off except Enhance CTA + multi-advertiser ads, and
Add music on statics only (audio OPT_IN *and* asset_feed_spec.audios -
the toggle alone leaves music off, confirmed 2026-10-16).

Usage: python3 build_specs.py static "<ad name>" <image_hash>
       python3 build_specs.py video  "<ad name>" <video_id> <thumbnail_url>
Prints the creative JSON to pass to ads_create_ad (drop the "name" key).
"""
import json
PT1="""Our Halloween Sale is here, and it's our thank-you to everyone in this community.

For the first time ever, our NMN is 75% off, and we are adding 3 bottles FREE, worth $591.
We've never offered this discount with 3 free bottles before. It's your biggest NMN saving ever.

✅ 1,000 mg of NMN per serving, with Resveratrol, CoQ10, TMG, Quercetin, Astaxanthin, Glutathione, Grape seed, Vitamin C.

✅ Third-party tested
✅ Made in the USA
✅ 30-day money-back guarantee
Supplies are limited, so don't wait on this one."""
PT2="""300+ clinical studies. 10 compounds targeting all 12 drivers of aging: NAD+, senescence, mitochondria, methylation, autophagy, gut-immune, and more.

From Prime Ingredients, trusted with 60,000+ ★★★★★ reviews.

🔬 Third-party lab tested.
30-day money-back guarantee."""
PT3="""𝗧𝗵𝗶𝘀 𝗶𝘀𝗻’𝘁 𝗷𝘂𝘀𝘁 𝗮 𝘀𝘂𝗽𝗽𝗹𝗲𝗺𝗲𝗻𝘁. It’s your membership to the world’s #1 Longevity Health Club. One Pill replaces 20+ pills and powders.

10 ingredients - 1,000 mg of NMN per serving, with Resveratrol, CoQ10, TMG, Quercetin, Astaxanthin, Glutathione, Grape seed, Vitamin C.

Sustainably sourced, third-party tested, NSF Certified, Clinician Choice and backed by science.

Join the movement and get your longevity back."""
PT4="""Ever feel like you hit a wall by 2 PM? 🥱☕📉 I used to rely on endless cups of coffee just to get through the day, but the crashes were brutal.

Then I learned about NAD+ and how our cells actually produce energy. ⚡ I started taking Prime Ingredients NMN Complex a few weeks ago, and the difference is wild. No jitters, just steady, clean energy from morning until night. Plus, I'm bouncing back from my workouts so much faster! 🏃‍♀️💨

If you're tired of feeling... well, tired all the time, you need to look into this. It's 1000mg NMN plus Resveratrol, CoQ10, TMG, Quercetin, Astaxanthin, Glutathione, Grape seed, Vitamin C, so your body actually uses it. 🧬✨

Check it out and see why everyone is obsessed! 👇"""
PT5="""Ever notice how some 55-year-olds have more energy than people half their age? 🤔 I used to think it was just genetics, until I learned what's actually happening inside their cells.

Turns out, NAD+ — the molecule your cells need for basically everything — drops by over 50% by the time you hit 40. 📉 Less NAD+, less energy, slower recovery, and yes, it shows on your skin too.

I started taking Prime Ingredients NMN Complex a few months ago. It's 1000mg NMN with liposomal absorption plus Resveratrol, CoQ10, TMG, Quercetin, Astaxanthin, Glutathione, Grape seed, Vitamin C, so your body can actually use it, not just pass it through. 🧬✨ My energy is steadier, my workouts recover faster, and honestly I just feel sharper.

If you're serious about aging on your terms, this is worth a look. 👇"""
PTS=[PT1,PT2,PT3,PT4,PT5]
H=["Halloween Sale - 75% off on NMN","One Capsule. All 12 Aging Pathways","One Pill. 10 Ingredients","Support Healthy Aging at the Cellular Level","Support Your Cellular Energy"]
D=["Free shipping. 30-Day Money-Back Guarantee.","1,000 mg of NMN + 10 compounds","1000mg NMN + 10 ingredients.","Support Healthy aging with 1000mg NMN + 10 ingredients"]
L="https://tryprimeingredients.com/products/nmn"
UT="utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&tw_source={{site_source_name}}&tw_adid={{ad.id}}"
PT1n=PT1.replace("our NMN is 75% off","our NMN is up to 75% off")
PTS=[PT1n,PT2,PT3,PT4,PT5]
H=["Support Cellular Energy Daily","Support Energy Without More Coffee","Halloween Sale - Up to 75% off on NMN","Support Your Cellular Energy","One Capsule. All 12 Anti-Aging Pathways"]
D=["Free shipping. 30-Day Money-Back Guarantee.","1,000 mg of NMN + 10 compounds","1000mg NMN + 10 ingredients.","Support Healthy aging with 1000mg NMN + 10 ingredients","Up to 75% OFF + 3 FREE Bottles. Limited Time only."]
OFF=["site_extensions","product_extensions","show_summary","local_store_extension","profile_card","image_touchups","text_optimizations","image_templates","adapt_to_placement","inline_comment","image_animation","add_text_overlay","description_automation","image_brightness_and_contrast","image_uncrop","video_auto_crop","media_type_automation","show_destination_blurbs","reveal_details_over_time","text_translation"]
def dof(static):
    f={"enhance_cta":{"enroll_status":"OPT_IN"},"audio":{"enroll_status":"OPT_IN" if static else "OPT_OUT"}}
    for k in OFF: f[k]={"enroll_status":"OPT_OUT"}
    return {"creative_features_spec":f}
def spec(name,story,static):
    return {"name":name,"url_tags":UT,"object_story_spec":{"page_id":"1012373248616002","instagram_user_id":"17841480103037701",**story},
      "asset_feed_spec":{"bodies":[{"text":t} for t in PTS],"titles":[{"text":t} for t in H],"descriptions":[{"text":t} for t in D],"optimization_type":"DEGREES_OF_FREEDOM"},
      "degrees_of_freedom_spec":dof(static),"contextual_multi_ads":{"enroll_status":"OPT_IN"}}
def static(name,h):
    s=spec(name,{"link_data":{"image_hash":h,"link":L,"message":PTS[0],"name":H[0],"description":D[0],"caption":"Primeingredients.com","call_to_action":{"type":"SHOP_NOW","value":{"link":L}}}},True)
    s["asset_feed_spec"]["audios"]=[{"type":"random"}]  # music asset: required or Add music stays off
    return s
def video(name,v,pic): return spec(name,{"video_data":{"video_id":v,"image_url":pic,"message":PTS[0],"title":H[0],"link_description":D[0],"call_to_action":{"type":"SHOP_NOW","value":{"link":L,"link_caption":"Primeingredients.com"}}}},False)

if __name__=="__main__":
    import sys
    kind,name=sys.argv[1],sys.argv[2]
    s=static(name,sys.argv[3]) if kind=="static" else video(name,sys.argv[3],sys.argv[4])
    s.pop("name")
    print(json.dumps(s,ensure_ascii=False))
