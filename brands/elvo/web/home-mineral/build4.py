#!/usr/bin/env python3
"""Home v4: tienda densa (sin scroll fijo). preview4.html + section4.liquid."""
import re, os
from build_home import LIQ_URLS, MOCK, wa
import build3
D = os.path.dirname(os.path.abspath(__file__))
WAHOLA = wa('Hola,%20quiero%20elegir%20mi%20purificador%20elvo%C2%B7%20%5BWEB-HOME%5D')

NATIVO_FORM = '''[[L]]<form method="post" action="/cart/add" accept-charset="UTF-8"><select name="id" aria-label="Plan">{%- for v in p_nativo.variants -%}<option value="{{ v.id }}"{% unless v.available %} disabled{% endunless %}>{{ v.title }} · S/ {{ v.price | money_without_currency | split: '.' | first }}</option>{%- endfor -%}</select><button class="a-pill a-pill--s a-pill--b" type="submit">Agregar al carrito</button></form>[[/L]][[M]]<form onsubmit="return false"><select><option>18 meses · S/ 299</option><option>3 años · S/ 349</option><option>6 años · S/ 399</option></select><button class="a-pill a-pill--s a-pill--b">Agregar al carrito</button></form>[[/M]]'''

HTML = '''
<div class="a">
<section class="a-hero">
 <div class="a-hero-l">
  <span class="a-lab" style="color:rgba(255,255,255,.9)">elvo· · Purificación doméstica de agua</span>
  <h1>El agua es el primer ingrediente.</h1>
  <p class="sub">Un purificador para cada lugar donde el agua te toca.</p>
  <div class="a-row"><span class="a-chip">Oferta hasta el 24 de octubre</span><span class="a-chip">Envío gratis</span><span class="a-chip">30 días de prueba</span></div>
  <div class="a-row"><a class="a-pill a-pill--s" href="{{ nativo_url }}">Comprar Nativo · desde S/ {{ nativo_price }}</a><a class="a-pill a-pill--wh" href="#linea">Ver la línea</a></div>
 </div>
 <div class="a-hero-r"><img src="{{ nativo_img }}" alt="elvo· Nativo, purificador para el caño, con un vaso de agua"></div>
</section>

<div class="a-ben"><div class="a-w">
 <div><b>30</b>días de prueba</div><div><b>1</b>año de garantía</div><div><b>6</b>cuotas sin interés</div><div><b>PE</b>envío gratis a todo el Perú</div>
</div></div>

<section class="a-sec" id="linea"><div class="a-w">
 <div class="a-head"><div><span class="a-lab">La línea</span><h2 class="a-h2">Elige tu purificador</h2></div><a class="a-pill" href="#comparar">Comparar los cuatro</a></div>
 <div class="a-grid">
  <article class="a-card"><a class="a-card-img" href="{{ nativo_url }}"><img src="{{ nativo_img }}" alt="elvo· Nativo"><span class="a-badge">Para el caño</span></a>
   <div class="a-card-b"><h3>Nativo</h3><p>Retiene plomo y metales pesados*. Se instala en 5 minutos, sin gasfitero.</p>
   <div class="a-price"><small>Desde</small> S/ {{ nativo_price }}</div>''' + NATIVO_FORM + '''</div></article>
  <article class="a-card"><a class="a-card-img" href="{{ vivo_url }}"><img src="{{ vivo_img }}" alt="elvo· Vivo"><span class="a-badge">Para el caño</span></a>
   <div class="a-card-b"><h3>Vivo</h3><p>Aporta magnesio y reduce cloro, olores y sabores. Agua más rica, directo de tu caño.</p>
   <div class="a-price"><small>Consulta el precio</small></div><a class="a-pill a-pill--b" href="{{ vivo_url }}">Consultar por WhatsApp</a></div></article>
  <article class="a-card"><a class="a-card-img a-card-img--c" href="{{ alivio_url }}"><span class="a-big">16 · 22 L</span><span class="a-badge">Para tener reserva</span></a>
   <div class="a-card-b"><h3>Alivio</h3><p>Purificador de bidón. Se llena con una jarra. Sin electricidad, sin conexión al caño.</p>
   <div class="a-price"><small>Consulta el precio</small></div><a class="a-pill a-pill--b" href="{{ alivio_url }}">Consultar por WhatsApp</a></div></article>
  <article class="a-card"><a class="a-card-img a-card-img--m" href="{{ cero_url }}"><span class="a-big">Cero</span><span class="a-badge">Pureza máxima</span></a>
   <div class="a-card-b"><h3>Cero</h3><p>Ósmosis inversa. Agua fría y caliente en un solo equipo.</p>
   <div class="a-price"><small>Consulta el precio</small></div><a class="a-pill a-pill--b" href="{{ cero_url }}">Consultar por WhatsApp</a></div></article>
 </div>
 <p class="a-fine">*Según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada.</p>
</div></section>

<section class="a-sec a-revs"><div class="a-w">
 <div class="a-head"><div><span class="a-lab">Clientes</span><h2 class="a-h2">Lo que cuentan en casa</h2></div></div>
 <div class="a-rev-grid">
  <figure class="a-rev"><blockquote>“Lo instalé en menos de 5 minutos, funciona perfecto y tiene muy buen caudal.”</blockquote><figcaption><i>L</i><span><b>Lucía P.</b> · Ica<small>Compra verificada</small></span></figcaption></figure>
  <figure class="a-rev"><blockquote>“El agua sale cristalina, sin sabor ni olor.”</blockquote><figcaption><i>C</i><span><b>Carmen S.</b> · Trujillo<small>Compra verificada</small></span></figcaption></figure>
  <figure class="a-rev"><blockquote>“Le consulté a un amigo químico de laboratorio y me dijo que era una muy buena compra y a buen precio.”</blockquote><figcaption><i>R</i><span><b>Roberto M.</b> · Piura<small>Compra verificada</small></span></figcaption></figure>
  <figure class="a-rev"><blockquote>“El agua sale transparente, sin sabor y sin ningún residuo. La instalación fue muy fácil.”</blockquote><figcaption><i>M</i><span><b>María G.</b> · Lima<small>Compra verificada</small></span></figcaption></figure>
 </div>
</div></section>

<section class="a-sec a-need"><div class="a-w">
 <div class="a-head"><div><span class="a-lab">¿Qué necesitas?</span><h2 class="a-h2">Empieza por tu casa</h2></div></div>
 <div class="a-need-grid">
  <a href="{{ vivo_url }}"><div><h3>Que el agua del caño sepa mejor</h3></div><div><p>Vivo aporta magnesio y reduce cloro, olores y sabores.</p><span>Ver Vivo →</span></div></a>
  <a href="{{ nativo_url }}"><div><h3>Retener metales pesados</h3></div><div><p>Nativo retiene plomo y metales pesados* en el mismo caño.</p><span>Ver Nativo →</span></div></a>
  <a href="{{ alivio_url }}"><div><h3>Tener agua guardada</h3></div><div><p>Alivio se llena con una jarra, sin electricidad ni conexión al caño.</p><span>Ver Alivio →</span></div></a>
  <a href="{{ cero_url }}"><div><h3>El máximo nivel de purificación</h3></div><div><p>Cero usa ósmosis inversa y entrega agua fría y caliente.</p><span>Ver Cero →</span></div></a>
 </div>
</div></section>

<section class="a-sec"><div class="a-w">
 <div class="a-head"><div><span class="a-lab">Por dentro</span><h2 class="a-h2">Caño, núcleo, vaso</h2></div></div>
 <div class="a-in">
  <div class="a-in-l">
   <div class="a-steps">
    <div><b>01</b><div><h3>Caño</h3><p>Lo instalas tú, sin obras ni gasfitero.</p></div><em>5 min</em></div>
    <div><b>02</b><div><h3>Núcleo</h3><p>Seis etapas de filtración en un solo cartucho.</p></div><em>6</em></div>
    <div><b>03</b><div><h3>Vaso</h3><p>Tendencia alcalina. Conserva sus minerales.</p></div><em>pH 8.5</em></div>
    <div><b>04</b><div><h3>Cambio</h3><p>Te avisamos por WhatsApp cuando toque.</p></div><em>18 m</em></div>
   </div>
   <p class="a-fine" style="margin:0">Descrito para elvo· Nativo. Resultados según la ficha técnica del núcleo PureCore y la calidad del agua de entrada.</p>
  </div>
  <div class="a-in-r">''' + build3.svg() + '''<p style="font-size:11px;color:#7B9BDD;margin-top:14px">Esquema ilustrativo del núcleo PureCore. El orden y el espesor de cada etapa son representativos.</p></div>
 </div>
</div></section>

<section class="a-sec" id="comparar" style="padding-top:0"><div class="a-w">
 <div class="a-head"><div><span class="a-lab">Comparar</span><h2 class="a-h2">Cuál es para ti</h2></div></div>
 <div class="a-cmp"><table>
  <tr><th></th><th>Nativo</th><th>Vivo</th><th>Alivio</th><th>Cero</th></tr>
  <tr><td>Para</td><td>El caño</td><td>El caño</td><td>Tener agua guardada</td><td>Pureza máxima</td></tr>
  <tr><td>Qué hace</td><td>Retiene plomo y metales pesados*</td><td>Aporta magnesio; reduce cloro, olores y sabores</td><td>Purifica por gravedad</td><td>Ósmosis inversa; agua fría y caliente</td></tr>
  <tr><td>Instalación</td><td>5 min, sin gasfitero</td><td>5 min, sin gasfitero</td><td>Se llena con una jarra</td><td class="no">Consultar</td></tr>
  <tr><td>Electricidad</td><td>Sin electricidad</td><td>Sin electricidad</td><td>Sin electricidad</td><td class="no">Consultar</td></tr>
  <tr><td>Capacidad</td><td class="no">—</td><td class="no">—</td><td>16 o 22 litros</td><td class="no">—</td></tr>
  <tr><td>Núcleo</td><td>18 meses</td><td>18 meses</td><td class="no">Consultar</td><td class="no">Consultar</td></tr>
  <tr><td>Garantía</td><td>1 año</td><td>1 año</td><td class="no">Consultar</td><td class="no">Consultar</td></tr>
 </table></div>
</div></section>

<section class="a-sec" style="padding-top:0"><div class="a-w">
 <p class="a-where"><span>Disponible en</span><b>elvo.pe</b><b>WhatsApp</b><b>Falabella</b><b>Sodimac</b><b>Plaza Vea</b><b>Promart</b><b>Oechsle</b><b>Mercado Libre</b></p>
</div></section>

<section class="a-sec" style="padding-top:8px"><div class="a-w">
 <div class="a-head"><div><span class="a-lab">Preguntas frecuentes</span><h2 class="a-h2">¿Tienes dudas?</h2></div></div>
 <div class="a-faq">
  <details><summary>¿Se adapta a mi caño?</summary><p>Incluye adaptador universal de jebe y derivador. Mándanos una foto por WhatsApp y te confirmamos antes de comprar.</p></details>
  <details><summary>¿Cada cuánto cambio el núcleo?</summary><p>Cada 18 meses de uso normal. Te avisamos por WhatsApp cuando toque cambiarlo.</p></details>
  <details><summary>¿Cuándo llega mi pedido?</summary><p>En Lima, el mismo día si confirmas antes de las 4 p. m. (lunes a sábado). En provincias, en 2 días. También puedes recogerlo en Jr. Varela 1235, Breña.</p></details>
  <details><summary>¿Cómo pago?</summary><p>Con Yape, tarjeta en hasta 6 cuotas sin interés o contraentrega. En provincias, la contraentrega va por agencia Shalom con una seña de S/ 50 y tu DNI.</p></details>
  <details><summary>¿Qué incluye mi pedido?</summary><p>El purificador y los núcleos de tu plan: 1 en el de 18 meses, 2 en el de 3 años y 4 en el de 6 años. También el adaptador universal de jebe.</p></details>
  <details><summary>¿Y si no me convence?</summary><p>Tienes 30 días de prueba. Escríbenos por WhatsApp y te devolvemos tu dinero. El equipo tiene 1 año de garantía.</p></details>
 </div>
</div></section>

<section class="a-end"><h2>¿No sabes cuál elegir? Escríbenos.</h2><a class="a-pill a-pill--wh" href="''' + WAHOLA + '''">Hablar por WhatsApp</a></section>
<p class="a-legal">*Según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada y del cambio oportuno del núcleo. elvo· no es un dispositivo médico ni reemplaza el tratamiento de agua de la red pública. Inversiones Gad SAC.</p>
</div>'''

def live(h): return re.sub(r'\[\[M\]\].*?\[\[/M\]\]', '', h, flags=re.S).replace('[[L]]', '').replace('[[/L]]', '')
def preview(h):
    h = re.sub(r'\[\[L\]\].*?\[\[/L\]\]', '', h, flags=re.S).replace('[[M]]', '').replace('[[/M]]', '')
    return re.sub(r'\{\{\s*(\w+)\s*\}\}', lambda m: MOCK[m.group(1)], h)

if __name__ == '__main__':
    css = open(f'{D}/store.css').read()
    page = LIQ_URLS + HTML
    open(f'{D}/preview4.html', 'w').write('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>' + css + '</style></head><body style="margin:0">' + preview(page) + '</body></html>')
    sec = "{{ 'elvo-mineral.css' | asset_url | stylesheet_tag }}\n" + live(page) + '\n{% schema %}{"name":"elvo· Home v4","settings":[],"presets":[{"name":"elvo· Home v4"}]}{% endschema %}'
    open(f'{D}/section4.liquid', 'w').write(sec)
    print('ok', len(sec), len(css))
