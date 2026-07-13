# -*- coding: utf-8 -*-
"""Generador estático de genigualdad.com — ejecutar: python3 build.py"""
import os, json

BASE = "https://www.genigualdad.com"
WA_NUM = "5491162296664"
WA_TEXT = "Hola,%20quiero%20hacer%20una%20consulta%20sobre%20los%20servicios%20de%20Gen%2B%20Igualdad"
WA_LINK = f"https://wa.me/{WA_NUM}?text={WA_TEXT}"
EMAIL = "contacto@genigualdad.com"
TODAY = "2026-07-05"
# Pegar aquí el link de Google Calendar (Espacios de citas) o Calendly cuando exista:
SCHEDULING_LINK = "https://calendar.google.com/calendar/appointments/schedules/AcZssZ236k6_EAuIPUEOZDl-iHwgndZxlDXi5A7C8zSNXzaSD8qEP-YTR8gVNbv-lYl4PysgAy9ep-da"

# ---------- SVG icons (reemplazan Font Awesome) ----------
def svg(path_d, vb="0 0 24 24", cls="icon", stroke=True):
    if stroke:
        return f'<svg class="{cls}" viewBox="{vb}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path_d}</svg>'
    return f'<svg class="{cls}" viewBox="{vb}" fill="currentColor" aria-hidden="true">{path_d}</svg>'

IC = {
 "check":   svg('<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>'),
 "ear":     svg('<path d="M6 8.5a6.5 6.5 0 1 1 13 0c0 6-6 6-6 10a3.5 3.5 0 1 1-7 0"/><path d="M15 8.5a2.5 2.5 0 0 0-5 0v1a2 2 0 1 1 0 4"/>'),
 "chat":    svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
 "scale":   svg('<path d="M12 3v18"/><path d="M5 7l7-4 7 4"/><path d="M5 7l-3 7a4 4 0 0 0 6 0z"/><path d="M19 7l-3 7a4 4 0 0 0 6 0z"/><path d="M8 21h8"/>'),
 "shield":  svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'),
 "doc":     svg('<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>'),
 "chart":   svg('<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="2" y1="20" x2="22" y2="20"/>'),
 "grad":    svg('<path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/>'),
 "arrow":   svg('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>'),
 "download":svg('<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/>'),
 "wa":      svg('<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>', stroke=False),
 "menu":    svg('<line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>'),
 "close":   svg('<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>'),
 "pin":     svg('<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>'),
}

# ---------- imagen helper ----------
DIMS = json.load(open("/home/claude/img_dims.json"))
def img(name, alt, cls="", lazy=True, w=None, h=None):
    if name in DIMS and not w:
        w, h = DIMS[name]
    lz = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="/img/{name}.webp" alt="{alt}" width="{w}" height="{h}"{lz}{c}>'

