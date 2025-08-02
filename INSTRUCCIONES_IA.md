# 🤖 INSTRUCCIONES PARA ASISTENTES DE IA

## 📍 Contexto del Proyecto
- **Ruta**: `/Users/emiliano/Documents/Testing/Cursos/Playwright  E2E/playwright_E2E`
- **Origen**: Curso de Playwright con TypeScript
- **Objetivo**: Adaptar todo a pytest (Python) porque no sé TypeScript
- **Estado**: Proyecto funcional con arquitectura sólida implementada

## 🎯 Objetivo del Aprendizaje
Este es un **proyecto educativo** donde estoy aprendiendo automatización E2E. Necesito:
- Progresión de conceptos simples a complejos
- Explicaciones pedagógicas en comentarios
- Comprensión profunda de cada implementación

## 📋 Reglas de Trabajo OBLIGATORIAS

### 🚨 ANTES DE MODIFICAR CÓDIGO
- **SIEMPRE preguntar** antes de modificar cualquier archivo
- Mostrar propuesta del cambio y esperar confirmación
- Explicar el "por qué" del cambio propuesto

### 🎓 Enfoque Pedagógico
- Agregar **comentarios explicativos** en español
- Ir de lo **más fácil a lo más complejo**
- Explicar conceptos nuevos antes de implementarlos
- Contextualizar cada decisión técnica

### 💻 Estándares de Código
- Mantener arquitectura **Page Object Model**
- Usar funciones de `Funciones.py` para reutilización
- Conservar estructura de carpetas existente
- Mantener integración con Allure y pytest

## 🏗️ Arquitectura Actual

```
playwright_E2E/
├── Pages/              # Page Object Model
│   ├── LoginPage.py
│   ├── RegistroPage.py
│   └── DashboardPage.py
├── Tests/              # Tests organizados
│   ├── test_login.py
│   ├── test_registro.py
│   └── test_*.py
├── Funciones.py        # Funciones reutilizables centralizadas
├── conftest.py         # Fixtures y configuración pytest
├── pytest.ini         # Configuración pytest + Allure
├── .env               # Variables de entorno
└── README.md          # Documentación técnica
```

## ⚙️ Stack Tecnológico
- **Framework**: Playwright + pytest
- **Reportes**: Allure Reports
- **Arquitectura**: Page Object Model
- **Variables**: python-dotenv
- **Screenshots**: Automáticos en fallos
- **Tracing**: Habilitado para debugging

## 🎯 Características Implementadas
- ✅ Login exitoso/fallido
- ✅ Registro exitoso/fallido
- ✅ Page Objects bien estructurados
- ✅ Funciones reutilizables
- ✅ Reportes profesionales
- ✅ Screenshots automáticos
- ✅ Tracing para debugging
- ✅ Variables de entorno

## 📝 Cuando Trabajes Conmigo

### ✅ HAZ ESTO:
- Analiza el código existente antes de proponer cambios
- Pregunta qué concepto específico quiero aprender
- Propón mejoras incrementales
- Explica beneficios de cada cambio
- Usa comentarios educativos en el código

### ❌ NO HAGAS ESTO:
- Modificar código sin preguntar
- Cambios masivos de una vez
- Asumir mi nivel de conocimiento
- Saltar conceptos básicos
- Eliminar comentarios existentes

## 🎓 Progresión Sugerida
1. **Básico**: Selectores, clicks, validaciones simples
2. **Intermedio**: Manejo de datos, loops, condicionales
3. **Avanzado**: Paralelización, CI/CD, reporting avanzado

## 🚀 Cómo Empezar
Cuando un nuevo asistente de IA trabaje conmigo:
1. Lee este archivo completo
2. Revisa la estructura del proyecto
3. Pregunta qué específicamente quiero mejorar o aprender
4. Propón el siguiente paso lógico en mi aprendizaje
5. SIEMPRE pregunta antes de modificar código