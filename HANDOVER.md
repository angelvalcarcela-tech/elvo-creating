# Handover — /static-ads para elvo·

## Estado
- Repo: `elvo-creating`, rama `claude/static-ads-recreation-myxa14` (todo commiteado y subido).
- Skill: `.claude/skills/static-ads/` (scripts en `scripts/`, `fal_client` ya requerido en `requirements.txt`; instalar con `pip install -r`).
- Marca: `brands/elvo/brand-identity/` (`visual-guidelines.md`, `products.json`, `doctrina.md`, `product-images/`).
- Productos en `products.json`: **Nativo** y **Vivo** (Vivo sacado de Shopify el 2-oct-2026; elvo.pe y el CDN de Shopify están bloqueados por el proxy del entorno, así que no se pudo bajar nada de ahí).
- Foto: Nativo y Vivo se ven IGUALES por fuera (cambia solo el interior). Se usa una sola foto: `product-images/vivo-front.png` (también `nativo-front.png`). Misma foto para ambos.
- `FAL_KEY`: el usuario ya la cargó en el entorno, pero la sesión anterior no la vio. Verificar con `env | grep FAL_KEY` (sin imprimirla). Si falta, avisar al usuario; nunca pedirle que la pegue en el chat.

## Decisiones del usuario
1. **Ignorar la doctrina** (sin miedo/urgencia/etc. ya no aplica). Usar las plantillas de la skill: iMessage, ingredient spotlight, precio/oferta (y scarcity si el usuario lo pide; el usuario dijo "las plantillas que tienes"). Pendiente: actualizar `CLAUDE.md` y `visual-guidelines.md` para no aplicar la doctrina (preguntar si quitar o relajar).
2. Productos: elvo· Nativo y elvo· Vivo.
3. Ángulos y públicos ganadores: elige Claude. Propuesta:
   - Nativo: plomo y metales pesados (red general); arsénico en pozo/provincia (solo ahí, con "No reemplaza la cloración del agua de pozo"); instalación sin gasfitero en 5 min.
   - Vivo: agua sin sabor a cloro; magnesio y tendencia alcalina; vaso en 5 segundos.
4. Formatos: 4:5 (feed) principal y 9:16 (stories) vía reformat.
5. Precios: mezcla de piezas con y sin precio. Nativo desde S/ 299 (18m), S/ 349 (3a), S/ 399 (6a). Vivo desde S/ 199, S/ 249, S/ 329.
6. Copy: claims solo de `products.json` (verified_claims). No usar restricted_claims (mercurio, certificaciones, garantía de por vida, UV de regalo, plomo/arsénico en Vivo).

## Pendiente (Pasos de la skill)
- Confirmar con el usuario cuántas piezas en total y el costo (~US$0.12 por imagen + reformat). Mostrarlo antes de generar.
- Paso 2: pedir imagen de referencia o usar plantillas directamente (modo B, sin `reference_image`).
- Pasos 4–10: copy en español, prompts en inglés, spec JSON por pieza, generar, reformatear a 9:16.
- Salida en `brands/elvo/static-ads/<formato>-<producto>/`.
