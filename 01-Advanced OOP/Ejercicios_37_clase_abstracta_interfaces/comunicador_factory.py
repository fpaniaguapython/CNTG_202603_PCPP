from interfaz_comunicador import IComunicador
from comunicador_email import ComunicadorPorEmail
from comunicador_whatsapp import ComunicadorPorWhatsapp

# Opción 1. Se obtiene la instancia a través de una función
def get_comunicador() -> IComunicador:
    tipo = get_tipo_comunicador()

    match tipo:
        case 0:
            return ComunicadorPorEmail()
        case 1:
            return ComunicadorPorWhatsapp()
        case _:
            return ComunicadorPorEmail()

# Opción 2. Se obtiene la instancia a través de un método estático de una clase
'''
class ComunicadorFactory:
    @staticmethod
    def crear_comunicador():
        tipo = get_tipo_comunicador()
        match tipo:
            case 0:
                return ComunicadorPorEmail()
            case 1:
                return ComunicadorPorWhatsapp()
            case _:
                return ComunicadorPorEmail()
'''

def get_tipo_comunicador():
    return 1