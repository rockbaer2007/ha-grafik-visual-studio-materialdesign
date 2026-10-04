"""Convert the upstream preview glyph mapping to inert, local MDI SVG assets.

Usage: python import_preview_icons.py upstream/mdi-font.css studio/mdi-icons.json
The inputs are read as data; no upstream code is executed.
"""
import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
CODES = dict(zip(
    ['color-schemes','dialog','dialog-iframe','autocomplete','select','input',
     'checkbox','switch','slider','slider-round','progress','progress-circular',
     'value','card','icon','installed-version','list','icon-list','table','alerts',
     'chart-bar','chart-pie','chart-json','chart-line-history','calendar','top-app-bar',
     'masonry-views','grid-views','view-in-widget','view-in-widget8'],
    ['F03D8','F10AC','F10AC','F13B8','F1400','F060E','F0135','F0A1A','F1542',
     'F04C5','F03F0','F07AF','F0199','F0B78','F0976','F02FD','F0279','F0572',
     'F04EB','F0026','F0128','F012B','F154E','F012A','F00ED','F06FC','F056E',
     'F11D9','F056A','F056A']))
BUTTONS = {'addition':'F0415','link':'F0337','navigation':'F0390',
           'state':'F03EB','multi-state':'F1144','toggle':'F0521','slider':'F1543'}

def generate(css_path, mdi_path):
    css = Path(css_path).read_text(encoding='utf-8')
    names = {code:name for name,code in re.findall(
        r'\.mdi-([a-z0-9-]+)::before\{content:"\\(F[0-9A-F]+)"\}', css)}
    paths = {icon['name']:icon['path'] for icon in json.loads(
        Path(mdi_path).read_text(encoding='utf-8'))['icons']}
    manifest = json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    mapping = {}
    for widget in manifest['widgets']:
        slug = widget['type'].split('/')[-1]
        if 'button-' in slug:
            action = slug.removeprefix('icon-').removeprefix('button-').removesuffix('-vertical')
            code = BUTTONS[action]
        else:
            code = CODES[slug]
        name = names[code]
        filename = f'icons/preview-{name}.svg'
        svg = ET.Element('svg', {'xmlns':'http://www.w3.org/2000/svg',
                                'viewBox':'0 0 44 44','width':'44','height':'44'})
        ET.SubElement(svg,'rect',{'width':'44','height':'44','rx':'8','fill':'#ffffff'})
        ET.SubElement(svg,'path',{'d':paths[name],'fill':'#44739e',
                                 'transform':'translate(11 11) scale(0.916666667)'})
        (ROOT/filename).write_text(ET.tostring(svg,encoding='unicode')+'\n',encoding='utf-8')
        widget['icon'] = filename
        mapping[slug] = filename
    (ROOT/'icons/catalog.json').write_text(json.dumps(mapping,indent=2)+'\n',encoding='utf-8')
    manifest['version'] = '1.0.1'
    (ROOT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"Mapped {len(mapping)} widgets to {len(set(mapping.values()))} original MDI preview icons.")

if __name__ == '__main__':
    generate(*sys.argv[1:])