# ---------- head ----------
def head(title, desc, path, extra_schema=None, hreflang=False, og_type="website", article_meta=""):
    canonical = BASE + path
    hl = ""
    if hreflang:
        hl = (f'<link rel="alternate" hreflang="es" href="{BASE}/">'
              f'<link rel="alternate" hreflang="es-ES" href="{BASE}/espana">'
              f'<link rel="alternate" hreflang="es-AR" href="{BASE}/argentina">'
              f'<link rel="alternate" hreflang="x-default" href="{BASE}/">')
    schemas = [{
        "@context":"https://schema.org","@type":"ProfessionalService","name":"GEN+ Igualdad",
        "url":BASE+"/", "logo":BASE+"/img/logo-principal.png", "image":BASE+"/img/og-genigualdad.jpg",
        "description":"Consultora especializada en violencia laboral, protocolos y planes de igualdad, y capacitación en género, diversidad e inclusión.",
        "email":EMAIL, "priceRange":"$$",
        "telephone":"+54 911 6229-6664",
        "areaServed":["Argentina","España"],
        "knowsAbout":["Violencia laboral","Protocolos de igualdad","Planes de igualdad","Capacitación en género","Diagnósticos organizacionales"],
        "address":[{"@type":"PostalAddress","addressLocality":"Ciudad Autónoma de Buenos Aires","addressCountry":"AR"},
                   {"@type":"PostalAddress","addressLocality":"Santiago de Compostela","addressRegion":"Galicia","addressCountry":"ES"}],
        "contactPoint":[{"@type":"ContactPoint","telephone":"+54-911-6229-6664","contactType":"customer service","areaServed":"AR","availableLanguage":["es"]},
                        {"@type":"ContactPoint","telephone":"+34-698-187-971","contactType":"customer service","areaServed":"ES","availableLanguage":["es","gl"]}]
    }]
    if extra_schema: schemas += extra_schema if isinstance(extra_schema, list) else [extra_schema]
    schema_tags = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google-site-verification" content="WGXqAflx3Op0Gn0R4FGOpBj21JjqxkNKiVKc76tDUeo">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">{hl}
  <link rel="icon" type="image/png" href="/img/favicon.png">
  <link rel="preconnect" href="https://www.googletagmanager.com">
  <link rel="preload" as="image" href="/img/logo-horizontal.png">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="GEN+ Igualdad">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/img/og-genigualdad.jpg">
  <meta property="og:locale" content="es_ES">
  <meta property="og:locale:alternate" content="es_AR">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{BASE}/img/og-genigualdad.jpg">
  {article_meta}{schema_tags}
  <link rel="stylesheet" href="/styles.css">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-FSFH021Y0F"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-FSFH021Y0F');</script>
</head>
<body>
<a class="skip-link" href="#contenido">Saltar al contenido</a>"""

NAV_LINKS = [("/argentina","Argentina"),("/espana","España"),("/#servicios","Servicios"),("/equipo","Equipo"),("/recursos","Recursos"),("/contacto","Contacto")]

def header():
    links = "".join(f'<a href="{h}">{t}</a>' for h,t in NAV_LINKS)
    return f"""
<header class="site-header">
  <a class="brand" href="/" aria-label="GEN+ Igualdad — inicio"><img src="/img/logo-horizontal.png" alt="GEN+ Igualdad" width="1049" height="167"></a>
  <div class="nav-wrap">
    <nav class="nav" aria-label="Navegación principal">{links}</nav>
    <a class="nav-cta" href="/contacto">Agendar consulta</a>
  </div>
  <button class="menu-button" type="button" aria-label="Abrir menú">{IC["menu"]}</button>
</header>
<div class="mobile-menu">
  <button class="close-menu" type="button" aria-label="Cerrar menú">{IC["close"]}</button>
  {links}
  <a class="button primary nav-cta" href="/contacto">Agendar consulta</a>
</div>"""

def wa_float():
    return f'<a class="wa-float" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp" data-ga="contact_whatsapp">{IC["wa"]}</a>'

def footer():
    return f"""
<footer>
  <div class="footer-grid">
    <div class="footer-brand">
      <div class="logo-chip"><img src="/img/logo-secundario.webp" alt="GEN+ igualdad" width="176" height="120" loading="lazy"></div>
      <p>Consultora en género, diversidad e inclusión. Formación, investigación y asesoramiento en Argentina y España.</p>
    </div>
    <div>
      <h4>Servicios</h4>
      <ul><li><a href="/servicios/protocolos-de-igualdad">Protocolos de igualdad</a></li><li><a href="/servicios/capacitaciones">Capacitaciones</a></li><li><a href="/servicios/diagnosticos-y-planes">Diagnósticos y planes</a></li><li><a href="/servicios/asesoria-juridica">Asesoría jurídica</a></li><li><a href="/servicios/investigacion">Investigación social</a></li></ul>
    </div>
    <div>
      <h4>Mercados</h4>
      <ul><li><a href="/argentina">Organizaciones en Argentina</a></li><li><a href="/espana">Empresas en España</a></li><li><a href="/equipo">Nuestro equipo</a></li><li><a href="/recursos">Recursos</a></li></ul>
    </div>
    <div>
      <h4>Contacto</h4>
      <ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="tel:+5491162296664">+54 911 6229-6664</a></li><li><a href="tel:+34698187971">+34 698 187 971</a></li><li><a class="button primary" href="/contacto" style="margin-top:8px">Agendar consulta</a></li></ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 GEN+ Igualdad · Consultora en Género</span>
    <span>Buenos Aires, Argentina · Santiago de Compostela, España</span>
  </div>
