# 13 · Backlog Automatisierung

Stand 03.10.2026. Bewertung und Freigabe durch Loris, Umsetzung durch Claude.

## ✅ Umgesetzt (Sprint 1, 03.10.)
- **Wächter** – ein offenes Issue „🚨 Wächter“, kommentiert nur bei rotem Workflow oder Schlüssel < 14 Tage (`automatik/waechter.py`, läuft im Lage-Lauf)
- **Stichwort-Abgleich** – `automatik/interaktion.json` ist die einzige Quelle; Abweichungen in Bildunterschriften erscheinen in `LAGE.md` unter „Braucht dich“
- **Radar-Pflege** – montags im Radar-Issue: 🧹 entfernen / ➕ aufnehmen, übernommen wird nur, was abgehakt ist
- **Erste-Stunde-Checkliste** – nach jedem Feed-Beitrag als Kommentar im Freigabe-Issue
- Actions auf Node 24, Runner fest `ubuntu-24.04`

## ✅ Umgesetzt (Sprint 2, 03.10.)
- **#3 Wochenbericht + #9 Herkunft der Demos** – sonntags ein Issue (`automatik/wochenbericht.py`); Demos/ManyChat/Herkunft per Kommentar von Hand (Variante a), zusätzlich gezählt aus `strategie/dm_tracking.csv` (Variante b, Spalte `termin_gebucht` = ja); Werte in `automatik/statistik/woche.csv`. Automatisch: Reclaim bucht fest in den Hauptkalender → Apps-Script `automatik/apps_script/demo_kopie.gs` (Loris' Google-Konto) kopiert nur Demo-Buchungen ohne Namen/E-Mails nach „maehrsteuern Autopilot“, Herkunft aus dem Pflichtfeld „Woher kennst du mich?“ (Variante C, 03.10.; Echttest 03.10. bestanden: Kopie „📅 Demo gebucht (Instagram)“ erschienen, nach Absage gelöscht; Herkunft mit allen 5 Optionen gegen das echte Reclaim-Format geprüft). Abgelehnt: Dienstkonto liest Hauptkalender (Variante B, zu weit). Nicht genutzt: UTM (Reclaim speichert ihn nicht sicher), eigene Links je Quelle (Feld ist genauer), ManyChat-API (nur Pro), Reclaim-Webhooks (nur Business).
- **`kalender.ics` entfernt** – ersetzt durch den Direkt-Sync
- **#1 Kalender-Direktsync** – Google-Kalender „maehrsteuern Autopilot“ per Dienstkonto (nur dieser Kalender, Scope `calendar.events`), jeder Lage-Lauf, idempotent, Postzeiten „beschäftigt“ für Reclaim, To-dos „frei“, Farben je Art (`automatik/kalender_sync.py`)

## ✅ Umgesetzt (Robustheit, 03.10.)
- **Kein Doppel-Post:** `posten.py` pusht den Status mit Wiederholung; nach dem Warten wird der Plan neu gelesen („stop“, neue Zeit, „entfaellt“ greifen noch); kurze API-Aussetzer (Verbindung, 5xx) 3× wiederholt – `media_publish` nie; fehlender Link nach dem Veröffentlichen markiert den Beitrag nicht mehr als „fehler“
- **Kein Schlüssel im Repo/Log:** IG_TOKEN wird aus Fehlermeldungen in `plan.json` entfernt; neuer Schlüssel beim Verlängern maskiert und per stdin an `gh secret set`; Ablaufdatum erst nach erfolgreichem Ersetzen
- **Keine verlorenen Antworten:** „go“/„K12 ok“/Nachträge laufen je Kommentar in eigener Concurrency-Gruppe (vorher konnte ein neuer Kommentar einen wartenden Lauf verdrängen)
- **Push-Wiederholung** mit `rebase --abort` in allen Skripten, Statistik-Push mit Wiederholung, LinkedIn-Paket bricht ohne Push ab
- **Reserve-Takt:** Lage stößt die Schlüssel-Verlängerung an, wenn < 30 Tage übrig; Statistik-Neuversuch nach 30 Min.
- **posten.yml:** Eingaben nur als Umgebungsvariable (keine Befehlseinschleusung)
- Offen (klein): `insights_voll.py` holt täglich die ganze Historie neu; `lage.py`-Protokoll liest das ganze Git-Log; Push-Schleifen in ein Modul zusammenführen

## ✅ Umgesetzt (Nachträge, 03.10. nachmittags)
- **Radar:** Backoff bei Meta-Drosselung (HTTP 429, Codes 4/17/32/613/8000x; 30/90/270 s, `Retry-After` beachtet), Abbruch statt Dauerfeuer; nur dauerhafte Fehler führen zu 🧹-Vorschlägen; 1 s Pause je Konto; Art-Erkennung mit mehr Stichwörtern, fehlende/unbekannte Art als Hinweis im Issue
- **Wochenbericht:** Demo-Kopien ohne `q`-Suche und mit Blättern gelesen, Herkunft-Regex bleibt in der Zeile, Nachträge nur am Zeilenanfang/nach Komma (keine Treffer in Zitaten oder in „Gesamtstand ManyChat …“)
- **Einmalige Erinnerungen:** `automatik/erinnerungen.json` → „Braucht dich“ in LAGE.md + Termin im Autopilot-Kalender (Art `erinnerung`, „frei“)


