#!/usr/bin/env python3
"""Genera la home mineral: preview.html (mock local) y sections.json (para templates/index.json)."""
import json, re, os
D = os.path.dirname(os.path.abspath(__file__))
WA = '51929190100'
def wa(msg): return f'https://wa.me/{WA}?text=' + msg.replace(' ', '%20')

# Bloques liquid: [[L]]...[[/L]] se ejecuta en Shopify y se elimina en el mock.
# Expresiones {{ x }} se sustituyen en el mock con MOCK[x].
MOCK = {
 'nativo_url': '/products/elvonativo', 'nativo_price': '299', 'nativo_img': 'nativo-front.png', 'vivo_img': 'vivo-front.png',
 'vivo_url': wa('Hola,%20quiero%20saber%20m%C3%A1s%20de%20elvo%C2%B7%20Vivo'),
 'alivio_url': wa('Hola,%20me%20interesa%20Alivio'),
 'cero_url': wa('Hola,%20me%20interesa%20Cero'),
}
LIQ_URLS = '''[[L]]{%- assign p_nativo = all_products['elvonativo'] -%}
{%- assign p_vivo = all_products['elvovivo'] -%}
{%- assign p_alivio = all_products['elvo-alivio'] -%}
{%- assign p_cero = all_products['elvo-cero'] -%}
{%- assign nativo_url = p_nativo.url | default: '/products/elvonativo' -%}
{%- assign nativo_price = p_nativo.price | money_without_currency | split: '.' | first -%}
{%- assign nativo_img = 'elvo-nativo-front.png' | file_url -%}
{%- assign vivo_img = 'elvo-vivo-front.png' | file_url -%}
{%- if p_vivo.id -%}{%- assign vivo_url = p_vivo.url -%}{%- else -%}{%- assign vivo_url = 'https://wa.me/''' + WA + '''?text=Hola%2C%20quiero%20saber%20m%C3%A1s%20de%20elvo%C2%B7%20Vivo' -%}{%- endif -%}
{%- if p_alivio.id -%}{%- assign alivio_url = p_alivio.url -%}{%- else -%}{%- assign alivio_url = 'https://wa.me/''' + WA + '''?text=Hola%2C%20me%20interesa%20Alivio' -%}{%- endif -%}
{%- if p_cero.id -%}{%- assign cero_url = p_cero.url -%}{%- else -%}{%- assign cero_url = 'https://wa.me/''' + WA + '''?text=Hola%2C%20me%20interesa%20Cero' -%}{%- endif -%}[[/L]]'''

S = {}  # nombre -> (titulo editor, html)

S['hero'] = ('Mineral · Hero', LIQ_URLS + '''
<section class="m m-hero"><div class="m-hero-grid">
<div class="m-hero-copy">
<span class="m-eyebrow">elvo· · Purificación doméstica de agua</span>
<h1>El agua es el primer ingrediente.</h1>
<p class="m-lead">Un purificador para cada lugar donde el agua te toca. Cuéntanos cómo es tu casa y te ayudamos a elegir.</p>
<div class="m-actions"><a class="m-btn m-btn--solid" href="#linea">Ver la línea</a><a class="m-btn m-btn--line" href="''' + wa('Hola,%20quiero%20elegir%20mi%20purificador%20elvo%C2%B7') + '''">Escríbenos</a></div>
<p class="m-hero-note">30 días de prueba · Envío gratis a todo el Perú · Garantía de 1 año</p>
</div>
<div class="m-hero-img"><img src="{{ nativo_img }}" alt="elvo· Nativo, purificador para el caño, con un vaso de agua" loading="eager"></div>
</div></section>''')

S['linea'] = ('Mineral · La línea', '''
<section class="m m-sec" id="linea"><div class="m-wrap">
<span class="m-eyebrow">La línea</span>
<h2 class="m-h2">Un purificador para cada lugar donde el agua te toca.</h2>
<div class="m-line">
<a class="m-card" href="{{ nativo_url }}"><div class="m-card-img"><img src="{{ nativo_img }}" alt="elvo· Nativo" loading="lazy"></div><div class="m-card-body"><span class="m-card-tag">Para el caño</span><h3>Nativo</h3><p>Retiene plomo y metales pesados*. Se instala en 5 minutos, sin gasfitero.</p><div class="m-card-foot">Ver Nativo <span>· desde S/ {{ nativo_price }}</span></div></div></a>
<a class="m-card" href="{{ vivo_url }}"><div class="m-card-img"><img src="{{ vivo_img }}" alt="elvo· Vivo" loading="lazy"></div><div class="m-card-body"><span class="m-card-tag">Para el caño</span><h3>Vivo</h3><p>Aporta magnesio y reduce cloro, olores y sabores. Agua más rica, directo de tu caño.</p><div class="m-card-foot">Consultar Vivo</div></div></a>
<a class="m-card" href="{{ alivio_url }}"><div class="m-card-img"><span class="m-card-ph m-card-ph--dark">Alivio</span></div><div class="m-card-body"><span class="m-card-tag">Para tener reserva</span><h3>Alivio</h3><p>Purificador de bidón de 16 y 22 litros. Se llena con una jarra, sin electricidad ni conexión al caño.</p><div class="m-card-foot">Consultar Alivio</div></div></a>
<a class="m-card" href="{{ cero_url }}"><div class="m-card-img m-card-img--slate"><span class="m-card-ph">Cero</span></div><div class="m-card-body"><span class="m-card-tag">Para la pureza máxima</span><h3>Cero</h3><p>Ósmosis inversa. Agua fría y caliente en un solo equipo.</p><div class="m-card-foot">Consultar Cero</div></div></a>
</div>
<p class="m-fine" style="color:var(--piedra-osc)">*Según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada.</p>
</div></section>''')

