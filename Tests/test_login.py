from playwright.sync_api import Page, expect
from Pages.LoginPage import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

def test_login_exitoso(page):
    """Test para verificar un login exitoso con credenciales válidas"""
    login_page = LoginPage(page)      
    login_page.ir_a_login()       
    login_page.verificar_url_login()      
    login_page.verificar_titulo()
    
    email = os.getenv('EMAIL_VALIDO')
    password = os.getenv('PASSWORD_VALIDO')
    login_page.hacer_login_completo(email, password)  
    
def test_login_incorrecto(page):
    """Test para verificar que el login falla con credenciales incorrectas"""
    
    # Crear instancia de la página de login
    login_page = LoginPage(page)
    # Ir a la página de login
    login_page.ir_a_login()
    # Llenar el email y la contraseña incorrectos
    email_incorrecto = os.getenv('EMAIL_INCORRECTO')
    password_incorrecto = os.getenv('PASSWORD_INCORRECTO')
    login_page.llenar_email(email_incorrecto)
    login_page.llenar_password(password_incorrecto)
    # Hacer click en el boton de login
    login_page.hacer_click_login()
    # Verificar que el login falló
    login_page.verificar_mensaje_error()

def test_login_campo_vacio(page):
    login_page = LoginPage(page)
    login_page.ir_a_login()
    # Dejar email vacío, solo llenar password
    login_page.llenar_password('cualquier_password')
    login_page.hacer_click_login()
    # Verificar que NO navega (se queda en login)
    login_page.verificar_url_login()  # Usa la función base con waits