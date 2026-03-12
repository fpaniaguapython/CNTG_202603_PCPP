# pip install pycodestyle -> Instalar el paquete pycodestyle

# Revisión de cumplimiento de PEP8 mediante pycodestyle

# Código no cumple con PEP8
'''
def f(x,
    y):
         z=x**y
         return z

r = f(8,5)





print(r)
'''
# Código que cumple con PEP8
'''
def f(x,
      y):
    z = x**y
    return z


r = f(8, 5)

print(r)
'''