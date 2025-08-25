import pytest
import allure
from playwright.sync_api import Page
from Pages.LoginPage import LoginPage
from Data.usuarios import usuarios  # ← Importar datos del archivo

# ==========================================
# PASO 1: ENTENDER CÓMO FUNCIONA DDT
# ==========================================

# Test tradicional (hardcodeado)
def test_login_tradicional_ejemplo(page: Page):
    """Ejemplo: así era ANTES - solo 1 caso"""
    login_page = LoginPage(page)
    
    email = "emilianomaure@gmail.com"
    password = "playwright"
    
    login_page.ir_a_login()
    login_page.llenar_email(email)
    login_page.llenar_password(password)
    login_page.hacer_click_login()
    login_page.verificar_login_exitoso()

# ==========================================
# CON DDT 
# ==========================================

@pytest.mark.parametrize("usuario", usuarios)  
@allure.feature("Autenticación")
@allure.story("Login con Data-Driven Testing")
@allure.severity(allure.severity_level.CRITICAL)

def test_login_ddt(page: Page, usuario):  
    
    login_page = LoginPage(page)
    
    with allure.step(f"Ejecutando login para: {usuario['nombre']}"):
        
        email = usuario["email"]
        password = usuario["password"]
        es_valido = usuario["valido"]
        
        # Adjuntar datos al reporte
        allure.attach(f"Usuario: {usuario['nombre']}", name="Tipo Usuario", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Email: {email}", name="Email Usado", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Válido: {es_valido}", name="Resultado Esperado", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Navegar e ingresar credenciales"):
        login_page.ir_a_login()
        login_page.verificar_titulo()
        login_page.llenar_email(email)
        login_page.llenar_password(password)
    
    with allure.step("Hacer clic en login"):
        login_page.hacer_click_login()
    
    with allure.step("Verificar resultado según tipo de usuario"):
        if es_valido:
            # Para usuarios válidos (VALIDO, EMISOR, RECEPTOR)
            login_page.verificar_mensaje_exito()
            login_page.verificar_login_exitoso()
        else:
            # Para usuarios inválidos (INVALIDO)
            login_page.verificar_mensaje_error()


# ==========================================
# TESTS ESPECÍFICOS (Sin DDT)
# ==========================================

@allure.feature("Autenticación")
@allure.story("Validación de Campos Obligatorios")
@allure.severity(allure.severity_level.NORMAL)
def test_TC003_login_campos_vacios_no_redirige(page: Page):
    """TC-003: Test específico - campos vacíos (sin DDT porque es caso único)"""
    login_page = LoginPage(page)
    
    with allure.step("Navegar a la página de login"):
        login_page.ir_a_login()
    
    with allure.step("Verificar que estamos en login"):
        login_page.verificar_url_login()
    
    with allure.step("Hacer clic en 'Iniciar sesión' SIN llenar campos"):
        login_page.hacer_click_login()
    
    with allure.step("Verificar que permanece en página de login (NO redirige)"):
        login_page.verificar_url_login()
        
    with allure.step("Verificar que NO aparece mensaje de éxito"):
        login_page.verificar_que_no_hay_mensaje_exito()


@allure.feature("Autenticación")
@allure.story("Validación Nativa del Navegador")
@allure.severity(allure.severity_level.NORMAL)
def test_TC004_login_validacion_nativa_html5(page: Page):
    """TC-004: Test específico - validación HTML5 (sin DDT porque es caso técnico único)"""
    login_page = LoginPage(page)
    
    with allure.step("Navegar a la página de login"):
        login_page.ir_a_login()
    
    with allure.step("Verificar que los campos tienen validación requerida"):
        email_input = page.locator(login_page.input_email)
        password_input = page.locator(login_page.input_password)
        
        email_required = email_input.get_attribute('required')
        password_required = password_input.get_attribute('required')
        
        assert email_required is not None, "Campo email debe tener atributo required"
        assert password_required is not None, "Campo password debe tener atributo required"
    
    with allure.step("Intentar hacer click en botón con campos vacíos"):
        login_page.hacer_click_login()
    
    with allure.step("Verificar estado de validación nativo del navegador"):
        email_is_valid = email_input.evaluate("el => el.validity.valid")
        password_is_valid = password_input.evaluate("el => el.validity.valid")
        
        assert email_is_valid == False, "Campo email debe ser inválido cuando está vacío"
        assert password_is_valid == False, "Campo password debe ser inválido cuando está vacío"
    
    with allure.step("Leer mensajes de validación nativos"):
        email_validation_msg = email_input.evaluate("el => el.validationMessage")
        password_validation_msg = password_input.evaluate("el => el.validationMessage")
        
        print(f"Mensaje email: '{email_validation_msg}'")
        print(f"Mensaje password: '{password_validation_msg}'")
        
        assert len(email_validation_msg) > 0, "Debe haber mensaje de validación para email"
        assert len(password_validation_msg) > 0, "Debe haber mensaje de validación para password"
    
    with allure.step("Verificar que permanece en login (no se envió el form)"):
        login_page.verificar_url_login()


# ==========================================
# RESUMEN DE LO QUE HACE ESTE ARCHIVO:
# ==========================================
"""
EJECUCIÓN:
1. test_login_ddt se ejecuta 4 veces automáticamente:
   - test_login_ddt[VALIDO] → login exitoso
   - test_login_ddt[INVALIDO] → login fallido  
   - test_login_ddt[EMISOR] → login exitoso
   - test_login_ddt[RECEPTOR] → login exitoso

2. test_TC003_campos_vacios → 1 vez (test específico)

3. test_TC004_validacion_html5 → 1 vez (test específico)

TOTAL: 6 ejecuciones de tests (4 DDT + 2 específicos)

En Allure aparecen como 6 tests separados con reportes individuales.
"""