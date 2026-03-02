'''
Crear una clase Empresa (Nombre, País, Activa)
Métodos:
- mostrar_estado (muestra el nombre y el valor de Activa)

Crear una clase EmpresaFamiliar que hereda de Empresa (Nombre, País, Apellido Familiar)
- Una empresa familiar SIEMPRE está Activa
- mostrar_situacion (muestra el país y ejecuta mostrar_estado)
'''
class Empresa:
    def __init__(self, nombre, pais, activa):
        self.nombre = nombre
        self.pais = pais
        self.activa = activa
    def mostrar_estado(self):
        print(f'Nombre:{self.nombre}. Activa:{self.activa}')

class EmpresaFamiliar(Empresa):
    def __init__(self, nombre, pais, apellido_familiar):
        super().__init__(nombre, pais, True)
        self.apellido_familiar = apellido_familiar
    def mostrar_situacion(self):
        print(f'Pais:{self.pais}')
        self.mostrar_estado()

mi_empresa = EmpresaFamiliar('Amaçon', 'España', 'López')
mi_empresa.mostrar_situacion()