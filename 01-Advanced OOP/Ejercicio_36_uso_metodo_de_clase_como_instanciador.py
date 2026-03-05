# Implementación simple del patrón de diseño Factory (con muchos peros)
class Cliente:
    def __init__(self, nombre, ciudad, estado, recorrido):
        self.nombre = nombre
        self.ciudad = ciudad
        self.estado = estado
        self.recorrido = recorrido

    @classmethod
    def obtener_nuevo_cliente(cls, nombre, ciudad):
        return cls(nombre, ciudad, 'Pendiente', 10.8)

# Instancia directa
clienteMarta = Cliente('Marta', 'Santiago', 'Pendiente', 8.3)

# Delegación de la creación de la instancia en el método de clase
clienteHector = Cliente.obtener_nuevo_cliente('Héctor', 'Coruña')

print(type(clienteMarta))
print(type(clienteHector))