from typing import Any

# Función decoradora
def funcionDecoradora(funcion_a_decorar):
    def inner_function(*args, **kwargs):
        # CÓDIGO 'EXTRA'
        print('***Decorando con una función***')
        return funcion_a_decorar(*args, **kwargs)
    return inner_function

# Clase decoradora
class ClaseDecoradora:
    def __init__(self, funcion_a_decorar) -> None:
        self.funcion_a_decorar = funcion_a_decorar

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print('***Decorando con una clase***')
        return self.funcion_a_decorar(*args, **kwargs)

#@funcionDecoradora # Decoración con una función
@ClaseDecoradora # Decoración con una clase
def saludar(nombre):
    print(f'Hola, {nombre}')     

saludar('Python')


