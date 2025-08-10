import allure
from playwright.sync_api import Page
from Pages.LoginPage import LoginPage
from Pages.DashboardPage import DashboardPage
import os
from dotenv import load_dotenv

load_dotenv()

@allure.feature("Gestión de Cuentas")
@allure.story("Crear Nueva Cuenta")
@allure.severity(allure.severity_level.CRITICAL)


def test_crear_cuenta(page: Page):
    '''Crear una cuenta nueva y verificar que se genera correctamente'''
    
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    with allure.step("Realizar login"):
        login_page.ir_a_login()
        email_correcto = os.getenv('EMAIL_VALIDO')
        password_correcto = os.getenv('PASSWORD_VALIDO')
        login_page.hacer_login_completo(email_correcto, password_correcto)
    
    with allure.step("Agregar una cuenta, haciendo click en el botón de Agregar Cuenta"):
        dashboard_page.abrir_modal_crear_cuenta()
    
    with allure.step("Verificar que se abre el modal de crear cuenta"):
        dashboard_page.verificar_modal_abierto()
    
    with allure.step("Seleccionar tipo de cuenta (débito)"):
        dashboard_page.seleccionar_tipo_cuenta("Débito")
    
    with allure.step("Ingresar un monto"):
        dashboard_page.ingresar_monto_inicial("200")
    
    with allure.step("Crear cuenta, haciendo click en el botón de Crear Cuenta"):
        dashboard_page.crear_cuenta()
    
    with allure.step("Verificar que la cuenta se creó exitosamente"):
        dashboard_page.verificar_cuenta_creada()


@allure.feature("Gestión de Cuentas")
@allure.story("Eliminar Cuenta")
@allure.severity(allure.severity_level.NORMAL)


def test_eliminar_cuenta(page: Page):
    '''Eliminar una cuenta existente y verificar eliminación'''
    
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    with allure.step("Realizar login"):
        login_page.ir_a_login()
        email_correcto = os.getenv('EMAIL_VALIDO')
        password_correcto = os.getenv('PASSWORD_VALIDO')
        login_page.hacer_login_completo(email_correcto, password_correcto)
    
    with allure.step("Abrir modal de eliminar cuenta"):
        dashboard_page.abrir_modal_eliminar_cuenta()
    
    with allure.step("Verificar que se abre el modal de eliminar"):
        dashboard_page.verificar_modal_eliminar_abierto()
    
    with allure.step("Seleccionar cuenta a eliminar"):
        dashboard_page.seleccionar_cuenta_para_eliminar("no importa")
    
    with allure.step("Confirmar eliminación de la cuenta"):
        dashboard_page.confirmar_eliminacion()
    
    with allure.step("Verificar que la cuenta se eliminó exitosamente"):
        dashboard_page.verificar_cuenta_eliminada()


@allure.feature("Gestión de Cuentas")
@allure.story("Validación Crear Cuenta")
@allure.severity(allure.severity_level.NORMAL)

def test_intentar_crear_cuenta_campos_vacios(page: Page):
    '''Verificar validación cuando se intenta crear cuenta con campos vacíos'''
    
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    with allure.step("Realizar login"):
        login_page.ir_a_login()
        email_correcto = os.getenv('EMAIL_VALIDO')
        password_correcto = os.getenv('PASSWORD_VALIDO')
        login_page.hacer_login_completo(email_correcto, password_correcto)
    
    with allure.step("Abrir modal crear cuenta"):
        dashboard_page.abrir_modal_crear_cuenta()
    
    with allure.step("Verificar que se abre el modal"):
        dashboard_page.verificar_modal_abierto()
    
    with allure.step("Intentar crear cuenta SIN llenar campos obligatorios"):
        # NO llamamos seleccionar_tipo_cuenta() ni ingresar_monto_inicial()
        # Vamos directo a hacer click en "CREAR CUENTA" con campos vacíos
        dashboard_page.crear_cuenta()
    
    with allure.step("Verificar mensaje de error de validación"):
        # Verificar que aparece el mensaje de error para tipo de cuenta requerido
        dashboard_page.verificar_error_tipo_cuenta_requerido()


