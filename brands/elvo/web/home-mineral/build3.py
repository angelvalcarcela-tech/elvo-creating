#!/usr/bin/env python3
"""Home v3 (sistema visual de referencia OQUVA, marca elvo): preview3.html + section3.liquid."""
import re, os
from build_home import LIQ_URLS, MOCK, wa
import build2
D = os.path.dirname(os.path.abspath(__file__))

JS = (build2.JS.replace('.s-hero-img', '.v-hero-r').replace("'.s-", "'.v-").replace('.s-h-track', '.v-h-track'))

def svg():
    stages = [('CARBÓN ACTIVADO', '#101417'), ('KDF-F', '#3355FF'), ('NANOTECNOLOGÍA', '#7B9BDD'),
              ('ALUMINOSILICATO SINTÉTICO', '#BED0DF'), ('PLATA COLOIDAL', '#DCE6EE'), ('PLATA IÓNICA', '#FFFFFF')]
    out = ['<svg viewBox="0 0 640 580" role="img" aria-label="Esquema ilustrativo de las seis etapas del núcleo">']
    out.append('<rect x="100" y="64" width="200" height="456" rx="30" fill="none" stroke="#7B9BDD" stroke-width="1"/>')
    y = 76
    for i, (name, col) in enumerate(stages):
        h = 68
        out.append(f'<rect x="112" y="{y}" width="176" height="{h}" rx="8" fill="{col}" stroke="rgba(255,255,255,.25)"/>')
        cy = y + h / 2
        out.append(f'<circle cx="288" cy="{cy}" r="3" fill="#fff"/><path d="M288 {cy} H340 H372" stroke="rgba(255,255,255,.55)" fill="none"/>')
        out.append(f'<text x="384" y="{cy - 4}" font-size="11" letter-spacing="1.6" fill="#7B9BDD" style="fill:#7B9BDD">0{i+1}</text>')
        out.append(f'<text x="384" y="{cy + 14}" font-size="13" letter-spacing="1.2">[ {name} ]</text>')
        y += h + 6
    out.append('<path d="M200 44 V548" stroke="#3355FF" stroke-width="1.5" stroke-dasharray="3 4"/><path d="M194 540 L200 552 L206 540" fill="#3355FF"/>')
    out.append('<text x="200" y="30" font-size="11" letter-spacing="1.8" text-anchor="middle" style="fill:#7B9BDD">ENTRADA · AGUA DEL CAÑO</text>')
    out.append('<text x="200" y="574" font-size="11" letter-spacing="1.8" text-anchor="middle" style="fill:#7B9BDD">SALIDA · AGUA PURIFICADA</text>')
    out.append('</svg>')
    return ''.join(out)

