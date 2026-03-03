class A:
    def saludar(self):
        print('Hola, soy A')

class C(A):
    def saludar(self):
        print('Hola, soy C')

# class D(A,C): # PROVOCA UN ERROR DE INCONSISTENCIA EN EL MRO
#    def saludar(self):
#        print('Hola, soy D')

class D(C,A): # NO PROVOCA UN ERROR DE INCONSISTENCIA EN EL MRO
    def saludar(self):
        print('Hola, soy D')

d = D()

print(isinstance(d,D)) # True
print(isinstance(d,C)) # True
print(isinstance(d,A)) # True

d.saludar()
