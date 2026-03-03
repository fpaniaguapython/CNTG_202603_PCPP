import abc

class Impresora(abc.ABC):
    def expulsar_papel(self):
        print('Expulsando papel')
    @abc.abstractmethod
    def imprimir(self, texto):
        pass

class ImpresoraLaser(Impresora):
    def imprimir(self, texto):
        print(f'Imprimiento {texto} como impresora láser')

class ImpresoraMatricial(Impresora):
    def imprimir(self, texto):
        print(f'Imprimiendo {texto} como impresora matricial')

def imprimir(impresora : Impresora, texto):
    if (isinstance(impresora, Impresora)):
        impresora.imprimir(texto)

impresora = ImpresoraLaser()
imprimir(impresora, 'Un poema muy bonito')