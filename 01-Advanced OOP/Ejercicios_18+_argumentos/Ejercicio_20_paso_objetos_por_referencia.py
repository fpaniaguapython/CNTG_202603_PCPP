def incrementar_contador(objeto):
    objeto.incrementar_contador()

class ListadoInvitados:
    def __init__(self) -> None:
        self.contador = 0
    
    def incrementar_contador(self):
        self.contador+=1

listado_invitados = ListadoInvitados()
incrementar_contador(listado_invitados)

# El paso del argumento (objeto) se realiza como referencia
print(listado_invitados.contador) # 1 (hemos incrementado dentro de la función y el efecto se ve fuera)