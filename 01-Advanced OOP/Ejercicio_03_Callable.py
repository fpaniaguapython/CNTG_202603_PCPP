from datetime import datetime
from typing import Any

altura = 180

def saludar():
    print('Hola')

class Reloj:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        ahora = datetime.now()
        print(ahora)

mi_reloj = Reloj('Xiamo', 'a80x')

print(callable(altura)) # False
print(callable(saludar)) # True
print(callable(mi_reloj)) # True

mi_reloj()



