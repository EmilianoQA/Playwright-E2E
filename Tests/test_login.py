import allure
from playwright.sync_api import Page, expect
from Pages.LoginPage import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# CASOS DE PRUEBA - LOGIN
# ==========================================

@allure.feature("Autenticación")
@allure.story("Login Exitoso")
@allure.severity(allure.severity_level.CRITICAL)

def test_TC001_login_exitoso(page: Page):
    """TC-001: Verificar login exitoso con credenciales válidas"""
    
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


@allure.feature("Autenticación")
@allure.story("Login con Credenciales Inválidas")
@allure.severity(allure.severity_level.NORMAL)

def test_TC002_login_credenciales_incorrectas(page: Page):
    """TC-002: Verificar que el login falla con credenciales incorrectas"""
    
    login_page = LoginPage(page)
    
    with allure.step("Navegar a la página de login"):
        login_page.ir_a_login()
    
    with allure.step("Ingresar credenciales inválidas"):
        email_incorrecto = os.getenv('EMAIL_INCORRECTO')
        password_incorrecto = os.getenv('PASSWORD_INCORRECTO')
        login_page.llenar_email(email_incorrecto)
        login_page.llenar_password(password_incorrecto)
    
    with allure.step("Hacer clic en el botón de login"):
        login_page.hacer_click_login()
    
    with allure.step("Verificar mensaje de error"):
        login_page.verificar_mensaje_error()


@allure.feature("Autenticación")
@allure.story("Validación de Campos Obligatorios")
@allure.severity(allure.severity_level.NORMAL)

def test_TC003_login_campos_vacios_no_redirige(page: Page):
    """TC-003: Verificar que con campos vacíos NO se redirige al dashboard"""
    
    login_page = LoginPage(page)
    
    with allure.step("Navegar a la página de login"):
        login_page.ir_a_login()
    
    with allure.step("Verificar que estamos en login"):
        login_page.verificar_url_login()
    
    with allure.step("Hacer clic en 'Iniciar sesión' SIN llenar campos"):
        # NO llamamos llenar_email() ni llenar_password() 
        # Click directo en el botón con campos vacíos
        login_page.hacer_click_login()
    
    with allure.step("Verificar que permanece en página de login (NO redirige)"):
        # Si hay validación correcta, debe seguir en /login
        login_page.verificar_url_login()
        
    with allure.step("Verificar que NO aparece mensaje de éxito"):
        # No debe aparecer "Inicio de sesión exitoso"
        login_page.verificar_que_no_hay_mensaje_exito()


@allure.feature("Autenticación")
@allure.story("Validación Nativa del Navegador")
@allure.severity(allure.severity_level.NORMAL)

def test_TC004_login_validacion_nativa_html5(page: Page):
    """TC-004: Verificar mensajes nativos HTML5 del navegador"""
    
    login_page = LoginPage(page)
    
    with allure.step("Navegar a la página de login"):
        login_page.ir_a_login()
    
    with allure.step("Verificar que los campos tienen validación requerida"):
        # Verificar atributo 'required' en ambos campos
        email_input = page.locator(login_page.input_email)
        password_input = page.locator(login_page.input_password)
        
        # Ambos campos deben tener el atributo 'required'
        email_required = email_input.get_attribute('required')
        password_required = password_input.get_attribute('required')
        
        assert email_required is not None, "Campo email debe tener atributo required"
        assert password_required is not None, "Campo password debe tener atributo required"
    
    with allure.step("Intentar hacer click en botón con campos vacíos"):
        # Click directo sin llenar campos
        login_page.hacer_click_login()
    
    with allure.step("Verificar estado de validación nativo del navegador"):
        # Verificar que los campos NO son válidos según HTML5
        email_is_valid = email_input.evaluate("el => el.validity.valid")
        password_is_valid = password_input.evaluate("el => el.validity.valid")
        
        assert email_is_valid == False, "Campo email debe ser inválido cuando está vacío"
        assert password_is_valid == False, "Campo password debe ser inválido cuando está vacío"
    
    with allure.step("Leer mensajes de validación nativos"):
        # Obtener mensajes nativos del navegador
        email_validation_msg = email_input.evaluate("el => el.validationMessage")
        password_validation_msg = password_input.evaluate("el => el.validationMessage")
        
        print(f"Mensaje email: '{email_validation_msg}'")
        print(f"Mensaje password: '{password_validation_msg}'")
        
        # Verificar que hay algún mensaje (varía por idioma del navegador)
        assert len(email_validation_msg) > 0, "Debe haber mensaje de validación para email"
        assert len(password_validation_msg) > 0, "Debe haber mensaje de validación para password"
    
    with allure.step("Verificar que permanece en login (no se envió el form)"):
        # Como validación final, verificar que sigue en /login
        login_page.verificar_url_login()
