#!/usr/bin/env python3
"""Arma la grilla de 30 publicaciones (3 columnas, lo más nuevo arriba a la izquierda)."""
import glob
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import project_root  # noqa: E402

IG = project_root() / "brands/elvo/brand-identity/instagram"
FIN = IG / "ia" / "final"
ORDER = ["pB1", "pB2", "pB3", "pB4", "B5", "pB6", "p01", "p02", "p03", "p04", "p05", "p06", "p07", "p08", "p09",
         "p10", "p11", "p12", "p13", "p14", "p15", "p16", "p17", "p18", "p19", "p20", "p21", "p22", "p23", "p24"]
TW, TH, GAP = 360, 450, 3


def tile(i):
    if i == "B5":
        return Image.open(IG / "tipograficas/p31-01.png").convert("RGB")
    if i == "p06":
        return Image.open(IG / "tipograficas/p19-01.png").convert("RGB")
    if i == "p03":  # fotos reales de instalación aún no disponibles
        im = Image.new("RGB", (1080, 1350), "#EAE7E0")
        d = ImageDraw.Draw(im)
        f = ImageFont.truetype(str(project_root() / "brands/elvo/brand-identity/fonts/Fraunces-Light.ttf"), 64)
        d.text((86, 540), "Instálalo tú.\n5 minutos.", font=f, fill="#2B2E2D", spacing=10)
        g = ImageFont.truetype(str(project_root() / "brands/elvo/brand-identity/fonts/HankenGrotesk-Regular.ttf"), 22)
        d.text((86, 1180), "FOTO REAL PENDIENTE", font=g, fill="#6B665D")
        return im
    c = sorted(glob.glob(str(FIN / f"{i}_v*_1080x1350.png")), key=lambda p: int(p.split("_v")[1].split("_")[0]))
    return Image.open(c[-1]).convert("RGB")


rows = 10
sheet = Image.new("RGB", (3 * TW + 2 * GAP, rows * TH + (rows - 1) * GAP), "#FFFFFF")
for k in range(30):
    i = ORDER[29 - k]  # k=0 es la publicación 30
    sheet.paste(tile(i).resize((TW, TH), Image.LANCZOS), ((k % 3) * (TW + GAP), (k // 3) * (TH + GAP)))
out = IG / "grilla-v6.png"
sheet.save(out)
# vista de teléfono: las 9 más recientes
sheet.crop((0, 0, sheet.width, 3 * TH + 2 * GAP)).save(IG / "grilla-v6-primeras9.png")
print("✓", out)
