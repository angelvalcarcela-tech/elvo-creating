# Pruebas de agua, minerales y consumibles plug and play para elvo· (Perú, oct 2026)

Nota de método: la búsqueda web devolvió snapshots de Mercado Libre Perú (sin fecha ni conteo de ventas), Sodimac Perú y poco de Alibaba/Made-in-China. No pude abrir listados de ML, Falabella ni Amazon directamente (fetch falló: DNS). Falabella, Amazon, Temu y 1688 quedan SIN verificar. Las cifras FOB, de aterrizaje y de margen son estimaciones mías (etiquetadas "EST") y deben cotizarse con proveedores antes de decidir. Fecha de consulta: 2026-10-26.

## 1. ¿Qué ítems superan un precio viable (S/59+ standalone) y cuáles son solo regalos baratos?

### Takeaway
Con la estructura de costos dada (courier S/12.5 + empaque S/3.5 + 3% pago + 20% fallidas + S/65-120 de anuncio por pedido), ningún ítem individual de esta categoría es rentable standalone a S/59; el precio de equilibrio de un ítem barato sale en ~S/115-190 (EST, cálculo abajo). Los candidatos viables son el medidor TDS como cross-sell/kit (S/40-65 en ML), los strips y consumibles como regalo o add-on, y los consumibles solo si se venden recurrentemente a la base instalada.

