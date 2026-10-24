# elvo· Nativo — Plan de Google Ads (embudo completo)

Preparado el 24-oct-2026. Producto: elvo· Nativo (elvo.pe). Mercado: Perú, PEN, español.
Todo lo marcado **[CONFIRMAR]** depende de datos que solo tienes tú (presupuesto, margen, precios finales).

## 0. Antes de subir nada (semana 0)

| Tarea | Detalle |
|---|---|
| Medición | Instala la app **Google & YouTube** de Shopify: conecta Google Ads + GA4 + Merchant Center. Conversión principal: `purchase`. Secundarias (no optimizan): `add_to_cart`, `begin_checkout`, clic a WhatsApp. Activa **conversiones mejoradas**. |
| Ventas por WhatsApp | Tu web empuja mucho a WhatsApp. Añade una etiqueta distinta por origen en el mensaje (hoy usas `[WEB-HOME]`, `[WEB-CANO]`): usa `[GADS-BUSQUEDA]`, `[GADS-PMAX]`, `[GADS-DG]` para medir qué campaña trae chats y ventas. |
| Contraentrega | `purchase` se dispara al crear el pedido aunque no se cobre. Revisa tu tasa de cancelación; si es alta, importa solo los pedidos entregados como conversión offline. |
| Merchant Center | Verifica que Shopify sincronice el feed de Nativo y que Perú esté habilitado para anuncios de Shopping **[CONFIRMAR en Merchant Center]**. Ficha con precio, disponibilidad y foto sin texto. |
| Landing | Anuncios fríos → `elvo.pe/products/elvonativo`. Marca → home. Que el precio del anuncio **coincida con el de la ficha** (hoy la home dice desde S/ 349 y la ficha aplica descuentos por plan: revisa antes). |
| Políticas | "Retiene metales pesados" debe llevar asterisco y la fuente (ficha técnica del núcleo PureCore) visible en la ficha. No uses plomo/arsénico/mercurio, ni certificaciones ISO/WQA como si fueran del producto, ni lámpara UV. "Garantía de por vida" solo si las condiciones están en tu página de garantía. |
| Presupuesto y margen | **[CONFIRMAR]** presupuesto diario y margen por plan. ROAS de equilibrio = 1 ÷ margen (ej. margen 40 % → ROAS 2,5). Define tu CPA objetivo antes de escalar. |

## 1. Estructura de campañas

Ejemplo con **S/ 100 al día** (≈ US$ 27); reparte igual en % si tu presupuesto es otro.

| # | Campaña | Etapa | % | Objetivo / puja |
|---|---|---|---|---|
| 1 | **Search – Marca** | Fondo | 8 % | Ventas. Maximizar conversiones (exacta + frase). |
| 2 | **Search – Genérico** | Medio/Fondo | 35 % | Ventas. Empieza en Maximizar conversiones; pasa a CPA objetivo con ≥ 30 conv. |
| 3 | **Performance Max – Nativo** | Medio/Fondo | 30 % | Ventas con valor de conversión (ROAS objetivo tras 2-3 semanas). |
| 4 | **Demand Gen – Prospección** | Tope/Medio | 17 % | Conversiones (o clics si aún no hay datos). YouTube, Discover, Gmail. |
| 5 | **Demand Gen – Remarketing** | Fondo | 10 % | Conversiones. Audiencias propias. |

### 1. Search – Marca
- Palabras: [elvo], [elvo nativo], [elvo filtro], [elvo purificador], "elvo.pe", "elvo filtros".
- Una sola agrupación. Sitelinks: Nativo, Planes, Cómo se instala, Repuestos, WhatsApp.

### 2. Search – Genérico (conjuntos de anuncios / grupos)
| Grupo | Palabras clave (frase / exacta) | Anuncio ancla |
|---|---|---|
| A. Filtro para caño | filtro de agua para caño, filtro para grifo, purificador para caño, filtro de agua para grifo de cocina | "Purificador para tu caño" |
| B. Purificador de casa | purificador de agua para casa, purificador de agua perú, purificador de agua lima, mejor purificador de agua | "Desde S/ 349" |
| C. Antimetales | filtro antimetales, filtro para metales pesados en el agua, purificador antimetales | "Retiene metales pesados*" |
| D. Cloro y sabor | filtro para quitar el cloro del agua, agua sin sabor a cloro, cómo quitar el cloro del agua | "Sin sabor a cloro" |
| E. Sin instalación | filtro de agua sin gasfitero, filtro sin instalación, purificador sin electricidad | "Lo instalas tú en 5 minutos" |
| F. Alternativa a bidones | dejar de comprar bidones, alternativa a bidones de agua, ahorrar en agua embotellada | "Adiós a los bidones" |

