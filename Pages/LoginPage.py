from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv
from Funciones import Funcion

load_dotenv()

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.funcion = Funcion(page)
        
        # URLs
        base_url = os.getenv('BASE_URL', 'http://localhost:3000')
        self.url_login = f"{base_url}/login"
        self.url_dashboard = f"{base_url}/dashboard"
        
        # Selectores
        self.titulo_login = '[data-testid="titulo-login"]'
        self.input_email = 'input[type="email"]'
        self.input_password = 'input[type="password"]'
        self.boton_login = '[data-testid="boton-login"]'
        self.mensaje_exito = 'text="Inicio de sesión exitoso"'
        self.mensaje_error = 'text="Invalid credentials"'

    def ir_a_login(self):
        """Navegar a la página de login"""
        self.funcion.navegar_a_url(self.url_login)
    
    def verificar_url_login(self):
        """Verificar que estamos en la página de login"""
        self.funcion.validar_url(self.url_login)
    
    def verificar_titulo(self):
        """Verificar que el título es correcto"""
        self.funcion.validar_texto(self.titulo_login, 'Iniciar sesión')
    
    def llenar_email(self, email: str):
        """Llenar el campo de email"""
        self.funcion.llenar_texto(self.input_email, email)
    
    def llenar_password(self, password: str):
        """Llenar el campo de contraseña"""
        self.funcion.llenar_texto(self.input_password, password)
    
    def hacer_click_login(self):
        """Hacer clic en el botón de login"""
        self.funcion.click_boton(self.boton_login)
    
    def verificar_mensaje_exito(self):
        """Verificar que aparece el mensaje de éxito"""
        self.funcion.validar_elemento_visible(self.mensaje_exito)
    
    def verificar_login_exitoso(self):
        """Verificar redirección al dashboard"""
        self.funcion.validar_url(self.url_dashboard)
    
    def verificar_mensaje_error(self):
        """Verificar que aparece el mensaje de error"""
        self.funcion.validar_elemento_visible(self.mensaje_error)
    
    def hacer_login_completo(self, email: str, password: str):
        """Realizar proceso completo de login"""
        self.llenar_email(email)
        self.llenar_password(password)
        self.hacer_click_login()
        self.verificar_mensaje_exito()
        self.verificar_login_exitoso()