### Cited Findings
- Medidores TDS en ML Perú, snapshot indexado (sin fecha exacta): TDS simple ~S/19 ("Tds Conductimetro Medidor Ppm Calidad Agua", 12 cuotas de S/1.58); 3 en 1 (TDS/EC/temperatura) S/41.40-S/64.99; 4 en 1 S/142; 7 en 1 Bluetooth S/207-S/329.90; 10 en 1 S/190 — [ML Perú: Medidor TDS](https://listado.mercadolibre.com.pe/medidor-tds), [Tester de agua](https://listado.mercadolibre.com.pe/tester-de-agua), [Conductímetro digital](https://listado.mercadolibre.com.pe/conductimetro-digital-para-agua). Reportado vía resumen de búsqueda; conteo de ventas no verificado.
- Tiras 16 en 1 (cloro, dureza, pH, alcalinidad, nitrato, nitrito, metales como plomo/mercurio) existen como kits de 50-100 tiras en marketplaces europeos; no encontré listados peruanos con precio — [ManoMano ES 16 en 1](https://www.manomano.es/p/kit-de-prueba-de-agua-potable-ulisem-16-en-1-kits-profesionales-de-prueba-de-dureza-tiras-de-prueba-para-agua-del-grifo-y-de-pozo-88472739), [ibspot 16 en 1 x50](https://ibspot.com/products/tiras-de-prueba-para-acuario-16-en-1-kit-de-50-tiras-reactivas-1231).
- Fiabilidad de tiras para plomo: estudio de Kriss, Pieper, Parks y Edwards (Environ. Sci. Technol., 2021): 12 de 16 marcas de kits de plomo no aptos para agua potable (límites de detección 5-20 mg/L); las tiras binarias detectan plomo disuelto pero no particulado; no hay entidad certificadora — resumido en [Water STP: challenge of detecting lead](https://waterstp.ca/challenge-of-detecting-lead/).
- Tiras de dureza: rangos gruesos (un pad puede saltar de 120 a 250 ppm), lectura subjetiva por color, se degradan con humedad y edad — [Softpro (fuente comercial, peso bajo)](https://www.softprowatersystems.com/pages/hardness-test-strips-water-quality-testing-softeners-real-truth); no encontré estudio revisado por pares sobre cloro/dureza.
- Bidón de 20 L con caño en Sodimac Perú: Klimber 20 L a S/29.90; caños genéricos de agua S/22.90-59.50 (no necesariamente de bidón) — [Sodimac Perú bidones/muebles](https://www.sodimac.com.pe/sodimac-pe/b/mueble-para-bidon-de-agua), [Sodimac Perú caños](https://www.sodimac.com.pe/sodimac-pe/b/canos-de-agua). Snapshot sin fecha.
- Tabletas limpiadoras de botella: no hallé listados peruanos específicos. Referencias regionales: Tabi Clean Colombia, 2 tabletas = 1 L, COP 9,891 en Farmatodo; CamelBak 8 tabletas en Europa — [Farmatodo CO](https://www.farmatodo.com.co/producto/500030476-multisuperficies-repuesto-x2-tabletas--tabi-clean-colombia-2-tabletas-efervescentes-x-1), [CamelBak 8-pack](https://varuste.net/es/p32569/camelbak-cleaning-tablets-8-pack). No son precios de Perú.
- Descalcificadores de ácido cítrico/láctico: formato sobres de 6 dosis (HG), líquido Melitta 250 ml a €2.42 en España. Sin precio peruano verificado — [HG](https://hg.eu/es/productos/hg-descalcificador-con-acido-citrico-cafeteras), [PcComponentes](https://www.pccomponentes.com/melitta-anti-calc-bio-descalcificador-liquido-para-cafeteras-250ml).
- FOB verificados (poco útiles): Made-in-China, medidor "económico" Hangzhou Supmea US$155-170, MOQ 1, pero es industrial, no pen — [Made-in-China](https://m.made-in-china.com/catlist/Other-Analysis-Instruments-3507040000.html). Alibaba Oway OW-9908 (pH/EC/TDS 4 en 1) y Wanbang TDS-3: capacidad 5,000/semana, sin precio visible — [Oway](https://www.alibaba.com/product-detail/_60679404628.html), [Wanbang](https://www.alibaba.com/product-detail/_1600437039215.html). Botella alcalina con cartucho: US$22 FOB, MOQ 140 (Beautetrade, otro B2B) — [Beautetrade](https://www.beautetrade.com/products/mymi-blueblue-600ml/88424/). Gotas de minerales OEM: MOQ desde 50 unidades hasta 50,000 — [Accio](https://www.accio.ai/find-product/potassium-magnesium-liquid-drops).
- Físico relevante a TDS (dato de la consigna, no verificado aquí): purificador de carbón apenas cambia TDS; Vivo (con magnesio) lo sube; RO Cero lo baja mucho. Consecuencia: un medidor TDS solo "demuestra" valor con Cero y puede confundir con Vivo (TDS sube por diseño).

### Inferences
Cálculo de equilibrio (EST, mi modelo): por pedido enviado, ingreso neto = 0.8 × P × 0.97 (20% fallidas, 3% pago); costo = anuncio + S/16 (courier + empaque, se pierde también en fallidas) + 0.8 × costo aterrizado L. Equilibrio P = (anuncio + 16 + 0.8L) / 0.776. Con L = S/10: anuncio S/65 → P ≈ S/115; anuncio S/120 → P ≈ S/186. Es decir, un ítem de S/59 pierde dinero standalone aunque el costo sea S/0. Solo un kit/bundle de S/115+ o un ítem con anuncio barato (tráfico propio, base instalada) funciona.

Tabla resumen (FOB y L son EST; L = FOB × 3.5 × ~1.35 por impuestos/logística, supuesto sin verificar; margen = sobre precio retail sugerido):

| Ítem | Retail Perú (verificado/EST) | FOB EST | Aterrizado EST | Veredicto |
|---|---|---|---|---|
| Medidor TDS 3 en 1 | S/41-65 ML (verif.) | US$1.5-3 | S/7-14 | Cross-sell (S/49-59) o regalo; margen ~75-85% pero bruto S/40-50 no cubre ad |
| Medidor TDS básico (solo TDS) | ~S/19 ML (verif.) | US$0.7-1.2 | S/3-6 | Regalo <S/10 landed; sirve de prueba de valor para Cero |
| Tiras 16 en 1 (50-100 u) | no encontrado en Perú | US$1.5-4 | S/7-19 | Cross-sell/regalo; claim limitado (screening, no plomo) |
| Gotas/concentrado de magnesio | sin precio PE | US$0.8-1.5 por 30 ml | S/4-7 | Recurrente atractivo, pero riesgo regulatorio alto: no lanzar hasta validar con DIGESA |
| Cartucho/stick mineralizador | sin precio PE | US$0.5-1.5 | S/3-7 | Cross-sell/recurrente si material food grade verificado; riesgo medio |
| Alkaline stick | ₹250 India (ref.) | US$0.5-1.5 | S/3-7 | Descartar: sin evidencia, claims riesgosos |
| Tabletas limpieza bidón | sin precio PE | US$0.03-0.06/tab | S/0.2-0.3/tab | Recurrente barato; pack de 12 como regalo o add-on |
| Cepillo de bidón | sin precio PE | US$0.3-0.8 | S/1.5-4 | Regalo |
| Descalcificador café/hervidor | sin precio PE | US$0.1-0.3/sobre | S/0.5-1.5 | Fuera del core; descartar o regalo |
| Stickers recordatorio cambio de filtro | n/d | US$0.02-0.05 | <S/0.5 | Regalo (valor percibido, incluido en caja) |
| Caño de repuesto para bidón | S/22.90-59.50 caños genéricos Sodimac; bidón completo S/29.90 | US$0.2-0.6 | S/1-3 | Add-on/regalo de postventa |
| Cubeteras/infusores | n/d | US$0.4-1.5 | S/2-7 | Regalo; sin retención |

Recurrencia (inferencia): los únicos con recompra natural son (1) gotas/sticks de mineral (si legales), (2) tabletas de limpieza de bidón (cada 1-2 meses, ticket bajo S/15-25 por pack), (3) tiras de prueba (rellenos de 50-100). Ninguno iguala a los cartuchos en ticket, pero pueden subir el valor del cliente si se venden por suscripción/WhatsApp.

### Gaps
- Precios y ventas acumuladas verificados de ML Perú (sin conteo de ventas), Falabella, Amazon y Temu para tiras, gotas, tabletas, descalcificador, sticks, infusores: no los pude abrir.
- FOB/MOQ reales en Alibaba/Made-in-China/1688 para pen TDS, tiras, tabletas, sticks: no hay precio visible en los resultados; todos los FOB de la tabla son EST.
- Aranceles/IGV reales de las partidas (medidores de pH/TDS, tiras reactivas, preparaciones): no verificados; el factor 1.35 es supuesto.

## 2. ¿Cuáles generan ingresos recurrentes (refills) tipo cartucho?

### Takeaway
Recurrentes plausibles: tiras de prueba (relleno), tabletas de limpieza de bidón, y gotas/sticks de minerales; sin embargo ningún precio peruano está verificado y el único con ticket suficiente (mineral) es el más riesgoso regulatoriamente. Los demás son complementos de bajo ticket para elevar LTV de la base instalada.

### Cited Findings
- Formato de dosificación de gotas de remineralización: ~2-4 gotas por vaso (resumen de búsqueda, no fuente primaria) — [Accio listados](https://www.accio.ai/find-product/potassium-magnesium-liquid-drops).
- Tabletas de limpieza de botella se venden como recarga: 1 tableta = 500 ml de limpiador (Chile) o 2 tabletas = 1 L (Colombia) — [Easy.cl](https://www.easy.cl/recargas-limpiabanos-mk1baejwa4/p), [Farmatodo CO](https://www.farmatodo.com.co/producto/500030476-multisuperficies-repuesto-x2-tabletas--tabi-clean-colombia-2-tabletas-efervescentes-x-1). Son para botellas pequeñas, no verificadas para bidones de 20 L.
- Referencia de producto mineral de marca: concentrado de oligoelementos en EE.UU. y Hawái con MSRP US$24.95 (Faire) — [Faire](https://faire.com/product/p_qzedb9y65q); precio internacional, no peruano.

### Inferences
- EST: gotas de magnesio 30-60 ml a S/39-59 con landed S/4-8 dan margen bruto 85-90% y duran ~1 mes de uso familiar, lo que lo haría el mejor refill de la categoría, pero ver pregunta 3.
- EST: pack de 12 tabletas a S/19-29 con landed ~S/3-4; margen bruto ~85%, ticket bajo, bueno como add-on en WhatsApp post-entrega, no standalone con Meta.
- Los consumibles no necesitan Meta si se venden a clientes existentes vía WhatsApp (costo de adquisición ~0), lo que evita el problema del S/65-120 de anuncio.

### Gaps
- Tasa real de recompra y precio dispuesto a pagar: no hay datos; requiere test.
- Vida útil y dosis correcta de tabletas para bidón de 20 L: sin fuente.

## 3. Factibilidad regulatoria en Perú (gotas de mineral y productos alcalinos)

### Takeaway
No pude confirmar una vía clara. Las gotas minerales para agua de bebida probablemente caen bajo DIGESA, ya sea como aditivo/alimento (registro sanitario) o como insumo de tratamiento de agua (procedimiento distinto), y los claims de salud se arriesgan ante Indecopi. Recomendación: tratarlas como NO lanzables hasta consulta formal con DIGESA.

### Cited Findings
- DIGESA tramita desinfectantes e insumos para tratar agua de consumo humano vía VUCE, procedimiento N° 27 del TUPA (D.S. 001-2016-SA) — [DIGESA expediente RSDAN31625](https://www.digesa.minsa.gob.pe/Expedientes/RSDAN_REGISTROS/RSDAN31625.pdf).
- El registro sanitario de alimentos industrializados figuraba en el procedimiento N° 30 del TUPA vía VUCE (presentación PromPerú 2016, numeración posiblemente desactualizada) — [PromPerú repositorio](https://repositorio.promperu.gob.pe/bitstreams/0024ddea-cc35-4be8-ba15-98c409d16e68/download).
- Una resolución DIGESA de 2003 trata a los aditivos como sustancias que no son alimentos y los distingue del registro de alimentos — [RD 06841-2003](https://cdn.www.gob.pe/uploads/document/file/282217/253984_RD06841-2003.pdf20190110-18386-18idp14.pdf).
- Suplementos alimenticios: ComexPerú (oct 2024) comenta el Proyecto de Ley 6435/2023-CR que crearía un registro sanitario específico a cargo de DIGESA; no confirmé si fue aprobado — [ComexPerú](https://www.comexperu.org.pe/upload/articles/proyectos-de-ley/carta_salud_registro-sanitario-en-suplementos-alimenticios_oct2024.pdf).
- Indecopi: la publicidad engañosa de alimentos puede sancionarse hasta con 700 UIT; ha abierto investigaciones desde la Ley 30021 — [Infomercado](https://infomercado.pe/indecopi-publicidad-de-productos-alimenticios-enganosa-puede-ser-sancionada-hasta-con-700-uit), [LP Derecho sobre Ley 30021](https://lpderecho.pe/octogonos-ley-30021-publicidad-informacion/).
- Vademécum Perú lista productos orales de magnesio con registro sanitario DN (medicamentos/suplementos), lo que indica que los productos de magnesio ingerible circulan con registro — [Vademécum PE](https://www.vademecum.es/peru/equivalencias/1465336/bio-magnes-250-mg-11-mg-1-sobre-polvo-efervescente-para-sol-oral).

### Inferences
- Gotas de magnesio para agua de bebida: riesgo ALTO. Por dosis ingerible, DIGESA probablemente las trate como alimento/suplemento (registro sanitario o notificación) y no como aditivo para agua; vender sin registro expone a decomiso y a que ML/Meta bajen la publicación. Claims como "alcaliniza", "cura", "mejora la salud" no deben usarse. Máximo prudente: describir el sabor/dureza del agua ya registrados.
- Sticks/cartuchos mineralizadores y alkaline sticks: riesgo MEDIO-ALTO; si son materiales en contacto con agua de bebida, aplican requisitos de materiales en contacto con alimentos; los claims de "alcalino" no tienen respaldo.
- Medidor TDS, tiras, tabletas de limpieza (producto de limpieza, no ingerible), caño, stickers, cubeteras: riesgo BAJO; evitar prometer "detecta plomo/metales" (tiras no confiables) y claims sanitarios sobre potabilidad.
- Medidor TDS: claim seguro = "mide sólidos disueltos", nunca "mide pureza/seguridad"; TDS alto en Vivo es por magnesio, y la comunicación debe explicarlo.

### Gaps
- Texto vigente del TUPA DIGESA (2026) y clasificación formal de gotas minerales: no verificado; requiere consulta escrita a DIGESA.
- Estado del proyecto de ley de suplementos (6435/2023-CR): sin confirmar.
- Reglas Indecopi específicas sobre claims de "agua alcalina": no encontré fuente.
- SUNAT: partidas arancelarias y tributos: no consultado.
