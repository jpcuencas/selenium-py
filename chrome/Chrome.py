#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Automatically download and use the correct ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Print ChromeDriver version
print(driver.capabilities['chrome']['chromedriverVersion'])

try:
    # 1 | open | /dgc/login |
    driver.get("http://development.dgc.agricultura.apps-crc.testing/dgc/login")
    # 2 | setWindowSize | 970x670 |
    driver.set_window_size(970, 670)

    driver.find_element(By.ID, "nif").click()
    driver.find_element(By.ID, "nif").send_keys("11111111H")
    driver.find_element(By.CSS_SELECTOR, ".mn-select-icon-container").click()
    driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted:nth-child(9)").click()
    driver.find_element(By.CSS_SELECTOR, ".button__container > .w-100").click()
    driver.find_element(By.LINK_TEXT, "Gestió econòmica").click()
    driver.find_element(By.LINK_TEXT, "Pagaments").click()
    driver.find_element(By.CSS_SELECTOR, ".button__primary > span").click()

    print("Prueba completada con éxito")

finally:
    driver.quit()