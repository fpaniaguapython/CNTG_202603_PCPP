import pickle

from Ejercicio_51_C_pickle_clientes import Cliente, get_clientes

def guardar_clientes(lista_clientes : list[Cliente]):
    for cliente in lista_clientes:
        print(f'Guardando cliente {cliente.dni}')
        nombre_fichero = cliente.dni+'.cliente'
        with open(nombre_fichero, mode='wb') as fichero_clientes:
            pickle.dump(cliente, fichero_clientes)


if __name__=='__main__':
    print('****Iniciando el proceso de almacenamiento de clientes****')
    lista_clientes = get_clientes(10)
    guardar_clientes(lista_clientes=lista_clientes)
    print('****Fin del proceso de almacenamiento de clientes****')

