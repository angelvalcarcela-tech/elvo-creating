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
