# Test de flujo completo de checkout en Saucedemo
# Este test cubre el escenario end-to-end:
# 1. Login
# 2. Agregar producto al carrito
# 3. Iniciar checkout
# 4. Completar información del cliente
# 5. Revisar overview
# 6. Finalizar compra
# 7. Validar página de confirmación

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import get_logger  



def test_checkout_flow(driver):
    logger = get_logger()  # <- inicializar logger

    # Login
    login_page = LoginPage(driver)
    logger.info("Abriendo página de login")
    login_page.open()

    logger.info("Ingresando credenciales para standard_user")
    login_page.login("standard_user", "secret_sauce")

    # Agregar producto al carrito
    inventory_page = InventoryPage(driver)
    logger.info("Agregando el primer producto al carrito")
    inventory_page.add_product_to_cart(0)

    logger.info("Navegando al carrito")
    inventory_page.go_to_cart()
 
    # Ir a checkout
    cart_page = CartPage(driver)
    logger.info("Navegando a la página de checkout")
    cart_page.go_to_checkout()

    # Checkout step one:rellenar info del cliente
    checkout_page = CheckoutPage(driver)
    logger.info("Rellenando información del cliente")
    checkout_page.fill_customer_info("John", "Doe", "12345")
    checkout_page.continue_to_overview() # Va a step two
    logger.info("Continuando a la página de overview (step two)")

    # Checkout Step Two: overview 
    checkout_overview_page = CheckoutOverviewPage(driver)
    WebDriverWait(driver, 10).until(
        EC.url_contains("/checkout-step-two.html")
    )
    logger.info("Página de overview cargada correctamente")


    logger.info("Finalizando checkout")
    checkout_overview_page.finish_checkout()  

    # Checkout Complete 
    checkout_complete_page = CheckoutCompletePage(driver)
    WebDriverWait(driver, 10).until(
        EC.url_contains("/checkout-complete.html")
    )
    logger.info(f"URL final: {driver.current_url}")

    # Validaciones finales
    assert checkout_complete_page.is_at_page()
    logger.info("Estamos en la página de checkout completo")

    success_msg = checkout_complete_page.get_success_message()
    assert success_msg != ""
    logger.info(f"Mensaje de éxito mostrado: '{success_msg}'")

    assert checkout_complete_page.is_success_image_displayed()
    logger.info("Imagen de éxito mostrada correctamente. Checkout finalizado con éxito")

    

    

    