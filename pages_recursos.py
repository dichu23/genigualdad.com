# -*- coding: utf-8 -*-
from build import *

def article_page(slug, tag, title, meta_desc, body_html, reading="6 min"):
    bc, bc_schema = breadcrumb([("/","Inicio"),("/recursos","Recursos"),(None,title)])
    schema = {"@context":"https://schema.org","@type":"Article","headline":title,
      "description":meta_desc,"datePublished":TODAY,"dateModified":TODAY,"inLanguage":"es",
      "author":{"@type":"Organization","name":"GEN+ Igualdad","url":BASE+"/"},
      "publisher":{"@type":"Organization","name":"GEN+ Igualdad","logo":{"@type":"ImageObject","url":BASE+"/img/logo-principal.png"}},
      "mainEntityOfPage":f"{BASE}/recursos/{slug}"}
    am = f'<meta property="article:published_time" content="{TODAY}">'
    body = f"""
<section class="page-hero compact">
  <div class="page-hero-copy">
    {bc}
    <p class="eyebrow">{tag} · Lectura de {reading}</p>
    <h1>{title}</h1>
  </div>
</section>
<article class="article-body">
{body_html}
<div class="article-footer">
  <p><strong>¿Necesitás llevar esto a la práctica en tu organización?</strong> Diseñamos protocolos, planes y capacitaciones a medida en Argentina y España.</p>
  <p style="margin-top:14px"><a class="button primary" href="/contacto">Agendar consulta</a> <a class="button dark" href="{WA_LINK}" target="_blank" rel="noopener" data-ga="contact_whatsapp">WhatsApp directo</a></p>
</div>
</article>"""
    page(f"recursos/{slug}.html", f"{title} | GEN+ Igualdad", meta_desc,
         f"/recursos/{slug}", body, extra_schema=[schema, bc_schema], og_type="article", article_meta=am)

# ============================================================ ARTÍCULO 1: Protocolo paso a paso
art1 = """
<p class="lead">Un protocolo de igualdad no es un trámite: es el procedimiento que define qué pasa en tu organización cuando alguien sufre violencia, discriminación o acoso. Estos son los componentes que no pueden faltar, en el orden en que conviene construirlos.</p>

<h2>1. Compromiso explícito de la dirección</h2>
<p>El protocolo empieza por una declaración de tolerancia cero firmada por la máxima autoridad. Sin respaldo visible de la dirección, ningún procedimiento genera la confianza necesaria para que las personas denuncien.</p>

<h2>2. Ámbito de aplicación y definiciones claras</h2>
<p>El documento debe definir a quiénes protege (toda persona vinculada a la organización: plantilla, pasantías, personal tercerizado, proveedores en las instalaciones) y qué conductas abarca, con ejemplos concretos: acoso sexual, acoso por razón de sexo o género, acoso laboral o mobbing, y discriminación. Las definiciones amplias del Convenio 190 de la OIT son la mejor referencia: incluyen conductas únicas o repetidas, el teletrabajo, los trayectos y los eventos sociales vinculados al trabajo.</p>

<h2>3. Canal de denuncia seguro y accesible</h2>
<p>Debe existir más de una vía para denunciar (una persona referente, un correo específico, un formulario), y quien recibe la denuncia no puede ser parte del conflicto. La confidencialidad se garantiza por diseño: acceso restringido a la información, expedientes codificados y compromiso de reserva firmado por quienes intervienen.</p>

<h2>4. Procedimiento con plazos y garantías</h2>
<p>El corazón del protocolo: qué pasa desde que se recibe una denuncia. Un buen procedimiento fija plazos máximos para cada etapa (recepción, evaluación inicial, investigación, resolución), garantiza que ambas partes sean escuchadas, y prevé la posibilidad de medidas cautelares —como la separación funcional de las personas involucradas— mientras dura la investigación.</p>

<h2>5. Herramientas técnicas de investigación</h2>
<p>La calidad de una investigación depende de las herramientas: un cuestionario de entrevista diseñado con criterios metodológicos permite obtener información pertinente y objetiva dentro de procesos respetuosos, confidenciales e imparciales. La improvisación en esta etapa es la principal fuente de revictimización y de nulidades.</p>

<h2>6. Protección contra represalias</h2>
<p>El protocolo debe prohibir expresamente cualquier represalia contra quien denuncia, testigos y personas que colaboren en la investigación, y prever consecuencias disciplinarias si ocurren. Este punto, más que ningún otro, determina si las personas confían o callan: recordemos que la mayoría de las víctimas nunca denuncia por miedo o desconfianza.</p>

<h2>7. Difusión y formación</h2>
<p>Un protocolo que nadie conoce no existe. Hay que comunicarlo activamente (inducción, carteleras, intranet, firma de recepción) y formar específicamente a quienes lo van a aplicar: RR.HH., mandos y comité de intervención.</p>

<h2>8. Registro, seguimiento y mejora</h2>
<p>Definí indicadores (denuncias recibidas, tiempos de resolución, medidas adoptadas) y una revisión periódica del protocolo. Los datos, debidamente anonimizados, son la mejor fuente para mejorar la prevención.</p>

<h2>El marco normativo, según tu país</h2>
<p><strong>En España</strong>, el protocolo frente al acoso sexual y por razón de sexo es obligatorio para todas las empresas (Ley Orgánica 3/2007, art. 48), y las de 50 o más personas deben integrarlo con su plan de igualdad (RD 901/2020) y sus medidas LGTBI (Ley 4/2023). <strong>En Argentina</strong> no existe una obligación general única para el sector privado, pero el Convenio 190 de la OIT (Ley 27.580) y el deber de indemnidad del empleador hacen del protocolo el estándar de diligencia exigible.</p>
"""
article_page("protocolo-de-igualdad-paso-a-paso","Guía",
 "Cómo diseñar un protocolo de igualdad, paso a paso",
 "Los 8 componentes de un protocolo eficaz contra la violencia, la discriminación y el acoso laboral: canal de denuncia, procedimiento, garantías y marco normativo de Argentina y España.",
 art1, reading="7 min")

