# Pauta de revisión y subida — elvo· Nativo (17-oct-2026)

Para pasar a otro chat. Meta: S/30,000 de ganancia antes del 5-nov-2026. Todo se vende como **Nativo** (Vivo y Ritual quedan fuera de la pauta).

## 1. Cuentas y IDs
- Cuenta de anuncios Meta: `893663859368314` (USD). Es la de elvo. Las demás (AQA Filtros, inmobilia.pe) no se tocan.
- Pixel correcto: `899375412789001`. El pixel `2299638197551071` no dispara desde el 1-oct y no lo usa ningún conjunto.
- WhatsApp: 929 190 100. Link: `https://wa.me/51929190100`.
- Shopify: `cirhgx-8a.myshopify.com` (elvo.pe).
- Archivos de este trabajo (rama `claude/busy-ramanujan-vj9ftf`):
  - `PLAN-30K.md`: plan y cuentas.
  - `brands/elvo/static-ads/elvo-nativo-kit/`: 4 imágenes 4:5, `static-ad-spec.json`, `copy-meta.md`.
  - `brands/elvo/brand-identity/products.json`: única fuente de claims y cifras.

## 2. Economía (datos de Angel)
- Kit Nativo S/349 con purificador y 2 núcleos (el instalado + 1 de repuesto extra). Costo: purificador S/35 + repuesto S/10 = S/45 (sin envío ni comisiones). Contribución antes de ads: ~S/304.
- Punto de equilibrio por venta: US$77.
- Para S/30,000: S/30,000 / (304 - costo por venta en S/). Con costo por venta de S/25 a S/80, son 108 a 134 ventas en 19 días (6 a 7 por día).
- Histórico (2-sep a 15-oct, solo ventas con código de anuncio): 150 ventas, US$28.8 por venta, 2.3 ventas por 100 chats, ticket promedio S/334. La mitad de las ventas de YaVendio no trae código, así que el costo real es menor.
- Mejores formatos: "kit/repuesto incluido" y "piel y cloro" con 5 a 7 ventas por 100 chats (~US$14 por venta). Peor: W1 cuotas (4 ventas, US$122 por venta).
- Shopify desde junio: 231 pedidos; Nativo = 128 pedidos y S/44,172 netos (77%). Web Nativo: US$17 a 23 por compra en Meta (subcuenta porque los pedidos del formulario propio no disparan Purchase).

## 3. Estado actual de Meta (a las ~04:30 del 17-oct)
| Qué | ID | Estado | US$/día |
|---|---|---|---|
| Campaña CTWA-Kit-Oct16 | 120254899662830401 | Activa | — |
| Conjunto K Lima 17 km, Oferta kit (K1, K2, K3, K4) | 120254899663550401 | Activo | 60 |
| Conjunto P Provincia sin Lima 40 km, Shalom (P1, P2) | 120254899663710401 | Activo | 20 |
| Conjunto K+ "Nativo con núcleo incluido hasta 24-oct" (A, B, C) | 120254901204110401 | Publicado, estaba IN_PROCESS | 40 |
| Campaña WEB-Nativo-Oct26-v2 | 120254634459170401 | Reactivada | — |
| N-Miedo (C1, C6) | 120254634460880401 | Activado, estaba PUBLISHING | 15 |
| N-Carruseles-Feeds (C2, C6, C7) | 120254651137710401 | Activado, estaba PUBLISHING | 10 |
| RTG-Web-30d | 120254701874300401 | Activo | 6 |
| N-Confianza | 120254634462950401 | Pausado | — |
| N-Valor, N-RTG-7d | 120254634462340401, 120254634463270401 | Pausados | — |
| V-WhatsApp-Lima (Vivo) | 120254634465540401 | Pausado | — |
| Anuncio RTG-Web C9v2 Vivo | 120254701878960401 | Pausado | — |
Total ~US$151 por día. Campaña CTWA-Sofia-Cuotas (W1) sigue apagada: no volver a prenderla.

Borradores descartados de K+ (dejar en PAUSED, no publicar): 120254901208830401, 120254901223100401, 120254901223180401, 120254899664690401.

