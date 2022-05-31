# selenium 3
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.core.utils import ChromeType

#driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
driver.get("http://www.goodstartbook.com")
driver.quit()
