# Instalación — skill /static-ads para elvo·

1. Descomprime esta carpeta donde quieras (ej. `~/elvo-ads`).
2. Terminal: `cd ~/elvo-ads && bash setup.sh`
3. Crea tu key en https://fal.ai/dashboard/keys, carga saldo y pégala en `.env` (`FAL_KEY=...`).
4. Abre Claude Code en la carpeta: `claude`
5. Escribe `/static-ads`. Te pedirá el ad de referencia: déjalo en `brands/elvo/static-ads/ad-references/`.

Ya vienen cargados: guía visual y de voz, doctrina, claims verificados/restringidos del Nativo (sincronizados con Shopify el 2-oct-2026) y la foto limpia del Nativo + núcleo.

Para Vivo/Ritual: agrega sus fotos limpias a `product-images/` y sus claims a `products.json`.

Prueba aislada del script (sin Claude Code), una vez que exista un spec:
`python3 .claude/skills/static-ads/scripts/generate-static-ad.py brands/elvo/static-ads/<carpeta> var-1`
