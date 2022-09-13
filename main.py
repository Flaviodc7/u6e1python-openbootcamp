class Vehiculo:
    color = "rojo"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 120
    cilindrada = 220

p = Coche()
print(p.color)
print(p.ruedas)
print(p.cilindrada)
print(p.velocidad)
print(p.puertas)
