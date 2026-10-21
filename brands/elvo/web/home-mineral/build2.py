#!/usr/bin/env python3
"""Home mineral v2 (scroll narrativo): preview2.html + section2.liquid + payload2.json."""
import re, json, os
from build_home import LIQ_URLS, MOCK, wa
D = os.path.dirname(os.path.abspath(__file__))

JS = r'''
(function(){
var root=document.currentScript.parentNode;
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function clamp(v){return Math.max(0,Math.min(1,v))}
var hero=root.querySelector('.s-hero-img img');
var story=root.querySelector('.s-story'),caps=root.querySelectorAll('.s-cap'),dots=root.querySelectorAll('.s-count i'),simg=root.querySelector('.s-stage img');
var STEPS=[{s:1.9,x:.5,y:.9},{s:2.1,x:.66,y:.34},{s:2.4,x:.27,y:.66},{s:1,x:.5,y:.5}];
var cur=-1;
function setStep(i){if(i===cur)return;cur=i;
 caps.forEach(function(c,k){c.classList.toggle('on',k===i)});
 dots.forEach(function(d,k){d.classList.toggle('on',k<=i)});
 var t=STEPS[i];var lim=(t.s-1)*50,tx=Math.max(-lim,Math.min(lim,-t.s*(t.x-.5)*100)),ty=Math.max(-lim,Math.min(lim,-t.s*(t.y-.5)*100));simg.style.transform='translate('+tx+'%,'+ty+'%) scale('+t.s+')';}
var hs=root.querySelector('.s-h'),track=root.querySelector('.s-h-track'),bar=root.querySelector('.s-prog i');
function frame(){
 var vh=window.innerHeight;
 if(hero&&!reduce){var r=hero.parentNode.getBoundingClientRect();if(r.bottom>0)hero.style.transform='translateY('+(-r.top*.08)+'px)';}
 if(story){var r2=story.getBoundingClientRect(),p=clamp(-r2.top/(r2.height-vh));setStep(Math.min(3,Math.floor(p*4)));}
 if(hs){var r3=hs.getBoundingClientRect(),p3=clamp(-r3.top/(r3.height-vh));
  var max=track.scrollWidth-window.innerWidth;track.style.transform='translateX('+(-p3*max)+'px)';bar.style.width=(p3*100)+'%';}
}
var tick=false;function onS(){if(!tick){tick=true;requestAnimationFrame(function(){tick=false;frame()})}}
window.addEventListener('scroll',onS,{passive:true});window.addEventListener('resize',onS);
var m=location.hash.match(/y=(\d+)/);if(m)window.scrollTo(0,+m[1]);
frame();
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');
 var n=e.target.querySelector('[data-to]');if(n&&!n.dataset.done){n.dataset.done=1;var to=+n.dataset.to,t0=performance.now();(function up(t){var k=clamp((t-t0)/1400),v=Math.round(to*(1-Math.pow(1-k,3)));n.firstChild.nodeValue=v;if(k<1)requestAnimationFrame(up)})(t0)}
 io.unobserve(e.target)}})},{threshold:.25});
root.querySelectorAll('.s-rv').forEach(function(el){io.observe(el)});
})();
'''

