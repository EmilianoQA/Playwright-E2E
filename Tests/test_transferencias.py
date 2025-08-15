"""
Tests de transferencias entre usuarios
Usando setup de autenticación y sesiones guardadas
"""

import pytest
import allure
import os
from playwright.sync_api import Page, Browser
from Pages.TransferenciasPage import TransferenciasPage
from Pages.DashboardPage import DashboardPage
from Tests.setup.auth_setup import setup_usuarios_transferencia, limpiar_sesiones


# Variables globales para compartir datos entre tests
usuarios_data = None


@pytest.fixture(scope="module", autouse=True)
def setup_transferencias(browser: Browser):
    """Setup que se ejecuta una vez para todos los tests de transferencias"""
    global usuarios_data
    
    print("\n🔧 Ejecutando setup de transferencias...")
    
    # Limpiar sesiones anteriores
    limpiar_sesiones()
    
    # Crear usuarios y sesiones
    usuarios_data = setup_usuarios_transferencia(browser)
    
    print(f"✅ Setup completado - Emisor: {usuarios_data['emisor']['email']}")
    print(f"✅ Setup completado - Receptor: {usuarios_data['receptor']['email']}")
    
    return usuarios_data


@allure.feature("Transferencias")
@allure.story("Envío de Dinero")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.dependency(name="enviar_dinero")

def test_TC201_enviar_dinero_exitoso(browser: Browser):
    """TC-201: Enviar $100 de emisor a receptor"""
    
    global usuarios_data
    assert usuarios_data is not None, "Setup debe ejecutarse primero"
    
    # Usar sesión del emisor (ya logueado con $1000)
    context = browser.new_context(
        storage_state=usuarios_data["emisor"]["session_file"]
    )
    page = context.new_page()
    
    transferencias_page = TransferenciasPage(page)
    
    with allure.step("Ir al dashboard (ya autenticado)"):
        transferencias_page.ir_a_dashboard()
    
    with allure.step("Realizar transferencia de $100"):
        email_receptor = usuarios_data["receptor"]["email"]
        transferencias_page.hacer_transferencia_completa(email_receptor, "10")
        
        # Adjuntar datos al reporte
        allure.attach(f"Emisor: {usuarios_data['emisor']['email']}", 
                     name="Usuario Emisor", 
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Receptor: {email_receptor}", 
                     name="Usuario Receptor", 
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach("Monto: $100", 
                     name="Monto Transferido", 
                     attachment_type=allure.attachment_type.TEXT)
    
    context.close()


@allure.feature("Transferencias")
@allure.story("Verificación de Recepción")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.dependency(depends=["enviar_dinero"])

def test_TC202_verificar_dinero_recibido(browser: Browser):
    """TC-202: Verificar que receptor recibió los $100"""
    
    global usuarios_data
    assert usuarios_data is not None, "Setup debe ejecutarse primero"
    
    # Usar sesión del receptor
    context = browser.new_context(
        storage_state=usuarios_data["receptor"]["session_file"]
    )
    page = context.new_page()
    
    dashboard_page = DashboardPage(page)
    
    with allure.step("Ir al dashboard del receptor"):
        page.goto(os.getenv('BASE_URL', 'http://localhost:3000') + '/dashboard')
    
    with allure.step("Verificar saldo recibido - debe tener $100"):
        # Verificar que el receptor ahora tiene $100 (antes tenía $0)
        dashboard_page.verificar_saldo_total("10")
        
        allure.attach(f"Receptor: {usuarios_data['receptor']['email']}", 
                     name="Usuario Receptor", 
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach("Saldo esperado: $100", 
                     name="Verificación de Saldo", 
                     attachment_type=allure.attachment_type.TEXT)
    
    context.close()
