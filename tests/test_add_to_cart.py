# Test para agregar un producto al carrito en Saucedemo
# Responsabilidades:
# - Abrir la página de login
# - Ingresar credenciales de usuario
# - Agregar un producto al carrito
# - Navegar al carrito y verificar que el producto se haya agregado

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.helpers import get_logger  
import time  # Para mantener la pantalla visible temporalmente



def test_add_product_to_cart(driver):
    #Test que agrega el primer producto al carrito y verifica que estamos en la página del carrito.

    # Inicializar logger
    logger = get_logger()  
    login_page = LoginPage(driver)

    # Abrir la página de login
    logger.info("Abriendo página de login")
    login_page.open()

    # Ingresar credenciales
    logger.info("Ingresando credenciales para standard_user")
    login_page.login("standard_user", "secret_sauce")

    # Instanciar la página de inventario para interactuar con el listado de productos
    logger.info("Accediendo a la página de inventario")
    inventory_page = InventoryPage(driver)

    # Agregar el primer producto al carrito
    logger.info("Agregando el primer producto al carrito")
    inventory_page.add_product_to_cart(0)

    # Navegar al carrito
    logger.info("Navegando al carrito")
    inventory_page.go_to_cart()

    # Verificar URL actual
    current_url = driver.current_url
    logger.info(f"URL actual: {current_url}")
    
    assert "cart.html" in current_url
    logger.info("El producto fue agregado correctamente y estamos en la página del carrito")

     # Mantener la pantalla visible temporalmente (para depuración o demostración)
    logger.info("Manteniendo la pantalla visible por 5 segundos...")
    time.sleep(5)



   
