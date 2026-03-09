import random
import string

class Cliente:
    def __init__(self, nombre, dni, saldo):
        self.nombre = nombre
        self.dni = dni
        self.saldo = saldo

    def incrementar_saldo(self, incremento):
        self.saldo+=incremento

    def __str__(self):
        return f'{self.nombre}:{self.dni}:{self.saldo}'
    

def get_clientes(numero):
    nombres = [
        "Ana", "Luis", "Carlos", "Marta", "Lucia",
        "Pedro", "Sofia", "Jorge", "Elena", "Pablo"
    ]

    clientes = []

    for _ in range(numero):
        nombre = random.choice(nombres)

        # Generar DNI: 8 números + 1 letra
        numeros = random.randint(10000000, 99999999)
        letra = random.choice(string.ascii_uppercase)
        dni = f"{numeros}{letra}"

        # Saldo aleatorio
        saldo = round(random.randint(-1000,2000))

        clientes.append(Cliente(nombre, dni, saldo))

    return clientes

# for x in get_clientes(10):
#    print(x)
