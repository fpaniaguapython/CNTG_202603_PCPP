import datetime

class Equipo:
    nombre_competicion = 'Liga de Fútbol Profesional' # Atributo de clase
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre # Atributo de instancia
        self.presupuesto = presupuesto # Atributo de instancia

    def get_presupuesto(self): # Método de instancia
        return self.presupuesto
    
    @classmethod 
    def get_nombre_competicion(cls): # Método de clase
        return cls.nombre_competicion
    
    @staticmethod
    def dame_la_hora(): # Método estático
        return datetime.datetime.now().time()
    
celta = Equipo('Celta de Vigo', 100_000_000)
print(celta.get_presupuesto()) # Llamada al método de instancia
print(Equipo.get_nombre_competicion()) # Llamada al método de clase
print(Equipo.dame_la_hora())
    