HTML = '''
<div class="s">
<section class="s-hero">
 <div class="s-hero-copy">
  <span class="s-eyebrow">elvo· · Purificación doméstica de agua</span>
  <h1>El agua es el primer ingrediente.</h1>
  <div class="s-hero-foot">
   <p>Un purificador para cada lugar donde el agua te toca.</p>
   <div class="s-row"><a class="s-btn s-btn--solid" href="#linea">Ver la línea</a><a class="s-btn" href="''' + wa('Hola,%20quiero%20elegir%20mi%20purificador%20elvo%C2%B7') + '''">Escríbenos</a></div>
   <span class="s-scroll"><i></i>Desliza</span>
  </div>
 </div>
 <div class="s-hero-img"><img src="{{ nativo_img }}" alt="elvo· Nativo, purificador para el caño, con un vaso de agua"><span class="s-hero-tag">elvo· Nativo</span></div>
</section>

<div class="s-marq" aria-label="Disponible en">
 <div class="s-marq-t"><b style="font-family:var(--sans);font-size:12px;letter-spacing:.16em;text-transform:uppercase;font-weight:500;color:var(--piedra-osc);align-self:center">Disponible en</b>elvo.pe <span>·</span> WhatsApp <span>·</span> Falabella <span>·</span> Sodimac <span>·</span> Plaza Vea <span>·</span> Promart <span>·</span> Oechsle <span>·</span> Mercado Libre <span>·</span></div>
 <div class="s-marq-t" aria-hidden="true"><b style="font-family:var(--sans);font-size:12px;letter-spacing:.16em;text-transform:uppercase;font-weight:500;color:var(--piedra-osc);align-self:center">Disponible en</b>elvo.pe <span>·</span> WhatsApp <span>·</span> Falabella <span>·</span> Sodimac <span>·</span> Plaza Vea <span>·</span> Promart <span>·</span> Oechsle <span>·</span> Mercado Libre <span>·</span></div>
</div>

<section class="s-story"><div class="s-pin">
 <div class="s-stage"><img src="{{ nativo_img }}" alt="elvo· Nativo en detalle" style="transform:translate(0,-38%) scale(1.9)"></div>
 <div class="s-caps">
  <div class="s-count"><i></i><i></i><i></i><i></i></div>
  <div class="s-cap"><span class="s-fig">5<small>min</small></span><h3>Lo instalas tú. Sin gasfitero.</h3></div>
  <div class="s-cap"><span class="s-fig">6<small>etapas</small></span><h3>Carbón, KDF-F, plata y más.</h3></div>
  <div class="s-cap"><span class="s-fig">8.5<small>pH</small></span><h3>Tendencia alcalina. Conserva sus minerales.</h3></div>
  <div class="s-cap"><span class="s-fig">18<small>meses</small></span><h3>Por núcleo. Te avisamos por WhatsApp.</h3></div>
  <p class="s-fine">Descrito para elvo· Nativo. Resultados según la ficha técnica del núcleo PureCore y la calidad del agua de entrada.</p>
 </div>
</div></section>

<section class="s-num"><div class="s-num-grid">
 <div class="s-num-i s-rv"><b><span data-to="30">0</span></b><span>días de prueba</span></div>
 <div class="s-num-i s-rv"><b><span data-to="1">0</span></b><span>año de garantía</span></div>
 <div class="s-num-i s-rv"><b><span data-to="6">0</span></b><span>cuotas sin interés</span></div>
 <div class="s-num-i s-rv"><b>Perú</b><span>envío gratis a todo el país</span></div>
</div></section>

<section class="s-h" id="linea"><div class="s-h-pin"><div class="s-h-track">
 <div class="s-h-intro"><div><span class="s-eyebrow">La línea</span><h2>Un purificador para cada lugar donde el agua te toca.</h2></div><span class="s-h-hint"><i></i>Sigue bajando</span></div>
 <a class="s-p" href="{{ nativo_url }}"><div class="s-p-bg"><img src="{{ nativo_img }}" alt="elvo· Nativo"></div><div class="s-p-info"><div><h3>Nativo</h3><p>Para el caño. Retiene plomo y metales pesados*.</p></div><span class="s-p-go">Ver · desde S/ {{ nativo_price }}</span></div></a>
 <a class="s-p" href="{{ vivo_url }}"><div class="s-p-bg"><img src="{{ vivo_img }}" alt="elvo· Vivo"></div><div class="s-p-info"><div><h3>Vivo</h3><p>Para el caño. Aporta magnesio, sin sabor a cloro.</p></div><span class="s-p-go">Consultar</span></div></a>
 <a class="s-p s-p--lime" href="{{ alivio_url }}"><div class="s-p-bg"></div><span class="s-p-big">16 · 22<small style="font-size:.2em;letter-spacing:0"> L</small></span><div class="s-p-info"><div><h3>Alivio</h3><p>Se llena con una jarra. Sin electricidad, sin conexión al caño.</p></div><span class="s-p-go">Consultar</span></div></a>
 <a class="s-p s-p--slate" href="{{ cero_url }}"><div class="s-p-bg"></div><span class="s-p-big">Cero</span><div class="s-p-info"><div><h3>Cero</h3><p>Ósmosis inversa. Agua fría y caliente.</p></div><span class="s-p-go">Consultar</span></div></a>
</div><div class="s-prog"><i></i></div></div></section>

<section class="s-end">
 <h2 class="s-rv">Escríbenos y te acompañamos.</h2>
 <div class="s-row s-rv"><a class="s-btn s-btn--solid" href="''' + wa('Hola,%20quiero%20elegir%20mi%20purificador%20elvo%C2%B7') + '''">Hablar por WhatsApp</a><a class="s-btn" href="#linea">Ver la línea</a></div>
 <div class="s-faq">
  <details><summary>¿Se adapta a mi caño?</summary><p>Incluye adaptador universal de jebe y derivador. Mándanos una foto por WhatsApp y te confirmamos antes de comprar.</p></details>
  <details><summary>¿Cuándo llega?</summary><p>En Lima, el mismo día si confirmas antes de las 4 p. m. (lunes a sábado). En provincias, en 2 días.</p></details>
  <details><summary>¿Y si no me convence?</summary><p>Tienes 30 días de prueba. Escríbenos por WhatsApp y te devolvemos tu dinero.</p></details>
 </div>
 <p style="margin-top:56px;font-size:11px;color:var(--piedra)">*Según la ficha técnica del núcleo PureCore. Los resultados dependen de la calidad del agua de entrada. elvo· no es un dispositivo médico. Inversiones Gad SAC.</p>
</section>
<script>''' + JS + '''</script>
</div>'''

