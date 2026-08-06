# -*- coding: utf-8 -*-
"""Generador de la version en ingles de genigualdad.com -> /en/
Ejecutar desde la raiz del repo: python3 build_en.py

IMPORTANTE: este script SOLO escribe dentro de /en/. No toca ninguna pagina en
espanol. Las paginas ES se editan a mano (tienen SEO que no esta en los .py).

Publico objetivo: visitantes desde Estados Unidos — casas matrices, legal y HR
corporativo con equipos o filiales en Argentina y Espana.
"""
import os, json

BASE = "https://www.genigualdad.com"
WA_NUM = "5491162296664"
EMAIL = "contacto@genigualdad.com"
SCHEDULING_LINK = "https://calendar.google.com/calendar/appointments/schedules/AcZssZ236k6_EAuIPUEOZDl-iHwgndZxlDXi5A7C8zSNXzaSD8qEP-YTR8gVNbv-lYl4PysgAy9ep-da"
GA_ID = "G-FSFH021Y0F"

# Pares ES <-> EN (fuente unica de verdad para hreflang y el boton de idioma)
PAIRS = [
    ("/",                                 "/en"),
    ("/servicios/protocolos-de-igualdad", "/en/services/equality-protocols"),
    ("/servicios/capacitaciones",         "/en/services/training"),
    ("/servicios/diagnosticos-y-planes",  "/en/services/assessments-and-equality-plans"),
    ("/servicios/asesoria-juridica",      "/en/services/legal-advisory"),
    ("/servicios/investigacion",          "/en/services/social-research"),
    ("/equipo",                           "/en/team"),
    ("/contacto",                         "/en/contact"),
]
EN2ES = {en: es for es, en in PAIRS}


def wa(page_label):
    txt = ("Hello,%20I%27d%20like%20to%20ask%20about%20Gen%2B%20Igualdad%27s%20services."
           "%20I%20came%20from%20the%20page:%20" + page_label.replace(" ", "%20"))
    return f"https://wa.me/{WA_NUM}?text={txt}"


# ---------- SVG icons ----------
def svg(d, cls="icon", stroke=True):
    if stroke:
        return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>')
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{d}</svg>'

ARROW = svg('<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>')
IC = {
    "check":  svg('<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>'),
    "ear":    svg('<path d="M6 8.5a6.5 6.5 0 1 1 13 0c0 6-6 6-6 10a3.5 3.5 0 1 1-7 0"/><path d="M15 8.5a2.5 2.5 0 0 0-5 0v1a2 2 0 1 1 0 4"/>'),
    "chat":   svg('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>'),
    "scale":  svg('<path d="M12 3v18"/><path d="M5 7l7-4 7 4"/><path d="M5 7l-3 7a4 4 0 0 0 6 0z"/><path d="M19 7l-3 7a4 4 0 0 0 6 0z"/><path d="M8 21h8"/>'),
    "shield": svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'),
    "chart":  svg('<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="2" y1="20" x2="22" y2="20"/>'),
    "grad":   svg('<path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/>'),
    "menu":   svg('<line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>'),
    "close":  svg('<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>'),
}
WA_ICON = svg('<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>', stroke=False)


# ---------- head ----------
ORG_SCHEMA = {
    "@context": "https://schema.org", "@type": "ProfessionalService", "name": "GEN+ Igualdad",
    "url": BASE + "/en", "logo": BASE + "/img/logo-principal.png", "image": BASE + "/img/og-genigualdad.jpg",
    "description": "Gender equality consultancy specialising in workplace violence and harassment, equality protocols, equality plans and training for organisations in Argentina and Spain.",
    "email": EMAIL, "priceRange": "$$", "telephone": "+54 911 6229-6664",
    "areaServed": ["Argentina", "Spain"],
    "knowsAbout": ["Workplace violence and harassment", "ILO Convention 190 compliance",
                   "Equality protocols", "Equality plans", "Gender training", "Organisational assessments"],
    "address": [
        {"@type": "PostalAddress", "addressLocality": "Buenos Aires", "addressCountry": "AR"},
        {"@type": "PostalAddress", "addressLocality": "Santiago de Compostela", "addressRegion": "Galicia", "addressCountry": "ES"},
    ],
    "contactPoint": [
        {"@type": "ContactPoint", "telephone": "+54-911-6229-6664", "contactType": "customer service",
         "areaServed": "AR", "availableLanguage": ["en", "es"]},
        {"@type": "ContactPoint", "telephone": "+34-698-187-971", "contactType": "customer service",
         "areaServed": "ES", "availableLanguage": ["en", "es", "gl"]},
    ],
}


def head(title, desc, en_path, extra_schema=None, preload_hero=False):
    es_path = EN2ES[en_path]
    canonical = BASE + en_path
    hl = (f'<link rel="alternate" hreflang="en" href="{BASE}{en_path}">'
          f'<link rel="alternate" hreflang="es" href="{BASE}{es_path}">')
    if en_path == "/en":
        hl += (f'<link rel="alternate" hreflang="es-ES" href="{BASE}/espana">'
               f'<link rel="alternate" hreflang="es-AR" href="{BASE}/argentina">')
    hl += f'<link rel="alternate" hreflang="x-default" href="{BASE}{es_path}">'

    schemas = [ORG_SCHEMA]
    if extra_schema:
        schemas.extend(extra_schema if isinstance(extra_schema, list) else [extra_schema])
    ld = "".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    preload = '<link rel="preload" as="image" href="/img/hero-laura.webp">' if preload_hero else ""

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">{hl}
  <link rel="icon" type="image/png" href="/img/favicon.png">
  <link rel="preconnect" href="https://www.googletagmanager.com">
  <link rel="preload" as="image" href="/img/logo-horizontal.png">{preload}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="GEN+ Igualdad">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/img/og-genigualdad.jpg">
  <meta property="og:locale" content="en_US">
  <meta property="og:locale:alternate" content="es_ES">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{BASE}/img/og-genigualdad.jpg">
  {ld}
  <link rel="stylesheet" href="/styles.css">
  <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA_ID}');</script>
</head>
<body>
'''


# ---------- header / footer ----------
NAV_EN = ('<a href="/en#services">Services</a><a href="/en#markets">Argentina &amp; Spain</a>'
          '<a href="/en/team">Team</a><a href="/en/contact">Contact</a>')


def header(en_path):
    es_path = EN2ES[en_path]
    lang = (f'<a class="lang-switch" href="{es_path}" hreflang="es" lang="es" '
            f'aria-label="Ver esta p&#225;gina en espa&#241;ol" data-ga="lang_switch_es">ES</a>')
    return f'''<a class="skip-link" href="#contenido">Skip to content</a>
