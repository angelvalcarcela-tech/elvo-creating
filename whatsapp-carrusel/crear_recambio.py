#!/usr/bin/env python3
"""Crea la plantilla `elvo_preventa_recambio_alivio` en WhatsApp Cloud API.

Descarga la foto del repuesto de Alivio desde la tienda y la usa como encabezado.

Variables de entorno (NO las pegues en ningún chat):
  META_TOKEN, META_APP_ID, WABA_ID

Uso:
  pip3 install requests pillow
  export META_TOKEN=... META_APP_ID=... WABA_ID=...
  python3 crear_recambio.py
"""
import io
import os
import sys

import requests
from PIL import Image

API = "https://graph.facebook.com/v21.0"
TOKEN = os.environ.get("META_TOKEN")
APP_ID = os.environ.get("META_APP_ID")
WABA_ID = os.environ.get("WABA_ID")
if not (TOKEN and APP_ID and WABA_ID):
    sys.exit("Faltan META_TOKEN, META_APP_ID o WABA_ID en el entorno.")

NOMBRE = "elvo_preventa_recambio_alivio"
IMAGEN_URL = "https://cdn.shopify.com/s/files/1/0738/0923/2107/files/elvo-foto-alivio-repuesto.webp?v=1792791312"

CUERPO = (
    "Tu agua también se cuida con tiempo. 💧\n\n"
    "Si ya disfrutas de tu purificador elvo· Alivio, sabes lo que se siente: "
    "agua más fresca y lista cada día. 💙\n\n"
    "Aprovecha la preventa de tu kit de filtros de repuesto, solo hasta este "
    "domingo 1 de noviembre. ✨\n\n"
    "Solo S/ 99 y lo recibes con envío gratis a todo el Perú. 🚚\n\n"
    "Pídelo aquí. 👇\n"
    "¿Dudas? Escríbenos y te ayudamos. 💬\n\n"
    "Si no quieres recibir más mensajes, responde NO."
)
BOTON = "Comprar en preventa"  # máx. 25 caracteres
URL = "https://elvo.pe/products/kit-de-filtros-purificador-de-agua"


def imagen_jpeg() -> bytes:
    """Descarga la foto y la convierte a JPEG (Meta no acepta webp)."""
    r = requests.get(IMAGEN_URL, timeout=30)
    r.raise_for_status()
    im = Image.open(io.BytesIO(r.content)).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=92)
    return buf.getvalue()


def subir_imagen(datos: bytes) -> str:
    """Sube la imagen con la Resumable Upload API y devuelve el handle."""
    r = requests.post(
        f"{API}/{APP_ID}/uploads",
        params={"file_length": len(datos), "file_type": "image/jpeg", "access_token": TOKEN},
    )
    r.raise_for_status()
    sesion = r.json()["id"]
    r = requests.post(
        f"{API}/{sesion}",
        headers={"Authorization": f"OAuth {TOKEN}", "file_offset": "0"},
        data=datos,
    )
    r.raise_for_status()
    return r.json()["h"]


def main():
    handle = subir_imagen(imagen_jpeg())
    print("Imagen subida")
    payload = {
        "name": NOMBRE,
        "language": "es",
        "category": "MARKETING",
        "components": [
            {"type": "HEADER", "format": "IMAGE", "example": {"header_handle": [handle]}},
            {"type": "BODY", "text": CUERPO},
            {"type": "BUTTONS", "buttons": [{"type": "URL", "text": BOTON, "url": URL}]},
        ],
    }
    r = requests.post(
        f"{API}/{WABA_ID}/message_templates",
        headers={"Authorization": f"Bearer {TOKEN}"},
        json=payload,
    )
    print(r.status_code, r.text)


if __name__ == "__main__":
    main()
