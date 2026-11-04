"""Make transparent versions of the official logo (logo.jpg) for dark backgrounds.

Outputs:
  assets/logo-gold.png   full logo (emblem + Arabic + English), transparent
  assets/logo-mark.png   the "A" emblem only, transparent

Run:  python tools/make_logo.py
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
src = Image.open(ROOT / "logo.jpg").convert("RGB")


def to_transparent(im: Image.Image) -> Image.Image:
    """Keep the gold pixels, turn the dark background transparent."""
    out = Image.new("RGBA", im.size)
    px_in, px_out = im.load(), out.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = px_in[x, y]
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            # gold has much more red than blue; dark textured background does not
            warmth = r - b
            a = max(0, min(255, int((lum - 45) * 2.2))) if warmth > 25 else 0
            px_out[x, y] = (r, g, b, a)
    return out.crop(out.getbbox())


full = to_transparent(src.crop((60, 150, 650, 640)))
full.save(ROOT / "assets" / "logo-gold.png", optimize=True)

mark = to_transparent(src.crop((200, 160, 500, 420)))
mark.save(ROOT / "assets" / "logo-mark.png", optimize=True)

print("logo-gold", full.size, "logo-mark", mark.size)