**Negativas (lista compartida):** gratis, casero, cómo hacer, hacer un filtro, diy, pdf, manual, industrial, piscina, acuario, pecera, osmosis industrial (si no vendes Cero), segunda mano, olx, mercado libre, repuesto (solo en C. de repuestos), empleo, trabajo, curso.

**Anuncio responsivo (RSA)** — ya validado: titulares ≤ 30 y descripciones ≤ 90 caracteres.
- Titulares (usa 15): elvo· Nativo para tu caño · Purificador para tu caño · Agua rica, directo del caño · Sin sabor a cloro · Retiene metales pesados* · Lo instalas tú en 5 minutos · Sin gasfitero ni obras · Sin electricidad · 30 días de prueba · Envío gratis a todo el Perú · Pago contra entrega · Hasta 6 cuotas sin interés · Desde S/ 349 · Garantía de por vida* · Más de 500 familias lo usan · Adiós a los bidones · Compra en elvo.pe · Oficial elvo· Perú · 6 etapas de filtración · Te avisamos por WhatsApp.
- Descripciones:
  1. Filtra tu agua directo del caño. Sin gasfitero, sin obras. Pruébalo 30 días.
  2. elvo· Nativo: retiene metales pesados* y reduce cloro, olores y sabores.
  3. Envío gratis a todo el Perú. Paga al recibir o hasta en 6 cuotas sin interés.
  4. Un núcleo dura unos 18 meses y te avisamos por WhatsApp cuando toque cambiarlo.
- Complementos: llamadas (WhatsApp +51 929 190 100), 6 textos destacados (Envío gratis · 30 días de prueba · Pago contra entrega · 6 cuotas sin interés · Instalación en 5 min · Sin electricidad), sitelinks, fragmento "Tipos: 18 meses, 3 años, 6 años", precio por plan.
- Ancla según grupo: fija un titular relevante en la posición 1.

### 3. Performance Max – Nativo
- Fuente: feed de Shopify (Merchant Center) + grupo de recursos manual.
- **Grupo de recursos 1 "Hogar"** (venta directa): imágenes de uso (mañana, familia, instalas, prueba) + plan más elegido.
- **Grupo de recursos 2 "Ahorro"**: bidones, duración, incluye.
- Señales de audiencia: clientes (lista de Shopify), visitantes web 30 d, segmentos personalizados con las búsquedas de la campaña 2.
- Video: PMax lo genera solo si no subes uno (suele salir flojo). Recomendado: un video de 15 s armado con 4 de estas imágenes **[puedo prepararlo]**.
- Excluye la marca (o crea la campaña separada) para que no canibalice Search – Marca.

### 4. Demand Gen – Prospección (tope y medio del embudo)
| Grupo de anuncios | Audiencia | Creativos |
|---|---|---|
| P1 Intención de compra | En el mercado: electrodomésticos de cocina, mejoras del hogar, filtros/purificadores de agua | manana, familia, bidones |
| P2 Segmento propio | Personas que buscaron las palabras de la campaña 2 | instalas, incluye, resena |
| P3 Lookalike | Lista de clientes de Shopify (mín. 100 coincidencias) | familia, manana, masvendido |
| Geografía | Lima Metropolitana primero (entrega el mismo día); luego provincias (entrega en 2 días con seña de S/ 50) | — |

### 5. Demand Gen – Remarketing (fondo)
| Grupo | Audiencia | Ventana | Creativos |
|---|---|---|---|
| R1 | Visitó la ficha de Nativo, no compró | 30 d | prueba, masvendido |
| R2 | Agregó al carrito / inició checkout | 14 d | maselegido, prueba, canales |
| R3 | Vio ≥ 50 % del video / interactuó en YouTube | 30 d | duracion, incluye |
| Excluir | Compradores de los últimos 180 d (luego cross-sell de Vivo / repuestos) | — | — |

## 2. Qué anuncio va a qué etapa

Todas las piezas están en `brands/elvo/static-ads/`. Formatos: 4:5 (1080×1350) en todas; 1:1, 16:9 (≈ 1,91:1 al recortar) y 9:16 en las piezas con foto; 1:1 y 9:16 en las de oferta.

| Etapa | Pieza | Carpeta | Mensaje |
|---|---|---|---|
| **Tope (despertar deseo)** | manana | elvo-nativo-contexto | Abres el caño. Sale agua rica. |
| | familia | elvo-nativo-contexto | Para toda la familia. |
| | bidones | elvo-nativo-contexto | Deja de cargar bidones. |
| **Medio (considerar)** | instalas (v2) | elvo-nativo-contexto | Lo instalas tú. En 5 minutos. |
| | caja / incluye | elvo-nativo-contexto · elvo-oferta | Todo viene incluido. |
| | resena | elvo-nativo-contexto | Reseña real de Carmen S., Trujillo. |
| | duracion | elvo-oferta | Un núcleo. Unos 18 meses. |
| | canales | elvo-oferta | Estamos en todos los canales. |
| **Fondo (decidir y comprar)** | masvendido | elvo-oferta | El favorito de los hogares · desde S/ 349. |
| | maselegido | elvo-oferta | El plan de 3 años es el más elegido. |
| | prueba | elvo-nativo-contexto | Pruébalo 30 días en tu casa. |