## 4. Qué revisar primero (en este orden)
1. Que K+ (`120254901204110401`) y sus 3 anuncios (`120254901234710401` A, `120254901234810401` B, `120254901235240401` C) estén en `effective_status` ACTIVE y no IN_PROCESS ni WITH_ISSUES.
2. Que N-Miedo y N-Carruseles estén ACTIVE y sus anuncios (C1, C1v2, C2, C6, C7) también. Los anuncios WITH_ISSUES de la campaña web (C12, C7, C2, C6 viejos) no se tocan.
3. Que el pixel de los 3 conjuntos web activos sea `899375412789001` con evento Purchase (lo era al 17-oct).
4. Gasto de las últimas 24 h por conjunto. Si K o P pasaron de US$0 de gasto y no hay entrega, revisar aprobación de anuncios.
5. Pedidos nuevos de YaVendio (conversaciones con `sale_status=positive`) y de Shopify del día.

## 5. Subir los 4 anuncios nuevos
Imágenes (4:5, 1122x1402, en `brands/elvo/static-ads/elvo-nativo-kit/`):
- `elvo-nativo-kit-kit-cloro_v1.png`
- `elvo-nativo-kit-kit-lima_v1.png`
- `elvo-nativo-kit-plomo_v1.png`
- `elvo-nativo-kit-kit-provincia_v1.png`

Bloqueo conocido: el entorno de Claude en la nube no puede subir imágenes a Meta porque la red bloquea `rupload.facebook.com`. Opciones: (a) agregar ese dominio en Allowed domains del entorno y repetir; (b) subir las imágenes en Ads Manager y usar sus `image_hash`; (c) dar URLs públicas y usar `image_url`.

Dónde van (los conjuntos K y P no usan creatividad dinámica, aceptan varios anuncios):
| Imagen | Conjunto | Texto principal | Titular |
|---|---|---|---|
| kit-cloro | K Lima 120254899663550401 | Purificador elvo· Nativo a S/349: viene con su núcleo instalado y 1 núcleo de repuesto extra. Pagas al recibir en Lima. | Menos cloro en tu vaso |
| kit-lima | K Lima | Tu purificador elvo· Nativo con repuesto incluido: S/349 con 2 núcleos. Pagas al recibir en Lima. Envío gratis a todo el Perú. | Con repuesto incluido |
| plomo | K Lima | elvo· Nativo retiene plomo y metales pesados* y reduce cloro, olores y sabores. S/349 con 2 núcleos incluidos. *Según la ficha técnica del núcleo PureCore. | Seis etapas de filtración |
| kit-provincia | P Provincia 120254899663710401 | Separa con S/50 por Yape y te enviamos tu elvo· Nativo por Shalom a tu ciudad. El resto lo pagas al recoger. S/349 con 2 núcleos incluidos. | Envío a todo el Perú |

Configuración de cada anuncio: botón WhatsApp (`WHATSAPP_MESSAGE`), página y WhatsApp de la cuenta, sin `link_url` propio (la herramienta pone el de WhatsApp). Los anuncios nuevos entran en PAUSED o DRAFT y se activan después.

Nota de presupuesto: dentro de un conjunto Meta reparte el gasto entre anuncios. Para fijar US$20 / 25 / 10 / 10 por anuncio, crear un conjunto aparte por anuncio copiando la segmentación de K o P:
- K: Lima, 17 km, edad 23-65, Advantage+ público activado, Facebook + Instagram (feed, marketplace, stories, reels, perfil), móvil, optimización CONVERSATIONS, destino WHATSAPP, facturación IMPRESSIONS, "Highest volume".
- P: Perú sin Lima 40 km (excluir radio 40 km desde -12.05, -77.04), mismos otros ajustes.
Reparto sugerido: kit-cloro US$20, kit-lima US$25, plomo US$10, kit-provincia US$10 (los dos de Lima salen del presupuesto de K, el de provincia del de P).

## 6. Cómo publicar (modo borrador de la herramienta)
- Crear anuncio con `ads_create_ad` deja un borrador. Publicar con `ads_activate_entity` pasando `object_ids` (conjunto + anuncios) y `publish_as_active=true` en el conjunto objetivo.
- Los cambios de presupuesto con `ads_update_entity` también quedan en borrador: hay que publicarlos con `ads_activate_entity` y `object_ids`.
- Pausar un objeto ya publicado es directo (`status: PAUSED`), no pasa por borrador. No llamar a `ads_activate_entity` después de una pausa.
- Los creativos no se editan: se crea uno nuevo.
- Verificar siempre con `ads_get_ad_entities` después de activar.

