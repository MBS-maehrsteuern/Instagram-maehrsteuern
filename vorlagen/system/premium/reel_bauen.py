"""Premium-Reel bauen (Motion-Design-Look, Wissen 25.10.): HTML-Szene → Frames (rendern.mjs) → MP4 mit Loris' Stimme.
    python3 vorlagen/system/premium/reel_bauen.py einspruch posts/34_2026-10-25_reel_einspruch 27
Erwartet <post>/ton/stimme.wav (optional <post>/ton/sfx.wav = Sounddesign aus sfx.py); schreibt <post>/reel.mp4 (−18 LUFS) und <post>/titelbild.png (= Frame 1, Hook)."""
import subprocess, sys, tempfile
from pathlib import Path
hier = Path(__file__).resolve().parent
REPO = hier.parent.parent.parent
# Klangabgleich für die Stimme (Loris 26.10.: „dumpf“): misst jede Aufnahme und gleicht sie an eine Sprach-Zielkurve an
sys.path.insert(0, str(hier))
from klang import filter_fuer
nur_ton = "--nur-ton" in sys.argv          # Bild aus vorhandenem reel.mp4 übernehmen, nur den Ton neu mischen
sys.argv = [a for a in sys.argv if a != "--nur-ton"]
name, post, dauer = sys.argv[1], REPO / sys.argv[2], float(sys.argv[3])
KLANG = filter_fuer(post / "ton/stimme.wav")
musik = REPO / (sys.argv[4] if len(sys.argv) > 4 else "musik/06_runway_lofi_ruhig.mp3")
sfx = post / "ton/sfx.wav"
eingaenge = ["-i", str(sfx)] if sfx.exists() else []
mix = "[3:a]volume=0.35[s];[1:a][m][s]amix=inputs=3" if sfx.exists() else "[1:a][m]amix=inputs=2"
with tempfile.TemporaryDirectory() as tmp:
    if nur_ton:
        bild, vcodec = ["-i", str(post / "reel_alt.mp4")], ["-c:v", "copy"]
        (post / "reel.mp4").rename(post / "reel_alt.mp4")
    else:
        subprocess.run(["node", "rendern.mjs", f"{name}.html", str(dauer), tmp], check=True, cwd=hier)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", f"{tmp}/f00000.jpg", str(post / "titelbild.png")], check=True)
        bild, vcodec = ["-framerate", "30", "-i", f"{tmp}/f%05d.jpg"], ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18"]
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", *bild, "-i", str(post / "ton/stimme.wav"),
                    "-i", str(musik), *eingaenge, "-filter_complex",
                    f"[1:a]{KLANG}[v];[2:a]volume=0.08,afade=t=in:d=0.8,afade=t=out:st={dauer - 1.5}:d=1.5[m];"
                    f"{mix.replace('[1:a]', '[v]')}:duration=longest:normalize=0,"
                    f"atrim=0:{dauer},asetpts=N/SR/TB,loudnorm=I=-18:TP=-1.5:LRA=11[a]",
                    "-map", "0:v", "-map", "[a]", *vcodec, "-c:a", "aac", "-b:a", "192k",
                    "-ar", "48000", "-t", str(dauer), "-movflags", "+faststart", str(post / "reel.mp4")], check=True)
if nur_ton:
    (post / "reel_alt.mp4").unlink()
print("✓", post / "reel.mp4")
