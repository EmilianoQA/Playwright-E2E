from playwright.sync_api import Page, expect
import os
from datetime import datetime

class Funcion:
    def __init__(self, page: Page):
        self.page = page
    
    def llenar_texto(self, selector: str, texto: str):
        """Llenar un campo de texto con waits explícitos"""
        campo = self.page.locator(selector)
        campo.wait_for(state="visible")
        campo.fill(texto)
    
    def click_boton(self, selector: str):
        """Hacer click en un botón con waits explícitos"""
        boton = self.page.locator(selector)
        boton.wait_for(state="visible")
        expect(boton).to_be_enabled()
        boton.click()
    
    def validar_texto(self, selector: str, texto_esperado: str):
        """Validar que un elemento contiene el texto esperado"""
        elemento = self.page.locator(selector)
        elemento.wait_for(state="visible")
        expect(elemento).to_have_text(texto_esperado)
    
    def validar_url(self, url_esperada: str, timeout: int = 10000):
        """Validar que estamos en la URL correcta"""
        self.page.wait_for_url(url_esperada, timeout=timeout)
        expect(self.page).to_have_url(url_esperada)
    
    def validar_elemento_visible(self, selector: str):
        """Validar que un elemento es visible"""
        elemento = self.page.locator(selector)
        elemento.wait_for(state="visible")
        expect(elemento).to_be_visible()
    
    def validar_elemento_contiene_texto(self, selector: str, texto: str):
        """Validar que un elemento contiene cierto texto"""
        elemento = self.page.locator(selector)
        elemento.wait_for(state="visible")
        expect(elemento).to_contain_text(texto)
    
    def navegar_a_url(self, url: str):
        """Navegar a una URL y esperar que cargue"""
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
    
    def capturar_pantalla(self, nombre_archivo: str, carpeta: str = "screenshots"):
        """Capturar screenshot y guardarlo con nombre específico"""
        # Crear carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        
        # Sin timestamp - sobrescribe archivo anterior
        nombre_completo = f"{nombre_archivo}.png"
        ruta_completa = os.path.join(carpeta, nombre_completo)
        
        # Capturar screenshot
        self.page.screenshot(path=ruta_completa)
        print(f"Screenshot guardado en: {ruta_completa}")
