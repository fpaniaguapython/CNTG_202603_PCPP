import json

class Motor:
    def __init__(self, nombre, potencia):
        self.nombre = nombre
        self.potencia = potencia
    
    # Invocado cuando se llama a la función str pasándole el objeto
    # Si no lo hay, se ejecuta __repr__
    def __str__(self) -> str:
        print('Ejecutando __str__')
        return f'Nombre:{self.nombre}. Potencia:{self.potencia}'
    
    # Inocado cuando el objeto está contenido en una estructura de datos (lista, tupla, etc.)
    # Si no lo hay, se ejecuta __repr__ de object
    def __repr__(self) -> str:
        print('Ejecutando __repr__')
        return f'{self.nombre}-{self.potencia}'
    
motor_v8 = Motor('V8', 350)
print(motor_v8)
mi_motor = str(motor_v8)

motor_v10 = Motor('V10', 200)

motores = (motor_v8, motor_v10)
print(motores) # Ejecuta el __repr__