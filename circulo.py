class Circulo:
    def __init__(self, radio, color, nombre):
        self.radio = radio
        self.color = color
        self.nombre = nombre

    def calcular_area(self):
        return 3.141592653589793 * (self.radio ** 2)

mi_circulo = Circulo(radio=5, color="azul", nombre="Círculo Azul")

print(f"El radio de {mi_circulo.nombre} es: {mi_circulo.radio}")
print(f"El color de {mi_circulo.nombre} es: {mi_circulo.color}")
area = mi_circulo.calcular_area()
print(f"El área de {mi_circulo.nombre} es: {area:.2f}")