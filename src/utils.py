def pedir_float(mensaje):

    while True:

        try:
            return float(input(mensaje))

        except ValueError:
            print("Ingresa un número válido.")

def pedir_texto(mensaje):
    return input(mensaje).strip()