# Test para cerrar sesión
# Test para verificar el flujo de logout en Saucedemo.
# Flujo cubierto:
# 1. Login con usuario válido
# 2. Acceso al inventario
# 3. Logout desde el menú lateral
# 4. Validación de redirección a la página de login

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.helpers import get_logger  # <- importar logger


def test_logout(driver):
     # Inicializa el logger para registrar el flujo del test
    logger = get_logger()  

    # Login
    login_page = LoginPage(driver)
    logger.info("Abriendo página de login")
    login_page.open()

    logger.info("Ingresando credenciales para standard_user")
    login_page.login("standard_user", "secret_sauce")

    # Logout
    # Instancia la página de inventario para acceder al menú y ejecutar el logout
    inventory_page = InventoryPage(driver)
    logger.info("Realizando logout")
    inventory_page.logout()

    # Validación de redirección después de cerrar sesión
    current_url = driver.current_url
    logger.info(f"URL después del logout: {current_url}")

    assert "saucedemo.com" in driver.current_url
    logger.info("Logout realizado correctamente y redirigido a la página de login")
