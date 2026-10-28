# WhatsApp: relanzamiento por producto (plan, 28-oct-2026)

Estado: **plan, nada cargado en Meta todavía.** Se carga como borrador y solo se publica con "publica".

## 0. Reglas acordadas
1. **Una campaña por producto.** Nunca se mezclan productos en una campaña. Dentro de cada campaña se agregan ángulos nuevos como anuncios.
2. **Todo anuncio a WhatsApp lleva el precio a la vista**, en el creativo o en el copy.
3. Se borra la campaña actual "ELVO | WhatsApp | Conversaciones | Feed FB" (incluye los 16 borradores "v2" que armé hoy; quedan reemplazados por este plan).

## 1. Antes de cargar: el número
Los 16 anuncios actuales llevan más de un día con 0 impresiones. La causa no está confirmada. Un anuncio viejo mostraba "WhatsApp Account Is Banned" para el 929190100. **Si el número tiene un problema, las campañas nuevas tampoco entregarán.** Revisar en WhatsApp Manager antes de publicar:
- que 51 929190100 esté registrado como cuenta de WhatsApp Business y no baneado,
- que esté vinculado a la página AQA Filtros Perú (la página Elvo Peru no lo acepta).

## 2. Estructura de campañas

| Campaña | Presupuesto/día (propuesto) | Conjunto | Anuncios iniciales |
|---|---|---|---|
| ELVO \| WA \| Nativo | US$25 | Amplio Perú (Advantage+) | 5 (ver sección 4) |
| ELVO \| WA \| Alivio 16 L | US$15 | Amplio Perú (Advantage+) | 6 |
| ELVO \| WA \| Alivio 22 L | US$15 | Amplio Perú (Advantage+) | 4 |

Total US$55, igual que hoy. Es una propuesta: confirma o cambia los montos.

Ajustes de cada campaña (iguales en las tres):
- Objetivo: Interacción, destino WhatsApp, optimiza conversaciones.
- Presupuesto a nivel de conjunto (ABO), sin topes de gasto por conjunto, para que no pase lo del aviso "una parte no se gastará".
- Página: AQA Filtros Perú. Número: 51 929190100.
- Público: Perú, 25–65, Advantage+. Excluye "Elvo | Compradores web 180d".
- Ubicaciones: Feed de Facebook, Facebook Stories, Facebook Reels y Feed de Instagram, solo móvil. (Es la configuración de los conjuntos que sí entregaron antes.)
- Fecha de fin: ninguna (se agregan ángulos y se pausan los que no funcionen).
- Para sumar un ángulo nuevo: crear un anuncio nuevo en el conjunto existente. No crear campaña nueva.

**Pregunta abierta:** el carrusel "Cyber WhatsApp v2" (campaña aparte, US$20) mezcla 4 productos y rompe la regla. Termina el 1-nov. ¿Lo dejamos hasta esa fecha o lo pausamos?

## 3. Auditoría de las 16 imágenes actuales

Precio a la vista en la imagen: **sí** en 12, **no** en 4.

| # | Imagen | Producto | Precio en la imagen |
|---|---|---|---|
| 1 | Reseña real (Yoannis) | Alivio 16 | **NO** |
| 2 | El Niño 2017 | Alivio 16 | Sí, S/ 159 |
| 3 | 7 millones | Alivio 22 | Sí, S/ 198 |
| 4 | Reseñas reales (3 clientes) | Nativo | **NO** |
| 5 | Ficha | Alivio 16 | Sí, S/ 159 |
| 6 | Ficha 3 años | Nativo | Sí, pero dice **S/ 389** y hoy es S/ 349 (desactualizado) |
| 7 | Río con 53 puntos críticos | Alivio 16 | Sí, S/ 159 |
| 8 | Ficha 6 años | Nativo | Sí, S/ 489 |
| 9 | Ficha 18 meses | Nativo | Sí, S/ 349 |
| 10 | "Se corta el agua" (miedo) | Alivio 16 | **NO** |
| 11 | "Lo que más nos preguntan" | Nativo | **NO** |
| 12 | Toda la casa | Alivio 22 | Sí, S/ 198 |
| 13 | Ficha | Alivio 22 | Sí, S/ 198 |
| 14 | El Niño 2017 | Alivio 22 | Sí, S/ 198 |
| 15 | Turbidez | Nativo | Sí, "desde S/ 349" |
| 16 | 7 millones | Alivio 16 | Sí, S/ 159 |

