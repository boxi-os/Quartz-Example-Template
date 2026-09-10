---
title: Explorer
description: Der Ordnerbaum links — bis zur vierten Ebene gestaltet.
section: 5 – Die Gestaltung
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
  Bei vier Ebenen sind das vier Linien, an denen das Auge zurückfindet. Sie steht unter der Spitze
  des Pfeils, der die Ebene aufgeklappt hat, nicht daneben — und Dateien beginnen auf derselben
  Kante wie die Ordner ihrer Ebene, nicht davor. Beides war eine Zeit lang um ein paar Pixel
  daneben, aus drei verschiedenen Gründen, und drei kleine Fehler in derselben Richtung sehen aus
  wie Absicht.
- **Gewicht sinkt mit der Tiefe.** Ebene 1 ist fett, Ebene 2 halbfett, ab Ebene 3 normal und
  kleiner. Der Kopf einer Verzweigung ist damit auffindbar.
- **Ab Ebene fünf wird nicht weiter eingerückt**, nur noch die Linie geführt — fünf Einzüge lassen
  in einer drei Spalten schmalen Leiste kein Wort mehr übrig.
- **Ein Symbol vor jeder Zeile.** Ordner tragen ein Ordner-Icon, das offen und geschlossen
  verschieden aussieht, Dateien ein Datei-Icon — beide aus dem Lucide-Satz. Die Zeile sagt damit,
  *was* sie ist, bevor sie sagt, wie sie heißt.