</footer>"""

SHARED_JS = """<script>
(function(){
var mb=document.querySelector('.menu-button'),cm=document.querySelector('.close-menu'),mm=document.querySelector('.mobile-menu');
if(mb){mb.addEventListener('click',function(){mm.classList.add('active')});cm.addEventListener('click',function(){mm.classList.remove('active')});
document.querySelectorAll('.mobile-menu a').forEach(function(l){l.addEventListener('click',function(){mm.classList.remove('active')})});}
document.querySelectorAll('[data-ga]').forEach(function(el){el.addEventListener('click',function(){if(window.gtag)gtag('event',el.getAttribute('data-ga'));})});
var sel='.section-title, .why-grid, .about-copy, .about-image, .team-grid, .pillars, .flagship, .corporate-grid, .timeline, .stats-grid, .impact-columns, .institutions-strip, .gallery, .process-grid, .blog-grid, .contact-form, .contact-copy, .summary-text, .summary-heading, .country-cards, .legal-grid, .faq, .service-cards, .cta-band-inner, .article-body';
var t=document.querySelectorAll(sel);t.forEach(function(e){e.classList.add('reveal')});
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('is-visible');io.unobserve(en.target)}})},{threshold:.12,rootMargin:'0px 0px -60px 0px'});t.forEach(function(e){io.observe(e)});}else{t.forEach(function(e){e.classList.add('is-visible')})}
var f=document.getElementById('contactForm');
if(f){var mc=document.querySelector('.message-container');
f.addEventListener('submit',async function(ev){ev.preventDefault();
if(document.getElementById('empresa_web').value){return;}
var p={nombre:document.getElementById('nombre').value,email:document.getElementById('email').value,telefono:document.getElementById('telefono').value,pais:document.getElementById('pais')?document.getElementById('pais').value:'',mensaje:document.getElementById('mensaje').value};
var btn=f.querySelector('button[type=submit]');btn.disabled=true;btn.textContent='Enviando…';
try{var r=await fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(p)});
if(r.ok){mc.innerHTML='<p class="success">Gracias '+p.nombre+'. Te responderemos a la brevedad.</p>';f.reset();if(window.gtag)gtag('event','generate_lead',{method:'form'});}
else{mc.innerHTML='<p class="error">Hubo un error al enviar el mensaje. Escríbenos por WhatsApp o a ${EMAIL}.</p>'}}
catch(e){mc.innerHTML='<p class="error">Hubo un error al enviar el mensaje. Escríbenos por WhatsApp o a ${EMAIL}.</p>'}
btn.disabled=false;btn.textContent='Enviar consulta';setTimeout(function(){mc.innerHTML=''},8000)});}
})();
</script>""".replace("${EMAIL}", EMAIL)

def page(filename, title, desc, path, body, extra_schema=None, hreflang=False, og_type="website", article_meta=""):
    html = head(title, desc, path, extra_schema, hreflang, og_type, article_meta) + header() + \
        f'\n<main id="contenido">{body}</main>' + wa_float() + footer() + SHARED_JS + "\n</body>\n</html>"
    full = os.path.join("/home/claude/site", filename)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f: f.write(html)
    print("✓", filename, f"{len(html)//1024}KB")

# ---------- componentes reutilizables ----------
def contact_section(country=None):
    """Sección de contacto con formulario (home y contacto)."""
    ar = '<div><h4>Argentina</h4><p>Ciudad Autónoma de Buenos Aires</p><p><a href="tel:+5491162296664">+54 911 6229-6664</a></p><p><a href="tel:+5491160595326">+54 911 6059-5326</a></p></div>'
    es = '<div><h4>España</h4><p>Santiago de Compostela, Galicia</p><p><a href="tel:+34698187971">+34 698 187 971</a></p></div>'
    locs = ar + es
    sched = ""
    if SCHEDULING_LINK:
        sched = f'<p style="margin-top:18px"><a class="button primary" href="{SCHEDULING_LINK}" target="_blank" rel="noopener" data-ga="schedule_click">Elegir día y horario en la agenda</a></p>'
    return f"""
