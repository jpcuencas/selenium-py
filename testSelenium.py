from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait
# Set up Chrome webdriver
driver_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

# Navigate to the webpage
driver.get("https://login.indraweb.net/logon/LogonPoint/tmindex.html")

button = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='authentication-screen']/div[3]/div/div[2]/div[2]/div[3]/a")))
button.click()

WebDriverWait(driver, 100).until(
    EC.text_to_be_present_in_element((By.ID, 'login'), 'jpcuenca')
)

WebDriverWait(driver, 100).until(
    EC.text_to_be_present_in_element((By.ID, 'passwd'), '3893u8300K')
)

button = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='nsg-x1-logon-button']")))
button.click()

WebDriverWait(driver, 10000).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

#for i in range(100):
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#    time.sleep(5)