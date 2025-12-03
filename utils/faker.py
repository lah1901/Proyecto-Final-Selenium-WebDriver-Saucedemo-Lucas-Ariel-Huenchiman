# Utilidad para generar credenciales inválidas utilizando Faker.
# Se usa para tests negativos de login (usuarios que no existen en el sistema).

from faker import Faker
fake = Faker()

def get_login_faker():
    # Devuelve un par (username, password) generados aleatoriamente
    return fake.user_name(), fake.password()

