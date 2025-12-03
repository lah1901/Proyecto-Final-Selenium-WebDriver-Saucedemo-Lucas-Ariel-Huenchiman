# Proyecto Automatización Web para SauceDemo con Pytest + Selenium

Este proyecto contiene una suite completa de pruebas automatizadas end-to-end para el sitio de demostración https://www.saucedemo.com
, utilizando el patrón Page Object Model (POM) y Pytest como framework principal.
Incluye manejo de datos externos, reportes HTML, captura de screenshots y generación de datos dinámicos.



# Propósito
El objetivo de este proyecto es:

- Validar el flujo completo de compra de productos en SauceDemo.

- Aplicar buenas prácticas de automatización con Page Object Model.

- Permitir pruebas reutilizables, escalables y fáciles de mantener.

- Facilitar reporting, logging y screenshots para depuración.

- Servir como plantilla base para proyectos de automatización web.



# Tecnologías usadas
- Python 3.11.5

- Pytest – framework de testing 8.4.2

- Selenium WebDriver – automatización del navegador 4.36.0

- Pytest-HTML – reportes en HTML 4.1.1

- Faker – generación de datos dinámicos 38.2.0

- CSV / JSON – manejo de datos externos

- Page Object Model (POM) – diseño modular de páginas



# Estructura del Proyecto

📦 proyecto-saucedemo/
│
├── data/
│   ├── __init__.py
│   ├── data_login.csv
│   ├── data_login.json
│   └── data_login.py           # Lectura y manejo de datos externos
│
├── pages/                       # Page Object Model (POM)
│   ├── __init__.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   ├── checkout_complete_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── reports/
│   └── reporte.html             # Reportes HTML generados por Pytest
│
├── screenshots/                 # Screenshots automáticos en fallos
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Fixtures globales (driver, setup/teardown)
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_add_to_cart.py
│   ├── test_checkout_flow.py
│   └── test_negative_login.py
│
├── utils/
│   ├── __init__.py
│   ├── example_csv.py
│   ├── faker.py                 # Generación de datos con Faker
│   └── helpers.py               # Funciones auxiliares
│
└── README.md




# Instalación de dependencias

Si tienes requirements.txt:

pip install -r requirements.txt

Si no lo tienes, instala lo básico:

pip install selenium pytest pytest-html faker




# Ejecución de pruebas
Para ejecutar los tests, seguí estos pasos desde la carpeta raíz del proyecto:
1. Abrí una terminal en la carpeta del proyecto.
2. Ejecutá el siguiente comando para correr todos los tests y ver los resultados en detalle:
```bash
pytest -v
```

Ejecutar un archivo de prueba particular:
```bash
pytest tests/test_login.py
```

# Screenshots Automáticos
Los screenshots son generados automáticamente cuando una prueba falla.
Se guardan en:
/screenshots/

Esto ayuda a depurar fallos visuales del flujo.


# ¿Cómo interpretar los reportes generados?
El archivo principal generado es:
/reports/reporte.html

Dentro del reporte encontrarás:

- Lista de pruebas ejecutadas

- Estado (passed / failed / skipped)

- Logs de cada prueba

- Screenshots embebidos en caso de fallos

- Duración de ejecución

- Información del entorno (versión de Python, Pytest, etc.)

El archivo es totalmente portable y puede abrirse en cualquier navegador.

