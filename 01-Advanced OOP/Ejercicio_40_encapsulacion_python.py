class CuentaBancaria:
    """
    Representa una cuenta bancaria.

    El saldo no puede ser negativo.
    """
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        # Puedo establecer una regla
        print('Obteniendo el saldo')
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        # Puedo establecer una regla
        print('Actualizando el saldo')
        self.__saldo = nuevo_saldo

    @saldo.deleter
    def saldo(self):
        # Puedo establecer una regla
        print('Eliminado saldo')
        del self.__saldo

    def __str__(self):
        return f'{self.titular}:{self.saldo}'

cuenta = CuentaBancaria('Fernando', 5_000)
print(cuenta.saldo)
cuenta.saldo = 8_000
print(cuenta.saldo)
delattr(cuenta,'saldo')
# print(cuenta.saldo) # Attribute Error