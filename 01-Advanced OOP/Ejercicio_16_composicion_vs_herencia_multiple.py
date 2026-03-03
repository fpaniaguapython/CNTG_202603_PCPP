class Motor:
    def __init__(self, nombre, velocidad) -> None:
        self.nombre = nombre
        self.velocidad = velocidad

    def avanzar(self):
        print(f'Avanzando usando {self.nombre}')

class Arma:
    def __init__(self, nombre, municion):
        self.nombre = nombre
        self.municion = municion

    def disparar(self):
        if self.municion>0:
            print(f'Disparando usando {self.nombre}')
            self.municion-=1
        else:
            raise ValueError('No hay munición')
        
class VehiculoBelico:
    def __init__(self, nombre: str, motor: Motor, arma: Arma):
        self.nombre = nombre
        self.motor = motor
        self.arma = arma
    def avanzar(self):
        self.motor.avanzar()
    def disparar(self):
        self.arma.disparar()

el_motor = Motor('V8', 100)
el_arma = Arma('AK47', 1000)
el_tanque = VehiculoBelico('SuperTanque', el_motor, el_arma)
el_tanque.avanzar()
el_tanque.disparar()


