import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    headless_mode = os.getenv("PLAYWRIGHT_HEADLESS", "0") == "1"
    slow_mo_delay = int(os.getenv("PLAYWRIGHT_SLOWMO", "100"))  # Valor en milisegundos
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless_mode,
            slow_mo=slow_mo_delay
        )
        yield browser
        browser.close()

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

@pytest.fixture  # Sin scope = se ejecuta PARA CADA test
def page(browser):
    """Crea una nueva página/pestaña limpia para cada test"""
    context = browser.new_context()  # Sesión aislada (cookies, localStorage independientes)
    
    # AGREGAR TRACING
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()        # Nueva pestaña
    yield page                       # Proporciona la página al test
    
    # GUARDAR TRACE
    context.tracing.stop(path="trace.zip")
    context.close()                  # Limpia la sesión después del test