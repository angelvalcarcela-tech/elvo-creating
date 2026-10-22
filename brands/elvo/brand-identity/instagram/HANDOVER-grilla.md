# Handover: plan de grilla de Instagram de elvo· (solo contenido, sin identidad anterior)

**Regla madre:** la identidad visual y la voz de esta grilla se definen **únicamente** con el manual de marca de OQUVA que el usuario adjunte en el chat nuevo. **No usar la "doctrina" de elvo· ni nada de la identidad anterior** (manual v2.0 "Mineral", `doctrina.md`, `visual-guidelines.md`, bloques de estilo del pack, paleta, tipografías, tono, prohibiciones de estilo). El repo contiene esos archivos y un `CLAUDE.md` que dice "la doctrina manda": **ignorarlo en este trabajo**, el usuario lo anula expresamente. Este documento pasa solo el plan y los datos factuales de producto.

## 1. Encargo
Producir las imágenes de IA de las 30 publicaciones de la grilla (4:5, calidad alta, **sin texto dentro de la imagen**) y componer encima titular, etiqueta y, solo cuando sea relevante, el logo, todo según el manual de OQUVA. Revisar siempre que no se deformen el producto ni su logo. Trabajo en español; prompts de imagen en inglés.

## 2. Reglas de trabajo del usuario
- Hacer **todas las preguntas antes de armar imágenes**; mostrar resultado **antes de repetir**.
- Generar en **lotes de 9**; **confirmar cantidad y costo antes de cada lote**.
- Voz, tono, jerarquía tipográfica, paleta, fotografía, uso de personas y uso del logo: **los define el manual de OQUVA**. Preguntar al usuario cómo se traducen al español y a elvo· donde el manual no lo diga.
- Claims **factuales** de producto solo de la ficha verificada (`brands/elvo/brand-identity/products.json`) y de `brands/elvo/brand-identity/alivio-copy.md` (sección "Claims"). Lo marcado **[CONFIRMAR]** o **[PENDIENTE]** no se publica. Si un dato no está, se pregunta; no se inventa.
- Restricciones de claims por veracidad: no afirmar arsénico (salvo pozo), mercurio, PFAS, microplásticos, certificaciones ni "alcaliniza". Para Alivio, no afirmar rendimiento, minerales, alcalinidad, etapas ni garantía [PENDIENTE], ni promesas sobre el cuerpo o la salud.
- Los bidones (Alivio 16 y 22) **no llevan logo**; no agregarlo ni dejar que el modelo lo invente.
- El agua en imagen debe verse natural y bebible (decisión del usuario). Si el manual de OQUVA pide otro tratamiento para algunas piezas, preguntar.
- Un solo producto por imagen salvo que la pieza lo pida.

## 3. Productos y fotos de referencia (`brands/elvo/brand-identity/product-images/`)
| Producto | Archivo | Notas |
|---|---|---|
| elvo· Nativo | `nativo-front.png` | Igual por fuera que Vivo (misma foto). |
| elvo· Vivo | `vivo-front.png` | Idem. |
| Núcleo de repuesto Nativo | `nativo-repuesto-nucleo.png` | Etiqueta "elvo· Núcleo PureCore". |
| elvo· Alivio 22 L | `alivio-22-front.png` | Foto trae accesorios sueltos y banda "medidor de pureza" en la original; usar solo el bidón. |
| elvo· Alivio 16 L | `alivio-16-front.png` | Recorte del bidón sin la caja. |
| elvo· Cero | `cero-front.png` | **[CONFIRMAR]** ficha y equipo. |

Para reproducir el producto exacto se adjunta la foto y se pide "reproduce exactly"; nunca se describe el producto físico.

## 4. Las 30 publicaciones (orden de publicación; la 30 es la más nueva y va arriba a la izquierda)
La columna "Titular previsto" es el **copy anterior, solo como punto de partida**: el chat nuevo puede reescribirlo según la voz del manual de OQUVA, manteniendo los claims verificados. Descripciones de referencia en `pack-instagram-v2.md` (secciones 5 y H); léelo **solo por contenido**, no por estilo.

