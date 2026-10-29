# Textos de elvo.pe que contradicen a Sofía (tema "elvo mineral (velocidad)", el publicado)

No los pude editar yo: Shopify solo me deja escribir en temas sin publicar, y este es el que está en vivo. Se cambian desde Personalizar tema (o Editar código) buscando el texto en el archivo indicado.

## Prioridad 1 — afectan la compra del Nativo
| Qué dice hoy | Dónde | Poner |
|---|---|---|
| «Garantía de por vida» (franja, tabla de ficha, FAQ, insignia) | `sections/elvo-nativo-ficha.liquid` (2 veces), `sections/elvo-home-faq.liquid`, `templates/product.elvo.json` (`guarantee_text`, `badge_2`, `garantias`, FAQ), `sections/elvo-vivo-php.liquid` | «Garantía de 1 año» |
| «seña de S/50» en provincia | `sections/elvo-home-faq.liquid`, `sections/elvo-mineral-home.liquid`, `sections/elvo-llega.liquid` («Lo separas con S/50»), `sections/elvo-pdp-cierre.liquid` (`prov_pago`), `templates/product.elvo.json` (varias) | «S/20» (y «adelanto», no «contraentrega» en provincia) |
| «Incluye lámpara UV de regalo» / «desbloquea tu lámpara UV de regalo» | `sections/elvo-pdp.liquid`, `snippets/elvo-cart-drawer.liquid`, `sections/elvo-planes.liquid` (poner «Valor de la lámpara» en 0) | «1 repuesto incluido» (el regalo es el repuesto) |
| «pH 8.5 certificado», «Agua alcalina pH 8.5», «tendencia alcalina» (Nativo) | `sections/elvo-nativo-pdp.liquid` (beneficios y estadística), `sections/elvo-nativo-ficha.liquid`, `sections/elvo-products-main.liquid`, `sections/elvo-trust.liquid`, `sections/elvo-recorrido.liquid`, `sections/elvo-mineral-home.liquid`, `templates/product.nativo.json` («Alcalina, directo del caño»), `templates/product.elvo.json`, `templates/index.json` | Quitar la mención al pH; usar «Agua de calidad como la embotellada, directo de tu caño» |
| «Elimina arsénico, plomo y mercurio» / «El único filtro en Perú que…» | `sections/elvo-nativo-pdp.liquid`, `sections/elvo-vivo-php.liquid` | «Retiene metales pesados como arsénico y plomo» (sin mercurio, sin «el único») |
| Etapa «KDF-F» | `sections/elvo-explosionado.liquid`, `sections/elvo-tecnologia.liquid`, `sections/elvo-mineral-home.liquid`, `sections/elvo-nativo-ficha.liquid`, `sections/elvo-nativo-pdp.liquid`, `sections/elvo-vivo-php.liquid`, `templates/product.nativo.json`, `templates/product.elvo.json`, `templates/index.json` | «Etapa antimetales» / «Retiene metales pesados» |

## Prioridad 2
- «Contraentrega» en provincia (`elvo-home-faq`, `elvo-mineral-home`): provincia es adelanto de S/20 y el saldo cuando llega.
- Tabla comparativa «Agua con tendencia alcalina / Agua alcalina mineral» (`elvo-comparar.liquid`, `elvo-vivo-php.liquid`): solo aplica al Vivo; verificar que el Nativo no la muestre.
- Alivio: «Medidor de pH gratis con tu compra» (`elvo-alivio-comprar.liquid`) — confirmar que sigue siendo cierto.

## Ya está bien
Dirección de recojo (Jr. Quilca 565, Breña, L–V 9 a 5), logos de canales (Falabella, Sodimac, Promart, Plaza Vea, Oechsle).
