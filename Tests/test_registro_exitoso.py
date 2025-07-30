import allure
from playwright.sync_api import Page, expect
from Pages.RegistroPage import RegistroPage
import os
from dotenv import load_dotenv

load_dotenv()

@allure.feature("Registro de Usuario")
@allure.story("Registro Exitoso")
@allure.severity(allure.severity_level.CRITICAL)
def test_registro_exitoso(page: Page):
    """Test para verificar que el registro funciona correctamente con datos válidos"""
    
    registro_page = RegistroPage(page)
    
    with allure.step("Navegar a la página de registro"):
        registro_page.ir_a_registro()
    
    with allure.step("Verificar que estamos en la página de registro"):
        registro_page.verificar_url_registro()
        registro_page.verificar_titulo()
    
    with allure.step("Generar datos aleatorios para el registro"):
        email = registro_page.generar_email_aleatorio()
        password = registro_page.generar_password_aleatorio()
    
    with allure.step("Realizar registro completo con datos válidos"):
        registro_page.hacer_registro_completo("Test", "Usuario", email, password)
    
 
