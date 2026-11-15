
from datetime import datetime
from functools import wraps

# Decorador para registrar fecha y hora
def registrar_pedido(funcion):
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        fecha = datetime.now()
        print("\nFecha:", fecha.strftime("%d/%m/%Y"))
        print("Hora:", fecha.strftime("%H:%M:%S"))

        resultado = funcion(*args, **kwargs)

        if resultado is not None:
            print("Operacion realizada correctamente")

        return resultado

    return envoltura


# Funcion que calcula el total con *args
@registrar_pedido
def calcular_total(*args):
    for precio in args:
        if (type(precio) not in (int, float)
                or precio <= 0):
            print("Error: precio invalido")
            return None

    return sum(args)


# Funcion que procesa pedidos con **kwargs
@registrar_pedido
def procesar_pedido(cliente, **kwargs):
    print("Cliente:", cliente)

    for producto, precio in kwargs.items():
        if (type(precio) not in (int, float)
                or precio <= 0):
            print("Error: precio invalido en", producto)
            return None

    total = sum(kwargs.values())
    print("Total del pedido: S/", total)
    return total


# PROGRAMA PRINCIPAL

print("=== SISTEMA DE PEDIDOS RAPPI ===")

# Prueba 1: Tres precios
print("\nPRUEBA 1: Tres precios")
total1 = calcular_total(15, 20, 10)
print("Total:", total1)

# Prueba 2: Seis precios
print("\nPRUEBA 2: Seis precios")
total2 = calcular_total(10, 15, 20, 8, 12, 5)
print("Total:", total2)

# Prueba 3: Pedido valido con 4 productos
print("\nPRUEBA 3: Pedido valido")
procesar_pedido(
    "Carlos",
    hamburguesa=18,
    pizza=25,
    gaseosa=5,
    papas=10
)

# Prueba 4: Pedido con precio negativo
print("\nPRUEBA 4: Pedido invalido")
procesar_pedido(
    "Ana",
    pollo=30,
    arroz=8,
    gaseosa=-5,
    ensalada=12
)
