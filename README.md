# Unificar capas del Catastro de varios municipios
Este script permite unificar capas de la misma clase de varios municipios.

> **Este script NO es oficial**

## Funcionalidades:
- Son 2 script, uno para el catastro urbano y otro para el catastro rústico. Se ejecutan de forma independiente.
- Unifica las capas de la misma clase y las guarda en un Geopackage.
- No incluye la capa rusubparcela para evitar errores con la capa parcela.

## Características técnicas:
- Lenguaje: R.
- Uso: Para usarse en QGIS dentro de consola de Python.
- Antes de ejecutar hay que definir los siguientes parámetros dentro del código:
    - Indica en el código la ruta donde están las carpetas de los municipios que quieres unir.
    - Indica la ruta donde está el Geopackage donde quieres guardar los resultados.

## ¿Cómo suarlo?:
Guarda en una carpeta todos los municipios de quieres unir. En esta carpeta sólo puede estar el catastro urbano o rústico. No hay que descomprimir los archivos zip de las capas, pero sí descomprimir los archivos zip de los municipios. No es necesario guardar todas las capas en una misma carpeta, el script puede buscar capas dentro de las carpetas. 

Para unir el catastro rústico, elimina todas las capas *rusubparcela* de todos los municipios en las carpetas.

Abre QGIS y carga el código en el la consola Python de QGIS.

Indica en el código la ruta de las carpetas de Catastro y del Geopackage donde guardar los resultados. El script no crea el Geopackage, puedes guardarlo en uno ya existente o crear uno nuevo.

El resultado tras ejecutar el script Python se guarda en el Geopackage sin cargarse en el proyecto de QGIS.

 ## Licencia:
 Creative Commons Attribution-ShareAlike 4.0 International

 CC BY-SA 4.0

 ## Colaborativa:
 Animamos a la Comunidad para que mejore el código y nos ayude a mejorarlo.
