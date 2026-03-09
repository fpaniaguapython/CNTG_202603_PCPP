class Factura:
    def __init__(self, importe):
        self.importe = importe

def duplicar_factura(factura):
    factura.importe*=2

def duplicar_importe(importe):
    importe*=2

importe = 1000
factura = Factura(importe)
duplicar_factura(factura)
duplicar_importe(importe)
print(factura.importe) # 2000
print(importe) # 1000