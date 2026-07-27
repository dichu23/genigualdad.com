# -*- coding: utf-8 -*-
from build import *

def service_page(slug, name, meta_title, meta_desc, hero_lead, incluye, para_quien, entregables, foto, foto_alt, related, extra=""):
    bc, bc_schema = breadcrumb([("/","Inicio"),("/#servicios","Servicios"),(None,name)])
    schema = {"@context":"https://schema.org","@type":"Service","name":name,
              "provider":{"@type":"ProfessionalService","name":"GEN+ Igualdad","url":BASE+"/"},
              "areaServed":["Argentina","España"],"description":meta_desc,
              "url":f"{BASE}/servicios/{slug}"}
    inc = "".join(f'<li>{i}</li>' for i in incluye)
    ent = "".join(f'<li>{e}</li>' for e in entregables)
    body = f"""
<section class="page-hero compact">
  <div class="page-hero-copy">
    {bc}
    <p class="eyebrow">Servicio</p>
    <h1>{name}</h1>
    <p class="lead">{hero_lead}</p>
    <div class="hero-actions"><a class="button primary" href="/contacto">Agendar consulta</a><a class="button ghost" href="{WA_LINK}" target="_blank" rel="noopener" data-ga="contact_whatsapp">Consultar por WhatsApp</a></div>
  </div>
</section>
<section class="service-detail">
  <div class="service-detail-grid">
    <div>
      <h2>Qué incluye</h2>
      <ul class="check-list">{inc}</ul>
      <h2 style="margin-top:40px">Para quienes</h2>
      <p>{para_quien}</p>
      {extra}
    </div>
    <aside class="service-side">
      {img(foto, foto_alt)}
      <div class="service-side-box">
        <h4>Entregables</h4>
        <ul class="dash-list">{ent}</ul>
      </div>
      <div class="service-side-box">
        <h4>Modalidad</h4>
        <p>Presencial, virtual o híbrida, en Argentina y España, según el contexto y los objetivos de cada organización.</p>
      </div>
    </aside>
  </div>
</section>
""" + cta_band("¿Este servicio responde a lo que tu organización necesita?",
               "En una consulta inicial sin costo definimos alcance, plazos y presupuesto a medida.") + f"""
<section class="related-strip"><p class="eyebrow">También puede interesarte</p><div class="service-links">{related}</div></section>"""
    page(f"servicios/{slug}.html", meta_title, meta_desc, f"/servicios/{slug}", body,
         extra_schema=[schema, bc_schema])

rel = lambda *items: "".join(f'<a href="{u}">{t} {IC["arrow"]}</a>' for u,t in items)

# --- 1. Protocolos ---
service_page(
 "protocolos-de-igualdad", "Protocolos de igualdad y canales de denuncia",
 "Protocolos contra el acoso y la violencia laboral | GEN+ Igualdad",
 "Diseño e implementación de protocolos frente a la violencia, la discriminación y el acoso laboral: canales de denuncia seguros, herramientas de recepción e investigación y medidas de protección.",
 "Un protocolo eficaz no es un documento en un cajón: es un procedimiento claro, conocido por todo el equipo, con canales seguros y garantías reales para quien denuncia. Lo diseñamos a medida de tu organización y del marco normativo de tu país.",
 ["Diagnóstico de la situación actual y de los procedimientos existentes",
  "Redacción del protocolo frente a la violencia, la discriminación y el acoso, adaptado a la normativa aplicable (Convenio 190 OIT en Argentina; LO 3/2007 y normativa de desarrollo en España)",
  "Diseño de canales de denuncia seguros y confidenciales",
  "Herramienta de recepción e investigación de denuncias: cuestionario de entrevista con criterios metodológicos y guía de aplicación",
  "Medidas de protección para denunciantes y garantías de no represalia",
  "Plan de difusión interna y capacitación del equipo que aplicará el protocolo"],
 "Empresas, PyMEs, organismos públicos, universidades y organizaciones sociales que necesitan crear su protocolo desde cero, actualizar uno existente o profesionalizar la recepción e investigación de denuncias.",
 ["Protocolo de actuación listo para aprobar y difundir",
  "Cuestionario de recepción de denuncias + guía metodológica",
  "Capacitación del equipo responsable de aplicarlo",
  "Informe final confidencial con recomendaciones"],
 "servicios-1", "Equipo de trabajo elaborando un protocolo de igualdad",
 rel(("/servicios/capacitaciones","Capacitación en entrevista de denuncia"),("/recursos/protocolo-de-igualdad-paso-a-paso","Guía: protocolo paso a paso")),
 extra="""<h2 style="margin-top:40px">Cómo trabajamos</h2>
 <p>La eficacia de un mecanismo de denuncias depende de dos factores: contar con herramientas técnicas adecuadas y con profesionales capacitados para aplicarlas. Por eso cada protocolo se entrega junto con la formación del equipo que lo va a usar: conducir entrevistas, formular preguntas, identificar indicadores relevantes, valorar la información y resguardar los derechos de todas las personas involucradas.</p>""")

