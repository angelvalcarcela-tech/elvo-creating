#!/usr/bin/env python3
"""Genera las imágenes de IA SIN texto del pack Instagram v2 (4:5, calidad alta).

Uso: python3 .claude/skills/static-ads/scripts/generate-ig.py <id> [<id> ...]
Salida: brands/elvo/brand-identity/instagram/ia/<id>_vN.png (nunca sobreescribe).
El texto (titular, etiqueta, logo) se compone después con Pillow.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import download, next_version, project_root, run_fal, upload  # noqa: E402

BRAND = "brands/elvo/brand-identity"
STYLE = {
    "PIEDRA": "Warm alabaster (#EAE7E0) and pale limestone (#D8D2C7) background, soft low-contrast cool-neutral daylight from the side, shallow depth of field, a single tactile prop (pale mineral stone, ceramic or a clear glass), generous negative space, no gradients, no hard shadows, muted stone tones, editorial apothecary aesthetic.",
    "FORMULACION": "Overhead flat-lay on deep slate charcoal (#2B2E2D), cool neutral studio lighting with a thin soft white rim-light, precise and considered arrangement, minimal, no gradients, no hard shadows.",
    "TECH": "Overhead flat-lay on deep slate charcoal (#2B2E2D), cool studio lighting with a thin glacier-teal (#82C3C4) rim-light, luminous aqua highlights, minimal, technological and precise, no gradients, no hard shadows.",
    "ARENA": "Warm mineral-toned interior in soft daylight, gentle warm sand light (#D7C4A6), considered architectural composition, muted stone-and-sand palette, one subject in frame, low-contrast, calm spa aesthetic, no people's faces, no gradients.",
}
WATER = " Any water in the image must look like fresh, natural, drinkable water: colorless, crystal clear, clean and appealing to drink, with no blue, teal or green tint and no colored light cast on it."
TAIL = WATER + " Full-bleed photograph filling the entire frame edge to edge: no borders, bands, letterboxing or flat-colored strips; the scene itself continues naturally (plain wall, surface or background) into the top and bottom areas. Absolutely no text, letters, numbers, captions, watermarks or added logos anywhere in the image. Keep the top 15% and bottom 15% of the frame empty and uncluttered (text will be added later)."
REF = " Reproduce the attached product photo exactly: same shape, proportions, colors and the elvo· logo as printed on it; do not redraw, restyle or alter the product or its logo."

PIECES = {
    "p18": ("PIEDRA", [f"{BRAND}/product-images/nativo-front.png"],
            "4:5 vertical. The attached elvo· Nativo water purifier standing on a pale stone counter next to a chrome tap, side window light, one clear glass of water beside it." + REF),
    "p16": ("FORMULACION", [],
            "4:5 vertical. Pale mineral stones and one small dark fragment arranged beside a clear glass of water."),
    "p19": ("PIEDRA", [f"{BRAND}/product-images/alivio-22-front.png"],
            "4:5 vertical. The attached jug-style water purifier standing on a pale kitchen shelf next to a clear glass jug, soft window light, calm and tidy." + REF),
    "p21": ("PIEDRA", [f"{BRAND}/product-images/alivio-16-front.png"],
            "4:5 vertical. The attached jug-style water purifier standing on a pale kitchen shelf, a clear glass jug beside it, one hand pouring water from the jug into a clear glass; no face." + REF),
    "p22": ("PIEDRA", [],
            "4:5 vertical. A ceramic cup with a thin line of steam beside a clear glass of cold water on a pale stone tray."),
    "p20": ("FORMULACION", [],
            "4:5 vertical. Overhead flat-lay: five pale stones in a neat line beside a clear glass of water."),
    "p23": ("PIEDRA", [f"{BRAND}/product-images/cero-front.png"],
            "4:5 vertical. The attached countertop water dispenser on a pale stone kitchen counter near a window, a clear glass beside it." + REF),
    "p24": ("FORMULACION", [],
            "4:5 vertical. Overhead flat-lay: a clear glass of cold water with a glacier highlight and a ceramic cup with thin steam, side by side."),
    "p02": ("TECH", [], "4:5 vertical. A single water drop on a slate surface with a thin glacier highlight, macro, nothing else in frame."),
    "p04": ("PIEDRA", [], "4:5 vertical. Two hands holding a clear glass of water over a pale stone counter; no faces."),
    "p05": ("PIEDRA", [], "4:5 vertical. One clear glass of water on a linen cloth."),
    "p07": ("FORMULACION", [f"{BRAND}/product-images/nativo-repuesto-nucleo.png"],
            "4:5 vertical. Overhead. The attached replacement filter core centered on the slate with a clear glass of water beside it." + REF),
    "p08": ("PIEDRA", [], "4:5 vertical. A clear glass of water on a bedside table beside a closed book, warm low light."),
    "p09": ("PIEDRA", [f"{BRAND}/product-images/vivo-front.png"],
            "4:5 vertical. The attached purifier on a pale stone kitchen counter, close framing; one hand holds a clear glass under its spout while it fills; no face." + REF),
    "p10": ("PIEDRA", [f"{BRAND}/product-images/nativo-front.png"],
            "4:5 vertical. The attached purifier on a pale stone counter, a clear glass of water filled at its spout." + REF),
    "p11": ("FORMULACION", [], "4:5 vertical. One clear glass of water at the center of the slate, a thin glacier rim-light on the glass."),
    "p14": ("PIEDRA", [f"{BRAND}/product-images/vivo-front.png"],
            "4:5 vertical. The attached purifier on a pale stone counter beside a clear glass and a small dark mineral fragment." + REF),
    "p12": ("PIEDRA", [], "4:5 vertical. A table set for two with clear glasses and a glass jug of water, linen napkins, calm light."),
    "p13": ("ARENA", [], "4:5 vertical. A stone bathroom shelf with a ceramic dish and a folded towel, soft sand light."),
    "p15": ("FORMULACION", [], "4:5 vertical. Overhead. A small ceramic dish with activated charcoal granules and a few metallic grains beside a clear glass of water."),
    "p17": ("PIEDRA", [], "4:5 vertical. A hand holding a clear glass of water by a window in the morning; no face."),
    "pB1": ("PIEDRA", [], "4:5 vertical. A pale stone windowsill with a clear glass of water and a folded linen cloth, soft diffuse coastal light through the window."),
    "pB2": ("PIEDRA", [], "4:5 vertical. A single clear glass at the center of a pale stone counter, lots of negative space."),
    "pB3": ("FORMULACION", [], "4:5 vertical. Overhead flat-lay: pale mineral stones of different sizes and one clear glass of water."),
    "pB4": ("TECH", [], "4:5 vertical. Overhead. One pale stone alone on the slate, a thin glacier highlight on its edge."),
    "pB6": ("PIEDRA", [], "4:5 vertical. Two hands holding a clear glass beside a closed notebook and a pen on a pale stone table, soft light, no phone, no faces."),
    "p01": ("ARENA", [],
            "4:5 vertical. A warm bathroom corner with a chrome shower fixture and a folded linen towel, soft sand light."),
}


def main():
    ids = sys.argv[1:]
    if not ids:
        sys.exit(__doc__)
    out = project_root() / BRAND / "instagram" / "ia"
    out.mkdir(parents=True, exist_ok=True)
    for i in ids:
        style, refs, scene = PIECES[i]
        url = run_fal(f"{scene} {STYLE[style]}{TAIL}", [upload(r) for r in refs], "4:5", "high")
        dest = next_version(out, i)
        download(url, dest)
        print("✓", dest.relative_to(project_root()))


if __name__ == "__main__":
    main()
