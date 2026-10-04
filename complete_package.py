"""Generate the remaining original UGSo declarations; no ioBroker runtime code.

The public ioBroker widget catalog is the functional reference. The first three
definitions remain byte-for-byte equivalent so installed packages update safely.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def field(key, label, value='', options=None, minimum=None, maximum=None):
    kind = 'select' if options else 'checkbox' if isinstance(value, bool) else 'number' if isinstance(value, (int, float)) else 'color' if 'Color' in key else 'text'
    descriptor = dict(key=key, label=label, type=kind)
    if options:
        descriptor['options'] = options
    if minimum is not None:
        descriptor['min'] = minimum
    if maximum is not None:
        descriptor['max'] = maximum
    return descriptor, value

def group(label, *fields):
    return label, fields

STYLE = group('Darstellung (erweitert)', field('backgroundColor', 'Hintergrundfarbe'), field('textColor', 'Textfarbe'), field('primaryColor', 'Primärfarbe'), field('hoverColor', 'Hover-Farbe'), field('selectedColor', 'Ausgewählte Farbe'), field('fontFamily', 'Schriftart'), field('fontSize', 'Schriftgröße', 16, minimum=8, maximum=100), field('cornerRadius', 'Eckenradius', 12, minimum=0, maximum=100))
SIZE = group('Größe und Position', field('width', 'Breite', 240, minimum=24, maximum=3000), field('height', 'Höhe', 70, minimum=20, maximum=3000))
INPUT_LAYOUT = group('Layout Eingabe (erweitert)', field('inputLayout', 'Layout', 'regular', ['regular', 'solo', 'solo-rounded', 'solo-shaped', 'filled', 'filled-rounded', 'filled-shaped', 'outlined', 'outlined-rounded', 'outlined-shaped']), field('inputAlignment', 'Textausrichtung', 'left', ['left','center','right']), *[field(k,l) for k,l in [('inputLayoutBackgroundColor','Hintergrundfarbe'),('inputLayoutBackgroundColorHover','Hintergrundfarbe hover'),('inputLayoutBackgroundColorSelected','Hintergrundfarbe ausgewählt'),('inputLayoutBorderColor','Randfarbe'),('inputLayoutBorderColorHover','Randfarbe hover'),('inputLayoutBorderColorSelected','Randfarbe ausgewählt'),('inputTextFontFamily','Schriftart')]], field('inputTextFontSize','Schriftgröße',16), field('inputTextColor','Textfarbe'),field('autofocus','Automatisch fokussieren',False))
INPUT_LABEL = group('Beschriftung der Eingabe', field('inputLabelText','Text'), field('inputLabelColor','Textfarbe'),field('inputLabelColorSelected','Textfarbe ausgewählt'),field('inputLabelFontFamily','Schriftart'),field('inputLabelFontSize','Schriftgröße',16),field('inputTranslateX','Versatz X',0),field('inputTranslateY','Versatz Y',0))
INPUT_EXTRAS = [group('Anhänge der Eingabe (erweitert)',field('inputPrefix','Vorangestellter Text'),field('inputSuffix','Angehängter Text'),field('inputAppendixColor','Textfarbe'),field('inputAppendixFontSize','Schriftgröße',14),field('inputAppendixFontFamily','Schriftart')),group('Untertext der Eingabe (erweitert)',field('showInputMessageAlways','Immer anzeigen',True),field('inputMessage','Text'),field('inputMessageFontFamily','Schriftart'),field('inputMessageFontSize','Schriftgröße',14),field('inputMessageColor','Textfarbe')),group('Zählerlayout (erweitert)',field('showInputCounter','Zähler anzeigen',False),field('inputCounterColor','Textfarbe'),field('inputCounterFontSize','Schriftgröße',14),field('inputCounterFontFamily','Schriftart'))]
ICON_FIELDS = [field('clearIconShow','Text-Löschen-Symbol anzeigen',True)]
for prefix,label,icon,size in [('clearIcon','Text-Löschen-Symbol','mdi:close',16),('collapseIcon','Menüsymbol','mdi:menu-down',16),('prepandIcon','Vorangestelltes Symbol','',20),('prepandInnerIcon','Inneres vorangestelltes Symbol','',20),('appendOuterIcon','Äußeres angehängtes Symbol','',20)]:
    ICON_FIELDS.extend([field(prefix,label,icon),field(prefix+'Size','Größe '+label,size),field(prefix+'Color','Farbe '+label)])
ICONS = group('Symbole (erweitert)', *ICON_FIELDS)
MENU = group('Daten des Menüs',field('listDataMethod','Eingabemethode','inputPerEditor',['inputPerEditor','jsonStringObject','multistatesObject','valueList']),field('countSelectItems','Anzahl Menüpunkte',3,minimum=0,maximum=20),field('jsonStringObject','JSON-String'),field('valueList','Werteliste'),field('valueListLabels','Werteliste: Beschriftung'),field('valueListIcons','Werteliste: Bilder'))
MENU_LAYOUT = group('Menü-Layout (erweitert)',field('listPosition','Position','auto',['auto','top','bottom']),field('listPositionOffset','Positionsoffset verwenden',False),field('openOnClear','Nach Löschen öffnen',False),field('listItemHeight','Höhe des Menüpunktes',48),field('showSelectedIcon','Symbol des ausgewählten Elements','prepend-inner',['no','prepend','prepend-inner','append-outer']),field('listIconSize','Symbolgröße',20),field('showValue','Wert anzeigen',True),*[field(k,l) for k,l in [('listItemBackgroundColor','Hintergrundfarbe'),('listItemBackgroundHoverColor','Hover-Farbe'),('listItemBackgroundSelectedColor','Farbe ausgewählt'),('listIconColor','Symbolfarbe'),('listIconHoverColor','Symbolfarbe hover'),('listIconSelectedColor','Symbolfarbe ausgewählt')]])
MENU_FONTS=[]
for prefix,label,size in [('listItem','Text',16),('listItemSub','Zweiter Text',14),('listItemValue','Wert',14)]:
    MENU_FONTS.extend([field(prefix+'FontSize',label+' Schriftgröße',size),field(prefix+'Font',label+' Schriftart'),field(prefix+'FontColor',label+' Farbe'),field(prefix+'FontHoverColor',label+' Farbe hover'),field(prefix+'FontSelectedColor',label+' Farbe ausgewählt')])
MENU_FONTS=group('Menü-Schrift (erweitert)',*MENU_FONTS)

def definition(slug,label,family,groups=(),defaults=None):
    common=group('Allgemein',field('labelText','Bezeichnung',label),field('entityId','Home-Assistant-Entität'),field('entityAttribute','Attribut'),field('designStyle','Gestaltungsstil','material3',['legacy','material3','project']),field('themeMode','Farbschema','project',['project','light','dark']),field('showAdvanced','Erweiterte Optionen anzeigen',False),field('readOnly','Nur anzeigen',False))
    data=dict(materialKind=family,state='',padding=0,borderWidth=0)
    properties=[]
    for title,fields in [common,*groups,STYLE,SIZE]:
        properties.append(dict(label=title,fields=[f for f,v in fields]))
        data.update({f['key']:v for f,v in fields})
    data.update(defaults or {})
    return dict(type='ugso.materialdesign/'+slug,label=label,icon='icons/palette.svg',defaults=data,render=dict(kind='material-widget',valueKey='labelText'),propertyGroups=properties)

def generate():
    manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    manifest['version']='1.0.0'
    manifest['widgets']=manifest['widgets'][:3]
    widgets=manifest['widgets']
    for slug,label in [('autocomplete','Autocomplete'),('select','Select'),('input','Input')]:
        groups=[group('Eingabe',field('inputMode','Eingabemodus','write',['write','select']),field('inputType','Eingabetyp','text',['text','number','date','time','password']),field('maxLength','Maximale Textlänge',255,minimum=1,maximum=255)),INPUT_LAYOUT,INPUT_LABEL,*INPUT_EXTRAS,ICONS]
        if slug!='input':
            groups.extend([MENU,MENU_LAYOUT,MENU_FONTS])
            for i in range(20):
                groups.append(group(f'Menüpunkt [{i}]',field(f'value{i}','Wert',str(i+1)),field(f'label{i}','Beschriftung',f'Eintrag {i+1}'),field(f'subLabel{i}','Zweiter Text'),field(f'listIcon{i}','Symbol'),field(f'listIconColor{i}','Symbolfarbe'),field(f'imageColorSelectedTextField{i}','Symbolfarbe im Textfeld')))
        widgets.append(definition(slug,label,slug,groups))
    actions=[('addition','Addition'),('link','Link'),('navigation','Navigation'),('state','State'),('multi-state','State Multi'),('toggle','Toggle')]
    for layout in ['default','vertical','icon']:
        for action,title in actions+([('slider','Slider')] if layout=='icon' else []):
            slug=('icon-button-' if layout=='icon' else 'button-')+action+('-vertical' if layout=='vertical' else '')
            groups=[group('Aktion',field('targetPage','Zielseite'),field('linkUrl','Link (HTTP/HTTPS)'),field('writeValue','Zu schreibender Wert','1'),field('offValue','Wert AUS','off'),field('onValue','Wert EIN','on'),field('addition','Addition',1),field('stateValues','Wertefolge (Semikolon)','0;1;2'),field('icon','Symbol','mdi:gesture-tap-button')),group('Button Layout (erweitert)',field('buttonStyle','Schaltflächenstil','raised',['raised','outlined','text']),field('lockEntityId','Sperr-Entität'),field('buttonTextColor','Schriftfarbe'),field('buttonBackgroundColor','Hintergrundfarbe'),field('pressedColor','Farbe gedrückt'))]
            widgets.append(definition(slug,('Icon Button ' if layout=='icon' else 'Button ')+title+(' vertical' if layout=='vertical' else ''),'button',groups,dict(actionKind=action,buttonLayout=layout,width=72 if layout=='icon' else 160,height=100 if layout=='vertical' else 48)))
    for slug,label in [('checkbox','Checkbox'),('switch','Switch')]:
        widgets.append(definition(slug,label,slug,[group('Schaltwerte',field('offValue','Wert AUS','off'),field('onValue','Wert EIN','on'),field('lockEntityId','Sperr-Entität'))]))
    for slug,label in [('slider','Slider'),('slider-round','Slider Round')]:
        widgets.append(definition(slug,label,slug,[group('Regler',field('minValue','Minimum',0),field('maxValue','Maximum',100),field('step','Schrittweite',1,minimum=.001),field('orientation','Ausrichtung','horizontal',['horizontal','vertical']),field('unit','Einheit'),field('lockEntityId','Sperr-Entität'),field('showValue','Wert anzeigen',True)),group('Skala (erweitert)',field('showTicks','Teilstriche anzeigen',False),field('tickCount','Anzahl Teilstriche',5,minimum=2,maximum=20),field('thumbSize','Griffgröße',18),field('trackWidth','Spurbreite',8))],dict(width=200,height=200 if slug.endswith('round') else 70,state=50)))
    for slug,label in [('progress','Progress'),('progress-circular','Progress Circular')]:
        widgets.append(definition(slug,label,slug,[group('Fortschritt',field('minValue','Minimum',0),field('maxValue','Maximum',100),field('showValue','Wert anzeigen',True),field('indeterminate','Unbestimmter Fortschritt',False),field('striped','Gestreift',False),field('trackWidth','Spurbreite',8),field('unit','Einheit','%'))],dict(width=140,height=140 if slug.endswith('circular') else 60,state=50)))
    widgets.append(definition('value','Value','value',[group('Wertformat',field('decimals','Nachkommastellen',1,minimum=0,maximum=6),field('unit','Einheit'),field('prefix','Präfix'),field('suffix','Suffix'),field('trueText','Text bei EIN','Ein'),field('falseText','Text bei AUS','Aus'),field('valueType','Werttyp','auto',['auto','number','boolean','text','date']),field('dateFormat','Datumformat','datetime',['datetime','date','time']),field('factor','Faktor',1),field('offset','Offset',0))],dict(state=21.5)))
    widgets.append(definition('card','HTML Card','card',[group('Karte',field('cardTitle','Titel','Material Design'),field('cardText','Inhalt','Text oder HTML'),field('image','Bild-URL'),field('linkUrl','Link (HTTP/HTTPS)'),field('targetPage','Zielseite'),field('contentIsHtml','Inhalt als isoliertes HTML anzeigen',False))],dict(width=300,height=200)))
    widgets.append(definition('icon','Material Design Icon','icon',[group('Symbol',field('icon','Symbol','mdi:home'),field('iconSize','Symbolgröße',48),field('iconColor','Symbolfarbe'),field('onIcon','Symbol EIN','mdi:home'),field('offIcon','Symbol AUS','mdi:home-outline'))],dict(width=80,height=80)))
    widgets.append(definition('installed-version','Installed Version','version',[],dict(width=180,height=40)))
    for slug,label in [('list','List'),('icon-list','Icon List'),('table','Table'),('alerts','Alerts')]:
        groups=[group('Daten',field('dataJson','JSON-Daten','[{"label":"Beispiel","value":"Bereit"}]'),field('rowCount','Anzahl Editor-Zeilen',3,minimum=0,maximum=10),field('dataMethod','Datenquelle','json',['json','editor','entity']),field('columns','Spalten (Schlüssel:Beschriftung)','label:Bezeichnung;value:Wert'),field('showHeader','Kopfzeile anzeigen',True),field('gridColumns','Icon-Spalten',3,minimum=1,maximum=12)),group('Zeilen Layout (erweitert)',field('rowHeight','Zeilenhöhe',48),field('rowGap','Abstand',8),field('acknowledgeValue','Quittierungswert',''),field('acknowledgeEntityId','Quittierungs-Entität'))]
        for i in range(10):
            groups.append(group(f'Zeile [{i}]',field(f'rowLabel{i}','Beschriftung',f'Zeile {i+1}'),field(f'rowEntityId{i}','Entität'),field(f'rowValue{i}','Vorschauwert','Bereit'),field(f'rowIcon{i}','Symbol','mdi:information-outline'),field(f'rowControl{i}','Bedienung','text',['text','button','switch','checkbox']),field(f'rowWriteValue{i}','Schreibwert','on')))
        widgets.append(definition(slug,label,slug,groups,dict(width=400,height=270)))
    for slug,label,kind in [('chart-bar','Bar Chart','bar'),('chart-pie','Pie Chart','pie'),('chart-json','JSON Chart','json'),('chart-line-history','Line History Chart','history')]:
        groups=[group('Diagrammdaten',field('dataJson','JSON (Chart.js oder Punkte)','{"labels":["A","B","C"],"datasets":[{"label":"Serie","data":[20,45,35]}]}'),field('dataCount','Anzahl Datenreihen',1,minimum=1,maximum=10),field('chartTitle','Diagrammtitel',label),field('showLegend','Legende anzeigen',True),field('historyHours','Verlauf in Stunden',24,minimum=1,maximum=168),field('unit','Einheit')),group('Achsen (erweitert)',field('yMin','Y-Minimum'),field('yMax','Y-Maximum'),field('gridColor','Rasterfarbe'),field('lineWidth','Linienbreite',2),field('showPoints','Punkte anzeigen',True))]
        for i in range(10):
            groups.append(group(f'Datenreihe [{i}]',field(f'seriesEntityId{i}','Entität'),field(f'seriesName{i}','Name',f'Serie {i+1}'),field(f'seriesColor{i}','Farbe'),field(f'seriesData{i}','JSON-Punkte','[]')))
        widgets.append(definition(slug,label,'chart',groups,dict(chartKind=kind,width=400,height=270)))
    widgets.append(definition('calendar','Calendar','calendar',[group('Kalender',field('eventJson','JSON-Termine','[]'),field('fcView','Ansicht','month',['month','week','day','year','listWeek']),field('firstDayOfWeek','Erster Wochentag','monday',['monday','sunday']),field('fcShowHeader','Kopfzeile anzeigen',True),field('fcShowWeekNumbers','Kalenderwochen anzeigen',False),field('fcAllowNavigation','Navigation erlauben',True)),group('Kalender Layout (erweitert)',field('fcEventBackgroundColor','Terminfarbe'),field('fcEventTextColor','Termintextfarbe'),field('fcEventFontSize','Termin-Schriftgröße',14),field('fcTodayBackgroundColor','Hintergrund heute'))],dict(width=500,height=300)))
    for slug,label,kind in [('top-app-bar','Top App Bar','navigation'),('masonry-views','Masonry Views','masonry'),('grid-views','Grid Views','grid'),('view-in-widget','Advanced View in Widget','view'),('view-in-widget8','Advanced View in Widget 8','view')]:
        groups=[group('Seiten',field('countViews','Anzahl Seiten',3,minimum=1,maximum=10),field('gridColumns','Spalten',2,minimum=1,maximum=12),field('viewGap','Abstand',12),field('childHeight','Höhe einer Ansicht',240),field('responsiveBreakpoint','Mobil-Breakpoint',600))]
        for i in range(10):
            groups.append(group(f'Ansicht [{i}]',field(f'targetPage{i}','Studio-Seite'),field(f'viewLabel{i}','Bezeichnung',f'Seite {i+1}'),field(f'viewValue{i}','Zustandswert',str(i)),field(f'viewHeight{i}','Höhe',240)))
        widgets.append(definition(slug,label,'layout',groups,dict(layoutKind=kind,width=600,height=400)))
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return manifest

if __name__=='__main__':
    print(f"{len(generate()['widgets'])} widget definitions generated")
