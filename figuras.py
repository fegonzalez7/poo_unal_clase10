from abc import ABC
from math import pi
import pdb


class Figura(ABC):
    def __init__(self):
        pass

    def calcular_area(self):
        # Solo para ser estrictos, también se podría poner un pass
        # raise NotImplementedError("Subclases deben implementar area()")
        pass


class Cuadrado(Figura):
    def __init__(self, lado: float):
        # super().__init__()
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado**2


class Circulo(Figura):
    def __init__(self, radio: float):
        # super().__init__()
        self.radio = radio

    def calcular_area(self) -> float:
        return pi * self.radio**2


figura_cuadrado = Cuadrado(5)
figura_circulo = Circulo(3)

pdb.set_trace()

print(f"El area del cuadrado es: {figura_cuadrado.calcular_area()}")
print(f"El area del circulo es: {figura_circulo.calcular_area()}")