## 🔧 Content-Fabrik für 2 Beiträge pro Tag (08.10.)
**Problem:** Die Fabrik baut höchstens 4 Beiträge pro Lauf an 2 Tagen, also 8 pro Woche. Der Testmonat braucht 14 Feed-Beiträge pro Woche.
**Lösung (Loris hat zugestimmt):**
- ✅ **Zeitplan:** 3 Läufe pro Woche, **Mo, Mi, Fr 08:47** (umgestellt am 08.10.; vorher Mo/Do).
- ⏳ **Prompt** (nur im Chat der Routine „Instagram Content-Fabrik (in Session)“ änderbar). Punkt 2 dort ersetzen:
  > Leere Slots von übermorgen bis +7 Tage füllen, **höchstens 6 Feed-Beiträge pro Lauf** (Teaser-/Frage-Storys zählen nicht).
  > Slots: 12:15 und 19:30 (Feed), Storys 12:45 und 19:35. Reihenfolge der Slots und Formate nach `strategie/15_plan_2_pro_tag.md`,
  > sobald es die Datei gibt. Bis dahin: mittags Karussell, abends Reel.
  > Stimm-Reels nur mit Sprachnachricht (sonst `wartet_auf_sprachnachricht`). Pro Beitrag `"stimme": true/false` und `"hook": "fall"|"zahl"` setzen.
  > Lieber ein Slot leer als ein schwacher Beitrag.

  Punkt 5 (Commit) ersetzen: Autor „Loris M.“ per `--author`, Committer = signierende Identität aus git config, Co-Authored-By-Zeile für Claude.
- **Rechnung:** 3 × 6 = 18 Plätze für 14 Beiträge. Das lässt Puffer für Slots, die bewusst leer bleiben, und für Loris' manuelle Reels.
- **Engpass ist nicht die Fabrik, sondern die Freigabe.** 14 Freigaben pro Woche heißt 2 pro Tag. Freigabe-Issues deshalb bündeln (ein Issue je Lauf statt je Beitrag), wenn das zu viel wird.

## 🔧 Umsetzung Auswertung 11.10.
**Erledigt (Claude, 11.10.):** Tagesbericht repariert (Reel-Länge auch für von Hand gepostete Reels, Soll-Ist, Skip-Verlauf, ⚠️ Geteilt > Erreicht,
Median-Hook, 1620 px) · Reels 13–16 auf 12–15 s gekürzt · Mittags-Feed 12:15, Storys 12:45 · Sprechtexte 18–22 (≤ 15 s, Rechtsstand geprüft;
Verlustvortrag auf 70 % korrigiert) · `15_plan_2_pro_tag.md` · Tagesbericht-Routine auf 09:15 · Monatsbericht-Routine: neue Commit-Regel + Commit-Erlaubnis.

