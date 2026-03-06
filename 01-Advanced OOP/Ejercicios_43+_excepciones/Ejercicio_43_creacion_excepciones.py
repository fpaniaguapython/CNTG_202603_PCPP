# type: ignore

class NoEnteroError(TypeError):
    pass

class ValorNegativoError(ValueError):
    pass

def sumar_enteros_positivos(argumento_1 : int, argumento_2 : int):
    if not isinstance(argumento_1, int) or not isinstance(argumento_2, int):
        raise NoEnteroError('Debe ser entero',)
    if argumento_1<0 or argumento_2<0:
        raise ValorNegativoError('Debe ser positivo')
    return argumento_1+argumento_2

# Capturar las excepciones no relacionadas jerárquicamente de manera individual    
try:
    resultado = sumar_enteros_positivos(-3, 4)
except NoEnteroError as nee:
    print('NoEnteroError:', nee)
except ValorNegativoError as vne:
    print('ValorNegativoError:', vne)
else:
    print(resultado)

# Capturar las excepciones no relacionadas jerárquicamente de manera 'grupal'
try:
    resultado = sumar_enteros_positivos(-3, 4)
except (NoEnteroError, ValorNegativoError) as excp:
    print('Los argumentos no son válidos:', excp)
else:
    print(resultado)