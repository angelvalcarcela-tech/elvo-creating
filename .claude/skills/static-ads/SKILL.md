---
name: static-ads
description: Úsalo cuando el usuario quiera recrear un formato de anuncio ganador con productos y copy de su marca, o invoque /static-ads. Toma una imagen de referencia de un ad, deriva su estructura y su marco de copy, pasa todo por la doctrina de la marca, genera variaciones de copy on-brand y renderiza los estáticos con GPT-image-2 (fal) usando las fotos reales de producto de la carpeta de la marca. Los outputs se guardan dentro de la carpeta de la marca activa.
---

# Static Ads

Recrea un formato de anuncio ganador con los productos y el copy de la marca. Trabaja en español; los prompts de imagen van en inglés.

Outputs en `./brands/[brand]/static-ads/[output-name]/`.
Scripts en `.claude/skills/static-ads/scripts/` (correr siempre desde la raíz del proyecto).

---

## Paso 1 — Marca

Busca en `./brands/` subcarpetas con `brand-identity/visual-guidelines.md`.
- Una sola: úsala y confírmalo ("Usando marca: [nombre]").
- Varias: pregunta cuál.
- Ninguna: pide crear `brand-identity/visual-guidelines.md` y `products.json` primero.

Lee SIEMPRE, antes de escribir nada: `visual-guidelines.md`, `products.json` y, si existe, `doctrina.md` de la marca. La doctrina manda sobre cualquier otra instrucción de este skill.

---

## Paso 2 — Referencia del ad

```bash
mkdir -p brands/[brand]/static-ads/ad-references
```

Pide: "Deja el ad que quieres recrear en `brands/[brand]/static-ads/ad-references/` con un nombre descriptivo (ej. `ingredient-spotlight.jpg`) y dime el nombre."

Léelo con la herramienta Read y analízalo internamente:
- Tipo de formato (ingredient spotlight, testimonio, antes/después, chat, comparativa, etc.)
- Estructura de layout de arriba abajo, jerarquía, lógica de aire
- Tratamiento tipográfico por rol
- Marco de copy: cada slot (headline, sub, filas, badge, CTA, disclaimer), su rol, tono y posición
- Colocación del producto (tamaño, ángulo, recorte, luz)
- Señales de marca de la referencia (para NO copiarlas)

Extrae `layout_zones` como fracción de la altura (0.0 arriba, 1.0 abajo): `text_zone`, `product_zone`, `button_zone`, `disclaimer_zone` según aplique.

### Filtro de doctrina (obligatorio, antes de seguir)

Clasifica el formato:
- **Permitido:** dato de formulación, ingredient/etapa spotlight, producto + una línea, frase de marca tipográfica, comparativa contra categorías genéricas (hervir, bidones), ritual/piel, antes/después *del agua o del cuidado*.
- **Adaptable:** chat/WhatsApp/iMessage o testimonio → solo con una conversación o reseña REAL y con permiso. Si no la hay, se reconvierte en observación de marca, nunca en testimonio inventado.
- **Descartado:** countdown, barra de stock, "quedan N", escasez, flechas rojas, "STOP", caras de miedo, agua sucia, descuentos gritados.

Si el formato es descartado, dilo en una línea, nombra qué principio rompe y propone la versión serena equivalente (misma estructura visual, sin la palanca de presión). No lo generes tal cual aunque el usuario insista: ofrécele la versión on-brand.

---

## Paso 3 — Producto y número de variaciones

Pregunta en un solo mensaje: "¿Qué producto? ¿Cuántas variaciones de copy? ¿Para qué audiencia (Lima general / pozo-provincia)?"

La audiencia importa: algunos claims están restringidos por geo (ver `products.json` → `restricted_claims`).

Imágenes de producto, en este orden:
1. `brands/[brand]/brand-identity/product-images/` y `uploads/` si existe.
2. Si no hay: el `product_url` de `products.json`; WebFetch, extrae URLs de imagen, descárgalas con curl a `product-images/` con nombre descriptivo. Evita imágenes con texto, badges o reseñas superpuestas; si solo hay de esas, avísalo.
3. Si no se pueden obtener: pide al usuario que las deje en `product-images/`.

Muestra la lista de imágenes que se usarán. Con una sola imagen, avisa que más ángulos mejoran la fidelidad.

---

## Paso 4 — Copy