HTML = '''
<div class="v">
<section class="v-hero">
 <div class="v-hero-l">
  <span class="v-lab">01 // Purificación doméstica de agua</span>
  <div>
   <h1>El agua es el primer ingrediente.</h1>
   <p class="sub">Un purificador para cada lugar donde el agua te toca.</p>
   <div class="v-hero-foot">
    <div class="v-row"><span class="v-chip">5 min</span><span class="v-chip">6 etapas</span><span class="v-chip">18 meses</span></div>
    <div class="v-row"><a class="v-pill v-pill--solid" href="#linea">Ver la línea</a><a class="v-pill v-pill--wh" href="''' + wa('Hola,%20quiero%20elegir%20mi%20purificador%20elvo%C2%B7') + '''">Escríbenos</a></div>
   </div>
  </div>
 </div>
 <div class="v-hero-r"><img src="{{ nativo_img }}" alt="elvo· Nativo, purificador para el caño, con un vaso de agua"><span class="v-tag"><i></i>elvo· Nativo · Para el caño</span></div>
</section>

<section class="v-flow">
 <div class="v-flow-top"><div><span class="v-lab" style="color:var(--cobalto)">02 // Cómo funciona</span><h2 style="margin-top:18px">Caño, núcleo, vaso.</h2></div><a class="v-pill" href="#esquema">Ver el esquema</a></div>
 <div class="v-flow-line">
  <div class="v-node v-rv"><b>01</b><h3>Caño</h3><p>Se instala en tu caño en 5 minutos. Sin obras, sin gasfitero.</p></div>
  <div class="v-node v-rv"><b>02</b><h3>Núcleo</h3><p>Seis etapas de filtración dentro de un solo cartucho.</p></div>
  <div class="v-node v-rv"><b>03</b><h3>Vaso</h3><p>Agua con tendencia alcalina. Conserva sus minerales.</p></div>
 </div>
</section>

<section class="v-story"><div class="v-pin">
 <div class="v-stage"><img src="{{ nativo_img }}" alt="elvo· Nativo en detalle" style="transform:translate(0,-38%) scale(1.9)"><span class="v-tag"><i></i>Nativo</span></div>
 <div class="v-caps">
  <div class="v-count"><i></i><i></i><i></i><i></i></div>
  <div class="v-cap"><span class="v-lab">Instalación</span><span class="v-fig">5<small>min</small></span><h3>Lo instalas tú. Sin gasfitero.</h3></div>
  <div class="v-cap"><span class="v-lab">Filtración</span><span class="v-fig">6<small>etapas</small></span><h3>Carbón, KDF-F, plata y más.</h3></div>
  <div class="v-cap"><span class="v-lab">Agua</span><span class="v-fig">8.5<small>pH</small></span><h3>Tendencia alcalina. Conserva sus minerales.</h3></div>
  <div class="v-cap"><span class="v-lab">Núcleo</span><span class="v-fig">18<small>meses</small></span><h3>Por núcleo. Te avisamos por WhatsApp.</h3></div>
  <p class="v-fine">Descrito para elvo· Nativo. Resultados según la ficha técnica del núcleo PureCore y la calidad del agua de entrada.</p>
 </div>
</div></section>

<section class="v-diag" id="esquema">
 <span class="v-lab">03 // Por dentro</span>
 <div class="v-diag-grid">
  <div>
   <h2>Seis etapas en un solo núcleo.</h2>
   <div class="v-row" style="margin-top:32px"><span class="v-chip" style="color:#fff">Plomo y metales pesados*</span><span class="v-chip" style="color:#fff">Cloro, olores, sabores</span><span class="v-chip" style="color:#fff">pH ~8.5</span></div>
   <p class="v-diag-note">Esquema ilustrativo del núcleo PureCore de elvo· Nativo. *Según la ficha técnica del núcleo y la calidad del agua de entrada. El orden y el espesor de cada etapa son representativos.</p>
  </div>
  <div>''' + svg() + '''</div>
 </div>
</section>

<section class="v-num">
 <span class="v-lab" style="color:var(--cobalto)">04 // Tranquilidad</span>
 <h2 style="margin-top:18px">Compras con calma.</h2>
 <div class="v-num-grid">
  <div class="v-num-i v-rv"><b><span data-to="30">0</span></b><span>días de prueba</span></div>
  <div class="v-num-i v-rv"><b><span data-to="1">0</span></b><span>año de garantía</span></div>
  <div class="v-num-i v-rv"><b><span data-to="6">0</span></b><span>cuotas sin interés</span></div>
  <div class="v-num-i v-rv"><b>Perú</b><span>envío gratis a todo el país</span></div>
 </div>
</section>

<section class="v-h" id="linea"><div class="v-h-pin"><div class="v-h-track">
 <div class="v-h-intro"><div><span class="v-lab" style="color:var(--cobalto)">05 // La línea</span><h2>Un purificador para cada lugar donde el agua te toca.</h2></div><span class="v-h-hint"><i></i>Sigue bajando</span></div>
 <a class="v-p" href="{{ nativo_url }}"><div class="v-p-bg"><img src="{{ nativo_img }}" alt="elvo· Nativo"></div><div class="v-p-info"><div><h3>Nativo</h3><p>Para el caño. Retiene plomo y metales pesados*.</p></div><span class="v-p-go">Ver · desde S/ {{ nativo_price }}</span></div></a>
 <a class="v-p" href="{{ vivo_url }}"><div class="v-p-bg"><img src="{{ vivo_img }}" alt="elvo· Vivo"></div><div class="v-p-info"><div><h3>Vivo</h3><p>Para el caño. Aporta magnesio, sin sabor a cloro.</p></div><span class="v-p-go">Consultar</span></div></a>
 <a class="v-p v-p--cob" href="{{ alivio_url }}"><span class="v-dome"></span><span class="v-p-big">16 · 22<small style="font-size:.2em;letter-spacing:0;font-weight:400"> L</small></span><div class="v-p-info"><div><h3>Alivio</h3><p>Se llena con una jarra. Sin electricidad, sin conexión al caño.</p></div><span class="v-p-go">Consultar</span></div></a>
 <a class="v-p v-p--mar" href="{{ cero_url }}"><span class="v-p-big">Cero</span><div class="v-p-info"><div><h3>Cero</h3><p>Ósmosis inversa. Agua fría y caliente.</p></div><span class="v-p-go">Consultar</span></div></a>
</div><div class="v-prog"><i></i></div></div></section>

<section class="v-end">
 <span class="v-dome"></span>
 <span class="v-lab">06 // Hablemos</span>
 <h2 class="v-rv" style="margin-top:22px">Escríbenos y te acompañamos.</h2>
 <div class="v-row v-rv"><a class="v-pill v-pill--wh" href="''' + wa('Hola,%20quiero%20elegir%20mi%20purificador%20elvo%C2%B7') + '''">Hablar por WhatsApp</a><a class="v-pill v-pill--wh" href="#linea">Ver la línea</a></div>
 <div class="v-faq">
  <details><summary>¿Se adapta a mi caño?</summary><p>Incluye adaptador universal de jebe y derivador. Mándanos una foto por WhatsApp y te confirmamos antes de comprar.</p></details>
  <details><summary>¿Cuándo llega?</summary><p>En Lima, el mismo día si confirmas antes de las 4 p. m. (lunes a sábado). En provincias, en 2 días.</p></details>
  <details><summary>¿Y si no me convence?</summary><p>Tienes 30 días de prueba. Escríbenos por WhatsApp y te devolvemos tu dinero.</p></details>
 </div>
 <p class="v-legal">*Según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada. elvo· no es un dispositivo médico. Inversiones Gad SAC.</p>
</section>
<script>''' + JS + '''</script>
</div>'''

