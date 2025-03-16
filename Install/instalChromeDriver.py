from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Descargar la última versión de ChromeDriver compatible
chrome_driver_path = ChromeDriverManager().install()

# Verifica si el archivo descargado es válido
print(f"ChromeDriver descargado en: {chrome_driver_path}")

# Usa el path manualmente
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("http://www.google.com")
driver.quit()