**Actualización (28-oct, tarde):** ya se editaron imágenes en `static-ads/elvo-whatsapp-promo/`:
- #10 (miedo) y #11 (dudas) ahora llevan la píldora de precio debajo del producto: "Ten un bidón Alivio desde S/ 159" y "elvo· Nativo desde S/ 349".
- Las 5 imágenes "ficha" (#5, #6, #8, #9, #13) ahora dicen **"Promo: S/ …"** en lugar de "Precio: S/ …". Sin precio tachado (se probó y se descartó).
- #6 (Nativo 3 años) ahora dice **S/ 349**, ya no S/ 389. Vale solo hasta el 1-nov.
- Siguen sin precio en la imagen: #1 (reseña Alivio 16) y #4 (reseñas Nativo). Para esas, el precio va en la **primera línea del copy** (sección 4).

Imagen 6 (Nativo 3 años): ya se regeneró con "Promo: S/ 349". El precio es válido solo hasta el 1-nov; después vuelve a S/ 389 y hay que pausar el anuncio. Ojo: durante el Cyber el plan de 3 años cuesta lo mismo que el de 18 meses, lo que resta sentido a vender el de 18 meses.

## 4. Anuncios: copy y mensaje precargado

Reglas de copy:
- Titular = producto + precio.
- "Retiene plomo y metales pesados" solo con la nota "según la ficha técnica del núcleo PureCore".
- Sin "envío gratis", sin lámpara UV, sin certificaciones, sin cifras de alcalinidad, sin arsénico ni mercurio.
- Cierre fijo: "Escríbenos por WhatsApp. Pago contraentrega."
- Botón: Enviar mensaje por WhatsApp.
- Enlace de destino: `https://fb.me/` (ya probado en el carrusel).

**Mensaje de bienvenida (igual en todos):** "Hola, te ayudamos con tu pedido."
**Mensaje precargado (lo que llega al chat):** identifica producto y plan, para que el vendedor sepa de qué anuncio viene.

### Campaña Nativo

| Anuncio / ángulo | Imagen | Titular | Copy principal | Mensaje precargado |
|---|---|---|---|---|
| Nativo 18 meses \| ficha | #9 | Nativo 18 meses · S/ 349 | El purificador que va directo a tu caño: sin electricidad, sin gasfitero, lo instalas tú en 5 minutos. Escríbenos por WhatsApp y te ayudamos a elegir tu plan. Pago contraentrega.<br><br>*Retiene plomo y metales pesados, según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada. | Hola, quiero el Nativo 18 meses (S/ 349) |
| Nativo 6 años \| ficha | #8 | Nativo 6 años · S/ 489 | Nativo 6 años: el purificador que va directo a tu caño, con 3 núcleos PureCore de repuesto incluidos. Sin electricidad, sin gasfitero, lo instalas tú en 5 minutos. Escríbenos por WhatsApp y te ayudamos a elegir tu plan. Pago contraentrega.<br><br>*Retiene plomo y metales pesados, según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada. | Hola, quiero el Nativo 6 años (S/ 489) |
| Nativo \| reseñas reales | #4 (sin precio) | Nativo · desde S/ 349 | **Nativo desde S/ 349.** Esto dicen quienes ya lo instalaron en su casa. Escríbenos por WhatsApp y te ayudamos a elegir tu plan. Pago contraentrega. | Hola, quiero información del Nativo (desde S/ 349) |
| Nativo \| lo que más preguntan | #11 (sin precio) | Nativo · desde S/ 349 | **Nativo desde S/ 349.** Lo que más nos preguntan, respondido. Si te queda otra duda, escríbenos por WhatsApp. Pago contraentrega. | Hola, tengo una duda sobre el Nativo (desde S/ 349) |
| Nativo \| turbidez (El Niño) | #15 | Purificador Nativo · desde S/ 349 | Con las lluvias, la calidad del agua puede cambiar (Gestión, 19-oct-2026). elvo· Nativo reduce la turbidez, el cloro, los olores y los sabores del agua de tu caño. Sin electricidad y sin gasfitero. Escríbenos por WhatsApp. Pago contraentrega.<br><br>Los resultados dependen de la calidad del agua de entrada. | Hola, quiero el Nativo (desde S/ 349) |
| Nativo 3 años \| ficha | #6 (S/ 389, desactualizada) | Nativo 3 años · S/ 349 | Pendiente: ver sección 3, imagen 6. | Hola, quiero el Nativo 3 años (S/ 349) |

El anuncio de 3 años queda fuera del lanzamiento hasta decidir. Entran 5.

### Campaña Alivio 16 L

| Anuncio / ángulo | Imagen | Titular | Copy principal | Mensaje precargado |
|---|---|---|---|---|
| Alivio 16 \| ficha | #5 | Alivio 16 · S/ 159 | Agua de reserva en casa, sin depender del caño. Se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp y te lo enviamos. Pago contraentrega. | Hola, quiero el Bidón Alivio 16 Litros (S/ 159) |
| Alivio 16 \| reseña real | #1 (sin precio) | Alivio 16 · S/ 159 | **Bidón Alivio 16 Litros, S/ 159.** Así lo cuenta quien ya lo usa. Se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp. Pago contraentrega. | Hola, quiero el Bidón Alivio 16 Litros (S/ 159) |
| Alivio 16 \| miedo | #10 (sin precio) | Alivio 16 · S/ 159 | **Bidón Alivio 16 Litros, S/ 159.** Con los cortes programados y las lluvias, tener agua lista en casa da tranquilidad. Se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp. Pago contraentrega. | Hola, quiero el Bidón Alivio 16 Litros (S/ 159) |
| Alivio 16 \| El Niño 2017 | #2 | Bidón Alivio 16 Litros · S/ 159 | En 2017, la planta que potabiliza el agua de Lima cerró sus compuertas hasta 6 días (Gestión, 19-oct-2026). Con El Niño Costero en alerta, que no te pase: Bidón Alivio 16 Litros se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp. Pago contraentrega. | Hola, quiero el Bidón Alivio 16 Litros (S/ 159) |
| Alivio 16 \| río de Lima | #7 | Bidón Alivio 16 Litros · S/ 159 | El río que abastece a Lima tiene 53 puntos críticos de huaicos, según Gestión (19-oct-2026). Que no te pase: Bidón Alivio 16 Litros se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp. Pago contraentrega. | Hola, quiero el Bidón Alivio 16 Litros (S/ 159) |
| Alivio 16 \| 7 millones | #16 | Bidón Alivio 16 Litros · S/ 159 | Casi 7 millones de peruanos podrían ver afectado su acceso al agua potable, según una estimación de Gestión (19-oct-2026). Que no te pase: Bidón Alivio 16 Litros se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp. Pago contraentrega. | Hola, quiero el Bidón Alivio 16 Litros (S/ 159) |

Son 6 anuncios. Los 3 de "El Niño" comparten tema y puede convenir lanzar solo 2.

### Campaña Alivio 22 L

| Anuncio / ángulo | Imagen | Titular | Copy principal | Mensaje precargado |
|---|---|---|---|---|
| Alivio 22 \| ficha | #13 | Alivio 22 · S/ 198 | Agua de reserva en casa, sin depender del caño. Se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp y te lo enviamos. Pago contraentrega. | Hola, quiero el Bidón Alivio 22 Litros (S/ 198) |
| Alivio 22 \| El Niño 7 millones | #3 | Bidón Alivio 22 Litros · S/ 198 | El agua de casi 7 millones de peruanos podría verse afectada, según una estimación de Gestión (19-oct-2026). Que no te pase: Bidón Alivio 22 Litros se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp. Pago contraentrega. | Hola, quiero el Bidón Alivio 22 Litros (S/ 198) |
| Alivio 22 \| toda la casa | #12 | Bidón Alivio 22 Litros · S/ 198 | Con El Niño en alerta, ten agua de reserva para toda la casa. Que no te pase: Bidón Alivio 22 Litros se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp. Pago contraentrega. | Hola, quiero el Bidón Alivio 22 Litros (S/ 198) |
| Alivio 22 \| El Niño 2017 | #14 | Bidón Alivio 22 Litros · S/ 198 | En 2017, la planta de agua de Lima cerró hasta 6 días (Gestión, 19-oct-2026). Con El Niño en alerta, que no te pase: Bidón Alivio 22 Litros se llena con una jarra, sin electricidad ni instalación. Escríbenos por WhatsApp. Pago contraentrega. | Hola, quiero el Bidón Alivio 22 Litros (S/ 198) |

Son 4 anuncios, todos con precio en la imagen.

## 5. Precios y vigencia
- Los precios están **escritos dentro de las imágenes** (S/ 159, 198, 349, 489). Si cambia un precio en la tienda hay que regenerar la imagen.
- Nativo 3 años: S/ 349 hasta el 1-nov, S/ 389 después.
- Alivio 16 (S/ 159) y Alivio 22 (S/ 198) coinciden con los precios de la tienda.

## 6. Cómo se carga (pasos)
1. Confirmas el número (sección 1), los presupuestos (sección 2) y las dos decisiones abiertas (carrusel y Nativo 3 años).
2. Tú borras la campaña actual.
3. Yo creo las 3 campañas como borrador, con sus anuncios, y te paso los enlaces de vista previa.
4. Revisas y dices "publica".
5. Reviso a las 2 horas si entregan. Si siguen en 0, el problema es el número, no los anuncios.

## 7. Decisiones pendientes
- Presupuesto por producto (propuesto 25 / 15 / 15).
- Carrusel Cyber: ¿pausar o dejar hasta el 1-nov?
- Nativo 3 años: ¿regenerar la imagen a S/ 349 o dejarlo fuera?
- ¿Regenerar las 4 imágenes sin precio, o basta con el precio en el copy?
- ¿Ubicaciones: también Instagram Feed y Reels? Lo propuesto incluye Instagram Feed y quita Instagram Reels.
