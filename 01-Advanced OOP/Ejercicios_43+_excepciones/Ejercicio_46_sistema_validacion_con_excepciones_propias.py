# Crear una clase Factura (Nombre cliente, CIF, importe)
# En el constructor, vamos a validar: 
# - Nombre del cliente no esté vacío
# - CIF sea válido 
# - Importe sea positivo (considerar que el importe siempre es un número)

from Ejercicio_46_excepciones import NombreVacioException, CIFNoValidoException, ImporteNegativoException

class Factura:
    def __init__(self, nombre_cliente : str, CIF : str, importe : int):
        Factura.__validar_nombre_cliente(nombre_cliente)
        Factura.__validar_cif(CIF)
        Factura.__validar_importe(importe)
        self.nombre_cliente = nombre_cliente
        self.CIF = CIF
        self.importe = importe
       
    @staticmethod
    def __validar_nombre_cliente(nombre : str):
        if nombre==None or len(nombre.strip())==0:
            raise NombreVacioException(108, 'El nombre está vacío o solo contiene espacios')

    @staticmethod
    def __validar_cif(cif):
        cif = cif.upper()
        if len(cif) != 9:
            raise CIFNoValidoException()

        letras_iniciales = "ABCDEFGHJNPQRSUVW"
        if cif[0] not in letras_iniciales:
            raise CIFNoValidoException()

        numeros = cif[1:8]
        if not numeros.isdigit():
            raise CIFNoValidoException()

        control = cif[-1]

        # Suma de posiciones pares
        suma_pares = sum(int(numeros[i]) for i in range(1, 7, 2))

        # Suma de posiciones impares multiplicadas por 2 y sumando cifras
        suma_impares = 0
        for i in range(0, 7, 2):
            doble = int(numeros[i]) * 2
            suma_impares += sum(int(d) for d in str(doble))

        total = suma_pares + suma_impares
        digito_control = (10 - (total % 10)) % 10

        # Diccionario para letras de control
        letras_control = "JABCDEFGHI"
        if cif[0] in "ABEH":  # Control solo dígito
            if control != str(digito_control):
                raise CIFNoValidoException()
        elif cif[0] in "KPQS":  # Control solo letra
            if control != letras_control[digito_control]:
                raise CIFNoValidoException()
        else:  # Puede ser dígito o letra
            if not (control == str(digito_control) or control == letras_control[digito_control]):
                raise CIFNoValidoException()

    @staticmethod
    def __validar_importe(importe):
        if importe<0:
            raise ImporteNegativoException(importe)

try:
    # factura = Factura('', 'ADFKSDFJ', -100) # El nombre está vacío: El nombre está vacío o solo contiene espacios / El código de error es: 108
    # factura = Factura('  ', 'ADFKSDFJ', -100) # El nombre está vacío: El nombre está vacío o solo contiene espacios / El código de error es: 108
    # factura = Factura('Porto S.L.', 'ADFKSDFJ', -100) # El CIF no es válido
    # factura = Factura('Porto S.L.', 'B12345678', -100) # El CIF no es válido
    # factura = Factura('Porto S.L.', 'A58818501', -100) # El importe debería haber sido 100
    factura = Factura('Porto S.L.', 'A58818501', 100) # ¡LA FACTURA SE HA CREADO CORRECTAMENTE!
except NombreVacioException as nve:
    print('El nombre está vacío:', nve)
    print('El código de error es:', nve.error_code)
except CIFNoValidoException as cnve:
    print('El CIF no es válido')
except ImporteNegativoException as ine:
    print(f'El importe debería haber sido {ine.get_valor_positivo()}')
else:
    print('¡LA FACTURA SE HA CREADO CORRECTAMENTE!')


