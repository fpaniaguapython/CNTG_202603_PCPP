# Escenario 1 - Copia por asignación - Copia las referencias
lista_1 = [1,2,3]
lista_2 = lista_1
lista_1[1]='dos'
print(lista_1) # [1, 'dos', 3]
print(lista_2) # [1, 'dos', 3]

# Escenario 2 - Copia por slicing - Copia los valores (OK en el primer nivel)
lista_1 = [1,2,3]
lista_2 = lista_1[:]
lista_1[1]='dos'
print(lista_1) # [1, 'dos', 3]
print(lista_2) # [1, 2, 3]

# Escenario 2 - Copia por slicing - Copia los valores (KO en los demás niveles)
lista_1 = [1,2,3,[4,5,6]]
'''
lista_1
-------1,2,3
------------4,5,6
'''
lista_2 = lista_1[:]
lista_1[1]='dos' # Esta modificación solo afecta a lista_1 (se hizo un duplicado de sus valores)
lista_1[3][0]='cuatro' # Esta modificación afecta a lista_1 y a lista_2 (se hizo un diplicado de sus referencias)
print(lista_1) # [1, 'dos', 3, ['cuatro', 5, 6]]
print(lista_2) # [1, 2, 3, ['cuatro', 5, 6]]

# Escenario 3 - Copia en profundiad - Copia los valores a todos los niveles (OK)
import copy
lista_1 = [1,2,3,[4,5,6]]
'''
lista_1
-------1,2,3
------------4,5,6
'''
lista_2 = copy.deepcopy(lista_1) # Copia en profundidad (deep copy)
lista_1[1]='dos' # Esta modificación solo afecta a lista_1
lista_1[3][0]='cuatro' # Esta modificación solo afecta a lista_1
print(lista_1) # [1, 'dos', 3, ['cuatro', 5, 6]]
print(lista_2) # [1, 2, 3, [4, 5, 6]] 