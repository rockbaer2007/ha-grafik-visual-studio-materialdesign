# UGSo Material Design

Externes Widget-Set für HA Grafik Visual Studio, inspiriert von
[ioBroker VIS2 Material Design](https://github.com/typhosj/ioBroker.vis2-materialdesign).

Version **0.1.0**, MIT, benötigt Studio **0.1.210** oder neuer.

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
Requires Studio 0.1.210. The first widget previews 26 palette rows in Classic,
Material 3 or Project default mode. Project default uses the General settings;
theme uses the page's light/dark setting or an explicit choice. Classic keeps a
white surface; Material 3 supports light/dark surfaces. Swatch colors remain identical.
Build with `python build.py`, install the `.wg` from `dist/`, then submit it through
the catalog registration form for review. No automatic catalog registration.

## Attribution

Independent Studio renderer; palette data adapted from MaterialDesignColorScheme.tsx
by typhosj and Scrounger under MIT. Original copyright and license are retained in
LICENSE.txt. No React/ioBroker runtime or external font is included.
