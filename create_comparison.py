"""Generate a Studio project for comparing all package widgets without HA writes."""
import json
from pathlib import Path
from complete_package import ROOT

def comparison():
    manifest = json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    pages=[]
    for start in range(0,len(manifest['widgets']),6):
        widgets=[]
        for i,definition in enumerate(manifest['widgets'][start:start+6]):
            w=dict(definition['defaults'],type=definition['type'],id=f'material-proof-{start+i}',name=definition['label'],x=30+(i%3)*340,y=30+(i//3)*330,width=310,height=290,visible=True)
            if w.get('materialKind') in {'input','select','autocomplete'}:
                w['labelText']=definition['label'];w['inputLabelText']=definition['label'];w['state']='';w['height']=130
            if w.get('materialKind')=='layout':
                w['targetPage0']='reference-page'
                w['state']='0'
                w['countViews']=1
            if w['type'].endswith('/dialog'):
                w['targetPage']='reference-page'
            if w['type'].endswith('/dialog-iframe'):
                w['src']='https://example.com/'
            if w.get('materialKind')=='button':
                w['targetPage']='reference-page';w['linkUrl']='https://example.com/'
            if w.get('materialKind') in {'list','icon-list','alerts'}:
                w['dataJson']='[{"label":"Erster Eintrag","value":"Bereit","icon":"mdi:check-circle"},{"label":"Zweiter Eintrag","value":"Aus","icon":"mdi:lightbulb-outline"}]'
            if w.get('materialKind')=='calendar':
                w['eventJson']='[{"title":"Vergleichstermin","start":"2026-10-04T14:00:00","end":"2026-10-04T15:00:00"}]'
            if w.get('chartKind')=='history':
                w['seriesData0']='[{"x":"10:00","y":20},{"x":"11:00","y":21},{"x":"12:00","y":19}]'
            widgets.append(w)
        pages.append(dict(id=f'compare-{start//6+1}',name=f'MaterialDesign {start+1}–{min(start+6,len(manifest["widgets"]))}',visible=True,page=dict(preset='custom',width=1080,height=720,background='#202124',theme='dark',enabledPropertyGroups={}),widgets=widgets))
    value_definition=next(w for w in manifest['widgets'] if w['type'].endswith('/value'))
    reference=dict(value_definition['defaults'],id='reference-text',type=value_definition['type'],name='Referenz',x=24,y=24,width=450,height=100,labelText='Studio-Referenzseite',valueType='text',state='Ansicht erfolgreich geladen',visible=True)
    pages.append(dict(id='reference-page',name='Referenzansicht',visible=True,page=dict(preset='custom',width=600,height=300,background='#eef6fa',theme='light'),widgets=[reference]))
    return dict(schemaVersion=2,name='MaterialDesign Widgetvergleich',currentPageId=pages[0]['id'],settings=dict(autoSave=False),pages=pages)

if __name__=='__main__':
    target=ROOT/'comparison/materialdesign-widgetvergleich.json'
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(comparison(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    checklist=['# MaterialDesign: Widgetvergleich','', f"Paket {manifest['version']} / Studio ab 0.1.216. Alle Einträge sind im Vergleichsprojekt enthalten.", '', 'Die Spalten bleiben bis zum gemeinsamen Vergleich offen. Prüfen: kompakte und', 'erweiterte Eigenschaften, Hell/Dunkel/Klassisch/Material 3, Zustandswechsel und Runtime.', '', '| Nr. | Widget | Vergleichsseite | Optik | Optionen | Funktion |', '| --- | --- | --- | --- | --- | --- |']
    for i,w in enumerate(manifest['widgets']):
        checklist.append(f'| {i+1} | {w["label"]} | {i//6+1} | offen | offen | offen |')
    checklist.extend(['','Die erste automatische Prüfung bestätigt Paketvertrag, Darstellung aller Varianten,','Autocomplete-Auswahl und gemeinsame Renderer-/Recorder-Logik. Sie ersetzt noch keinen','direkten Vergleich mit allen Originaleinstellungen oder einen Test mit echten HA-Entitäten.',''])
    (target.parent/'VERGLEICH.md').write_text('\n'.join(checklist),encoding='utf-8')
    print(target)
