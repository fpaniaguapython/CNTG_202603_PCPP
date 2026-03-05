def decorador_1(function_a_decorar):
    print('Decorador 1:',function_a_decorar.__name__)
    def inner_function(*args, **kwargs):
        print('Inner function de decorador 1')
        print('args de decorador_1:', args)
        resultado = function_a_decorar(*args, **kwargs)
        print('Resultado decorador_1:', resultado)
        return resultado+'*'
    return inner_function

def decorador_2(function_a_decorar):
    print('Decorador 2:',function_a_decorar.__name__)
    def inner_function(*args, **kwargs):
        print('Inner function de decorador 2')
        print('args de decorador_2:', args)
        resultado = function_a_decorar(*args, **kwargs)
        print('Resultado decorador_2:', resultado)
        return resultado+'#'
    return inner_function

@decorador_1
@decorador_2
def sumar(s1, s2):
    print('Ejecutando la función sumar')
    return s1+s2

print("PRINT FINAL:" + sumar('abc','def'))