DBG = r'''
var dm=location.hash.match(/only=(\w+)&p=([\d.]+)/);var DBG=dm?{only:dm[1],p:+dm[2]}:null;
if(DBG){var map={hero:'.v-hero',flow:'.v-flow',story:'.v-story',diag:'.v-diag',num:'.v-num',h:'.v-h',end:'.v-end'};Object.keys(map).forEach(function(k){if(k!==DBG.only){var e=root.querySelector(map[k]);if(e)e.style.display='none'}});root.querySelectorAll('.v-rv').forEach(function(e){e.classList.add('on')});}
'''

def preview(h):
    h = re.sub(r'\[\[L\]\].*?\[\[/L\]\]', '', h, flags=re.S)
    h = h.replace('function frame(){', DBG + 'function frame(){')
    h = h.replace('p=clamp(-r2.top/(r2.height-vh))', 'p=DBG?DBG.p:clamp(-r2.top/(r2.height-vh))').replace('p3=clamp(-r3.top/(r3.height-vh))', 'p3=DBG?DBG.p:clamp(-r3.top/(r3.height-vh))')
    return re.sub(r'\{\{\s*(\w+)\s*\}\}', lambda m: MOCK[m.group(1)], h)

if __name__ == '__main__':
    css = open(f'{D}/v3.css').read()
    page = LIQ_URLS + HTML
    open(f'{D}/preview3.html', 'w').write('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>' + css + '</style></head><body style="margin:0">' + preview(page) + '</body></html>')
    sec = "{{ 'elvo-mineral.css' | asset_url | stylesheet_tag }}\n" + page.replace('[[L]]', '').replace('[[/L]]', '') + '\n{% schema %}{"name":"elvo· Home v3","settings":[],"presets":[{"name":"elvo· Home v3"}]}{% endschema %}'
    open(f'{D}/section3.liquid', 'w').write(sec)
    print('ok', len(sec), len(css))
