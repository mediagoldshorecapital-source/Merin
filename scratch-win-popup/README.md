# Scratch & Win — Subscription Pop-up

A self-contained HTML subscription pop-up with a scratch-and-win mechanic.

## Behaviour

- **5 pill-shaped scratch areas**, each hiding the same prize: **3 Months Free**.
- The customer picks **one** pill and scratches it (mouse or touch).
- The moment they start scratching a pill, **all other pills lock** and no
  longer react — only one pill can ever be scratched.
- Scratching past ~45% of the coating auto-reveals the prize, fires confetti,
  and shows the email capture / **Claim Reward** row.

## Usage

Open `scratch-win-popup.html` in a browser, or embed the markup/styles/script
into your site. It has **no external dependencies**.

## Integration

Wire the reward to your backend inside the `claimBtn` click handler
(near the bottom of the `<script>`):

```js
fetch('/api/subscribe', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email, reward: '3-months-free' })
});
```

## Tuning

- `PILL_COUNT` — number of pills (default `5`).
- `PRIZE_LABEL` — the reward text (default `"3 Months Free"`).
- `REVEAL_THRESHOLD` — fraction of coating scratched before auto-reveal
  (default `0.45`).
