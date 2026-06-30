# NMN Welcome — "So glad you're here" (violet)

The whole welcome email used **as a single image**, with working links — per the
instruction to use the entire design image and not rebuild on top of it.

## Files
- `assets/nmn-welcome-full.png` — the entire design (457×2000, converted from the
  supplied render; webp isn't reliable in email so it's PNG).
- `email.html` — the image used whole as one clickable email. Open it from a repo
  checkout to preview (it loads the PNG via the relative `assets/` path).

## Links wired
| Clicked element | Goes to |
| --- | --- |
| The image (anywhere) | `https://tryprimeingredients.com/products/nmn` |
| **Visit our store** (live footer) | `https://tryprimeingredients.com` |
| **Unsubscribe** (live footer) | `{% unsubscribe 'Unsubscribe' %}` (Klaviyo live unsubscribe) |

> The image has a footer with an "unsubscribe" line baked into the picture — that's
> just pixels and can't be clicked. The single live footer line beneath the image is
> the working unsubscribe (legally required, and Klaviyo won't send without it).

## Klaviyo — to finish (needs the Klaviyo connector reconnected)
The Klaviyo connection dropped mid-session, so the image couldn't be hosted on
Klaviyo's CDN or pushed to the template yet. To finish:
1. Reconnect the Klaviyo connector (claude.ai connector settings).
2. The image gets uploaded to Klaviyo (Content → Images) and its hosted URL drops
   into the template `TBHuLK` in place of the `src` — replacing the earlier
   HTML build with this single-image version.

You can also do it by hand right now without waiting: in Klaviyo upload
`assets/nmn-welcome-full.png` under **Content → Images**, copy its URL, paste it as
the `<img src="…">` in the email code, and paste the code into the template's CODE
editor. The `{% unsubscribe %}` tag and the store link are already in place.