<header class="site-header">
  <a class="brand" href="/en" aria-label="GEN+ Igualdad — home"><img src="/img/logo-horizontal.png" alt="GEN+ Igualdad" width="1049" height="167"></a>
  <div class="nav-wrap">
    <nav class="nav" aria-label="Main navigation">{NAV_EN}</nav>
    {lang}
    <a class="nav-cta" href="/en/contact">Book a consultation</a>
  </div>
  <div class="header-mobile">{lang}<button class="menu-button" type="button" aria-label="Open menu">{IC["menu"]}</button></div>
</header>
<div class="mobile-menu">
  <button class="close-menu" type="button" aria-label="Close menu">{IC["close"]}</button>
  {NAV_EN}
  <a class="button primary nav-cta" href="/en/contact">Book a consultation</a>
  <a href="{es_path}" hreflang="es" lang="es">Ver en espa&#241;ol</a>
</div>
'''


def footer(page_label):
    return f'''<a class="wa-float" href="{wa(page_label)}" target="_blank" rel="noopener" aria-label="Message us on WhatsApp" data-ga="contact_whatsapp">{WA_ICON}</a>
<footer>
  <div class="footer-grid">
    <div class="footer-brand">
      <div class="logo-chip"><img src="/img/logo-principal.png" alt="GEN+ Igualdad" width="265" height="180" loading="lazy"></div>
      <p>Gender, diversity and inclusion consultancy. Training, research and advisory services in Argentina and Spain.</p>
    </div>
    <div>
      <h4>Services</h4>
      <ul><li><a href="/en/services/equality-protocols">Equality protocols</a></li><li><a href="/en/services/training">Training</a></li><li><a href="/en/services/assessments-and-equality-plans">Assessments &amp; equality plans</a></li><li><a href="/en/services/legal-advisory">Legal advisory</a></li><li><a href="/en/services/social-research">Social research</a></li></ul>
    </div>
    <div>
      <h4>Company</h4>
      <ul><li><a href="/en/team">Our team</a></li><li><a href="/en#markets">Argentina &amp; Spain</a></li><li><a href="/en/contact">Contact</a></li><li><a href="/" hreflang="es" lang="es">Sitio en espa&#241;ol</a></li></ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="tel:+5491162296664">+54 911 6229-6664</a></li><li><a href="tel:+34698187971">+34 698 187 971</a></li><li><a class="button primary" href="/en/contact" style="margin-top:8px">Book a consultation</a></li></ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>&#169; 2026 GEN+ Igualdad &#183; Gender equality consultancy</span>
    <span>Buenos Aires, Argentina &#183; Santiago de Compostela, Spain</span>
  </div>
</footer>
'''


SCRIPTS = '''<script>
(function(){
var mb=document.querySelector('.menu-button'),cm=document.querySelector('.close-menu'),mm=document.querySelector('.mobile-menu');
if(mb&&mm){mb.addEventListener('click',function(){mm.classList.add('active')});
if(cm)cm.addEventListener('click',function(){mm.classList.remove('active')});
document.querySelectorAll('.mobile-menu a').forEach(function(l){l.addEventListener('click',function(){mm.classList.remove('active')})});}
document.querySelectorAll('[data-ga]').forEach(function(el){el.addEventListener('click',function(){if(window.gtag)gtag('event',el.getAttribute('data-ga'));})});
var sel='.section-title, .why-grid, .about-copy, .about-image, .team-grid, .pillars, .flagship, .timeline, .impact-columns, .institutions-strip, .gallery, .process-grid, .contact-form, .contact-copy, .summary-text, .summary-heading, .country-cards, .faq, .service-cards, .cta-band-inner, .article-body, .bio';
var t=document.querySelectorAll(sel);t.forEach(function(e){e.classList.add('reveal')});
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('is-visible');io.unobserve(en.target)}})},{threshold:.12,rootMargin:'0px 0px -60px 0px'});t.forEach(function(e){io.observe(e)});}else{t.forEach(function(e){e.classList.add('is-visible')})}
var f=document.getElementById('contactForm');
if(f){var mc=document.querySelector('.message-container');
f.addEventListener('submit',async function(ev){ev.preventDefault();
if(document.getElementById('empresa_web').value){return;}
var p={nombre:document.getElementById('nombre').value,email:document.getElementById('email').value,telefono:document.getElementById('telefono').value,pais:document.getElementById('pais')?document.getElementById('pais').value:'',mensaje:document.getElementById('mensaje').value,idioma:'en'};
var btn=f.querySelector('button[type=submit]');btn.disabled=true;btn.textContent='Sending\\u2026';
try{var r=await fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(p)});
if(r.ok){mc.innerHTML='<p class="success">Thank you, '+p.nombre+'. We will get back to you shortly.</p>';f.reset();if(window.gtag)gtag('event','generate_lead',{method:'form'});}
else{mc.innerHTML='<p class="error">Something went wrong. Please email us at contacto@genigualdad.com or message us on WhatsApp.</p>'}}
catch(e){mc.innerHTML='<p class="error">Something went wrong. Please email us at contacto@genigualdad.com or message us on WhatsApp.</p>'}
btn.disabled=false;btn.textContent='Send enquiry';setTimeout(function(){mc.innerHTML=''},8000)});}
})();
</script>
</body>
</html>
'''


def contact_block(page_label, heading, intro):
    return f'''<section class="contact" id="contact">
  <div class="contact-copy">
    <p class="eyebrow">Contact</p>
    <h2>{heading}</h2>
    <p>{intro}</p>
    <p style="margin-top:18px"><a class="button primary" href="{SCHEDULING_LINK}" target="_blank" rel="noopener" data-ga="schedule_click">Pick a time on our calendar</a></p>
    <p style="margin-top:18px"><a class="button ghost" href="{wa(page_label)}" target="_blank" rel="noopener" data-ga="contact_whatsapp">Message us on WhatsApp</a></p>
    <div class="contact-locations"><div><h4>Argentina</h4><p>Buenos Aires</p><p><a href="tel:+5491162296664">+54 911 6229-6664</a></p><p><a href="tel:+5491160595326">+54 911 6059-5326</a></p></div><div><h4>Spain</h4><p>Santiago de Compostela, Galicia</p><p><a href="tel:+34698187971">+34 698 187 971</a></p></div></div>
    <div class="contact-email"><p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
    <p style="margin-top:14px;font-size:.92rem">We work across US, Argentina and Spain time zones, and report in English.</p>
  </div>
  <form class="contact-form" id="contactForm">
    <div><label for="nombre">Name</label><input id="nombre" name="nombre" type="text" placeholder="Your name" autocomplete="name" required></div>
    <div><label for="email">Email</label><input id="email" name="email" type="email" placeholder="you@company.com" autocomplete="email" required></div>
    <div><label for="telefono">Phone</label><input id="telefono" name="telefono" type="tel" placeholder="Optional" autocomplete="tel"></div>
    <div><label for="pais">Where are your teams?</label><select id="pais" name="pais"><option value="">Select&#8230;</option><option>Argentina</option><option>Spain</option><option>Argentina and Spain</option><option>Other</option></select></div>
    <div><label for="mensaje">Message</label><textarea id="mensaje" name="mensaje" placeholder="Tell us briefly what your organisation needs" required></textarea></div>
    <div class="hp" aria-hidden="true"><label for="empresa_web">Do not fill</label><input id="empresa_web" name="empresa_web" type="text" tabindex="-1" autocomplete="off"></div>
    <div class="message-container" role="status" aria-live="polite"></div>
    <button type="submit">Send enquiry</button>
  </form>
