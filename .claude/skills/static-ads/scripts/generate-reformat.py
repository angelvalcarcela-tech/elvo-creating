#!/usr/bin/env python3
"""Recompone un ad ya generado a otro aspect ratio, sin cambiar copy ni producto.

Uso:
  python3 .claude/skills/static-ads/scripts/generate-reformat.py brands/elvo/static-ads/<out>/<out>-var-1_v1.png 9:16

Guarda <out>-var-1_9x16_v1.png en la misma carpeta (+ export exacto en exports/).
Siempre reformatea desde el output primario, nunca desde otro reformat.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (  # noqa: E402
    check_ratio, download, export_exact, load_env, next_version,
    project_root, run_fal, upload,
)

PROMPT = (
    "{ratio} aspect ratio. Recompose the attached advertisement into a {ratio} canvas. "
    "Keep every word of text exactly as written (same spelling, accents and punctuation), "
    "the same product exactly as shown, the same colors, the same typography and the same visual hierarchy. "
    "Only re-arrange spacing and extend the plain background naturally to fill the new frame — "
    "do not add any new text, badge, logo, icon or graphic element, and do not crop the product or any text. "
    "Safe zones: keep the top {sz}% and bottom {sz}% of the frame free from text, logos, icons and buttons."
)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    load_env()
    src = Path(sys.argv[1])
    if not src.is_absolute():
        src = project_root() / src
    ratio = sys.argv[2]
    check_ratio(ratio)
    if not src.exists():
        sys.exit(f"No existe {src}")

    m = re.match(r"(.+)_v\d+$", src.stem)
    base = m.group(1) if m else src.stem
    base = f"{base}_{ratio.replace(':', 'x')}"

    safe = 14 if ratio == "9:16" else 10
    url = run_fal(PROMPT.format(ratio=ratio, sz=safe), [upload(str(src))], ratio, "high")
    dest = next_version(src.parent, base)
    download(url, dest)
    exp = export_exact(dest, ratio)
    print(f"✓ {dest.relative_to(project_root())}")
    print(f"✓ {exp.relative_to(project_root())}")


if __name__ == "__main__":
    main()
