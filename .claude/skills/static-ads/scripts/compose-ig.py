#!/usr/bin/env python3
"""Compone titular y etiqueta sobre las imágenes de IA sin texto (Fraunces Light + Hanken Grotesk).

Uso: python3 .claude/skills/static-ads/scripts/compose-ig.py <id> [<id> ...]
Lee la última versión de instagram/ia/<id>_vN.png y escribe instagram/ia/final/<id>_1080x1350.png.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import project_root  # noqa: E402

BRAND = "brands/elvo/brand-identity"
W, H = 1080, 1350
M = int(W * 0.08)
INK = {"light": ("#2B2E2D", "#6B665D"), "dark": ("#EAE7E0", "#9A948A")}  # (titular, etiqueta)

SUB = {"p05": "Si no encaja en tu caño, te devolvemos tu dinero."}
LOGO = {"p02"}  # piezas con logo elvo· abajo a la izquierda
SIZE = {"p18": 52, "p14": 48}  # tamaño del titular si el default roza el producto

# id: (titular, producto de la etiqueta o None, tono, posición)
TEXTS = {
    "p18": ("El agua es el primer ingrediente.", "NATIVO", "light", "top"),
    "p16": ("Lo que se aporta.", None, "dark", "top"),
    "p01": ("Lo que el agua toca.", None, "light", "top"),
    "p19": ("Agua de reserva en casa.", "ALIVIO", "light", "top"),
    "p21": ("Un alivio cuando no hay agua.", "ALIVIO", "light", "top"),
    "p22": ("El té también\nempieza en el agua.", None, "light", "top"),
    "p20": ("Cinco etapas.", None, "dark", "top"),
    "p23": ("Fría o caliente, un solo gesto.", "CERO", "light", "top"),
    "p02": ("", None, "dark", "top"),
    "p04": ("Lo simple, bien hecho.", None, "light", "top"),
    "p05": ("30 días de prueba.", None, "light", "top"),
    "p07": ("18 meses.", "!NÚCLEO DE REPUESTO", "dark", "top"),
    "p08": ("Un vaso antes de dormir.", None, "light", "top"),
    "p09": ("Agua purificada,\ndirecto de tu caño.", None, "light", "top"),
    "p10": ("¿Qué necesitas?", None, "light", "top"),
    "p11": ("El agua primero.", None, "dark", "top"),
    "p14": ("Agua con magnesio,\ndirecto de tu caño.", "VIVO", "light", "top"),
    "p12": ("Agua como ritual.", None, "light", "top"),
    "p13": ("Vida sin prisa.", None, "light", "top"),
    "p15": ("Lo que se retira.", None, "dark", "top"),
    "p17": ("La primera decisión del día.", None, "light", "top"),
    "pB1": ("elvo· es una marca peruana.", "!LIMA · PERÚ", "light", "top"),
    "pB2": ("Un purificador para cada lugar donde el agua te toca.", None, "light", "top"),
    "pB3": ("Materia mineral, luz serena.", None, "dark", "top"),
    "pB4": ("Lo que nos guía.", None, "dark", "top"),
    "pB6": ("Consulta, no venta.", None, "light", "top"),
    "p24": ("Fría. Caliente.", None, "dark", "top"),
}


def font(name, size):
    return ImageFont.truetype(str(project_root() / BRAND / "fonts" / name), size)


def tracked(d, xy, text, f, fill, track):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + track
    return x


def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = f"{cur} {w}".strip()
        if d.textlength(t, font=f) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + [cur]


def latest(i):
    ia = project_root() / BRAND / "instagram" / "ia"
    c = sorted(ia.glob(f"{i}_v*.png"), key=lambda p: int(p.stem.split("_v")[1]))
    if not c:
        sys.exit(f"No hay imagen para {i}")
    return c[-1]


def compose(i):
    head, prod, tone, pos = TEXTS[i]
    src = latest(i)
    im = Image.open(src).convert("RGB").resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    ink, soft = INK[tone]
    fs = SIZE.get(i, 64)
    hf, lf = font("Fraunces-Light.ttf", fs), font("HankenGrotesk-Medium.ttf", 19)
    lines = [w for part in head.split("\n") for w in wrap(d, part, hf, W - 2 * M - 120)]
    lh = int(fs * 1.14)
    lines = [ln for ln in lines if ln]
    block = (50 if prod else 0) + len(lines) * lh
    y = int(H * 0.115) if pos == "top" else int(H * 0.885) - block
    if prod and prod.startswith("!"):
        tracked(d, (M, y), prod[1:], lf, soft, 4)
        y += 50
    elif prod:
        x = tracked(d, (M, y), "elvo·", font("HankenGrotesk-Regular.ttf", 19), soft, 1)
        tracked(d, (x + 12, y), prod, lf, soft, 4)
        y += 50
    for ln in lines:
        d.text((M, y), ln, font=hf, fill=ink)
        y += lh
    if i in SUB:
        sf = font("HankenGrotesk-Regular.ttf", 27)
        y += 14
        for ln in wrap(d, SUB[i], sf, W - 2 * M - 160):
            d.text((M, y), ln, font=sf, fill=soft if tone == "dark" else "#4A4740")
            y += 36
    if i in LOGO:
        lg = font("Fraunces-Light.ttf", 44)
        ly = int(H * 0.885) - 44
        d.text((M, ly), "elvo", font=lg, fill=ink)
        x0 = M + d.textlength("elvo", font=lg) + 5
        d.ellipse([x0, ly + 27, x0 + 10, ly + 37], fill="#82C3C4")
        d.polygon([(x0 + 5, ly + 12), (x0 + 1, ly + 28), (x0 + 9, ly + 28)], fill="#82C3C4")
    out = src.parent / "final"
    out.mkdir(exist_ok=True)
    dest = out / f"{src.stem}_1080x1350.png"
    im.save(dest, optimize=True)
    print("✓", dest.relative_to(project_root()))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for i in sys.argv[1:]:
        compose(i)
