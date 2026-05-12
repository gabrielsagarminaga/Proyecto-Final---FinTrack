from src.models import Movimiento
from src.storage import guardar_datos, cargar_datos
import matplotlib.pyplot as plt

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

def filtrar_por_categoria_recursivo(movimientos, categoria, indice=0, resultados=None):
    if resultados is None:
        resultados = []

    if indice >= len(movimientos):
        return resultados

    movimiento = movimientos[indice]

    if movimiento["categoria"].lower() == categoria.lower():
        resultados.append(movimiento)

    return filtrar_por_categoria_recursivo(movimientos, categoria, indice + 1, resultados)

def filtrar_por_categoria(categoria):
    datos = cargar_datos()
    return filtrar_por_categoria_recursivo(datos, categoria)

def resumen_por_categoria():
    datos = cargar_datos()
    resumen = {}

    for movimiento in datos:
        categoria = movimiento["categoria"].lower()
        monto = movimiento["monto"]

        if movimiento["tipo"] == "gasto":
            if categoria in resumen:
                resumen[categoria] += monto
            else:
                resumen[categoria] = monto

def resumen_financiero():
    datos = cargar_datos()

    total_ingresos = 0
    total_gastos = 0

    for movimiento in datos:

        if movimiento["tipo"] == "ingreso":
            total_ingresos += movimiento["monto"]

        elif movimiento["tipo"] == "gasto":
            total_gastos += movimiento["monto"]

    balance = total_ingresos - total_gastos

    return {
        "ingresos": total_ingresos,
        "gastos": total_gastos,
        "balance": balance
    }

def resumen_por_categoria():
    datos = cargar_datos()
    resumen = {}

    for movimiento in datos:
        if movimiento["tipo"] == "gasto":
            categoria = movimiento["categoria"].lower()
            monto = movimiento["monto"]

            if categoria in resumen:
                resumen[categoria] += monto
            else:
                resumen[categoria] = monto

    return resumen

def mostrar_grafica_gastos():
    resumen = resumen_por_categoria()

    if not resumen:
        print("No hay datos para mostrar.")
        return

    categorias = list(resumen.keys())
    montos = list(resumen.values())

    plt.figure(figsize=(8, 5))
    plt.bar(categorias, montos)
    plt.title("Gastos por Categoría")
    plt.xlabel("Categorías")
    plt.ylabel("Monto en Quetzales")
    plt.tight_layout()
    plt.show()