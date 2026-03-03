class Vehiculo(object):
    def __init__(self, nombre: str, velocidad: int, capacidad: int , autonomia: int):
        self.nombre = nombre
        self.velocidad = velocidad
        self.capacidad = capacidad
        self.autonomia = autonomia
    def arrancar(self):
        print(f'Soy {self.nombre} y estoy arrancando como Vehiculo')
    def avanzar(self):
        print(f'Soy {self.nombre} y estoy avanzando como Vehiculo')

class VehiculoTerrestre(Vehiculo):
    def __init__(self, nombre: str, velocidad: int, capacidad: int, autonomia: int, numero_ruedas: int):
        super().__init__(nombre, velocidad, capacidad, autonomia)
        self.numero_ruedas = numero_ruedas
    def aparcar(self):
        print(f'Soy {self.nombre} y estoy aparcando como VehiculoTerrestre')

class VehiculoAereo(Vehiculo):
    def __init__(self, nombre: str, velocidad: int, capacidad: int, autonomia: int, numero_alas: int):
        super().__init__(nombre, velocidad, capacidad, autonomia)
        self.numero_alas = numero_alas
    def despegar(self):
        print(f'Soy {self.nombre} y estoy despegando como VehiculoAereo')
    def avanzar(self): # SOBREESCRITURA DE MÉTODO
        super().avanzar() # Llama a la implementación de la clase base
        print(f'Soy {self.nombre} y estoy avanzando como VehiculoAereo')

seat_600 = VehiculoTerrestre(nombre='Seat 600', velocidad=100, capacidad=50, autonomia=500, numero_ruedas=4)
seat_600.arrancar()
seat_600.avanzar()

cesna = VehiculoAereo('Cesna', 150, 2, 800, 2)
cesna.despegar()
cesna.avanzar()

