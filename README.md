# Playwright + pytest Automation

Proyecto de automatización de pruebas usando Playwright con pytest y reportes con Allure.

## Setup
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install pytest playwright allure-pytest python-dotenv

# Instalar navegador
playwright install chromium

# Instalar Allure CLI (para reportes)
brew install allure
```

## Estructura del Proyecto
```
playwright_E2E/
├── Pages/
│   ├── LoginPage.py         # Page Object para Login
│   └── RegistroPage.py      # Page Object para Registro
├── Tests/
│   ├── test_registro_exitoso.py
│   ├── test_registro_fallido.py
│   └── ...
├── Funciones.py             # Funciones base reutilizables
├── conftest.py              # Configuración de fixtures
├── pytest.ini              # Configuración de pytest y Allure
├── .env                     # Variables de entorno
├── test_login.py            # Tests de login
└── README.md                # Este archivo
```

## Ejecutar Tests
```bash
# Ejecutar todos los tests (con Allure configurado automáticamente)
pytest

# Ejecutar con más detalle
pytest -v

# Ejecutar por categorías
pytest -m login        # Solo tests de login
pytest -m registro     # Solo tests de registro  
pytest -m smoke        # Solo smoke tests

# Ejecutar test específico
pytest Tests/test_login.py -v

# Ejecutar con navegador visible
pytest --headed
```

## Reportes con Allure
```bash
# 1. Ejecutar tests (genera datos en allure-results/)
pytest

# 2. Generar y abrir reporte HTML
allure serve allure-results

# O generar reporte estático
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Reportes Nativos

### pytest-html (Reporte nativo de pytest)
```bash
# Instalar
pip install pytest-html

# Generar reporte
pytest --html=report.html --self-contained-html

# Abrir report.html en navegador
```

### Playwright HTML Report (Reporte nativo de Playwright)
```bash
# Instalar
pip install pytest-playwright

# Generar reporte
pytest --browser chromium --html=playwright-report.html

# Abrir playwright-report.html en navegador
```

### Trace Viewer (Herramienta más potente de Playwright)
```bash
# Tu conftest.py ya genera traces automáticamente
# Después de ejecutar cualquier test:
pytest Tests/test_login.py

# Ver trace paso a paso (interfaz interactiva)
playwright show-trace trace.zip

# Muestra: screenshots, network, código, timeline, etc.
```

## Debug y Desarrollo
```bash
# Playwright Inspector - interfaz gráfica para debug paso a paso
PWDEBUG=1 pytest nombre_del_test.py

# Ejecutar con navegador visible
pytest --headed

# Reducir velocidad para observar
pytest --slowmo 1000

# Combinar opciones
pytest test_login.py --headed --slowmo 1000 -v
```

## Trace Viewer (como UI Mode de JavaScript)
Para generar traces, primero configura tu `conftest.py` con tracing habilitado:
```python
# En conftest.py, agregar en la fixture page:
context.tracing.start(screenshots=True, snapshots=True, sources=True)
# ... después del test ...
context.tracing.stop(path="trace.zip")
```

Luego ejecutar y ver:
```bash
# 1. Ejecutar test (genera trace.zip automáticamente)
pytest test_login.py -v

# 2. Ver el trace en interfaz web
playwright show-trace trace.zip
```

## Herramientas de Análisis
```bash
# Reportes HTML simples
pip install pytest-html
pytest --html=report.html --self-contained-html
```

## Workflow recomendado
# 1. Desarrollar/debug con Inspector
PWDEBUG=1 pytest test_registro_exitoso.py

# 2. Ejecutar para generar trace
pytest test_registro_exitoso.py -v

# 3. Analizar resultados con Trace Viewer
playwright show-trace trace.zip

# Verificar sintaxis (rápido)
python -m py_compile test_login.py