# ============================================================ ARTÍCULO 2: Convenio 190
art2 = """
<p class="lead">El Convenio 190 de la Organización Internacional del Trabajo es el primer tratado internacional que reconoce el derecho de toda persona a un mundo del trabajo libre de violencia y acoso. Si tu organización opera en Argentina o España, ya está dentro de su alcance. Esto es lo que cambia.</p>

<h2>Qué es y desde cuándo rige</h2>
<p>Adoptado por la OIT en 2019 junto con la Recomendación 206, el Convenio 190 obliga a los Estados que lo ratifican a exigir medidas de prevención y abordaje de la violencia y el acoso en el trabajo. Argentina lo ratificó mediante la Ley 27.580 y está vigente desde 2021; España lo ratificó en 2022 y está en vigor desde 2023.</p>

<h2>Una definición más amplia que la tradicional</h2>
<p>El Convenio define la violencia y el acoso como un conjunto de comportamientos y prácticas inaceptables —o sus amenazas— que causen o puedan causar un daño físico, psicológico, sexual o económico. Dos consecuencias prácticas enormes: <strong>no exige repetición</strong> (una conducta única puede configurar violencia) y <strong>no exige intención</strong> (importa el daño, no el propósito declarado).</p>

<h2>El "mundo del trabajo" es más grande que la oficina</h2>
<p>El C190 alcanza situaciones que ocurren durante el trabajo, en relación con él o como resultado del mismo: el lugar de trabajo, pero también los espacios de descanso y comedores, los desplazamientos y viajes, los eventos sociales de la empresa, las comunicaciones por medios digitales y el teletrabajo. También protege a personas en formación, pasantías, voluntariado y a quienes buscan empleo.</p>

<h2>Qué implica para las organizaciones</h2>
<p>El estándar de diligencia que se desprende del Convenio incluye, como mínimo: una política interna de tolerancia cero, la identificación de riesgos psicosociales en la gestión de la seguridad y salud, procedimientos de denuncia e investigación con garantías, protección contra represalias, y formación e información para todo el equipo. En caso de conflicto judicial, contar con estas medidas es la principal evidencia de que la organización actuó con diligencia.</p>

<h2>La dimensión de género</h2>
<p>El Convenio dedica atención específica a la violencia y el acoso por razón de género, y pide abordar el impacto de la violencia doméstica en el mundo del trabajo: medidas como licencias, flexibilidad y protección frente al despido para personas que atraviesan situaciones de violencia son parte del nuevo estándar.</p>

<h2>Por dónde empezar</h2>
<p>Tres pasos concretos: (1) un diagnóstico de situación —qué procedimientos existen y qué percibe el equipo—, (2) un protocolo de actuación con canal de denuncias y garantías, y (3) capacitación para plantilla, mandos y RR.HH. En ese orden: sin diagnóstico, las medidas suelen quedarse en el papel.</p>
"""
article_page("convenio-190-oit","Normativa",
 "Convenio 190 de la OIT: qué cambia para tu organización",
 "El primer tratado internacional sobre violencia y acoso laboral, vigente en Argentina (Ley 27.580) y España: definición amplia, alcance del 'mundo del trabajo' y qué medidas exige.",
 art2, reading="6 min")