# --- 2. Capacitaciones ---
service_page(
 "capacitaciones", "Capacitaciones y talleres",
 "Capacitación en igualdad de género y prevención de violencia laboral | GEN+ Igualdad",
 "Talleres teórico-prácticos: igualdad de género en entornos laborales, prevención de la violencia de género en empresas y formación de RR.HH. en entrevista de denuncia.",
 "Formación teórico-práctica con simulaciones reales, análisis de casos y lenguaje claro. Tres programas probados, adaptables a cada organización, dictados por especialistas con más de 25 años de experiencia.",
 ["<strong>Igualdad de género en entornos laborales</strong> — nuestro taller insignia: 5 encuentros sincrónicos más trabajo asincrónico guiado. Sexo-género y estereotipos; micromachismos cotidianos y comunicación respetuosa; buenas y nuevas masculinidades; acoso sexual y por razón de sexo; empatía, escucha activa e identificación temprana de conflictos; planes de igualdad; igualdad retributiva, conciliación y sesgos en la selección; el caso de negocio de la igualdad; compromisos y plan de acción.",
  "<strong>Prevención de la violencia de género en las empresas</strong> — formación para plantilla, mandos medios y dirección: concepto y normativa, estereotipos y casos reales, indicadores de detección, consecuencias para las personas y la empresa, y acciones de prevención.",
  "<strong>Formación de RR.HH. en entrevista de denuncia</strong> — jornada intensiva presencial: técnicas de entrevista, detección de inconsistencias, preguntas de profundización, confidencialidad, análisis de casos y simulación de entrevistas.",
  "Sensibilización comunitaria, formación de formadores y charlas para líderes y decisores"],
 "Personal de empresas, mandos medios, dirección, equipos de RR.HH., instituciones públicas y organizaciones sociales. Grupos reducidos o programas escalados para organizaciones grandes.",
 ["Programa y materiales de cada encuentro",
  "Ejercicios prácticos, casos y role playing",
  "Informe de evaluación final grupal, confidencial",
  "Certificado de participación"],
 "servicios-2", "Taller de capacitación en igualdad de género",
 rel(("/servicios/protocolos-de-igualdad","Protocolos de igualdad"),("/recursos/entrevista-de-denuncia","Artículo: la entrevista de denuncia")),
 extra="""<h2 style="margin-top:40px">Modalidades</h2>
 <p><strong>Presencial:</strong> interacción auténtica, simulaciones reales, lenguaje no verbal y feedback inmediato (recomendada para temáticas sensibles). <strong>Virtual:</strong> encuentros en vivo accesibles desde cualquier punto del país. <strong>Híbrida:</strong> jornadas presenciales clave con seguimiento virtual, equilibrando profundidad y alcance.</p>""")

# --- 3. Diagnósticos y planes ---
service_page(
 "diagnosticos-y-planes", "Diagnósticos y planes de igualdad",
 "Diagnósticos organizacionales y planes de igualdad | GEN+ Igualdad",
 "Diagnósticos de brechas de género con estándar estadístico INDEC, planes de igualdad con metas medibles y registro oficial en España (RD 901/2020), e informes basados en evidencia.",
 "Ninguna medida funciona sin un buen diagnóstico. Aplicamos el rigor de 25 años de estadística oficial para medir brechas reales y convertirlas en planes con metas, plazos e indicadores verificables.",
 ["Diagnóstico organizacional: encuestas, entrevistas en profundidad y grupos focales",
  "Análisis de brechas de igualdad: retribución, acceso a puestos de decisión, conciliación, selección y promoción",
  "Plan de igualdad con medidas, metas medibles, cronograma e indicadores de seguimiento",
  "En España: diagnóstico y plan conforme al RD 901/2020, negociación con la representación legal y acompañamiento del registro oficial; registro retributivo y auditoría (RD 902/2020)",
  "Elaboración y análisis de estadísticas de género a medida",
  "Informes con recomendaciones basadas en evidencia"],
 "Empresas obligadas a registrar su plan de igualdad en España, organizaciones que quieren medir y cerrar sus brechas en Argentina, e instituciones que necesitan datos sólidos para decidir.",
 ["Informe de diagnóstico con evidencia y brechas priorizadas",
  "Plan de igualdad completo, listo para negociar y registrar",
  "Tablero de indicadores de seguimiento",
  "Presentación ejecutiva para la dirección"],
 "servicios-3", "Análisis de datos y diagnóstico organizacional",
 rel(("/espana","Obligaciones legales en España"),("/servicios/asesoria-juridica","Asesoría jurídica")))

