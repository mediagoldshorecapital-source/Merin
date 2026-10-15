#!/usr/bin/env python3
"""
Pull still frames out of an ad so visuals and on-screen text can be OBSERVED
with the Read tool instead of imagined.

Writes <outdir>/frames/frame_<mmss>.png plus a contact-sheet index. Read the
PNGs before describing wardrobe, setting, b-roll, pack shots or OST cards.

Also writes <outdir>/cover.jpg: the first non-black frame of the ad, used as
the cover image under each video's title in the report so a reader can
recognise the ad and its creator at a glance.
"""
import argparse, os, shutil, subprocess, sys

def ts_label(sec):
    m, s = divmod(int(sec), 60)
    return f"{m:02d}m{s:02d}s"

def duration(path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration", "-of",
                              "default=noprint_wrappers=1:nokey=1", path],
                             capture_output=True, text=True, check=True).stdout.strip()
        return float(out)
    except Exception:
        return None

def mean_brightness(path):
    try:
        from PIL import Image, ImageStat
        return ImageStat.Stat(Image.open(path).convert("L")).mean[0]
    except Exception:
        return None

def write_cover(video, outdir, width, dur):
    """First frame that isn't a black fade-in. Falls back to the 0s frame."""
    out = os.path.join(outdir, "cover.jpg")
    cands = [0.0, 0.3, 0.7, 1.2, 2.0]
    if dur:
        cands = [t for t in cands if t < dur] or [0.0]
    first = None
    for t in cands:
        tmp = os.path.join(outdir, f".cover_{t}.jpg")
        r = subprocess.run(["ffmpeg", "-y", "-ss", str(t), "-i", video,
                            "-frames:v", "1", "-q:v", "3",
                            "-vf", f"scale={width}:-1", tmp],
                           capture_output=True, text=True)
        if r.returncode != 0 or not os.path.exists(tmp):
            continue
        first = first or tmp
        b = mean_brightness(tmp)
        if b is None or b > 18:
            shutil.copyfile(tmp, out); break
    else:
        if first:
            shutil.copyfile(first, out)
    for f in os.listdir(outdir):
        if f.startswith(".cover_"):
            os.remove(os.path.join(outdir, f))
    return out if os.path.exists(out) else None

def main():
    p = argparse.ArgumentParser()
    p.add_argument("video")
    p.add_argument("--outdir", default="./ad-workdir")
    p.add_argument("--every", type=float, default=2.0,
                   help="seconds between frames (2s suits a 60s UGC ad)")
    p.add_argument("--at", default="",
                   help="comma-separated extra timestamps in seconds, e.g. 0,3,15,45")
    p.add_argument("--width", type=int, default=720)
    p.add_argument("--max-frames", type=int, default=60,
                   help="guard against dumping hundreds of PNGs from a long VSL")
    a = p.parse_args()

    if not shutil.which("ffmpeg"):
        print("ERROR: ffmpeg not installed — cannot extract frames.\n"
              "Say 'Visuals not analyzed — no frames available' in the report "
              "rather than describing a scene you have not seen.", file=sys.stderr)
        sys.exit(2)
    if not os.path.exists(a.video):
        print(f"ERROR: not found: {a.video}", file=sys.stderr); sys.exit(2)

    fdir = os.path.join(a.outdir, "frames")
    os.makedirs(fdir, exist_ok=True)
    dur = duration(a.video)

    times = []
    if dur:
        step = max(a.every, dur / a.max_frames)
        t = 0.0
        while t < dur:
            times.append(round(t, 2)); t += step
    if a.at:
        times += [float(x) for x in a.at.split(",") if x.strip()]
    times = sorted(set(times))[: a.max_frames]
    if not times:
        times = [0.0]

    made = []
    for t in times:
        out = os.path.join(fdir, f"frame_{ts_label(t)}.png")
        r = subprocess.run(["ffmpeg", "-y", "-ss", str(t), "-i", a.video,
                            "-frames:v", "1", "-vf", f"scale={a.width}:-1", out],
                           capture_output=True, text=True)
        if r.returncode == 0 and os.path.exists(out):
            made.append((t, out))

    cover = write_cover(a.video, a.outdir, a.width, dur)

    idx = ["# Extracted frames", "",
           f"Cover: {cover}" if cover else "Cover: none", "",
           f"Source: {os.path.abspath(a.video)}",
           f"Duration: {dur:.1f}s" if dur else "Duration: unknown", "",
           "Read these images before writing any visual or on-screen-text "
           "description. Anything you cannot see in a frame does not go in the report.", ""]
    for t, f in made:
        m, s = divmod(int(t), 60)
        idx.append(f"- `{m}:{s:02d}` -> {f}")
    open(os.path.join(a.outdir, "frames_index.md"), "w").write("\n".join(idx) + "\n")

    print(f"Extracted {len(made)} frames -> {fdir}")
    print(f"Index: {os.path.join(a.outdir, 'frames_index.md')}")
    if cover:
        print(f"Cover: {cover}  (put ![Cover]({cover}) under the video title)")
    print("Next: Read the PNGs (especially hook + CTA frames) before describing visuals.")

if __name__ == "__main__":
    main()
