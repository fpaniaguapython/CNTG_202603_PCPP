# Opción 1. Obtención de la instancia de IComunicador mediante una función
from comunicador_factory import get_comunicador
# Opción 2. Obtención de la instancia de IComunicador mediante un método estático de una clase
#from comunicador_factory import ComunicadorFactory
from interfaz_comunicador import IComunicador

if __name__=='__main__':
    destinatario = input('Introduce el destinatario:')
    mensaje = input('Introduce el mensaje:')

    # Opción 1. Obtención de la instancia de IComunicador mediante una función
    comunicador = get_comunicador()
    # Opción 2. Obtención de la instancia de IComunicador mediante un método estático de una clase
    #comunicador = ComunicadorFactory.crear_comunicador()
    if (isinstance(comunicador, IComunicador)):
        comunicador.enviar(destinatario=destinatario, mensaje=mensaje)
    else:
        raise Exception('Me has proporcionado un objeto que no es un Comunicador')

