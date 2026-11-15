
# Clase padre
class Vehiculo:
    def __init__(self, marca, modelo, anio=2020):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def actualizar_marca(self, nueva_marca):
        self.marca = nueva_marca

    def actualizar_anio(self, nuevo_anio):
        if nuevo_anio > 0:
            self.anio = nuevo_anio
        else:
            print("Error: el año debe ser mayor que cero.")

    def mostrar_datos(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.anio)


# Clase hija
class VehiculoAlquiler(Vehiculo):
    def __init__(self, marca, modelo, codigo, tarifa_diaria, anio=2020):
        super().__init__(marca, modelo, anio)
        self.codigo = codigo
        self.__tarifa_diaria = 0
        self.actualizar_tarifa(tarifa_diaria)

    def actualizar_tarifa(self, nueva_tarifa):
        if nueva_tarifa > 0:
            self.__tarifa_diaria = nueva_tarifa
        else:
            print("Error: la tarifa debe ser mayor que cero.")

    def aumentar_tarifa(self, porcentaje=10):
        if porcentaje > 0:
            self.__tarifa_diaria *= (1 + porcentaje / 100)
        else:
            print("Error: porcentaje no válido.")

    def calcular_descuento(self, dias_alquiler):
        if dias_alquiler <= 0:
            print("Error: los días deben ser mayores que cero.")
            return

        importe = self.__tarifa_diaria * dias_alquiler

        if dias_alquiler < 2:
            descuento = 0.05
        elif dias_alquiler <= 5:
            descuento = 0.10
        else:
            descuento = 0.15

        total = importe * (1 - descuento)

        self.mostrar_datos()
        print("Código:", self.codigo)
        print(f"Tarifa diaria: S/ {self.__tarifa_diaria:.2f}")
        print("Días de alquiler:", dias_alquiler)
        print(f"Importe inicial: S/ {importe:.2f}")
        print(f"Descuento: {descuento * 100:.0f}%")
        print(f"Total final: S/ {total:.2f}")
        print("----------------------------")




# Crear dos vehículos
vehiculo1 = VehiculoAlquiler("Jeep", "Commander", "V001", 100, 2022)
vehiculo2 = VehiculoAlquiler("Hyundai", "Accent", "V002", 150)

# Aplicar dos incrementos consecutivos
vehiculo1.aumentar_tarifa()
vehiculo1.aumentar_tarifa(20)

# Calcular importes con diferentes días
print("VEHÍCULO 1")
vehiculo1.calcular_descuento(1)
vehiculo1.calcular_descuento(4)
vehiculo1.calcular_descuento(7)

print("VEHÍCULO 2")
vehiculo2.calcular_descuento(3)

# Intentar asignar tarifa negativa
print("PRUEBA DE TARIFA NEGATIVA")
vehiculo1.actualizar_tarifa(-50)

# Verificar que la tarifa no cambió
vehiculo1.calcular_descuento(2)
