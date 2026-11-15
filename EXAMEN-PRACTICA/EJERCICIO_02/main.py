import operaciones

def procesar(n):
    try:
        lista = operaciones.generar_numeros(n)

        print("\nCantidad de números:", n)
        print("Lista original:", lista)

        sin_repetidos = operaciones.eliminar_duplicados(lista)
        print("Lista sin duplicados:", sin_repetidos)

        asc, desc = operaciones.ordenar_numeros(lista)
        print("Orden ascendente:", asc)
        print("Orden descendente:", desc)

        par = operaciones.mayor_par(lista)
        if par is None:
            print("No existen números pares")
        else:
            print("Mayor número par:", par)

        return lista

    except ValueError as error:
        print("Error:", error)
        return []


print("===== PRIMERA EJECUCIÓN =====")
lista1 = procesar(10)

print("\n===== SEGUNDA EJECUCIÓN =====")
lista2 = procesar(15)

print("\n===== PRUEBA DE POSICIONES =====")

try:
    print("Posición válida (2):",
          operaciones.obtener_elemento(lista1, 2))
except (IndexError, TypeError) as error:
    print("Error:", error)

try:
    print("Posición inválida (50):",
          operaciones.obtener_elemento(lista1, 50))
except (IndexError, TypeError) as error:
    print("Error:", error)

print("\n===== PRUEBA DE CANTIDAD INVÁLIDA =====")
procesar(-5)
