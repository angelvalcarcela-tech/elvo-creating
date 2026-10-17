# Plan S/30,000 de ganancia antes del 5-nov (borrador, 17-oct)

Faltan 19 días. Fuentes: §3 del contexto (Shopify por mes, ventas por 100 chats) y Meta Ads cuenta 893663859368314, últimos 30 días.

## Lo medido (Meta, 30 días)
| Campaña | Gasto US$ | Resultado | Costo/resultado US$ |
|---|---|---|---|
| CTWA-Sofia-Cuotas | 709.99 | 2,109 chats | 0.34 |
| WEB-Nativo-Oct26-v2 | 273.02 | 12 compras pixel | 22.75 |
| TEST-CTWA-Nativo-Angulos | 246.31 | 513 chats | 0.48 |
| nuevos (web) | 214.32 | 9 compras pixel | 23.81 |
| RTG-WA-Nativo-Oferta | 145.29 | 307 chats | 0.47 |
| CTWA-Vivo-Lima-v2 | 118.51 | 205 chats | 0.58 |
| WEB-Vivo-Oct26-v2 | 99.69 | 4 compras pixel | 24.92 |
| TEST-WEB-Nativo-Angulos | 84.89 | 1 compra | 84.89 |

CPA implícito en WhatsApp = costo por chat x 100 / ventas por 100 chats (costo por chat de campañas comparables, ~US$0.5, es supuesto):
- Cuotas todo el Perú (0.3 ventas/100 chats): ~US$113 por venta. Es el 41% del gasto.
- "En azul" Lima (2.2): ~US$23.
- Kit incluido (7.1): ~US$7.
La mitad de las ventas de YaVendio no trae código, así que estos CPA son orientativos.

## Matemática de la meta
Ganancia = ventas x (precio - costo de producto/envío - CPA). No hay costo de producto en `products.json` ni en este repo: **se necesita de Angel**. Con ticket S/349 y CPA de S/25 a S/80 (tipo de cambio ~3.5, supuesto):

| Contribución antes de ads por venta | CPA S/80 | CPA S/25 |
|---|---|---|
| S/150 | 429 ventas | 240 ventas |
| S/200 | 250 | 171 |
| S/250 | 177 | 133 |

Ritmo actual en Shopify: 27 pedidos en 17 días (~30 en los próximos 19). YaVendio suma más, pero su estado es todo "pending" (1,090), así que no sirve para contar ventas cerradas. Con cualquier margen razonable la meta exige entre 4 y 10 veces el ritmo web actual; es alcanzable solo si el canal WhatsApp con kit incluido escala.

## Acciones propuestas (ordenadas por impacto)
1. Recortar CTWA-Sofia-Cuotas (la de peor CPA) y mover ese presupuesto al formato con kit incluido / Lima.
2. Activar K+ (A, B, C) con el presupuesto que Angel confirme.
3. Mantener WEB-Nativo-Oct26-v2 y "nuevos" (CPA ~US$23, comparable al mejor observado de US$12 a 25); pausar TEST-WEB-Nativo-Angulos (US$85 por compra).
4. Cerrar el funnel de WhatsApp: seguimiento a los 646 leads calientes sin venta (si el archivo existe).
5. Publicar el tema nuevo con garantía de 1 año, 929 y cuenta regresiva al 24-oct.

## Inconsistencias a resolver
- El contexto dice que ningún anuncio activo va a la web, pero Meta muestra gasto y compras pixel en campañas WEB-* y "nuevos" en los últimos 30 días. Verificar cuáles siguen activas.
- Textos K+ dicen "Pagas al recibir en Lima. Envío gratis a todo el Perú"; los pedidos reales a provincia se cobran con seña S/50 y saldo en Shalom (texto de P1/P2). Alinear el texto.
- `HANDOVER.md` dice ignorar la doctrina; `CLAUDE.md` dice que manda. Falta decisión.