# --- 4. Asesoría jurídica ---
service_page(
 "asesoria-juridica", "Asesoría jurídica con perspectiva de género",
 "Asesoría jurídica en igualdad y violencia laboral | GEN+ Igualdad",
 "Asesoramiento legal con perspectiva de género para organizaciones y personas: adecuación normativa en Argentina y España, acompañamiento de casos y diseño de políticas internas.",
 "El derecho es la columna vertebral de cualquier política de igualdad. Nuestro equipo jurídico, con formación en Argentina y España, traduce la norma en procedimientos que protegen a las personas y a la organización.",
 ["Adecuación normativa integral: revisión de políticas, reglamentos y procedimientos frente al marco legal aplicable",
  "Asesoramiento en la gestión de casos de violencia, discriminación y acoso, resguardando los derechos de todas las partes",
  "Protección jurídica de víctimas de violencia basada en género",
  "Diseño de políticas organizacionales y cláusulas contractuales con perspectiva de género",
  "Coaching jurídico para liderazgo inclusivo y toma de decisiones",
  "Seguimiento de casos y representación según jurisdicción"],
 "Direcciones de RR.HH. y legales, comités de igualdad, organizaciones que enfrentan un caso concreto y personas que necesitan protección jurídica especializada.",
 ["Dictámenes e informes jurídicos",
  "Políticas y procedimientos revisados o redactados",
  "Hoja de ruta de adecuación normativa",
  "Acompañamiento documentado de casos"],
 "genmas-1", "Asesoramiento jurídico con perspectiva de género",
 rel(("/servicios/protocolos-de-igualdad","Protocolos de igualdad"),("/equipo","Conocer al equipo")),
 extra="""<h2 style="margin-top:40px">Quién lo lidera</h2>
 <p>José Ignacio Sampedro, abogado con Máster en Derecho Transnacional de la Empresa y las Tecnologías Digitales (Universidad de Santiago de Compostela), integró la Unidad de Mujeres, Géneros y Diversidad del Ministerio de Seguridad de la Nación entre 2009 y 2023, y asesora a víctimas de violencia basada en género en ejercicio independiente.</p>""")

# --- 5. Investigación social ---
service_page(
 "investigacion", "Investigación social aplicada",
 "Investigación social: encuestas de violencia de género, grupos focales e indicadores | GEN+ Igualdad",
 "Encuestas de violencia de género en poblaciones que las estadísticas oficiales no alcanzan, grupos focales, indicadores y estudios cualitativos y cuantitativos con estándar de estadística oficial.",
 "Las buenas decisiones se apoyan en datos que existen. Producimos evidencia donde no llegan las estadísticas oficiales, con el rigor de 25 años en estadística pública (INDEC) y en evaluación de proyectos internacionales (ONU Mujeres · UN Trust Fund).",
 ["Encuestas de violencia de género en poblaciones que las estadísticas oficiales no alcanzan",
  "Grupos focales y entrevistas en profundidad",
  "Elaboración de indicadores y estadísticas de género a medida",
  "Estudios cualitativos y cuantitativos: diseño metodológico, trabajo de campo, análisis y difusión",
  "Evaluación de programas y políticas con perspectiva de género",
  "Informes con recomendaciones basadas en evidencia"],
 "Administraciones públicas, organismos internacionales, universidades, fundaciones y organizaciones sociales que necesitan datos sólidos sobre violencia de género y desigualdades; y empresas que quieren medir con rigor su punto de partida.",
 ["Diseño metodológico e instrumentos de relevamiento",
  "Base de datos documentada",
  "Informe de resultados con indicadores",
  "Presentación ejecutiva de hallazgos"],
 "territorio-fondo", "Trabajo de campo en investigación social",
 rel(("/servicios/diagnosticos-y-planes","Diagnósticos y planes de igualdad"),("/equipo","Conocer al equipo")))

