import pandas as pd

class SuelosParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def cargar_datos(self):
        """
        Carga el archivo Excel o CSV de resultados de laboratorio de la EEAOC.
        """
        if self.file_path.endswith('.xlsx') or self.file_path.endswith('.xls'):
            df = pd.read_excel(self.file_path)
        elif self.file_path.endswith('.csv'):
            df = pd.read_csv(self.file_path)
        else:
            raise ValueError("Formato de archivo no soportado. Debe ser Excel (.xlsx/.xls) o CSV.")
        
        return df

   
    def validar_columnas(self, df: pd.DataFrame):
        """
        Valida que las columnas obligatorias estén presentes en el archivo.
        """
        columnas_requeridas = ['Muestra', 'Cultivo', 'Materia Organica', 'pH', 'Salinidad', 'Fosforo']
        faltantes = [col for col in columnas_requeridas if col not in df.columns]
        
        if faltantes:
            raise ValueError(f"Faltan las siguientes columnas obligatorias en el archivo: {faltantes}")
        return True