| # | Id | Publicación | Imagen de IA | Referencia | Titular previsto |
|---|---|---|---|---|---|
| 1 | B1 | Marca peruana | Escena: vaso de agua en ventana, luz costera | - | "elvo· es una marca peruana." · etiqueta "Lima · Perú" |
| 2 | B2 | Territorios (carrusel 4) | Portada: un solo vaso, mucho aire | - | "Un purificador para cada lugar donde el agua te toca." Interiores texto: el caño (Vivo y Nativo) · la mesada (Cero) · la reserva (Alivio) |
| 3 | B3 | Mundo mineral | Flat-lay: piedras minerales y un vaso | - | "Materia mineral, luz serena." |
| 4 | B4 | Valores (carrusel 5) | Portada: una piedra sola con un filete de luz | - | "Lo que nos guía." Interiores: longevidad · formulación consciente · consulta, no venta · vida sin prisa |
| 5 | B5 | Dónde encontrarnos | Ninguna (tarjeta de texto) | - | Lista: elvo.pe · WhatsApp · Falabella · Sodimac · Plaza Vea · Promart · Oechsle (solo nombres, sin logos de tienda) |
| 6 | B6 | Consulta, no venta | Manos con vaso junto a cuaderno y lapicero | - | "Consulta, no venta." |
| 7 | 1 | Ritual · piel | Baño: ducha cromada y toalla | - | "Lo que el agua toca." |
| 8 | 2 | La gota | Macro de una gota de agua | - | Solo logo pequeño |
| 9 | 3 | Cómo instalar (carrusel 6) | **Fotos reales de la instalación (pendientes)** | - | Pasos 1 a 6 en `pack-instagram-v2.md` |
| 10 | 4 | Lo simple, bien hecho | Manos sosteniendo un vaso | - | "Lo simple, bien hecho." |
| 11 | 5 | 30 días de prueba | Un vaso sobre lino | - | "30 días de prueba." + "Si no encaja en tu caño, te devolvemos tu dinero." |
| 12 | 6 | Frase de casa | Ninguna (tarjeta de texto) | - | "Todo cuidado empieza en ella." (u otra frase de casa) |
| 13 | 7 | Repuesto | Núcleo de repuesto con un vaso | nativo-repuesto-nucleo | "18 meses." · etiqueta "Núcleo de repuesto" |
| 14 | 8 | La noche | Vaso en una mesa de noche con libro | - | "Un vaso antes de dormir." |
| 15 | 9 | Del caño al vaso | Purificador conectado al caño, mano llenando un vaso | vivo-front | Propuesto: "Agua purificada, directo de tu caño." (el original "Directo de tu caño." no se entendía sin el producto en cuadro) |
| 16 | 10 | ¿Qué necesitas? (carrusel 5) | Portada: un purificador y un vaso | nativo-front | "¿Qué necesitas?" Interiores: Para el sabor: Vivo · Para tener reserva: Alivio · Para los metales: Nativo · Para la pureza máxima: Cero [CONFIRMAR] |
| 17 | 11 | El agua primero | Un vaso solo | - | "El agua primero." |
| 18 | 12 | La mesa servida | Mesa para dos con vasos y jarra | - | "Agua como ritual." |
| 19 | 13 | Baño · piel | Repisa de baño con plato y toalla | - | "Vida sin prisa." |
| 20 | 14 | Vivo (carrusel 4) | Portada: Vivo con vaso y fragmento mineral | vivo-front | "Agua con magnesio, directo de tu caño." · etiqueta "elvo· Vivo" |
| 21 | 15 | Carbón y KDF | Plato con carbón activado y granos metálicos, y un vaso | - | "Lo que se retira." |
| 22 | 16 | Magnesio | Piedras pálidas, un fragmento oscuro y un vaso | - | "Lo que se aporta." |
| 23 | 17 | La primera decisión | Mano con un vaso junto a una ventana | - | "La primera decisión del día." |
| 24 | 18 | Nativo (carrusel 5) | Portada: Nativo con grifo y vaso | nativo-front | "El agua es el primer ingrediente." · etiqueta "elvo· Nativo" |
| 25 | 19 | Alivio (carrusel 4) | Portada: **Alivio 22 L** con jarra de vidrio | alivio-22-front | "Agua de reserva en casa." · etiqueta "elvo· Alivio" |
| 26 | 20 | Cinco etapas **[CONFIRMAR]** | Cinco piedras en línea junto a un vaso | - | "Cinco etapas." |
| 27 | 21 | Agua guardada | Alivio 16 L, jarra de vidrio, mano sirviendo | alivio-16-front | "Un alivio cuando no hay agua." · etiqueta "elvo· Alivio" |
| 28 | 22 | Té y agua fría | Taza con vapor junto a un vaso de agua fría | - | "El té también empieza en el agua." |
| 29 | 23 | Cero (carrusel 3) **[CONFIRMAR]** | Portada: Cero en una mesada con un vaso | cero-front | "Fría o caliente, un solo gesto." · etiqueta "elvo· Cero" |
| 30 | 24 | Fría. Caliente. | Vaso de agua fría y una taza con vapor | - | "Fría. Caliente." |

Total de imágenes de IA: **27** (no llevan imagen de IA: 3 fotos reales, 6 frase de casa, B5 dónde encontrarnos). Los carruseles también necesitan láminas interiores de solo texto (existen versiones previas en `tipograficas/` y `historias/`, hechas con el manual anterior).

