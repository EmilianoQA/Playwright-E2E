"""
TransferenciasPage - Página para manejar envío de dinero entre usuarios
"""

from playwright.sync_api import Page
import os
from dotenv import load_dotenv
from Utils.Funciones import Funcion

load_dotenv()

class TransferenciasPage:
    def __init__(self, page: Page):
        self.page = page
        self.funcion = Funcion(page)
        
        # URLs
        base_url = os.getenv('BASE_URL', 'http://localhost:3000')
        self.url_dashboard = f"{base_url}/dashboard"
        
        # Selectores para abrir modal de transferencia
        self.boton_enviar_dashboard = '[data-testid="boton-enviar"]'
        
        # Selectores del modal "Enviar transferencia"
        self.titulo_modal = 'text="Enviar transferencia"'
        self.email_destinatario = 'role=textbox[name="Email del destinatario *"]'
        self.cuenta_origen = 'role=combobox[name="Cuenta origen *"]'
        self.monto_enviar = 'role=spinbutton[name="Monto a enviar *"]'
        self.boton_enviar_modal = 'role=button[name="Enviar"]'
        self.boton_cancelar = 'text="CANCELAR"'
        
        # Mensajes de respuesta
        self.mensaje_exito = ':text("Transferencia enviada a")'  # Mensaje dinámico
        self.mensaje_error = 'text="Error en la transferencia"'  # Ajustar según app

    def ir_a_dashboard(self):
        """Navegar al dashboard"""
        self.funcion.navegar_a_url(self.url_dashboard)

    def abrir_modal_transferencia(self):
        """Abrir modal de enviar transferencia"""
        self.funcion.click_boton(self.boton_enviar_dashboard)

    def verificar_modal_abierto(self):
        """Verificar que el modal de transferencia está abierto"""
        self.funcion.validar_elemento_visible(self.titulo_modal)
        self.funcion.validar_elemento_visible(self.email_destinatario)
        self.funcion.validar_elemento_visible(self.cuenta_origen)
        self.funcion.validar_elemento_visible(self.monto_enviar)

    def llenar_email_destinatario(self, email: str):
        """Llenar email del destinatario"""
        self.funcion.llenar_texto(self.email_destinatario, email)

    def seleccionar_cuenta_origen(self):
        """Seleccionar la primera cuenta disponible"""
        self.funcion.seleccionar_primera_opcion_combo(self.cuenta_origen)

    def llenar_monto(self, monto: str):
        """Llenar monto a enviar"""
        self.funcion.llenar_texto(self.monto_enviar, monto)

    def enviar_transferencia(self):
        """Hacer clic en botón ENVIAR"""
        self.funcion.click_boton(self.boton_enviar_modal)

    def verificar_transferencia_exitosa(self):
        """Verificar mensaje de transferencia exitosa"""
        self.funcion.validar_elemento_visible(self.mensaje_exito)

    def verificar_transferencia_fallida(self):
        """Verificar mensaje de error en transferencia"""
        self.funcion.validar_elemento_visible(self.mensaje_error)

    def cancelar_transferencia(self):
        """Hacer clic en botón CANCELAR"""
        self.funcion.click_boton(self.boton_cancelar)

    def hacer_transferencia_completa(self, email_receptor: str, monto: str):
        """
        Proceso completo de transferencia
        
        Args:
            email_receptor: Email del usuario receptor
            monto: Cantidad a transferir
        """
        self.abrir_modal_transferencia()
        self.verificar_modal_abierto()
        self.llenar_email_destinatario(email_receptor)
        self.seleccionar_cuenta_origen()
        self.llenar_monto(monto)
        self.enviar_transferencia()
        self.verificar_transferencia_exitosa()  # Ahora con mensaje correcto
