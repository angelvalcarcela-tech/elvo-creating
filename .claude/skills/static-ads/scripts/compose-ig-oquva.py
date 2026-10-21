#!/usr/bin/env python3
"""PRUEBA: sistema tipográfico y de maquetación completo de OQUVA aplicado a elvo·.
Fila superior de microtexto (01 // ... → ...) con filete de 1px, titular Outfit Bold en mayúsculas,
línea de apoyo Outfit Light, cápsulas con contorno. Paleta OQUVA para texto: #010A15, #FAFAFA, azul #3355FF.
Escribe en instagram/ia/final-oquva/. No toca las láminas actuales."""
import importlib.util
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cig", here / "compose-ig.py")
cig = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cig)
W, H, M = cig.W, cig.H, cig.M
BLUE = "#3355FF"
INK = {"light": ("#010A15", "#4D5560"), "dark": ("#FAFAFA", "#B8C2CC")}

# id: (num, tema, flujo, apoyo, cápsulas)
OQ = {
    "p19": ("01", "AGUA DE RESERVA", "AGUA → BIDÓN → VASO", "Se llena con una jarra. Sin electricidad, sin conexión al caño.", ["SIN ELECTRICIDAD", "SIN CONEXIÓN AL CAÑO"]),
    "p21": ("02", "ELVO· ALIVIO", "JARRA → BIDÓN → VASO", "Alivio 16 y Alivio 22: elige cuánto alivio quieres tener en casa.", ["ALIVIO 16", "ALIVIO 22"]),
    "p16": ("03", "FORMULACIÓN", "AGUA → MINERAL → VASO", "elvo· Vivo aporta magnesio al vaso.", ["APORTA MAGNESIO"]),
    "p05": ("04", "PRUEBA", "PRUEBA → DECISIÓN", "Si no encaja en tu caño, te devolvemos tu dinero.", []),
    "p23": ("05", "ELVO· CERO", "FRÍA → CALIENTE", "", []),
    "p01": ("06", "LO QUE EL AGUA TOCA", "AGUA → PIEL", "", []),
}


def F(n, s):
    return ImageFont.truetype(str(cig.project_root() / cig.BRAND / "fonts" / n), s)


def words(d, xy, text, f, fill, track=0, gap=16):
    x, y = xy
    for w in text.split(" "):
        x = cig.tracked(d, (x, y), w, f, fill, track) + gap
    return x


def width(d, text, f, track=0, gap=16):
    return sum(sum(d.textlength(c, font=f) + track for c in w) + gap for w in text.split(" ")) - gap


def compose(i):
    head, _, tone, _ = cig.TEXTS[i]
    num, tema, flujo, apoyo, pills = OQ[i]
    src = cig.latest(i)
    im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    ink, soft = INK[tone]
    mf = F("Inter-Regular.ttf", 15)
    y = int(H * 0.10)
    x = cig.tracked(d, (M, y), f"{num} // ", mf, BLUE if tone == "light" else "#8FA6FF", 3)
    cig.tracked(d, (x, y), tema, mf, soft, 3)
    wf = width(d, flujo, mf, 3, 12)
    words(d, (W - M - wf, y), flujo, mf, soft, 3, 12)
    d.line([(M, y + 30), (W - M, y + 30)], fill=soft, width=1)
    y += 62
    hf = F("Outfit-Bold.ttf", 60)
    lines, cur = [], ""
    for w in head.upper().replace("\n", " ").split():
        t = f"{cur} {w}".strip()
        if width(d, t, hf, 0, 18) <= W - 2 * M - 40 or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    for ln in lines:
        words(d, (M, y), ln, hf, ink, 0, 18)
        y += 68
    if apoyo:
        y += 8
        sf = F("Outfit-Light.ttf", 26)
        for ln in cig.wrap(d, apoyo, sf, 620):
            d.text((M, y), ln, font=sf, fill=soft)
            y += 36
    x = M
    y += 14
    pf = F("Inter-Regular.ttf", 15)
    for p in pills:
        tw = width(d, p, pf, 2, 9)
        d.rounded_rectangle([x, y, x + tw + 40, y + 42], radius=21, outline=soft, width=2)
        words(d, (x + 20, y + 11), p, pf, ink, 2, 9)
        x += tw + 54
    out = src.parent / "final-oquva"
    out.mkdir(exist_ok=True)
    dest = out / f"{src.stem}_1080x1350.png"
    im.save(dest, optimize=True)
    print("✓", dest.relative_to(cig.project_root()))


for i in sys.argv[1:]:
    compose(i)
