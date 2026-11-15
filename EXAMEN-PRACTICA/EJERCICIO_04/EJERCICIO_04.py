
# Sistema de inventario y compras

# Diccionario de productos
productos = {
    "P001": {"nombre": "Arroz", "precio": 4.50, "cantidad": 20},
    "P002": {"nombre": "Azucar", "precio": 3.80, "cantidad": 15},
    "P003": {"nombre": "Leche", "precio": 5.00, "cantidad": 10},
    "P004": {"nombre": "Aceite", "precio": 9.50, "cantidad": 8}
}

# Funcion para mostrar productos
def mostrar_productos():
    print("\n--- INVENTARIO ---")
    for codigo, datos in productos.items():
        print(f"Codigo: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Precio: S/ {datos['precio']:.2f}")
        print(f"Stock: {datos['cantidad']}")
        print("--------------------")

# Funcion para realizar compras
def comprar_producto(codigo, cantidad):
    if codigo not in productos:
        print("Error: El producto no existe.")
        return

    if type(cantidad) != int or cantidad <= 0:
        print("Error: La cantidad debe ser un entero positivo.")
        return

    producto = productos[codigo]

    if cantidad > producto["cantidad"]:
        print("Error: Stock insuficiente.")
        return

    total = producto["precio"] * cantidad
    producto["cantidad"] -= cantidad

    print(f"Compra exitosa: {producto['nombre']}")
    print(f"Cantidad comprada: {cantidad}")
    print(f"Importe total: S/ {total:.2f}")

# Funcion para calcular valor del inventario
def valor_inventario():
    total = 0
    for producto in productos.values():
        total += producto["precio"] * producto["cantidad"]
    return total


# PRUEBAS OBLIGATORIAS

# Inventario inicial
print("INVENTARIO INICIAL")
mostrar_productos()

# Compra valida
print("\nPRUEBA 1: COMPRA VALIDA")
comprar_producto("P001", 5)

# Producto inexistente
print("\nPRUEBA 2: PRODUCTO INEXISTENTE")
comprar_producto("P005", 2)

# Cantidad superior al stock
print("\nPRUEBA 3: STOCK INSUFICIENTE")
comprar_producto("P003", 20)

# Inventario actualizado
print("\nINVENTARIO ACTUALIZADO")
mostrar_productos()

# Valor total del inventario
print(f"\nValor total del inventario: S/ {valor_inventario():.2f}")

