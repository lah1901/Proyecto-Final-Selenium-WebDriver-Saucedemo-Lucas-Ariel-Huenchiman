# Función para leer casos de login desde un archivo CSV
# El CSV debe contener las columnas: username, password y expected.
# Devuelve una lista de tuplas listas para parametrizar tests:
#   (username, password, expected_boolean)

import csv

def get_login_csv(file_path="data/data_login.csv"):
    # Abrir el archivo CSV con codificación segura para evitar problemas con BOM
    with open(file_path, newline='', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)

        # Normalizar los encabezados removiendo espacios y pasando a minúsculas
        reader.fieldnames = [h.strip().lower() for h in reader.fieldnames]
        cases = []

        # Procesar cada fila del CSV y extraer los valores relevantes
        for row in reader:
            username = row.get("username")
            password = row.get("password")
            expected = row.get("expected")

             # Convertir el campo "expected" a booleano para usarlo directamente en los tests
            cases.append((username, password, expected == "True"))
            
        return cases

