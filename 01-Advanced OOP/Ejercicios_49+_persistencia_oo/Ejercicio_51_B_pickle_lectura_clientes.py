import pickle
import sys

class ClienteNoEncontradoError(Exception):
    pass

def leer_cliente(dni):
    nombre_fichero = dni+'.cliente'
    try:
        with open(nombre_fichero, mode='rb') as fichero_clientes:
            cliente = pickle.load(fichero_clientes)
    except FileNotFoundError as fnfe:
        raise ClienteNoEncontradoError(f'El cliente {dni} no existe')
    return cliente

if __name__=='__main__':
    while True:
        try:
            dni = input('Introduce DNI:')
            cliente = leer_cliente(dni)
        except ClienteNoEncontradoError as cne:
            print('No se ha encontrado el cliente')
        except KeyboardInterrupt:
            print('\nEl usuario se ha salido de la aplicación')
            sys.exit(-1)
        else:
            print(cliente)