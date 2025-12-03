# Page Object para la página de login de saucedemo.com
# Responsabilidades:
# - Abrir la página de login
# - Ingresar credenciales y hacer login
# - Leer mensajes de error si las credenciales son incorrectas

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
     # URL de la página de login
    URL = "https://www.saucedemo.com/"

    # Localizadores de elementos de la página
    USERNAME_INPUT = (By.ID, "user-name")        # Campo de nombre de usuario
    PASSWORD_INPUT = (By.ID, "password")          # Campo de contraseña
    LOGIN_BUTTON = (By.ID, "login-button")        # Botón de login
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")   # Contenedor de mensajes de error

    def __init__(self, driver):
        # Inicializa el Page Object con el WebDriver y una espera explícita.
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def open(self):
        # Abre la página de login en el navegador.
        self.driver.get(self.URL)

    
    def login(self, username, password):
        """
        Completa los campos de usuario y contraseña y hace clic en login.

        Parámetros:
        - username: nombre de usuario
        - password: contraseña

        Pasos:
        1. Espera a que los campos de usuario y contraseña sean visibles.
        2. Limpia los campos y escribe los valores proporcionados.
        3. Verifica que los valores se hayan escrito correctamente.
        4. Espera a que el botón de login sea clickeable y hace clic en él.
        """

        # Completa el campo de username
        username_input = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        username_input.clear()
        username_input.send_keys(username)
        self.wait.until(lambda d: username_input.get_attribute("value") == username)

        # Completa el campo de password
        password_input = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)
        self.wait.until(lambda d: password_input.get_attribute("value") == password)

        # Debug: imprimir los valores escritos
        print("Username escrito:", username_input.get_attribute("value"))
        print("Password escrito:", password_input.get_attribute("value"))

        # Hacer clic en el botón de login
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()


    def get_error_message(self): #  Devuelve el texto del mensaje de error si existe.
                                 # Retorna:- Texto del mensaje de error si está presente
                                          # - Cadena vacía si no hay mensaje de error
        try:
            error_el = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error_el.text
        except:
            return ""
