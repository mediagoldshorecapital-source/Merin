# Naming Convention

Copy-paste reference. Consistency here is what makes every report in this SOP possible.

---

## Campaign

```
PI | CORE | CBO | Sales
PI | TEST | CBO | Sales          ← T4 only
```

Format: `{BRAND} | {PURPOSE} | {BUDGET TYPE} | {OBJECTIVE}`

---

## Ad set

```
CONTROL
TESTA_3PMCRASH_UGC
TESTB_BRAINFOG_VSL
TESTC_SKEPTIC_STATIC          ← T3+
```

Format: `{SLOT}_{ANGLE}_{FORMAT}` — CONTROL takes no suffix.

| Slot | Meaning |
|------|---------|
| `CONTROL` | Proven winners. No spending limit |
| `TESTA` / `TESTB` / `TESTC` | Test slots. Forced daily minimum = 1× AOV |

---

## Ad

```
R{ring}_{ANGLE}_{FORMAT}_{PERSONA}_{VISUALSCENE}_v{n}
```

Examples:
```
R1_3PMCRASH_UGC_LINDA62_KITCHEN_v1
R1_3PMCRASH_UGC_LINDA62_CARPARK_v1
R2_SKEPTIC_FOUNDER_FOUNDER_OFFICE_v1
R3_3PMCRASH_TESTIMONIAL_MASHUP_v1
R4_SKEPTIC_STATIC_BUNDLE_LABCERT_v2
R5_SKEPTIC_STATIC_REVIEW_OLIVIA_v1
R1_3PMCRASH_UGC_LINDA62_FLEX322_v1     ← Flexible ad (3:2:2)
```

### Allowed values

| Slot | Values |
|------|--------|
| `{ring}` | `1` `2` `3` `4` `5` |
| `{ANGLE}` | `3PMCRASH` · `BRAINFOG` · `GRANDKIDS` · `SKEPTIC` |
| `{FORMAT}` | `UGC` · `VSL` · `FOUNDER` · `TESTIMONIAL` · `STATIC` · `ADVERTORIAL` |
| `{PERSONA}` | `LINDA62` · `LINDA55` · `ROBERT65` · `FOUNDER` · `MASHUP` |
| `{VISUALSCENE}` | free text, no spaces, UPPERCASE — `KITCHEN` `CARPARK` `COUCH` `PARKWALK` `BUNDLE` |
| `v{n}` | iteration: `v1` `v2` `v3` |
| `FLEX322` | append instead of a scene when it's a 3:2:2 Flexible Ad |

---

## Custom audiences

```
EXCL_Purchasers_180d
EXCL_Purchasers_180d_CRM
SEED_HighAOV_Buyers
ENG_VideoViewers_75_30d
ENG_AllEngagers_90d
```

Format: `{PURPOSE}_{DESCRIPTION}_{WINDOW}`

| Prefix | Meaning |
|--------|---------|
| `EXCL_` | Exclusion audience |
| `SEED_` | Value/seed signal |
| `ENG_` | Engagement, diagnostics |

---

## Landing pages

```
/pages/energy-advertorial
/pages/clarity-advertorial
/products/nmn-complex?variant=b3g3
```

---

## UTM block (paste into every ad's URL parameters field)

```
utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&utm_id={{campaign.id}}&utm_source_platform=meta&placement={{placement}}&site_source={{site_source_name}}
```

---

## Creative files (in your asset store)

```
PI_R1_3PMCRASH_UGC_LINDA62_KITCHEN_v1_4x5.mp4
PI_R1_3PMCRASH_UGC_LINDA62_KITCHEN_v1_9x16.mp4
PI_R1_3PMCRASH_UGC_LINDA62_KITCHEN_v1_HOOK-A.mp4
PI_R4_SKEPTIC_STATIC_BUNDLE_LABCERT_v2_1080x1350.png
```

---

## The rules

1. **Never rename a live ad.** It breaks historical reporting joins and your UTM history.
2. **Version, don't overwrite.** A revised asset is `v2`, never an edited `v1`.
3. **Uppercase for the fixed vocabulary, no spaces anywhere.**
4. If a name doesn't fit the grammar, the *asset* is probably wrong — you've likely built
   something that doesn't map to a Ring. Go back to the Concept Matrix.
