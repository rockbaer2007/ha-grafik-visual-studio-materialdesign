"""Build the data-only Material Design Studio widget package."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent

def build():
    target = ROOT / 'dist' / 'ugso.materialdesign-0.1.0.wg'
    target.parent.mkdir(exist_ok=True)
    with ZipFile(target, 'w') as archive:
        for name in ['manifest.json', 'icons/palette.svg', 'LICENSE.txt', 'README.md']:
            info = ZipInfo(name, (2026, 10, 4, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, (ROOT / name).read_bytes())
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    (target.parent / 'SHA256SUMS').write_text(f'{digest}  {target.name}\n', encoding='utf-8')
    return target

if __name__ == '__main__':
    print(build())
