#!/usr/bin/env python3
"""Genera una variación de static ad desde static-ad-spec.json vía fal (gpt-image-2).

Uso:
  python3 .claude/skills/static-ads/scripts/generate-static-ad.py brands/elvo/static-ads/<output-name> var-1

Modos (campo "mode" del spec):
  reference  → Image 1 = el ad de referencia; luego las fotos de producto.
  wireframe  → Image 1 = wireframe neutro generado desde layout_zones; luego producto. (default)
  text       → solo las fotos de producto; el prompt describe todo el layout.
Si no hay ninguna imagen, usa el endpoint text-to-image.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import (  # noqa: E402
    check_ratio, download, export_exact, load_env, make_wireframe,
    next_version, project_root, run_fal, upload,
)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    load_env()
    out_dir = Path(sys.argv[1])
    if not out_dir.is_absolute():
        out_dir = project_root() / out_dir
    slug = sys.argv[2]

    spec_path = out_dir / "static-ad-spec.json"
    if not spec_path.exists():
        sys.exit(f"No encuentro {spec_path}")
    spec = json.loads(spec_path.read_text())

    var = next((v for v in spec["variations"] if v["slug"] == slug), None)
    if var is None:
        sys.exit(f"No existe la variación '{slug}' en el spec.")

    ratio = var.get("aspect_ratio", spec.get("aspect_ratio", "4:5"))
    check_ratio(ratio)
    quality = spec.get("quality", "high")
    mode = spec.get("mode", "wireframe")

    image_urls = []
    if mode == "reference" and spec.get("reference_image"):
        image_urls.append(upload(spec["reference_image"]))
    elif mode == "wireframe" and spec.get("layout_zones"):
        wf = make_wireframe(spec["layout_zones"], ratio, out_dir / f"wireframe_{ratio.replace(':', 'x')}.png")
        image_urls.append(upload(str(wf)))
    for p in spec.get("product_images", []):
        image_urls.append(upload(p))

    url = run_fal(var["prompt"], image_urls, ratio, quality)
    dest = next_version(out_dir, f"{spec['output_name']}-{slug}")
    download(url, dest)
    exp = export_exact(dest, ratio)
    print(f"✓ {dest.relative_to(project_root())}")
    print(f"✓ {exp.relative_to(project_root())}")


if __name__ == "__main__":
    main()