</section>'''


def cta_band(page_label, heading, sub):
    return f'''<section class="cta-band"><div class="cta-band-inner">
  <div><h2>{heading}</h2><p>{sub}</p></div>
  <div class="cta-band-actions"><a class="button primary" href="/en/contact">Book a consultation</a><a class="button ghost" href="{wa(page_label)}" target="_blank" rel="noopener" data-ga="contact_whatsapp">WhatsApp</a></div>
</div></section>'''


def write(path_rel, html):
    full = os.path.join("en", path_rel)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("  wrote en/" + path_rel)


# =====================================================================
# HOME  /en
# =====================================================================
HOME_FAQ = {
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": "Does our US anti-harassment policy comply in Argentina or Spain?",
         "acceptedAnswer": {"@type": "Answer", "text": "Almost never on its own. A US EEO or anti-harassment policy is a good starting point, but neither country accepts it as evidence of compliance. Argentina and Spain each require a locally drafted procedure, in Spanish, with specific reporting channels, timelines and safeguards defined by their own law. A translation of the US policy is not enough."}},
        {"@type": "Question", "name": "What does Spain require from a company with more than 50 employees?",
         "acceptedAnswer": {"@type": "Answer", "text": "A negotiated and officially registered equality plan, a harassment protocol, a pay register and, where pay gaps exceed the legal threshold, a pay audit. Spanish law also requires agreed LGBTI measures. These are negotiated with worker representatives, not issued unilaterally by management."}},
        {"@type": "Question", "name": "What is ILO Convention 190 and does it apply to us?",
         "acceptedAnswer": {"@type": "Answer", "text": "ILO Convention 190 is the first international treaty on violence and harassment in the world of work. Argentina and Spain have both ratified it — it entered into force in Argentina in February 2022 and in Spain in May 2023 — which means its standards flow into national obligations for employers operating there, including your local subsidiary."}},
        {"@type": "Question", "name": "Do you work in English?",
         "acceptedAnswer": {"@type": "Answer", "text": "Yes. We report, present and correspond in English with headquarters, while the deliverables that must be legally valid locally are produced in Spanish. Training is delivered in Spanish, which is what local teams need for it to work."}},
    ],
}


def build_home():
    p = "/en"
    label = "Home"
    h = head(
        "Gender Equality Compliance in Argentina &amp; Spain | GEN+ Igualdad",
        "US companies with teams in Argentina or Spain: harassment protocols, equality plans, pay audits and training that meet local law. 25+ years in official statistics, academia and legal practice.",
        p, extra_schema=HOME_FAQ, preload_hero=True)
    h += header(p)
    h += f'''<main id="contenido">
<section class="hero" id="top">
  <div class="hero-copy">
    <p class="eyebrow">Gender equality consultancy &#183; Argentina &amp; Spain</p>
    <h1>Equality compliance for your teams in Argentina and Spain</h1>
    <p class="lead">If your company employs people in Argentina or Spain, the anti-harassment and EEO policies drafted at head office don't carry over. Both countries require their own protocols, their own reporting channels and, in Spain, a negotiated and officially registered equality plan. We build them, train the local teams who will use them, and report back to headquarters in English.</p>
    <div class="hero-actions"><a class="button primary" href="/en/contact">Book a consultation</a><a class="button ghost" href="{wa(label)}" target="_blank" rel="noopener" data-ga="contact_whatsapp">Message us on WhatsApp</a></div>
    <div class="trust-strip"><span>INDEC</span><span>FLACSO</span><span>UNTREF</span><span>UN Women</span><span>RUCVM</span><span>USC Galicia</span></div>
  </div>
  <figure class="hero-image">
    <img src="/img/hero-laura.webp" alt="Laura Rodr&#237;guez of the GEN+ Igualdad team delivering a session on the history of gender policy" width="1200" height="800" fetchpriority="high">
    <figcaption>Fair workplaces don't happen by accident. They are designed.</figcaption>
  </figure>
</section>

<section class="country-band" id="markets">
  <div class="section-title"><p class="eyebrow">Two jurisdictions, two rulebooks</p><h2>What each country actually requires</h2></div>
  <div class="country-cards">
    <a class="country-card" href="/en/services/equality-protocols">
      <p class="eyebrow">Argentina</p>
      <h3>Prevent workplace violence and harassment</h3>
      <p>Argentina has ratified ILO Convention 190, and its labour framework has been reshaped by recent reform. Employers need a working protocol, a safe reporting channel and HR staff trained to run a complaint intake interview properly &#8212; not a translated head-office document.</p>
      <span class="card-link">See how we build it {ARROW}</span>
    </a>
    <a class="country-card" href="/en/services/assessments-and-equality-plans">
      <p class="eyebrow">Spain</p>
      <h3>Meet the equality plan and pay transparency rules</h3>
      <p>Companies with 50 or more employees must negotiate and officially register an equality plan, keep a pay register, run a pay audit where gaps exceed the legal threshold, hold a harassment protocol and agree LGBTI measures. Failure is an inspection and sanction risk, not a paperwork one.</p>
      <span class="card-link">See obligations and scope {ARROW}</span>
    </a>
  </div>
</section>

<section class="summary" id="about">
  <div class="summary-heading"><p class="eyebrow">Who we are</p><h2>Specialists in building more equal organisations</h2></div>
  <div class="summary-text">
    <p>GEN+ Igualdad was founded by professionals with more than 25 years producing gender statistics at INDEC &#8212; Argentina's national statistics institute &#8212; coordinating the national registry of violence against women (RUCVM), and training across Argentina and in Galicia, Spain.</p>
    <p>Every protocol, plan and workshop is built to measure. We listen to how an organisation actually works before proposing a single measure, and every recommendation rests on evidence, the applicable legal framework and field experience.</p>
  </div>
