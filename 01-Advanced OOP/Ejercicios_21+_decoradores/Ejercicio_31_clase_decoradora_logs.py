# Versión Alejandro

import logging
import datetime
from typing import Any

def escribidor_logs(funcion_a_decorar):
    logging.basicConfig(level=logging.INFO,
                    filename="fichero_actividad.log",
                    filemode="a")
    def internal_wrapper(*args,**kwargs):
        logger = logging.getLogger()
        logger.info(f'Se ha ejecutado "{funcion_a_decorar.__name__}" con argumentos {args},{kwargs} a las {datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")}')
        return funcion_a_decorar(*args,**kwargs)
    return internal_wrapper
   
class ClaseDecoradora():
    def __init__(self, funcion_a_decorar) -> None:
        super().__init__()
        self.funcion_a_decorar = funcion_a_decorar
       
        logging.basicConfig(level=logging.INFO,
                            filename="fichero_actividad.log",
                            filemode="a")
   
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        logger = logging.getLogger()
        logger.info(f'Se ha ejecutado "{self.funcion_a_decorar.__name__}" con argumentos {args},{kwargs} a las {datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")}')
        return self.funcion_a_decorar(*args,**kwargs)
   
#@escribidor_logs
@ClaseDecoradora
def obtener_saldo():
    print("obtenemos saldo")

obtener_saldo()