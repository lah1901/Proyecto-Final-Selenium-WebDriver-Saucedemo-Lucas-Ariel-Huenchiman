# Page Object para la página de resumen del checkout en saucedemo.com.
# Responsabilidades:
# - Verificar que la página de resumen esté cargada
# - Finalizar el checkout haciendo clic en el botón "Finish"


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage:
    # Page Object para la página de resumen del checkout (Step Two).

     # Fragmento de URL para confirmar la página de resumen del checkout
    URL_CURRENT = "/checkout-step-two.html"

     # Localizadores de elementos en la página
    FINISH_BUTTON = (By.ID, "finish")  # Botón para finalizar el checkout

    def __init__(self, driver):
        # Inicializa el Page Object con el WebDriver y una espera explícita.
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_at_page(self):
        # Verifica si estamos en la página de resumen del checkout comprobando la URL.
        return self.URL_CURRENT in self.driver.current_url

    def finish_checkout(self):
        # Hace clic en el botón "Finish" para completar el checkout.Espera explícitamente a que el botón sea clickeable antes de interactuar.
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