S['necesitas'] = ('Mineral · ¿Qué necesitas?', '''
<section class="m m-sec"><div class="m-wrap">
<span class="m-eyebrow">¿Qué necesitas?</span>
<h2 class="m-h2">Empieza por tu casa, no por el equipo.</h2>
<div class="m-need">
<a href="{{ vivo_url }}"><span class="m-need-q">Quiero que el agua del caño sepa mejor.</span><span class="m-need-a">Vivo aporta magnesio y reduce cloro, olores y sabores.</span><span class="m-need-go">Ver Vivo →</span></a>
<a href="{{ nativo_url }}"><span class="m-need-q">Quiero retener metales pesados.</span><span class="m-need-a">Nativo retiene plomo y metales pesados* en el mismo caño.</span><span class="m-need-go">Ver Nativo →</span></a>
<a href="{{ alivio_url }}"><span class="m-need-q">Quiero tener agua guardada.</span><span class="m-need-a">Alivio se llena con una jarra. Sin electricidad, sin conexión al caño.</span><span class="m-need-go">Ver Alivio →</span></a>
<a href="{{ cero_url }}"><span class="m-need-q">Quiero el máximo nivel de purificación.</span><span class="m-need-a">Cero usa ósmosis inversa y entrega agua fría y caliente.</span><span class="m-need-go">Ver Cero →</span></a>
</div>
<div class="m-actions"><a class="m-btn m-btn--line" href="''' + wa('Hola,%20no%20s%C3%A9%20cu%C3%A1l%20elvo%C2%B7%20elegir') + '''">No sé cuál elegir: escríbenos</a></div>
</div></section>''')

S['formulacion'] = ('Mineral · Cómo funciona (pizarra)', '''
<section class="m m-sec m-slate"><div class="m-wrap">
<span class="m-eyebrow">Formulación</span>
<h2 class="m-h2">Tres pasos. Un solo gesto.</h2>
<p class="m-lead">Sin electricidad, sin obras y sin gasfitero.</p>
<div class="m-steps">
<div class="m-step"><span class="m-step-n">01</span><h3>Instala</h3><p>Lo instalas tú en 5 minutos. Incluye adaptador universal de jebe y derivador.</p></div>
<div class="m-step"><span class="m-step-n">02</span><h3>Purifica</h3><p>Seis etapas de filtración: carbón activado, KDF-F, nanotecnología, aluminosilicato sintético, plata coloidal y plata iónica.</p></div>
<div class="m-step"><span class="m-step-n">03</span><h3>Toma</h3><p>Conserva los minerales naturales del agua. El núcleo dura 18 meses de uso normal y te avisamos por WhatsApp cuando toque cambiarlo.</p></div>
</div>
<p class="m-fine">Descrito para elvo· Nativo. *Según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada y del cambio oportuno del núcleo. elvo· no es un dispositivo médico ni reemplaza el tratamiento de agua de la red pública.</p>
</div></section>''')

S['marca'] = ('Mineral · Marca y valores', '''
<section class="m m-sec m-brand"><div class="m-wrap"><div class="m-brand-grid">
<div><span class="m-eyebrow">elvo·</span><h2>Todo cuidado empieza en ella.</h2><p class="m-lead">El agua es lo primero que llega a tu casa y lo último en lo que solemos pensar. Diseñamos objetos que se instalan sin ruido y duran.</p></div>
<div class="m-vals">
<div class="m-val"><span class="m-val-n">01</span><div><h3>Longevidad.</h3><p>Objetos que duran años, no temporadas.</p></div></div>
<div class="m-val"><span class="m-val-n">02</span><div><h3>Formulación consciente.</h3><p>Lo que se retira y lo que se aporta, dicho con exactitud.</p></div></div>
<div class="m-val"><span class="m-val-n">03</span><div><h3>Consulta, no venta.</h3><p>Acompañar la decisión antes que empujarla.</p></div></div>
<div class="m-val"><span class="m-val-n">04</span><div><h3>Vida sin prisa.</h3><p>Contra la tendencia; a favor de lo perdurable.</p></div></div>
</div>
</div></div></section>''')

