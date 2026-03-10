# Crear una clase utilizando type que se llame Vehiculo.
### Contiene el método de instancia arrancar
# Crear una clase utilizando type que se llame Barco
### Heredar de Vehiculo
### Contiene el método de instancia atracar

# Instancia de un Barco, arrancarlo y atracarlo en puerto.

def arrancar(self):
    print('Arrancando...')

def atracar(self):
    print('Atracando...')

Vehiculo = type('Vehiculo', (), {'arrancar':arrancar})

Barco = type('Barco', (Vehiculo,), {'atracar':atracar})

bribon = Barco()
bribon.arrancar()
bribon.atracar()
