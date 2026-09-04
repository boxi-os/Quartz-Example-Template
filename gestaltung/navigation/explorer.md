---
title: Explorer
description: Der Ordnerbaum links — bis zur vierten Ebene gestaltet.
section: Gestaltung
tags:
  - gestaltung
  - navigation
translationKey: gestaltung/navigation/explorer
---

Links im Fenster steht der Baum über alle Notizen. Er ist die Komponente mit dem größten
Gestaltungsaufwand in dieser Vorlage, weil die Tiefe das eigentliche Problem ist.

## Von Haus aus

Quartz rückt jede Ebene ein und färbt den aktiven Eintrag. Auf Ebene drei oder vier lässt sich
nicht mehr erkennen, zu welchem Elternordner eine Datei gehört — der Einzug allein trägt die
Struktur nicht.

## In dieser Vorlage

- **Führungslinie je Ebene.** Jede verschachtelte Liste bekommt eine Haarlinie zum Elternordner.
  Bei vier Ebenen sind das vier Linien, an denen das Auge zurückfindet.
- **Gewicht sinkt mit der Tiefe.** Ebene 1 ist fett, Ebene 2 halbfett, ab Ebene 3 normal und
  kleiner. Der Kopf einer Verzweigung ist damit auffindbar.
- **Ab Ebene fünf wird nicht weiter eingerückt**, nur noch die Linie geführt — fünf Einzüge lassen
  in einer drei Spalten schmalen Leiste kein Wort mehr übrig.
- **Ein Symbol vor jeder Zeile.** Ordner tragen ein Ordner-Icon, das offen und geschlossen
  verschieden aussieht, Dateien ein Datei-Icon — beide aus dem Lucide-Satz. Die Zeile sagt damit,
  *was* sie ist, bevor sie sagt, wie sie heißt.
- **Der aktive Eintrag** bekommt Farbe, Halbfett *und* einen Balken links.
- **Der ganze Weg dorthin ist markiert.** Jeder Ordner, unter dem die offene Seite liegt, färbt
  seinen Namen und sein Symbol im Akzent ein, und die Führungslinie des direkten Elternordners
  färbt mit. Vorher sah ein aufgeklappter Ordner genauso aus wie einer, den jemand vor zehn Minuten
  von Hand aufgeklappt hatte — die Spur von der Wurzel zur aktuellen Seite war unsichtbar.
- **Alle Ausklapp-Pfeile sind dieselbe Lucide-Chevron.** Vorher zeichneten der Kopf des Baums, jeder
  Ordner, das Inhaltsverzeichnis und die aufklappbare Layout-Box vier verschiedene.
- **Lange Namen** werden abgeschnitten statt umgebrochen; drei Zeilen für einen Dateinamen zerreißen
  den Baum.
- **Ein langer Baum scrollt in sich selbst** (60 % der Fensterhöhe) statt die Fußzeile
  wegzuschieben, und blendet dabei **oben und unten weich aus** — die Kante sagt, dass da noch mehr
  ist, ohne eine Linie zu ziehen.
- **Am Telefon ist er eine Schublade.** Der Knopf sitzt in der App-Leiste, wird beim Öffnen zum
  Kreuz, die Schublade fährt von links über eine abgedunkelte Seite, und die Seite selbst scrollt
  solange nicht mit.

Zu sehen ist das am besten unter [[handbuch/grundlagen/begriffe/abkuerzungen/liste|Liste]] — vier
Ordner tief.

## Zwei Sprachen, ein Baum

Der Explorer weiß nichts von Sprachen: Er baut seinen Baum aus jeder Seite des Builds und zeigte
ohne Zutun den deutschen und den englischen zugleich. Die Vorlage löst das im Stylesheet. Auf einer
deutschen Seite ist der `en`-Ordner ausgeblendet; auf einer englischen alles außer ihm, und seine
eigene Zeile gleich mit, damit der englische Baum ganz oben steht statt eine Ebene eingerückt.

Der Weg des Plugins — ein `filterFn` für den Explorer — ist von hier aus nicht erreichbar: Er wird
nur aus `quartz.ts` entgegengenommen, und dieses Projekt baut sein Layout aus
`quartz.config.yaml`. Siehe [[gestaltung/mehrsprachigkeit/grenzen|Wo die zwei Sprachen aufhören]].

## Zwei Funde beim Bauen

Die Klassennamen führen in die Irre. **Nur die Wurzelliste heißt `explorer-ul`**; jede verschachtelte
heißt `ul.tree-item-children`. Und **`.nav-file-title` ist der Link selbst**, nicht sein Elternteil.
Die erste Fassung dieser Datei stylte deshalb ins Leere — sichtbar war das nicht, weil Quartz'
eigene Einrückung ähnlich genug aussah.

Zugeklappt kappt Quartz die ganze Komponente bei `1.2em`. Wer seiner Überschrift eine Zielgröße von
44 px gibt, verliert sie damit vollständig. Diese Vorlage verlegt das Einklappen deshalb auf den
Inhalt und lässt den Kopf stehen.

## Was das Plugin nicht kann

> [!warning] Die Ordner starten zugeklappt, und die Option dagegen wirkt nicht
> `@quartz-community/explorer` 0.1.0 kennt `folderDefaultState: 'open'` und schreibt den Wert auch
> brav ins Markup — sein eigenes Skript liest ihn nur nie. Es holt den Faltzustand ausschließlich
> aus dem `localStorage` und nimmt für alles, was dort nicht steht, *zugeklappt* an. Offen sind
> deshalb nur die Ordner auf dem Weg zur aktuellen Seite.
>
> Mit einem Stylesheet ist das nicht zu heilen: „offen“ und „noch nie angefasst“ tragen dieselbe
> Klasse, CSS kann die beiden nicht unterscheiden.

Der Explorer **selbst** — die ganze Komponente — ist dagegen aufgeklappt und bleibt es; nur am
Telefon startet er geschlossen, sonst stünde vor dem Text erst einmal die halbe Navigation.

> [!bug] Und einer, der hausgemacht war
> Genau das ging eine Zeit lang schief: Eine Regel dieser Vorlage gab dem Schubladen-Knopf
> `display: grid`, ohne ihn auf schmale Fenster zu beschränken. Weil hier alles ungeschichtet steht,
> schlug das Quartz' eigenes `display: none` — der Knopf war auch bei 1600 px da. Und das Skript des
> Plugins endet mit „wenn dieser Knopf sichtbar ist, klapp den Baum zu“. Der Baum war also auf jedem
> Desktop-Aufruf zu, obwohl er gerendert wurde.
