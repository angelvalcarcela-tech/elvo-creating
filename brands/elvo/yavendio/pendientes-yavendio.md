# Pendientes fuera de la plantilla (se hacen en el panel de YaVendio / Meta)

## 1. Arreglar lo que falla hoy
- [ ] Reemplazar la imagen de combos en YaVendio por `imagenes/combos-elvo-nativo.jpg` (mismo nombre: "combos-elvo-nativo").
- [ ] Subir `imagenes/resenas-clientes-elvo.jpg` con el nombre "resenas-clientes-elvo" (Sofía la manda cuando dudan de si es confiable).
- [ ] Catálogo de productos de YaVendio: corregir precios y quitar "(preventa)" de los nombres.
  - Nativo Combo 3 años S/349 (S/389 desde el 2-nov) · Combo 6 años S/489 · Combo 18 meses S/299 (solo sin repuesto)
  - Alivio 16 L S/159 · Alivio 22 L S/198 · Kit repuesto Alivio S/95 · Cero S/1,799 (Cyber)
  - Repuesto Nativo suelto S/199
- [ ] Anuncio Cyber: el texto "2 núcleos + 1 repuesto" confunde. Reescribir como "1 purificador + 1 kit de repuesto (3 años) / 1 purificador + 3 repuestos (6 años), solo por Cyber".
- [ ] Descripciones y FAQs de productos en YaVendio: quitar claims técnicos (arsénico, mercurio, "8 etapas").

## 2. Recordatorios automáticos (hot / warm / cold): textos finales
Todos terminan con una pregunta que empuja al cierre. Imagen o video según se indica.
- **cold1** (video, ~2 h): «Hola 💧 ¿Hoy compras agua en bidones o la hierves? Con el elvo· Nativo tienes agua como la embotellada directo de tu caño. ¿Te cuento cómo?»
- **cold2** (imagen `hoy-vs-elvo`): «Dejas de cargar, comprar y hervir: un solo filtro rinde unos 1.000 bidones 💧 ¿Te muestro los combos?»
- **warm1** (imagen `combos-elvo-nativo`): «Por Cyber tienes 2 opciones: 6 años S/489 (1 purificador + 3 repuestos, el de mayor valor) o 3 años S/349 (1 purificador + 1 kit de repuesto). ¿Cuál te acomoda?»
- **warm2** (imagen `cuotas-sin-intereses`): «Lo pagas en 6 cuotas sin intereses con tarjeta de crédito: desde S/58.17 al mes el de 3 años y S/81.50 el de 6 años 💳 ¿Cuál eliges?»
- **warm3** (video instalación): «¿Te quedó alguna duda de la instalación? Se conecta a tu caño en 5 minutos y tienes 30 días de prueba y 1 año de garantía 😊 ¿Te lo separo?»
- **hot1** (imagen `resenas-clientes-elvo`): «Te guardo tu elvo· Nativo 😊 Solo me faltan tus datos: nombre completo, dirección con distrito y celular (y DNI si es provincia).»
- **hot2** (video): «¿Lo agendamos? En Lima llega hoy o mañana y pagas al recibir; a provincia en 2 a 3 días separando con S/20 ✅»
- Aviso: el precio Cyber termina el 1-nov. Después del 1-nov hay que cambiar estos textos.

## 2b. Anuncios Cyber (texto)
- Nativo 3 años / 6 años: «1 purificador + 1 kit de repuesto (3 años, S/349) · 1 purificador + 3 repuestos (6 años, S/489). Solo hasta el 1 de noviembre. Lima: pagas al recibir · Provincia: separas con S/20. 30 días de prueba y 1 año de garantía.»
- Quitar «2 núcleos + 1 repuesto», «regalo incluido 🎁» y «pago contraentrega».

## 2c. Difusión Cyber (`elvo_cyber_carrusel`, error 132012 «header component parameter should not be empty»)
La plantilla es un carrusel: cada tarjeta exige su imagen de encabezado al momento de enviar y la campaña salió sin ellas. Al lanzar la difusión hay que adjuntar una imagen por tarjeta (sugeridas: `combos-elvo-nativo`, `cuotas-sin-intereses`, `resenas-clientes-elvo`). Además el texto aprobado dice «con regalo incluido 🎁» y «pago contraentrega»: conviene enviar una plantilla nueva a aprobación con el texto de 2b.

## 3. Medición (pendiente de pedir)
Cruzar conversaciones por anuncio de origen: escriben, cierran, y en qué paso se caen.