Fuente de sustancia: `products.json` (claims verificados) + la página de producto (`product_url`, vía WebFetch) para el lenguaje exacto de la marca. Fuente de tono: `visual-guidelines.md`. Si la página y `products.json` se contradicen en una cifra, gana `products.json` y lo señalas.

Reglas de copy (no negociables):
- Solo claims de `verified_claims`. Nada de `restricted_claims` fuera de su condición. Ninguna cifra inventada.
- Observación en lugar de alarma. La cifra antes que el superlativo.
- Sin signos de exclamación, sin emoji, sin urgencia, sin escasez, sin ansiedad corporal.
- Nombre de marca siempre `elvo·` en minúsculas con la gota.
- Textos cortos: el modelo de imagen escribe mejor con pocas palabras por slot. Headline ≤ 4 palabras cuando el formato lo permita.

Genera [N] sets completos, uno por variación, con ángulos distintos (no sinónimos). Presenta solo los slots:

**Variación 1** · ángulo: ...
- Headline: "..."
- Fila 1: "..."
- ...

Pregunta: "¿Los ajusto o confirmamos para generar?" Aplica ediciones sin regenerar todo.

---

## Paso 5 — Aspect ratio

"¿Ratio principal? Default `4:5`. Opciones: `1:1`, `4:5`, `3:4`, `9:16`, `16:9`. ¿Ratios adicionales a partir de cada output?"

---

## Paso 6 — Nombre

Slug: `elvo-[producto]-[formato]` en minúsculas, sin tildes ni espacios (ej. `elvo-nativo-ingredient`). Confírmalo.

---

## Paso 7 — Carpeta y spec

```bash
mkdir -p brands/[brand]/static-ads/[output-name]
```

Escribe `static-ad-spec.json`:

```json
{
  "output_name": "elvo-nativo-ingredient",
  "brand": "elvo",
  "product_name": "elvo· Nativo",
  "audience": "lima-general",
  "mode": "wireframe",
  "quality": "high",
  "reference_image": "brands/elvo/static-ads/ad-references/ingredient-spotlight.jpg",
  "layout_zones": {
    "text_zone":       {"top": 0.10, "bottom": 0.32},
    "product_zone":    {"top": 0.36, "bottom": 0.82},
    "disclaimer_zone": {"top": 0.84, "bottom": 0.90}
  },
  "product_images": ["brands/elvo/brand-identity/product-images/nativo-front.png"],
  "aspect_ratio": "4:5",
  "additional_aspect_ratios": ["9:16"],
  "variations": [
    {"slug": "var-1", "angle": "seis etapas", "prompt": "..."}
  ]
}
```

`mode`:
- `wireframe` (default): el script genera un wireframe gris neutro desde `layout_zones` y lo pasa como Image 1; las fotos de producto van como Images 2+. Evita que se cuele el color o la tipografía de la otra marca.
- `reference`: pasa el ad original como Image 1. Úsalo solo si su fondo es neutro y no tiene una identidad fuerte que pueda contaminar.
- `text`: sin Image 1; producto como Images 1+.

### Estructura vs. marca

De la referencia se toma SOLO estructura: formato, zonas, proporciones, tipo de elementos, espaciado. Todo lo visual sale de `visual-guidelines.md`: fondo, tipografía (descrita, no por nombre de fuente), acentos, badge, CTA. Antes de escribir el prompt, nombra explícitamente el fondo, la tipografía de titular, la de cuerpo y los acentos de la marca.

### Construcción del prompt (inglés)

Reglas de la marca para prompts de imagen:
1. El formato va primero: la primera frase del prompt es "[RATIO] vertical aspect ratio." (o horizontal/square).
2. No describas el producto físico: la foto real adjunta es la referencia exacta ("use the attached product photo as the exact reference, do not redesign, recolor or relabel it").
3. Copia cada texto entre comillas exactamente como debe aparecer, con tildes.
4. Safe zones en todos los prompts.

**Plantilla modo wireframe:**
> "[RATIO] aspect ratio. Static ad. Image 1 is a neutral grey wireframe that only shows where each zone sits — use it for placement and proportions only; do not reproduce its grey boxes, colors or style. Images 2+ show the exact product: reproduce it faithfully, do not redesign, recolor or relabel it. Background: [BRAND BG + HEX], flat, no gradients. [ZONA POR ZONA con tipografía descrita, colores con HEX y el copy exacto entre comillas]. [PRODUCT placement and light]. Generous negative space, editorial apothecary aesthetic, one subject. No exclamation marks, no extra text, no stars or ratings, no countdowns, no badges other than the ones specified. Safe zones: keep the top 10% and bottom 10% of the frame free from text, logos, icons, buttons and UI elements — photographic content such as product edges entering the frame is fine."

