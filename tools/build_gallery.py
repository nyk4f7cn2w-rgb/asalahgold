#!/usr/bin/env python3
"""Rebuild the gallery markup in index.html from gallery/catalog.json.

To add a new photo:
  1. upload it to gallery/
  2. add an entry to gallery/catalog.json  (n, file, cat, latest, w, h, color)
     cat is one of: necklaces, sets, bangles, bullion, showroom
  3. python3 tools/optimize_images.py && python3 tools/build_gallery.py
  4. bump the build number (tools/stamp_version.sh)
"""
import json, os, re, html
CAT = {'necklaces': ('قلادة ذهب', 'القلائد'), 'sets': ('طقم ذهب', 'الأطقم'), 'bangles': ('أساور ذهب', 'الأساور'),
       'bullion': ('سبائك', 'السبائك'), 'showroom': ('من صالة عرض', 'صالة العرض')}
items = json.load(open('gallery/catalog.json', encoding='utf-8'))
out = []
for it in items:
    n = f"{it['n']:02d}"; stem = os.path.splitext(it['file'])[0]
    alt = f"{CAT[it['cat']][0]} أصالة الذهب — قطعة Nº {n}"
    w, h = it['w'], it['h']; lw = 640 if w <= h else 640; lh = round(lw * h / w)
    new = '<span class="new">NEW</span>' if it['latest'] else ''
    out.append(
        f'<figure class="piece" id="p{n}" data-n="{n}" data-cat="{it["cat"]}" data-latest="{1 if it["latest"] else 0}" data-stem="{stem}" data-file="{it["file"]}" style="--ar:{w}/{h};--ph:{it["color"]}">'
        f'<button class="piece-btn" type="button" aria-label="عرض القطعة Nº {n}">{new}'
        f'<img src="gallery/opt/{stem}-640.webp" width="{lw}" height="{lh}" loading="lazy" decoding="async" alt="{html.escape(alt)}">'
        f'<span class="piece-view"><svg aria-hidden="true"><use href="#i-zoom"/></svg></span></button>'
        f'<figcaption><span class="n">Nº {n}</span><span class="cat">{CAT[it["cat"]][1]}</span></figcaption></figure>')
src = open('index.html', encoding='utf-8').read()
src = re.sub(r'<!--GALLERY-->.*?<!--/GALLERY-->', '<!--GALLERY-->\n' + '\n'.join(out) + '\n<!--/GALLERY-->', src, flags=re.S)
open('index.html', 'w', encoding='utf-8').write(src)
print(len(out), 'pieces written')
