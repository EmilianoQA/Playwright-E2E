from playwright.sync_api import Page, expect
from Pages.RegistroPage import RegistroPage
import os
from dotenv import load_dotenv

load_dotenv()

def test_registro_fallido_usuario_existente(page: Page):
    registro_page = RegistroPage(page)
    
    # Ir a registro y verificar página
    registro_page.ir_a_registro()
    registro_page.verificar_url_registro()
    registro_page.verificar_titulo()
    
    # Usar credenciales que ya existen (del .env)
    email_existente = os.getenv('EMAIL_VALIDO')  # Email que ya está registrado
    password = registro_page.generar_password_aleatorio()
    
    # Intentar registrar con email existente
    registro_page.llenar_nombre("Nuevo")
    registro_page.llenar_apellido("Usuario")
    registro_page.llenar_email(email_existente)
    registro_page.llenar_password(password)
    registro_page.hacer_click_registro()
    
    # Verificar que aparece error y NO redirige
    registro_page.verificar_mensaje_error()
    registro_page.verificar_url_registro()  # Se queda en la misma página