## 7. Reglas de copy
- Solo claims de `products.json`. Todo número sale de ahí.
- Prohibidos: mercurio, certificaciones, "garantía de por vida", lámpara UV de regalo, "rinde 20,000 litros" sin los 18 meses, reseñas o estrellas que no existan.
- "Retiene arsénico" solo en anuncios de pozo/provincia con "No reemplaza la cloración del agua de pozo". No se usó.
- Oferta correcta: "2 núcleos incluidos" (el instalado + 1 extra). Incorrecto: "2 núcleos de repuesto".
- Texto de Lima: "Pagas al recibir en Lima". Texto de provincia: "separas con S/50 por Yape, envío por Shalom, el resto al recoger". No mezclarlos.
- La regla de doctrina de marca la dejó de lado Angel; el tono sigue siendo sobrio.

## 8. Reglas de decisión (revisión del 19-oct y siguientes)
- Subir presupuesto si un conjunto da menos de US$29 por venta o más de 5 ventas por 100 chats. Bajar o pausar si pasa de US$77 por venta (punto de equilibrio) o gasta más de US$30 sin ventas.
- Si K+/K/P juntos no llegan a 6 ventas por día, subir gasto en el que mejor convierta antes de abrir otros.
- No reactivar: W1 cuotas, Vivo, los 5 anuncios sin ventas (que tiene agua familia, C13 Oct26, Elvo Nativo 1, A4B 30 días, Elvo Cero 4), posts viejos de "Quedan pocas unidades".
- Cruce de ventas: cada venta registrada de YaVendio (conversación positive) cuenta como venta concretada. Se une por código de anuncio del primer mensaje (`referral`) con el gasto de Meta. Sin código: no atribuible.

## 9. Pendientes que llevan otros chats
- Tema de Shopify nuevo (duplicar v5.9; 929 en vez de 917; garantía de 1 año; sin lámpara UV; cuenta regresiva al 24-oct; ver `§4` del contexto). La API no publica temas.
- Purchase del formulario propio: los pedidos como el #1263 no llegan a Meta como compra. Revisar envío server-side (Conversions API) o disparar el evento en la página de gracias.
- Auditoría por anuncio con el export de YaVendio ("Código de anuncio").
- Tarea semanal `trig_01AFZWRXgUT9ZjtM75LdyVn2` (lunes 8:48).

## 10. Actualización (17-oct, tarde): anuncios nuevos publicados
Imágenes subidas por Angel a la biblioteca de Meta (hashes) y anuncios creados con página 383158558224028, botón WhatsApp, `link_url` `https://api.whatsapp.com/send`:
| Anuncio | ID anuncio | Creativo | Hash imagen | Conjunto | Estado al publicar |
|---|---|---|---|---|---|
| K5 Menos cloro en tu vaso | 120254902712910401 | 1126028056560921 | ad2ab44eb1173ca19d51444fa9d24b17 | K Lima | IN_PROCESS |
| K6 Con repuesto incluido | 120254902713080401 | 1571068824791218 | b84ed4fd4de6ad34f1d3584186245cc6 | K Lima | IN_PROCESS |
| K7 Seis etapas | 120254902713210401 | 1671826737909235 | b22cfe9ab287689cbada7775d3ad2521 | K Lima | IN_PROCESS |
| P3 Separa con S/50 · Shalom | 120254902713260401 | 1453470359995612 | 9680e47d02586da43a44e83728618f06 | P Provincia | IN_PROCESS |
Angel confirmó que cada imagen corresponde a su texto. Verificar que pasen de IN_PROCESS a ACTIVE.
Observación: en el conjunto P ya existía el anuncio `PV · Separa con S/50 por Yape [PV]` (120254902675840401, ACTIVE), con el mismo mensaje que P3. Revisar si es duplicado y pausar el que rinda menos tras unos días.
Estado de conjuntos verificado: K+ 40, K 60, P 20, N-Miedo 15, N-Carruseles 10, RTG-Web 6 (US$ por día), todos ACTIVE.
