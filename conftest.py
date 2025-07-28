import pytest
from playwright.sync_api import sync_playwright, Playwright, Browser, Page
import os

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar screenshot solo en fallos"""
    outcome = yield
    rep = outcome.get_result()
    
    # Si el test falló, tomar screenshot
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get('page')
        if page:
            # Crear carpeta si no existe
            if not os.path.exists('screenshots'):
                os.makedirs('screenshots')
            # Capturar screenshot del fallo
            page.screenshot(path=f"screenshots/FAILED_{item.name}.png")
            print(f"Screenshot de fallo guardado: screenshots/FAILED_{item.name}.png")

@pytest.fixture(scope="session")  # Se ejecuta UNA VEZ por toda la sesión de testing
def playwright():
    """Inicia la instancia principal de Playwright"""
    with sync_playwright() as p:
        yield p  # Proporciona el objeto playwright a otros fixtures
        # Al salir del 'with', se cierra automáticamente

@pytest.fixture(scope="session")  # Se ejecuta UNA VEZ, reutiliza el mismo navegador
def browser(playwright: Playwright):
    """Abre el navegador Chromium para todos los tests"""
    browser = playwright.chromium.launch(headless=False)  # Ventana visible
    yield browser  # Proporciona el navegador a los tests
    browser.close()  # Se ejecuta al final de todos los tests

@pytest.fixture  # Sin scope = se ejecuta PARA CADA test
def page(browser: Browser):
    """Crea una nueva página/pestaña limpia para cada test"""
    context = browser.new_context()  # Sesión aislada (cookies, localStorage independientes)
    
    # AGREGAR TRACING
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()        # Nueva pestaña
    yield page                       # Proporciona la página al test
    
    # GUARDAR TRACE
    context.tracing.stop(path="trace.zip")
    context.close()                  # Limpia la sesión después del test