class Ordenador: 
    vida_util = 10 # Atributo de clase
    def __init__(self, marca : str) -> None:
        self.marca = marca # Creando una atributo de instancia
    
    def arrancar(self):
        print("Arrancando...")
        self.arrancado = True # Creando una atributo de instancia

mi_dell = Ordenador("Dell")
mi_hp = Ordenador("HP")
mi_dell.arrancar()
mi_hp.estropeado = True # Creando una atributo de instancia
mi_dell.marka = "Lenovo" # (OJO, ERROR TIPOGRÁFICO) Creando una atributo de instancia
setattr(mi_dell, "cores", 4) # Creando una atributo de instancia

print(mi_hp.vida_util) # 10
print(mi_dell.vida_util) # 10
print(Ordenador.vida_util) # 10
Ordenador.vida_util = 12
print(mi_hp.vida_util) # 12
print(mi_dell.vida_util) # 12
print(Ordenador.vida_util) # 12
mi_hp.vida_util = 15 # ERROR -> Creación de una variable de instancia
print(mi_hp.vida_util) # 12
print(mi_dell.vida_util) # 12
print(Ordenador.vida_util) # 12

# NO ACCEDER A LOS ATRIBUTOS DE CLASE A TRAVÉS DE LOS OBJETOS

Ordenador.reciclable = True # ATributo de clase creado en 'runtime'

del mi_hp.estropeado # Eliminación de un atributo de instancia
mi_hp.arrancar()
# del mi_hp.arrancar # Error, los métodos no son propios de las instancias
del Ordenador.arrancar # Ok, borrar el método de la clase
# mi_hp.arrancar() # AttributeError: 'Ordenador' object has no attribute 'arrancar'. Did you mean: 'arrancado'?

print(mi_hp.__dict__) # {'marca': 'HP', 'vida_util': 15, 'arrancado': True} -> Atributos de instancia
print(Ordenador.__dict__) # {'vida_util': 12, '__init__': <function>, 'reciclable': True} -> Atributos de clase