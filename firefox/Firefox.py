import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start WebDriver
driver = webdriver.Firefox()

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
    # Define explicit wait
    wait = WebDriverWait(driver, 20)

    # Ensure spinner disappears before proceeding
    wait.until(EC.invisibility_of_element((By.CLASS_NAME, "spinner-overlay")))

    # Click "Gestió econòmica"
    gestio_economica_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Gestió econòmica")))
    gestio_economica_link.click()

    # Click "Pagaments"
    pagaments_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Pagaments")))
    pagaments_link.click()

    # Ensure spinner disappears before clicking the next button
    wait.until(EC.invisibility_of_element((By.CLASS_NAME, "spinner-overlay")))

    # Find the button
    button_search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button__primary > span")))

    # Scroll to the button to ensure it's visible
    driver.execute_script("arguments[0].scrollIntoView(true);", button_search)
    time.sleep(1)  # Small delay to let animation settle

    # Wait for button to be clickable
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button__primary > span")))

    try:
        button_search.click()
    except Exception as e:
        print("Click failed, trying JavaScript click instead...")
        driver.execute_script("arguments[0].click();", button_search)  # Fallback using JavaScript

    print("Prueba completada con éxito")

finally:
    # Keep the browser open for 1 minute before quitting
    print("Waiting for 1 minute before closing...")
    time.sleep(60)
    driver.quit()
