# Versión en inglés (/en) — qué se hizo y cómo mantenerla

## La decisión de fondo

No se usó un botón que traduce en el navegador (tipo Google Translate). Esa opción es más
rápida pero Google no indexa el resultado, así que no genera tráfico orgánico en inglés —
que es justamente para lo que sirve tener el sitio en inglés. Además destroza la
terminología jurídica (Convenio 190, plan de igualdad, deber de seguridad).

Lo que hay es **8 páginas HTML reales en `/en`**, con un botón ES/EN en el header que
linkea a la página equivalente. Cada par ES↔EN está declarado con `hreflang`, así que
Google entiende que son la misma página en dos idiomas y no las trata como contenido
duplicado.

## Alcance

Se tradujo el core comercial. Los recursos legales (Ley Micaela, reforma 27.802, etc.)
quedan solo en español a propósito: ese contenido lo busca quien busca en español.

| Español | Inglés |
|---|---|
| `/` | `/en` |
| `/servicios/protocolos-de-igualdad` | `/en/services/equality-protocols` |
| `/servicios/capacitaciones` | `/en/services/training` |
| `/servicios/diagnosticos-y-planes` | `/en/services/assessments-and-equality-plans` |
| `/servicios/asesoria-juridica` | `/en/services/legal-advisory` |
| `/servicios/investigacion` | `/en/services/social-research` |
| `/equipo` | `/en/team` |
| `/contacto` | `/en/contact` |

## El ángulo del contenido

El público es alguien mirando desde Estados Unidos. La versión en inglés no es una
traducción literal: está escrita para una casa matriz, un área legal o de compliance con
gente empleada en Argentina o España. El argumento central es que la política de
anti-harassment y EEO que tienen redactada en EE.UU. no cumple sola en ninguno de los dos
países — hace falta un procedimiento local, en español, con los canales y plazos que
define cada legislación.

Por eso la home en inglés tiene una sección de preguntas frecuentes que la versión en
español no tiene (son las preguntas que hace una casa matriz, no un cliente local), y no
tiene la sección de recursos del blog.

## Cómo se regenera

```bash
python3 build_en.py
```

`build_en.py` **solo escribe dentro de `/en/`**. No toca ninguna página en español, ni los
generadores existentes (`build.py`, `pages_*.py`). Para editar un texto en inglés, se
cambia en `build_en.py` y se vuelve a correr.

Las páginas en español se editaron a mano y de forma quirúrgica (solo el header y el
`hreflang`) — no se regeneraron, para no perder el SEO que tienen en el HTML y que no está
en los `.py`.

## Qué se tocó fuera de /en

- **8 páginas ES** (home, 5 servicios, equipo, contacto): botón `EN` en el header desktop
  y mobile, link "View in English" en el menú mobile, y `hreflang` hacia la página inglesa.
- **`styles.css`**: bloque nuevo al final con `.lang-switch` y `.header-mobile`. No se
  modificó ninguna regla existente.
- **`sitemap.xml`**: 8 URLs nuevas (31 en total).

## Datos verificados al cierre

- Convenio 190 OIT: ratificado por Argentina (en vigor feb. 2022) y por España
  (instrumento en BOE del 16/06/2022, en vigor 25/05/2023). EE.UU. no lo ratificó.
- España: plan de igualdad obligatorio, negociado y registrado para empresas de 50 o más
  personas trabajadoras (RD 901/2020, vigente); registro retributivo y auditoría
  (RD 902/2020).

## Pendientes para Eze

1. **Push desde GitHub Desktop** (git no corre desde acá).
2. Después del deploy, revisar que `/en` abra bien y que el botón ES/EN funcione en los dos
   sentidos. Vercel tiene `cleanUrls`, así que `/en/services/training` resuelve solo.
3. Correr el ping de IndexNow con las 8 URLs nuevas.
4. En Search Console, verificar que no aparezcan errores de hreflang a los pocos días.
## El formulario en inglés y los emails

El formulario de `/en` postea al mismo `/api/contact` y manda `idioma: "en"` en el payload.
El endpoint lo usa para marcar el **aviso interno** que llega a `larod63@` y `genigualdad@`:

- el asunto se prefija con `[EN]`;
- arriba del cuerpo aparece una banda oscura que dice que la consulta llegó en inglés y hay
  que responder en inglés;
- el campo "País" pasa a llamarse "Equipos en", que es lo que pregunta el formulario inglés.

Con cualquier otro valor de `idioma` (o sin el campo), el mail sale exactamente como salía
antes. El flujo en español no cambió en nada.

**Ojo con una confusión fácil:** quien completa el formulario de contacto no recibe ningún
mail automático, ni en español ni en inglés. El único mail al lead lo dispara la
calculadora de brecha salarial, que manda el informe y viaja con `copiaAlLead: true`. Si en
algún momento se quiere sumar un acuse de recibo para quien consulta, es una función nueva,
no un ajuste de idioma.
