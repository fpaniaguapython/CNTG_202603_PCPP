# Crear un decorador que escriba un registro de log cada vez que se ejecuten las funciones que decora
# Opcionalmente escribimos la fecha y la hora de la ejecución
# Opcionalmente escribimos el nombre de la función que se ejecutó
import logging
import datetime

def escribidor_logs(funcion_a_decorar):
    logging.basicConfig(level=logging.ERROR, filename='fichero_actividad.log', filemode='a')
    logger = logging.getLogger()
    def inner_function(*args, **kwargs):
        now = datetime.datetime.now()
        logger.error(f'{now}:{funcion_a_decorar.__name__}')
        return funcion_a_decorar(*args, **kwargs)
    return inner_function

@escribidor_logs
def obtener_saldo(nombre):
    return len(nombre)

saldo = obtener_saldo('Iñaki')
print(saldo)

@escribidor_logs
def sumar(s1, s2):
    return s1+s2

resultado = sumar(7,5)
print(resultado)