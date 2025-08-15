"""
API Helpers - Funciones para interactuar con la API de Redux Athena Bank
Permite crear usuarios, cuentas y realizar operaciones via API
"""

import requests
import random
import string
import os
import time
from typing import Dict, Optional


class APIHelpers:
    """Clase para manejar operaciones con la API"""
    
    def __init__(self):
        self.base_url = os.getenv('API_BASE_URL', 'http://localhost:6007')
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def generar_email_unico(self, prefijo: str = "test") -> str:
        """Genera un email único para testing"""
        timestamp = random.randint(10000, 99999)
        return f"{prefijo}_{timestamp}@test.com"
    
    def generar_password_seguro(self) -> str:
        """Genera una contraseña segura para testing"""
        return "Test123456!"
    
    def crear_usuario_via_api(self, 
                             nombre: str = "Usuario", 
                             apellido: str = "Test") -> Dict:
        """
        Crea un nuevo usuario via API - BASADO EN TC053 QUE YA FUNCIONA
        
        Returns:
            dict: Datos del usuario creado (email, password, id, token)
        """
        
        # Generar datos únicos (evitar colisiones de timestamp)
        import time
        timestamp = str(int(time.time() * 1000))[-8:]  # Usar milisegundos
        email = f"test{timestamp}@example.com"
        password = "password123"
        
        # Payload (mismo formato que TC053)
        payload = {
            "firstName": f"{nombre}{timestamp}",
            "lastName": f"{apellido}{timestamp}", 
            "email": email,
            "password": password
        }
        
        try:
            # POST a la API (mismo endpoint que TC053)
            response = requests.post(
                f"{self.base_url}/api/auth/signup",
                json=payload,
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 201:
                response_data = response.json()
                return {
                    "id": response_data["user"]["id"],
                    "email": email,
                    "password": password,
                    "nombre": payload["firstName"],
                    "apellido": payload["lastName"],
                    "token": response_data["token"],
                    "status": "success"
                }
            else:
                print(f"Error al crear usuario: {response.status_code}")
                print(f"Response: {response.text}")
                return {"status": "error", "message": response.text}
                
        except Exception as e:
            print(f"Error en crear_usuario_via_api: {e}")
            return {"status": "error", "message": str(e)}
    
    def crear_cuenta_via_api(self, 
                           usuario_token: str,
                           tipo: str = "debito", 
                           saldo_inicial: float = 1000.0) -> Dict:
        """
        Crea una cuenta bancaria via API
        
        Args:
            usuario_token: Token de autenticación del usuario
            tipo: Tipo de cuenta (debito/credito)
            saldo_inicial: Saldo inicial de la cuenta
            
        Returns:
            dict: Datos de la cuenta creada
        """
        
        # Headers con autenticación
        auth_headers = self.headers.copy()
        auth_headers['Authorization'] = f"Bearer {usuario_token}"
        
        payload = {
            "tipo": tipo,
            "saldo_inicial": saldo_inicial
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/api/cuentas/crear",
                json=payload,
                headers=auth_headers,
                timeout=10
            )
            
            if response.status_code in [200, 201]:
                cuenta_data = response.json()
                return {
                    "numero_cuenta": cuenta_data.get("numero_cuenta"),
                    "tipo": tipo,
                    "saldo": saldo_inicial,
                    "status": "success"
                }
            else:
                print(f"Error al crear cuenta: {response.status_code}")
                return {"status": "error", "message": response.text}
                
        except Exception as e:
            print(f"Error en crear_cuenta_via_api: {e}")
            return {"status": "error", "message": str(e)}
    
    def obtener_saldo_via_api(self, usuario_token: str) -> Dict:
        """
        Obtiene el saldo de las cuentas del usuario via API
        
        Args:
            usuario_token: Token de autenticación del usuario
            
        Returns:
            dict: Información de saldos
        """
        
        auth_headers = self.headers.copy()
        auth_headers['Authorization'] = f"Bearer {usuario_token}"
        
        try:
            response = requests.get(
                f"{self.base_url}/api/cuentas/saldo",
                headers=auth_headers,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "error", "message": response.text}
                
        except Exception as e:
            return {"status": "error", "message": str(e)}


# Instancia global para usar en tests
api_helper = APIHelpers()