</section>

<section class="why" id="why-us">
  <div class="why-intro">
    <p class="eyebrow">Why organisations choose us</p>
    <h2>What a head office gets from working with us</h2>
    <p>The people who design the engagement are the people who deliver it. No account layer, no junior handover, no template with your logo dropped on top.</p>
  </div>
  <div class="why-grid">
    <article>{IC["check"]}<h3>Local law, properly applied</h3><p>Argentine and Spanish requirements are different from each other and from US practice. We work in both, so nothing gets approximated.</p></article>
    <article>{IC["ear"]}<h3>We listen before we act</h3><p>The assessment always comes before the prescription. What works in a 40-person subsidiary is not what works in a plant of 800.</p></article>
    <article>{IC["chat"]}<h3>Reporting you can take upstairs</h3><p>Deliverables in Spanish where the law requires it, executive reporting in English for headquarters, legal and compliance.</p></article>
    <article>{IC["scale"]}<h3>Institutional track record</h3><p>INDEC, FLACSO, UNTREF, UN Women and legal practice in both Argentina and Spain.</p></article>
  </div>
</section>

<section class="services" id="services">
  <div class="section-title"><p class="eyebrow">Services</p><h2>Five services, one standard</h2></div>
  <div class="service-cards">
    <a class="service-card" href="/en/services/equality-protocols">
      <img src="/img/servicios-1.webp" alt="Team drafting a workplace equality protocol" width="500" height="338" loading="lazy" decoding="async">
      <div>{IC["shield"]}<h3>Equality protocols</h3><p>Protocols against violence, discrimination and harassment, secure reporting channels, and intake and investigation tools.</p><span class="card-link">View service {ARROW}</span></div>
    </a>
    <a class="service-card" href="/en/services/training">
      <img src="/img/servicios-2.webp" alt="Gender equality training workshop" width="500" height="338" loading="lazy" decoding="async">
      <div>{IC["grad"]}<h3>Training</h3><p>Practical workshops on equality and violence prevention, plus HR training on how to conduct a complaint intake interview.</p><span class="card-link">View service {ARROW}</span></div>
    </a>
    <a class="service-card" href="/en/services/assessments-and-equality-plans">
      <img src="/img/servicios-3.webp" alt="Data analysis and organisational assessment" width="500" height="338" loading="lazy" decoding="async">
      <div>{IC["chart"]}<h3>Assessments &amp; equality plans</h3><p>Organisational assessments, equality plans with measurable targets, and gender statistics built to official standards.</p><span class="card-link">View service {ARROW}</span></div>
    </a>
    <a class="service-card" href="/en/services/legal-advisory">
      <img src="/img/genmas-1.webp" alt="Legal advisory with a gender perspective" width="555" height="577" loading="lazy" decoding="async">
      <div>{IC["scale"]}<h3>Legal advisory</h3><p>Bringing policies into line with local law, case handling support and legal protection, in Argentina and Spain.</p><span class="card-link">View service {ARROW}</span></div>
    </a>
  </div>

  <div class="flagship">
    <div>
      <p class="eyebrow">Flagship programme</p>
      <h3>Gender equality in the workplace</h3>
      <p>A five-session practical programme with real simulations, case analysis and complaint handling &#8212; the training local teams need for a protocol to function once it is signed.</p>
      <ul>
        <li>Build a culture of equality inside the organisation</li>
        <li>Understand the applicable law &#8212; ILO Convention 190, national and regional rules</li>
        <li>Promote non-discriminatory language</li>
        <li>Prevent sexual and psychological harassment and workplace discrimination</li>
        <li>Develop interview skills and safeguards for complainants</li>
      </ul>
    </div>
    <div class="flagship-side">
      <h4>Format</h4>
      <p>Five live sessions plus guided asynchronous work. On site, remote or hybrid.</p>
      <p>Original materials, case analysis and a final group assessment.</p>
      <p><a class="button primary" href="/en/services/training" style="margin-top:16px">See the full programme</a></p>
    </div>
  </div>
</section>

<section class="about">
  <div class="about-image"><img src="/img/territorio-indec.webp" alt="Mar&#237;a Rosa Diez de Ulzurr&#250;n and her team running a secondary-school course with INDEC" width="900" height="632" loading="lazy"></div>
  <div class="about-copy">
    <p class="eyebrow">About us</p>
    <h2>Consultancy in gender, equality and cultural change</h2>
    <p>At GEN+ we advise organisations on how to build gender equality into how they operate. We identify barriers, design concrete measures and support the shift toward inclusive, equitable and respectful workplaces.</p>
    <div class="mission"><h3>Our mission</h3><p>To promote workplaces that are safe, inclusive and free of violence, through an integrated approach: identifying gaps, designing evidence-based strategies and supporting the change in day-to-day practice.</p></div>
    <div class="mission"><h3>Our vision</h3><p>To be a reference point in building organisations where a gender perspective informs every decision, policy and practice.</p></div>
  </div>
</section>

<section class="team" id="team">
  <div class="section-title"><p class="eyebrow">Our team</p><h2>Specialists with institutional backing</h2></div>
  <div class="team-grid">
    <article>
      <div class="card-photo"><img src="/img/panel-maria-rosa.webp" alt="Mar&#237;a Rosa Diez de Ulzurr&#250;n" width="640" height="1099" loading="lazy" decoding="async"></div>
      <div><h3>Mar&#237;a Rosa Diez de Ulzurrun</h3><h4>Executive Director</h4>
      <p>Sociologist, MA in Social Policy (University of Buenos Aires). Coordinator of Argentina's national registry of violence against women (RUCVM). Lecturer at UNTREF on gender violence, workplace harassment and gender statistics.</p>
      <p class="credentials">INDEC &#183; UNTREF &#183; RUCVM</p></div>
    </article>
    <article>
      <div class="card-photo"><img src="/img/equipo1.webp" alt="Laura Fabiana Rodr&#237;guez" width="500" height="338" loading="lazy" decoding="async"></div>
      <div><h3>Laura Fabiana Rodr&#237;guez</h3><h4>Director of Projects</h4>
      <p>Geographer, MA in Gender, Society and Policy (FLACSO). Coordinator of the Gender Unit at INDEC. Project evaluator for the UN Trust Fund to End Violence against Women.</p>
      <p class="credentials">INDEC &#183; FLACSO &#183; UN Women</p></div>
    </article>
    <article>
      <div class="card-photo"><img src="/img/equipo3.webp" alt="Jos&#233; Ignacio Sampedro" width="500" height="338" loading="lazy" decoding="async"></div>
      <div><h3>Jos&#233; Ignacio Sampedro</h3><h4>Director of Legal Affairs</h4>
      <p>Lawyer, LLM in Transnational Business and Digital Technology Law (University of Santiago de Compostela). Served in the Women, Gender and Diversity Unit of Argentina's Ministry of Security (2009&#8211;2023).</p>
      <p class="credentials">Ministry of Security &#183; USC Galicia</p></div>
    </article>
  </div>
  <p style="margin-top:28px"><a class="button dark" href="/en/team">Meet the full team</a></p>
