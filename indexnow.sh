#!/bin/bash
# IndexNow — avisa a Bing/Copilot que cambiaron páginas de genigualdad.com
#
# Uso:
#   ./indexnow.sh                                   -> envía las 18 URLs del sitemap
#   ./indexnow.sh /contacto /recursos/calculadora-brecha-salarial   -> envía sólo esas
#
# Requisito: que https://www.genigualdad.com/26ab7c66fd1bc219966c52cb3a054cff.txt
# esté publicado (se sube junto con el resto del sitio).

set -euo pipefail

KEY="26ab7c66fd1bc219966c52cb3a054cff"
HOST="www.genigualdad.com"
KEY_LOCATION="https://${HOST}/${KEY}.txt"

# Chequeo previo: la clave tiene que estar accesible o IndexNow rechaza todo.
if ! curl -sf "$KEY_LOCATION" | grep -q "$KEY"; then
  echo "ERROR: no se puede leer la clave en $KEY_LOCATION"
  echo "Deployá el archivo ${KEY}.txt antes de correr esto."
  exit 1
fi

if [ $# -gt 0 ]; then
  PATHS=("$@")
else
  PATHS=(
    "/"
    "/espana"
    "/argentina"
    "/servicios/protocolos-de-igualdad"
    "/servicios/capacitaciones"
    "/servicios/diagnosticos-y-planes"
    "/servicios/asesoria-juridica"
    "/servicios/investigacion"
    "/equipo"
    "/recursos"
    "/recursos/protocolo-de-igualdad-paso-a-paso"
    "/recursos/protocolo-acoso-laboral-pymes"
    "/recursos/convenio-190-oit"
    "/recursos/ley-26485"
    "/recursos/deber-de-seguridad-lct-75"
    "/recursos/ley-micaela"
    "/recursos/entrevista-de-denuncia"
    "/recursos/checklist-plan-de-igualdad"
    "/recursos/checklist-convenio-190"
    "/recursos/calculadora-brecha-salarial"
    "/contacto"
  )
fi

URL_LIST=""
for p in "${PATHS[@]}"; do
  URL_LIST="${URL_LIST}\"https://${HOST}${p}\","
done
URL_LIST="${URL_LIST%,}"

PAYLOAD=$(cat <<JSON
{
  "host": "${HOST}",
  "key": "${KEY}",
  "keyLocation": "${KEY_LOCATION}",
  "urlList": [${URL_LIST}]
}
JSON
)

echo "Enviando ${#PATHS[@]} URL(s) a IndexNow..."

HTTP_CODE=$(curl -s -o /tmp/indexnow_resp -w "%{http_code}" \
  -X POST "https://api.indexnow.org/IndexNow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "$PAYLOAD")

case "$HTTP_CODE" in
  200|202) echo "OK ($HTTP_CODE) — URLs aceptadas." ;;
  400) echo "ERROR 400: formato inválido." ; cat /tmp/indexnow_resp ;;
  403) echo "ERROR 403: la clave no valida. Revisá que $KEY_LOCATION esté publicado." ;;
  422) echo "ERROR 422: alguna URL no pertenece al host declarado." ; cat /tmp/indexnow_resp ;;
  429) echo "ERROR 429: demasiadas peticiones. Esperá un rato." ;;
  *) echo "Respuesta inesperada: $HTTP_CODE" ; cat /tmp/indexnow_resp ;;
esac
