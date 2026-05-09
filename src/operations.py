from src.models import Movimiento
from src.storage import guardar_datos, cargar_datos

def agregar_movimiento(tipo, monto, categoria, descripcion, fecha):
    datos = cargar_datos()

    nuevo_movimiento = Movimiento(
        tipo,
        monto,
        categoria,
        descripcion,
        fecha
    )

    datos.append(nuevo_movimiento.__dict__)

    guardar_datos(datos)

def mostrar_movimientos():
    return cargar_datos()

def calcular_balance():
    datos = cargar_datos()

    balance = 0

    for movimiento in datos:

        if movimiento["tipo"] == "ingreso":
            balance += movimiento["monto"]

        elif movimiento["tipo"] == "gasto":
            balance -= movimiento["monto"]

    return balance

def filtrar_por_categoria(categoria):
    datos = cargar_datos()

    resultados = []

    for movimiento in datos:

        if movimiento["categoria"].lower() == categoria.lower():
            resultados.append(movimiento)

    return resultados