# INSTRUCTIVO PRIVADO - Athena Bank E2E

---

## ¿De qué se trata el proyecto?

Este proyecto automatiza pruebas end-to-end (E2E) para Athena Bank, una app bancaria fullstack. Simula el uso real de la app: login, registro, cuentas, transferencias y navegación, verificando que todo funcione como espera el usuario.

---

## Beneficios o cosas que destacan el proyecto

- **Uso de Page Object Model (POM):** Cada página o sección de la app tiene su propia clase, lo que facilita el mantenimiento y la escalabilidad de los tests.
- **Data Driven Testing (DDT):** Los datos de prueba (usuarios, credenciales, etc.) están separados en archivos dedicados, permitiendo agregar o modificar casos fácilmente sin tocar la lógica de los tests.
- **Tests parametrizados:** Se utilizan decoradores como `pytest.mark.parametrize` para ejecutar el mismo test con diferentes datos, acelerando la cobertura y reduciendo la duplicación de código.
- **Reportes visuales con Allure:** Los resultados de los tests se presentan en reportes gráficos y detallados, facilitando la revisión y el análisis.
- **Integración continua (CI/CD):** El proyecto está preparado para ejecutarse automáticamente en GitHub Actions, levantando el backend y frontend, corriendo los tests y generando los reportes.
- **Separación clara de responsabilidades:** El código de automatización está organizado en carpetas específicas para tests, páginas, funciones, datos y utilidades, lo que mejora la legibilidad y el orden.

---

## ¿Qué tecnologías usamos y para qué?

- **Playwright (Python):** Automatiza el navegador para simular acciones de usuario.
- **Pytest:** Framework para organizar y ejecutar los tests.
- **Allure:** Genera reportes visuales de los resultados de los tests.
- **Node.js + Express + MongoDB:** Backend de la app (API y base de datos).
- **React + Vite:** Frontend de la app.
- **GitHub Actions:** CI/CD para ejecutar los tests automáticamente en cada cambio.

---

## ¿Qué hace cada carpeta?

- **Tests/**  
  Contiene todos los archivos de pruebas automatizadas (login, registro, cuentas, transferencias, navegación).

- **Pages/**  
  Implementa el patrón Page Object Model: cada archivo representa una página o sección de la app, encapsulando los selectores y acciones posibles.

- **Funciones.py**  
  Funciones reutilizables para interactuar con la app (llenar campos, hacer clic, validar textos, subir archivos, etc).

- **Utils/**  
  Utilidades y helpers para los tests (generación de datos, manejo de fechas, etc).

- **Data/**  
  Carpeta dedicada a los datos de prueba. Aquí se almacenan archivos como `usuarios.py` que contienen listas de usuarios, credenciales y otros datos parametrizables para los tests. Permite centralizar y modificar los datos de prueba fácilmente, facilitando el enfoque DDT y la extensión de casos.

- **redux-athena-bank/**  
  Carpeta con el código fuente de la app Athena Bank (backend y frontend).

- **screenshots/**  
  Carpeta donde se guardan capturas de pantalla de los tests fallidos.

- **allure-results/**  
  Carpeta donde se guardan los resultados de los tests para los reportes de Allure.

---

## Archivos relevantes

- **package.json**  
  Scripts para levantar backend/frontend, correr tests, generar reportes, etc.

- **pytest.ini**  
  Configuración de Pytest: dónde buscar los tests, cómo generar los reportes, etc.

- **.env**  
  Variables de entorno para los tests (URLs, usuarios de prueba, etc).

- **requirements.txt**  
  Dependencias Python necesarias para ejecutar los tests.

- **conftest.py**  
  Configuración avanzada de Pytest y Playwright (fixtures, hooks, screenshots en fallos).

- **.github/workflows/**  
  Workflows de GitHub Actions para CI/CD: levantan la app, corren los tests y generan los reportes automáticamente.

  - **package-lock.json**  
  Archivo generado automáticamente por npm. Registra las versiones exactas de todas las dependencias instaladas, asegurando que el entorno sea idéntico para todos los desarrolladores y

---

## ¿Cómo explicarlo rápido si alguien pregunta?

"Es un proyecto para automatizar pruebas de la app Athena Bank. Usa Playwright y Pytest para simular el uso real, verifica que todo funcione y genera reportes visuales con Allure. Está preparado para ejecutarse localmente y en CI/CD, levantando el backend y frontend, corriendo los tests y mostrando los resultados."

---

**Este instructivo es solo para uso personal y no debe compartirse.**