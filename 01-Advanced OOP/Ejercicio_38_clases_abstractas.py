import abc

class Motor(abc.ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def arrancar(self):
        print(f'Soy {self.nombre} y estoy arrancando')
    
    @abc.abstractmethod
    def cambiar_de_marcha(self):
        pass 

class MotorManual(Motor):
    def cambiar_de_marcha(self):
        print(f'Soy {self.nombre} y estoy cambiando de marchas manualmente')

class MotorAutomatico(Motor):
    def cambiar_de_marcha(self):
        print(f'Soy {self.nombre} y estoy cambiando de marchas automática')

# motor_manual = Motor('manual') # Error, por que Motor tiene métodos abstractos

motor_manual = MotorManual('Seat 600')
motor_automatico = MotorAutomatico('Ferrari F80')

motor_manual.arrancar()
motor_manual.cambiar_de_marcha()

motor_automatico.arrancar()
motor_automatico.cambiar_de_marcha()