</section>

<section class="timeline-section" id="track-record">
  <div class="section-title"><p class="eyebrow">Track record</p><h2>Twenty-five years in gender policy</h2></div>
  <div class="timeline">
    <div class="timeline-item"><div class="timeline-dot">1</div><h3>2000 &#8212; 2015</h3><p>Producing and analysing gender statistics at INDEC, Argentina's national statistics institute.</p></div>
    <div class="timeline-item"><div class="timeline-dot">2</div><h3>2015 &#8212; 2020</h3><p>Delivering statistical literacy workshops in universities and secondary schools.</p></div>
    <div class="timeline-item"><div class="timeline-dot">3</div><h3>2020 &#8212; 2025</h3><p>Training public officials, community leaders, NGOs and local communities across every Argentine province.</p></div>
    <div class="timeline-item"><div class="timeline-dot">4</div><h3>2025 +</h3><p>Founding GEN+ Igualdad: protocols, equality plans, assessments and violence prevention in Argentina and Spain.</p></div>
  </div>
</section>

<section class="impact">
  <div>
    <p class="eyebrow">The case for it</p>
    <h2>Why bring in specialists rather than adapt the head-office template</h2>
    <p style="margin-top:18px">Working with people who know the legal framework, the local context and the methodology reduces legal and organisational exposure &#8212; and makes the intervention actually land with the people it is meant for.</p>
  </div>
  <div class="impact-columns">
    <div><h4>For people</h4><div class="impact-list">
      <p><strong>Protection</strong><span>A safe workplace, free of violence</span></p>
      <p><strong>Wellbeing</strong><span>People who feel valued and respected</span></p>
      <p><strong>Growth</strong><span>Fair access to opportunity</span></p>
    </div></div>
    <div><h4>For the business</h4><div class="impact-list">
      <p><strong>Compliance</strong><span>Lower legal and reputational exposure</span></p>
      <p><strong>Productivity</strong><span>Less absenteeism, better performance</span></p>
      <p><strong>Retention</strong><span>Attracts talent, reduces turnover</span></p>
    </div></div>
  </div>
</section>

<section class="institutions" id="presence">
  <div class="section-title"><p class="eyebrow">On the ground</p><h2>Workshops and training in schools, institutions and public bodies</h2></div>
  <div class="institutions-strip">
    <span>INDEC</span><span>FLACSO</span><span>UNTREF</span><span>UN Women &#183; UN Trust Fund</span><span>Argentine Ministry of Security</span><span>RUCVM</span><span>University of Santiago de Compostela</span>
  </div>
  <div class="gallery">
    <div class="gallery-item"><img src="/img/territorio-fondo.webp" alt="Awareness workshop with secondary school students" width="1000" height="626" loading="lazy" decoding="async"></div>
    <div class="gallery-item"><img src="/img/territorio-baradero.webp" alt="Census activity at Instituto San Jos&#233;, Baradero" width="900" height="572" loading="lazy" decoding="async"></div>
    <div class="gallery-item"><img src="/img/territorio-indec.webp" alt="Secondary-school course delivered with INDEC" width="900" height="632" loading="lazy" decoding="async"></div>
    <div class="gallery-item"><img src="/img/territorio-embajada.webp" alt="Presentation at the Embassy of Canada in Argentina" width="1000" height="667" loading="lazy" decoding="async"></div>
    <div class="gallery-item"><img src="/img/territorio-facultad.webp" alt="Working session at the university" width="694" height="749" loading="lazy" decoding="async" style="object-position:center 70%"></div>
    <div class="gallery-item"><img src="/img/genmas-1.webp" alt="A GEN+ Igualdad training session" width="555" height="577" loading="lazy" decoding="async"></div>
  </div>
  <p style="margin-top:28px;max-width:760px">Confidentiality agreements prevent us from naming the private organisations we work with. We are happy to share references during an initial consultation.</p>
</section>

<section class="process">
  <div class="section-title"><p class="eyebrow">Getting started</p><h2>From assessment to change</h2></div>
  <div class="process-grid">
    <article><span class="process-num">01</span><h3>Initial consultation</h3><p>We learn how your organisation works, its context and its objectives.</p></article>
    <article><span class="process-num">02</span><h3>Assessment</h3><p>An analysis of where things stand today and where the equality gaps are.</p></article>
    <article><span class="process-num">03</span><h3>Tailored plan</h3><p>Measures fitted to your reality, with targets you can actually measure.</p></article>
    <article><span class="process-num">04</span><h3>Implementation</h3><p>Continuous support through delivery, on the ground and with your teams.</p></article>
  </div>
  <p style="margin-top:20px"><a class="button primary" href="/en/contact">Book an initial consultation</a></p>
</section>

<section class="faq-section">
  <div class="section-title"><p class="eyebrow">Common questions</p><h2>What head offices ask us first</h2></div>
  <div class="faq">
    <details class="faq-item"><summary>Does our US anti-harassment policy comply in Argentina or Spain?</summary><div class="faq-a"><p>Almost never on its own. A US EEO or anti-harassment policy is a reasonable starting point, but neither country accepts it as evidence of compliance. Argentina and Spain each require a locally drafted procedure, in Spanish, with the reporting channels, timelines and safeguards their own law defines. A translation of the head-office policy is not enough.</p></div></details>
    <details class="faq-item"><summary>What does Spain require from a company with more than 50 employees?</summary><div class="faq-a"><p>A negotiated and officially registered equality plan, a harassment protocol, a pay register and, where pay gaps exceed the legal threshold, a pay audit. Spanish law also requires agreed LGBTI measures. Crucially, these are negotiated with worker representatives &#8212; management cannot simply issue them.</p></div></details>
    <details class="faq-item"><summary>What is ILO Convention 190 and does it apply to us?</summary><div class="faq-a"><p>ILO Convention 190 is the first international treaty on violence and harassment in the world of work. Argentina and Spain have both ratified it &#8212; it entered into force in Argentina in February 2022 and in Spain in May 2023 &#8212; so its standards feed into the national obligations that apply to employers operating there, including your local subsidiary. The United States has not ratified it, which is one reason a US-drafted policy tends not to map onto what these two countries expect. The official text is available on the <a href="https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C190" target="_blank" rel="noopener">ILO's Normlex database</a>.</p></div></details>
    <details class="faq-item"><summary>Do you work in English?</summary><div class="faq-a"><p>Yes. We report, present and correspond in English with headquarters, legal and compliance. Deliverables that must hold up locally are produced in Spanish, and training is delivered in Spanish &#8212; that is what local teams need for any of it to work.</p></div></details>
    <details class="faq-item"><summary>How long does an engagement take?</summary><div class="faq-a"><p>It depends on scope. A harassment protocol with team training typically runs a few weeks. A full Spanish equality plan takes longer, because the law requires a negotiation process with worker representatives before it can be registered. We give you a timeline in the initial consultation, before any commitment.</p></div></details>
  </div>
