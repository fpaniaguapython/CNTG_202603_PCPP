import pickle

class IPod:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100
    def consumir_bateria(self):
        self.bateria-=1
    def __str__(self):
        return f'{self.marca}:{self.modelo}:{self.bateria}'

mi_ipod = None
while True:
    opcion = int(input('Introduce una opción: 1(Guardar); 2(Leer); 3(Gastar batería); 4(Mostrar):'))
    if opcion==1:
        # Proceso de escritura
        if mi_ipod==None:
            mi_ipod = IPod(marca='Apple', modelo='A5')
        with open('mi_ipod.pckl', 'wb') as file_out:
            pickle.dump(obj=mi_ipod, file=file_out)
    elif opcion==2:
        # Proceso de lectura
        with open('mi_ipod.pckl', 'rb') as file_in:
            mi_ipod = pickle.load(file=file_in)
            print(mi_ipod)
    elif opcion==3:
        # Gastar batería
        mi_ipod.consumir_bateria()
    elif opcion==4:
        print(mi_ipod)
    else:
        break




