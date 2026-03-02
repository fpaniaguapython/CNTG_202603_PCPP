class Factura:
    def __init__(self, nombre_cliente, importe) -> None:
        self.nombre_cliente = nombre_cliente # Atributo de instancia
        self.importe = importe # Atributo de instancia

    def mostrar(self):
        self.mostrado = True # Añadimos un atributo de instancia al objeto
        print(f'Nombre:{self.nombre_cliente}. Importe:{self.importe}')

factura_1 = Factura('Xunta', 1_000)
print(dir(Factura)) # ... 'mostrar'
print(dir(factura_1)) # ... 'importe', 'mostrar', 'nombre_cliente'

# PYTHON considera atributos tanto atributos como métodos 
# print(factura.impuesto) # AttributeError: 'Factura' object has no attribute 'impuesto'
# factura.saltar() # AttributeError: 'Factura' object has no attribute 'saltar'

factura_1.pagado = False # Añadimos un atributo de instancia a factura_1
print(factura_1.pagado)

factura_2 = Factura('CAM', 5_000)
factura_2.mostrar()

print(dir(factura_1))
print(dir(factura_2))