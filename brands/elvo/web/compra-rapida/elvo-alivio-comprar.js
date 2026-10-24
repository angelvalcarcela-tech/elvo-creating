(function () {
var cfgEl = document.getElementById('bn-cfg');
var root = document.getElementById('bn');
if (!cfgEl || !root || root.dataset.on) return;
root.dataset.on = '1';
var C = JSON.parse(cfgEl.textContent);
var $ = function (s) { return root.querySelector(s); };
var $$ = function (s) { return [].slice.call(root.querySelectorAll(s)); };
var S = { v: { id: 0, p: 0, t: '' }, zona: 'lima', metodo: '', comp: '', pend: false, leads: 0, hecho: false, abierto: false,
ref: 'ck' + Date.now() + Math.floor(Math.random() * 100000) };
function money(c) { var s = c / 100; return 'S/ ' + (s % 1 ? s.toFixed(2) : s.toFixed(0)); }
function val(n) { var e = $('[name="' + n + '"]'); return e ? e.value.trim() : ''; }
function px(ev, d) { try { if (window.fbq) fbq('track', ev, d || {}); } catch (e) {} }
function wa(msg) { return 'https://wa.me/' + C.wa + '?text=' + encodeURIComponent(msg); }
function telOk() { var d = val('tel').replace(/\D/g, ''); return /^(51)?9\d{8}$/.test(d); }
function mailOk() { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val('correo')); }
function lineas() {
var l = [{ id: S.v.id, cantidad: 1, gratis: false, titulo: S.v.t }];
if (S.v.g && C.gid) l.push({ id: C.gid, cantidad: S.v.g, gratis: true, titulo: C.gt + ' (incluido en el plan)' });
return l;
}
function resumen() { return '1x ' + S.v.t; }
function sel() {
var f = document.querySelector('form[data-pe-form] input[name="id"]:checked') || document.querySelector('form[data-pe-form] input[name="id"]');
var id = String(f ? f.value : C.def), v = C.vs[id] || C.vs[C.def];
S.v = { id: parseInt(id, 10) || parseInt(C.def, 10), p: v.p, t: v.t, g: v.g || 0 };
var t = $('[data-bn-t]'), p = $('[data-bn-p]');
if (t) t.textContent = v.t;
if (p) p.textContent = money(v.p) + ' · envío gratis';
}
function abrir() {
sel();
root.hidden = false; S.abierto = true;
document.documentElement.classList.add('bn-lock');
mostrar(S.hecho ? '3' : '1');
px('InitiateCheckout', { value: S.v.p / 100, currency: 'PEN' });
setTimeout(function () { var f = $('[name="tel"]'); if (f && !f.value) f.focus(); }, 60);
}
function cerrar() { root.hidden = true; S.abierto = false; document.documentElement.classList.remove('bn-lock'); }
function mostrar(n) {
$$('[data-step]').forEach(function (e) { e.hidden = e.getAttribute('data-step') !== n; });
var b = $('.bn__box'); if (b) b.scrollTop = 0;
}
function zona() { var r = $('[name="zona"]:checked'); return r ? r.value : 'lima'; }
function pintarZona() {
S.zona = zona();
$('[data-z-lima]').hidden = S.zona !== 'lima';
$('[data-z-prov]').hidden = S.zona !== 'provincia';
}
$$('[name="zona"]').forEach(function (r) { r.addEventListener('change', pintarZona); });
function opciones() {
var cuota = money(Math.round(S.v.p / 6));
if (S.zona === 'lima') return [
{ v: 'tarjeta', t: 'Tarjeta', s: 'Hasta 6 cuotas sin intereses · ' + cuota + ' al mes', b: 'Recomendado' },
{ v: 'yape', t: 'Yape, Plin o transferencia', s: 'Pagas ahora y adjuntas tu comprobante' },
{ v: 'cod', t: 'Pagar al recibir', s: 'Yape o efectivo al entregar', n: 'Con esta opción no aplican las 6 cuotas sin intereses.' }
];
return [
{ v: 'tarjeta', t: 'Envío a domicilio · Tarjeta', s: 'Hasta 6 cuotas sin intereses · ' + cuota + ' al mes', b: 'Recomendado' },
{ v: 'yape', t: 'Envío a domicilio · Yape, Plin o transferencia', s: 'Pago completo ahora' },
{ v: 'shalom', t: 'Recojo en Shalom · adelanto de ' + money(C.adelanto), s: 'El saldo (' + money(S.v.p - C.adelanto) + ') lo pagas al recoger',
n: 'No aplican las cuotas sin intereses. El envío a domicilio es solo con pago completo por la web.' }
];
}
function pintarOpciones() {
var cont = $('[data-opts]'); cont.innerHTML = '';
var os = opciones();
if (!os.some(function (o) { return o.v === S.metodo; })) S.metodo = os[0].v;
os.forEach(function (o) {
var l = document.createElement('label'); l.className = 'bn__op';
var i = document.createElement('input'); i.type = 'radio'; i.name = 'metodo'; i.value = o.v; i.checked = o.v === S.metodo;
i.addEventListener('change', function () { S.metodo = o.v; pintarPago(); px('AddPaymentInfo'); });
var d = document.createElement('span'); d.className = 'bn__dot';
var tx = document.createElement('span'); tx.className = 'bn__tx';
var b = document.createElement('b'); b.textContent = o.t;
var sm = document.createElement('small'); sm.textContent = o.s;
tx.appendChild(b); tx.appendChild(sm);
l.appendChild(i); l.appendChild(d); l.appendChild(tx);
if (o.b) { var tg = document.createElement('em'); tg.textContent = o.b; l.appendChild(tg); }
cont.appendChild(l);
});
pintarPago();
}
function pintarPago() {
var m = S.metodo, os = opciones(), act = os.filter(function (o) { return o.v === m; })[0] || {};
var nota = $('[data-nota]'); nota.textContent = act.n || ''; nota.hidden = !act.n;
var pagaYape = m === 'yape' || m === 'shalom';
$('[data-yape]').hidden = !pagaYape;
$('[data-yape-monto]').textContent = money(m === 'shalom' ? C.adelanto : S.v.p);
$('[data-f-dir]').hidden = !(S.zona === 'provincia' && (m === 'tarjeta' || m === 'yape'));
$('[data-f-ag]').hidden = m !== 'shalom';
$('[data-total]').textContent = m === 'shalom' ? 'Hoy pagas ' + money(C.adelanto) + ' · saldo ' + money(S.v.p - C.adelanto) + ' al recoger'
: m === 'cod' ? 'Total ' + money(S.v.p) + ' · pagas al recibir' : 'Total ' + money(S.v.p) + ' · envío gratis';
$('[data-confirmar]').textContent = m === 'tarjeta' ? 'Ir a pagar con tarjeta' : 'Confirmar pedido';
err('');
}
var inComp = $('[data-comp]');
if (inComp) inComp.addEventListener('change', function () {
var f = inComp.files && inComp.files[0]; S.comp = ''; pintarComp(); if (!f) return;
var lector = new FileReader();
lector.onload = function () {
var img = new Image();
img.onload = function () {
try {
var c = document.createElement('canvas'), esc = Math.min(1, 1280 / Math.max(img.width, img.height));
c.width = Math.max(1, Math.round(img.width * esc)); c.height = Math.max(1, Math.round(img.height * esc));
c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
S.comp = c.toDataURL('image/jpeg', 0.72);
} catch (e) { S.comp = String(lector.result); }
if (S.comp.length > 4500000) { S.comp = ''; err('La imagen pesa demasiado, prueba con otra captura.'); return; }
S.pend = false; pintarComp(); err('');
};
img.onerror = function () { err('No pudimos leer la imagen, prueba con otra.'); };
img.src = String(lector.result);
};
lector.readAsDataURL(f);
});
function pintarComp() {
var ok = $('[data-comp-ok]'); ok.hidden = !S.comp;
var pe = $('[data-pend-ok]'); pe.hidden = !S.pend;
}
$('[data-pend]').addEventListener('click', function () { S.pend = true; S.comp = ''; if (inComp) inComp.value = ''; pintarComp(); err(''); });
$$('[data-copiar]').forEach(function (b) {
b.addEventListener('click', function () {
var t = (b.getAttribute('data-v') || C.yape).replace(/\s+/g, '');
var listo = function () { b.textContent = 'Copiado'; setTimeout(function () { b.textContent = 'Copiar'; }, 1600); };
if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(listo).catch(function () {});
else listo();
});
});
function err(m) { var e = $('[data-err]'); e.textContent = m || ''; e.hidden = !m; }
function marcar(n, m) {
var e = $('[name="' + n + '"]'); if (e) { e.classList.add('bn__bad'); e.focus(); }
err(m);
}
$$('.bn__in').forEach(function (e) { e.addEventListener('input', function () { e.classList.remove('bn__bad'); }); });
function validar1() {
$$('.bn__bad').forEach(function (e) { e.classList.remove('bn__bad'); });
if (!telOk()) return marcar('tel', 'Escribe tu número de celular (9 dígitos).'), false;
if (val('nombre').split(/\s+/).filter(Boolean).length < 2) return marcar('nombre', 'Escribe tu nombre y apellido.'), false;
if (!mailOk()) return marcar('correo', 'Escribe un correo válido.'), false;
if (!/^\d{8}$/.test(val('dni').replace(/\D/g, ''))) return marcar('dni', 'Escribe tu DNI (8 dígitos).'), false;
if (S.zona === 'lima') {
if (val('distrito').length < 3) return marcar('distrito', 'Escribe tu distrito.'), false;
if (val('direccion').length < 5) return marcar('direccion', 'Escribe tu dirección.'), false;
} else if (val('ciudad').length < 3) return marcar('ciudad', 'Escribe tu departamento y ciudad.'), false;
err(''); return true;
}
$('[data-sig]').addEventListener('click', function () {
pintarZona(); if (!validar1()) return;
enviarLead(true); pintarOpciones(); mostrar('2');
});
$('[data-atras]').addEventListener('click', function () { mostrar('1'); });
$$('[data-cerrar]').forEach(function (b) { b.addEventListener('click', cerrar); });
document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && S.abierto) cerrar(); });
function enviarLead(f) {
if (!C.backend || !telOk() || S.hecho) return;
S.leads++;
var d = { secreto: C.secreto, tipo: 'lead', ref: S.ref, nombre: val('nombre'), whatsapp: val('tel'),
correo: mailOk() ? val('correo') : '', acepta_correos: false, zona: S.zona, metodo: S.metodo,
resumen: resumen(), total: S.v.p, pagina: location.pathname + location.search };
try { fetch(C.backend, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: 'lead=' + encodeURIComponent(JSON.stringify(d)) }); } catch (e) {}
}
$('[name="tel"]').addEventListener('blur', function () { if (!S.leads) enviarLead(false); });
function direccionFinal() {
if (S.metodo === 'shalom') return 'RECOJO EN SHALOM: ' + val('agencia') + ' (' + val('ciudad') + ')';
return dirDomicilio();
}
function validar2() {
var m = S.metodo;
if (m === 'shalom' && val('agencia').length < 3) return marcar('agencia', 'Escribe la agencia Shalom donde recogerás.'), false;
if (S.zona === 'provincia' && (m === 'tarjeta' || m === 'yape') && val('direccion-p').length < 5) return marcar('direccion-p', 'Escribe tu dirección de entrega.'), false;
if ((m === 'yape' || m === 'shalom') && !S.comp && !S.pend) { err('Adjunta tu comprobante o elige "Lo envío por WhatsApp".'); return false; }
err(''); return true;
}
function dirDomicilio() { return S.zona === 'provincia' ? val('direccion-p') : val('direccion'); }
var btn = $('[data-confirmar]');
btn.addEventListener('click', function () {
if (!validar2()) return;
var txt = btn.textContent; btn.disabled = true;
var falla = function () {
btn.disabled = false; btn.textContent = txt;
var e = $('[data-err]');
e.innerHTML = 'No pudimos registrar tu pedido. <a target="_blank" rel="noopener" href="' + wa('Hola, quiero pedir ' + resumen() + ' (' + money(S.v.p) + '). Soy ' + val('nombre') + ', ' + val('tel') + '.') + '">Envíalo por WhatsApp</a> y lo confirmamos al instante.';
e.hidden = false;
};
var partes = val('nombre').split(/\s+/), nombre1 = partes.shift(), apell = partes.join(' ') || '.';
var ciudad = S.zona === 'lima' ? val('distrito') : val('ciudad');
if (S.metodo === 'tarjeta') {
btn.textContent = 'Abriendo el pago…';
var attrs = { 'Pago': 'Tarjeta (compra rápida)', 'WhatsApp': val('tel'), 'DNI': val('dni'), 'Zona': S.zona === 'lima' ? 'Lima' : 'Provincia', 'Referencia': val('referencia') || '—', 'Regalos incluidos': S.v.g && C.gid ? S.v.g + 'x ' + C.gt : '—' };
fetch('/cart/clear.js', { method: 'POST' })
.then(function () { return fetch('/cart/add.js', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ items: [{ id: S.v.id, quantity: 1 }] }) }); })
.then(function () { return fetch('/cart/update.js', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ note: 'Compra rápida: pago con tarjeta', attributes: attrs }) }); })
.then(function () {
location.href = '/checkout?checkout[email]=' + encodeURIComponent(val('correo')) +
'&checkout[shipping_address][first_name]=' + encodeURIComponent(nombre1 || '') +
'&checkout[shipping_address][last_name]=' + encodeURIComponent(apell) +
'&checkout[shipping_address][address1]=' + encodeURIComponent(dirDomicilio()) +
'&checkout[shipping_address][city]=' + encodeURIComponent(ciudad) +
'&checkout[shipping_address][phone]=' + encodeURIComponent(val('tel'));
})
.catch(falla);
return;
}
btn.textContent = 'Registrando pedido…';
var m = S.metodo, adel = m === 'shalom', pendiente = S.pend && !S.comp, pago, nota, tags;
if (m === 'cod') { pago = 'Contraentrega (Yape o efectivo al recibir)'; nota = 'Compra rápida — CONTRAENTREGA LIMA: cobrar al entregar (Yape o efectivo).'; tags = ['COD', 'Contraentrega', 'compra-rapida']; }
else if (adel) { pago = 'Contraentrega PROVINCIA — adelanto ' + money(C.adelanto) + '; saldo ' + money(S.v.p - C.adelanto) + ' al recoger en Shalom'; nota = 'Compra rápida — SHALOM: adelanto de ' + money(C.adelanto) + ' (Yape, Plin o transferencia). Enviar la guía por WhatsApp y cobrar el saldo al recoger.'; tags = ['COD', 'Contraentrega', 'Provincia', 'compra-rapida']; }
else { pago = pendiente ? 'Yape/Plin/transferencia por web — comprobante PENDIENTE (lo envía por WhatsApp)' : 'Yape/Plin/transferencia por web — comprobante adjunto'; nota = 'Compra rápida — pago web: validar el comprobante y confirmar el despacho por WhatsApp.'; tags = ['COD', 'Yape web', 'compra-rapida']; }
if (pendiente && m !== 'cod') { nota += ' COMPROBANTE PENDIENTE: el cliente lo enviará por WhatsApp. Validar el pago antes de despachar.'; tags.push('comprobante-pendiente'); }
var payload = {
secreto: C.secreto, modo: m === 'cod' || adel ? 'contraentrega' : 'yape', pago: pago, nota: nota, tags: tags,
adelanto: adel ? C.adelanto : 0,
cliente: { nombre: val('nombre'), whatsapp: val('tel'), correo: val('correo'), dni: val('dni'), zona: S.zona,
ruc: '', razon: '', direccion: direccionFinal(), distrito: ciudad,
referencia: val('referencia'), aviso_nucleo: false, acepta_correos: false },
lineas: lineas(),
descuento: 0, descuentoTitulo: '', total: S.v.p, ref: S.ref, comprobante: S.comp || ''
};
if (!C.backend) { falla(); return; }
var listo = false, malo = false;
var alRecibir = function (ev) {
var d = null; try { d = JSON.parse(ev.data); } catch (x) { return; }
if (!d || d.fuente !== 'elvo-backend') return;
var r = d.resultado || {};
if (r.ok) { listo = true; ok(r.pedido || ''); } else if (!listo) { malo = true; falla(); }
};
window.addEventListener('message', alRecibir);
var f = $('[data-envio]');
f.action = C.backend; f.querySelector('[name="pedido"]').value = JSON.stringify(payload); f.submit();
if (S.comp) btn.textContent = 'Subiendo comprobante…';
setTimeout(function () { if (!listo && !malo) { listo = true; ok(''); } }, S.comp ? 18000 : 4000);
setTimeout(function () { window.removeEventListener('message', alRecibir); }, 45000);
});
function ok(pedido) {
S.hecho = true;
var m = S.metodo, pendiente = S.pend && !S.comp && m !== 'cod', num = pedido ? ' Tu pedido es el ' + pedido + '.' : '';
var msg = m === 'cod' ? 'Registramos tu pedido.' + num + ' Te escribimos por WhatsApp para confirmar tu entrega.'
: m === 'shalom' ? 'Registramos tu pedido y tu adelanto.' + num + ' Te enviamos la guía de Shalom por WhatsApp.'
: 'Recibimos tu pedido.' + num + ' Validamos tu pago y te confirmamos por WhatsApp.';
if (pendiente) msg = 'Registramos tu pedido.' + num + ' Envíanos tu comprobante por WhatsApp para validar tu pago.';
$('[data-ok-msg]').textContent = msg;
var b = $('[data-ok-wa]');
b.href = wa(pendiente ? 'Hola, te envío el comprobante de mi pedido de ' + resumen() + (pedido ? ' (' + pedido + ')' : '') + '. Soy ' + val('nombre') + '.'
: 'Hola, hice mi pedido de ' + resumen() + (pedido ? ' (' + pedido + ')' : '') + '. Soy ' + val('nombre') + '.');
b.textContent = pendiente ? 'Enviar comprobante por WhatsApp' : 'Escribirnos por WhatsApp';
mostrar('3');
px('Purchase', { value: (m === 'shalom' ? C.adelanto : S.v.p) / 100, currency: 'PEN', content_name: resumen() });
}
var form = document.querySelector('form[data-pe-form]'), add = document.querySelector('[data-pe-add]');
if (form && add && !add.disabled && !form.querySelector('.bn-open')) {
var nb = document.createElement('button');
nb.type = 'button'; nb.className = 'pe__add bn-open'; nb.textContent = 'Comprar ahora';
add.parentNode.insertBefore(nb, add); form.classList.add('bn-on');
nb.addEventListener('click', abrir);
}
var barBtn = document.querySelector('[data-ab-bar-add]');
if (barBtn) {
var nbb = barBtn.cloneNode(true); nbb.textContent = 'Comprar ahora';
barBtn.parentNode.replaceChild(nbb, barBtn); nbb.addEventListener('click', abrir);
}
pintarZona();
})();
