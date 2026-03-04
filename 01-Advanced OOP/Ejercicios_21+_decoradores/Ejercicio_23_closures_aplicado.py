'''
Un closure (o clausura) es una función que "recuerda" y tiene acceso a 
las variables de su ámbito léxico (entorno superior) incluso después de 
que la función externa haya terminado de ejecutarse. Es una combinación 
de una función anidada y el entorno donde fue creada, permitiendo mantener 
estados privados y modular el código.
'''

def gestor_persistencia(tipo=0):
    def guardar(objeto):
        if (tipo==1):
            print(f'Guardando el objeto {objeto} en fichero')
        elif (tipo==2):
            print(f'Guardando el objeto {objeto} en base de datos')
        else:
            print(f'Guardando el objeto {objeto} en la nube')
    return guardar

guardador_bbdd = gestor_persistencia(2)
guardador_fichero = gestor_persistencia(1)
guardador_cloud = gestor_persistencia()

guardador_fichero("Melón")
guardador_bbdd("Libro")