</section>

{contact_block(label, "Let's talk about what your organisation needs",
               "We start with a free initial consultation to understand where you stand, and then set out a clear, workable proposal for your teams.")}
</main>'''
    h += footer(label) + SCRIPTS
    write("index.html", h)


# =====================================================================
# SERVICES
# =====================================================================
SERVICES = [
    dict(
        slug="equality-protocols", label="Service Protocols",
        title="Workplace Harassment &amp; Equality Protocols in Argentina and Spain | GEN+ Igualdad",
        desc="Harassment and equality protocols drafted to Argentine and Spanish law, with secure reporting channels, intake tools and training for the HR team that will apply them.",
        h1="Equality protocols and reporting channels",
        lead="An effective protocol is not a document in a drawer. It is a clear procedure the whole workforce knows about, with secure channels and real safeguards for anyone who reports. We build it around your organisation &#8212; from small subsidiaries to large employers and institutions &#8212; and around the law that actually applies where your people work.",
        img=("/img/servicios-1.webp", "Team drafting a workplace equality protocol", 500, 338),
        includes=[
            "Assessment of current practice and any procedures already in place",
            "Drafting of the protocol against violence, discrimination and harassment, aligned to the applicable framework &#8212; ILO Convention 190 in Argentina; Organic Law 3/2007 and its implementing rules in Spain",
            "Design of secure, confidential reporting channels",
            "Intake and investigation toolkit: a structured interview questionnaire with methodological criteria and a guide to applying it",
            "Protective measures for complainants and guarantees against retaliation",
            "Internal rollout plan and training for the team that will operate the protocol",
        ],
        who="Companies, subsidiaries of foreign groups, SMEs, public bodies, universities and non-profits that need to create a protocol from scratch, update an existing one, or professionalise how complaints are received and investigated.",
        extra_h2="How we work",
        extra_p="Whether a reporting mechanism works comes down to two things: adequate technical tools, and people trained to use them. So every protocol is delivered together with training for the team that will apply it &#8212; conducting interviews, framing questions, identifying relevant indicators, weighing information, and protecting the rights of everyone involved.",
        deliverables=[
            "A protocol ready to approve and roll out",
            "Complaint intake questionnaire plus methodological guide",
            "Training for the team responsible for applying it",
            "Confidential final report with recommendations",
        ],
        related=[("/en/services/training", "Training in complaint intake interviews"),
                 ("/en/services/legal-advisory", "Legal advisory")],
    ),
    dict(
        slug="training", label="Service Training",
        title="Gender Equality &amp; Anti-Harassment Training for Teams in Argentina and Spain | GEN+ Igualdad",
        desc="Practical training on equality, harassment prevention and complaint intake interviews, delivered in Spanish to local teams by specialists with 25+ years of experience.",
        h1="Training and workshops",
        lead="Practical, case-based training with real simulations and plain language. Three proven programmes, adapted to each organisation, delivered by specialists with more than 25 years of experience. Sessions run in Spanish, because that is what makes them land with local teams.",
        img=("/img/servicios-2.webp", "Gender equality training workshop", 500, 338),
        includes=[
            "<strong>Gender equality in the workplace</strong> &#8212; our flagship programme: five live sessions plus guided asynchronous work. Sex, gender and stereotypes; everyday sexism and respectful communication; new models of masculinity; sexual harassment and harassment on grounds of sex; empathy, active listening and early identification of conflict; equality plans; pay equity, work-life balance and bias in hiring; the business case for equality; commitments and an action plan.",
            "<strong>Preventing gender-based violence in the workplace</strong> &#8212; for staff, middle management and leadership: concepts and law, stereotypes and real cases, warning signs, consequences for people and for the business, and preventive measures.",
            "<strong>HR training on complaint intake interviews</strong> &#8212; an intensive on-site session: interview technique, spotting inconsistencies, follow-up questioning, confidentiality, case analysis and simulated interviews.",
            "Community awareness sessions, train-the-trainer programmes and briefings for leaders and decision-makers",
        ],
        who="Staff, middle managers, leadership, HR teams, public institutions and non-profits. Small groups or scaled programmes for large organisations.",
        extra_h2="Formats",
        extra_p="<strong>On site:</strong> genuine interaction, real simulations, body language and immediate feedback (recommended for sensitive subject matter). <strong>Remote:</strong> live sessions accessible from anywhere in the country. <strong>Hybrid:</strong> key sessions on site with remote follow-up, balancing depth and reach.",
        deliverables=[
            "Programme and materials for every session",
            "Practical exercises, case studies and role play",
            "Confidential final group assessment report",
            "Certificate of participation",
        ],
        related=[("/en/services/equality-protocols", "Equality protocols"),
                 ("/en/services/assessments-and-equality-plans", "Assessments &amp; equality plans")],
    ),
    dict(
        slug="assessments-and-equality-plans", label="Service Assessments",
        title="Equality Plans &amp; Pay Audits for Spain and Argentina | GEN+ Igualdad",
        desc="Organisational assessments, registered equality plans under Spanish law, pay registers and pay audits, and bespoke gender statistics built to official standards.",
        h1="Assessments and equality plans",
        lead="No measure works without a proper diagnosis first. We apply 25 years of official statistical practice to measure real gaps, and turn them into plans with targets, deadlines and indicators you can verify.",
        img=("/img/servicios-3.webp", "Data analysis and organisational assessment", 500, 338),
        includes=[
            "Organisational assessment: surveys, in-depth interviews and focus groups",
            "Analysis of equality gaps: pay, access to decision-making roles, work-life balance, hiring and promotion",
            "An equality plan with measures, measurable targets, a timeline and monitoring indicators",
            "In Spain: assessment and plan under Royal Decree 901/2020, negotiation with worker representatives and support through official registration; pay register and pay audit under Royal Decree 902/2020",
            "Bespoke gender statistics and indicators",
            "Reports with evidence-based recommendations",
        ],
        who="Companies required to register an equality plan in Spain, organisations that want to measure and close their gaps in Argentina, and institutions that need solid data to decide.",
        extra_h2="A note for head offices",
        extra_p="In Spain an equality plan is not a policy management can issue. It has to be negotiated with worker representatives and officially registered, and the process takes time. If your group is planning a compliance deadline, build the negotiation period into the schedule &#8212; that is usually the step that gets underestimated.",
        deliverables=[
            "Assessment report with evidence and prioritised gaps",
            "A complete equality plan, ready to negotiate and register",
            "Monitoring indicator dashboard",
            "Executive presentation for leadership, in English",
        ],
        related=[("/en/services/social-research", "Social research"),
                 ("/en/services/legal-advisory", "Legal advisory")],
    ),
    dict(
        slug="legal-advisory", label="Service Legal",
        title="Legal Advisory on Gender Equality in Argentina and Spain | GEN+ Igualdad",
        desc="Bringing corporate policies into line with Argentine and Spanish equality law, support on harassment and discrimination cases, and legal protection with a gender perspective.",
        h1="Legal advisory with a gender perspective",
        lead="Law is the backbone of any equality policy. Our legal team, qualified across Argentina and Spain, turns the rules into procedures that protect both the people involved and the organisation.",
        img=("/img/genmas-1.webp", "Legal advisory with a gender perspective", 555, 577),
        includes=[
            "Full compliance review: policies, internal rules and procedures against the applicable legal framework",
            "Advice on handling violence, discrimination and harassment cases, safeguarding the rights of all parties",
            "Legal protection for victims of gender-based violence",
            "Drafting organisational policies and contractual clauses with a gender perspective",
            "Legal coaching for inclusive leadership and decision-making",
            "Case follow-up and representation, subject to jurisdiction",
        ],
        who="HR and legal leadership, equality committees, organisations facing a live case, and individuals who need specialist legal protection.",
        extra_h2="Who leads it",
        extra_p="Jos&#233; Ignacio Sampedro, a lawyer with an LLM in Transnational Business and Digital Technology Law (University of Santiago de Compostela). He served in the Women, Gender and Diversity Unit of Argentina's Ministry of Security between 2009 and 2023, and advises victims of gender-based violence in independent practice.",
        deliverables=[
            "Legal opinions and reports",
            "Policies and procedures reviewed or drafted",
            "A compliance roadmap",
            "Documented case support",
        ],
        related=[("/en/services/equality-protocols", "Equality protocols"),
                 ("/en/services/assessments-and-equality-plans", "Assessments &amp; equality plans")],
    ),
    dict(
        slug="social-research", label="Service Research",
        title="Applied Social Research on Gender and Inequality | GEN+ Igualdad",
        desc="Surveys, focus groups, bespoke gender indicators and programme evaluation, with the rigour of 25 years in official statistics and international project evaluation.",
        h1="Applied social research",
        lead="Good decisions rest on data that actually exists. We produce evidence where official statistics do not reach, with the rigour of 25 years in public statistics (INDEC) and in international project evaluation (UN Women &#183; UN Trust Fund).",
        img=("/img/territorio-fondo.webp", "Fieldwork in social research", 1000, 626),
        includes=[
            "Surveys on gender-based violence among populations official statistics do not reach",
            "Focus groups and in-depth interviews",
            "Bespoke gender indicators and statistics",
            "Qualitative and quantitative studies: methodological design, fieldwork, analysis and dissemination",
            "Evaluation of programmes and policies with a gender perspective",
            "Reports with evidence-based recommendations",
        ],
        who="Public administrations, international organisations, universities, foundations and non-profits that need solid data on gender-based violence and inequality &#8212; and companies that want a rigorous measure of their starting point.",
        extra_h2=None, extra_p=None,
        deliverables=[
            "Methodological design and data collection instruments",
            "A documented dataset",
            "Results report with indicators",
            "Executive presentation of findings",
        ],
        related=[("/en/services/assessments-and-equality-plans", "Assessments &amp; equality plans"),
                 ("/en/team", "Meet the team")],
    ),
]


def build_service(s):
    p = "/en/services/" + s["slug"]
    label = s["label"]
    schema = {"@context": "https://schema.org", "@type": "Service",
              "serviceType": s["h1"], "provider": {"@type": "Organization", "name": "GEN+ Igualdad", "url": BASE + "/en"},
              "areaServed": ["Argentina", "Spain"], "url": BASE + p,
              "description": s["desc"]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/en"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": BASE + "/en#services"},
        {"@type": "ListItem", "position": 3, "name": s["h1"]}]}
    h = head(s["title"], s["desc"], p, extra_schema=[schema, bc])
    h += header(p)
    src, alt, w, ht = s["img"]
    extra = ""
    if s.get("extra_h2"):
        extra = f'<h2 style="margin-top:40px">{s["extra_h2"]}</h2>\n      <p>{s["extra_p"]}</p>'
    inc = "".join(f"<li>{i}</li>" for i in s["includes"])
    dlv = "".join(f"<li>{i}</li>" for i in s["deliverables"])
    rel = "".join(f'<a href="{u}">{t} {ARROW}</a>' for u, t in s["related"])
    h += f'''<main id="contenido">