**Vorschläge zu freigegebenen Beiträgen (nicht umgesetzt – Go im Freigabe-Issue):**
- ~~**04-story-frage** (Do 15.10. 18:00, Issue #44): Tipp-Version~~ → **erledigt 12.10.** (go tippen): Plan zeigt `story_mo_frage_tippen.png`
  (👏 = mehr über mich · 😮 = mehr Tools).
- ~~**01-reel-ampel** (Sa 17.10.): auf ca. 15 s kürzen~~ → **erledigt 12.10.** (go kürzen): `reel_kurz.mp4`, 15,3 s, −18 LUFS
  (Schnitt `vorlagen/system/schnitt/p01_reel_ampel_kurz_bauen.py`), Langfassung `reel_stimme.mp4` bleibt liegen.
- **04-reel-mein-weg** (Fr 16.10.): 13 s, passt.
- ~~**22-reel-steuersatz** (So 18.10.): auf KW 44 schieben~~ → **erledigt 13.10.** (go): Mo 26.10. 19:30.
- **Erledigt 13.10. (go Loris für alle offenen Konflikte in `15_plan_2_pro_tag.md`):** Ampel-Reel Sa 17.10. 12:15 (Teaser 12:45),
  Notlösung ohne Stimme ab Do 15.10. 12:00, Mo 12.10. mittags leer ok. Story Bio-Link lief bereits Di 13.10. 19:35.

**Routinen – nur Loris kann klicken (claude.ai/code → Routinen):**
1. „Instagram Tagesbericht 9 Uhr“: **Quelle/Repo** `MBS-maehrsteuern/Instagram-maehrsteuern` mit Schreibzugriff eintragen (die Routine hat aktuell
   *keine* Quelle → Push 403 „not in this session's authorized repository set“). **Connectoren:** Google Calendar und GitHub hinzufügen.
   GitHub → Settings → Applications → Claude → Repository access: Instagram-maehrsteuern (großes I) freigeben.
2. Prompt der Tagesbericht- und der Fabrik-Routine: nur aus deren eigenem Chat änderbar. Neue Texte: `automatik/routinen/tagesbericht.md`
   und `automatik/routinen/content_fabrik.md` – die Bitte zum Übernehmen wurde am 11.10. in beide Routine-Chats geschickt; prüfen, ob sie es getan haben.
3. Berechtigungen: Die Prompts enthalten jetzt die Zeile „ERLAUBNIS: … darf und soll committen und pushen“. Falls der Auto-Modus trotzdem
   „Unrequested Commit“ meldet: in den Routine-Einstellungen den Berechtigungsmodus auf „Bypass/Auto mit Git erlaubt“ stellen.

**Zeitplan:** Statistik ca. 08:48, Tagesbericht jetzt 09:15 (vorher 08:58, zu knapp). Die zwei Zusatzläufe am 09.10. um 05:54/05:55 Berlin
(03:54/03:55 UTC) fallen mit der Änderung der Routine um 03:50 UTC zusammen (Prompt-Update + Testauslösung) – kein Doppel-Trigger im Zeitplan.

**Sammel-Freigabe (3.3a, Vorschlag):** ein Freigabe-Issue pro Woche (Mo 19:00) mit allen Entwürfen der Woche, „go 12“ / „go alle“ je Zeile.
Dafür `automatik/freigabe.py` umbauen – erst nach Loris' Go.

## ⏸️ Zurückgestellt bis ca. 15 Beiträge
Vorher fehlen die Daten, um daraus etwas Belastbares abzuleiten.
- **#4 Rückmeldung an die Content-Fabrik** – 48 h nach jedem Beitrag Speichern/Teilen pro Reichweite bewerten, Ergebnis in `strategie/was_funktioniert.md`, die Fabrik liest es mit
- **#5 Themenliste aus Kommentaren und Radar** – wöchentlich Fragen und häufige Begriffe sammeln (Claude, ca. 0,50 €/Monat) → `strategie/themen.md`
- **#10 Beste Uhrzeiten monatlich** – Empfehlung aus den Aktiv-Zeiten der Follower, nie automatisch umstellen
- **#11 Collab nachfassen** – 7 Tage nach abgehakter Anfrage ohne Antwort ein Hinweis im Radar

## ❌ Abgelehnt
- **#12 LinkedIn per API posten** – Dokument-Posts brauchen die freigabepflichtige Community-Management-API; 2 Min. von Hand sind günstiger

## Grundsätze
- Nie automatisch posten, kommentieren, folgen, liken oder DMs senden. DMs nur über ManyChat.
- Benachrichtigungen niedrig halten, lieber bündeln (ein Issue je Zweck, Status im Issue-Text statt neuer Kommentare).
- Kosten, Upgrades, neue Zugänge: erst fragen.

## Serie „Zinsschranke – 6 Regeln“ (Loris, Aufnahme 17.10.)
Reel 21 (Do 22.10.) endet mit „Das ist Regel Nr. 1. Es gibt aber noch 5 andere.“ → Folge-Reels (je 12–20 s, Stimme, Hook *zahl*):
1. ✓ 30 % vom steuerlichen EBITDA / Freigrenze < 3 Mio. € Nettozinsaufwand (§ 4h Abs. 1, Abs. 2 S. 1 Buchst. a EStG)
2. EBITDA-Vortrag: ungenutztes verrechenbares EBITDA 5 Jahre vortragbar (§ 4h Abs. 1 S. 3 EStG)
3. Zinsvortrag: nicht abziehbare Zinsen gehen in spätere Jahre (§ 4h Abs. 1 S. 5 EStG)
4. Stand-alone-Klausel: kein Konzern → keine Zinsschranke (§ 4h Abs. 2 S. 1 Buchst. b; bei KapGes § 8a Abs. 2 KStG beachten)
5. Escape-Klausel: Eigenkapitalquote nicht mehr als 2 Prozentpunkte unter Konzern (§ 4h Abs. 2 S. 1 Buchst. c; § 8a Abs. 3 KStG)
6. Untergang des Zinsvortrags bei schädlichem Anteilseignerwechsel (§ 8a Abs. 1 S. 3 i. V. m. § 8c KStG) bzw. Betriebsaufgabe (§ 4h Abs. 5 EStG)
Vor dem Einsprechen Rechtsstand prüfen; Sprechtexte dann in posts/sprechtexte.md, Termine ab KW 44/45 in freie Stimm-Slots (Sa mittags) oder als Ersatz für 17.
