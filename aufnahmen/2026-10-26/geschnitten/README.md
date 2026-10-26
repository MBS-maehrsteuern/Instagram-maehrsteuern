# Schnitt Aufnahme 26.10.2026 – Finanzamt-Insider I1–I12

Rohdatei `../insider_roh.mp3` (7:38 min, −12,9 LUFS). Transkript mit Wortzeiten `../woerter.json` (faster-whisper medium),
Sprechabschnitte `../chunks.json` (Energie-Erkennung, Rauschboden −45,5 dB, Schwelle +12 dB). Schnitt: `schnitt.py`.

Entfernt: Vorgespräch (0–31 s), alle angesagten Nummern („Nummer eins“, „zwei“, „3.“ …), abgebrochene Anläufe:
- I2: erster Satz in zwei Fassungen + „Beim Konto, nochmal“ (102–112 s) → Fassung 1 („deinen Kontostand“) + „Beim Kontenabruf …“
- I3: erster Anlauf bis „Du hast einen Monat ab…“ (132–143 s) → zweiter, vollständiger Anlauf
- I9: „Schick das an werdende, nochmal, am Ende“ (340–344 s) → Neuansatz „Viele Eltern … Schick das an werdende Eltern.“
- I11: erster Anlauf („… oben auf dem Bescheid“, 388–394 s) → zweiter Anlauf („… Briefkopf“)
Pausen > 0,45 s auf 0,30 s gekürzt, Atmer/Geräusche in Pausen um 28 dB abgesenkt, 12-ms-Blenden an jedem Schnitt.
Klang: Hochpass 80 Hz, leichte Entrauschung, Kompressor 2,5:1, De-Esser, −16 LUFS / −1,5 dBTP.
Kontrolle: jede Spur neu transkribiert (`woerter.json`) – vollständig, keine Nummern, keine Doppelungen.
