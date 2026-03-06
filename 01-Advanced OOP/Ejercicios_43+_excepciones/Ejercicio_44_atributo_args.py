# El atributo args de una excepción tiene los argumentos que se pasó al constructor de esta.

class MiException(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def funcion_de_prueba(numero):
    if (numero%2==0):
        raise MiException(numero, 'ES PAR')
    return numero+1

try:
    funcion_de_prueba(4)
except MiException as me:
    print(me.args) # (4, 'ES PAR') -> Tupla con los argumentos con los que construimos la excepción