# ============================================================ ARTÍCULO 3: Entrevista de denuncia
art3 = """
<p class="lead">La entrevista es el momento más delicado de cualquier investigación interna por violencia o acoso: de su calidad dependen la información obtenida, los derechos de las partes y la confianza de todo el equipo en el procedimiento. Estos son los criterios técnicos esenciales.</p>

<h2>Antes: preparación y encuadre</h2>
<p>Quien entreviste debe conocer el protocolo, el expediente y los hechos denunciados antes de sentarse. Conviene definir por anticipado qué información se necesita obtener, en qué orden se abordarán los temas y qué garantías se comunicarán. El espacio importa: privado, sin interrupciones, sin la presencia de personas ajenas al procedimiento.</p>

<h2>El encuadre inicial define todo</h2>
<p>Los primeros minutos deben dedicarse a explicar el propósito de la entrevista, quiénes tendrán acceso a la información, qué implica la confidencialidad y cuáles son los próximos pasos del procedimiento. Una persona que entiende el proceso declara con más precisión y menos angustia.</p>

<h2>Durante: preguntas que abren, no que inducen</h2>
<p>La regla de oro es preferir preguntas abiertas ("contame qué pasó ese día") sobre preguntas cerradas o sugestivas ("¿te gritó fuerte?"). Las preguntas de profundización se reservan para precisar detalles ya mencionados: fechas, lugares, testigos, frecuencia. Un cuestionario diseñado con criterios metodológicos ayuda a cubrir todos los puntos relevantes sin convertir la entrevista en un interrogatorio.</p>

<h2>Evitar la revictimización</h2>
<p>No se le pide a la persona denunciante que repita su relato innecesariamente, no se emiten juicios sobre su conducta ("¿por qué no lo dijiste antes?") y no se confronta su versión con la de la otra parte en la misma entrevista. La empatía no compromete la imparcialidad: son planos distintos.</p>

<h2>Indicadores y detección de inconsistencias</h2>
<p>Quien investiga debe registrar indicadores relevantes —precisión del relato, coherencia interna, correspondencia con otros elementos del expediente— sin convertirse en detector de mentiras: las inconsistencias se exploran con preguntas de precisión, no con acusaciones. La valoración final se hace sobre el conjunto de la evidencia, nunca sobre impresiones de una sola entrevista.</p>

<h2>El registro protege a todos</h2>
<p>Un acta fiel —revisada y firmada por la persona entrevistada— protege a la denunciante, a la persona denunciada y a la organización. El expediente debe manejarse con acceso restringido y con compromiso de confidencialidad firmado por cada persona que intervenga.</p>

<h2>Después: cierre y próximos pasos</h2>
<p>Toda entrevista termina comunicando qué sigue: plazos, posibles medidas provisorias y canales de contacto. El silencio posterior a una denuncia es una de las principales causas de pérdida de confianza en los procedimientos internos.</p>

<h2>La herramienta no reemplaza la formación</h2>
<p>Un buen cuestionario en manos no capacitadas produce malas investigaciones. La formación práctica del equipo de RR.HH. —con simulación de entrevistas y análisis de casos— es la otra mitad de la ecuación: conducir entrevistas, formular preguntas, valorar la información y resguardar los derechos de todas las personas involucradas.</p>
"""
article_page("entrevista-de-denuncia","RR.HH.",
 "Cómo conducir una entrevista de denuncia: criterios técnicos para RR.HH.",
 "Preparación, encuadre, preguntas abiertas, prevención de la revictimización, registro y confidencialidad: los criterios profesionales para recibir e investigar denuncias de violencia laboral.",
 art3, reading="7 min")