DBG_JS = r'''
var dm=location.hash.match(/only=(\w+)&p=([\d.]+)/);
var DBG=dm?{only:dm[1],p:+dm[2]}:null;
if(DBG){var map={hero:'.s-hero',story:'.s-story',num:'.s-num',h:'.s-h',end:'.s-end'};Object.keys(map).forEach(function(k){if(k!==DBG.only){var e=root.querySelector(map[k]);if(e)e.style.display='none'}});var mq=root.querySelector('.s-marq');if(mq)mq.style.display='none';root.querySelectorAll('.s-rv').forEach(function(e){e.classList.add('on')});}
'''

def preview(h):
    h = h.replace('function frame(){', DBG_JS + 'function frame(){')
    h = h.replace('p=clamp(-r2.top/(r2.height-vh))', 'p=DBG?DBG.p:clamp(-r2.top/(r2.height-vh))').replace('p3=clamp(-r3.top/(r3.height-vh))', 'p3=DBG?DBG.p:clamp(-r3.top/(r3.height-vh))')
    h = re.sub(r'\[\[L\]\].*?\[\[/L\]\]', '', h, flags=re.S)
    return re.sub(r'\{\{\s*(\w+)\s*\}\}', lambda m: MOCK[m.group(1)], h)

if __name__ == '__main__':
    css = open(f'{D}/scroll.css').read()
    page = LIQ_URLS + HTML
    open(f'{D}/preview2.html', 'w').write('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>' + css + '</style></head><body style="margin:0">' + preview(page) + '</body></html>')
    sec = "{{ 'elvo-mineral.css' | asset_url | stylesheet_tag }}\n" + page.replace('[[L]]', '').replace('[[/L]]', '') + '\n{% schema %}{"name":"elvo· Mineral · Home","settings":[],"presets":[{"name":"elvo· Mineral · Home"}]}{% endschema %}'
    open(f'{D}/section2.liquid', 'w').write(sec)
    print('ok', len(sec), len(css))
