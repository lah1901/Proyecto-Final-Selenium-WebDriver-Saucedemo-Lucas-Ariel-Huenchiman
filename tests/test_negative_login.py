# Test de login inválido usando Faker
# Test para validar que el sistema rechaza credenciales generadas aleatoriamente con Faker.
# Flujo:
# 1. Generar un usuario y contraseña inválidos
# 2. Intentar iniciar sesión
# 3. Verificar que se muestre un mensaje de error

from pages.login_page import LoginPage
from utils.faker import get_login_faker
from utils.helpers import get_logger  

def test_invalid_login(driver):
    # Inicializar logger para registrar el proceso del test
    logger = get_logger()  

    # Generar credenciales aleatorias de prueba (siempre inválidas)
    username, password = get_login_faker()
    logger.info(f"Probando login inválido con usuario: '{username}' y contraseña: '{password}'")

    # Instanciar la página de login y abrirla
    login_page = LoginPage(driver)
    logger.info("Abriendo página de login")
    login_page.open()

    # Intentar iniciar sesión con credenciales inválidas
    logger.info("Intentando login con credenciales falsas")
    login_page.login(username, password)

    # Verificar que se muestre un mensaje de error
    error_msg = login_page.get_error_message()
    assert error_msg != ""
    logger.warning(f"Login fallido como se esperaba. Mensaje de error mostrado: '{error_msg}'")

