# Es una definición de clase
def xxx(self):
    return self.nombre

Cosa = type("Cosa", (object,), {"numero_maximo":10, "get_nombre":xxx})

la_cosa = Cosa()
# print(la_cosa.get_nombre()) # Error -> Aún no tenemos atributo nombre
la_cosa.nombre = 'Hulk' # Creando un atributo de instancia
print(type(la_cosa)) # <class '__main__.Cosa'>
print(Cosa.numero_maximo) # 10
print(la_cosa.nombre) # Hulk
print(la_cosa.get_nombre()) # Hulk

print('The class name is:', Cosa.__name__)
print('The class is an instance of:', Cosa.__class__)
print('The class is based on:', Cosa.__bases__)
print('The class attributes are:', Cosa.__dict__)