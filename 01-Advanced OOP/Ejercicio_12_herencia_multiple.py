class A:
    def saludar(self):
        print('Hola, soy A')

class B(A):
    def saludar(self):
        print('Hola, soy B')

class C(A):
    def saludar(self):
        print('Hola, soy C')

class D(B,C):
    def saludar(self):
        print('Hola, soy D')

d = D()

print(isinstance(d,D)) # True
print(isinstance(d,C)) # True
print(isinstance(d,B)) # True
print(isinstance(d,A)) # True

d.saludar()