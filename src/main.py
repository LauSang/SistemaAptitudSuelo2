import os
from src.pdf_generator import PDFReportGenerator

def main():
    print("=== Sistema de Análisis e Informe de Aptitud de Suelos (EEAOC) ===")
    
    # 1. Definir rutas de trabajo
    archivo_datos = "datos/muestras_suelo.xlsx"
    output_pdf = "test/informe_final_eeaoc.pdf"
    
    # 2. Verificar si existe el archivo de datos o usar datos de respaldo para prueba
    if not os.path.exists(archivo_datos):
        print(f"[Aviso] No se encontró '{archivo_datos}'. Usando datos de prueba por defecto...")
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
                'recomendacion': 'Nivel bajo de materia orgánica. Se recomienda incorporar abonos orgánicos o coberturas.'
            },
            {
                'variable': 'pH',
                'valor': 6.2,
                'unidad': 'pH',
                'clasificacion': 'Ligeramente ácido',
                'recomendacion': 'OK'
            },
            {
                'variable': 'Salinidad (CE)',
                'valor': 1.2,
                'unidad': 'dS/m',
                'clasificacion': 'Normal',
                'recomendacion': 'Salinidad óptima para soja (OK).'
            },
            {
                'variable': 'Fósforo Disponible',
                'valor': 6.0,
                'unidad': 'mg/kg',
                'clasificacion': 'Bajo',
                'recomendacion': 'Fósforo bajo para soja. Requerimiento de fertilización fosforada.'
            }
        ]
    else:
        print(f"Leyendo y procesando datos desde '{archivo_datos}'...")
        # Aquí conectaremos el parser y el evaluador cuando leas el Excel real

    # 3. Generar el informe PDF institucional
    print("Generando informe PDF institucional...")
    generator = PDFReportGenerator(output_pdf)
    ruta_generada = generator.generar_informe(datos_muestra, resultados)
    
    print(f"¡Proceso completado con éxito! Informe PDF guardado en: {ruta_generada}")

if __name__ == "__main__":
    main()