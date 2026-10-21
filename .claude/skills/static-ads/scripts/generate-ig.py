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
    "PIEDRA": "Warm alabaster (#EAE7E0) and pale limestone (#D8D2C7) background, soft low-contrast cool-neutral daylight from the side, shallow depth of field, a single tactile prop (pale mineral stone, ceramic or a clear glass), subtle glacier-teal (#82C3C4) tint only in the water, generous negative space, no gradients, no hard shadows, muted stone tones, editorial apothecary aesthetic.",
    "FORMULACION": "Overhead flat-lay on deep slate charcoal (#2B2E2D), cool studio lighting with a thin glacier-teal (#82C3C4) rim-light, precise and considered arrangement, luminous aqua highlights only on glass and water, minimal, no gradients, no hard shadows.",
    "ARENA": "Warm mineral-toned interior in soft daylight, gentle warm sand light (#D7C4A6), considered architectural composition, muted stone-and-sand palette, one subject in frame, low-contrast, calm spa aesthetic, no people's faces, no gradients.",
}
TAIL = " Full-bleed photograph filling the entire frame edge to edge: no borders, bands, letterboxing or flat-colored strips; the scene itself continues naturally (plain wall, surface or background) into the top and bottom areas. Absolutely no text, letters, numbers, captions, watermarks or added logos anywhere in the image. Keep the top 15% and bottom 15% of the frame empty and uncluttered (text will be added later)."
REF = " Reproduce the attached product photo exactly: same shape, proportions, colors and the elvo· logo as printed on it; do not redraw, restyle or alter the product or its logo."

PIECES = {
    "p18": ("PIEDRA", [f"{BRAND}/product-images/nativo-front.png"],
            "4:5 vertical. The attached elvo· Nativo water purifier standing on a pale stone counter next to a chrome tap, side window light, one clear glass of water beside it." + REF),
    "p16": ("FORMULACION", [],
            "4:5 vertical. Pale mineral stones and one small dark fragment arranged beside a clear glass of water."),
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
