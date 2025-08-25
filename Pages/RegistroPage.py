from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
from Utils.Funciones import Funcion
import random
import string

# Cargar variables de entorno
load_dotenv()

class RegistroPage:
    def __init__(self, page: Page):
        self.page = page
        self.funcion = Funcion(page)
        
        # URLs desde variables de entorno
        base_url = os.getenv('BASE_URL', 'http://localhost:3000')
        self.url_registro = f"{base_url}/signup"
        self.url_login = f"{base_url}/login"
        self.url_dashboard = f"{base_url}/dashboard"
        
        # Selectores
        self.titulo_registro = '[data-testid="titulo-registro"]'
        self.input_nombre = 'input[name="firstName"]'
        self.input_apellido = 'input[name="lastName"]'
        self.input_email = 'input[name="email"]'
        self.input_password = 'input[name="password"]'
        self.boton_registro = '[data-testid="boton-registrarse"]'
        self.mensaje_exito = 'text="Registro exitoso!"'
        self.mensaje_error = 'text="Email already in use"'  

    def ir_a_registro(self):
        """Ir a la página de registro"""
        self.funcion.navegar_a_url(self.url_registro)
    
    def verificar_url_registro(self):
        """Verificar que estamos en la URL de registro"""
        self.funcion.validar_url(self.url_registro)
    
    def verificar_titulo(self):
        """Verificar que el título es correcto"""
        self.funcion.validar_texto(self.titulo_registro, 'Registrarse')
    
    def llenar_nombre(self, nombre: str):
        """Llenar campo nombre"""
        self.funcion.llenar_texto(self.input_nombre, nombre)
    
    def llenar_apellido(self, apellido: str):
        """Llenar campo apellido"""
        self.funcion.llenar_texto(self.input_apellido, apellido)
    
    def llenar_email(self, email: str):
        """Llenar campo email"""
        self.funcion.llenar_texto(self.input_email, email)
    
    def llenar_password(self, password: str):
        """Llenar campo password"""
        self.funcion.llenar_texto(self.input_password, password)
    
    def hacer_click_registro(self):
        """Hacer click en el botón de registro"""
        self.funcion.click_boton(self.boton_registro)
    
    def verificar_mensaje_exito(self):
        """Verificar que aparece el mensaje de éxito"""
        self.funcion.validar_elemento_visible(self.mensaje_exito)
    
    def verificar_mensaje_error(self):
        """Verificar que aparece el mensaje de error"""
        self.funcion.validar_elemento_visible(self.mensaje_error)
    
    def verificar_redireccion_login(self):
        """Verificar que redirige al login después del registro exitoso"""
        self.funcion.validar_url(self.url_login)
    
    def generar_email_aleatorio(self):
        """Generar email aleatorio para tests"""
        letras = string.ascii_lowercase
        usuario = ''.join(random.choice(letras) for i in range(8))
        return f"{usuario}@test.com"
    
    def generar_password_aleatorio(self):
        """Generar password aleatorio para tests"""
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for i in range(10))
    
    def hacer_registro_completo(self, nombre: str, apellido: str, email: str, password: str):
        """Método que hace todo el proceso de registro"""
        self.llenar_nombre(nombre)
        self.llenar_apellido(apellido)
        self.llenar_email(email)
        self.llenar_password(password)
        self.hacer_click_registro()
        self.verificar_mensaje_exito()
        self.verificar_redireccion_login()
