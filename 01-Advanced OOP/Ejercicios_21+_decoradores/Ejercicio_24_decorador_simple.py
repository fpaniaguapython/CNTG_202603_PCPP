def decorador_simple(funcion_a_decorar):
    print('Paso 1') # Se ejecuta cuando se decora la función
    def inner_function(*args, **kwars): # Este bloque se ejecuta cuando se ejecuta la función
        print('Paso 3')
        print('***********************************')
        retorno = funcion_a_decorar(*args, **kwars)
        return retorno
    print('Paso 2') # Se ejecuta cuando se decora la función
    return inner_function

@decorador_simple
def saludador(nombre, mensaje):
    print(f'Holi, {nombre}, {mensaje}')
    return True

respuesta = saludador('Álvaro', '¿Cómo estás?')
print(respuesta)

@decorador_simple
def mostrar_listado(lista):
    for item in lista:
        print(item)

lista = ['HP', 'Lenovo', 'Dell']
mostrar_listado(lista)