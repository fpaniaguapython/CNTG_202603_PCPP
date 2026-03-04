'''
Un closure (o clausura) es una función que "recuerda" y tiene acceso a 
las variables de su ámbito léxico (entorno superior) incluso después de 
que la función externa haya terminado de ejecutarse. Es una combinación 
de una función anidada y el entorno donde fue creada, permitiendo mantener 
estados privados y modular el código.
'''

def maquina_generadora_funciones(tipo):
    def nueva_funcion():
        print(f'Hola, soy una nueva función y soy del tipo {tipo}')
    return nueva_funcion

tipo=8
f1 = maquina_generadora_funciones(tipo)
tipo=21
f2 = maquina_generadora_funciones(tipo)
tipo=1
f3 = maquina_generadora_funciones(tipo)

f1()
f2()
f3()



