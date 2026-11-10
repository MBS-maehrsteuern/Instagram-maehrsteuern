#!/usr/bin/env python3
"""Ehrensaft-Renderer: HTML -> Video (Reel 1080x1920) oder Bilder (Karussell 1080x1350).

Video:  python3 ehrensaft/kit/render.py video <seite.html> <ziel.mp4> --dauer 9 [--musik musik/xx.mp3] [--fps 30]
        Die Seite muss window.zeichne(t) anbieten (t in Sekunden, deterministisch – KEINE CSS-Animationen/Timer).
        Zusätzlich entsteht <ziel>_titel.jpg (Bild bei --titel Sekunde, Standard: 60 % der Dauer).
Bilder: python3 ehrensaft/kit/render.py bilder <seite.html> <zielordner> [--b 1080 --h 1350]
        Jedes Element mit class="folie" wird als folie_01.jpg, folie_02.jpg … gespeichert.
"""
import argparse, pathlib, subprocess, tempfile
from playwright.sync_api import sync_playwright

CHROME = "/usr/bin/google-chrome"


def seite(p, pfad, b, h):
    br = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--allow-file-access-from-files"])
    pg = br.new_page(viewport={"width": b, "height": h})
    pg.goto(pathlib.Path(pfad).resolve().as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(300)
    return br, pg


def video(a):
    b, h = a.b or 1080, a.h or 1920
    n = round(a.dauer * a.fps)
    with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
        br, pg = seite(p, a.html, b, h)
        for i in range(n):
            pg.evaluate("t => window.zeichne(t)", i / a.fps)
            pg.screenshot(path=f"{tmp}/f{i:05d}.jpg", type="jpeg", quality=92)
        t_titel = a.titel if a.titel is not None else a.dauer * .6
        pg.evaluate("t => window.zeichne(t)", t_titel)
        pg.screenshot(path=str(pathlib.Path(a.ziel).with_suffix("")) + "_titel.jpg", type="jpeg", quality=92)
        br.close()
        cmd = ["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(a.fps), "-i", f"{tmp}/f%05d.jpg"]
        if a.musik:
            cmd += ["-ss", str(a.musik_ab), "-i", a.musik, "-af", f"afade=t=in:d=0.3,afade=t=out:st={a.dauer - 0.8}:d=0.8,volume={a.lautstaerke}", "-c:a", "aac", "-b:a", "192k"]
        else:  # Instagram mag Reels mit Tonspur – stille Spur anlegen
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-c:a", "aac", "-b:a", "96k"]
        cmd += ["-t", str(a.dauer), "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", a.ziel]
        subprocess.run(cmd, check=True)
    print("fertig:", a.ziel)


def bilder(a):
    b, h = a.b or 1080, a.h or 1350
    ziel = pathlib.Path(a.ziel); ziel.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        br, pg = seite(p, a.html, b, h)
        folien = pg.query_selector_all(".folie")
        for i, f in enumerate(folien, 1):
            f.screenshot(path=str(ziel / f"folie_{i:02d}.jpg"), type="jpeg", quality=93)
        br.close()
    print("fertig:", len(folien), "Folien in", ziel)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("art", choices=["video", "bilder"]); ap.add_argument("html"); ap.add_argument("ziel")
    ap.add_argument("--dauer", type=float, default=8); ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--musik"); ap.add_argument("--musik_ab", type=float, default=0); ap.add_argument("--lautstaerke", type=float, default=0.9)
    ap.add_argument("--titel", type=float); ap.add_argument("--b", type=int); ap.add_argument("--h", type=int)
    a = ap.parse_args()
    video(a) if a.art == "video" else bilder(a)
