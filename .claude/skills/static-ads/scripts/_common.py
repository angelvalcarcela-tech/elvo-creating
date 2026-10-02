"""Utilidades compartidas: tamaños, .env, subida a fal, descarga y export."""
import os
import re
import sys
from pathlib import Path

import requests
from PIL import Image, ImageDraw

# Tamaños de generación: múltiplos de 16 y >= 655,360 px (requisito de gpt-image-2 en fal).
GEN_SIZES = {
    "1:1": (1024, 1024),
    "4:5": (1088, 1360),
    "3:4": (1152, 1536),
    "9:16": (1152, 2048),
    "16:9": (2048, 1152),
}
# Tamaños de entrega exactos por canal.
EXPORT_SIZES = {
    "1:1": (1080, 1080),
    "4:5": (1080, 1350),
    "3:4": (1080, 1440),
    "9:16": (1080, 1920),
    "16:9": (1920, 1080),
}

EDIT_ENDPOINT = "openai/gpt-image-2/edit"
T2I_ENDPOINT = "openai/gpt-image-2"


def project_root() -> Path:
    """Sube desde el directorio actual hasta encontrar la carpeta brands/."""
    p = Path.cwd().resolve()
    for cand in [p, *p.parents]:
        if (cand / "brands").is_dir():
            return cand
    return p


def load_env():
    """Carga FAL_KEY desde .env en la raíz del proyecto si no está ya en el entorno."""
    env = project_root() / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
    if not os.environ.get("FAL_KEY"):
        sys.exit("Falta FAL_KEY. Agrégala a .env en la raíz del proyecto (FAL_KEY=...).")


def check_ratio(ratio: str):
    if ratio not in GEN_SIZES:
        sys.exit(f"Aspect ratio no soportado: {ratio}. Usa uno de: {', '.join(GEN_SIZES)}")


def upload(path: str) -> str:
    import fal_client
    full = Path(path)
    if not full.is_absolute():
        full = project_root() / path
    if not full.exists():
        sys.exit(f"No existe la imagen: {full}")
    return fal_client.upload_file(str(full))


def run_fal(prompt: str, image_urls: list, ratio: str, quality: str = "high") -> str:
    import fal_client
    w, h = GEN_SIZES[ratio]
    args = {
        "prompt": prompt,
        "image_size": {"width": w, "height": h},
        "quality": quality,
        "num_images": 1,
        "output_format": "png",
    }
    endpoint = T2I_ENDPOINT
    if image_urls:
        args["image_urls"] = image_urls[:16]
        endpoint = EDIT_ENDPOINT
    print(f"→ {endpoint} · {w}x{h} · quality={quality} · {len(image_urls)} imagen(es) de referencia")
    result = fal_client.subscribe(endpoint, arguments=args, with_logs=False)
    return result["images"][0]["url"]


def download(url: str, dest: Path):
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    dest.write_bytes(r.content)


def next_version(folder: Path, base: str) -> Path:
    """Devuelve folder/base_vN.png con N siguiente libre (nunca sobreescribe)."""
    n = 1
    pat = re.compile(re.escape(base) + r"_v(\d+)\.png$")
    for f in folder.glob(f"{base}_v*.png"):
        m = pat.match(f.name)
        if m:
            n = max(n, int(m.group(1)) + 1)
    return folder / f"{base}_v{n}.png"


def export_exact(src: Path, ratio: str):
    """Recorta al centro y escala al tamaño exacto del canal; guarda en exports/."""
    tw, th = EXPORT_SIZES[ratio]
    im = Image.open(src).convert("RGB")
    sw, sh = im.size
    target = tw / th
    if sw / sh > target:
        nw = int(sh * target)
        left = (sw - nw) // 2
        im = im.crop((left, 0, left + nw, sh))
    else:
        nh = int(sw / target)
        top = (sh - nh) // 2
        im = im.crop((0, top, sw, top + nh))
    im = im.resize((tw, th), Image.LANCZOS)
    out_dir = src.parent / "exports"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{src.stem}_{tw}x{th}.png"
    im.save(out, optimize=True)
    return out


def make_wireframe(zones: dict, ratio: str, dest: Path) -> Path:
    """Wireframe neutro, sin texto: solo rectángulos grises por zona."""
    w, h = GEN_SIZES[ratio]
    im = Image.new("RGB", (w, h), (236, 236, 236))
    d = ImageDraw.Draw(im)
    tones = {
        "text_zone": (190, 190, 190),
        "product_zone": (160, 160, 160),
        "button_zone": (120, 120, 120),
        "disclaimer_zone": (210, 210, 210),
    }
    mx = int(w * 0.08)
    for name, z in zones.items():
        top, bottom = int(z["top"] * h), int(z["bottom"] * h)
        d.rectangle([mx, top, w - mx, bottom], fill=tones.get(name, (175, 175, 175)))
    im.save(dest)
    return dest
