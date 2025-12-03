import logging
import os



# Función auxiliar para validar URLs
# Verifica que la URL actual del navegador contenga un texto específico.
# Se usa como pequeña utilidad para validar redirecciones dentro de los tests.
def assert_url_contains(driver, text):
    assert text in driver.current_url



   
# Función que crea y configura un logger centralizado para todos los tests.
# - Guarda los logs en logs/execution.log
# - Evita duplicar handlers al ejecutarse múltiples tests en Pytest
def get_logger(name="test_logger"):
    # Asegurar que la carpeta de logs exista
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Evitar agregar handlers duplicados si el logger ya existe
    if not logger.handlers:
        file_handler = logging.FileHandler(os.path.join(log_dir, "execution.log"))
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger