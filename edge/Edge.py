# selenium 3
#from selenium import webdriver
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

#driver = webdriver.Edge(EdgeChromiumDriverManager().install())

# selenium 4
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get("http://www.goodstartbook.com")
driver.quit()
