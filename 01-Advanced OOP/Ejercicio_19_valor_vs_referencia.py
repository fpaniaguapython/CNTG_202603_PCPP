# la variable valor se pasa 'por valor' (se copia el contenido)
# la variable lista se pasa 'por referencia' (se proporciona es la dirección de memoria en la que se encuentra)
def calcular(valor: int, lista: list):
    valor+=1
    lista.append(valor)
    print('Valor dentro:', valor)
    print('Lista dentro:', lista)

valor = 10
lista = [valor]
print('Valor antes:', valor)
print('Lista antes:', lista)
calcular(valor, lista)
print('Valor después:', valor)
print('Lista después:', lista)