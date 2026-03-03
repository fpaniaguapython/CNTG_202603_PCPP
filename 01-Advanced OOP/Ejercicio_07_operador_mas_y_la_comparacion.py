class Motor:
    def __init__(self, nombre, potencia):
        self.nombre = nombre
        self.potencia = potencia
    def __add__(self, other : Motor) -> Motor:
        if (not isinstance(other, Motor)):
            raise TypeError('El operador + solo se puede aplicar sobre instancias de Motor')
        motorAcumulado = Motor(self.nombre+other.nombre, self.potencia+other.potencia)
        return motorAcumulado
    def __eq__(self, other: object) -> bool:
        if (not isinstance(other, Motor)):
            raise TypeError('Solo se puede comparar un Motor con otro Motor')
        return abs(self.potencia-other.potencia)<self.potencia*0.1
    def __str__(self) -> str:
        return f'Nombre:{self.nombre}. Potencia:{self.potencia}'

x, y = 10, 20
resultado = x+y
print(resultado) # 30

x, y = 'Diez', 'Veinte'
resultado = x+y
print(resultado) # DiezVeinte

x, y, z = Motor("Motor 1", 100), Motor("Motor 2", 500), Motor("Motor 3", 549)
resultado = x+y+z
# resultado = x+y+z+"Melón" # TypeError: El operador + solo se puede aplicar sobre instancias de Motor
print(resultado) # Nombre:Motor 1Motor 2. Potencia:600

# Modificar la clase para que cuando se compare un motor con otro diga si son iguales
# si tienen la misma pontencia con un +-10% sobre la potencia del primer motor
print(x==y)
print(y==z)
# print(x=='Melón') # TypeError: Solo se puede comparar un Motor con otro Motor