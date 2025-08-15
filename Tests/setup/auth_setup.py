"""
Setup de autenticación para tests de transferencias
Crea 2 usuarios via API y guarda las sesiones
"""

import os
from playwright.sync_api import Browser
from Pages.LoginPage import LoginPage
from Pages.DashboardPage import DashboardPage  # Cambiar a DashboardPage
from Utils.api_helpers import api_helper


def setup_usuarios_transferencia(browser: Browser) -> dict:
    """
    Setup completo para tests de transferencias:
    1. Crear usuario emisor via API
    2. Login emisor + crear cuenta + depositar dinero
    3. Guardar sesión emisor
    4. Crear usuario receptor via API  
    5. Login receptor + crear cuenta
    6. Guardar sesión receptor
    
    Returns:
        dict: Datos de emisor y receptor
    """
    
    print("🔧 Iniciando setup de usuarios para transferencias...")
    
    # 1. CREAR USUARIOS VIA API
    print("📝 Creando usuarios via API...")
    emisor = api_helper.crear_usuario_via_api("Emisor", "Test")
    receptor = api_helper.crear_usuario_via_api("Receptor", "Test")
    
    if emisor["status"] != "success" or receptor["status"] != "success":
        raise Exception("Error creando usuarios via API")
    
    print(f"✅ Emisor creado: {emisor['email']}")
    print(f"✅ Receptor creado: {receptor['email']}")
    
    # 2. SETUP EMISOR (con dinero)
    print("💰 Configurando emisor...")
    context_emisor = browser.new_context()
    page_emisor = context_emisor.new_page()
    
    # Login emisor
    login_page = LoginPage(page_emisor)
    login_page.ir_a_login()
    login_page.hacer_login_completo(emisor["email"], emisor["password"])
    
    # Crear cuenta débito con dinero inicial
    dashboard_page = DashboardPage(page_emisor)
    dashboard_page.crear_cuenta_completa("Débito", "1000")  # $1000 inicial
    
    # Guardar sesión emisor
    context_emisor.storage_state(path="Tests/setup/emisor_session.json")
    context_emisor.close()
    
    # 3. SETUP RECEPTOR (sin dinero inicial)
    print("📥 Configurando receptor...")
    context_receptor = browser.new_context()
    page_receptor = context_receptor.new_page()
    
    # Login receptor
    login_page = LoginPage(page_receptor)
    login_page.ir_a_login()
    login_page.hacer_login_completo(receptor["email"], receptor["password"])
    
    # Crear cuenta débito (sin dinero inicial)
    dashboard_page = DashboardPage(page_receptor)
    dashboard_page.crear_cuenta_completa("Débito", "0")  # Sin dinero inicial
    
    # Guardar sesión receptor
    context_receptor.storage_state(path="Tests/setup/receptor_session.json")
    context_receptor.close()
    
    print("✅ Setup completado exitosamente!")
    
    return {
        "emisor": {
            "email": emisor["email"],
            "password": emisor["password"],
            "id": emisor["id"],
            "session_file": "Tests/setup/emisor_session.json"
        },
        "receptor": {
            "email": receptor["email"],
            "password": receptor["password"],
            "id": receptor["id"],
            "session_file": "Tests/setup/receptor_session.json"
        }
    }


def limpiar_sesiones():
    """Elimina archivos de sesión anteriores"""
    archivos = [
        "Tests/setup/emisor_session.json",
        "Tests/setup/receptor_session.json"
    ]
    
    for archivo in archivos:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"🗑️ Eliminado: {archivo}")
