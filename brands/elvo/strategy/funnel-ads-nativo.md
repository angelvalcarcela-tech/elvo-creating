# elvo· Nativo — Estrategia de funnel para Meta Ads

Fecha: 2026-10-22 · Producto: Nativo (S/ 299 · 349 · 399) · Mercado: Perú · Estilo: v3 cobalto (`visual-guidelines.md`)
Doctrina manda: sin miedo, sin urgencia, sin exclamaciones, cifra antes que superlativo. Claims solo de `products.json`.

## 1 · Punto de partida (datos propios, cuenta 893663859368314, histórico, USD)

- Compras web, costo por compra típico en prospección: US$25–33 (ROAS ~3). Retargeting: US$12–14 (ROAS 8–10).
- Mejores señales de Nativo: RTG Cuotas (US$11.9, ROAS 9.7) · N12 de "Último de Nativo" (US$8.4, ROAS 11.7) · "Hervir no basta" limpio (US$13.5, ROAS 8.0) · "¿Un solo cartucho?" (CTR 3.6%, ROAS 5.3).
- Peor: "Hervir no saca los metales" v2 (US$99), "Precio a la vista" (US$42), "Deja de cargar bidones" a escala (US$41).
- Las campañas de clic a WhatsApp (~US$3,000 gastados) no se pueden evaluar: la venta ocurre en el chat y Meta no la ve.
- Muchos "ganadores" tienen 1–4 compras: son pistas, no certezas.
- Mercado (Ad Library, Perú): compite por precio bajo (S/129–169) y por "pura y segura". Nahua ocupa "sin cloro, sin bidones". Nuwa usa el mito de los minerales.

## 2 · Idea rectora

elvo· no compite por precio ni por miedo. Compite por **el gesto**: el primer vaso del día. Beneficio primero, dato como apoyo.
Diferenciadores verificados a explotar: conserva los minerales · reduce cloro, olores y sabores · núcleo con aviso por WhatsApp · instalación en 5 min · devolución si no encaja · 30 días de prueba.

## 3 · Funnel

### TOFU · Descubrimiento (beneficio primero)
- Objetivo: ventas web (compra). Audiencia amplia: Lima + provincias, 28–55, sin intereses estrechos.
- Creativos: P1 sabor sin cloro · P2 minerales · P3 5 minutos · P4 núcleo 18 meses.
- Formatos: estático 4:5 y 9:16 (y luego video corto de agua cayendo, macro).
- KPIs: CTR de enlace ≥ 1.8% · costo por compra ≤ US$30 · frecuencia < 2.5.

### MOFU · Consideración
- Audiencia: vieron ≥ 50% de video, interactuaron con la página/IG (30 d), visitantes de la web sin ver el producto (30 d). Excluir compradores.
- Creativos: anatomía del núcleo (callouts, 6 etapas como dato de apoyo) · "Un núcleo, no un bidón" (comparativa sin nombrar marcas) · mito "hervir no basta" en versión calma, sin claim de plomo.
- KPIs: CTR ≥ 1.5% · costo por visita al producto · tasa de añadir al carrito.

### BOFU · Conversión (retargeting)
- Audiencia: vieron producto / añadieron al carrito / iniciaron compra (7–14 d). Excluir compradores.
- Creativos: R1 cuotas (hasta 6 sin intereses) · R2 "Si no encaja en tu caño, te devolvemos tu dinero. 30 días de prueba." · R3 pago contra entrega + envío gratis.
- KPIs: costo por compra ≤ US$15 · ROAS ≥ 6.

### Mensajería (WhatsApp) — carril paralelo
- Mantener solo si se mide. Pendiente: devolver las ventas de WhatsApp a Meta (evento de compra por Conversions API / importación) para poder comparar con web.
- Hasta entonces: no escalar CTWA; sí dejar una campaña pequeña como control.

### Post-compra y retención (no es ad de adquisición)
- WhatsApp: instrucción de instalación, aviso de cambio de núcleo (18 meses), propuesta de plan de 3 o 6 años al renovar.
- Audiencia de compradores: excluida de TOFU/MOFU/BOFU; lookalike 1–3% para TOFU.

