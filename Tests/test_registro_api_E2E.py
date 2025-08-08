import requests
import allure
import time
from playwright.sync_api import Page
from Pages.LoginPage import LoginPage

def generar_usuario_aleatorio():
    """Generar datos únicos para nuevo usuario"""
    timestamp = str(int(time.time()))[-6:]
    return {
        "firstName": f"Test{timestamp}",
        "lastName": f"User{timestamp}",
        "email": f"test{timestamp}@example.com", 
        "password": "password123"
    }

@allure.feature("Registro de Usuario")
@allure.story("Creación via API + Verificación E2E")
@allure.severity(allure.severity_level.CRITICAL)
def test_registro_usuario_via_api_y_e2e(page: Page):
    """Test híbrido: Crear usuario por API, verificar login E2E"""
    
    BASE_URL = "http://localhost:6007"
    
    with allure.step("Generar datos aleatorios para nuevo usuario"):
        usuario_data = generar_usuario_aleatorio()
        print(f"Usuario a crear: {usuario_data['email']}")
    
    with allure.step("Crear usuario via API POST"):
        response = requests.post(f"{BASE_URL}/api/auth/signup", json=usuario_data)
        assert response.status_code == 201, f"Error creando usuario: {response.status_code}"
        
        # Parsear respuesta
        response_data = response.json()
        assert "token" in response_data, "Respuesta debe contener token"
        assert "user" in response_data, "Respuesta debe contener datos de usuario"
        assert response_data["user"]["email"] == usuario_data["email"]
        
        print(f"Usuario creado exitosamente - ID: {response_data['user']['id']}")
        
    with allure.step("Hacer login E2E con el usuario recién creado"):
        login_page = LoginPage(page)
        login_page.ir_a_login()
        login_page.hacer_login_completo(usuario_data['email'], usuario_data['password'])
        
    with allure.step("Verificar acceso exitoso al dashboard"):
        login_page.verificar_login_exitoso()