from playwright.sync_api import Page, expect
from Pages.LoginPage import LoginPage
import os
from dotenv import load_dotenv
import random
import string
from Funciones import Funcion

URL_LOGIN = "http://localhost:3000/login"
URL_REGISTRO = "http://localhost:3000/signup"
URL_DASHBOARD = "http://localhost:3000/dashboard"

titulo_registro = '[data-testid="titulo-registro"]'
input_nombre = 'input[name="firstName"]'
input_apellido = 'input[name="lastName"]'
input_email = 'input[name="email"]'
input_password = 'input[name="password"]'
boton_registro = '[data-testid="boton-registrarse"]'
mensaje_exito = 'text="Registro exitoso!"'

load_dotenv()

def generar_email_aleatorio():
    letras = string.ascii_lowercase
    usuario = ''.join(random.choice(letras) for i in range(8))
    return f"{usuario}@test.com"

def generar_password_aleatorio():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for i in range(10))

def test_registro_exitoso(page: Page):
    funcion = Funcion(page)
    
    funcion.navegar_a_url(URL_REGISTRO)
    funcion.validar_url(URL_REGISTRO)
    funcion.validar_texto(titulo_registro, 'Registrarse')
    
    email_aleatorio = generar_email_aleatorio()
    password_aleatorio = generar_password_aleatorio()
    
    funcion.llenar_texto(input_nombre, "Test")
    funcion.llenar_texto(input_apellido, "Usuario")
    funcion.llenar_texto(input_email, email_aleatorio)
    funcion.llenar_texto(input_password, password_aleatorio)
    
    funcion.click_boton(boton_registro)
    funcion.validar_elemento_visible(mensaje_exito)
    funcion.validar_url(URL_LOGIN)  