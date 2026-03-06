# FacturadorBaseException
# - NombreVacioException
# - CIFNoValidoException
# - ImporteNegativoException
#   - Método get_valor_positivo (devolver el valor positivo del importe)

class FacturadorBaseException(Exception):
    pass

class NombreVacioException(FacturadorBaseException):
    def __init__(self, error_code, *args: object) -> None:
        self.error_code = error_code
        super().__init__(*args)

class CIFNoValidoException(FacturadorBaseException):
    pass

class ImporteNegativoException(FacturadorBaseException):
    def __init__(self, importe, *args: object) -> None:
        self.importe = importe
        super().__init__(*args)

    def get_valor_positivo(self):
        return abs(self.importe)