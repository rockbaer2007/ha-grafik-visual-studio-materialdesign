"""Additive Material 1.1 options. Existing field/default contracts are retained."""
import json
from pathlib import Path
from complete_package import field as base_field, group

ROOT = Path(__file__).resolve().parent

def field(key, *args, **kwargs):
    descriptor,value=base_field(key,*args,**kwargs)
    if ('color' in key.lower() and 'condition' not in key.lower() and key!='colorScheme') and isinstance(value,str):
        descriptor['type']='color'
    return descriptor,value

def upgrade():
    manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
    for widget in manifest['widgets']:
        kind = widget['defaults'].get('materialKind')
        additions = [group('Material-Sprache',field('materialLocale','Material-Sprache','auto',['auto','de','en','fr']))]
        def add(label, *fields):
            additions.append(group(label, *fields))
        if kind in {'button', 'switch', 'checkbox', 'slider', 'slider-round'}:
            add('Feedback und Sperre (erweitert)', field('vibrateOnMobilDevices','Auf mobilen Geräten vibrieren (ms)',0),field('clickSoundPlay','Klicksound abspielen',False),field('clickSoundVolume','Klicksound-Lautstärke',.5),field('lockEnabled','Sperre aktivieren',False),field('autoLockAfter','Automatisch sperren nach (s)',10),field('lockIcon','Sperrsymbol','mdi:lock'),field('lockIconSize','Sperrsymbolgröße',24),field('lockIconColor','Sperrsymbolfarbe'))
        if kind == 'button':
            add('Original Button (erweitert)',field('labelTrue','Beschriftung bei EIN'),field('labelFalse','Beschriftung bei AUS'),field('labelColorTrue','Textfarbe bei EIN'),field('labelColorFalse','Textfarbe bei AUS'),field('colorBgTrue','Hintergrund bei EIN'),field('colorBgFalse','Hintergrund bei AUS'),field('imageTrue','Symbol bei EIN'),field('imageTrueColor','Symbolfarbe bei EIN'),field('imageColor','Symbolfarbe'),field('iconHeight','Symbolhöhe',24),field('iconPosition','Symbolposition','left',['left','right']),field('distanceBetweenTextAndImage','Abstand Text und Symbol',8),field('alignment','Ausrichtung','center',['flex-start','center','flex-end']),field('openNewWindow','In neuem Fenster öffnen',False),field('pushButton','Taster-Modus',False),field('additionMin','Minimum'),field('additionMax','Maximum'))
            if widget['defaults'].get('actionKind') == 'multi-state':
                add('Mehrziel-Aktion',field('multiStateMode','Mehrziel-Modus','targets',['targets','cycle']),field('countTargets','Anzahl Ziele',1,minimum=1,maximum=10))
                for i in range(10):
                    add(f'Ziel [{i}]',field(f'targetEntityId{i}','Entität'),field(f'targetValue{i}','Schreibwert','on'),field(f'targetDelay{i}','Verzögerung (ms)',0,minimum=0,maximum=60000))
            if widget['defaults'].get('actionKind') == 'slider':
                add('Button-Regler',field('sliderShape','Reglerform','round',['round','linear']),field('sliderMin','Minimum',0),field('sliderMax','Maximum',100),field('sliderStep','Schrittweite',1))
        if kind in {'switch','checkbox'}:
            add('Original Schalter (erweitert)',field('labelTrue','Beschriftung bei EIN'),field('labelFalse','Beschriftung bei AUS'),field('labelPosition','Beschriftungsposition','right',['left','right']),field('labelColorTrue','Textfarbe bei EIN'),field('labelColorFalse','Textfarbe bei AUS'),field('valueFontSize','Schriftgröße',16),field('md3SwitchIcon','Symbol im Schalter',False),field('colorSwitchTrue','Schalterfarbe EIN'),field('colorSwitchTrack','Schalterspurfarbe'),field('colorSwitchThumb','Schaltergriff-Farbe'),field('colorCheckBox','Checkbox-Farbe'),field('colorCheckBoxBorder','Checkbox-Randfarbe'))
        if kind in {'slider','slider-round'}:
            add('Original Regler (erweitert)',field('reverseSlider','Regler umkehren',False),field('workingEntityId','Arbeitsstatus-Entität'),field('sendValueOnRelease','Erst beim Loslassen schreiben',True),field('tickLabels','Skalenbeschriftungen (Semikolon)'),field('valueLabelStyle','Wertdarstellung','value',['value','percent']),field('minDecimals','Mindestens Nachkommastellen',0),field('maxDecimals','Maximal Nachkommastellen',2),field('startAngle','Startwinkel',-90),field('arcLength','Bogenlänge',360,minimum=10,maximum=360),field('rtl','Gegen Uhrzeigersinn',False),field('roundSize','Kreisgröße',160),field('colorSliderBg','Innere Farbe'))
        if kind in {'progress','progress-circular'}:
            add('Original Fortschritt (erweitert)',field('progressCircularSize','Kreisgröße',90),field('progressCircularRotate','Drehung',0),field('innerColor','Innere Farbe'),field('colorProgress','Fortschrittsfarbe'),field('colorProgressBackground','Spurfarbe'),field('colorOneCondition','Erster Farbschwellwert'),field('colorOne','Erste Schwellenfarbe'),field('colorTwoCondition','Zweiter Farbschwellwert'),field('colorTwo','Zweite Schwellenfarbe'),field('valueLabelStyle','Wertdarstellung','value',['value','percent']),field('valueLabelCustom','Eigener Werttext'),field('valueLabelColor','Werttextfarbe'))
        if kind == 'value':
            add('Original Wertanzeige (erweitert)',field('minDecimals','Mindestens Nachkommastellen',1),field('maxDecimals','Maximal Nachkommastellen',1),field('valueFontSize','Wert Schriftgröße',16),field('valueFontColor','Wert Farbe'),field('textAlign','Textausrichtung','left',['left','center','right']),field('valueIcon','Symbol'),field('iconSize','Symbolgröße',24),field('iconColor','Symbolfarbe'),field('valueLink','Link (HTTP/HTTPS)'),field('openNewWindow','In neuem Fenster öffnen',False),field('valueCondition','Anzeigebedingung','',['','==','!=','<','<=','>','>=','exist','not exist']),field('valueConditionValue','Vergleichswert'),field('changeEffectEnabled','Änderungseffekt aktivieren',False),field('effectFontColor','Effektfarbe'),field('effectDuration','Effektdauer (ms)',1000))
            for g in widget['propertyGroups']:
                for f in g['fields']:
                    if f['key']=='valueType' and 'duration' not in f['options']:f['options'].append('duration')
        if kind == 'icon':add('Symbolmodus',field('iconMode','Symbolmodus','static',['static','state']))
        if kind == 'card':
            add('Original Karte (erweitert)',field('cardLayout','Kartenlayout','Basic',['Basic','BasicHeader','BasicHeaderOverlay','Horizontal']),field('cardSubtitle','Untertitel'),field('showTitle','Titel anzeigen',True),field('showText','Text anzeigen',True),field('titleFontSize','Titel-Schriftgröße',20),field('colorTitle','Titelfarbe'),field('colorBody','Inhaltsfarbe'),field('colorTitleSectionBackground','Titelhintergrund'),field('colorTextSectionBackground','Inhaltshintergrund'),field('imageRefreshSeconds','Bildaktualisierung (s)',0,minimum=0,maximum=3600))
        if kind in {'list','icon-list','alerts'}:
            add('Original Liste (erweitert)',field('listLayout','Listenlayout','standard',['standard','card']),field('itemBackgroundColor','Zeilenhintergrund'),field('listImageHeight','Symbolhöhe',24),field('showMaxAlerts','Maximale Meldungen',500),field('alertDense','Kompakte Meldungen',False),field('alertBorderColor','Meldungsrandfarbe'))
            for i in range(10):
                add(f'Zeilenzusätze [{i}]',field(f'rowSubLabel{i}','Zweiter Text'),field(f'rowTargetPage{i}','Zielseite'),field(f'rowLinkUrl{i}','Link (HTTP/HTTPS)'))
            for g in widget['propertyGroups']:
                for f in g['fields']:
                    if f['key'].startswith('rowControl'):
                        for value in ['navigation','link']:
                            if value not in f['options']:f['options'].append(value)
        if kind == 'table':
            add('Original Tabelle (erweitert)',field('tableLayout','Tabellenlayout','standard',['standard','card','cardOutlined']),field('fixedHeader','Feste Kopfzeile',False))
            for i in range(10):
                add(f'Spalte [{i}]',field(f'showColumn{i}','Spalte anzeigen',True),field(f'columnType{i}','Spaltentyp','text',['text','image']),field(f'columnWidth{i}','Breite',0),field(f'columnNoWrap{i}','Kein Zeilenumbruch',False),field(f'columnAlignment{i}','Textausrichtung','left',['left','center','right']),field(f'columnColor{i}','Textfarbe'),field(f'columnFontSize{i}','Schriftgröße',14),field(f'columnPrefix{i}','Präfix'),field(f'columnSuffix{i}','Suffix'),field(f'columnImageSize{i}','Bildgröße',32))
        if kind == 'chart':
            add('Original Diagramm (erweitert)',field('chartOrientation','Ausrichtung','vertical',['vertical','horizontal']),field('chartType','Diagrammtyp','pie' if widget['defaults'].get('chartKind')=='pie' else 'line',['line','bar','pie','doughnut']),field('doughnutCutOut','Donut-Innengröße (%)',50),field('colorScheme','Farbpalette','scrounger.pie'),field('barWidth','Balkenbreite',34),field('barBorderWidth','Randbreite',1),field('borderColor','Randfarbe'),field('showTooltip','Tooltip anzeigen',True),field('showValues','Wertlabels anzeigen',False),field('valuesFontColor','Werttextfarbe'),field('legendPosition','Legendenposition','bottom',['top','bottom','left','right']),field('legendFontSize','Legenden-Schriftgröße',14),field('axisFontSize','Achsen-Schriftgröße',12),field('axisLabelRotation','Achsenbeschriftung drehen',0),field('axisTitle','X-Achsentitel'),field('yAxisTitle','Y-Achsentitel'),field('pointSize','Punktgröße',3),field('animationDuration','Animation (ms)',300),field('xAxisType','X-Achsentyp','time' if widget['defaults'].get('chartKind')=='history' else 'category',['category','time']))
            add('Verlauf-Auswertung (erweitert)',field('historyAggregation','Aggregation','none',['none','average','min','max','sum','last']),field('historyBucketMinutes','Intervall (Minuten)',15,minimum=1,maximum=1440))
            for i in range(10):
                add(f'Datenreihenoptionen [{i}]',field(f'seriesAxis{i}','Y-Achse','left',['left','right','axis3','axis4']),field(f'seriesYMin{i}','Y-Minimum'),field(f'seriesYMax{i}','Y-Maximum'),field(f'seriesStack{i}','Stapel-ID'),field(f'seriesFill{i}','Linie füllen',False),field(f'seriesStepped{i}','Stufenlinie',False))
        if kind == 'layout':
            add('Original Ansichten (erweitert)',field('viewSelectionMode','Ansichtsauswahl','index' if widget['type'].endswith('widget8') else 'name',['mapped','name','index']),field('navigationMode','Navigationsmodus','state',['links','state']),field('persistent','Ansichten erhalten',False),field('renderAlways','Alle Ansichten vorladen',False),field('fadeInDuration','Einblendung (ms)',0),field('showViewTitle','Ansichtstitel anzeigen',True),field('hideErrorMessage','Hinweis ausblenden',False),field('mobileColumns','Mobile Spalten',1),field('tabletBreakpoint','Tablet-Breakpoint',1000),field('tabletColumns','Tablet-Spalten',2),field('drawerLayout','Drawer-Modus','auto',['auto','permanent','modal']),field('drawerWidth','Drawer-Breite',260),field('permanentIfResolutionHigherThan','Permanenter Drawer ab (px)',800),field('drawerHeader','Drawer-Kopfzeile'),field('showSelectedItemAsTitle','Auswahl als Titel',True),field('selectParentItems','Elterneinträge auswählbar',False),field('selectedItemNameEntityId','Entität für ausgewählten Namen'),field('topAppBarHeight','App-Bar-Höhe',64),field('colorTopAppBarBackground','App-Bar-Hintergrund'),field('colorTopAppBarTitle','App-Bar-Titelfarbe'),field('colorDrawerBackground','Drawer-Hintergrund'))
            for i in range(10):
                add(f'Ansichtsoptionen [{i}]',field(f'viewIcon{i}','Symbol'),field(f'viewParent{i}','Elternindex'),field(f'viewMinWidth{i}','Sichtbar ab Breite',0),field(f'viewMaxWidth{i}','Sichtbar bis Breite'),field(f'viewVisibilityEntityId{i}','Sichtbarkeits-Entität'),field(f'viewVisibilityCondition{i}','Bedingung','==',['==','!=','<','<=','>','>=','exist','not exist','consist','not consist']),field(f'viewVisibilityValue{i}','Vergleichswert'))
        if kind == 'input':add('Original Eingabe (erweitert)',field('inputMask','Eingabemaske'),field('appendIcon','Inneres angehängtes Symbol'),field('appendIconSize','Symbolgröße',20),field('appendIconColor','Symbolfarbe'))
        if kind == 'calendar':
            add('Original Kalender (erweitert)',field('fcShowNowIndicator','Aktuelle Zeit anzeigen',False),field('fcNowIndicatorColor','Farbe aktuelle Zeit'),field('fcDayFontSize','Tag-Schriftgröße',14),field('fcDayTextColor','Tag-Textfarbe'),field('fcDayOutsideMonthTextColor','Textfarbe außerhalb des Monats'),field('fcBorderColor','Randfarbe'),field('fcShowBorders','Ränder anzeigen',True),field('fcTimeStart','Zeitachse von','00:00:00'),field('fcTimeEnd','Zeitachse bis','24:00:00'),field('fcTimeInterval','Zeitraster (Minuten)',30))
        known = {f['key'] for g in widget['propertyGroups'] for f in g['fields']}
        for label, fields in additions:
            remaining = [f for f in fields if f[0]['key'] not in known]
            if not remaining:continue
            widget['propertyGroups'].append({'label':label,'fields':[f[0] for f in remaining]})
            for descriptor, value in remaining:
                key=descriptor['key'];widget['defaults'].setdefault(key,value);known.add(key)
    for widget in manifest['widgets']:
        extras=[]
        kind=widget['defaults'].get('materialKind')
        if kind in {'list','icon-list','alerts'}:extras.append(field('listTextIsHtml','Bereinigtes HTML in Listentexten',False))
        if kind in {'button','switch','checkbox','slider','slider-round'}:
            extras += [field('lockIconTop','Sperrsymbol oben (px)',0),field('lockIconLeft','Sperrsymbol links (px)',0)]
        if kind in {'button','switch','checkbox'}:
            extras += [field('toggleType','Art der Umschaltung','value',['value','boolean']),field('stateIfNotTrueValue','Zustand bei anderem Wert','off',['off','on'])]
        if extras:
            known={f['key'] for g in widget['propertyGroups'] for f in g['fields']}
            extra_fields=[item for item in extras if item[0]['key'] not in known]
            if extra_fields:
                widget['propertyGroups'].append({'label':'Original Details (erweitert)','fields':[f for f,v in extra_fields]})
                for descriptor,value in extra_fields:widget['defaults'][descriptor['key']]=value
        for group_data in widget['propertyGroups']:
            for descriptor in group_data['fields']:
                if descriptor['key']=='valueCondition':
                    descriptor['options']=['always','==','!=','<','<=','>','>=','exist','not exist']
                    widget['defaults']['valueCondition']='always'
    manifest['name']='Material Design'
    manifest['version']='1.1.0'
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return manifest

if __name__=='__main__':
    print(f"{len(upgrade()['widgets'])} compatible widget definitions upgraded")