<section class="contact" id="contacto">
  <div class="contact-copy">
    <p class="eyebrow">Contacto</p>
    <h2>Conversemos sobre las necesidades de tu organización</h2>
    <p>Coordinamos una reunión inicial sin costo para analizar el punto de partida y diseñar una propuesta clara, viable y adaptada a tu equipo.</p>
    {sched}
    <p style="margin-top:18px"><a class="button ghost" href="{WA_LINK}" target="_blank" rel="noopener" data-ga="contact_whatsapp">Escríbenos por WhatsApp</a></p>
    <div class="contact-locations">{locs}</div>
    <div class="contact-email"><p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
  </div>
  <form class="contact-form" id="contactForm">
    <div><label for="nombre">Nombre</label><input id="nombre" name="nombre" type="text" placeholder="Tu nombre" autocomplete="name" required></div>
    <div><label for="email">E-mail</label><input id="email" name="email" type="email" placeholder="tu@email.com" autocomplete="email" required></div>
    <div><label for="telefono">Teléfono</label><input id="telefono" name="telefono" type="tel" placeholder="Opcional" autocomplete="tel"></div>
    <div><label for="pais">País</label><select id="pais" name="pais"><option value="">Seleccionar…</option><option{' selected' if country=='es' else ''}>España</option><option{' selected' if country=='ar' else ''}>Argentina</option><option>Otro</option></select></div>
    <div><label for="mensaje">Mensaje</label><textarea id="mensaje" name="mensaje" placeholder="Cuéntanos brevemente qué necesita tu organización" required></textarea></div>
    <div class="hp" aria-hidden="true"><label for="empresa_web">No completar</label><input id="empresa_web" name="empresa_web" type="text" tabindex="-1" autocomplete="off"></div>
    <div class="message-container" role="status" aria-live="polite"></div>
    <button type="submit">Enviar consulta</button>
  </form>
</section>"""

def cta_band(h, p, btn="Agendar consulta", href="/contacto"):
    return f"""
<section class="cta-band"><div class="cta-band-inner">
  <div><h2>{h}</h2><p>{p}</p></div>
  <div class="cta-band-actions"><a class="button primary" href="{href}">{btn}</a><a class="button ghost" href="{WA_LINK}" target="_blank" rel="noopener" data-ga="contact_whatsapp">WhatsApp directo</a></div>
</div></section>"""

def breadcrumb(items):
    # items: [(url, label), ...] último sin url
    lis = []
    schema_items = []
    for i,(u,l) in enumerate(items, 1):
        if u:
            lis.append(f'<a href="{u}">{l}</a>')
            schema_items.append({"@type":"ListItem","position":i,"name":l,"item":BASE+u})
        else:
            lis.append(f'<span aria-current="page">{l}</span>')
            schema_items.append({"@type":"ListItem","position":i,"name":l})
    sch = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":schema_items}
    return f'<nav class="breadcrumb" aria-label="Miga de pan">{" <span>›</span> ".join(lis)}</nav>', sch

def faq_block(qas, title="Preguntas frecuentes"):
    items = "".join(f'<details class="faq-item"><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>' for q,a in qas)
    schema = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qas]}
    html = f'<section class="faq-section"><div class="section-title"><p class="eyebrow">Dudas habituales</p><h2>{title}</h2></div><div class="faq">{items}</div></section>'
    return html, schema

print("Componentes listos.")
