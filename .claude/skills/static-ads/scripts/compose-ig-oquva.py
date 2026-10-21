#!/usr/bin/env python3
"""PRUEBA de estilo tipográfico tipo OQUVA: titular en mayúsculas (Outfit Bold), etiquetas tracked
(Inter), cápsulas con contorno fino. Escribe en instagram/ia/final-oquva/. No toca las láminas actuales."""
import importlib.util
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cig", here / "compose-ig.py")
cig = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cig)

W, H, M = cig.W, cig.H, cig.M
PILLS = {
    "p18": ["SIN ELECTRICIDAD", "INSTALACIÓN EN 5 MINUTOS"],
    "p05": ["30 DÍAS DE PRUEBA"],
}


def pill(d, x, y, text, f, ink):
    tw = sum(d.textlength(c, font=f) + 2 for c in text)
    d.rounded_rectangle([x, y, x + tw + 44, y + 46], radius=23, outline=ink, width=2)
    cig.tracked(d, (x + 22, y + 12), text, f, ink, 2)
    return x + tw + 44 + 14


def compose(i):
    head, prod, tone, pos = cig.TEXTS[i]
    src = cig.latest(i)
    im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    ink, soft = cig.INK[tone]
    F = lambda n, s: ImageFont.truetype(str(cig.project_root() / cig.BRAND / "fonts" / n), s)
    hf, lf, pf = F("Outfit-Bold.ttf", 54), F("Inter-Regular.ttf", 17), F("Inter-Regular.ttf", 16)
    y = int(H * 0.105)
    if prod:
        txt = prod[1:] if prod.startswith("!") else f"elvo· {prod}"
        cig.tracked(d, (M, y), "01 // " + txt if False else txt, lf, soft, 4)
        d.line([(M, y + 34), (M + 56, y + 34)], fill=soft, width=1)
        y += 56
    for part in head.split("\n"):
        for ln in cig.wrap(d, part.upper(), hf, W - 2 * M - 80):
            d.text((M, y), ln, font=hf, fill=ink)
            y += 62
    x = M
    y += 14
    for p in PILLS.get(i, []):
        if x + 300 > W - M:
            x, y = M, y + 58
        x = pill(d, x, y, p, pf, soft if tone == "dark" else "#4A4740")
    out = src.parent / "final-oquva"
    out.mkdir(exist_ok=True)
    dest = out / f"{src.stem}_1080x1350.png"
    im.save(dest, optimize=True)
    print("✓", dest.relative_to(cig.project_root()))


for i in sys.argv[1:]:
    compose(i)