## 4 · Reparto inicial de presupuesto (hipótesis a validar)

| Etapa | % | Por qué |
|---|---|---|
| TOFU | 60 | Alimenta todo el funnel; costo ~US$30 por compra |
| MOFU | 15 | Pool chico; calienta antes del retargeting |
| BOFU | 25 | Mejor ROAS, pero se satura rápido (pool pequeño) |

Monto mensual: pendiente de definir por el dueño de la cuenta.

## 5 · Reglas de prueba y escala (propuestas, basadas en tu historial)

- Cada creativo recibe ~US$40–50 antes de juzgar.
- Pausar: ≥ US$45 gastados, 0 compras y CTR < 1.2%.
- Candidato a escalar: ≥ 3 compras y costo por compra < US$25 (prospección) o < US$15 (retargeting). Escalar ≤ 20–30% cada 3 días.
- Rotar creativo si frecuencia > 3 o CTR cae 30% vs. la primera semana.
- Una variable por prueba: titular/beneficio primero, formato después.

## 6 · Matriz de creativos (Nativo)

| Código | Etapa | Titular | Apoyo (verificado) |
|---|---|---|---|
| NAT-T-P1 | TOFU | El primer vaso del día, sin sabor a cloro. | Reduce cloro, olores y sabores. |
| NAT-T-P2 | TOFU | Agua mejor, con todos sus minerales. | Conserva los minerales. Tendencia alcalina, pH ~8.5. |
| NAT-T-P3 | TOFU | Mejor agua en 5 minutos. | La instalas tú. Sin electricidad, obras ni gasfitero. |
| NAT-T-P4 | TOFU | Un núcleo, 18 meses. | Te avisamos por WhatsApp cuando toca cambiarlo. |
| NAT-M-A1 | MOFU | Lo que pasa dentro del núcleo. | Anatomía con callouts 01–04. |
| NAT-M-A2 | MOFU | Un núcleo en lugar de bidones. | Agua mejor directo de tu caño. |
| NAT-B-R1 | BOFU | Tu Nativo, en hasta 6 cuotas sin intereses. | Envío gratis a todo el Perú. |
| NAT-B-R2 | BOFU | Si no encaja en tu caño, te devolvemos tu dinero. | 30 días de prueba. |
| NAT-B-R3 | BOFU | Págalo cuando lo recibas. | Pago contra entrega. |

Formatos: 4:5 y 9:16 por concepto. Producto real siempre (`nativo-front.png`).

## 7 · Qué retirar o corregir de lo activo

- "Hasta el 24 de octubre" (K+C, anuncio AQA): urgencia con fecha. Quitar.
- "5 años" (C2): el núcleo dura 18 meses; los planes de 3 y 6 años incluyen más núcleos. No usar "5 años".
- "Nativo + kit gratis" (K4): la mini lámpara UV se retiró como regalo el 28-sep-2026. Confirmar que sigue pausado.
- "Separa con S/50 por Yape" (PV): no figura en `verified_claims`. Confirmar la oferta antes de repetirla.
- Claim de plomo / metales pesados: sin disclaimer no se usa.
- Reseñas y estrellas: solo si son reales y visibles en la tienda.

## 8 · Calendario

| Semana | Qué |
|---|---|
| 1 | Generar P1–P4 + R1 (10 imágenes). Revisar. Subir a Meta en borrador. |
| 2 | Lanzar TOFU (4 conceptos) + R1. Leer a los 5–7 días. |
| 3 | Ganadores a escala; generar MOFU (A1, A2) y R2/R3. |
| 4 | Revisar CTWA con ventas de WhatsApp conectadas. Primera ronda de rotación. |

## 9 · Pendientes por decidir

1. Presupuesto mensual y moneda de referencia.
2. ¿WhatsApp es canal principal o de apoyo?
3. ¿Se conectan las ventas de WhatsApp a Meta?
4. Confirmar oferta de pago/separación antes de usarla en piezas.
