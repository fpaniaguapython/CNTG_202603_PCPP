from typing import Any, SupportsIndex

class Videoconsola:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f'{self.marca}:{self.modelo}'
    
    def __repr__(self):
        return self.__str__()

class ListaVideoconsolas(list):
    def __init__(self, iterable=()) -> None:
        for obj in iterable:
            ListaVideoconsolas.__check_type(obj)
        super().__init__(iterable)

    def append(self, obj : Videoconsola) -> None:
        print('Ejecutando append...')
        ListaVideoconsolas.__check_type(obj)
        super().append(obj)

    def insert(self, index: SupportsIndex, object: Any) -> None:
        print('Ejecutando insert...')
        ListaVideoconsolas.__check_type(object)
        return super().insert(index, object)

    def __setitem__(self, key, value):
        print('Ejecutando __setitem__...')
        ListaVideoconsolas.__check_type(value)
        super().__setitem__(key, value)

    @staticmethod
    def __check_type(obj):
        if not isinstance(obj, Videoconsola):
            raise TypeError('La estructura solo admite objetos Videoconsola')
    

xbox_360 = Videoconsola('XBox', '360')
playstation_2 = Videoconsola('PlayStation', '2')
ds_lite = Videoconsola('DS', 'Lite')

# Construcción/Inicialización
tupla_videoconsolas = (xbox_360, playstation_2, ds_lite)
# tupla_videoconsolas = (xbox_360, playstation_2, 'Grillo')
lista_videoconsolas = ListaVideoconsolas(tupla_videoconsolas)
print(lista_videoconsolas)

#Método append
lista_videoconsolas = ListaVideoconsolas()
lista_videoconsolas.append(xbox_360) # Un punto de entrada
# lista_videoconsolas.append('Grillo') # TypeError
print(lista_videoconsolas)

#Asignación
lista_videoconsolas.append(playstation_2)
lista_videoconsolas[1]=ds_lite
# lista_videoconsolas[1]='Elefante' # TypeError
print(lista_videoconsolas)

# lista_videoconsolas.insert(1, 'Rana') # TypeError
lista_videoconsolas.insert(1, xbox_360)
print(lista_videoconsolas)

# Pendientes (OJO, habría que 'bloquear' todas las entradas posibles de datos)
lista_videoconsolas = lista_videoconsolas+[1,3,4]
print(lista_videoconsolas) # [XBox:360, XBox:360, DS:Lite, 1, 3, 4]



