from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome webdriver
driver_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

# Navigate to the webpage
driver.get("https://apps.indraweb.net/registrohorario/#/dashboard/registro")

# Wait for the button to be clickable (you can adjust the timeout as needed)
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/dashboard/div/dashboard-registro/div/div[1]/div[2]/div[2]/div[1]/button"))
)

# Click the button
button.click()
