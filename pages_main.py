# -*- coding: utf-8 -*-
"""Páginas principales — ejecutar después de build.py: exec en el mismo proceso"""
from build import *

# ============================================================ HOME
home_body = f"""
<section class="hero" id="inicio">
  <div class="hero-copy">
    <p class="eyebrow">Consultoría en género · Argentina y España</p>
    <h1>Impulsamos organizaciones más igualitarias, sostenibles y competitivas</h1>
    <p class="lead">Elaboramos protocolos frente al acoso y la violencia laboral, planes de igualdad y diagnósticos, y dictamos capacitaciones. Contamos con más de 25 años de reconocida experiencia en la temática: el mismo rigor que aplicamos en el INDEC, la FLACSO y el territorio, al servicio de empresas e instituciones.</p>
    <div class="hero-actions"><a class="button primary" href="/contacto">Agendar consulta</a><a class="button ghost" href="{WA_LINK}" target="_blank" rel="noopener" data-ga="contact_whatsapp">WhatsApp directo</a></div>
    <div class="trust-strip"><span>INDEC</span><span>FLACSO</span><span>UNTREF</span><span>ONU Mujeres</span><span>RUCVM</span><span>USC Galicia</span></div>
  </div>
  <figure class="hero-image">
    <img src="/img/hero-laura.webp" alt="Equipo de Gen+ Igualdad elaborando un protocolo de igualdad" width="1200" height="800" fetchpriority="high">
    <figcaption>Más de 25 años formando equipos en el territorio</figcaption>
  </figure>
</section>

<section class="country-band">
  <div class="section-title"><p class="eyebrow">Presencia en Argentina y España</p><h2>¿Desde dónde nos visitas?</h2></div>
  <div class="country-cards">
    <a class="country-card" href="/espana">
      <p class="eyebrow">España</p>
      <h3>Cumple con la normativa de igualdad</h3>
      <p>Protocolo frente al acoso, plan de igualdad, registro retributivo y medidas LGTBI: qué exige la ley a tu empresa y cómo resolverlo sin fricción.</p>
      <span class="card-link">Ver obligaciones y servicios {IC["arrow"]}</span>
    </a>
    <a class="country-card" href="/argentina">
      <p class="eyebrow">Argentina</p>
      <h3>Prevenga la violencia laboral</h3>
      <p>Convenio 190 de la OIT, protocolos, herramientas de recepción de denuncias y capacitación para equipos y RR.HH. en todo el país.</p>
      <span class="card-link">Ver marco normativo y servicios {IC["arrow"]}</span>
    </a>
  </div>
</section>

<section class="summary" id="empresas">
  <div class="summary-heading"><p class="eyebrow">Especialización real</p><h2>Especialistas en construir organizaciones más igualitarias</h2></div>
  <div class="summary-text">
    <p>Gen+ Igualdad nace del trabajo de profesionales que llevan más de 25 años elaborando estadísticas de género en el INDEC, coordinando el Registro Único de Casos de Violencia contra las Mujeres (RUCVM) y capacitando en todo el territorio argentino y en Galicia, España.</p>
    <p>Cada protocolo, plan y taller se diseña a medida: escuchamos la realidad de cada organización antes de proponer una sola medida, y cada propuesta se apoya en evidencia, marco normativo y experiencia territorial.</p>
  </div>
</section>

<section class="why" id="por-que">
  <div class="why-intro">
    <p class="eyebrow">Por qué nos eligen</p>
    <h2>Razones por las que las organizaciones confían en Gen+ Igualdad</h2>
    <p>Un recorrido sólido en capacitaciones y talleres de sensibilización sobre violencia de género, con perspectiva y enfoque comunitario, construido en todo el país en el marco del RUCVM.</p>
  </div>
  <div class="why-grid">
    <article>{IC["check"]}<h3>Experiencia al servicio de la igualdad</h3><p>Cada intervención se apoya en más de dos décadas de trabajo estadístico, académico y territorial, adaptado a cada organización.</p></article>
    <article>{IC["ear"]}<h3>Escuchamos antes de actuar</h3><p>Adaptamos cada propuesta a la realidad de quienes la reciben: el diagnóstico siempre viene antes que la receta.</p></article>
    <article>{IC["chat"]}<h3>Hacemos fácil lo difícil</h3><p>Hablamos claro, conectamos con las personas y generamos impacto real en temas sensibles.</p></article>
    <article>{IC["scale"]}<h3>Respaldo institucional</h3><p>Trayectoria en INDEC, FLACSO, UNTREF, ONU Mujeres y el ámbito jurídico de Argentina y España.</p></article>
  </div>
</section>

<section class="services" id="servicios">
  <div class="section-title"><p class="eyebrow">Servicios</p><h2>Cuatro soluciones, un mismo estándar</h2></div>
  <div class="service-cards">
    <a class="service-card" href="/servicios/protocolos-de-igualdad">
      {img("servicios-1","Equipo de trabajo elaborando un protocolo de igualdad")}
      <div>{IC["shield"]}<h3>Protocolos de igualdad</h3><p>Protocolos frente a la violencia, la discriminación y el acoso, canales de denuncia seguros y herramientas de recepción e investigación.</p><span class="card-link">Ver servicio {IC["arrow"]}</span></div>
    </a>
    <a class="service-card" href="/servicios/capacitaciones">
      {img("servicios-2","Taller de capacitación en igualdad de género")}
      <div>{IC["grad"]}<h3>Capacitaciones</h3><p>Talleres teórico-prácticos en igualdad, prevención de la violencia y formación de RR.HH. en entrevista de denuncia.</p><span class="card-link">Ver servicio {IC["arrow"]}</span></div>
    </a>
    <a class="service-card" href="/servicios/diagnosticos-y-planes">
      {img("servicios-3","Análisis de datos y diagnóstico organizacional")}
      <div>{IC["chart"]}<h3>Diagnósticos y planes</h3><p>Diagnósticos organizacionales, planes de igualdad con metas medibles y estadísticas de género con estándar INDEC.</p><span class="card-link">Ver servicio {IC["arrow"]}</span></div>
    </a>
    <a class="service-card" href="/servicios/asesoria-juridica">
      {img("genmas-1","Asesoramiento jurídico con perspectiva de género")}
      <div>{IC["scale"]}<h3>Asesoría jurídica</h3><p>Adecuación normativa, acompañamiento de casos y protección jurídica con perspectiva de género en Argentina y España.</p><span class="card-link">Ver servicio {IC["arrow"]}</span></div>
    </a>
  </div>

  <div class="flagship">
    <div>
      <p class="eyebrow">Taller insignia</p>
      <h3>Igualdad de género en entornos laborales</h3>
      <p>Taller teórico-práctico de transformación: 5 encuentros interactivos con simulaciones reales, análisis de casos y gestión de denuncias de violencia laboral.</p>
      <ul>
        <li>Fomentar una cultura de igualdad en la organización</li>
        <li>Conocer la legislación vigente — Convenio 190 OIT, normativa nacional y autonómica</li>
        <li>Promover el lenguaje no discriminatorio</li>
        <li>Prevenir el acoso sexual, psicológico y la discriminación laboral</li>
        <li>Desarrollar habilidades de entrevista y protección de denunciantes</li>
      </ul>
    </div>
    <div class="flagship-side">
      <h4>Modalidad</h4>
      <p>5 encuentros sincrónicos más trabajo asincrónico guiado. Presencial, virtual o híbrido.</p>
      <p>Material propio, análisis de casos y evaluación final grupal.</p>
      <p><a class="button primary" href="/servicios/capacitaciones" style="margin-top:16px">Ver programa completo</a></p>
    </div>
  </div>
</section>

<section class="about">
  <div class="about-image"><img src="/img/territorio-indec.webp" alt="María Rosa Diez de Ulzurrún junto a su equipo en un curso para nivel secundario con el INDEC" width="900" height="632" loading="lazy"></div>
  <div class="about-copy">
    <p class="eyebrow">Sobre nosotros</p>
    <h2>Consultoría especializada en género, igualdad y transformación cultural</h2>
    <p>En GEN+ brindamos asesoramiento y orientación para fomentar la igualdad de género en empresas y organizaciones. Nuestro equipo identifica barreras, diseña acciones concretas y promueve entornos inclusivos, equitativos y respetuosos.</p>
    <div class="mission"><h3>Nuestra misión</h3><p>Promover espacios laborales seguros, inclusivos y libres de violencia mediante un abordaje integral con perspectiva de género: identificamos brechas, diseñamos estrategias basadas en evidencia y acompañamos la transformación de las prácticas.</p></div>
    <div class="mission"><h3>Nuestra visión</h3><p>Ser referentes en la construcción de organizaciones donde la perspectiva de género forme parte de cada decisión, política y práctica.</p></div>
  </div>
</section>

<section class="team" id="equipo">
  <div class="section-title"><p class="eyebrow">Nuestro equipo</p><h2>Especialistas con respaldo institucional</h2></div>
  <div class="team-grid">
    <article>
      <div class="card-photo">{img("panel-maria-rosa","María Rosa Diez de Ulzurrún")}</div>
      <div><h3>María Rosa Diez de Ulzurrun</h3><h4>Directora ejecutiva</h4>
      <p>Socióloga, Magíster en Políticas Sociales (UBA). Coordinadora del RUCVM. Docente de grado y posgrado en la UNTREF sobre violencia de género, acoso laboral y estadísticas con perspectiva de género.</p>
      <p class="credentials">INDEC · UNTREF · RUCVM</p></div>
    </article>
    <article>
      <div class="card-photo">{img("equipo1","Laura Fabiana Rodríguez")}</div>
      <div><h3>Laura Fabiana Rodríguez</h3><h4>Directora de proyectos</h4>
      <p>Geógrafa, Magíster en Género, Sociedad y Políticas (FLACSO). Coordinadora de la Unidad de Género del INDEC. Evaluadora de proyectos para el UN Trust Fund de Naciones Unidas.</p>
      <p class="credentials">INDEC · FLACSO · ONU Mujeres</p></div>
    </article>
    <article>
      <div class="card-photo">{img("equipo3","José Ignacio Sampedro")}</div>
      <div><h3>José Ignacio Sampedro</h3><h4>Director de asuntos jurídicos</h4>
      <p>Abogado, Máster en Derecho Transnacional de la Empresa y las Tecnologías Digitales (USC). Integró la Unidad de Mujeres, Géneros y Diversidad del Ministerio de Seguridad de la Nación (2009–2023).</p>
      <p class="credentials">Ministerio de Seguridad · USC Galicia</p></div>
    </article>
  </div>
  <p style="margin-top:28px"><a class="button dark" href="/equipo">Conocer al equipo completo</a></p>
</section>

<section class="timeline-section" id="trayectoria">
  <div class="section-title"><p class="eyebrow">Experiencia que respalda</p><h2>Veinticinco años en políticas de género</h2></div>
  <div class="timeline">
    <div class="timeline-item"><div class="timeline-dot">1</div><h3>2000 — 2015</h3><p>Trabajamos en el INDEC elaborando y analizando estadísticas de género.</p></div>
    <div class="timeline-item"><div class="timeline-dot">2</div><h3>2015 — 2020</h3><p>Dictamos talleres de alfabetización estadística en universidades y secundarios.</p></div>
    <div class="timeline-item"><div class="timeline-dot">3</div><h3>2020 — 2025</h3><p>Capacitamos en todas las provincias a funcionarios, líderes, ONGs y comunidad.</p></div>
    <div class="timeline-item"><div class="timeline-dot">4</div><h3>2025 +</h3><p>Creamos Gen+ Igualdad: protocolos, planes de igualdad, diagnósticos y prevención de violencia en Argentina y España.</p></div>
  </div>
</section>

<section class="impact">
  <div>
    <p class="eyebrow">El impacto</p>
    <h2>Por qué incorporar la agenda de igualdad con especialistas</h2>
    <p style="margin-top:18px">Trabajar con quienes conocen el marco normativo, el territorio y la metodología reduce el riesgo legal y organizacional, y multiplica el impacto real de cada intervención.</p>
  </div>
  <div class="impact-columns">
    <div><h4>Para las personas</h4><div class="impact-list">
      <p><strong>Protección</strong><span>Espacio seguro y libre de violencia</span></p>
      <p><strong>Bienestar</strong><span>Personas valoradas y respetadas</span></p>
      <p><strong>Crecimiento</strong><span>Oportunidades equitativas</span></p>
    </div></div>
    <div><h4>Para la empresa</h4><div class="impact-list">
      <p><strong>Cumplimiento</strong><span>Menos riesgo legal y reputacional</span></p>
      <p><strong>Productividad</strong><span>Menos ausentismo, más rendimiento</span></p>
      <p><strong>Retención</strong><span>Atrae talento y reduce rotación</span></p>
    </div></div>
  </div>
</section>

<section class="institutions" id="presencia">
  <div class="section-title"><p class="eyebrow">Presentes en el territorio</p><h2>Talleres y capacitaciones en escuelas, instituciones y organismos</h2></div>
  <div class="institutions-strip">
    <span>INDEC</span><span>FLACSO</span><span>UNTREF</span><span>ONU Mujeres · UN Trust Fund</span><span>Ministerio de Seguridad de la Nación</span><span>RUCVM</span><span>Universidad de Santiago de Compostela</span>
  </div>
  <div class="gallery">
    <div class="gallery-item">{img("territorio-fondo","Taller de sensibilización con estudiantes secundarios")}</div>
    <div class="gallery-item">{img("territorio-baradero","Actividad de censo en el Instituto San José, Baradero")}</div>
    <div class="gallery-item">{img("territorio-indec","Curso para nivel secundario junto al INDEC")}</div>
    <div class="gallery-item">{img("territorio-amanecer","Jornada de capacitación territorial")}</div>
    <div class="gallery-item">{img("territorio-cimdip","Capacitación junto al CIMDIP")}</div>
    <div class="gallery-item">{img("genmas-1","Actividad de formación de Gen+ Igualdad")}</div>
  </div>
  <p style="margin-top:28px;max-width:760px">Por acuerdos de confidencialidad, no publicamos el detalle de las organizaciones privadas con las que trabajamos. Con gusto compartimos referencias en la consulta inicial.</p>
</section>

<section class="process">
  <div class="section-title"><p class="eyebrow">El primer paso</p><h2>Del diagnóstico a la transformación</h2></div>
  <div class="process-grid">
    <article><span class="process-num">01</span><h3>Consulta inicial</h3><p>Conocemos tu organización, su contexto y sus objetivos.</p></article>
    <article><span class="process-num">02</span><h3>Diagnóstico</h3><p>Análisis de la situación actual y de las brechas de igualdad.</p></article>
    <article><span class="process-num">03</span><h3>Plan personalizado</h3><p>Soluciones adaptadas a tu realidad, con metas medibles.</p></article>
    <article><span class="process-num">04</span><h3>Implementación</h3><p>Acompañamiento integral y continuo en la ejecución.</p></article>
  </div>
  <p style="margin-top:28px">Acompañamos cada etapa con presencia real en el territorio.</p>
  <p style="margin-top:20px"><a class="button primary" href="/contacto">Agendar consulta inicial</a></p>
</section>

<section class="resources" id="recursos">
  <div class="section-title"><p class="eyebrow">Recursos</p><h2>Guías y artículos sobre igualdad en el trabajo</h2></div>
  <p style="max-width:760px">Contenido basado en nuestra experiencia en el territorio: guías prácticas, marco normativo y criterios técnicos.</p>
  <div class="blog-grid">
    <a class="blog-card" href="/recursos/protocolo-de-igualdad-paso-a-paso"><span class="tag">Guía</span><h3>Cómo diseñar un protocolo de igualdad, paso a paso</h3><p>Los componentes que no pueden faltar en un protocolo eficaz.</p><span class="card-link">Leer guía {IC["arrow"]}</span></a>
    <a class="blog-card" href="/recursos/convenio-190-oit"><span class="tag">Normativa</span><h3>Convenio 190 de la OIT: qué cambia para tu organización</h3><p>El tratado internacional contra la violencia laboral, explicado en claro.</p><span class="card-link">Leer artículo {IC["arrow"]}</span></a>
    <a class="blog-card" href="/recursos/entrevista-de-denuncia"><span class="tag">RR.HH.</span><h3>Cómo conducir una entrevista de denuncia</h3><p>Criterios técnicos para recibir e investigar casos con rigor y cuidado.</p><span class="card-link">Leer artículo {IC["arrow"]}</span></a>
  </div>
</section>
""" + contact_section()

