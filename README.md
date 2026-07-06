# genigualdad.com

Sitio estático multipágina de GEN+ Igualdad, deployado en Vercel.

## Estructura
- `*.html` — páginas generadas (NO editar a mano: editar los `pages_*.py` y regenerar)
- `build.py` — componentes compartidos (head, header, footer, contacto, FAQ, breadcrumbs)
- `pages_main.py` / `pages_services.py` / `pages_recursos.py` — contenido de cada página
- `img/` — imágenes optimizadas (WebP)
- `descargas/` — lead magnets (PDF)
- `api/contact.js` — formulario de contacto (Resend, honeypot, reply_to)

## Regenerar el sitio tras editar contenido
```
python3 -c "import pages_main, pages_services, pages_recursos"
```

## Configurar el link de agenda
1. Crear "Espacios de citas" en Google Calendar (o Calendly gratuito)
2. Pegar el link en `SCHEDULING_LINK` dentro de `build.py`
3. Regenerar (comando de arriba) y pushear

## Antes de deployar (pendiente)
- [ ] Activar Email Forwarding en Porkbun: contacto@genigualdad.com → genigualdad@gmail.com
- [ ] Crear link de agenda y pegarlo en SCHEDULING_LINK