# ============================================================ EQUIPO
bc_eq, bc_eq_schema = breadcrumb([("/","Inicio"),(None,"Equipo")])
team_schema = [{"@context":"https://schema.org","@type":"Person","name":n,"jobTitle":j,"worksFor":{"@type":"Organization","name":"GEN+ Igualdad"}}
 for n,j in [("María Rosa Diez de Ulzurrun","Directora ejecutiva"),("Laura Fabiana Rodríguez","Directora de proyectos"),("José Ignacio Sampedro","Director de asuntos jurídicos")]]

equipo_body = f"""
<section class="page-hero compact">
  <div class="page-hero-copy">
    {bc_eq}
    <p class="eyebrow">Nuestro equipo</p>
    <h1>Especialistas con respaldo institucional</h1>
    <p class="lead">Credenciales que respaldan cada intervención: estadística oficial, academia, organismos internacionales y ejercicio jurídico en Argentina y España.</p>
  </div>
</section>
<section class="team-full">
  <article class="bio">
    <div class="bio-photo">{img("panel-maria-rosa","María Rosa Diez de Ulzurrún")}</div>
    <div class="bio-copy">
      <h2>María Rosa Diez de Ulzurrun</h2><h4>Directora ejecutiva</h4>
      <p>Socióloga y Magíster en Políticas Sociales (Universidad de Buenos Aires). Coordinadora del Registro Único de Casos de Violencia contra las Mujeres (RUCVM). Docente de la UNTREF y profesora en cursos de grado y posgrado sobre violencia de género, acoso en el ámbito laboral y producción de estadísticas con perspectiva de género.</p>
      <p>Especialista en diseño, análisis y difusión de información para las políticas públicas de género. Recorrió el país brindando talleres en el marco del RUCVM, formando a funcionarios, líderes comunitarios y organizaciones de la sociedad civil.</p>
      <p class="credentials">UBA · INDEC · UNTREF · RUCVM</p>
    </div>
  </article>
  <article class="bio reverse">
    <div class="bio-photo">{img("equipo1","Laura Fabiana Rodríguez")}</div>
    <div class="bio-copy">
      <h2>Laura Fabiana Rodríguez</h2><h4>Directora de proyectos</h4>
      <p>Geógrafa y Magíster en Género, Sociedad y Políticas (FLACSO). Coordinadora de la Unidad de Género del INDEC. Capacitadora en talleres y cursos sobre sensibilización y prevención de la violencia basada en género.</p>
      <p>Evaluadora de proyectos de organizaciones de la sociedad civil para la prevención y erradicación de la violencia contra las mujeres del Fondo Fiduciario de las Naciones Unidas para Eliminar la Violencia contra la Mujer (UN Trust Fund).</p>
      <p class="credentials">FLACSO · INDEC · ONU Mujeres · UN Trust Fund</p>
    </div>
  </article>
  <article class="bio">
    <div class="bio-photo">{img("equipo3","José Ignacio Sampedro")}</div>
    <div class="bio-copy">
      <h2>José Ignacio Sampedro</h2><h4>Director de asuntos jurídicos</h4>
      <p>Abogado con Máster en Derecho Transnacional de la Empresa y las Tecnologías Digitales (Universidad de Santiago de Compostela). Especialista en perspectiva de género aplicada al ámbito jurídico.</p>
      <p>Integró la Unidad de Mujeres, Géneros y Diversidad del Ministerio de Seguridad de la Nación (2009–2023) y la Fiscalía Nacional en lo Criminal de Instrucción N.º 31 (2006–2009). Actualmente ejerce de manera independiente, asesorando a víctimas de violencia basada en género, y lidera la operación de Gen+ Igualdad en España.</p>
      <p class="credentials">USC · Ministerio de Seguridad de la Nación · Fiscalía Nacional</p>
    </div>
  </article>
</section>
""" + cta_band("Un equipo senior, sin intermediarios","Quienes diseñan la propuesta son quienes la ejecutan. Conversemos sobre tu organización.")

page("equipo.html",
     "Nuestro equipo | GEN+ Igualdad",
     "María Rosa Diez de Ulzurrun (INDEC, UNTREF, RUCVM), Laura Rodríguez (FLACSO, ONU Mujeres) y José Ignacio Sampedro (USC): el equipo detrás de GEN+ Igualdad.",
     "/equipo", equipo_body, extra_schema=team_schema + [bc_eq_schema])

print("Servicios + equipo listos.")
