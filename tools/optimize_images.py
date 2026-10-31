#!/usr/bin/env python3
"""Generate fast-loading WebP copies of every photo in gallery/.
Originals are never modified or deleted. Run from the repo root:
    python3 tools/optimize_images.py
Outputs gallery/opt/<name>-640.webp and gallery/opt/<name>-1600.webp
"""
import glob, os
from PIL import Image, ImageOps
SIZES = {640: 74, 1600: 82}
os.makedirs('gallery/opt', exist_ok=True)
for src in sorted(glob.glob('gallery/*.*')):
    if src.endswith('.gitkeep'):
        continue
    stem = os.path.splitext(os.path.basename(src))[0]
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    for w, q in SIZES.items():
        out = f'gallery/opt/{stem}-{w}.webp'
        if os.path.exists(out) and os.path.getmtime(out) > os.path.getmtime(src):
            continue
        c = im.copy()
        c.thumbnail((w, w * 2), Image.LANCZOS)
        c.save(out, 'WEBP', quality=q, method=6)
# logo / icons
logo = Image.open('logo.jpg').convert('RGB')
for s in (64, 192, 512):
    l = logo.copy(); l.thumbnail((s, s), Image.LANCZOS)
    canvas = Image.new('RGB', (s, s), (12, 9, 10)); canvas.paste(l, ((s - l.width) // 2, (s - l.height) // 2))
    canvas.save(f'assets/icon-{s}.png', optimize=True)
l = logo.copy(); l.thumbnail((320, 320), Image.LANCZOS); l.save('assets/logo-320.webp', 'WEBP', quality=88)
c = Image.new('RGB', (180, 180), (12, 9, 10)); t = logo.copy(); t.thumbnail((180, 180)); c.paste(t, ((180 - t.width) // 2, (180 - t.height) // 2)); c.save('assets/apple-touch-icon.png')
print('done')
