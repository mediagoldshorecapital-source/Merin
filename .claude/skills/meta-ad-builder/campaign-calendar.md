# Q4 2026 campaign calendar (NMN & Astaxanthin)

Source: the user's "Q4 Longevity Marketing Campaign Schedule" (shared 2026-10-16). Each window opens 10–15 days before the special day.

| Period | Dates | Copy file |
|---|---|---|
| Halloween / Fall Reset | Oct 16 – Oct 31 | `copy/2026-q4-halloween.json` (approved 2026-10-15) |
| Veterans Day | Oct 27 – Nov 11 | not written yet |
| Thanksgiving / BFCM Warm-up | Nov 11 – Nov 26 | not written yet |
| Black Friday & Cyber Monday (BFCM) | Nov 12 – Nov 30 | not written yet |
| Winter Solstice & Holiday Gifting | Dec 05 – Dec 25 | not written yet |
| New Year's Eve / Fresh Start | Dec 16 – Jan 01 | not written yet |

## Copy rules (from the user, 2026-10-16)

1. **Copy is locked per period.** The copy agreed at the start of a period is used on every ad set that starts inside that period, until the period ends. Don't change it mid-period unless the user asks.
2. **Confirm every time.** Even when the period's copy is already approved, show it to the user and get a confirmation before each build.
3. **Overlaps: split-test inside the 5 slots (the user's default, 2026-10-16).** Each ad has 5 slots each for primary text, headline and description, and Meta tests the combinations. In an overlap, fill those slots with a mix of both occasions, all in one copy file used on every ad in the ad set. For example, during Halloween + Veterans Day:
   - 2–3 primary texts for Halloween and 2–3 for Veterans Day (or one bridging both)
   - the same mix for headlines
   - the same mix for descriptions

   Propose the mix (which slots go to which occasion) and get the user's OK before building. Other splits (by ad set, or by ad with two copy files) are used only if the user asks for them.
4. **Record the result.** Save each approved copy as `copy/<year>-q<n>-<period>.json` (fields `period`, `dates`, `approved`, `primary_texts`, `headlines`, `descriptions`; 1–5 each). Then add the file to the table above.
5. **The offer always reads "Up to 75% off".** `build_specs.py` refuses a flat "75% off".

## Ad set start dates vs periods

New ad set every 2 days at 00:01 ET (ad set 81 started Fri Oct 16).

| Ad set | Letter | Starts | Active period(s) |
|---|---|---|---|
| 85 | C | Sat Oct 24 | Halloween |
| 86 | D | Mon Oct 26 | Halloween |
| 87 | E | Wed Oct 28 | **Overlap:** Halloween + Veterans Day |
| 88 | F | Fri Oct 30 | **Overlap:** Halloween + Veterans Day |
| 89 | G | Sun Nov 01 | Veterans Day |
| 90 | H | Tue Nov 03 | Veterans Day |
| 91 | I | Thu Nov 05 | Veterans Day |
| 92 | J | Sat Nov 07 | Veterans Day |
| 93 | K | Mon Nov 09 | Veterans Day |
| 94 | L | Wed Nov 11 | **Overlap:** Veterans Day + Thanksgiving |
| 95–101 | M–S | Nov 13 – Nov 25 | **Overlap:** Thanksgiving + BFCM |
| 102 | T | Fri Nov 27 | BFCM |
| 103 | U | Sun Nov 29 | BFCM |
| 104 | V | Tue Dec 01 | **Gap:** no period (ask the user) |
| 105 | W | Thu Dec 03 | **Gap:** no period (ask the user) |
| 106–108 | X–Z | Dec 05 – Dec 09 | Winter / Holiday Gifting |
| 109–111 | ask | Dec 11 – Dec 15 | Winter / Holiday Gifting |
| 112–116 | ask | Dec 17 – Dec 25 | **Overlap:** Winter + New Year's |
| 117–119 | ask | Dec 27 – Dec 31 | New Year's Eve / Fresh Start |

The batch letters run out at Z (ad set 108). Ask the user how naming continues before building 109.
