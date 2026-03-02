# Programar la función arrancar para que se pueda utilizar como método
# Dinámicamente añadir componentes al objeto. Los nombres no pueden tener espacios
# y deben estar en formato snake-case: Caja de cambios -> caja_de_cambios

# Dinámicamente recorremos los atributos del motor y los mostramos o los ejecutamos si
# son callable

componentes = ('Embrague', 'Caja de cambios', 'Carburador')

class Motor:
    def __init__(self, nombre):
        self.nombre = nombre

def funcion_arrancar(self):
    print(f'Soy {self.nombre} y estoy arrancando')

# Instanciación
motor = Motor('V8')
# Asignación del método a la clase
Motor.arrancar = funcion_arrancar
# Cambio de notación de los componentes - List comprenhension
componentes = [componente.lower().replace(' ','_') for componente in componentes]
# Agregar los atributos al motor
for componente in componentes:
    setattr(motor, componente, 10) # 10 es el valor que damos a los atributos

# Forma artesanal
for item in dir(motor):
    if not (item.startswith('__') and item.endswith('__')):
        # No es un atributo mágico
        if (callable(getattr(motor, item))):
            getattr(motor, item)() # Invocación al método 'item' del motor
        else:
            print(f'{item}:{getattr(motor, item)}')

# Utilizando filter
# atributos_propios = filter(lambda item : not (item.startswith('__') and item.endswith('__')), dir(motor))
# for atributo in atributos_propios:
#    print(atributo)