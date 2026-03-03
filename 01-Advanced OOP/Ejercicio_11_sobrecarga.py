# En Python la sobrecarga se 'simula' con asignación de valores por defecto
# a los argumentos

def sumar(x, y, z=0):
    return x+y+z

r = sumar(103, 5)
print(r)

r = sumar(103, 5, 3)
print(r)