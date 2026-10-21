#!/usr/bin/env python3
"""PRUEBA: OQUVA + manual elvo·. Titular Fraunces Light (manual), etiqueta Hanken en mayúsculas con
tracking +0.2em y filete de 1px (OQUVA, pero sin cajas: el manual pide filetes), línea de datos
verificados en mayúsculas tracked. Escribe en instagram/ia/final-manual/."""
import importlib.util
import sys
from pathlib import Path

from PIL import Image, ImageDraw

here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cig", here / "compose-ig.py")
cig = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cig)
W, H, M = cig.W, cig.H, cig.M

DATA = {  # solo claims de la ficha verificada / alivio-copy.md
    "p19": "SIN ELECTRICIDAD  ·  SIN CONEXIÓN AL CAÑO",
    "p21": "SE LLENA CON UNA JARRA  ·  PURIFICA POR GRAVEDAD",
    "p14": "TENDENCIA ALCALINA  ·  UN VASO EN 5 SEGUNDOS",
}


def compose(i):
    head, prod, tone, pos = cig.TEXTS[i]
    src = cig.latest(i)
    im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    ink, soft = cig.INK[tone]
    fs = cig.SIZE.get(i, 64)
    hf = cig.font("Fraunces-Light.ttf", fs)
    lf = cig.font("HankenGrotesk-Medium.ttf", 18)
    y = int(H * 0.105)
    if prod:
        if prod.startswith("!"):
            cig.tracked(d, (M, y), prod[1:], lf, soft, 4)
        else:
            x = cig.tracked(d, (M, y), "elvo·", cig.font("HankenGrotesk-Regular.ttf", 18), soft, 1)
            cig.tracked(d, (x + 12, y), prod, lf, soft, 4)
        d.line([(M, y + 36), (M + 64, y + 36)], fill=soft, width=1)
        y += 62
    for part in head.split("\n"):
        for ln in cig.wrap(d, part, hf, W - 2 * M - 120):
            d.text((M, y), ln, font=hf, fill=ink)
            y += int(fs * 1.14)
    if i in DATA:
        y += 22
        d.line([(M, y), (W - M, y)], fill=soft, width=1)
        cig.tracked(d, (M, y + 16), DATA[i], cig.font("HankenGrotesk-Medium.ttf", 16), soft, 3.2)
    out = src.parent / "final-manual"
    out.mkdir(exist_ok=True)
    dest = out / f"{src.stem}_1080x1350.png"
    im.save(dest, optimize=True)
    print("✓", dest.relative_to(cig.project_root()))


for i in sys.argv[1:]:
    compose(i)
