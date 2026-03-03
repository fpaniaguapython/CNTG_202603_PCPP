class A:
    def __init__(self):
        print('Soy A')
    def saludar(self):
        print('Hola, soy A')

class B(A):
    def __init__(self):
        print('Soy B')
        super().__init__()
    def saludar(self):
        print('Hola, soy B')

class C(A):
    def __init__(self):
        print('Soy C')
        super().__init__()
    def saludar(self):
        print('Hola, soy C')

class D(B,C):
    def __init__(self):
        print('Soy D')
        super().__init__()
    def saludar(self):
        print('Hola, soy D')
        super().saludar() # Saluda como B, porque B es la primera clase de la que hereda (MRO)
        C.saludar(self) # Invocación explícita al método pero llamándole como función
        
d = D()
d.saludar() # Hola, soy D - Hola, soy B