Las rondas anteriores (`elvo-nativo-feed` y `elvo-nativo-feed-2`) usan la identidad vieja: **no las subas**.

## 3. Especificaciones de imagen para Google

| Uso | Relación | Tamaño recomendado | Nota |
|---|---|---|---|
| Horizontal (PMax, Demand Gen, Display) | 1,91:1 | 1200×628 | Recorta la versión 16:9 a 1200×628. |
| Cuadrado | 1:1 | 1200×1200 (mín. 300) | |
| Vertical (Demand Gen, PMax) | 4:5 | 960×1200 | Las 4:5 ya generadas sirven (escalarlas a 960×1200). |
| Vertical stories/Shorts | 9:16 | 1080×1920 | |
| Logo | 1:1 y 4:1 | 1200×1200 y 1200×300 | Usar `product-images/elvo-logo-trim.png` sobre fondo. |
Evita texto pequeño; Google puede rechazar imágenes casi sin producto o con demasiado texto **[verifica el estado de aprobación tras subirlas]**.

## 4. Calendario

| Cuándo | Qué hacer |
|---|---|
| Semana 0 | Medición, feed, políticas, landing, UTMs (`utm_source=google&utm_medium=cpc&utm_campaign={campaña}&utm_content={pieza}`). |
| Día 1 | Lanzar 1 (marca), 2 (genérico) y 3 (PMax). |
| Día 3-5 | Lanzar 4 (prospección) y 5 (remarketing, cuando haya ≥ 1.000 visitantes en la audiencia; antes se queda sin impresiones). |
| Días 1-14 | Fase de aprendizaje: no toques puja ni presupuesto salvo errores. Solo agrega negativas con el informe de términos de búsqueda. |
| Día 15 | Primera lectura: CPA, ROAS, % de impresiones, términos de búsqueda, calidad del tráfico de PMax. |
| Día 15-30 | Pausa grupos con ≥ 2× tu CPA objetivo sin conversión; sube +20 % cada 3-4 días lo que esté bajo CPA. Cambia los 2 creativos con menor CTR por variaciones nuevas. |
| Mes 2 | Búsqueda → CPA/ROAS objetivo. PMax → ROAS objetivo. Prueba video propio. Duplica lo ganador a provincias y a Vivo. |

## 5. KPIs por etapa

| Etapa | Métrica principal | Referencia a vigilar |
|---|---|---|
| Tope | Tasa de clics (CTR), visitas de calidad, costo por visita | CTR > 0,5 % en Demand Gen; tiempo en ficha |
| Medio | % de visitas que llegan a `add_to_cart`, clics a WhatsApp | Costo por clic a WhatsApp |
| Fondo | CPA y ROAS de `purchase` | ROAS ≥ tu ROAS de equilibrio × 1,3 |
| Cuenta | Cuota de impresiones en marca, términos nuevos, tasa de cancelación contraentrega | Marca > 90 % de cuota |

## 6. Cómo subirlo en Google Ads (paso a paso)

1. **Search:** Campañas → Nueva campaña → Ventas → Búsqueda. Pega palabras clave por grupo, crea el RSA con los titulares/descripciones de arriba, agrega los complementos.
2. **PMax:** Nueva campaña → Ventas → Performance Max. Conecta Merchant Center, crea los 2 grupos de recursos, sube imágenes por relación, logos, titulares y descripciones, señales de audiencia.
3. **Demand Gen:** Nueva campaña → Ventas → Demand Gen. Crea un grupo por audiencia, sube imágenes (carrusel o imagen única), titulares ≤ 40 y descripciones ≤ 90 **[verifica límites al crearla]**.
4. **Remarketing:** primero crea audiencias en Administrador de audiencias (visitantes de `/products/elvonativo`, carrito, YouTube) y luego la campaña 5 con esas audiencias + exclusión de compradores.
5. Revisa estado de aprobación a las 24 h.

## 7. Qué puedo preparar después
- Versiones 1,91:1 recortadas a 1200×628 y 4:5 a 960×1200.
- Video de 15 s para PMax y YouTube a partir de las imágenes.
- Variantes de copy y de imagen para pruebas A/B.
- Misma estructura para Meta Ads (tengo acceso a la cuenta publicitaria) o para Vivo.
