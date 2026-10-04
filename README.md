# UGSo Material Design

Externes Widget-Set für HA Grafik Visual Studio, inspiriert von
[ioBroker VIS2 Material Design](https://github.com/typhosj/ioBroker.vis2-materialdesign).

Version **1.0.1**, MIT mit MDI-Icon-Lizenzhinweisen, benötigt Studio **0.1.216** oder neuer.

Die Palette verwendet die originalen MDI-Symbole pro Widget: blau (#44739e),
weiße Kachel und abgerundete Ecken. Alle 49 Zuordnungen liegen als lokale SVGs
vor, ohne Font- oder Internet-Abhängigkeit. `icons/catalog.json` dokumentiert
die Zuordnung; LICENSE.txt enthält die Pictogrammers- und Apache-2.0-Hinweise.
Studio 0.1.216 erlaubt reine Icon-Updates bestehender Pakete; Eigenschaften,
Standardwerte und Renderer bleiben bei diesem Update unverändert.

Das Set enthält jetzt **49 Widgets**: alle Button- und Icon-Button-Varianten,
Checkbox/Switch, Input/Select/Autocomplete, Slider/Slider Round, Value, Card,
Icon, Fortschritt linear/rund, Listen, Icon List, Table, Alerts, vier Diagramme,
Calendar, Top App Bar, Grid/Masonry Views, Advanced View in Widget/8 und die
bisherigen Dialoge sowie Farbvorschau. Die ersten drei Definitionen bleiben
unverändert; ein Update von 0.3.0 ist möglich.

Autocomplete unterstützt Editor-Menüpunkte, JSON, Wertelisten und HA-Entitätsoptionen,
Filtern, Tastaturauswahl, freie Texteingabe oder reine Auswahl, Löschen sowie
kompakte/erweiterte Eigenschaften. „Felder neu aus der Entität befüllen“ übernimmt
HA-Namen, Einheit, Optionen und verfügbare Reglergrenzen. Neue Renderer schreiben
nur unterstützte switch/input_boolean, input_number/input_text und select/input_select;
Sensoren und Attribute bleiben Anzeigen. Ohne Entität funktionieren Vorschauwerte
und Aktionen lokal. Bei echten Entitäten entscheidet zusätzlich Home Assistant.

JSON Chart akzeptiert axisLabels/graphs, labels/datasets und Punktlisten. History
liest HA Recorder für bis zu zehn Entitäten und 1–168 Stunden. List/Icon List bieten
Editor- oder JSON-Zeilen mit Entitätsanzeige und Bedienung; Table kann sortiert werden.
Alerts können lokal aus der Liste entfernt oder über eine schreibbare Entität bzw.
separate Quittierungs-Entität bestätigt werden. Calendar nutzt den Studio-Kalender.
Ansichten verwenden andere lokale Studio-Seiten mit Rekursionsschutz.

`python complete_package.py` erzeugt die zusätzlichen deklarativen Definitionen;
`python create_comparison.py` erzeugt das importierbare Projekt unter `comparison/`.
Es enthält neun Vergleichsseiten plus eine Referenzansicht, ohne echte HA-Entitäten.
Der anschließende Widget-für-Widget-Vergleich prüft Originaloptik und Detailoptionen.
Es ist keine automatische ioBroker-Projektübernahme: ioBroker Theme-/Objekt-IDs,
History-Adapter, Binding-Ausdrücke und ioBroker-Schreibdienste werden durch die
Studio-/HA-Funktionen ersetzt. Nicht jede ioBroker-Detailoption hat eine Entsprechung;
mehrere Y-Achsen, gestapelte Balken, ioBroker-Timer-Sperren und HTML in Listentexten
sind noch nicht enthalten. HTML-Karten werden getrennt in einer Sandbox angezeigt.
Die erneute Registrierung erfordert Katalog-Webseite 0.1.13 (lokales Update-ZIP).

Drittes Widget: **Dialog iFrame** mit HTTP-/HTTPS-Quelle oder relativem Pfad.
Es übernimmt Auslöser, Vollbild, Kopf-/Fußzeile und erweiterte Layoutoptionen
des Seiten-Dialogs. Die iFrame-Einstellungen bleiben auch ohne erweiterte
Optionen sichtbar. Standardmäßig gilt eine Sandbox mit Scripts/Formularen;
„Sandbox deaktivieren“ entfernt sie ausdrücklich. „Nahtlos“ entfernt den Rahmen.
Scrolloptionen werden wie beim Studio-iFrame gesetzt; die Kontrolle einzelner
Achsen auf fremden Seiten hängt vom Browser und der eingebetteten Seite ab.
Seiten mit CSP frame-ancestors/X-Frame-Options können das Einbetten blockieren.
Es gibt keinen Proxy und keinen Zugriff auf den Inhalt fremder Seiten.

Zweites Widget: **Dialog** zum Einbetten einer anderen Studio-Seite. Unter Allgemein
die Ansicht auswählen; die aktuelle Seite und rekursive Seitenketten sind gesperrt.
Ohne erweiterte Optionen bleiben Allgemein und Layout Dialog sichtbar. Die Gruppen
Button Layout, Kopfzeile und Fußzeilen-Schaltflächen kommen bei aktivierter Option hinzu.
Ausblenden löscht keine Einstellungen. Der Klick öffnet nur in der Runtime.

Alternativ öffnet eine boolesche Home-Assistant-Entität den Dialog. Beim Schließen
wird eine switch/input_boolean-Entität ausgeschaltet. Andere Entitäten bleiben
unverändert; nach lokalem Schließen öffnet der Dialog erst beim nächsten Aus/Ein-Wechsel.
Vollbild, Außenklick, Escape, Titel, Fußzeile, Farben, Schrift und optionales
Vibrieren/Klicksound sind einstellbar. Browser können Feedback einschränken.
Symbole sind Text/Unicode; der ioBroker-Bildkatalog und dessen Theme-Objekte werden
nicht importiert. Als Ansicht wird eine lokale Studio-Seite verwendet.

Erstes Widget: **Preview Color Schemes** mit allen 26 Farbreihen, horizontalem
und vertikalem Scrollen sowie Klassisch, Material 3 und Projektstandard.
Der Projektstandard folgt der Material-Design-Auswahl unter Einstellungen → Allgemein.
Das Farbschema folgt wahlweise dem hellen/dunklen Seitenthema oder einer festen Auswahl.
Klassisch verwendet wie das Original einen weißen Hintergrund; Material 3 unterstützt beide Farbschemata.
Farbreihen bleiben beim Stilwechsel unverändert. Keine Entitätsbindung und keine Schreibaktion.

`python build.py` erzeugt das reproduzierbare `.wg` unter `dist/`, inklusive Prüfsumme.
In Studio über Einstellungen → Widget-Pakete → Lokal oder den direkten GitHub-Dateilink installieren.
Für den Registrierungstest das Paket über die Katalog-Webseite einreichen und anschließend prüfen/freigeben.
Das Paket wird nicht automatisch im Katalog eingetragen.

Original-Referenz: `tplVis2-materialdesign-ColorScheme-Preview`.
`designStyle=legacy` entspricht Klassisch. Die ioBroker-Objekt-ID `__mdwThemeDark`
wird durch das Studio-Seitenthema ersetzt. Der ioBroker-Button „Thema verwenden“
ist kein eigener Theme-Import in Studio.

## English

External data-only widget package inspired by ioBroker VIS2 Material Design.
Version 0.3.0 requires Studio 0.1.214. The third widget, Dialog iFrame, embeds
HTTP/HTTPS sources or relative paths. It keeps the iFrame settings visible in
compact mode and reuses dialog controls. Default sandbox allows scripts/forms;
the explicit opt-out removes it. Seamless removes the border. Scrolling support
depends on the browser and embedded site; CSP/X-Frame-Options may block embedding.
There is no proxy or access to external page content. Dialog embeds another local Studio page;
advanced mode reveals button, header and footer controls while preserving hidden values.
Runtime supports button or boolean entity triggers, responsive fullscreen, native modal
keyboard/focus handling and outside-click closing. Closing switch/input_boolean triggers
turns them off. Other entities remain read-only and need a new off/on transition to reopen.
Symbols use text/Unicode; ioBroker image and theme objects are not imported.
The first widget previews 26 palette rows in Classic,
Material 3 or Project default mode. Project default uses the General settings;
theme uses the page's light/dark setting or an explicit choice. Classic keeps a
white surface; Material 3 supports light/dark surfaces. Swatch colors remain identical.
Build with `python build.py`, install the `.wg` from `dist/`, then submit it through
the catalog registration form for review. No automatic catalog registration.

## Attribution

Version 1.0.1 contains all 49 widget entries with their original MDI preview
symbols as local SVGs. Icon license notices are included in LICENSE.txt.
It requires Studio 0.1.216 and catalog 0.1.13. Input/select/autocomplete, action buttons, displays,
lists/tables/alerts, charts/calendar and local page layouts use original UGSo
renderers. HA entities replace ioBroker object IDs and Recorder replaces history
adapters. The comparison project uses local demo values. Detailed visual parity
is subject to the planned widget-by-widget review; multiple Y axes, stacked bars,
ioBroker timed locks and HTML in list text are not implemented. The first three
definitions are unchanged, allowing additive updates from 0.3.0.

Independent Studio renderer; palette data adapted from MaterialDesignColorScheme.tsx
by typhosj and Scrounger under MIT. Original copyright and license are retained in
LICENSE.txt. No React/ioBroker runtime or external font is included.
