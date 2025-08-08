import allure
from playwright.sync_api import Page
from Pages.LoginPage import LoginPage
from Pages.DashboardPage import DashboardPage
import os
from dotenv import load_dotenv

load_dotenv()

@allure.feature("Navegación")
@allure.story("Enlace de Registro")
@allure.severity(allure.severity_level.NORMAL)
def test_enlace_registro_desde_login(page: Page):
    """Verificar navegación desde login hacia registro usando enlace"""
    
    login_page = LoginPage(page)
    
    with allure.step("Navegar a la página de login"):
        login_page.ir_a_login()
    
    with allure.step("Verificar que estamos en login"):
        login_page.verificar_url_login()
    
    with allure.step("Hacer clic en el enlace '¿No tienes cuenta? Regístrate'"):
        # Click en el enlace que lleva a la página de registro
        login_page.hacer_click_enlace_registro()
    
    with allure.step("Verificar que se redirige a página de registro"):
        # Debe navegar a /signup
        login_page.verificar_redireccion_a_registro()


@allure.feature("Autenticación")
@allure.story("Logout y Protección de Rutas")
@allure.severity(allure.severity_level.CRITICAL)
def test_logout_y_proteccion_rutas(page: Page):
    """Test completo: Login → Logout → Verificar protección de rutas"""
    
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    # PARTE 1: Login exitoso (reutilizar lógica existente)
    with allure.step("Realizar login exitoso para acceder al dashboard"):
        login_page.ir_a_login()
        email_correcto = os.getenv('EMAIL_VALIDO')
        password_correcto = os.getenv('PASSWORD_VALIDO')
        login_page.hacer_login_completo(email_correcto, password_correcto)
    
    # PARTE 2: Logout desde dashboard
    with allure.step("Hacer logout desde el dashboard"):
        # Hacer clic en el botón "Cerrar Sesión"
        dashboard_page.hacer_logout()
        
    with allure.step("Verificar redirección a login tras logout"):
        # Después del logout debe volver a /login
        login_page.verificar_url_login()
    
    # PARTE 3: Protección de rutas - intentar acceder sin sesión
    with allure.step("Intentar acceder directamente al dashboard sin sesión"):
        # Navegar directamente a la URL del dashboard
        page.goto(dashboard_page.url_dashboard)
        
    with allure.step("Verificar que redirige a login (ruta protegida)"):
        # El sistema debe redirigir automáticamente a /login
        # porque la ruta /dashboard está protegida
        login_page.verificar_url_login()
