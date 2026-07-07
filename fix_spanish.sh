#!/bin/bash

# 1. Arreglar el titular: doble "en" -> "de"
sed -i 's/Convertimos el cumplimiento en igualdad en una ventaja/Convertimos el cumplimiento de igualdad en una ventaja/g' pages_main.py

# 2. Cambiar voseo: "visitás" -> "visitas"
sed -i 's/¿Desde dónde nos visitás?/¿Desde dónde nos visitas?/g' pages_main.py

# 3. "Cumplí" -> "Cumple"
sed -i 's/Cumplí con la normativa de igualdad/Cumple con la normativa de igualdad/g' pages_main.py

# 4. "Prevení" -> "Prevenga"
sed -i 's/Prevení la violencia laboral/Prevenga la violencia laboral/g' pages_main.py

# 5. "Escribinos" -> "Escríbenos" (en build.py - plural neutro)
sed -i 's/Escribinos por WhatsApp/Escríbenos por WhatsApp/g' build.py

# También en el script de error
sed -i "s/Escribinos por WhatsApp o a/Escríbenos por WhatsApp o a/g" build.py

echo "✓ Cambios realizados en pages_main.py y build.py"
