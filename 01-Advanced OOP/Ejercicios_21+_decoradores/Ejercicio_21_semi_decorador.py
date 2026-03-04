# Esta función recibe una función como argumento
def funcion_decoradora(funcion_a_decorar):
    print('Soy la función decoradora y estoy haciendo algo extra...')
    return funcion_a_decorar

def mi_funcion():
    print('Soy mi_funcion')

# Pasando una función como argumento y recibiendo una función
funcion_decorada = funcion_decoradora(mi_funcion)
input('Pulsa Enter para continuar')
# Ejecutando la función que nos devolvió la llamada anterior
funcion_decorada()

