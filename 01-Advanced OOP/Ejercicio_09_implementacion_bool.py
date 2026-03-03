class Motor:
    def __init__(self, nombre, potencia):
        self.nombre = nombre
        self.potencia = potencia

    # Devuelve True si la potencia es mayor de 200CV
    def __bool__(self):
        return self.potencia > 200
    
    def __int__(self):
        return self.potencia

motor = Motor('V8', 200)

print(bool(motor))
print(int(motor))

