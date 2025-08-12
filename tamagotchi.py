class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=50):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def mostrar_estado(self):
        print(f"{self.nombre} | Salud: {self.salud} | Felicidad: {self.felicidad} | Energía: {self.energia}")

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        self.energia -= 10
        print(f"{self.nombre} ha jugado. ¡Está más feliz!")

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        self.energia += 15
        print(f"{self.nombre} ha comido. ¡Está más saludable!")

    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(f"{self.nombre} ha sido curado. Salud mejorada.")

class TamagotchiDragon(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color, salud=150, felicidad=60, energia=80)

    def lanzar_fuego(self):
        print(f"{self.nombre} lanza fuego  y pierde 20 de energía.")
        self.energia -= 20

class TamagotchiRobot(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color, salud=200, felicidad=40, energia=100)

    def recargar(self):
        print(f"{self.nombre} se recarga  y gana 50 de energía.")
        self.energia += 50
