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

# id: (titular, producto de la etiqueta o None, tono, posición)
TEXTS = {
    "p18": ("El agua es el primer ingrediente.", "NATIVO", "light", "top"),
    "p16": ("Lo que se aporta.", None, "dark", "top"),
    "p01": ("Lo que el agua toca.", None, "light", "top"),
    "p19": ("Agua de reserva en casa.", "ALIVIO", "light", "top"),
    "p21": ("Un alivio cuando no hay agua.", "ALIVIO", "light", "top"),
    "p22": ("El té también empieza en el agua.", None, "light", "top"),
    "p20": ("Cinco etapas.", None, "dark", "top"),
    "p23": ("Fría o caliente, un solo gesto.", "CERO", "light", "top"),
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
    hf, lf = font("Fraunces-Light.ttf", 64), font("HankenGrotesk-Medium.ttf", 19)
    lines = wrap(d, head, hf, W - 2 * M - 120)
    lh = int(64 * 1.14)
    block = (50 if prod else 0) + len(lines) * lh
    y = int(H * 0.115) if pos == "top" else int(H * 0.885) - block
    if prod:
        x = tracked(d, (M, y), "elvo·", font("HankenGrotesk-Regular.ttf", 19), soft, 1)
        tracked(d, (x + 12, y), prod, lf, soft, 4)
        y += 50
    for ln in lines:
        d.text((M, y), ln, font=hf, fill=ink)
        y += lh
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
