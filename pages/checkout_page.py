"""
    Page Object para la página de checkout (Step One) en saucedemo.com.

    Responsabilidades:
    - Verificar que la página de checkout esté cargada
    - Completar información del cliente (nombre, apellido, código postal)
    - Continuar o cancelar el checkout
    - Leer mensajes de error si existen
    """


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



class CheckoutPage:
    # Localizadores de elementos en la página
    FIRST_NAME_INPUT = (By.ID, 'first-name')    # Campo de nombre
    LAST_NAME_INPUT = (By.ID, 'last-name')      # Campo de apellido
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')   # Campo de código postal
    CONTINUE_BUTTON = (By.ID, 'continue')         # Botón para continuar al resumen
    CANCEL_BUTTON = (By.ID, 'cancel')             # Botón para cancelar checkout
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message-container')   # Mensaje de error si falta info 

    def __init__(self, driver):
        # Inicializa el Page Object con el WebDriver y una espera explícita.
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_at_page(self):
        # Verifica si estamos en la página de checkout comprobando la URL.
        return '/checkout-step-one.html' in self.driver.current_url

    def fill_customer_info(self, first_name, last_name, postal_code):
       """
        Completa la información del cliente: nombre, apellido y código postal.

        Pasos:
        1. Espera a que cada campo sea clickeable o visible.
        2. Limpia el campo y escribe el valor correspondiente.
        3. Verifica que el valor haya quedado escrito correctamente.
        """
       
       # First Name
       first_name_input = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT))
       first_name_input.click()
       first_name_input.clear()
       first_name_input.send_keys(first_name)
       first_name_input.send_keys(Keys.TAB)

       # Espera hasta que el valor quede realmente escrito
       self.wait.until(lambda d: first_name_input.get_attribute("value") == first_name)

       # Last Name
       last_name_input = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT))
       last_name_input.click()
       last_name_input.clear()
       last_name_input.send_keys(last_name)
       if last_name_input.get_attribute("value") != last_name:
           last_name_input.clear()
           last_name_input.send_keys(last_name)

       # Postal Code
       postal_code_input = self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE_INPUT))
       postal_code_input.click()
       postal_code_input.clear()
       postal_code_input.send_keys(postal_code)
       if postal_code_input.get_attribute("value") != postal_code:
           postal_code_input.clear()
           postal_code_input.send_keys(postal_code)

       # Debug: verificar que los valores se hayan escrito correctamente
       print("First name escrito:", first_name_input.get_attribute("value"))
       print("Last name escrito:", last_name_input.get_attribute("value"))
       print("Postal code escrito:", postal_code_input.get_attribute("value"))


    def continue_to_overview(self):
        # Hace clic en el botón "Continue" para avanzar al resumen del checkout.Espera explícitamente a que el botón sea clickeable.
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()


    def cancel_checkout(self):
        #  Hace clic en el botón "Cancel" para volver al listado de productos.Espera explícitamente a que el botón sea clickeable.
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_BUTTON)).click()

    def get_error_message(self):
        #Devuelve el texto del mensaje de error si existe.Retorna cadena vacía si no se encuentra ningún mensaje.
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except Exception:
            return ""