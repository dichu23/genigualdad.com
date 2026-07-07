#!/bin/bash

# Función para actualizar archivo HTML
update_file() {
  local file=$1
  
  # 1. Arreglar el titular: doble "en" -> "de"
  sed -i 's/Convertimos el cumplimiento en igualdad en una ventaja/Convertimos el cumplimiento de igualdad en una ventaja/g' "$file"
  
  # 2. Cambiar voseo: "visitás" -> "visitas"
  sed -i 's/¿Desde dónde nos visitás?/¿Desde dónde nos visitas?/g' "$file"
  
  # 3. "Cumplí" -> "Cumple"
  sed -i 's/Cumplí con la normativa de igualdad/Cumple con la normativa de igualdad/g' "$file"
  
  # 4. "Prevení" -> "Prevenga"
  sed -i 's/Prevení la violencia laboral/Prevenga la violencia laboral/g' "$file"
  
  # 5. "Escribinos" -> "Escríbenos"
  sed -i 's/Escribinos por WhatsApp/Escríbenos por WhatsApp/g' "$file"
  sed -i "s/Escribinos por WhatsApp o a/Escríbenos por WhatsApp o a/g" "$file"
}

# Actualizar index.html
update_file "index.html"

# Actualizar archivos en subdirectorios
for file in $(find . -name "*.html" -type f); do
  update_file "$file"
done

echo "✓ Todos los archivos HTML actualizados"
