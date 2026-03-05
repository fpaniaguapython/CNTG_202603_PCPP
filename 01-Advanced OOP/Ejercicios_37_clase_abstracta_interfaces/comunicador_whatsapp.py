from interfaz_comunicador import IComunicador

class ComunicadorPorWhatsapp(IComunicador):
    def enviar(self, destinatario : str, mensaje : str) -> None:
        print(f'Enviando {mensaje} a {destinatario} por whatsapp')
    
    def recibir(self, emisor : str) -> str:
        print(f'Recibiendo mensaje de {emisor}')
        return 'El mensaje obtenido por whatsapp'