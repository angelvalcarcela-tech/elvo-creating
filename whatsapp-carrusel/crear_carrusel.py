#!/usr/bin/env python3
"""Crea la plantilla de carrusel `elvo_cyber_carrusel` en WhatsApp Cloud API.

Variables de entorno (NO las pegues en ningún chat):
  META_TOKEN   token de acceso (usuario del sistema, permiso whatsapp_business_management)
  META_APP_ID  ID de la app de Meta
  WABA_ID      ID de la cuenta de WhatsApp Business

Uso:
  pip install requests
  export META_TOKEN=... META_APP_ID=... WABA_ID=...
  python3 crear_carrusel.py
"""
import os
import sys
from pathlib import Path

import requests

API = "https://graph.facebook.com/v21.0"
TOKEN = os.environ.get("META_TOKEN")
APP_ID = os.environ.get("META_APP_ID")
WABA_ID = os.environ.get("WABA_ID")
if not (TOKEN and APP_ID and WABA_ID):
    sys.exit("Faltan META_TOKEN, META_APP_ID o WABA_ID en el entorno.")

NOMBRE = "elvo_cyber_carrusel"

CUERPO = (
    "Hay decisiones que lo cambian todo. 💧\n\n"
    "Ese vaso de agua de cada mañana, el café, la comida de todos los días... "
    "merecen algo mejor. Y hoy, por fin, es posible. ✨\n\n"
    "Llegó el Cyber elvo·. Solo hasta este domingo 1 de noviembre, tu purificador "
    "ideal tiene un precio que no vas a querer dejar pasar, y con regalo incluido. 🎁\n\n"
    "Sin obras. Sin gasfitero. Envío gratis a todo el Perú y pago contra entrega.\n\n"
    "Desliza y encuentra el tuyo. 👇 ¿Dudas? Escríbenos, te acompañamos hasta que "
    "elijas el correcto. 💙\n\n"
    "Si no quieres recibir más mensajes, responde NO."
)

# (imagen, texto de la tarjeta (máx. 160), url)
TARJETAS = [
    ("tarjetas/nativo.jpg",
     "Nativo Antimetales: la protección que tu familia merece. Hoy S/ 349 + filtro de repuesto de regalo. 🎁",
     "https://elvo.pe/products/elvonativo"),
    ("tarjetas/vivo.jpg",
     "Vivo con Magnesio: agua suave y sin sabor a cloro, directo de tu caño. Hoy S/ 259 + medidor de agua de regalo. 🎁",
     "https://elvo.pe/products/elvovivo"),
    ("tarjetas/alivio16.jpg",
     "Alivio 16 L: agua fresca para toda la casa. Hoy S/ 159 + medidor de agua de regalo. 🎁",
     "https://elvo.pe/products/elvo-bidon-16l"),
    ("tarjetas/alivio22.jpg",
     "Alivio 22 L: más agua, más tranquilidad. Hoy S/ 198 + medidor de agua de regalo. 🎁",
     "https://elvo.pe/products/elvo-bidon-22l"),
]
BOTON = "Lo quiero"  # máx. 25 caracteres, igual en todas las tarjetas

AQUI = Path(__file__).parent


def subir_imagen(ruta: Path) -> str:
    """Sube la imagen con la Resumable Upload API y devuelve el handle."""
    datos = ruta.read_bytes()
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
    cards = []
    for imagen, texto, url in TARJETAS:
        assert len(texto) <= 160, f"Texto de tarjeta > 160: {texto}"
        handle = subir_imagen(AQUI / imagen)
        print(f"Subida {imagen}")
        cards.append({
            "components": [
                {"type": "HEADER", "format": "IMAGE", "example": {"header_handle": [handle]}},
                {"type": "BODY", "text": texto},
                {"type": "BUTTONS", "buttons": [{"type": "URL", "text": BOTON, "url": url}]},
            ]
        })

    payload = {
        "name": NOMBRE,
        "language": "es",
        "category": "MARKETING",
        "components": [
            {"type": "BODY", "text": CUERPO},
            {"type": "CAROUSEL", "cards": cards},
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
