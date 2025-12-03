# Test de login parametrizado utilizando datos desde un CSV.
# Cada fila del CSV contiene: username, password, expected_success
# El test valida tanto logins exitosos como fallidos.

import pytest
from pages.login_page import LoginPage
from utils.example_csv import get_login_csv
from utils.helpers import get_logger  

# Carga dinámica de casos de prueba desde el CSV
login_cases = get_login_csv()

# Indica a Pytest que el test se va a ejecutar una vez por cada fila que haya en login_cases.
@pytest.mark.parametrize("username,password,expected", login_cases)  
def test_login(driver, username, password, expected):
     # Inicializa el logger para registrar los pasos del test
    logger = get_logger()  

    # Instancia la página de login para interactuar con sus elementos
    login_page = LoginPage(driver)
    logger.info(f"Iniciando test de login con usuario: '{username}'")

    # Abrir página de login
    login_page.open()
    logger.info("Página de login abierta")

    # Intentar autenticación
    login_page.login(username, password)
    logger.info("Credenciales ingresadas y botón de login presionado")

    # Validación según caso esperado
    if expected:
        # Caso esperado: login exitoso
        assert "inventory.html" in driver.current_url
        logger.info("Login exitoso, redirigido a inventory.html")
    else:
        # Caso esperado: login fallido
        error_msg = login_page.get_error_message()
        assert error_msg != ""
        logger.warning(f"Login fallido como se esperaba. Mensaje de error: '{error_msg}'")

