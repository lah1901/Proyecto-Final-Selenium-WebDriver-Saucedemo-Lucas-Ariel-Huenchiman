# Page Object para la página del carrito de compras en saucedemo.com.
# Responsabilidades:
# - Verificar que la página esté cargada
# - Contar y remover ítems del carrito
# - Continuar comprando o ir al checkout

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    # Fragmento de URL para confirmar la página del carrito
    URL_CURRENT = "/cart.html"

    # Localizadores de elementos de la página
    CART_ITEMS = (By.CLASS_NAME, "cart_item")                 # Filas de ítems en el carrito
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Remove')]")  # Botones "Remove" por ítem
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")   # Botón para volver al inventario
    CHECKOUT_BUTTON = (By.ID, "checkout")                     # Botón para iniciar el checkout

    def __init__(self, driver):
        # Inicializa el Page Object con el WebDriver y una espera explícita.
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_at_page(self):
        # Verifica si estamos en la página del carrito comprobando la URL.
        return self.URL_CURRENT in self.driver.current_url

    def get_item_count(self):
        # Devuelve la cantidad de ítems actualmente en el carrito
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_item_by_index(self, item_index=0):
        # Remueve un ítem del carrito según su índice (si existe). No lanza error si el índice es inválido.
        remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        if remove_buttons and 0 <= item_index < len(remove_buttons):
            remove_buttons[item_index].click()

    def continue_shopping(self):
        # Vuelve a la página de inventario haciendo clic en el botón correspondiente.
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)).click()

    def go_to_checkout(self):
        """
        # Inicia el proceso de checkoout

        Pasos:
        1. Espera que el botón de checkout sea clickeable.
        2. Hace scroll hacia el botón en caso de que no esté visible.
        3. Intenta un clic normal y, si falla, hace un clic forzado vía JavaScript.
        4. Espera a que cargue la página de Checkout Step One. 
        """
        
        # Imprime en consola la URL actual del navegador justo antes de hacer clic en el botón de checkout.
        print("DEBUG -> URL ANTES del clic:", self.driver.current_url)

        # Asegura que el botón de checkout esté listo para interactuar
        checkout_btn = self.wait.until(
        EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )

        # Asegura que el botón esté visible. Scroll por si el botón está abajo
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkout_btn)

        # Intento de clic normal
        try:
          checkout_btn.click()
        except:
          pass

        print("DEBUG -> URL después del clic NORMAL:", self.driver.current_url)

        # Clic forzado (por si el normal no funciona)
        self.driver.execute_script("arguments[0].click();", checkout_btn)

        print("DEBUG -> URL después del clic FORZADO:", self.driver.current_url)

        # Espera a que cargue la página de Step One
        self.wait.until(EC.url_contains("checkout-step-one.html"))
