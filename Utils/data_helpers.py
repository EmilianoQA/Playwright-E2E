"""
Data Helpers - Funciones para generar datos de prueba
"""

import random
import string
from datetime import datetime


class DataHelpers:
    """Clase para generar datos de prueba"""
    
    @staticmethod
    def generar_string_aleatorio(length: int = 8) -> str:
        """Genera string aleatorio para IDs únicos"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    @staticmethod
    def generar_nombre_usuario() -> tuple:
        """Genera nombre y apellido aleatorio para testing"""
        nombres = ["Ana", "Carlos", "María", "Juan", "Laura", "Pedro", "Sofia", "Miguel"]
        apellidos = ["García", "López", "Martín", "González", "Rodríguez", "Fernández"]
        
        return random.choice(nombres), random.choice(apellidos)
    
    @staticmethod
    def generar_monto_transferencia() -> float:
        """Genera monto aleatorio para transferencias (entre 10 y 500)"""
        return round(random.uniform(10.0, 500.0), 2)
    
    @staticmethod
    def obtener_timestamp() -> str:
        """Obtiene timestamp actual para logs"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")


# Instancia global
data_helper = DataHelpers()
