def funcion_sin_argumentos_ni_retorno():
    pass

def funcion_con_un_argumento_sin_retorno(argumento_1):
    pass

def funcion_con_varios_argumentos_sin_retorno(argumento_1, argumento_2, argumento_3):
    pass

def funcion_con_un_argumento_con_retorno(argumento_1):
    return "resultado"

funcion_con_varios_argumentos_sin_retorno(10, 20, 30) # Argumentos posicionales
funcion_con_varios_argumentos_sin_retorno(argumento_2=20, argumento_3=30, argumento_1=10) # Argumentos posicionales
funcion_con_varios_argumentos_sin_retorno(10, argumento_3=30, argumento_2=10) # Los posicionales SIEMPRE al principio

def funcion_con_valores_por_defecto(arg_1, arg_2, arg_3=12):
    print(arg_1, arg_2, arg_3)

funcion_con_valores_por_defecto(15, 2)
funcion_con_valores_por_defecto(15, 2, 8)

def sumar(*sumando): # Permite recoger un número indeterminado de argumentos posicionales
    print(type(sumando))
    print(sumando)

sumar() # <class 'tuple'> ()
sumar(1) # <class 'tuple'> (1,)
sumar(1,8) # <class 'tuple'> (1,8)
sumar(1,8,8,10,-5,100,200,400) # <class 'tuple'> (1, 8, 8, 10, -5, 100, 200, 400)

def calcular(**kwargs) :
    print(type(kwargs))
    print(kwargs)

calcular() # <class 'dict'> {}
calcular(posicion=1) # <class 'dict'> {'posicion': 1}
calcular(posicion=1, longitud=10, peso=3.2) # <class 'dict'> {'posicion': 1, 'longitud': 10, 'peso': 3.2}


def funcion_variada(*args, arg_1, arg_3,  **kwargs):
    pass

# funcion_variada(3, 2, 1, valor=10, peso=80) # ERROR, los tres argumentos posicionales se van a *args y los argumentos arg_1 y arg_2 no tendrían valor
funcion_variada(3, arg_1=2, arg_3=1, valor=10, peso=80)


# ************************************************************
# ************************************************************
# ************************************************************
# función f1 que recibe *args (números enteros)
# Llama a f2 y le pasa los argumentos que ha recibido
def f1(*args):
    print('f1:', len(args)) # 4
    #f2(args) # Pasa una tupla con 4 elementos 
    f2(*args) # Pasa los 4 elementos de la tupla

# funcion f2 que recibe *args (números enteros)
# Mostrar la longitud de args ¿cuántos elementos ha recibido?
def f2(*args):
    print('f2:', len(args)) # 1 (si la llamada se hace con args) ; # 4 (si la llamada se hace con *args)

f1(10, 20, 40, 80)


# ************************************************************
# ************************************************************
# ************************************************************



