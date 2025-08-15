# 🎭 Playwright E2E - Automatización Profesional

Proyecto de automatización E2E usando **Playwright + Python + Allure Reports** con arquitectura **Page Object Model** y **API Helpers**.

## 🏗️ Arquitectura del Proyecto

```
playwright_E2E/
├── Pages/                    # Page Object Model
│   ├── LoginPage.py         # Página de login
│   ├── RegistroPage.py      # Página de registro
│   ├── DashboardPage.py     # Dashboard principal
│   └── TransferenciasPage.py # Transferencias de dinero
├── Tests/                   # Tests organizados por funcionalidad
│   ├── setup/              # Setup de autenticación
│   │   └── auth_setup.py   # Crear usuarios + sesiones
│   ├── test_login.py       # TC001-TC004: Tests de login
│   ├── test_registro.py    # TC051-TC053: Tests de registro
│   ├── test_cuentas.py     # TC101-TC103: Tests de cuentas
│   ├── test_navegacion.py  # TC151-TC152: Tests de navegación
│   └── test_transferencias.py # TC201-TC202: Tests de transferencias
├── Utils/                   # Utilidades reutilizables
│   ├── api_helpers.py      # Crear usuarios via API
│   └── data_helpers.py     # Generar datos de prueba
├── Funciones.py            # Funciones centralizadas
├── conftest.py             # Configuración pytest
├── pytest.ini             # Configuración de pytest
├── package.json            # Scripts npm para ejecutar tests
├── requirements.txt        # Dependencias Python
└── TEST_CASES.md          # Registro de casos de prueba
```

## 🚀 Configuración del Entorno

### Prerrequisitos
- **Python 3.13+**
- **Node.js** (para npm scripts)
- **Redux Athena Bank** app corriendo en `localhost:3000`

### Instalación
```bash
# 1. Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Instalar navegadores de Playwright
playwright install

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones
```

## 🧪 Ejecución de Tests

### Comandos NPM (Recomendado)
```bash
# Todos los tests con reporte
npm run test:report

# Tests específicos
npm run test:all              # Todos los tests
npm run test:login            # Solo tests de login
npm run test:transferencias   # Solo tests de transferencias

# Solo generar reporte
npm run report
```

### Comandos Pytest Directos
```bash
# Ejecutar tests específicos
pytest Tests/test_transferencias.py -v

# Todos los tests
pytest -v

# Con Allure (manual)
pytest -v -p allure_pytest --alluredir=allure-results --clean-alluredir
allure serve allure-results
```

## 📊 Casos de Prueba Implementados

### 🔐 Autenticación (TC001-TC004)
- **TC001**: Login exitoso
- **TC002**: Login con credenciales incorrectas  
- **TC003**: Validación campos vacíos
- **TC004**: Validación HTML5 nativa

### 📝 Registro (TC051-TC053)
- **TC051**: Registro exitoso frontend
- **TC052**: Registro con usuario existente
- **TC053**: Registro via API + verificación E2E

### 💳 Gestión de Cuentas (TC101-TC103)
- **TC101**: Crear cuenta débito exitoso
- **TC102**: Eliminar cuenta existente
- **TC103**: Validación campos vacíos

### 🧭 Navegación (TC151-TC152)
- **TC151**: Enlace registro desde login
- **TC152**: Logout y protección de rutas

### 💸 Transferencias (TC201-TC202)
- **TC201**: Enviar dinero entre usuarios
- **TC202**: Verificar dinero recibido

## 🔧 Características Técnicas

### 🏛️ Arquitectura
- **Page Object Model**: Separación clara de responsabilidades
- **Setup con API**: Usuarios creados automáticamente via API
- **Sesiones guardadas**: Sin login repetido entre tests
- **Tests con dependencias**: TC202 depende de TC201

### 📈 Reportes
- **Allure Reports**: Reportes profesionales con screenshots
- **Limpieza automática**: Reportes frescos en cada ejecución
- **Screenshots automáticos**: En caso de fallos
- **Datos adjuntos**: Información relevante en reportes

### 🔄 Reutilización
- **API Helpers**: Crear usuarios/cuentas programáticamente
- **Data Helpers**: Generar datos de prueba dinámicos
- **Funciones centralizadas**: Métodos reutilizables
- **Utils modulares**: Componentes independientes

## 🛠️ Configuración Avanzada

### Variables de Entorno (.env)
```env
# URLs de la aplicación
BASE_URL=http://localhost:3000
API_BASE_URL=http://localhost:6007

# Credenciales de prueba
EMAIL_VALIDO=test@example.com
PASSWORD_VALIDO=password123
EMAIL_INCORRECTO=wrong@example.com
PASSWORD_INCORRECTO=wrongpass
```

### Configuración Pytest (pytest.ini)
```ini
[tool:pytest]
addopts = --alluredir=allure-results --clean-alluredir -p allure_pytest
testpaths = Tests
python_files = test_*.py
python_functions = test_*
markers =
    smoke: marca tests como smoke tests
    regression: marca tests como regression tests
```

## 📋 Flujo de Trabajo

### Tests Independientes
```bash
# Tests que no requieren setup especial
npm run test:login
npm run test:registro
npm run test:cuentas
npm run test:navegacion
```

### Tests con Setup Automático
```bash
# Tests de transferencias (requieren 2 usuarios)
npm run test:transferencias
```

**El setup automáticamente:**
1. Crea 2 usuarios via API (emisor y receptor)
2. Hace login de ambos usuarios
3. Crea cuentas (emisor con $1000, receptor con $0)
4. Guarda las sesiones para reutilizar
5. Ejecuta tests de transferencias

## 🎯 Buenas Prácticas Implementadas

### ✅ Código Limpio
- Nombres descriptivos en español
- Separación de responsabilidades
- Reutilización de componentes
- Documentación clara

### ✅ Tests Robustos
- Selectores estables
- Validaciones múltiples
- Manejo de errores
- Screenshots automáticos

### ✅ Mantenibilidad
- Arquitectura escalable
- Configuración centralizada
- Utils reutilizables
- Documentación actualizada

## 🚀 Próximos Pasos

- [ ] CI/CD con GitHub Actions
- [ ] Tests paralelos
- [ ] Data-driven testing
- [ ] Integración con bases de datos
- [ ] Tests de performance

## 📞 Contacto

**Proyecto desarrollado como parte del aprendizaje de automatización E2E profesional.**

---

*Automatización E2E • Playwright • Python • Allure Reports • Page Object Model*
