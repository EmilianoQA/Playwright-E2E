# Playwright + pytest + Allure Automation

Proyecto de automatización E2E usando Playwright con pytest y reportes profesionales con Allure.

## Estructura del Proyecto

```
playwright_E2E/
├── Pages/
│   ├── LoginPage.py
│   └── RegistroPage.py
├── Tests/
│   ├── test_login.py
│   ├── test_registro.py
│   ├── test_registro_exitoso.py
│   └── test_registro_fallido.py
├── Funciones.py
├── conftest.py
├── pytest.ini
├── .env
└── README.md
```

## Setup

### 1. Crear y activar entorno virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install pytest playwright python-dotenv allure-pytest
```

### 3. Instalar navegadores de Playwright
```bash
playwright install chromium
```

### 4. Instalar Allure (para reportes)
```bash
brew install allure
```

### 5. Configurar variables de entorno
Crear archivo `.env` en la raíz del proyecto:
```properties
# URLs de la aplicación
BASE_URL=http://localhost:3000

# Credenciales de prueba
EMAIL_VALIDO=usuario@test.com
PASSWORD_VALIDO=password123

# Credenciales incorrectas para tests negativos
EMAIL_INCORRECTO=malo@test.com
PASSWORD_INCORRECTO=wrongpass
```

## Ejecución de Tests

### Comandos básicos
```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests específicos
pytest Tests/test_login.py

# Ejecutar con más detalle
pytest -v

# Ejecutar tests por categoría
pytest -k "exitoso"
pytest -k "fallido"
```

### Ver reportes de Allure
```bash
# Después de ejecutar tests
allure serve allure-results
```

### Ver traces de Playwright (para debugging)
```bash
playwright show-trace trace.zip
```

## Características

### 🎯 Tests Implementados
- **Login exitoso** con credenciales válidas
- **Login fallido** con credenciales incorrectas
- **Registro exitoso** con datos aleatorios
- **Registro fallido** con email existente

### 📊 Reportes Profesionales
- **Allure Reports** con features, stories y steps
- **Trace Viewer** de Playwright para debugging
- **Screenshots** automáticos en fallos
- **Timeline** detallado de ejecución

### 🏗️ Arquitectura
- **Page Object Model** para mantenibilidad
- **Funciones reutilizables** centralizadas
- **Variables de entorno** para configuración
- **Fixtures** de pytest para setup/teardown

### 🧪 Configuración Automatizada
- **pytest.ini** configurado para ejecución simple
- **Limpieza automática** de reportes anteriores
- **Tracing habilitado** por defecto
- **Markers** para categorización de tests

## Comandos Útiles

```bash
# Desarrollo
source .venv/bin/activate
pytest -v

# Reportes
allure serve allure-results

# Debugging
playwright show-trace trace.zip

# Git
git add .
git commit -m "descripción"
git push
```

## Notas

- Los tests usan **datos aleatorios** para registros
- **Allure** genera reportes automáticamente en cada ejecución
- **Traces** se guardan en `trace.zip` para debugging
- Las **variables de entorno** deben estar configuradas antes de ejecutar