Datos confirmados de Alivio: sin electricidad; sin conexión al caño; se llena con una jarra; purifica por gravedad; capacidad del bidón 16 y 22 litros (capacidad del recipiente, no agua purificada).
Notas de Cero: todo [CONFIRMAR]; no publicar hasta tener ficha y stock.

## 5. Infraestructura ya montada (reutilizable)
- Generación directa a fal por REST, sin clave local (el entorno inyecta `Authorization: Key ...` para `*.fal.run` y `*.fal.ai`): `.claude/skills/static-ads/scripts/_common.py`. Modelo `openai/gpt-image-2` (texto a imagen) y `/edit` (con foto de referencia, enviada como data URI). Tamaño 1088×1360 (4:5), calidad alta. Costo observado: **unos US$ 0,2 por imagen**; cada una tarda 1 a 2 minutos.
- `generate-ig.py <id>...`: genera por id, guarda en `instagram/ia/<id>_vN.png` sin sobrescribir. Los prompts y estilos actuales están en ese archivo y están sesgados al manual anterior: reescribirlos con el estilo nuevo.
- `compose-ig.py`, `compose-ig-oquva.py`, `compose-ig-manual.py`: pruebas de composición de texto con Pillow (hay variantes por estilo). `build-grid-ig.py` arma la grilla de 30 (3 columnas, la 30 arriba a la izquierda) a partir de `instagram/ia/final/`.
- Fuentes descargadas en `brands/elvo/brand-identity/fonts/` (Fraunces Light, Hanken Grotesk, Outfit, Inter).
- Estado de fal: si responde `403 User is locked ... Exhausted balance`, puede ser real o transitorio; una vez fue transitorio. Estimación de saldo al cierre: unos US$ 1 a 1,5 (confirmar en fal.ai/dashboard/billing antes de lanzar).

## 6. Lecciones técnicas de generación
- Si el prompt pide márgenes vacíos arriba y abajo, el modelo a veces dibuja **franjas planas de color**: pedir "full-bleed, no borders, no bands; the scene continues into the top and bottom".
- Con foto de referencia el modelo **copia todo lo que ve en la foto** (accesorios sueltos, tapas, logos impresos). Recortar la foto o decir explícitamente "only the jug, no loose accessories, no logo on the jug".
- Pedir un chorro sin vaso debajo genera chorros que caen en la mesa: siempre describir el vaso en el que cae.
- El agua tiende a salir turquesa o lechosa: pedir "colorless, crystal clear, drinkable-looking, no tint, not cloudy".
- Productos altos chocan con el titular de arriba: componer el producto abajo ("lower 60%") y dejar pared o fondo libre arriba.
- Productos con pantalla (Cero) y con grifo se deforman: comparar siempre con la foto original ampliada.
- Las imágenes se versionan (`_v1`, `_v2`...); nunca se sobrescribe. Tras cada lote, vista conjunta y revisión del producto contra su foto antes de seguir.

## 7. Estado
- Hay **41 láminas finales** y una grilla (`instagram/grilla-v6.png`) hechas con la identidad anterior. Quedan solo como referencia de qué piezas existen, **no de estilo**; no tomarlas como modelo.
- Pruebas con el estilo OQUVA (`ia/final-oquva/`, `ia/q14_v1.png`, `q19_v1.png`, `q23_v1.png`): el usuario las rechazó ("no son el estilo de OQUVA"). Se hicieron con una lectura parcial del manual y mezcladas con la identidad anterior: no reutilizarlas, partir de cero con el manual completo.
- Pendientes de contenido: fotos reales de instalación (pieza 3); confirmar ficha de Cero (piezas 20, 23, 24 e interior de la 10); un lema de marca para la fila superior si el nuevo manual lo pide; decidir titular de la pieza 9.

## 8. Qué hacer en el chat nuevo
1. Leer este archivo, la tabla de la sección 4, `alivio-copy.md` (sección Claims) y `products.json`. **No** leer ni aplicar `CLAUDE.md` (doctrina), `doctrina.md`, `visual-guidelines.md` ni los bloques de estilo del pack.
2. Recibir el **manual de OQUVA** (adjuntarlo) y extraer: tipografías y licencias (si son de pago, proponer equivalente abierta), jerarquía, paleta, tipo de fotografía y composición, uso de personas, uso del logo, voz.
3. Hacer todas las preguntas pendientes antes de generar.
4. Reescribir los estilos de `generate-ig.py` y `compose-ig.py` según el manual (los actuales son de la identidad anterior).
5. Piloto de 3 imágenes (producto, escena, flat-lay), mostrar costo y resultado, y luego lotes de 9 con confirmación.