page("index.html",
     "GEN+ Igualdad | Protocolos, planes de igualdad y capacitación en Argentina y España",
     "Consultora especializada en violencia laboral, protocolos y planes de igualdad y capacitación en género. Más de 25 años de reconocida experiencia en la temática en Argentina y España.",
     "/", home_body, hreflang=True)

# ============================================================ ESPAÑA
faq_es, faq_es_schema = faq_block([
 ("¿Mi empresa está obligada a tener un plan de igualdad?",
  "Sí, si tiene 50 o más personas en plantilla (RD 901/2020). También puede ser obligatorio por convenio colectivo o por resolución de la autoridad laboral, con independencia del tamaño. El plan debe partir de un diagnóstico negociado con la representación legal de las personas trabajadoras y registrarse oficialmente."),
 ("¿El protocolo frente al acoso es obligatorio aunque tengamos pocas personas empleadas?",
  "Sí. La Ley Orgánica 3/2007 obliga a todas las empresas, sin importar su tamaño, a adoptar medidas y un procedimiento específico para prevenir y dar cauce a las denuncias por acoso sexual y por razón de sexo."),
 ("¿Qué es el registro retributivo y quién debe tenerlo?",
  "Todas las empresas deben llevar un registro salarial desagregado por sexo (RD 902/2020), con los valores medios de salarios, complementos y percepciones extrasalariales. Las empresas con plan de igualdad deben además realizar una auditoría retributiva."),
 ("¿Qué sanciones hay por incumplir?",
  "El incumplimiento constituye infracción grave o muy grave según la LISOS, con multas que en los supuestos más graves pueden superar los 200.000 €, además de la pérdida de ayudas y bonificaciones y de la posibilidad de contratar con el sector público."),
 ("¿Trabajáis en toda España?",
  "Sí. Tenemos sede en Santiago de Compostela y trabajamos de forma presencial en Galicia y en modalidad virtual o híbrida en el resto de España. Atendemos en castellano y galego."),
])