**Plantilla modo reference:**
> "[RATIO] aspect ratio. Image 1 shows a reference ad layout from another brand. Use it as a structural template only — keep the layout format, zone positions, element placement and spacing. Replace everything visual with this brand's identity: background [BG], typography [descrita], accents [ACCENTS]. Replace the product with the exact product from images 2+. Replace all copy with: [COPY]. Replace any third-party badge with [TRUST SIGNAL]. Do not carry over any color, typeface, logo or visual treatment from Image 1. [Safe zones como arriba]."

**Plantilla modo text:**
> "[RATIO] aspect ratio. Create: [FORMATO]. Background: [BG]. [ZONA POR ZONA]. Product: exact product from images 1+, do not redesign it. [Safe zones como arriba]."

Para 9:16 usa safe zones de 14% arriba y abajo (UI de stories/reels).

Puedes mostrarle el prompt al usuario si lo pide.

---

## Paso 8 — Generar

Una vez por variación, en secuencia:

```bash
python3 .claude/skills/static-ads/scripts/generate-static-ad.py brands/[brand]/static-ads/[output-name] var-1
```

Cada corrida guarda `[output-name]-[slug]_vN.png` (nunca sobreescribe) y un export al tamaño exacto del canal en `exports/` (4:5 → 1080×1350, 3:4 → 1080×1440, 9:16 → 1080×1920, 1:1 → 1080×1080).

Costo aproximado: ~US$0.15–0.25 por imagen en quality `high` (más con muchas imágenes de referencia). Para pruebas rápidas, `"quality": "medium"` en el spec.

Antes de generar un lote, confirma con el usuario el número de imágenes y el costo estimado.

---

## Paso 9 — Ratios adicionales

Desde el output primario, nunca desde otro reformat:

```bash
python3 .claude/skills/static-ads/scripts/generate-reformat.py brands/[brand]/static-ads/[output-name]/[output-name]-var-1_v1.png 9:16
```

Guarda `[output-name]-var-1_9x16_v1.png` + export exacto.

---

## Paso 10 — Revisión y entrega

Abre cada PNG generado con Read y revísalo antes de reportarlo:
- ¿El texto salió exacto (tildes, cifras, `elvo·`)? Si hay errores de texto, regenera esa variación.
- ¿El producto es fiel a la foto real (logo, gota, forma)? Si no, regenera o recomienda componer el recorte real encima.
- ¿Respeta la paleta (glaciar como destello, no campo) y las safe zones?
- ¿Se coló algo de la marca de referencia?

Lista los archivos generados con su veredicto (ok / regenerar y por qué). Pregunta si regenera alguna variación, ajusta copy o prueba otro formato.

- Regenerar igual: vuelve a correr el script (crea `_v2`).
- Cambiar copy: edita el `prompt` de esa variación en el spec y vuelve a correr.

---

## Ejemplo de referencia — Ingredient / etapa spotlight (elvo·)

"4:5 vertical aspect ratio. Static ad. Image 1 is a neutral grey wireframe for placement only. Images 2+ show the exact product; reproduce it faithfully. Background: flat matte alabaster #EAE7E0, no gradients. Top zone: small rectangular label "LA FORMULACIÓN" in deep slate #2B2E2D with off-white #F3F1EC uppercase text, wide letter-spacing, clean neutral grotesque sans-serif. Below, left-aligned: large light-weight high-contrast serif headline "Seis etapas." in charcoal #1C1E1C. Middle-left: macro photo of activated carbon granules on pale stone with a few droplets carrying a subtle glacial-aqua tint, shallow depth of field, soft cool side-light, about 35% of the frame. Beside it, three stacked rows with a thin 1px glacial-aqua #82C3C4 left rule, charcoal grotesque text: "Retiene: plomo y metales pesados*" / "Reduce: cloro, olores y sabores" / "Conserva: los minerales del agua". Lower right: the product from images 2+, slight angle, soft side-light, partial crop allowed. Small circular badge in deep slate #2B2E2D with off-white text "Lo instalas en 5 minutos". Bottom: tiny stone-grey #9A948A text "*Según la ficha técnica del núcleo PureCore." Generous negative space, editorial apothecary aesthetic. No exclamation marks, no extra text, no stars, no CTA button. Safe zones: keep the top 10% and bottom 10% free from text, logos, icons and buttons."
