from pathlib import Path
import base64, io, zipfile, shutil

ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT/'tmp'/'am-galleries'
TARGETS={
    'am1': ROOT/'assets'/'mockups'/'am-1',
    'am850': ROOT/'assets'/'mockups'/'am-850',
}

changed=False
for key,target in TARGETS.items():
    parts=sorted(TMP.glob(f'{key}.part*')) if TMP.exists() else []
    if not parts:
        continue
    data=''.join(p.read_text().strip() for p in parts)
    raw=base64.b64decode(data)
    target.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        for name in z.namelist():
            if not name.endswith('.webp'):
                continue
            (target/name).write_bytes(z.read(name))
    for p in parts:
        p.unlink()
    changed=True

if TMP.exists() and not any(TMP.iterdir()):
    TMP.rmdir()
print('installed' if changed else 'nothing to install')
