import shelve

######################################################
######################################################

class Jugador:
    def __init__(self, posicion, nombre):
        self.posicion = posicion
        self.nombre = nombre
        
    def __str__(self):
        return f'{self.nombre}:{self.posicion}'

######################################################
######################################################

diego = Jugador('Delantero', 'Diego')

######################################################
# Guardando el objeto a partir de su atributo __dict__
######################################################

equipo = shelve.open('seleccion.shv', flag='c')

# Guardado del jugador
equipo['10']=diego.__dict__

# print(type(datos)) # <class 'dict'>
# print(datos) # {'posicion': 'Delantero', 'nombre': 'Diego'}

equipo.close()

######################################################
# Recuperando el objeto a partir de su atributo __dict__
######################################################

equipo = shelve.open('seleccion.shv', flag='r')

datos = equipo['10']
# print(type(datos)) # <class 'dict'>
# print(datos) # {'posicion': 'Delantero', 'nombre': 'Diego'}

diego = Jugador(**datos)
print(diego)

######################################################
######################################################

equipo.close()