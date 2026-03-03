import abc

class IMotor(abc.ABC):
    @abc.abstractmethod
    def avanzar(self):
        pass

class IArma(abc.ABC):
    @abc.abstractmethod
    def disparar(self):
        pass

class MotorCombustion(IMotor):
    def __init__(self, nombre, velocidad) -> None:
        self.nombre = nombre
        self.velocidad = velocidad

    def avanzar(self):
        print(f'Avanzando usando {self.nombre}')

class ArmaFuego(IArma):
    def __init__(self, nombre, municion):
        self.nombre = nombre
        self.municion = municion

    def disparar(self):
        if self.municion>0:
            print(f'(ArmaFuego)Disparando usando {self.nombre}')
            self.municion-=1
        else:
            raise ValueError('No hay munición')
        
class Arco(IArma):
    def __init__(self, nombre, municion):
        self.nombre = nombre
        self.municion = municion

    def disparar(self):
        if self.municion>0:
            print(f'(Arco)Disparando usando {self.nombre}')
            self.municion-=1
        else:
            raise ValueError('No hay munición')
        
class VehiculoBelico:
    def __init__(self, nombre: str, motor: IMotor, arma: IArma):
        self.nombre = nombre
        self.motor = motor
        self.arma = arma
    def avanzar(self):
        self.motor.avanzar()
    def disparar(self):
        self.arma.disparar()

el_motor = MotorCombustion('V8', 100)
# el_arma = ArmaFuego('AK47', 1000)
el_arma = Arco('Arco potente', 5)
el_tanque = VehiculoBelico('SuperTanque', el_motor, el_arma)
el_tanque.avanzar()
el_tanque.disparar()


