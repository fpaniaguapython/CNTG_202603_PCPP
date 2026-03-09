import json

class Factura:
    def __init__(self, cliente, importe):
        self.cliente = cliente
        self.importe = importe

    def get_json_data(self):
        return json.dumps({
            "cliente": self.cliente,
            "importe": self.importe
        }, ensure_ascii=False)
    
factura = Factura('Rosalía',1000)

json = factura.get_json_data()
print(json)


