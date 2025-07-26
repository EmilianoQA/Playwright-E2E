from playwright.sync_api import Page, expect
from Pages.RegistroPage import RegistroPage
import os
from dotenv import load_dotenv

load_dotenv()

def test_registro_exitoso(page: Page):
    registro_page = RegistroPage(page)
    
    # Ir a registro y verificar página
    registro_page.ir_a_registro()
    registro_page.verificar_url_registro()
    registro_page.verificar_titulo()
    
    # Generar datos aleatorios
    email = registro_page.generar_email_aleatorio()
    password = registro_page.generar_password_aleatorio()
    
    # Hacer registro completo
    registro_page.hacer_registro_completo("Test", "Usuario", email, password)
