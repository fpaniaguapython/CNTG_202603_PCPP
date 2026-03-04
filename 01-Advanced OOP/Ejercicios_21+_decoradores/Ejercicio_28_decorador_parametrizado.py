# Crear un decorador de log que reciba como parámetro:
# un valor que determine si escribir o no escribir la fecha/hora
import logging
import datetime

def escribidor_logs(fecha_hora_activa):#El argumento indica si se debe reistrar la fecha y la hora en el log
    logging.basicConfig(level=logging.ERROR, filename='log.txt', filemode='a')
    logger = logging.getLogger()
    def outer_function(funcion_a_decorar):
        def inner_function(*args, **kwargs):
            if fecha_hora_activa:
                now = datetime.datetime.now()
                logger.error(f'{now}:{funcion_a_decorar.__name__}')
            else:
                logger.error(f'{funcion_a_decorar.__name__}')
            return funcion_a_decorar(*args, **kwargs)
        return inner_function
    return outer_function

@escribidor_logs(fecha_hora_activa=True)
def obtener_saldo(nombre):
    return len(nombre)

saldo = obtener_saldo('Iñaki')
print(saldo)

@escribidor_logs(fecha_hora_activa=False)
def sumar(s1, s2):
    return s1+s2

resultado = sumar(7,5)
print(resultado)