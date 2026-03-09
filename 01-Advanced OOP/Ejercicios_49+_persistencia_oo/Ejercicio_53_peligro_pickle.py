'''
El objeto serializado puede contener código 'peligroso' que 
se ejecute a través de las funciones eval o exec -> es importante
tener en cuenta de qué fuente se obtienen los objetos serializados
y almacenados.
'''

import pickle
import os

class Cosa:
    def __init__(self, valor):
        self.valor = valor
    
    def mostrar_valor(self):
        exec(self.valor)

# Etapa 1. Creación y almacenamiento del objeto
cosa = Cosa("os.system('notepad teheformateadoeldisco.txt')")

with open('cosa.pickle',mode='wb') as fichero:
    pickle.dump(cosa, fichero)
# Etapa 2. Recuperación del objeto.

with open('cosa.pickle',mode='rb') as fichero:
    cosa = pickle.load(fichero)
    cosa.mostrar_valor()