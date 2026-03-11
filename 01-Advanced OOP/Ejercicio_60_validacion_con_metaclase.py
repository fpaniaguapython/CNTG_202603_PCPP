class MCEjecutador(type):
    def __new__(mcs, name, bases, dictionary):
        print('Ejecutando método __new__')
        # Comprobar si existe determinado atributo para añadirlo en caso contrario
        if (not 'vida_util' in dictionary):
            dictionary['vida_util'] = 0
        clase = super().__new__(mcs, name, bases, dictionary)
        print(name) # Televisor
        print(bases) # (<class '__main__.Aparato'>,)
        print(dictionary) # ... 'encender':<function ...>
        return clase

class Aparato():
    pass

class Televisor(Aparato, metaclass=MCEjecutador):
    # vida_util=10 # En caso de que no exista este atributo, se crea en la metaclase
    def __init__(self):
        print('Ejecutando método __main__')

tv = Televisor()

print(Televisor.__dict__)