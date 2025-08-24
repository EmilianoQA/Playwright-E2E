# Datos para tests de registro con DDT
usuarios_registro = [
    {"nombre": "Juan", "apellido": "Pérez", "email": "juan@test.com", "password": "password123", "esperado": "exitoso"},
    {"nombre": "", "apellido": "Test", "email": "test1@test.com", "password": "password123", "esperado": "error_nombre"},
    {"nombre": "Ana", "apellido": "", "email": "ana@test.com", "password": "password123", "esperado": "error_apellido"},
    {"nombre": "Carlos", "apellido": "López", "email": "", "password": "password123", "esperado": "error_email"},
    {"nombre": "María", "apellido": "García", "email": "maria@test.com", "password": "", "esperado": "error_password"},
]
