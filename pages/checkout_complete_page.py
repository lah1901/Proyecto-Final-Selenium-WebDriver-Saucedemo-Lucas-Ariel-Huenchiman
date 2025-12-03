# Page Object para la página final de confirmación del checkout en saucedemo.com.
# Responsabilidades:
# - Verificar que la página esté cargada
# - Leer el mensaje de éxito y texto descriptivo
# - Volver al listado de productos
# - Validar visibilidad de la imagen de éxito (pony express)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage:
    # Fragmento de URL para confirmar la página de confirmación final
    URL_CURRENT = "/checkout-complete.html"

    # Localizadores de elementos en la página.
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")   # Encabezado principal de éxito
    SUCCESS_TEXT = (By.CLASS_NAME, "complete-text")        # Texto descriptivo de confirmación
    BACK_HOME_BUTTON = (By.ID, "back-to-products")         # Botón para volver al inventario
    PONY_EXPRESS_IMAGE = (By.CLASS_NAME, "pony_express")   # Imagen de éxito

    def __init__(self, driver):
        # Inicializa el Page Object con el WebDriver y una espera explícita.
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_at_page(self):
        # Verifica si estamos en la página de confirmación final comprobando la URL.
        return self.URL_CURRENT in self.driver.current_url

    def get_success_message(self):
        # Devuelve el texto del encabezado de éxito si está presente.  Retorna cadena vacía si el elemento no se encuentra.
        try:
            return self.driver.find_element(*self.SUCCESS_MESSAGE).text
        except:
            return ""

    def get_success_text(self):
        # Devuelve el texto descriptivo de confirmación si está presente. Retorna cadena vacía si el elemento no se encuentra.
        try:
            return self.driver.find_element(*self.SUCCESS_TEXT).text
        except:
            return ""

    def back_to_home(self):
        # Clic en el botón para regresar al listado de productos
        self.wait.until(EC.element_to_be_clickable(self.BACK_HOME_BUTTON)).click()

    def is_success_image_displayed(self):
        # Verifica si la imagen de éxito está visible en la página. Retorna False si el elemento no se encuentra.
        try:
            return self.driver.find_element(*self.PONY_EXPRESS_IMAGE).is_displayed()
        except:
            return False