espana_body = f"""
<section class="page-hero">
  <div class="page-hero-copy">
    <p class="eyebrow">Empresas e instituciones en España</p>
    <h1>¿Tu empresa cumple con la normativa de igualdad?</h1>
    <p class="lead">Todas las empresas están obligadas a contar con un protocolo frente al acoso; a partir de 50 personas en plantilla, también con un plan de igualdad registrado. Te ayudamos a cumplir de forma ágil — y a que el cumplimiento se convierta en una ventaja real.</p>
    <div class="hero-actions"><a class="button primary" href="/contacto">Agendar consulta</a><a class="button ghost" href="/recursos/checklist-plan-de-igualdad">Descargar checklist de obligaciones</a></div>
  </div>
</section>

<section class="legal-section">
  <div class="section-title"><p class="eyebrow">Lo que exige la ley</p><h2>Las obligaciones que tu empresa debe tener resueltas</h2></div>
  <div class="legal-grid">
    <article class="legal-card"><span class="badge">Todas las empresas</span><h3>Protocolo frente al acoso</h3><p>Medidas y procedimiento específico para prevenir el acoso sexual y por razón de sexo y dar cauce a las denuncias.</p><p class="legal-ref">Ley Orgánica 3/2007, art. 48</p></article>
    <article class="legal-card"><span class="badge accent">50+ personas</span><h3>Plan de igualdad</h3><p>Diagnóstico negociado, medidas evaluables, registro oficial y seguimiento periódico del plan.</p><p class="legal-ref">RD 901/2020</p></article>
    <article class="legal-card"><span class="badge">Todas las empresas</span><h3>Registro retributivo</h3><p>Registro salarial desagregado por sexo; auditoría retributiva para las empresas con plan de igualdad.</p><p class="legal-ref">RD 902/2020</p></article>
    <article class="legal-card"><span class="badge accent">50+ personas</span><h3>Medidas LGTBI</h3><p>Conjunto planificado de medidas y protocolo frente al acoso y la violencia contra las personas LGTBI.</p><p class="legal-ref">Ley 4/2023 · RD 1026/2024</p></article>
    <article class="legal-card"><span class="badge">Vigente desde 2023</span><h3>Convenio 190 OIT</h3><p>Primer tratado internacional sobre violencia y acoso en el mundo del trabajo, ratificado por España en 2022. Alcanza a todos los sectores y modalidades, incluido el teletrabajo.</p><p class="legal-ref"><a href="https://normlex.ilo.org/dyn/nrmlx_es/f?p=NORMLEXPUB:12100:0::NO::P12100_INSTRUMENT_ID:3999810" target="_blank" rel="noopener">Texto oficial (OIT)</a></p></article>
  </div>
  <div class="notice"><p><strong>El incumplimiento de la normativa vigente</strong> podría exponer su empresa a multas, pérdida de ayudas y bonificaciones, y exclusión de la contratación pública (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2000-15060" target="_blank" rel="noopener">LISOS</a>). Cumplir bien, además, mejora el clima laboral, la atracción de talento y la reputación.</p></div>
</section>

<section class="services-lite">
  <div class="section-title"><p class="eyebrow">Nuestros ejes de trabajo</p><h2>Cuatro ejes, un mismo objetivo: igualdad real y cumplimiento</h2></div>
  <div class="ejes">
    <details class="eje-item" open>
      <summary><span class="eje-num">01</span><span class="eje-head"><span class="eje-title">Planes de igualdad</span><span class="eje-sub">Del diagnóstico al registro oficial, conforme al RD 901/2020.</span></span></summary>
      <div class="eje-body">
        <ul class="check-list">
          <li>Diagnóstico y valoración de puestos de trabajo</li>
          <li>Elaboración y adaptación de protocolos frente al acoso sexual y por razón de sexo</li>
          <li>Registro retributivo y auditoría retributiva (RD 902/2020)</li>
          <li>Prevención del acoso y de la violencia en el trabajo</li>
          <li>Indicadores de evaluación y seguimiento del plan</li>
        </ul>
        <div class="eje-links"><a href="/servicios/diagnosticos-y-planes">Planes de igualdad y diagnósticos {IC["arrow"]}</a><a href="/servicios/protocolos-de-igualdad">Protocolos de igualdad {IC["arrow"]}</a></div>
      </div>
    </details>
    <details class="eje-item">
      <summary><span class="eje-num">02</span><span class="eje-head"><span class="eje-title">Asesoramiento jurídico</span><span class="eje-sub">La legislación de igualdad, traducida en decisiones seguras para tu empresa.</span></span></summary>
      <div class="eje-body">
        <ul class="check-list">
          <li>Asesoramiento sobre la legislación vigente: LO 3/2007, RD 901/2020 y 902/2020, Ley 4/2023</li>
          <li>Revisión de políticas, reglamentos y procedimientos internos</li>
          <li>Prevención de multas y sanciones (LISOS) y de la exclusión de la contratación pública</li>
          <li>Acompañamiento jurídico en casos de acoso y discriminación</li>
        </ul>
        <div class="eje-links"><a href="/servicios/asesoria-juridica">Asesoría jurídica {IC["arrow"]}</a></div>
      </div>
    </details>
    <details class="eje-item">
      <summary><span class="eje-num">03</span><span class="eje-head"><span class="eje-title">Capacitación</span><span class="eje-sub">Cursos y talleres para empresas, administraciones públicas, centros educativos y entidades sociales y deportivas.</span></span></summary>
      <div class="eje-body">
        <ul class="check-list">
          <li>Formación de plantilla, mandos intermedios y RR.HH.</li>
          <li>Taller insignia: igualdad de género en entornos laborales</li>
          <li>Prevención del acoso sexual y por razón de sexo</li>
          <li>Formación de RR.HH. en entrevista de denuncia</li>
          <li>Sensibilización en centros educativos, clubes deportivos y entidades sociales</li>
        </ul>
        <div class="eje-links"><a href="/servicios/capacitaciones">Capacitaciones y talleres {IC["arrow"]}</a></div>
      </div>
    </details>
    <details class="eje-item">
      <summary><span class="eje-num">04</span><span class="eje-head"><span class="eje-title">Investigación social</span><span class="eje-sub">Datos rigurosos donde no llegan las estadísticas oficiales.</span></span></summary>
      <div class="eje-body">
        <ul class="check-list">
          <li>Encuestas de violencia de género en poblaciones que las estadísticas oficiales no alcanzan</li>
          <li>Grupos focales y entrevistas en profundidad</li>
          <li>Elaboración de indicadores y estadísticas de género</li>
          <li>Estudios cualitativos y cuantitativos, con el estándar de 25 años en estadística oficial</li>
        </ul>
        <div class="eje-links"><a href="/servicios/investigacion">Investigación social {IC["arrow"]}</a></div>
      </div>
    </details>
  </div>
</section>

<section class="galicia">
  <div class="galicia-inner">
    <div>
      <p class="eyebrow">Sede en Galicia</p>
      <h2>Desde Santiago de Compostela, para toda España</h2>
      <p>Nuestro equipo de asuntos jurídicos, formado en la Universidad de Santiago de Compostela, lidera la operación en España. Trabajamos de forma presencial en Galicia y virtual o híbrida en el resto del territorio, en castellano y en galego.</p>
      <p style="margin-top:14px">Experiencia de más de 25 años en políticas públicas de género, estadística oficial y formación, hoy al servicio de empresas, administraciones y entidades del tercer sector.</p>
    </div>
    <div class="galicia-contact">
      <h4>{IC["pin"]} Santiago de Compostela</h4>
      <p><a href="tel:+34698187971">+34 698 187 971</a></p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <a class="button primary" href="/contacto" style="margin-top:16px">Agendar consulta</a>
    </div>
  </div>
</section>

{faq_es}

<section class="lead-magnet">
  <div class="cta-band-inner">
    <div><p class="eyebrow">Recurso gratuito</p><h2>Checklist: ¿está tu empresa obligada a tener un plan de igualdad?</h2><p>Repasa en 5 minutos qué obligaciones aplican a tu empresa según su tamaño y situación, y qué documentos deberías tener al día.</p></div>
    <div class="cta-band-actions"><a class="button primary" href="/recursos/checklist-plan-de-igualdad">{IC["download"]} Ver y descargar el checklist</a></div>
  </div>
</section>
""" + contact_section(country="es")

