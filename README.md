# UGSo Material Design

Externes Widget-Set für HA Grafik Visual Studio, inspiriert von
[ioBroker VIS2 Material Design](https://github.com/typhosj/ioBroker.vis2-materialdesign).

Version **0.3.0**, MIT, benötigt Studio **0.1.214** oder neuer.

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

Independent Studio renderer; palette data adapted from MaterialDesignColorScheme.tsx
by typhosj and Scrounger under MIT. Original copyright and license are retained in
LICENSE.txt. No React/ioBroker runtime or external font is included.