# ============================================================ CHECKLIST (lead magnet)
checklist_items_html = """
<h2>Paso 1 — ¿Qué obligaciones aplican a tu empresa?</h2>
<ul class="check-list">
<li><strong>¿Tenéis 50 o más personas en plantilla?</strong> → Plan de igualdad obligatorio, negociado y registrado (RD 901/2020) + medidas planificadas LGTBI con protocolo específico (Ley 4/2023, RD 1026/2024).</li>
<li><strong>¿Vuestro convenio colectivo exige plan de igualdad?</strong> → Es obligatorio aunque tengáis menos de 50 personas.</li>
<li><strong>¿Tenéis al menos 1 persona empleada?</strong> → Protocolo frente al acoso sexual y por razón de sexo (LO 3/2007, art. 48) y registro retributivo desagregado por sexo (RD 902/2020): obligatorios para todas las empresas.</li>
<li><strong>¿Tenéis plan de igualdad vigente?</strong> → Auditoría retributiva obligatoria como parte del diagnóstico.</li>
</ul>

<h2>Paso 2 — Documentos que deberías poder mostrar hoy</h2>
<ul class="check-list">
<li>Protocolo frente al acoso aprobado, comunicado a la plantilla y con canal de denuncia activo</li>
<li>Registro retributivo actualizado del último año</li>
<li>Si corresponde: plan de igualdad inscrito en el registro oficial (REGCON), con diagnóstico previo y comisión negociadora documentada</li>
<li>Si corresponde: medidas LGTBI planificadas y protocolo frente al acoso por LGTBIfobia</li>
<li>Evidencia de formación: registros de asistencia a acciones formativas en igualdad</li>
</ul>

<h2>Paso 3 — Señales de que el cumplimiento es solo formal</h2>
<ul class="check-list">
<li>El protocolo existe pero nadie de la plantilla sabría decir cómo denunciar</li>
<li>El plan de igualdad venció o sus medidas no tienen responsable ni indicador</li>
<li>El registro retributivo se hizo una vez y no se actualizó</li>
<li>Nunca se formó a mandos ni a RR.HH. en la aplicación del protocolo</li>
</ul>

<div class="notice"><p><strong>¿Por qué importa?</strong> El incumplimiento constituye infracción grave o muy grave (LISOS), con multas que pueden superar los 200.000 € en los supuestos más graves, además de la pérdida de ayudas y de la exclusión de la contratación pública. Y un cumplimiento meramente formal no protege ante una denuncia o una inspección.</p></div>
"""

bc_ck, bc_ck_schema = breadcrumb([("/","Inicio"),("/recursos","Recursos"),(None,"Checklist: plan de igualdad")])
checklist_body = f"""
<section class="page-hero compact">
  <div class="page-hero-copy">
    {bc_ck}
    <p class="eyebrow">Recurso gratuito · España</p>
    <h1>Checklist: ¿está tu empresa obligada a tener un plan de igualdad?</h1>
    <p class="lead">Repasa en 5 minutos qué obligaciones de igualdad aplican a tu empresa, qué documentos deberías tener al día y cuáles son las señales de un cumplimiento solo formal.</p>
    <div class="hero-actions"><a class="button primary" href="/descargas/checklist-plan-de-igualdad-genigualdad.pdf" download data-ga="download_checklist">{IC["download"]} Descargar en PDF</a></div>
  </div>
</section>
<article class="article-body">
{checklist_items_html}
<div class="article-footer">
  <p><strong>¿Encontraste casillas sin marcar?</strong> Hacemos el diagnóstico, elaboramos el plan y el protocolo, y acompañamos el registro oficial. Primera consulta sin costo.</p>
  <p style="margin-top:14px"><a class="button primary" href="/contacto">Agendar consulta</a> <a class="button dark" href="/descargas/checklist-plan-de-igualdad-genigualdad.pdf" download data-ga="download_checklist">Descargar el checklist en PDF</a></p>
</div>
</article>"""

page("recursos/checklist-plan-de-igualdad.html",
     "Checklist: ¿tu empresa está obligada a tener un plan de igualdad? | GEN+ Igualdad",
     "Checklist gratuito para empresas en España: plan de igualdad (RD 901/2020), protocolo de acoso, registro retributivo y medidas LGTBI. Con PDF descargable.",
     "/recursos/checklist-plan-de-igualdad", checklist_body, extra_schema=[bc_ck_schema])