page("espana.html",
     "Planes de igualdad y protocolos de acoso para empresas | GEN+ Igualdad España",
     "Plan de igualdad (RD 901/2020), protocolo frente al acoso, registro retributivo y medidas LGTBI. Consultora especializada con sede en Santiago de Compostela.",
     "/espana", espana_body, extra_schema=[faq_es_schema], hreflang=True)

# ============================================================ ARGENTINA
faq_ar, faq_ar_schema = faq_block([
 ("¿Las empresas argentinas están obligadas a tener un protocolo contra la violencia laboral?",
  "No existe una única norma que lo imponga de forma general al sector privado, pero el Convenio 190 de la OIT (vigente en Argentina por la Ley 27.580) exige a los Estados que empleadores adopten medidas de prevención, y el deber de seguridad e indemnidad del empleador (LCT) genera responsabilidad frente a casos de violencia y acoso. Contar con protocolo, canal de denuncias y capacitación es hoy el estándar que reduce el riesgo legal y organizacional."),
 ("¿Qué es el Convenio 190 y desde cuándo rige?",
  "Es el primer tratado internacional sobre violencia y acoso en el mundo del trabajo. Argentina lo ratificó mediante la Ley 27.580 y está vigente desde 2021. Define la violencia y el acoso de forma amplia y alcanza a todas las personas del mundo del trabajo, incluyendo modalidades remotas y espacios conexos al trabajo."),
 ("¿La capacitación en género es obligatoria?",
  "La Ley Micaela (27.499) obliga a capacitarse a quienes integran los tres poderes del Estado. En el sector privado no es obligatoria con carácter general, pero es la medida de prevención más efectiva y la principal evidencia de diligencia del empleador ante un caso."),
 ("¿Trabajan en todo el país?",
  "Sí. Hemos capacitado en todas las provincias. Trabajamos en modalidad presencial, virtual o híbrida según el contexto y las necesidades de cada equipo."),
 ("¿Qué incluye una intervención típica?",
  "Una evaluación previa para relevar la situación, el diseño de la herramienta o capacitación a medida, la implementación con nuestro equipo de especialistas y un informe final confidencial con recomendaciones."),
])

