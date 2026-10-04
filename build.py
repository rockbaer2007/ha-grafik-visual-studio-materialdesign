"""Build the data-only Material Design Studio widget package."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent

def build():
    version = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))['version']
    target = ROOT / 'dist' / f'ugso.materialdesign-{version}.wg'
    target.parent.mkdir(exist_ok=True)
    with ZipFile(target, 'w') as archive:
        manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
        icons = {manifest['icon'], *(widget['icon'] for widget in manifest['widgets'])}
        for name in ['manifest.json', *sorted(icons), 'LICENSE.txt', 'README.md']:
            info = ZipInfo(name, (2026, 10, 4, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            body = (ROOT / name).read_text(encoding='utf-8')
            if name == 'manifest.json':
                body = json.dumps(json.loads(body), ensure_ascii=False, separators=(',', ':'))
            archive.writestr(info, body.encode('utf-8'))
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    (target.parent / 'SHA256SUMS').write_text(f'{digest}  {target.name}\n', encoding='utf-8')
    return target

if __name__ == '__main__':
    print(build())
