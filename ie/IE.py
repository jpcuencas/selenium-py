# selenium 3
#from selenium import webdriver
#from webdriver_manager.microsoft import IEDriverManager

#driver = webdriver.Ie(IEDriverManager().install())

# selenium 4
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import IEDriverManager

driver = webdriver.Ie(service=Service(IEDriverManager().install()))

driver.get("http://www.goodstartbook.com")
driver.quit()
