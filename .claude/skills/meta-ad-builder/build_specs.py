"""Spec builder for Prime Ingredients ads (account 2009539369903270 only).

Encodes the CLAUDE.md core rules: URL parameters, creative setup/Advantage+
all off except Enhance CTA + multi-advertiser ads, and Add music on statics
only (audio OPT_IN *and* asset_feed_spec.audios - the toggle alone leaves
music off, confirmed 2026-10-16). Copy comes from an approved copy file
(copy/<period>.json: primary_texts, headlines, descriptions; 1-5 each).

Usage:
  python3 .claude/skills/meta-ad-builder/build_specs.py <copy.json> static "<ad name>" <image_hash>
  python3 .claude/skills/meta-ad-builder/build_specs.py <copy.json> video  "<ad name>" <video_id> <thumbnail_url>
Prints the creative JSON to pass to ads_create_ad.
"""
import json,sys
L="https://tryprimeingredients.com/products/nmn"
UT="utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&tw_source={{site_source_name}}&tw_adid={{ad.id}}"
PAGE="1012373248616002"; IG="17841480103037701"
OFF=["site_extensions","product_extensions","show_summary","local_store_extension","profile_card","image_touchups","text_optimizations","image_templates","adapt_to_placement","inline_comment","image_animation","add_text_overlay","description_automation","image_brightness_and_contrast","image_uncrop","video_auto_crop","media_type_automation","show_destination_blurbs","reveal_details_over_time","text_translation"]

def load_copy(path):
    c=json.load(open(path))
    for k in ("primary_texts","headlines","descriptions"):
        if not 1<=len(c[k])<=5: sys.exit(f"{k}: need 1-5 entries, got {len(c[k])}")
    for t in c["primary_texts"]+c["headlines"]+c["descriptions"]:
        if "75%" in t and "up to 75%" not in t.lower(): sys.exit(f"offer must say 'Up to 75%': {t[:60]}")
    return c

def dof(static):
    f={"enhance_cta":{"enroll_status":"OPT_IN"},"audio":{"enroll_status":"OPT_IN" if static else "OPT_OUT"}}
    for k in OFF: f[k]={"enroll_status":"OPT_OUT"}
    return {"creative_features_spec":f}

def spec(c,story,static):
    afs={"bodies":[{"text":t} for t in c["primary_texts"]],"titles":[{"text":t} for t in c["headlines"]],
         "descriptions":[{"text":t} for t in c["descriptions"]],"optimization_type":"DEGREES_OF_FREEDOM"}
    if static: afs["audios"]=[{"type":"random"}]  # music asset: required or Add music stays off
    return {"url_tags":UT,"object_story_spec":{"page_id":PAGE,"instagram_user_id":IG,**story},
            "asset_feed_spec":afs,"degrees_of_freedom_spec":dof(static),"contextual_multi_ads":{"enroll_status":"OPT_IN"}}

def static(c,h):
    P,H,D=c["primary_texts"],c["headlines"],c["descriptions"]
    return spec(c,{"link_data":{"image_hash":h,"link":L,"message":P[0],"name":H[0],"description":D[0],"caption":"Primeingredients.com","call_to_action":{"type":"SHOP_NOW","value":{"link":L}}}},True)

def video(c,v,pic):
    P,H,D=c["primary_texts"],c["headlines"],c["descriptions"]
    return spec(c,{"video_data":{"video_id":v,"image_url":pic,"message":P[0],"title":H[0],"link_description":D[0],"call_to_action":{"type":"SHOP_NOW","value":{"link":L,"link_caption":"Primeingredients.com"}}}},False)

if __name__=="__main__":
    c=load_copy(sys.argv[1]); kind=sys.argv[2]
    s=static(c,sys.argv[4]) if kind=="static" else video(c,sys.argv[4],sys.argv[5])
    print(json.dumps(s,ensure_ascii=False))
