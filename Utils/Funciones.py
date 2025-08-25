from playwright.sync_api import Page, expect
import os
import time
import re
from datetime import datetime

class Funcion:
    def __init__(self, page: Page):
        self.page = page
    
    # === FUNCIONES DE TEXTO ===
    def llenar_texto(self, selector: str, texto: str, limpiar: bool = True, tiempo: float = 0.5):
        """Llenar un campo de texto con validaciones robustas"""
        elemento = self.page.locator(selector)
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()
        elemento.highlight()
        
        if limpiar:
            elemento.fill("")
            expect(elemento).to_be_empty()
        
        elemento.fill(texto)
        time.sleep(tiempo)
    
    def llenar_texto_calendario(self, selector: str, texto: str, tiempo: float = 0.5):
        """Llenar campo de calendario sin limpiar primero"""
        elemento = self.page.locator(selector)
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()
        elemento.highlight()
        elemento.fill(texto)
        time.sleep(tiempo)
    
    # === FUNCIONES DE CLICK ===
    def click_boton(self, selector: str, tiempo: float = 0.5):
        """Hacer click con validaciones robustas"""
        elemento = self.page.locator(selector)
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()
        elemento.highlight()
        elemento.click()
        time.sleep(tiempo)
    
    def click_primer_elemento(self, selector: str, tiempo: float = 0.5):
        """Hacer click en el primer elemento que coincida"""
        self.page.locator(selector).first.click()
        time.sleep(tiempo)
    
    def click_con_screenshot(self, selector: str, ruta_imagen: str, tiempo: float = 0.5):
        """Click + captura de pantalla"""
        elemento = self.page.locator(selector)
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()
        elemento.highlight()
        elemento.click()
        self.page.screenshot(path=ruta_imagen)
        time.sleep(tiempo)
    
    # === FUNCIONES DE COMBO BOX ===
    def seleccionar_combo_por_valor(self, selector: str, valor: str, tiempo: float = 0.5):
        """Seleccionar opción de combo por valor (select HTML tradicional)"""
        elemento = self.page.locator(selector)
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()
        elemento.highlight()
        elemento.select_option(valor)
        time.sleep(tiempo)
    
    def seleccionar_combo_por_label(self, selector: str, label: str, tiempo: float = 0.5):
        """Seleccionar opción de combo por label (select HTML tradicional)"""
        elemento = self.page.locator(selector)
        expect(elemento).to_be_visible()
        expect(elemento).to_be_enabled()
        elemento.highlight()
        elemento.select_option(label=label)
        time.sleep(tiempo)
    
    def seleccionar_combo_moderno(self, selector_combo: str, opcion_texto: str):
        """Seleccionar opción en combo moderno (div/ul con roles)"""
        self.page.locator(selector_combo).click()
        self.page.get_by_role("option", name=opcion_texto).click()
    
    def seleccionar_primera_opcion_combo(self, selector_combo: str):
        """Seleccionar la primera opción de un combo moderno"""
        self.page.locator(selector_combo).click()
        self.page.get_by_role("option").first.click()
    
    # === FUNCIONES DE VALIDACIÓN ===
    def validar_texto_exacto(self, selector: str, texto_esperado: str, tiempo: float = 0.5):
        """Validar texto exacto"""
        elemento = self.page.locator(selector)
        elemento.wait_for(state="visible")
        expect(elemento).to_have_text(texto_esperado)
        time.sleep(tiempo)
    
    def validar_texto_contiene(self, selector: str, texto: str, tiempo: float = 0.5):
        """Validar que elemento contiene texto"""
        elemento = self.page.locator(selector)
        elemento.wait_for(state="visible")
        expect(elemento).to_contain_text(texto)
        time.sleep(tiempo)
    
    def validar_elemento_visible(self, selector: str, timeout: int = 5000):
        """Validar que elemento es visible"""
        elemento = self.page.locator(selector)
        expect(elemento).to_be_visible(timeout=timeout)
    
    def validar_titulo_pagina(self, titulo: str, tiempo: float = 0.5):
        """Validar título de la página"""
        expect(self.page).to_have_title(titulo)
        time.sleep(tiempo)
    
    def validar_url(self, url_esperada: str, es_regex: bool = False, tiempo: float = 0.5):
        """Validar URL actual"""
        if es_regex:
            expect(self.page).to_have_url(re.compile(url_esperada))
        else:
            expect(self.page).to_have_url(url_esperada)
        time.sleep(tiempo)
    
    def validar_input_valor(self, selector: str, valor_esperado: str, tiempo: float = 0.5):
        """Validar valor de input"""
        elemento = self.page.locator(selector)
        expect(elemento).to_be_visible(timeout=tiempo * 1000)
        expect(elemento).to_have_value(valor_esperado)
    
    def validar_saldo_mxn(self, selector: str, tiempo: float = 0.5):
        """Validar formato de saldo en MXN"""
        elemento = self.page.locator(selector)
        expect(elemento).to_be_visible(timeout=tiempo * 1000)
        texto = elemento.text_content().strip()
        if not re.match(r"^\d{1,3}(?: \d{3})*\.\d{2} MXN$", texto):
            raise AssertionError(f"El texto '{texto}' no es un saldo válido en MXN.")
    
    # === FUNCIONES DE NAVEGACIÓN ===
    def navegar_a_url(self, url: str):
        """Navegar a URL y esperar carga"""
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")
    
    def refrescar_pagina(self, nombre_imagen: str = None, tiempo: float = 1):
        """Refrescar página y opcionalmente capturar"""
        self.page.reload()
        if nombre_imagen:
            self.capturar_pantalla(nombre_imagen)
        time.sleep(tiempo)
    
    # === FUNCIONES DE TECLADO Y MOUSE ===
    def presionar_tab(self, tiempo: float = 0.5):
        """Presionar tecla Tab"""
        self.page.keyboard.press("Tab")
        time.sleep(tiempo)
    
    def presionar_enter(self, tiempo: float = 0.5):
        """Presionar tecla Enter"""
        self.page.keyboard.press("Enter")
        time.sleep(tiempo)
    
    def click_coordenadas(self, x: int, y: int, tiempo: float = 0.5):
        """Click en coordenadas específicas"""
        self.page.mouse.click(x, y)
        time.sleep(tiempo)
    
    def scroll_xy(self, x: int, y: int):
        """Scroll usando coordenadas"""
        self.page.mouse.wheel(x, y)
    
    # === FUNCIONES DE ARCHIVOS ===
    def subir_archivo(self, selector: str, ruta_archivo: str, tiempo: float = 0.5):
        """Subir archivo"""
        self.page.locator(selector).set_input_files(ruta_archivo)
        time.sleep(tiempo)
    
    def subir_archivo_con_screenshot(self, selector: str, ruta_archivo: str, ruta_imagen: str, tiempo: float = 0.5):
        """Subir archivo + captura"""
        self.page.locator(selector).set_input_files(ruta_archivo)
        self.page.screenshot(path=ruta_imagen)
        time.sleep(tiempo)
    
    def remover_archivo(self, selector: str, tiempo: float = 0.5):
        """Remover archivo seleccionado"""
        self.page.locator(selector).set_input_files([])
        time.sleep(tiempo)
    
    # === FUNCIONES DE SCREENSHOT ===
    def capturar_pantalla(self, nombre_archivo: str, carpeta: str = "screenshots"):
        """Capturar screenshot mejorado"""
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        
        nombre_completo = f"{nombre_archivo}.png"
        ruta_completa = os.path.join(carpeta, nombre_completo)
        
        self.page.screenshot(path=ruta_completa)
        print(f"📸 Screenshot guardado en: {ruta_completa}")
        return ruta_completa
    
    # === FUNCIONES DE UTILIDAD ===
    def esperar(self, tiempo: float = 0.5):
        """Espera simple"""
        time.sleep(tiempo)
    
    def esperar_elemento(self, selector: str, timeout: int = 5000):
        """Esperar que elemento aparezca"""
        self.page.locator(selector).wait_for(state="visible", timeout=timeout)

    # Mantener funciones actuales para compatibilidad
    def validar_texto(self, selector: str, texto_esperado: str):
        """Compatibilidad - usar validar_texto_exacto"""
        return self.validar_texto_exacto(selector, texto_esperado)
    
    def validar_elemento_contiene_texto(self, selector: str, texto: str):
        """Compatibilidad - usar validar_texto_contiene"""
        return self.validar_texto_contiene(selector, texto)