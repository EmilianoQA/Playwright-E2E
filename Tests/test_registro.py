import allure
from playwright.sync_api import Page, expect
from Pages.LoginPage import LoginPage
from Pages.RegistroPage import RegistroPage
from Funciones import Funcion
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# CASOS DE PRUEBA - REGISTRO DE USUARIOS
# ==========================================

@allure.feature("Registro de Usuario")
@allure.story("Registro Exitoso")
@allure.severity(allure.severity_level.CRITICAL)
def test_TC051_registro_exitoso_frontend(page: Page):
    """TC-051: Verificar registro exitoso usando formulario frontend"""
    
    funcion = Funcion(page)
    
    URL_REGISTRO = f"{os.getenv('BASE_URL')}/signup"
    URL_LOGIN = f"{os.getenv('BASE_URL')}/login"
    
    titulo_registro = '[data-testid="titulo-registro"]'
    input_nombre = 'input[name="firstName"]'
    input_apellido = 'input[name="lastName"]'
    input_email = 'input[name="email"]'
    input_password = 'input[name="password"]'
    boton_registro = '[data-testid="boton-registrarse"]'
    mensaje_exito = 'text="Registro exitoso!"'
    
    def generar_email_aleatorio():
        timestamp = str(int(time.time()))[-6:]
        return f"test{timestamp}@example.com"
    
    def generar_password_aleatorio():
        return "password123"
    
    with allure.step("Navegar a página de registro"):
        funcion.navegar_a_url(URL_REGISTRO)
        funcion.validar_url(URL_REGISTRO)
        funcion.validar_texto(titulo_registro, 'Registrarse')
    
    with allure.step("Generar datos únicos para el registro"):
        email_aleatorio = generar_email_aleatorio()
        password_aleatorio = generar_password_aleatorio()
        
        allure.attach(f"Email: {email_aleatorio}", name="Email Generado", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Llenar formulario de registro"):
        funcion.llenar_texto(input_nombre, "Test")
        funcion.llenar_texto(input_apellido, "Usuario")
        funcion.llenar_texto(input_email, email_aleatorio)
        funcion.llenar_texto(input_password, password_aleatorio)
    
    with allure.step("Enviar formulario de registro"):
        funcion.click_boton(boton_registro)
    
    with allure.step("Verificar registro exitoso"):
        funcion.validar_elemento_visible(mensaje_exito)
        funcion.validar_url(URL_LOGIN)


@allure.feature("Registro de Usuario")
@allure.story("Registro Fallido")
@allure.severity(allure.severity_level.NORMAL)
def test_TC052_registro_fallido_usuario_existente(page: Page):
    """TC-052: Verificar que el registro falla al intentar crear un usuario con email ya existente"""
    
    registro_page = RegistroPage(page)

    with allure.step("Navegar a la página de registro"):
        registro_page.ir_a_registro()

    with allure.step("Verificar que estamos en la URL de registro"):
        registro_page.verificar_url_registro()
        registro_page.verificar_titulo()

    with allure.step("Preparar datos de registro con email existente"):
        email_existente = os.getenv('EMAIL_VALIDO')
        password = registro_page.generar_password_aleatorio()
        
        allure.attach(f"Email existente: {email_existente}", name="Email Utilizado", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Llenar formulario de registro"):
        registro_page.llenar_nombre("Nuevo")
        registro_page.llenar_apellido("Usuario")
        registro_page.llenar_email(email_existente)
        registro_page.llenar_password(password)

    with allure.step("Enviar formulario"):
        registro_page.hacer_click_registro()

    with allure.step("Verificar mensaje de error por usuario existente"):
        registro_page.verificar_mensaje_error()


@allure.feature("Registro de Usuario")
@allure.story("Creación via API + Verificación E2E")
@allure.severity(allure.severity_level.CRITICAL)
def test_TC053_registro_usuario_via_api_y_e2e(page: Page):
    """TC-053: Test híbrido - Crear usuario por API, verificar login E2E"""
    
    def generar_usuario_aleatorio():
        timestamp = str(int(time.time()))[-6:]
        return {
            "firstName": f"Test{timestamp}",
            "lastName": f"User{timestamp}",
            "email": f"test{timestamp}@example.com", 
            "password": "password123"
        }
    
    login_page = LoginPage(page)
    API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:6007')
    
    with allure.step("Generar datos aleatorios para nuevo usuario"):
        usuario_data = generar_usuario_aleatorio()
        allure.attach(f"Usuario a crear: {usuario_data['email']}", name="Datos Usuario", attachment_type=allure.attachment_type.TEXT)
    
    with allure.step("Crear usuario via API POST"):
        response = requests.post(f"{API_BASE_URL}/api/auth/signup", json=usuario_data)
        assert response.status_code == 201, f"Error creando usuario: {response.status_code}"
        
        # Parsear respuesta
        response_data = response.json()
        assert "token" in response_data, "Respuesta debe contener token"
        assert "user" in response_data, "Respuesta debe contener datos de usuario"
        assert response_data["user"]["email"] == usuario_data["email"]
        
        allure.attach(f"Usuario creado - ID: {response_data['user']['id']}", name="API Response", attachment_type=allure.attachment_type.TEXT)
        
    with allure.step("Hacer login E2E con el usuario recién creado"):
        login_page.ir_a_login()
        login_page.hacer_login_completo(usuario_data['email'], usuario_data['password'])
        
    with allure.step("Verificar acceso exitoso al dashboard"):
        login_page.verificar_login_exitoso()
