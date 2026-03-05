from typing import Any

# Función decoradora con argumentos
def funcion_decoradora(argumento_1, argumento_2):
    def funcion_externa(funcion_a_decorar):
        def funcion_interna(*args, **kwargs):
            print(f'Soy la función decoradora: {argumento_1}-{argumento_2}')
            return funcion_a_decorar(*args, *kwargs)
        return funcion_interna
    return funcion_externa

# Clase decoradora con argumentos
class ClaseDecoradora:
    def __init__(self, argumento_1, argumento_2) -> None:
        self.argumento_1 = argumento_1
        self.argumento_2 = argumento_2

    def __call__(self, funcion_a_decorar) -> Any:
        def funcion_interna(*args, **kwargs):
            print(f'Soy la clase decoradora: {self.argumento_1}-{self.argumento_2}')
            return funcion_a_decorar(*args, *kwargs)
        return funcion_interna
    
#@funcion_decoradora(argumento_1='uno', argumento_2='dos')
@ClaseDecoradora(argumento_1='Tres',argumento_2='Cuatro')
def saludar(nombre):
    return f'Hola, {nombre}'

print(saludar('Python'))