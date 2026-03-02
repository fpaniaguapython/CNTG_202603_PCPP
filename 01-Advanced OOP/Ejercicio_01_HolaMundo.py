class Saludador: # Definimos la clase
    def __init__(self, simpatico : bool): # Inicializador o constructor
        self.simpatico = simpatico # Declaración de atributo de instancia

    def saludar(self, nombre : str): # Método de instancia
        if (self.simpatico):
            print(f'Hola, {nombre}')
        else:
            print('No tengo nada que decir')

class SaludadorEspecial(Saludador): #SaludadorEspecial hereda de Saludador
    def saludar(self, nombre : str): # Sobreescritura del método saludar
        print(f'Me llamo {nombre} y soy muy especial')
        super().saludar(nombre) # Hace referencia a la forma 'base' del método saludar

if __name__=='__main__':# Ejecuta el bloque si el módulo es el principal
    objetoSaludador = Saludador(simpatico=False) # Instanciación de un objeto de la clase Saludador
    objetoSaludador.saludar('participantes del curso') # Invocación a un método

    objetoSaludadorEspecial = SaludadorEspecial(simpatico=True)
    objetoSaludadorEspecial.saludar('Participantes')


