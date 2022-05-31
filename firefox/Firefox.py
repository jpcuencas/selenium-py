# selenium 3
#from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("http://www.goodstartbook.com")
driver.quit()