<section class="page-hero compact">
  <div class="page-hero-copy">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/en">Home</a> <span>&#8250;</span> <a href="/en#services">Services</a> <span>&#8250;</span> <span aria-current="page">{s["h1"]}</span></nav>
    <p class="eyebrow">Service</p>
    <h1>{s["h1"]}</h1>
    <p class="lead">{s["lead"]}</p>
    <div class="hero-actions"><a class="button primary" href="/en/contact">Book a consultation</a><a class="button ghost" href="{wa(label)}" target="_blank" rel="noopener" data-ga="contact_whatsapp">Ask on WhatsApp</a></div>
  </div>
</section>
<section class="service-detail">
  <div class="service-detail-grid">
    <div>
      <h2>What it includes</h2>
      <ul class="check-list">{inc}</ul>
      <h2 style="margin-top:40px">Who it is for</h2>
      <p>{s["who"]}</p>
      {extra}
    </div>
    <aside class="service-side">
      <img src="{src}" alt="{alt}" width="{w}" height="{ht}" loading="lazy" decoding="async">
      <div class="service-side-box">
        <h4>Deliverables</h4>
        <ul class="dash-list">{dlv}</ul>
      </div>
      <div class="service-side-box">
        <h4>Format</h4>
        <p>On site, remote or hybrid, in Argentina and Spain, depending on the context and objectives of each organisation. Executive reporting in English.</p>
      </div>
    </aside>
  </div>
