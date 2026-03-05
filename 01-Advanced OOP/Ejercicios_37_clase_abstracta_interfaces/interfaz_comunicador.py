import abc

class IComunicador(abc.ABC):
    @abc.abstractmethod
    def enviar(self, destinatario : str, mensaje : str) -> None:
        pass
    
    @abc.abstractmethod
    def recibir(self, emisor : str) -> str:
        pass



