# Fixture y hook de pytest para inicializar el navegador y capturar screenshots en fallos

import os
import pytest
from datetime import datetime
from selenium import webdriver


# FIXTURE DEL DRIVER
@pytest.fixture
def driver(): # Fixture de pytest para inicializar un navegador Chrome antes de cada test y cerrarlo al finalizar.
              # Maximiza la ventana al inicio. Cierra/quita el navegador automáticamente después del test.
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# HOOK: CAPTURA AUTOMÁTICA DE SCREENSHOTS EN FAIL
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest para capturar automáticamente un screenshot si un test falla.

    - La imagen se guarda en la carpeta 'screenshots'.
    - El nombre del archivo incluye:
        testname_param_timestamp.png
      Ejemplo:
        test_login_standard_user_2025-02-15_20-33-10.png

    Pasos:
    1. Espera a que el test termine y obtiene el reporte.
    2. Solo actúa si la fase es 'call' y el test falló.
    3. Recupera el fixture 'driver' del test.
    4. Crea la carpeta 'screenshots' si no existe.
    5. Genera el nombre del archivo usando test name, parámetro (si existe) y timestamp.
    6. Captura el screenshot y lo guarda en la carpeta indicada.
    """
    outcome = yield
    report = outcome.get_result()

    # Solo si el fallo ocurre durante la ejecución del test (fase 'call')
    if report.when == "call" and report.failed:

        # Obtener driver del test
        driver = item.funcargs.get("driver")
        if driver:

            # Carpeta donde se guardarán los screenshots
            screenshots_dir = "screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            # Nombre del test
            test_name = item.name

            # Intentar obtener parámetros del test (ej: username)
            username = "no_param"
            try:
                username = item.callspec.params.get("username", "no_param")
            except Exception:
                pass

            # Timestamp actual para evitar sobreescritura
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Nombre final del archivo
            file_name = f"{test_name}_{username}_{timestamp}.png"

            file_path = os.path.join(screenshots_dir, file_name)

            # Capturar y guardar screenshot
            driver.save_screenshot(file_path)

            print(f"\n Screenshot guardado: {file_path}\n")