</section>

{cta_band(label, "Is this what your organisation needs?", "In a free initial consultation we define scope, timeline and a tailored quote.")}
<section class="related-strip"><p class="eyebrow">You may also be interested in</p><div class="service-links">{rel}</div></section>
</main>'''
    h += footer(label) + SCRIPTS
    write(f"services/{s['slug']}.html", h)


# =====================================================================
# TEAM  /en/team
# =====================================================================
BIOS = [
    dict(img=("/img/panel-maria-rosa.webp", 640, 1099), reverse=False,
         name="Mar&#237;a Rosa Diez de Ulzurrun", role="Executive Director",
         paras=[
             "Sociologist and MA in Social Policy (University of Buenos Aires). Coordinator of Argentina's national registry of violence against women (RUCVM). Lecturer at UNTREF and on undergraduate and postgraduate courses covering gender violence, workplace harassment and the production of gender statistics.",
             "A specialist in designing, analysing and communicating the information behind public gender policy. She has travelled the country delivering workshops under the RUCVM, training public officials, community leaders and civil society organisations.",
         ],
         creds="UBA &#183; INDEC &#183; UNTREF &#183; RUCVM"),
    dict(img=("/img/equipo1.webp", 500, 338), reverse=True,
         name="Laura Fabiana Rodr&#237;guez", role="Director of Projects",
         paras=[
             "Geographer and MA in Gender, Society and Policy (FLACSO). Coordinator of the Gender Unit at INDEC, Argentina's national statistics institute. Trainer on awareness and prevention of gender-based violence.",
             "Project evaluator for civil society work on preventing and eliminating violence against women, for the UN Trust Fund to End Violence against Women.",
         ],
         creds="FLACSO &#183; INDEC &#183; UN Women &#183; UN Trust Fund"),
    dict(img=("/img/equipo3.webp", 500, 338), reverse=False,
         name="Jos&#233; Ignacio Sampedro", role="Director of Legal Affairs",
         paras=[
             "Lawyer with an LLM in Transnational Business and Digital Technology Law (University of Santiago de Compostela). Specialist in applying a gender perspective within legal practice.",
             "He served in the Women, Gender and Diversity Unit of Argentina's Ministry of Security (2009&#8211;2023) and at National Criminal Investigation Prosecutor's Office No. 31 (2006&#8211;2009). He now practises independently, advising victims of gender-based violence, and leads GEN+ Igualdad's operation in Spain.",
         ],
         creds="USC &#183; Argentine Ministry of Security &#183; National Prosecutor's Office"),
]


def build_team():
    p, label = "/en/team", "Team"
    people = [{"@type": "Person", "name": b["name"].replace("&#237;", "i").replace("&#233;", "e"),
               "jobTitle": b["role"], "worksFor": {"@type": "Organization", "name": "GEN+ Igualdad"}}
              for b in BIOS]
    h = head("Our Team | GEN+ Igualdad &#8212; Gender Equality Specialists",
             "A senior team from Argentina's national statistics institute, FLACSO, UNTREF, UN Women and legal practice in Argentina and Spain. The people who design the work deliver it.",
             p, extra_schema=[{"@context": "https://schema.org", "@type": "ItemList",
                               "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": pr}
                                                   for i, pr in enumerate(people)]}])
    h += header(p)
    bios_html = ""
    for b in BIOS:
        src, w, ht = b["img"]
        cls = "bio reverse" if b["reverse"] else "bio"
        ps = "".join(f"<p>{x}</p>" for x in b["paras"])
        bios_html += f'''  <article class="{cls}">
    <div class="bio-photo"><img src="{src}" alt="{b["name"]}" width="{w}" height="{ht}" loading="lazy" decoding="async"></div>
    <div class="bio-copy">
      <h2>{b["name"]}</h2><h4>{b["role"]}</h4>
      {ps}
      <p class="credentials">{b["creds"]}</p>
    </div>
  </article>
'''
    h += f'''<main id="contenido">
<section class="page-hero compact">
  <div class="page-hero-copy">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/en">Home</a> <span>&#8250;</span> <span aria-current="page">Team</span></nav>
    <p class="eyebrow">Our team</p>
    <h1>Specialists with institutional backing</h1>
    <p class="lead">Credentials behind every engagement: official statistics, academia, international organisations and legal practice in Argentina and Spain.</p>
  </div>
</section>
<section class="team-full">
{bios_html}</section>

{cta_band(label, "A senior team, with no one in between", "The people who design the proposal are the people who deliver it. Let's talk about your organisation.")}
</main>'''
    h += footer(label) + SCRIPTS
    write("team.html", h)


# =====================================================================
# CONTACT  /en/contact
# =====================================================================
def build_contact():
    p, label = "/en/contact", "Contact"
    h = head("Contact | GEN+ Igualdad &#8212; Equality Consultancy for Argentina &amp; Spain",
             "Book a free initial consultation. We work across US, Argentine and Spanish time zones and report in English. Offices in Buenos Aires and Santiago de Compostela.",
             p, extra_schema=[{"@context": "https://schema.org", "@type": "ContactPage",
                               "url": BASE + p, "name": "Contact GEN+ Igualdad"}])
    h += header(p)
    h += f'''<main id="contenido">
<section class="page-hero compact">
  <div class="page-hero-copy">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="/en">Home</a> <span>&#8250;</span> <span aria-current="page">Contact</span></nav>
    <p class="eyebrow">Contact</p>
    <h1>Let's talk about your organisation</h1>
    <p class="lead">The first step is an initial consultation, with no commitment. We learn your context and map out the route to a fairer, safer organisation &#8212; wherever your teams are based.</p>
  </div>
</section>
<section class="scheduling"><div class="section-title"><p class="eyebrow">Book directly</p><h2>Pick a day and time</h2></div>
<p style="text-align:center"><a class="button primary" href="{SCHEDULING_LINK}" target="_blank" rel="noopener" data-ga="schedule_click">Open the booking calendar</a></p>
<p style="text-align:center;margin-top:12px;font-size:.92rem">Times shown are Argentina time (UTC&#8722;3). If nothing fits your working day, email us and we will find a slot.</p></section>

{contact_block(label, "Let's talk about what your organisation needs",
               "We start with a free initial meeting to understand where you stand, and then set out a clear, workable proposal for your teams.")}
</main>'''
    h += footer(label) + SCRIPTS
    write("contact.html", h)


if __name__ == "__main__":
    print("Building /en ...")
    build_home()
    for s in SERVICES:
        build_service(s)
    build_team()
    build_contact()
    print("Done. %d pages." % (2 + len(SERVICES) + 1))

