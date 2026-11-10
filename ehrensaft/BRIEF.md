# Ehrensaft – Brief für Instagram-Posts (@ehrensaft_official)

## Marke (aus dem Businessplan)
- Ehrensaft = Getränk aus Zitrone + Himbeere, klare Flasche mit echten Fruchtstücken. Marke in Gründung, Produkt gibt es noch NICHT zu kaufen.
- Positionierung: „Der Drink für Ehrenmänner und Ehrenfrauen“ – frech, laut, Entertainment und Straße (nicht clean/Gaming).
- Zielgruppe: Erwachsene 18–30, Späti-, Festival-, Gym-Gänger. Deutsch, Du-Form, kurz, Meme-Ton.
- Look: Zitronengelb + Himbeerpink, Neongrün NUR für alles, was leuchtet (Glow-Shaker). Dicke dunkle Konturen, Sticker-Optik. Etikett = Ehrenurkunde mit Siegel.
- Slogans (frei nutzbar): „Ehrensaft. Du weißt Bescheid.“ · „Frisch abgefüllt. Ehrenwort.“ · „Ehrensache.“ · „Nachschub für Ehrenmänner.“ · „Leuchtet, wenn's dunkel wird.“ (Glow-Shaker)

## Leitplanken – PFLICHT
1. **Keine Aussagen zu Inhaltsstoffen oder Wirkung.** Kein „Vitamin“, „gesund“, „Energie“, „beruhigt“, „Immunsystem“, „Bio“, „ohne Zucker“ usw. Nur Geschmack/Optik: Zitrone, Himbeere, echte Früchte, süß-sauer.
2. **Humor: andeuten statt aussprechen.** Der Insider-Witz entsteht im Kopf (Gelb, Flasche, „Du weißt Bescheid“). NIE Körperflüssigkeiten nennen oder zeigen, nichts Sexuelles ausschreiben, keine Emojis in die Richtung.
3. Keine Menschen/Gesichter, keine Minderjährigen, keine echten Marken/Logos anderer, niemand ist die Zielscheibe des Witzes.
4. Kein Alkohol-Bezug, keine Aufforderung zu viel zu trinken.
5. Nichts versprechen, was nicht feststeht: keine Preise, keine Daten, kein „jetzt kaufen“. Sortiment und #Ehrentester immer als „geplant“ / „bald“.
6. Jedes Video/Bild trägt unten klein den Hinweis „Design-Entwurf · Computergrafik“ (Klasse `.ki-hinweis` oder eigener Text, gut lesbar aber dezent).
7. Deutsche Rechtschreibung, echte Umlaute. Versal-„ß“ wird zu „SS“ – das ist okay.

## Technik
- Kit: `ehrensaft/kit/brand.css` (Farben, Schriften: `--display` Anton, `--fett` Bowlby One, `--hand` Permanent Marker, `--text` Inter), `ehrensaft/kit/kit.js` (`EK.flasche(opts)`, `EK.splash(p, opts)`, `EK.frucht(art, r)`, `EK.siegel(r, text)`, `EK.prog/ease/lerp/rnd`). Kit NICHT ändern – brauchst du mehr, bau es in deiner eigenen HTML-Datei.
- Beispiel, wie eine Seite aufgebaut ist: `ehrensaft/_test/demo.html`.
- Reels: 1080×1920, 30 fps, 7–12 s. Seite bietet `window.zeichne(t)` an und ist rein zeitgesteuert (keine CSS-Animationen, kein setTimeout, kein Math.random ohne `EK.rnd`). Wichtiges nicht in die oberen 250 px und unteren 420 px legen (Instagram-Bedienelemente), der Hinweis darf unten stehen.
  `python3 ehrensaft/kit/render.py video <html> <ordner>/reel.mp4 --dauer N --musik musik/<datei>.mp3 [--musik_ab S] [--titel S]` (vom Repo-Stamm aus). Erzeugt auch `reel_titel.jpg`.
- Musik: nur Dateien `musik/05…12_runway_*.mp3` (eigene, rechtefreie Tracks). Zum Ton passend wählen, Schnitt/Bewegung grob auf den Beat.
- Karussells/Bilder: 1080×1350, jede Folie ein `<div class="folie">` (1080×1350, `position:relative; overflow:hidden`).
  `python3 ehrensaft/kit/render.py bilder <html> <ordner>`
- Qualität: Hook in der ersten Sekunde (Bewegung + große Schrift), viel Bewegung (Einfliegen, Aufploppen, Wackeln, Zoom), große Schrift (Schlagzeilen ≥ 110 px), saubere Ränder (≥ 70 px), nichts überlappt oder läuft aus dem Bild. Kein statisches „Folien-Video“.
- **Selbst prüfen:** Für jedes Reel mit ffmpeg 5 Einzelbilder ziehen (z. B. bei 10/30/50/70/95 % der Dauer), mit dem Read-Werkzeug ansehen und Fehler beheben. Jede Karussell-Folie ansehen.

## Ablage je Post: `ehrensaft/posts/<nr>_<kurzname>/`
- `seite.html` (Quelle), `reel.mp4` + `reel_titel.jpg` ODER `folie_01.jpg …`
- `bildunterschrift.txt`: 2–5 kurze Zeilen im Marken-Ton, eine Mitmach-Frage oder Aufforderung (Kommentar/Speichern/Senden/Folgen), dann Leerzeile, „Design-Entwurf, Computergrafik. Produkt in Entwicklung.“, dann 5–8 Hashtags (#ehrensaft #ehrenmann #ehrenfrau #duweißtbescheid + passende).
