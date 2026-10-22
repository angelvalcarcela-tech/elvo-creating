# Ajustes globales del tema (auditoría 2026-10-22)

Aplicados en el tema borrador "elvo mineral (rebrand, borrador)":

- `sections/header.liquid`: el logo ya no es `<h1>` en la home (queda un solo h1: el de la portada); preconnect + `<link>` único para Inter y Plus Jakarta Sans; carga `assets/elvo-fixes.css`.
- `assets/elvo-web.css`: se quitó el `@import` de fuentes; `color-scheme-5` usa texto oscuro (contraste).
- `assets/elvo-fixes.css` (nuevo): zonas táctiles mínimas de 44 px (resúmenes de preguntas, barra de anuncios, enlaces del pie).

Pendiente: `assets/elvo.css` (legado) aún hace `@import` de DM Serif + Inter.