- **Der aktive Eintrag** bekommt Farbe, Halbfett *und* einen Balken links — auch dann, wenn er
  eine Ordnerseite ist. Das Plugin selbst kann das nicht: Es setzt seine Klasse nur auf Datei-
  Zeilen, eine Ordnerzeile trägt bloß ein `data-folderpath`, und die aktuelle Seite steht in
  `<body data-slug>`. Zwei Attribute miteinander vergleichen kann kein Selektor — also wird die
  Regel gebaut statt gesucht, von einer [[7-nachschlagen/01-glossar#Layout-Box|Layout-Box]], die nichts ausgibt als ein `<style>` mit dem
  Pfad dieser einen Seite darin.
- **Die ganze Zeile ist anklickbar**, bei Dateien wie bei Ordnern. Bei Ordnern war lange nur der
  Name der Link, während die Hinterlegung beim Überfahren über die volle Breite lief — sie
  versprach ein Ziel auf ganzer Zeile und antwortete auf einem Drittel. Der Pfeil bleibt daneben
  das, was auf- und zuklappt.
- **Der ganze Weg dorthin ist markiert.** Jeder Ordner, unter dem die offene Seite liegt, färbt
  seinen Namen und sein Symbol im Akzent ein, und die Führungslinie des direkten Elternordners
  färbt mit. Vorher sah ein aufgeklappter Ordner genauso aus wie einer, den jemand vor zehn Minuten
  von Hand aufgeklappt hatte — die Spur von der Wurzel zur aktuellen Seite war unsichtbar.
- **Alle Ausklapp-Pfeile sind dieselbe Lucide-Chevron.** Vorher zeichneten der Kopf des Baums, jeder
  Ordner, das Inhaltsverzeichnis und die aufklappbare [[7-nachschlagen/01-glossar#Layout-Box|Layout-Box]] vier verschiedene.
- **Lange Namen** werden abgeschnitten statt umgebrochen; drei Zeilen für einen Dateinamen zerreißen
  den Baum.
- **Ein langer Baum scrollt in sich selbst** (60 % der Fensterhöhe) statt die Fußzeile
  wegzuschieben, und blendet dabei **oben und unten weich aus**. Der Kasten trägt dafür genau so
  viel Innenabstand, wie die Kante tief ist: Ganz oben steht die erste Zeile deshalb *unter* dem
  Verlauf statt darin, ganz unten die letzte darüber. Beide Enden liest man in voller Stärke; weich
  wird nur, was gerade vorbeizieht.
- **Am Telefon ist er eine Schublade.** Der Knopf sitzt in der App-Leiste, wird beim Öffnen zum
  Kreuz, die Schublade fährt von links über eine abgedunkelte Seite, und die Seite selbst scrollt
  solange nicht mit.

Zu sehen ist das am besten unter [[2-formatierung/05-callouts/grundform|Callouts — Grundform]] —
drei Ordner tief, und im Explorer ein voll aufgeklappter Ast.

## Zwei Sprachen, ein Baum

Der Explorer weiß nichts von Sprachen: Er baut seinen Baum aus jeder Seite des [[7-nachschlagen/01-glossar#Build|Builds]] und zeigte
ohne Zutun den deutschen und den englischen zugleich. Die Vorlage löst das im [[7-nachschlagen/01-glossar#Stylesheet|Stylesheet]]. Auf einer
deutschen Seite ist der `en`-Ordner ausgeblendet; auf einer englischen alles außer ihm, und seine
eigene Zeile gleich mit, damit der englische Baum ganz oben steht statt eine Ebene eingerückt.

Der Weg des [[7-nachschlagen/01-glossar#Plugin|Plugins]] — ein `filterFn` für den Explorer — ist von hier aus nicht erreichbar: Er wird
nur aus `quartz.ts` entgegengenommen, und dieses Projekt baut sein Layout aus
`quartz.config.yaml`. Siehe [[6-anpassen/07-zwei-sprachen/grenzen|Wo die zwei Sprachen aufhören]].

## Welches Element eigentlich rollt

Das musste erst geklärt werden, bevor Maske und Kante überhaupt an der richtigen Stelle sitzen
konnten. Quartz gibt der inneren Liste `max-height: 100%` — und die beiden Browser lösen das
verschieden auf:

| | rollendes Element | Kasten | Liste |
| --- | --- | --- | --- |
| Chrome | die innere `ul` | 540 px, kein Überlauf | 540 px, 148 px Überlauf |
| Firefox | der Kasten `.explorer-content` | 540 px, 148 px Überlauf | 688 px, kein Überlauf |

Gemessen auf derselben Seite: 148 px Überlauf in beiden, aber an zwei verschiedenen Elementen.
Alles, was diese Vorlage an das Rollen hängt — die weiche Kante, das eingesperrte Überscrollen, die
dünne Rollleiste —, sitzt auf `.explorer-content`. In Chrome traf es damit ein Element, das gar
nicht rollt.

Die Liste gibt ihre Deckelung deshalb auf (`max-height: none; overflow: visible`), und der Kasten
ist in beiden Browsern der eine Roller.

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
> Klasse, [[7-nachschlagen/01-glossar#CSS und SCSS|CSS]] kann die beiden nicht unterscheiden.

Der Explorer **selbst** — die ganze Komponente — ist dagegen aufgeklappt und bleibt es; nur am
Telefon startet er geschlossen, sonst stünde vor dem Text erst einmal die halbe Navigation.

> [!bug] Und einer, der hausgemacht war
> Genau das ging eine Zeit lang schief: Eine Regel dieser Vorlage gab dem Schubladen-Knopf
> `display: grid`, ohne ihn auf schmale Fenster zu beschränken. Weil hier alles ungeschichtet steht,
> schlug das Quartz' eigenes `display: none` — der Knopf war auch bei 1600 px da. Und das Skript des
> Plugins endet mit „wenn dieser Knopf sichtbar ist, klapp den Baum zu“. Der Baum war also auf jedem
> Desktop-Aufruf zu, obwohl er gerendert wurde.

<!-- QuartzControl:variables:start -->
## Welche Variablen hier greifen

Diese 33 Variablen liest `nav-explorer.scss`. Ändern lassen sie sich in der App unter *Stile → Variablen* — ohne eine Zeile CSS.

| Variable | Wert | gilt außerdem für |
| --- | --- | --- |
| `--dark` | `#17171A` · dunkel `#FCFCFA` | 13 weitere Komponenten |
| `--darkgray` | `#333333` · dunkel `#DDDDDD` | 18 weitere Komponenten |
| `--gray` | `#5F5F5F` · dunkel `#A1A1A1` | 21 weitere Komponenten |
| `--headerFont` | `"Instrument Sans", ui-sans-serif, system-…` | 14 weitere Komponenten |
| `--icon-close` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--icon-file` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--icon-folder` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--icon-folder-open` | im Stylesheet gesetzt (`base.scss`) | nur hier |
| `--light` | `#FCFCFA` · dunkel `#16171A` | 13 weitere Komponenten |
| `--secondary` | `#1463A3` · dunkel `#699DC3` | 20 weitere Komponenten |
| `--tpl-accent-bar` | `3px` | 5 weitere Komponenten |
| `--tpl-drawer-width` | `min(86vw, 340px)` | nur hier |
| `--tpl-header-h` | im Stylesheet gesetzt (`base.scss`) | 6.4 – Variablen |
| `--tpl-icon` | `1.1rem` | Farbschema-Umschalter, Lesemodus |
| `--tpl-icon-sm` | `0.95rem` | 6.4 – Variablen, Der Sprachumschalter |
| `--tpl-indent` | `0.85rem` | Inhaltsverzeichnis |
| `--tpl-motion` | `150ms ease` | 12 weitere Komponenten |
| `--tpl-radius-lg` | `14px` | 3 weitere Komponenten |
| `--tpl-radius-md` | `8px` | 16 weitere Komponenten |
| `--tpl-radius-sm` | `4px` | 9 weitere Komponenten |
| `--tpl-rule` | `var(--lightgray)` = `#DDDDDD` | 18 weitere Komponenten |
| `--tpl-rule-width` | `1px` | 24 weitere Komponenten |
| `--tpl-shadow` | `0 6px 24px rgba(23, 23, 26, 0.10)` · dunkel `0 6px 24px rgba(0, 0, 0, 0.55)` | 4 weitere Komponenten |
| `--tpl-space-2xs` | `0.25rem` | 15 weitere Komponenten |
| `--tpl-space-lg` | `1.5rem` | 11 weitere Komponenten |
| `--tpl-space-md` | `1rem` | 17 weitere Komponenten |
| `--tpl-space-xs` | `0.5rem` | 19 weitere Komponenten |
| `--tpl-surface` | `var(--lightgray)` = `#DDDDDD` | 6 weitere Komponenten |
| `--tpl-surface-tint` | `var(--highlight)` = `rgba(42, 78, 108, 0.10)` | 14 weitere Komponenten |
| `--tpl-target` | `44px` | 11 weitere Komponenten |
| `--tpl-text-sm` | `0.875rem` | 19 weitere Komponenten |
| `--tpl-text-xs` | `0.78rem` | 9 weitere Komponenten |
| `--tpl-tracking-label` | `0.08em` | 8 weitere Komponenten |

*Diese Tabelle ist erzeugt: Sie wird aus den Stylesheets gelesen, nicht von Hand gepflegt.*
<!-- QuartzControl:variables:end -->
