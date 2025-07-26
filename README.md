# Playwright + pytest Automation

Proyecto de automatización de pruebas usando Playwright con pytest.

## Setup
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install pytest playwright

# Instalar navegador
playwright install chromium
```

## Estructura del Proyecto
```
proyecto_playwright/
├── conftest.py              # Configuración de fixtures para pytest
├── test_mi_primer_test.py   # Test básico de pytest
├── test_playwright_basico.py # Test básico con Playwright
├── test_login.py            # Test de login para aplicación local
├── requirements.txt         # Dependencias del proyecto
├── .gitignore              # Archivos a ignorar en Git
└── README.md               # Este archivo
```

## Ejecutar Tests
```bash
# Ejecutar todos los tests
pytest

# Ejecutar con más detalle
pytest -v

# Ejecutar test específico
pytest test_login.py -v

# Ejecutar con navegador visible y lento para debug
pytest test_login.py --headed --slowmo 1000

# Debug con Playwright Inspector (modo paso a paso)
PWDEBUG=1 pytest test_login.py

# Ejecutar múltiples tests
pytest test_playwright_basico.py test_login.py -v
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