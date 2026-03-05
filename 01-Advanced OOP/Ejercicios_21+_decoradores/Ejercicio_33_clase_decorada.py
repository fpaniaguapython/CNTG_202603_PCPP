def contador(clase_a_decorar):
    clase_a_decorar.atributos = clase_a_decorar.__getattribute__
    def detector(self, name):
        print(f'Detectando... {name}')
        if name == 'kilometros':
            print('Se ha leído el kilometraje')
        return clase_a_decorar.atributos(self, name)
    clase_a_decorar.__getattribute__ = detector
    return clase_a_decorar

@contador
class Coche:
    def __init__(self, matricula):
        self.kilometros = 0
        self.matricula = matricula
    def arrancar(self):
        print('Arrancando')

coche = Coche('M-7797-HH')
print('El kilometraje es', coche.kilometros)
print('La matrícula es', coche.matricula)
coche.arrancar()