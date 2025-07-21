from playwright.sync_api import sync_playwright

def test_abrir_pagina():
    with sync_playwright() as p:
        # Abrir navegador
        browser = p.chromium.launch(headless=False)  # headless=False para ver el navegador
        
        # Crear una página
        page = browser.new_page()
        
        # Ir a una página web
        page.goto("https://ateneaconocimientos.com")
        
        # Verificar que llegamos
        assert "Atenea Conocimientos" in page.title()
        
        # Cerrar navegador
        browser.close()