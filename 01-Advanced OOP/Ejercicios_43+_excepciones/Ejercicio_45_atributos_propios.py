# Mostrar atributos específicos de ModuleNotFoundError

try:
    import modulo_inexistente
except ModuleNotFoundError as mnfe:
    print(mnfe.name) # modulo_inexistente
    print(mnfe.path) # None

# Mostrar atributos específicos de MiException

class MiException(BaseException):
    def __init__(self, *args: object) -> None:
        self.activo = True # Atributo específico de esta Exception
        super().__init__(*args)

def funcion_de_prueba(numero):
    if (numero%2==0):
        raise MiException(numero, 'ES PAR')
    return numero+1

try:
    funcion_de_prueba(4)
except MiException as me:
    print(me.activo) # True -> Atributo específico de mi exception