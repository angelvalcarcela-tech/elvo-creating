# Meta Ads — borrador reconstruido desde cero (24-oct-2026)

Cuenta 893663859368314 (USD) · Página AQA Filtros Perú 383158558224028 · IG @elvo_filtros 17841460108164627 · Pixel 899375412789001 · Destino https://www.elvo.pe/products/elvonativo (UTM: utm_campaign=nativo_lima | nativo_provincias | nativo_remarketing, utm_content=slug).
Estado: **BORRADOR**, nada publicado. El usuario borró todos los borradores anteriores y se reconstruyó todo (los IDs viejos ya no existen).

Cada anuncio es un creativo inline con `asset_feed_spec`: 4:5 en feed/explorar y 9:16 en historias/reels (FB e IG), `contextual_multi_ads` y mejoras automáticas en OPT_OUT (sin "contenido multimedia relacionado"). Sin declaración de contenido generado con IA (decisión del usuario). Un solo mensaje por anuncio, CTA SHOP_NOW.

## Prospección — campaña 120255012416420401 (CBO US$40/día, OUTCOME_SALES)
- **LIMA** ad set 120255012417100401: círculo 35 km (-12.0464, -77.0428), 25-65, excluye compradores 180d (120255011194460401), tope diario US$32.
  manana 120255012417890401 (prueba) · bidones 120255012423680401 · familia 120255012423820401 · caja 120255012423970401 · instalas 120255012424410401 · resena 120255012424630401
- **PROVINCIAS** ad set 120255012417190401: Perú excluyendo el círculo de Lima, tope diario US$16.
  manana 120255012424850401 · familia 120255012424970401 · caja 120255012425400401 · instalas 120255012425600401 · resena 120255012425690401 · retail 120255012426400401

## Remarketing — campaña 120255012416560401 (CBO US$15/día), ad set 120255012417320401
Visitantes web 30d (120255011194330401) + interacción FB 90d (120255011956700401) + IG 90d (120255011956800401), excluye compradores.
prueba 120255012426730401 · masvendido (4,2 · 124 reseñas Falabella, confirmado por el usuario) 120255012426980401 · maselegido 120255012427160401 · duracion 120255012427330401 · retail 120255012427420401

## Hashes de imagen (cuenta 893…)
4:5: manana 5388c96da082f96ca3acce57014001c0 · bidones 1a347ce5aa95e7661256a2e11c782cc6 · familia c609a6a11144997d5260f81918389f18 · caja 57adb3eb0cd882fb8dbedd2e0614b4fd · instalas 69ee0182052c50136b96cae31bd53794 · prueba 6fb221adc9c54ea2669009f9f9c88710 · resena ee2ac8567b1dc6db89ad0e8c5fe1970f · maselegido d82a38dc808ee84ef51f4cf1644d4b9a · duracion 2394ac623cd9bb0d8713a55b0c18588f · masvendido cfd6415ab5b8e87f2f47e911f22be414 · retail 2b2d2799c35a18d67b9a02ce69438677
9:16: manana b8857312089670b3430c8ecf4280074a · bidones 0e4c523f588c71fed3bf4f03ca6e466e · familia 885d72ea602f84d096794cd006f6650b · caja efd491039eb70e4ce1bcd5f3cc33bbf4 · instalas 40a5138cc2a4aeea084d35c0ceba791b · prueba 9dac3bc199a33e39929b5eeb5a6e8b97 · resena c6fe05b4a1010283e8b698b0258d0c57 · maselegido 923e7086f9fefcfd070c5637bafa8519 · duracion 44753a2b02e52658f8b53a185c66da83 · masvendido 3a1ed7a5decad9405a5c52cf63792649 · retail d42b736be4f136b60e1cc6465e1c7baf

## Pendiente
- Revisión del usuario en Ads Manager y OK explícito; publicar solo estos objetos por ID.
- Videos del usuario como campaña aparte (la cuenta no tiene ninguno cargado).
- Tamaño de las audiencias de remarketing (muy pequeñas) antes de publicar.

