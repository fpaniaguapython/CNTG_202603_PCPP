def escritor_simbolos(simbolo):
    def outer_function(funcion_a_decorar):
        def inner_function(*args, **kwargs):
            for i in range(10):
                print(simbolo, end='')
            print()
            return funcion_a_decorar(*args, **kwargs)
        return inner_function
    return outer_function

@escritor_simbolos(simbolo='?')
def saludar(nombre):
    print(f'Hola, {nombre}')

saludar('Fernando')