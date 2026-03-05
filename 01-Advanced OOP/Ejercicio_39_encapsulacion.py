class CuentaBancaria:
    """
    Representa una cuenta bancaria.

    El saldo no puede ser negativo.
    """
    def __init__(self, titular, saldo):
        self.titular = titular
        self.set_saldo(saldo)

    def get_saldo(self):# Getter manual
        # Puedo establecer una regla
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo): # Setter manual
        # Puedo establecer una regla
        self.__saldo = nuevo_saldo

    def retirar_cantidad(self, cantidad : int):
        if (cantidad>self.__saldo):
            raise ValueError('La cantidad excede el saldo')
        self.__saldo-=cantidad
    
    def __str__(self):
        return f'{self.titular}:{self.__saldo}'

cuenta = CuentaBancaria('Julio', 1_000_000)
# cuenta.__saldo-=1_500_000 # ERROR
# cuenta._CuentaBancaria__saldo-=1_500_000 # Funciona, pero NO SE HACE
# cuenta.retirar_cantidad(1_500_000) # Provoca un ValueError porque excede el saldo
print(cuenta.get_saldo())