## v3 limpio (26-oct-2026): estructura simple, todo en BORRADOR (nada publicado)
El usuario borró todo lo anterior y pidió cargar de nuevo con un solo conjunto por público, imagen 4:5 en todas las ubicaciones (ubicaciones automáticas). Creativos de imagen única sin descripción ni enlace visible (evita el error #1815589 "título y descripción obsoletos"; Meta no muestra esas líneas en anuncios de imagen única).
- Campaña **ELVO | Nativo | Compra web | Prospección v3** 120255022621530401 (CBO US$40):
  P1 Lima 35 km 120255022622150401 (tope US$32) · P2 Perú sin Lima 120255022622180401 (tope US$16). 25-65, excluye compradores 120255011194460401.
- Campaña **ELVO | Nativo | Compra web | Remarketing v3** 120255022621680401 (CBO US$15):
  R1 120255022622350401 (Carrito 60d, Checkout 60d, Visitantes 30d, Interacción 180d; sin compradores).
- 17 anuncios 4:5: Lima manana/bidones/familia/caja/instalas/resena (6) · Provincias manana/familia/caja/instalas/resena/retail (6, hashes únicos por píxel) · Remarketing prueba/masvendido/maselegido/duracion/retail (5).
- UTM: utm_campaign=nativo_lima | nativo_provincias | nativo_remarketing, utm_content=slug.
Pendiente: revisión del usuario en Ads Manager y "publica" explícito (conjuntos y anuncios primero, luego campañas, por ID); videos como campaña aparte.

## Estado actual (26-oct-2026): versión original con feed 1:1 + Historias/Reels 9:16, todo en BORRADOR
Meta exige 1,91:1 para Feed de Facebook, así que las imágenes de feed se regeneraron en 1:1 (1080×1080) con generate-reformat.py.
- Campaña **Prospección (Lima + Provincias)** 120255022971680401 (US$40): LIMA 120255022973540401 (tope US$32), PROVINCIAS 120255022973820401 (tope US$16).
- Campaña **Remarketing** 120255022972040401 (US$15): conjunto 120255022973860401 (Carrito 60d, Checkout 60d, Visitas 30d, Interacción 180d; sin compradores).
- Anuncios "… | 1x1" (17): feed 1:1 (img_feed) + 9:16 (img_story); ubicaciones solo Facebook e Instagram.
- Hashes 1:1: manana 4bf4d16a…, bidones 5a5bc7d3…, familia e2bc81d9…, caja f01c2fc9…, instalas 5f84ae7d…, resena 7181ac01…, prueba afc7867a…, masvendido 399ea79b…, maselegido 00985198…, duracion 0dfaf31e…, retail 90d8881f….
- Los anuncios viejos sin "1x1" (imagen 4:5) deben borrarse a mano antes de publicar.

## Actualización: feed en 1,91:1 (Meta lo exige en Feed de Facebook; entra también en el rango de Instagram Feed)
Anuncios "… | feed 1.91" (17) en los conjuntos LIMA 120255023215620401, PROVINCIAS 120255023215750401 y REMARKETING 120255023215890401 (campañas 120255023213110401 y 120255023213290401). Feed 1200×628 + Historias/Reels 9:16, solo Facebook e Instagram.
Hashes 1,91:1: manana 012facac…, bidones 0eac4842…, familia e353a9f1…, caja 9c77baec…, instalas 1951e86f…, resena b4214235…, prueba 35cd5bf9…, masvendido 9adb2cf8…, maselegido 58843086…, duracion 596e0d36…, retail 7a69ce24….
Borrar a mano: anuncios de prueba (PRUEBA…), el conjunto "ZZ PRUEBA | Solo Facebook Feed" y cualquier anuncio sin "feed 1.91".

## Estado vigente (reconstruido, 1.91:1 feed + 9:16 stories, solo FB + IG) — BORRADORES

Reemplaza los IDs anteriores (borrados a mano en Ads Manager).

**Campaña Prospección** `120255023618650401` (CBO US$40/día)
- Ad set LIMA `120255023623070401` (tope 32/día): manana `120255023627220401`, bidones `120255023630140401`, familia `120255023632740401`, caja `120255023634670401`, instalas `120255023635950401`, resena `120255023638100401`
- Ad set PROVINCIAS `120255023623370401` (tope 16/día): manana `120255023640060401`, familia `120255023642210401`, caja `120255023643620401`, instalas `120255023644630401`, resena `120255023647430401`, retail `120255023649530401`

**Campaña Remarketing** `120255023619100401` (CBO US$15/día)
- Ad set REMARKETING `120255023623730401`: prueba `120255023651480401`, masvendido `120255023653170401`, maselegido `120255023655590401`, duracion `120255023657270401`, retail `120255023659010401`

Formato: asset_feed_spec con img_feed (1200x628) -> FB feed / IG stream+explore y img_story (1080x1920) -> FB/IG story + reels. Nada publicado; esperar "publica".

## Estado vigente v4 (4:5 feed + 9:16 stories, como N2/C1v2/C9v3; solo FB + IG) — BORRADORES

Reemplaza los IDs anteriores (1.91:1, borrados a mano). Feed = hashes `v3-*` (1080x1350), stories = `s-*`/`manana_v2_916`/`retail_rmk_9x16` (1080x1920).

**Prospección** `120255024123900401` (CBO US$40/día)
- LIMA `120255024127880401` (tope 32): manana `120255024128990401`, bidones `120255024130280401`, familia `120255024130800401`, caja `120255024130950401`, instalas `120255024131390401`, resena `120255024131990401`
- PROVINCIAS `120255024127960401` (tope 16): manana `120255024132830401`, familia `120255024133360401`, caja `120255024133560401`, instalas `120255024134210401`, resena `120255024134470401`, retail `120255024134770401`

**Remarketing** `120255024124000401` (CBO US$15/día)
- REMARKETING `120255024128020401`: prueba `120255024135190401`, masvendido `120255024135530401`, maselegido `120255024135820401`, duracion `120255024137070401`, retail `120255024137570401`

Nada publicado; esperar "publica".

## Ronda v5 — reacciones (enojo/alegría/risa) + El Niño (Nativo) — BORRADORES sobre campañas ya publicadas

Las campañas v4 fueron publicadas por el dueño (activas, US$0 gastado al 26-oct). Estos 8 anuncios están en borrador (`action: add`, VALIDATED) dentro de los conjuntos existentes; no están al aire hasta publicar los cambios.

LIMA `120255024127880401`: enojo-bidon `120255024567560401`, enojo-hervir `120255024571300401`, alegria-listo `120255024572500401`, alegria-cero `120255024573950401`, risa-vida-social `120255024576400401`, risa-espalda `120255024577290401`, nino-turbia `120255024578370401`
PROVINCIAS `120255024127960401`: nino-turbia `120255024579260401`

Imágenes: `brands/elvo/static-ads/elvo-nativo-v4/` (4:5 + 9:16). Hashes feed/story: alegria-cero 457d5d25…/7cf49b66…, alegria-listo 8be230b1…/fc6cfda2…, enojo-bidon f50bab1a…/c2221761…, enojo-hervir 88b576b0…/2c5c91af…, nino-turbia f6a6e851…/e1324ea2…, risa-espalda 0aa9cb05…/1be06e92…, risa-vida-social a67f50d2…/31b8c5f9….

Claim El Niño: "El Niño Costero en alerta" (ENFEN comunicado 18-2026, 16-oct-2026; próximo comunicado 30-oct). Releer antes de publicar. Turbidez: claim verificado de products.json ("Reduce cloro, olores, sabores y turbidez").

## Alivio — estructura en borrador (sin anuncios aún)

Prospección `120255024856150401` (CBO US$25/día): LIMA `120255024860540401` (tope 20), PROVINCIAS `120255024860810401` (tope 10).
Remarketing `120255024856310401` (CBO US$10/día): REMARKETING `120255024860920401`.
Pendiente: imágenes (fal sin saldo 26-oct), copy aprobado, listar Alivio en Shopify (hoy "no listado"), landing `elvo.pe/products/elvo-bidon-16l`.

## Ronda v6 — zona segura de Facebook Feed (borradores, "zona segura 4x5")

Facebook Feed recorta ~10% arriba/abajo de una 4:5. Imágenes corregidas en `brands/elvo/static-ads/elvo-nativo-zonasegura/` (logo real pegado, titulares dentro). Los anuncios nuevos reemplazan a los de la ronda 4:5 original (Nativo activos) y a los 8 borradores de la ronda v5.

LIMA `120255024127880401`: enojo-bidon `120255024957810401`, enojo-hervir `120255024958590401`, alegria-listo `120255024959980401`, alegria-cero `120255024960930401`, risa-vida-social `120255024962800401`, risa-espalda `120255024965150401`, nino-turbia `120255024966070401`, manana `120255024972110401`, bidones `120255024972840401`, familia `120255024974020401`, caja `120255024974710401`, instalas `120255024975520401`, resena `120255024976120401`
PROVINCIAS `120255024127960401`: nino-turbia `120255024969400401`, manana `120255024976900401`, familia `120255024977520401`, caja `120255024978230401`, instalas `120255024978590401`, resena `120255024979470401`
REMARKETING `120255024128020401`: prueba `120255024980200401`, masvendido `120255024981670401`, maselegido `120255024982420401`, duracion `120255024983890401`

Borrar a mano en Ads Manager (borradores v5, ya reemplazados): `120255024567560401` (con error al marcarlo DELETED), `120255024571300401`, `120255024572500401`, `120255024573950401`, `120255024576400401`, `120255024577290401`, `120255024578370401`, `120255024579260401`.
Al publicar los "zona segura", pausar los anuncios activos equivalentes (mismos nombres sin "zona segura", 4x5 + 9x16) para no duplicar. El anuncio retail no se corrigió.

## WhatsApp — fichas (26-oct-2026, en preparación, NADA creado en campañas todavía)

Decisiones del dueño: WhatsApp 929 190 100; campaña aparte con conjuntos distintos por producto (Nativo / Alivio) para no mezclar aprendizaje ni tracking; solo Facebook Feed (sin Instagram, Stories ni Reels, 4:5); sin logo; atención 24 horas; el bot de YaVendio se actualiza por su cuenta; presupuesto derivado del CAC aceptado (pendiente: no hay un CAC definido en el repo).

Imágenes 4:5 (1080×1350) subidas a la cuenta 893663859368314 (hash): Nativo 18 meses `952720df40b0bc26429228c6f1a85264` · Nativo 3 años `a96668d3c737d72b6a52774a0fbea3d2` · Nativo 6 años `cfec2720c0b5540b3ef6bcb28e9d9e39` · Alivio 16 `45894e633346ebadb5b301ed8b3c7379` · Alivio 22 `9b0292075381e1baa3fcc0e3b81df146`.

Auditoría de zona segura (Feed recorta ~10 % arriba y abajo): las 5 fichas tienen el contenido entre ~10 % y ~90 % de la altura; la más justa es Alivio 22 (pill del título a ~10 %). Nativo 6 años usa otro layout (tarjeta enmarcada, beneficios en 2×2).

Mensajes precargados previstos: "Hola, quiero el Nativo 18 meses (S/ 349)" · "…Nativo 3 años (S/ 389)" · "…Nativo 6 años (S/ 489)" · "…Alivio 16 (S/ 159)" · "…Alivio 22 (S/ 198)". Respuestas rápidas: ¿Cuánto cuesta? / ¿Cómo se instala? / ¿Llegan a mi ciudad? / Quiero pagar al recibir.
Disclaimer de Nativo (metales pesados): "Según la ficha técnica del núcleo PureCore" va en el texto del anuncio, no en la imagen.

### WhatsApp — borrador creado (26-oct-2026, SIN publicar)
Campaña `120255038541140401` "ELVO | WhatsApp | Conversaciones | Feed FB" (OUTCOME_ENGAGEMENT, CBO US$11/día ≈ S/ 41 al tipo de cambio ~3.7; objetivo conversaciones, WhatsApp 51929190100, Página 383158558224028).
- Conjunto **Nativo** `120255038543220401` (tope US$7/día): 18 meses `120255038544510401` · 3 años `120255038545190401` · 6 años `120255038545710401`.
- Conjunto **Alivio** `120255038543270401` (tope US$5/día): Alivio 16 `120255038546350401` · Alivio 22 `120255038546510401`.
Targeting: Perú, 25-65 (sugerencia Advantage+), excluye compradores web `120255011194460401`. Ubicación: solo Facebook Feed (`publisher_platforms:["facebook"]`, `facebook_positions:["feed"]`). Creativos: ficha 4:5 sin logo, CTA WHATSAPP_MESSAGE, mensaje precargado por producto/plan.
Pendiente antes de publicar: bot de YaVendio con precios nuevos; confirmar que el 929 190 100 está conectado a la Página; publicar solo con "publica".

### WhatsApp — 4 anuncios más en borrador (26-oct-2026, SIN publicar)
Hashes: Nativo reseñas `b986b5c6f62fe1cc006204fd98181769` · Nativo dudas `8d2f2cfe3ef0fa4fde486e619963aaa9` · Alivio miedo v2 `74e559b984ec6336ea2d73dee2d8afd9` · Alivio reseña (Yoannis) `5e1aa77cc54b92fe5e054c21d70f33e2`.
- Conjunto Nativo `120255038543220401`: reseñas reales `120255038627650401` · lo que más preguntan `120255038627810401`.
- Conjunto Alivio `120255038543270401`: miedo `120255038628590401` · reseña real `120255038628830401`.
Con esto: Nativo 5 anuncios (3 fichas + 2), Alivio 4 (2 fichas + 2). Con US$11/día conviene dejar activos como máximo ~3 por conjunto al inicio; los demás en pausa.
La imagen de miedo v2 tiene el titular bajado por script (leve mancha clara donde estaba el texto original).

### WhatsApp — El Niño (datos de Gestión 19-oct-2026), 4 anuncios más en borrador, SIN publicar
Cierre "Que no te pase." + nombre completo "Bidón Alivio 16 Litros · S/ 159" (pedido del dueño: usar siempre el nombre completo en los ads de Alivio).
Hashes: 2017 v4 `620aa21141d71ee38a7ad9261317decb` · 7 millones v3 `322f169b88e347047f1ff4f4eb3faa69` · río de Lima v3 `5da65dc5952833bce52a28a2abe560c0` · turbidez Nativo v3 `f725ded5bfd762b4e69fabd5f647607f`.
- Conjunto Alivio `120255038543270401`: El Niño 2017 `120255038893950401` · 7 millones `120255038895230401` · el río de Lima `120255038895750401`.
- Conjunto Nativo `120255038543220401`: turbidez `120255038895960401`.
Totales en borrador: Alivio 7 anuncios (2 fichas, miedo, reseña, 3 El Niño); Nativo 6 (3 fichas, reseñas, dudas, turbidez). Con US$11/día activar como máximo ~3 por conjunto.
Pendiente: los anuncios de fichas de Alivio (16 y 22) aún usan "Alivio 16"/"Alivio 22" como titular y en la imagen; cambiar al nombre completo si el dueño lo confirma. Verificar cifras de Gestión antes de publicar. Datos citados: Atarjea cerró compuertas hasta 6 días en 2017; casi 7 millones (estimación de Gestión); 53 puntos críticos de huaico en la cuenca del Rímac (de 362 en Lima).

### WhatsApp — Alivio 22 L, El Niño (titulares más cortos), 3 anuncios en borrador, SIN publicar
Nombre completo "Bidón Alivio 22 Litros · S/ 198"; cierre "Que no te pase."; mensaje precargado "Hola, quiero el Bidón Alivio 22 Litros (S/ 198)".
Hashes: 22 L 2017 `f81173816bdeb341db3cac8a3ca3f8d8` · 7 millones `cffdca31caa6dc26cf9ca5ecc5d23af9` · toda la casa `d89c85879d5036d19a86693a46bfc188`.
Conjunto Alivio `120255038543270401`: 2017 `120255038935000401` · 7 millones `120255038935250401` · toda la casa `120255038936040401`.
Nota: en "toda la casa" el equipo queda pegado al borde derecho (ligeramente cortado); considerar regenerar. Alivio ahora tiene 10 anuncios en borrador; activar como máximo ~3 con US$11/día.

## Campaña Repuestos WhatsApp (borrador, 26-oct-2026)
- Campaña 120255039167520401 "ELVO | Repuestos | WhatsApp | Lanzamiento hasta el viernes" — CBO US$6/día (600 centavos). BORRADOR, sin publicar.
- Conjunto 120255039183210401: Perú, solo Facebook Feed, incluye compradores de bidón (120255033451230401), excluye compradores de kit (120255039152460401), Advantage+ audience apagado (solo la lista), WhatsApp 51929190100, CONVERSATIONS, termina 2026-10-31T04:59Z (vie 30-oct 23:59 Lima).
- Anuncios (todos dicen "Oferta de lanzamiento: envío gratis hasta el viernes"; mensaje prellenado "Hola, quiero el Kit de filtros de repuesto (S/ 99)"):
  - 120255039184450401 Cambia el filtro — hash a0cd2981b28a4e3023ac089b558e30ff
  - 120255039184960401 Cada cuánto — hash 29bc11a09121b639146352dde5cf464e
  - 120255039185080401 Lanzamiento envío gratis — hash 9cc8f3596d2d434aa8fd767bf560343c
- No se afirma "entrega este fin de semana" ni compatibilidad con bidones AQA antiguos (sin confirmar).

## Cyber elvo· — carrusel CTWA (27-oct-2026), BORRADOR
- Conjunto `120255041658470401` "WA | Cyber carrusel | Perú | Feed FB" dentro de la campaña WhatsApp `120255038541140401`: Perú 25–65, solo Facebook Feed, excluye compradores web 180d, Advantage+ audience, tope US$20/día, termina 2026-11-02T04:59Z (1-nov 23:59 Lima).
- Anuncio `120255041664570401` "WA | Cyber carrusel | 4 tarjetas v2" (carrusel WhatsApp, mensaje prellenado único "Hola, quiero la oferta del Cyber elvo·"). El primer intento `120255041659560401` falló por `degrees_of_freedom_spec` (mejoras estándar obsoletas) y se eliminó.
- Orden: Nativo `adffcbf5642286050266dfc4b675a594`, Vivo `9d5b774cfd5c68ef2d1a7ff2714c13d8`, Alivio 16 `796af38abcfe80d85d10181653b0e93c`, Alivio 22 `49c07b85cc9f8aa4016d51e59f9943ff`.
- Imágenes alojadas en Shopify Files como `cyber-elvo-*.png` (se subieron desde ahí a Meta).
- Precios en Shopify cambiados el 27-oct: Nativo 3 Años S/ 349 (tachado 598), Vivo 18 meses S/ 259. Revertir/revisar después del 1-nov.

### Cyber carrusel — PUBLICADO (27-oct-2026)
- Anuncio activo: `120255041765200401` "WA | Cyber carrusel | 4 tarjetas | urgencia" (texto: "Tu agua de casa tiene fecha límite: este domingo… Solo hasta este domingo…"). Conjunto `120255041658470401` activo, tope US$20/día, termina 1-nov 23:59 (hora Lima), en revisión de Meta.
- Borradores a borrar a mano: `120255041664570401` (v2, pausado) y `120255041659560401` (primer intento con error).
- Después del 1-nov: revertir Nativo 3 Años (S/ 349 → S/ 389) y revisar Vivo 18 meses (S/ 259).

## Cyber Stories (web) — BORRADOR (27-oct-2026)
- Campaña `120255057349560401` "ELVO | Cyber | Stories | Web" OUTCOME_SALES CBO US$20/día. Conjunto `120255057349800401`: Perú 25–65, Stories FB+IG, excluye compradores web 180d, pixel 899375412789001 PURCHASE, termina 1-nov 23:59 Lima.
- Anuncios: Nativo `120255057350170401` (hash 3f3c4fc3…), Alivio 16 `120255057350270401` (f3d7224b…), Alivio 22 `120255057350400401` (b1080858…), Cero `120255057350720401` (1b272540…). CTA Comprar, UTM cyber-elvo-oct26.
- Imágenes en Shopify Files `cyber-story-*.png`; fuentes en `static-ads/elvo-cyber-direccion/`.

## Diagnóstico entrega WhatsApp (27-oct)
- Campañas WA (`120255038541140401` y repuestos `120255039167520401`): ACTIVAS, 0 impresiones y US$0. Sin errores de bloqueo en ads_get_errors.
- Un anuncio antiguo "repuesto incluido v3 (929190100)" aparece con "WhatsApp Account Is Banned: phone number is banned from using WhatsApp". Ese es el mismo número de los conjuntos nuevos.
- Cuenta publicitaria activa y con método de pago; las campañas web sí entregan (≈US$24 en 3 días).

## WhatsApp recreado (27-oct, BORRADOR)
- Prueba de vinculación: el número 51929190100 es aceptado con la Página AQA Filtros Perú (383158558224028); con la Página "Elvo Peru" (980802948447615) da "This WhatsApp phone number is not linked to your account".
- Campaña `120255057359900401` "ELVO | Cyber | WhatsApp v2 (recreado)" (CBO US$20/día), conjunto `120255057360660401` (Perú 25–65, Feed FB, excluye compradores web), anuncio carrusel `120255057362320401` (4 tarjetas, texto de urgencia). Sin errores en el borrador. El conjunto de prueba `120255057360630401` (Elvo Peru) quedó marcado como eliminado.
- Siguen activos pero sin entrega los originales (carrusel `120255041765200401`, 16 anuncios, repuestos).

## Stories corregidos a zonas seguras (27-oct, BORRADOR)
- Medición: las piezas v1 dejaban 15.2% libre arriba y 17.7% abajo (regla Meta: ~14% arriba, ~20% abajo). Rehechas (`static-ads/elvo-cyber-direccion/elvo-cyber-{nativo,alivio16,alivio22,cero}_v2.png`): 15.2% arriba / 20.1% abajo.
- Hashes Meta v2: Nativo `dfd45a18…`, Alivio 16 `4548330f…`, Alivio 22 `16aa14a8…`, Cero `a002d1b6…`.
- Anuncios v2 en el conjunto `120255057349800401`: Nativo `120255057614930401`, Alivio 16 `120255057615270401`, Alivio 22 `120255057615840401`, Cero `120255057616520401`. Los v1 (`…350170401`, `…350270401`, `…350400401`, `…350720401`) quedaron pausados: borrar.
- Carrusel WhatsApp v2 (conjunto `120255057360660401`) pasó a solo Feed móvil: las imágenes 1:1 no sirven para Stories/Reels.
