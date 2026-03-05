from interfaz_comunicador import IComunicador

class ComunicadorPorEmail(IComunicador):
    def enviar(self, destinatario : str, mensaje : str) -> None:
        print(f'Enviando {mensaje} a {destinatario} por email')
    
    def recibir(self, emisor : str) -> str:
        print(f'Recibiendo mensaje de {emisor}')
        return 'El mensaje obtenido por email'