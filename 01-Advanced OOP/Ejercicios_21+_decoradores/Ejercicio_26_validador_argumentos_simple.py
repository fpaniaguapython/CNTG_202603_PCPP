# Comprueba que todos los argumentos de la llamada a la
# función son enteros
def validar_argumentos(funcion_a_decorar):
    def inner_function(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise Exception('Todos los argumentos deben ser enteros')
        return funcion_a_decorar(*args, **kwargs)
    return inner_function

@validar_argumentos
def sumar(s1, s2, s3):
    return s1+s2+s3

@validar_argumentos
def restar(r1, r2):
    return r1-r2

print(sumar(1,2,3))

print(restar(1,2.8))