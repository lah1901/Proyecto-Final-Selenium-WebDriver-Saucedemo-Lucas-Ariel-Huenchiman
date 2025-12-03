# Page Object para la página de inventario (listado de productos) de saucedemo.com.
# Responsabilidades:
# - Verificar que la página esté cargada
# - Agregar productos al carrito por índice
# - Navegar al carrito
# - Cerrar sesión desde el menú lateral

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    # Fragmento de URL para confirmar que estamos en la página de inventario
    URL_CURRENT = "/inventory.html"

    # Localizadores de elementos de la página
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")             # Botón del menú (arriba a la izquierda)
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")               # Enlace de logout dentro del menú lateral
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(), 'Add to cart')]")  # Todos los botones "Add to cart"
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")          # Icono/enlace del carrito (arriba a la derecha)
    CART_TITLE = (By.CLASS_NAME, "title")                       # Título de la página 

    def __init__(self, driver):
        # Inicializa el Page Object con el WebDriver y una espera explícita.
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_at_page(self):
        # Verifica si estamos en la página de inventario comprobando la URL.
        return self.URL_CURRENT in self.driver.current_url

    def add_product_to_cart(self, product_index=0):
        # Hace clic en un botón "Add to cart" por índice (por defecto: primer producto)
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if buttons and 0 <= product_index < len(buttons):
            buttons[product_index].click()

    def go_to_cart(self):
        """
        Navega al carrito de compras haciendo clic en el icono correspondiente.

        Pasos:
        1. Espera explícitamente a que el icono del carrito sea clickeable.
        2. Hace clic mediante JavaScript por si el clic normal no funciona.
        3. Espera hasta que la URL contenga 'cart.html'.
        """
        cart_icon = self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        # Clic forzado con JS por si el elemento no es clickeable normalmente
        self.driver.execute_script("arguments[0].click();", cart_icon)

        print("URL después del clic (JS):", self.driver.current_url)
        self.wait.until(EC.url_contains("cart.html"))


    def logout(self):
        """
        Cierra la sesión del usuario.

        Pasos:
        1. Abre el menú lateral.
        2. Hace clic en el enlace de logout dentro del menú.
        Ambos elementos se esperan explícitamente para garantizar que sean clickeables.
        """
        self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK)).click()


