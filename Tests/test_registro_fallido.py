from playwright.sync_api import Page, expect
from Pages.RegistroPage import RegistroPage
import os
from dotenv import load_dotenv
import allure
load_dotenv()


@allure.feature("Registro de Usuario")
@allure.story("Registro Fallido")
@allure.severity(allure.severity_level.NORMAL)
def test_registro_fallido_usuario_existente(page: Page):
    '''Verificar que el registro falla al intentar crear un usuario con un email ya existente'''
    registro_page = RegistroPage(page)
    
    with allure.step("Navegar a la página de registro"):
        registro_page.ir_a_registro()

    with allure.step("Verificar que estamos en la URL de registro"):
        registro_page.verificar_url_registro()
        registro_page.verificar_titulo()

    with allure.step("Preparar datos de registro"):
        email_existente = os.getenv('EMAIL_VALIDO')  
        password = registro_page.generar_password_aleatorio()
    
    with allure.step("Llenar formulario de registro"):
        registro_page.llenar_nombre("Nuevo")
        registro_page.llenar_apellido("Usuario")
        registro_page.llenar_email(email_existente)
        registro_page.llenar_password(password)

    with allure.step("Intentar registrarse"):
        registro_page.hacer_click_registro()

    with allure.step("Verificar que aparece error y NO redirige"):
        registro_page.verificar_mensaje_error()
        registro_page.verificar_url_registro()
