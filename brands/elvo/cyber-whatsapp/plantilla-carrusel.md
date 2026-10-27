# Cyber elvo· — plantilla de WhatsApp con carrusel (27-oct al 1-nov-2026)

Estado: borrador. Falta confirmar dónde se crea y se envía (YaVendio o administrador de WhatsApp de Meta) y los precios en Shopify.

## Datos de la plantilla
- Categoría: Marketing. Idioma: español.
- Nombre sugerido: `cyber_elvo_carrusel_oct26`
- Lista: compradores del bidón (620) que hayan aceptado recibir mensajes. No enviar a quien no dio su consentimiento.
- Imágenes: 5 tarjetas 1:1 (1024×1024) en `tarjetas/`, todas del mismo tamaño y formato.

## Texto principal (cuerpo, máx. 1024 caracteres)
```
Hola {{1}}, empezó el Cyber elvo·.

Del 27 de octubre al 1 de noviembre tienes precios especiales y regalos en nuestros purificadores. Pagas al recibir y tienes 30 días de prueba.

Desliza para ver las ofertas. Si no sabes cuál elegir, responde este mensaje y te ayudamos.
```
Variable {{1}}: nombre del cliente. Sin emojis ni signos de exclamación, como pide el manual de marca.

## Tarjetas (orden del carrusel)
| # | Imagen | Texto de la tarjeta (máx. 160 caracteres) | Botón 1 (URL) | Botón 2 (respuesta rápida) |
|---|---|---|---|---|
| 1 | `1-kit.png` | Kit de filtros de repuesto: S/ 99 (regular S/ 120). Envío gratis. | Ver detalles → https://elvo.pe/products/kit-de-filtros-purificador-de-agua?utm_source=whatsapp&utm_medium=cyber&utm_campaign=cyber-elvo-oct26 | Lo quiero |
| 2 | `2-nativo.png` | Purificador Nativo Antimetales: S/ 349 (regular S/ 598). De regalo, un filtro de repuesto. | Ver detalles → https://elvo.pe/products/elvonativo?utm_source=whatsapp&utm_medium=cyber&utm_campaign=cyber-elvo-oct26 | Lo quiero |
| 3 | `3-vivo.png` | Purificador Vivo con Magnesio: S/ 259. De regalo, un medidor de agua. | Ver detalles → https://elvo.pe/products/elvovivo?utm_source=whatsapp&utm_medium=cyber&utm_campaign=cyber-elvo-oct26 | Lo quiero |
| 4 | `4-alivio16.png` | Bidón Alivio 16 Litros: S/ 159 (regular S/ 201). De regalo, un medidor de agua. | Ver detalles → https://elvo.pe/products/elvo-bidon-16l?utm_source=whatsapp&utm_medium=cyber&utm_campaign=cyber-elvo-oct26 | Lo quiero |
| 5 | `5-alivio22.png` | Bidón Alivio 22 Litros: S/ 198 (regular S/ 213). De regalo, un medidor de agua. | Ver detalles → https://elvo.pe/products/elvo-bidon-22l?utm_source=whatsapp&utm_medium=cyber&utm_campaign=cyber-elvo-oct26 | Lo quiero |

Por qué este orden: la lista ya tiene un bidón Alivio, así que lo más relevante es el repuesto (1), luego el mayor ahorro visible (2 Nativo), la otra opción al caño (3 Vivo) y al final los bidones (4 y 5), pensados para regalar o llevar a otra casa.

## Botón "Lo quiero" y chat
Cada botón de respuesta rápida debe disparar en el chat un mensaje que diga por qué producto preguntan (ej. "Quiero el Purificador Nativo Antimetales (S/ 349)"), igual que los anuncios de WhatsApp. Ahí entra el upsell del kit de repuesto, que se hace por chat.

## Antes de enviar (tienda y operación)
1. Nativo a S/ 349 en Shopify (precio o código de descuento hasta el 1-nov). Hoy el plan 3 años está en S/ 389.
2. Vivo a S/ 259. Hoy el plan 18 meses está en S/ 249.
3. Regalos: medidor de agua (3 productos) y filtro de repuesto (Nativo). Definir qué es el medidor y confirmar stock.
4. Envío gratis del kit durante el cyber: que el checkout cobre S/ 0.
5. Precios regulares citados: Nativo S/ 598 (349 equipo + 249 repuesto); Alivio 16 S/ 201, Alivio 22 S/ 213 y kit S/ 120 son los precios tachados de Shopify.
6. Consentimiento de la lista y envío de prueba a tu propio número antes del envío masivo.

## Medición
- UTM `cyber-elvo-oct26` en los enlaces.
- Pedidos en YaVendio y Shopify con esa campaña.
- Si se conecta el conjunto de datos de mensajes, las ventas por WhatsApp llegarán a Meta.
