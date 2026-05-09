import json
import os

FILE_PATH = "data/movimientos.json"

def cargar_datos():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []

def guardar_datos(datos):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)