# Sistema de Análisis e Informe de Aptitud de Suelos de la EEAOC

## 1. Objetivo del proyecto

Desarrollar un sistema que permita ingresar un análisis de suelo, interpretar sus resultados según el cultivo seleccionado y generar un informe PDF con los valores analizados, su clasificación y recomendaciones agronómicas.

## 2. Usuarios del sistema

Los usuarios principales serán técnicos y trabajadores del laboratorio encargados de procesar los análisis de suelo.

## 3. Cultivos iniciales

- Cítricos
- Caña de azúcar
- Maíz
- Soja

## 4. Variables prioritarias

El sistema deberá contemplar inicialmente las siguientes variables:

- Materia orgánica
- Fósforo disponible
- pH
- Salinidad

## 5. Clasificación de resultados

Cada variable deberá poder clasificarse en cinco niveles:

- Muy bajo
- Bajo
- Normal
- Alto
- Muy alto

Los rangos de clasificación deberán ser validados por la EEAOC y podrán variar según el cultivo.

## 6. Informe PDF

El informe deberá incluir:

- Identificación de la muestra.
- Cultivo seleccionado.
- Resultados de las variables evaluadas.
- Clasificación de cada resultado.
- Recomendaciones agronómicas correspondientes.
- Vista previa del informe antes de generarlo definitivamente.

## 7. Entrada de datos

El sistema deberá adaptarse al formato Excel utilizado actualmente por el laboratorio. Antes de implementar la importación automática, se deberá examinar un archivo Excel real para identificar sus columnas, unidades y estructura.

## 8. Reglas técnicas pendientes de validación

No se deberán inventar rangos agronómicos ni recomendaciones definitivas. Los criterios técnicos deberán ser proporcionados o aprobados por la EEAOC.

## 9. Alcance inicial

El proyecto incluirá la carga o importación de datos, la interpretación de las variables prioritarias y la generación de informes PDF.

Quedan fuera del alcance inicial el muestreo de suelo, los análisis de laboratorio y la determinación autónoma de criterios agronómicos.

## 10. Pruebas

Se deberá comprobar que el sistema lea correctamente los datos, aplique los criterios aprobados, genere informes consistentes y gestione los errores de entrada.