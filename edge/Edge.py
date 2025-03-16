from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

# Configurar el servicio de Edge
service = Service(EdgeChromiumDriverManager().install())

# Iniciar el driver
driver = webdriver.Edge(service=service)

# Abrir la página web
driver.get("http://www.google.com")

# Cerrar el navegador
driver.quit()