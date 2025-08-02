from playwright.sync_api import Page
import os
from dotenv import load_dotenv
from Funciones import Funcion

load_dotenv()

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.funcion = Funcion(page)
        
        # URLs
        base_url = os.getenv('BASE_URL', 'http://localhost:3000')
        self.url_dashboard = f"{base_url}/dashboard"
        
        # Selectores para crear cuenta
        self.tarjeta_agregar_cuenta = '[data-testid="tarjeta-agregar-cuenta"]'
        self.boton_crear_cuenta = '[data-testid="boton-crear-cuenta"]'
        self.mensaje_exito = 'text="¡Cuenta creada exitosamente!"'
        self.numero_cuenta = '[data-testid="texto-numero-cuenta"]'
        
        # Modal/Formulario crear
        self.combo_tipo_cuenta = 'role=combobox[name="Tipo de cuenta *"]'
        self.opcion_debito = 'role=option[name="Débito"]'
        self.input_monto = 'role=spinbutton[name="Monto inicial *"]'
        
        # Selectores para eliminar cuenta 
        self.boton_eliminar_cuenta = '[data-testid="boton-eliminar-cuenta"]'
        self.titulo_eliminar = 'role=heading[name="Eliminar cuenta"]'
        self.combo_seleccionar_cuenta = 'role=combobox[name="Selecciona cuenta"]'
        self.boton_eliminar_confirmar = 'role=button[name="Eliminar"]'
        self.mensaje_eliminacion_exitosa = 'text="Cuenta eliminada exitosamente"'
        
        # Selectores para validaciones de error
        self.mensaje_error_tipo_cuenta = '[data-testid="texto-error-tipo-cuenta"]'

    # Métodos para crear cuenta (mantener como están)
    def abrir_modal_crear_cuenta(self):
        """Hacer clic en el botón de agregar cuenta"""
        self.funcion.click_boton(self.tarjeta_agregar_cuenta)

    def verificar_modal_abierto(self):
        """Verificar que se abre el modal de crear cuenta"""
        self.funcion.validar_elemento_visible(self.combo_tipo_cuenta)
        self.funcion.validar_elemento_visible(self.input_monto)
        self.funcion.validar_elemento_visible(self.boton_crear_cuenta)
    
    def seleccionar_tipo_cuenta(self, tipo: str = "Débito"):
        """Seleccionar tipo de cuenta """
        self.funcion.seleccionar_combo_moderno(self.combo_tipo_cuenta, tipo)
    
    
    def ingresar_monto_inicial(self, monto: str):
        """Ingresar monto inicial en el campo"""
        self.funcion.click_boton(self.input_monto)
        self.funcion.llenar_texto(self.input_monto, monto)

    def crear_cuenta(self):
        """Hacer clic en el botón crear cuenta"""
        self.funcion.click_boton(self.boton_crear_cuenta)

    def verificar_cuenta_creada(self):
        """Verificar que la cuenta se creó exitosamente"""
        self.funcion.validar_texto(self.mensaje_exito, "¡Cuenta creada exitosamente!")
        #self.funcion.validar_elemento_visible('[data-testid="texto-numero-cuenta"]')

    def crear_cuenta_completa(self, tipo_cuenta: str = "Débito", monto: str = "200"):
        """Proceso completo de creación de cuenta"""
        self.abrir_modal_crear_cuenta()
        self.verificar_modal_abierto()
        self.seleccionar_tipo_cuenta(tipo_cuenta)
        self.ingresar_monto_inicial(monto)
        self.crear_cuenta()
        self.verificar_cuenta_creada()

    # Métodos para eliminar cuenta (mantener como están)
    def abrir_modal_eliminar_cuenta(self):
        """Hacer clic en el botón de eliminar cuenta"""
        self.funcion.click_boton(self.boton_eliminar_cuenta)

    def verificar_modal_eliminar_abierto(self):
        """Verificar que se abre el modal de eliminar cuenta"""
        self.funcion.validar_elemento_visible(self.titulo_eliminar)
        self.funcion.validar_elemento_visible(self.combo_seleccionar_cuenta)

    def seleccionar_cuenta_para_eliminar(self, nombre_cuenta: str):
        """Seleccionar la primera cuenta disponible para eliminar"""
        self.funcion.seleccionar_primera_opcion_combo(self.combo_seleccionar_cuenta)

    def confirmar_eliminacion(self):
        """Hacer clic en el botón eliminar para confirmar"""
        self.funcion.click_boton(self.boton_eliminar_confirmar)

    def verificar_cuenta_eliminada(self):
        """Verificar que la cuenta se eliminó exitosamente"""
        self.funcion.validar_texto(self.mensaje_eliminacion_exitosa, "Cuenta eliminada exitosamente")

    # Métodos para validación de errores
    def verificar_error_tipo_cuenta_requerido(self):
        """Verificar mensaje de error cuando tipo de cuenta está vacío"""
        self.funcion.validar_texto_contiene(self.mensaje_error_tipo_cuenta, "Tipo de cuenta requerido")