import sys
import os

# Esto le avisa a Python dónde buscar el código fuente dentro del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from pdf_generator import PDFReportGenerator

# Creamos el generador y le indicamos que guarde el PDF DENTRO de la carpeta test
gen = PDFReportGenerator("test/informe_suelo_eeaoc.pdf")

datos_muestra = {
    'muestra': 'Lote 1 - Finca Experimental',
    'cultivo': 'Soja',
    'fecha': '13/10/2026'
}

resultados = [
    {
        'variable': 'Materia Orgánica',
        'valor': 1.5,
        'unidad': '%',
        'clasificacion': 'Bajo',
        'recomendacion': 'Nivel bajo. Se recomienda incorporar abonos orgánicos.'
    },
    {
        'variable': 'pH',
        'valor': 6.2,
        'unidad': 'pH',
        'clasificacion': 'Ligeramente ácido',
        'recomendacion': 'OK'
    }
]

# Ejecutamos la creación del PDF
ruta_creada = gen.generar_informe(datos_muestra, resultados)
print("¡Listo! El PDF se guardó correctamente en:", ruta_creada)