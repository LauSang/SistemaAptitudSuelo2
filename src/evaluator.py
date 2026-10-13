import pandas as pd

def evaluar_materia_organica(valor):
    if valor < 1.8:
        return "Bajo", "Nivel bajo de materia orgánica. Se recomienda incorporar abonos orgánicos o coberturas."
    elif 1.8 <= valor <= 2.2:
        return "Normal", "Nivel adecuado de materia orgánica en el suelo."
    else:
        return "Alto", "Nivel alto de materia orgánica."

def evaluar_fosforo(valor, cultivo):
    # Lógica basada en los umbrales del Excel para Fósforo
    umbrales = {
        "Soja": {"Bajo": 8, "Medio": 13, "Alto": 20},
        "Maíz": {"Bajo": 12, "Medio": 15, "Alto": 20},
        "Citrus": {"Bajo": 20, "Medio": 30, "Alto": 40},
        "Caña de azúcar": {"Bajo": 13, "Medio": 25, "Alto": 50}
    }
    
    if cultivo not in umbrales:
        return "Desconocido", "Cultivo no configurado para fósforo."
    
    limites = umbrales[cultivo]
    if valor < limites["Bajo"]:
        return "Bajo", f"Fósforo deficiente para {cultivo}. Requiere fertilización fosforada."
    elif valor < limites["Medio"]:
        return "Normal", f"Fósforo en rango medio para {cultivo}."
    elif valor < limites["Alto"]:
        return "Alto", f"Fósforo en buen nivel para {cultivo}."
    else:
        return "Muy Alto", f"Fósforo elevado para {cultivo}."