# elvo· — Visual & voice guidelines v3 (para static ads)

Estilo gráfico: sistema "cobalto + cúpula de luz" (referencia visual: caso de estudio OQUVA, solo estilo). Mercado: Perú. Idioma del copy: español. Prompts de imagen: inglés.
La versión anterior (mineral: alabastro/pizarra/glaciar + serif) queda archivada en `visual-guidelines-mineral.md`.

## Qué se toma y qué NO de la referencia
- SÍ: paleta azul, tipografía geométrica, cúpula translúcida, textura de puntos, pills con contorno, línea de flujo, callouts numerados, fotografía limpia.
- NO: el logo/símbolo de la referencia, su nombre, su tagline, ninguna cifra ni claim (micras, etapas, "zero-plastic"). Todo dato sale de `products.json`. El logo siempre es `elvo·` con gota.

## Esencia
Precisión + calma, ahora con aire de tecnología de diseño: objeto considerado, no aparato escondido. El agua como ingrediente. Voz de `doctrina.md` intacta: sin miedo, sin urgencia, sin exclamaciones.

## Paleta
| Rol | Nombre | HEX | Uso |
|---|---|---|---|
| Acento | Cobalto | #2F5BFF | fondos de impacto, cúpula, CTA sólido |
| Acento 2 | Periwinkle | #7C9BE8 | degradados suaves, texturas de puntos |
| Base | Niebla azul | #9EB8CF | paneles grandes (fondo de titular) |
| Base | Hielo | #DCE6EE | superficies claras, tarjetas |
| Base 60% | Blanco óptico | #FAFAFA | fondo por defecto |
| Texto | Tinta | #0A0F1C | titulares y cuerpo sobre claro |
| Profundidad | Abisal | #010A21 | fondos oscuros (agua cayendo, macro) |
| Neutros | Grises | #D9D9D9 → #6E6E6E | etiquetas, filetes, disclaimers |

- Combinaciones: blanco + cobalto; niebla azul + blanco; abisal + hielo.
- Degradado permitido y característico: cobalto → periwinkle → blanco, vertical, con cúpula translúcida de borde luminoso. Sin otros degradados, sin sombras duras, sin saturación extra.

## Tipografía (describirla en el prompt, no nombrar la fuente)
- **Titular:** sans geométrica ancha, regular a bold, tracking ajustado, en minúscula/frase (no gritar). En prompt: "wide geometric grotesque sans-serif, regular to bold, tight tracking, sentence case".
- **Cuerpo/datos:** grotesca neutra limpia, peso ligero. En prompt: "clean neutral grotesque sans-serif, light weight".
- **Etiquetas técnicas:** mayúsculas pequeñas con tracking amplio, estilo mono-técnico: "01 // EL AGUA, SIN RUIDO".
- Alineación a la izquierda. Jerarquía por escala. Mayúsculas solo en etiquetas, nunca en titulares.

## Motivos gráficos
1. **Cúpula translúcida:** arco grande de luz con borde brillante sobre degradado cobalto/blanco; el producto o el texto viven sobre ella.
2. **Textura de puntos (dither/halftone):** azul periwinkle sobre blanco, para fondos de sección y bordes de degradado.
3. **Pills con contorno:** cápsulas de 1 px, texto pequeño, para señales ("Lo instalas en 5 minutos", "Garantía de 1 año"). Sobre foto: relleno blanco translúcido.
4. **Línea de flujo:** tres nodos conectados con flecha: "Caño → Núcleo → Vaso". Hairline de 1 px, círculos numerados 01 02 03.
5. **Callouts técnicos:** líneas finas desde el producto a etiquetas numeradas (01–04) con nombre del componente en mayúsculas pequeñas; fondo claro con cuadrícula tenue.
6. **Hairlines y marcas de registro:** filetes de 1 px, cruces pequeñas en esquinas, rejilla muy tenue.
7. **Bandas borrosas verticales:** franjas celestes desenfocadas sobre blanco, para fondos de calma.
8. Esquinas redondeadas (radio generoso) en tarjetas y paneles.

## Logotipo
`elvo·` en minúsculas con gota, en tinta sobre claro y en blanco sobre cobalto/abisal. Nunca "ELVO", nunca con efectos. En la foto real del producto el logo es sans redondeado gris: no se modifica.

## Composición
Un sujeto, una idea. Formatos recurrentes:
- **Panel dividido:** mitad niebla azul con titular claro, mitad foto del producto sobre mesada de piedra.
- **Cúpula:** degradado cobalto, cúpula, titular arriba, producto o logo abajo.
- **Anatomía:** fondo claro con cuadrícula, producto/núcleo al centro, 3–4 callouts numerados.
- **Macro oscuro:** fondo abisal, chorro de agua en macro, una línea de dato en hielo.
Mucho aire; safe zones libres.

## Fotografía / luz
Cocina sobria, mesada de piedra pálida, grifería de acero, luz natural lateral suave y fría. Agua macro sobre negro con luz de borde, tinte azul tenue (no saturado). Personas: bebiendo agua con naturalidad, sin dramatismo ni gesto de dolor/miedo. Producto siempre a la vista, nunca escondido.

## Voz
- Precisa, sensorial, serena. Observación en lugar de alarma.
- La cifra antes que el superlativo ("Retiene plomo y metales pesados*", no "la mejor agua").
- **Sin signos de exclamación. Sin emoji. Sin urgencia. Sin superlativos vacíos.**
- Líneas de casa: "El agua que entra a tu cuerpo es una decisión." · "El agua es el primer ingrediente."

## Señales de confianza permitidas (pills / CTA / disclaimer)
Pago contra entrega · Envío gratis a todo el Perú · Garantía de 1 año · 30 días de prueba · Hasta 6 cuotas sin intereses · Lo instalas en 5 minutos · Te avisamos por WhatsApp cuando toca cambiar el núcleo · Si no encaja en tu caño, te devolvemos tu dinero.

CTA serenos (botón cobalto sólido, texto blanco): "Conoce elvo· Nativo", "Ver planes", "Escríbenos por WhatsApp", "Elige tu plan".

## Prohibido (doctrina)
Cuentas regresivas, "quedan N", barras de stock, escasez inventada, descuentos gritados, flechas rojas, "STOP", caras de miedo, agua sucia como amenaza, contaminación local sin respaldo, ansiedad corporal o de edad, testimonios inventados, estrellas/reseñas inexistentes, comparativas con marcas competidoras. Además: ninguna cifra, claim, tagline ni símbolo de la referencia OQUVA.

## Reglas para prompts de imagen
1. La primera frase es el formato: "4:5 vertical aspect ratio."
2. Nunca describir el producto físico: se adjunta la foto real y se pide reproducirla exacta.
3. Todo texto entre comillas, exacto, corto.
4. Safe zones: 10% arriba y abajo (14% en 9:16) libres de texto, logos y botones.
