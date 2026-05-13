from datetime import date

from src.operations import (
    agregar_movimiento,
    mostrar_movimientos,
    calcular_balance,
    filtrar_por_categoria,
    resumen_por_categoria,
    resumen_financiero,
    mostrar_grafica_gastos
)

from src.utils import (
    pedir_float,
    pedir_texto
)

def menu():

    while True:

        print("\n==============================")
        print("         FINTRACK")
        print("==============================")
        print("1. Agregar ingreso")
        print("2. Agregar gasto")
        print("3. Ver movimientos")
        print("4. Ver balance")
        print("5. Filtrar por categoría")
        print("6. Resumen de gastos")
        print("7. Resumen financiero")
        print("8. Mostrar gráfica de gastos")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            monto = pedir_float("Monto: ")
            categoria = pedir_texto("Categoría: ")
            descripcion = pedir_texto("Descripción: ")

            agregar_movimiento(
                "ingreso",
                monto,
                categoria,
                descripcion,
                str(date.today())
            )

            print("\n✅ Ingreso agregado correctamente.")

        elif opcion == "2":

            monto = pedir_float("Monto: ")
            categoria = pedir_texto("Categoría: ")
            descripcion = pedir_texto("Descripción: ")

            agregar_movimiento(
                "gasto",
                monto,
                categoria,
                descripcion,
                str(date.today())
            )

            print("\n✅ Gasto agregado correctamente.")

        elif opcion == "3":

            movimientos = mostrar_movimientos()

            if not movimientos:
                print("No hay movimientos registrados.")

            else:
                for movimiento in movimientos:
                    print("\n------------------------")
                    print(f"Tipo: {movimiento['tipo']}")
                    print(f"Monto: Q{movimiento['monto']}")
                    print(f"Categoría: {movimiento['categoria']}")
                    print(f"Descripción: {movimiento['descripcion']}")
                    print(f"Fecha: {movimiento['fecha']}")
                    print("------------------------")

        elif opcion == "4":

            balance = calcular_balance()

            print(f"Balance actual: Q{balance:.2f}")

        elif opcion == "5":

            categoria = pedir_texto("Categoría a buscar: ")

            resultados = filtrar_por_categoria(categoria)

            if not resultados:
                print("No se encontraron movimientos.")

            else:
                for movimiento in resultados:
                    print("\n------------------------")
                    print(f"Tipo: {movimiento['tipo']}")
                    print(f"Monto: Q{movimiento['monto']}")
                    print(f"Categoría: {movimiento['categoria']}")
                    print(f"Descripción: {movimiento['descripcion']}")
                    print(f"Fecha: {movimiento['fecha']}")
                    print("------------------------")

        elif opcion == "6":

            resumen = resumen_por_categoria()
        
            if not resumen:
                print("\nNo hay gastos registrados.")

            else:

             print("\n===== RESUMEN DE GASTOS =====")

            for categoria, total in resumen.items():
                print(f"{categoria}: Q{total:.2f}")

        elif opcion == "7":

             resumen = resumen_financiero()

             print("\n===== RESUMEN FINANCIERO =====")
             print(f"Ingresos totales: Q{resumen['ingresos']:.2f}")
             print(f"Gastos totales: Q{resumen['gastos']:.2f}")
             print(f"Balance final: Q{resumen['balance']:.2f}")

        elif opcion == "8":
            mostrar_grafica_gastos()

        elif opcion == "9":
         print("\nGracias por usar FinTrack.")
         break

        else:
            print("\n❌ Opción inválida.")
if __name__ == "__main__":
    menu()