argentina_body = f"""
<section class="page-hero">
  <div class="page-hero-copy">
    <p class="eyebrow">Empresas y organizaciones en Argentina</p>
    <h1>La violencia laboral es un riesgo real. Prevenirla es una decisión estratégica.</h1>
    <p class="lead">Desde la vigencia del Convenio 190 de la OIT, ratificado por Argentina mediante la Ley 27.580, la prevención de la violencia y el acoso dejó de ser opcional: es un estándar de gestión. Diseñamos protocolos, herramientas de denuncia y capacitaciones con 25 años de reconocida experiencia en la temática.</p>
    <div class="hero-actions"><a class="button primary" href="/contacto">Agendar consulta</a><a class="button ghost" href="{WA_LINK}" target="_blank" rel="noopener" data-ga="contact_whatsapp">WhatsApp directo</a></div>
  </div>
</section>

<section class="impact-stats" id="datos">
  <div class="section-title"><p class="eyebrow">Violencia laboral en Argentina</p><h2>Datos que demandan acción</h2></div>
  <div class="stats-grid">
    <div class="stat-card"><span class="stat-number">30%</span><p>de las personas ocupadas vivió violencia en el trabajo</p></div>
    <div class="stat-card"><span class="stat-number">14%</span><p>de las personas asalariadas sufrió acoso u hostigamiento</p></div>
    <div class="stat-card"><span class="stat-number">88%</span><p>de las mujeres recibió comentarios sexistas o discriminatorios</p></div>
    <div class="stat-card"><span class="stat-number">67%</span><p>de las víctimas nunca denuncia por miedo, vergüenza o desconfianza</p></div>
  </div>
  <p class="stats-sources">Fuentes: ECETSS · Encuesta de Condiciones de Empleo, Trabajo, Salud y Seguridad — OAVL · Oficina de Asesoramiento sobre Violencia Laboral — ELA-NODOS · Equipo Latinoamericano de Justicia y Género.</p>
</section>

<section class="legal-section alt">
  <div class="section-title"><p class="eyebrow">Marco normativo</p><h2>El estándar legal que las organizaciones deben conocer</h2></div>
  <div class="legal-grid">
    <a class="legal-card" href="/recursos/convenio-190-oit"><span class="badge">Vigente desde 2021</span><h3>Convenio 190 OIT</h3><p>Primer tratado internacional sobre violencia y acoso en el mundo del trabajo, ratificado por la Ley 27.580 el 11 de noviembre de 2020. Alcanza a todos los sectores y modalidades, incluido el teletrabajo.</p><p class="legal-ref">Ley 27.580 · Leer el artículo →</p></a>
    <a class="legal-card" href="/recursos/ley-26485"><span class="badge accent">Protección integral</span><h3>Ley 26.485</h3><p>Reconoce la violencia laboral contra las mujeres como una de las modalidades de violencia de género y habilita vías de protección específicas.</p><p class="legal-ref">Ley 26.485, art. 6 · Leer el artículo →</p></a>
    <a class="legal-card" href="https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=25552" target="_blank" rel="noopener"><span class="badge">Responsabilidad</span><h3>Deber de seguridad</h3><p>El art. 75 de la LCT obliga a proteger la integridad y la dignidad de tus equipos. No prevenir la violencia laboral genera responsabilidad y litigios en aumento.</p><p class="legal-ref">LCT, art. 75 · Texto oficial (InfoLeg) →</p></a>
    <a class="legal-card" href="https://servicios.infoleg.gob.ar/infolegInternet/anexos/315000-319999/318666/norma.htm" target="_blank" rel="noopener"><span class="badge accent">Sector público</span><h3>Ley Micaela</h3><p>Capacitación en género obligatoria en el Estado — y el estándar que cada vez más empresas privadas adoptan para no quedarse atrás.</p><p class="legal-ref">Ley 27.499 (2018) · Texto oficial (InfoLeg) →</p></a>
  </div>
  <p class="stats-sources">Textos oficiales: <a href="https://normlex.ilo.org/dyn/nrmlx_es/f?p=NORMLEXPUB:12100:0::NO::P12100_INSTRUMENT_ID:3999810" target="_blank" rel="noopener">Convenio 190 de la OIT (Normlex)</a> · <a href="https://servicios.infoleg.gob.ar/infolegInternet/anexos/150000-154999/152155/texact.htm" target="_blank" rel="noopener">Ley 26.485 texto actualizado (InfoLeg)</a> · <a href="https://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=25552" target="_blank" rel="noopener">Ley de Contrato de Trabajo (InfoLeg)</a></p>
</section>

<section class="services-lite">
  <div class="section-title"><p class="eyebrow">Cómo trabajamos</p><h2>Soluciones para empresas, PyMEs e instituciones</h2></div>
  <div class="service-links">
    <a href="/servicios/protocolos-de-igualdad">Protocolos y herramientas de recepción de denuncias {IC["arrow"]}</a>
    <a href="/servicios/capacitaciones">Capacitación para equipos, mandos y RR.HH. {IC["arrow"]}</a>
    <a href="/servicios/diagnosticos-y-planes">Diagnósticos y estadísticas de género {IC["arrow"]}</a>
    <a href="/servicios/asesoria-juridica">Asesoría jurídica y acompañamiento de casos {IC["arrow"]}</a>
  </div>
</section>

{faq_ar}
""" + cta_band("Empecemos por una consulta inicial, sin compromiso",
               "Contanos la situación de tu organización y te proponemos un camino claro, viable y a medida.") + contact_section(country="ar")

page("argentina.html",
     "Prevención de violencia laboral y protocolos para empresas | GEN+ Igualdad Argentina",
     "Protocolos contra la violencia y el acoso laboral, herramientas de denuncia y capacitación bajo el estándar del Convenio 190 OIT (Ley 27.580). 25 años de reconocida experiencia en la temática.",
     "/argentina", argentina_body, extra_schema=[faq_ar_schema], hreflang=True)

print("Home + países listos.")
