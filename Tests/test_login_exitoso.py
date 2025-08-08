import allure
from playwright.sync_api import Page
from Pages.LoginPage import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

@allure.feature("Autenticación")
@allure.story("Login Exitoso")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_exitoso(page: Page):
    """Test para verificar que el login funciona con credenciales correctas"""
    
    login_page = LoginPage(page)
    
    with allure.step("Navegar a la página de login"):
        login_page.ir_a_login()
        
    with allure.step("Verificar título de la página"):
        login_page.verificar_titulo()
    
    with allure.step("Ingresar credenciales válidas"):
        email_correcto = os.getenv('EMAIL_VALIDO')
        password_correcto = os.getenv('PASSWORD_VALIDO')
        login_page.llenar_email(email_correcto)
        login_page.llenar_password(password_correcto)
    
    with allure.step("Hacer clic en el botón de login"):
        login_page.hacer_click_login()
    
    with allure.step("Verificar login exitoso"):
        login_page.verificar_mensaje_exito()
        login_page.verificar_login_exitoso()
