"""
Crear una clase Motor:
- Nombre
- Velocidad
- Método avanzar

Crear una clase Arma
- Nombre
- Munición
- Método disparar

Crear una clase VehiculoBelico que herede de ambas clases.

Instanciar y utilizar.
"""
class Motor:
    def __init__(self, nombre, velocidad) -> None:
        self.nombre = nombre
        self.velocidad = velocidad

    def avanzar(self):
        print(f'Avanzando... {self.nombre}')

class Arma:
    def __init__(self, nombre, municion):
        self.nombre = nombre
        self.municion = municion

    def disparar(self):
        if self.municion>0:
            print(f'Disparando... {self.nombre}')
            self.municion-=1
        else:
            raise ValueError('No hay munición')
        
class VehiculoBelico(Motor, Arma):
    def __init__(self, nombre, nombre_motor, velocidad, nombre_arma, municion) -> None:
        Motor.__init__(self, nombre_motor, velocidad)
        Arma.__init__(self, nombre_arma, municion)
        self.nombre = nombre
        
auto_belico = VehiculoBelico('SuperVehiculo', 'V80', 100, 'AK48', 1000)
auto_belico.avanzar()
auto_belico.disparar()
print(auto_belico.velocidad)