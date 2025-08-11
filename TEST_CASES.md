# REGISTRO DE CASOS DE PRUEBA

## 📊 RESUMEN
- **Total casos definidos**: 12
- **Próximo número disponible**: TC153

---

## 🔐 AUTENTICACIÓN (TC001-TC050)
| Código | Descripción | Archivo | Estado |
|--------|-------------|---------|--------|
| TC001 | Login exitoso con credenciales válidas | test_login.py | ✅ Implementado |
| TC002 | Login con credenciales incorrectas | test_login.py | ✅ Implementado |
| TC003 | Login con campos vacíos - no redirige | test_login.py | ✅ Implementado |
| TC004 | Login validación nativa HTML5 | test_login.py | ✅ Implementado |
| TC005-TC050 | [DISPONIBLES] | - | 🔲 Pendiente |

---

## 📝 REGISTRO DE USUARIOS (TC051-TC100)
| Código | Descripción | Archivo | Estado |
|--------|-------------|---------|--------|
| TC051 | Registro exitoso usando formulario frontend | test_registro.py | ✅ Implementado |
| TC052 | Registro fallido con email existente | test_registro.py | ✅ Implementado |
| TC053 | Registro híbrido API + verificación E2E | test_registro.py | ✅ Implementado |
| TC054-TC100 | [DISPONIBLES] | - | 🔲 Pendiente |

---

## 🏦 GESTIÓN DE CUENTAS (TC101-TC150)
| Código | Descripción | Archivo | Estado |
|--------|-------------|---------|--------|
| TC101 | Crear cuenta débito exitoso | test_cuentas.py | ✅ Implementado |
| TC102 | Eliminar cuenta existente | test_cuentas.py | ✅ Implementado |
| TC103 | Crear cuenta con campos vacíos - validación | test_cuentas.py | ✅ Implementado |
| TC104-TC150 | [DISPONIBLES] | - | 🔲 Pendiente |

---

## 🧭 NAVEGACIÓN (TC151-TC200)
| Código | Descripción | Archivo | Estado |
|--------|-------------|---------|--------|
| TC151 | Enlace registro desde login | test_navegacion.py | ✅ Implementado |
| TC152 | Logout y protección de rutas | test_navegacion.py | ✅ Implementado |
| TC153-TC200 | [DISPONIBLES] | - | 🔲 Pendiente |

---

## 📋 INSTRUCCIONES DE USO

### Para agregar un nuevo caso:
1. Buscar el próximo número disponible en la tabla de resumen
2. Actualizar la tabla correspondiente
3. Actualizar el "Total casos definidos" y "Próximo número disponible"
4. Implementar el test con el código asignado

### Rangos por módulo:
- **Autenticación**: TC001-TC050
- **Registro**: TC051-TC100  
- **Cuentas**: TC101-TC150
- **Navegación**: TC151-TC200
- **API**: TC201-TC250
- **Futuros módulos**: TC251+

---

## 🗓️ HISTORIAL
- **2025-01-07**: Creación inicial con TC001-TC004 (Login)
