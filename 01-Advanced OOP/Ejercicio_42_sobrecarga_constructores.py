from typing import Union

class Contenedor:
    def __init__(self, valor : Union[int,str]):
        if (isinstance(valor, int)):
            # Hacemos una inicialización
            pass
        elif (isinstance(valor, str)):
            # Hacemos otra inicialización diferente
            pass
        else:
            raise TypeError('Vamos mal')

    @classmethod
    def crear_contenedor_entero(cls, valor : int):
        return cls(valor)

x = Contenedor.crear_contenedor_entero(10)