# ============================================================ RECURSOS INDEX
bc_r, bc_r_schema = breadcrumb([("/","Inicio"),(None,"Recursos")])
recursos_body = f"""
<section class="page-hero compact">
  <div class="page-hero-copy">
    {bc_r}
    <p class="eyebrow">Recursos</p>
    <h1>Guías y artículos sobre igualdad en el trabajo</h1>
    <p class="lead">Contenido práctico basado en 25 años de método: marco normativo explicado en claro, guías de implementación y criterios técnicos para RR.HH.</p>
  </div>
</section>
<section class="resources">
  <div class="blog-grid">
    <a class="blog-card" href="/recursos/protocolo-de-igualdad-paso-a-paso"><span class="tag">Guía</span><h3>Cómo diseñar un protocolo de igualdad, paso a paso</h3><p>Los 8 componentes que no pueden faltar en un protocolo eficaz: canal de denuncia, procedimiento, garantías y difusión.</p><span class="card-link">Leer guía {IC["arrow"]}</span></a>
    <a class="blog-card" href="/recursos/convenio-190-oit"><span class="tag">Normativa</span><h3>Convenio 190 de la OIT: qué cambia para tu organización</h3><p>El primer tratado internacional sobre violencia y acoso laboral, vigente en Argentina y España, explicado en claro.</p><span class="card-link">Leer artículo {IC["arrow"]}</span></a>
    <a class="blog-card" href="/recursos/entrevista-de-denuncia"><span class="tag">RR.HH.</span><h3>Cómo conducir una entrevista de denuncia</h3><p>Criterios técnicos para recibir e investigar casos con rigor, cuidado y garantías para todas las partes.</p><span class="card-link">Leer artículo {IC["arrow"]}</span></a>
    <a class="blog-card featured" href="/recursos/checklist-plan-de-igualdad"><span class="tag">Descargable · España</span><h3>Checklist: ¿tu empresa está obligada a tener un plan de igualdad?</h3><p>Obligaciones según el tamaño de tu empresa, documentos que deberías tener al día y señales de alerta. Con PDF.</p><span class="card-link">{IC["download"]} Ver checklist {IC["arrow"]}</span></a>
  </div>
</section>
""" + cta_band("¿Preferís que lo resolvamos juntos?","Una consulta inicial sin costo para analizar el punto de partida de tu organización.")

page("recursos/index.html",
     "Recursos: guías sobre igualdad, protocolos y violencia laboral | GEN+ Igualdad",
     "Guías prácticas y artículos: protocolos de igualdad paso a paso, Convenio 190 OIT, entrevistas de denuncia y checklist de obligaciones legales en España.",
     "/recursos", recursos_body, extra_schema=[bc_r_schema])

# ============================================================ CONTACTO
bc_c, bc_c_schema = breadcrumb([("/","Inicio"),(None,"Contacto")])
sched_block = ""
if SCHEDULING_LINK:
    sched_block = f"""<section class="scheduling"><div class="section-title"><p class="eyebrow">Agenda directa</p><h2>Elegí día y horario</h2></div>
<p style="text-align:center"><a class="button primary" href="{SCHEDULING_LINK}" target="_blank" rel="noopener" data-ga="schedule_click">Abrir agenda de consultas</a></p></section>"""
else:
    sched_block = "<!-- SCHEDULING: cuando exista el link de Google Calendar/Calendly, definir SCHEDULING_LINK en build.py y regenerar -->"

contacto_body = f"""
<section class="page-hero compact">
  <div class="page-hero-copy">
    {bc_c}
    <p class="eyebrow">Contacto</p>
    <h1>Hablemos de tu organización</h1>
    <p class="lead">El primer paso es una consulta inicial, sin compromiso: conocemos tu contexto y diseñamos juntos el camino hacia una organización más justa y segura.</p>
  </div>
</section>
{sched_block}
""" + contact_section()

page("contacto.html",
     "Contacto | GEN+ Igualdad — Consulta inicial sin costo",
     "Agendá una consulta inicial sin compromiso. WhatsApp, teléfono y formulario. Buenos Aires, Argentina · Santiago de Compostela, España.",
     "/contacto", contacto_body, extra_schema=[bc_c_schema])

print("Recursos + contacto listos.")