S['donde'] = ('Mineral · Dónde comprar', '''
<section class="m m-sec m-where"><div class="m-wrap">
<span class="m-eyebrow">Dónde comprar</span>
<h2 class="m-h2">Encuentra elvo·</h2>
<p class="m-lead" style="color:var(--pizarra)">En la tienda, por WhatsApp o en las principales cadenas del país.</p>
<div class="m-where-list">
<div>elvo.pe<small>Tienda online</small></div>
<a href="''' + wa('Hola,%20quiero%20comprar%20elvo%C2%B7') + '''">WhatsApp<small>Te acompañamos a elegir</small></a>
<div>Falabella<small>Disponible</small></div>
<div>Sodimac<small>Disponible</small></div>
<div>Plaza Vea<small>Disponible</small></div>
<div>Promart<small>Disponible</small></div>
<div>Oechsle<small>Disponible</small></div>
<div>Mercado Libre<small>Online</small></div>
</div>
</div></section>''')

S['faq'] = ('Mineral · Preguntas', '''
<section class="m m-sec"><div class="m-wrap"><div class="m-faq">
<div><span class="m-eyebrow">Preguntas frecuentes</span><h2 class="m-h2">¿Tienes dudas?</h2></div>
<div>
<details><summary>¿Se adapta a mi caño?</summary><p>Sí. Incluye un adaptador universal de jebe y un derivador para grifos estándar. Si tienes dudas, mándanos una foto de tu caño por WhatsApp y te confirmamos antes de comprar.</p></details>
<details><summary>¿Cada cuánto cambio el núcleo?</summary><p>Cada 18 meses de uso normal. Te avisamos por WhatsApp cuando toque cambiarlo.</p></details>
<details><summary>¿Cuándo llega mi pedido?</summary><p>En Lima, el mismo día si confirmas antes de las 4 p. m. (lunes a sábado). En provincias, en 2 días. También puedes recogerlo en Jr. Varela 1235, Breña, de lunes a sábado de 9 a. m. a 5 p. m.</p></details>
<details><summary>¿Cómo pago?</summary><p>Con Yape, tarjeta en hasta 6 cuotas sin interés o contraentrega. En provincias, la contraentrega va por agencia Shalom con una seña de S/ 50 y tu DNI.</p></details>
<details><summary>¿Qué incluye mi pedido?</summary><p>El purificador y los núcleos de tu plan: 1 en el de 18 meses, 2 en el de 3 años y 4 en el de 6 años. También el adaptador universal de jebe.</p></details>
<details><summary>¿Y si no me convence?</summary><p>Tienes 30 días de prueba. Si no te convence, escríbenos por WhatsApp y te devolvemos tu dinero. Además, el equipo tiene 1 año de garantía.</p></details>
</div></div></div></section>''')

S['cierre'] = ('Mineral · Cierre', '''
<section class="m m-sec m-close"><div class="m-wrap">
<h2>Escríbenos y te acompañamos.</h2>
<p class="m-lead">Cuéntanos cómo es el agua de tu casa y te ayudamos a elegir. Sofía te responde por WhatsApp.</p>
<div class="m-actions"><a class="m-btn m-btn--solid" href="''' + wa('Hola,%20quiero%20elegir%20mi%20purificador%20elvo%C2%B7') + '''">Hablar por WhatsApp</a><a class="m-btn m-btn--line" href="#linea">Ver la línea</a></div>
</div></section>''')

ORDER = ['hero', 'linea', 'necesitas', 'formulacion', 'marca', 'donde', 'faq', 'cierre']

def preview(html):
    html = re.sub(r'\[\[L\]\].*?\[\[/L\]\]', '', html, flags=re.S)
    return re.sub(r'\{\{\s*(\w+)\s*\}\}', lambda m: MOCK[m.group(1)], html)

def live(html):
    return html.replace('[[L]]', '').replace('[[/L]]', '')

if __name__ == '__main__':
    css = open(f'{D}/mineral.css').read()
    body = '\n'.join(preview(S[k][1]) for k in ORDER)
    open(f'{D}/preview.html', 'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>{css}</style></head><body style="margin:0">{body}</body></html>')
    out = {k: {'name': S[k][0], 'liquid': live(S[k][1])} for k in ORDER}
    json.dump({'order': ORDER, 'sections': out}, open(f'{D}/sections.json', 'w'), ensure_ascii=False, indent=1)
    print('ok', len(body))
