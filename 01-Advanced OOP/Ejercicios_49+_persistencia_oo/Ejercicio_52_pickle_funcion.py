import pickle

def sumar(s1, s2):
    return s1+s2

def restar(r1, r2):
    return r1-r2

# Guardar las referencias a las funciones en un fichero
# with open('funciones.pckl', mode='wb') as fichero_funciones:
#    pickle.dump(sumar, fichero_funciones)
#    pickle.dump(restar, fichero_funciones)

# Leer las referencias a las funciones de un fichero
# Sólo funciona si están visibles las funciones que dieron origen
# a la serialización.
with open('funciones.pckl', mode='rb') as fichero_funciones:
    f1 = pickle.load(fichero_funciones) # Función sumar
    f2 = pickle.load(fichero_funciones) # Función restar


print(f2(3,5)) # -2
print(f1(8,2)) # 10
